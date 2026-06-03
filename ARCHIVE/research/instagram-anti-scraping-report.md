# Instagram Anti-Scraping & Bot Detection: Comprehensive Technical Report

**Scope**: Instagram private mobile API + instagrapi library
**Last updated**: June 2026
**Confidence level**: HIGH — corroborated across instagrapi docs, HikerAPI field reports, Scrapfly research, GitHub issues, and developer forums

---

## 1. What Triggers Account Checkpoints / Challenges (`challenge_required`)

### Primary Trigger Signals

Instagram fires `challenge_required` (soft) or `checkpoint_required` (hard escalated form) when its server-side risk model detects a request that looks like an attacker rather than the legitimate account owner.

**The four signal layers that compound multiplicatively:**

| Layer | Signal | Notes |
|---|---|---|
| **Network** | New/different IP for this account | Most common trigger; especially datacenter IPs (AWS, GCP, DigitalOcean, Hetzner) |
| **Device fingerprint** | Fresh `Client()` with no persisted settings | New UUIDs (`device_id`, `phone_id`, `uuid`, `client_session_id`) generated on every script run |
| **Behavioral** | Request velocity spike, unusual patterns | 50 API calls/hour on an account that normally has 2/week = instant challenge |
| **Account history** | New account (<14 days old), recent password change, fresh 2FA enrollment | Account-level risk signals independent of fingerprint |

**Specific instagrapi trigger conditions:**
- Calling `cl.login()` without prior `load_settings()` → generates brand-new device fingerprint every run → Instagram sees "new device every time" → challenge fires
- Fresh password login from a datacenter ASN → instant challenge (no real user logs in from AWS)
- Rapid proxy rotation mid-session → geographic impossibility signal
- Retrying challenges in a tight loop → escalates to `checkpoint_required`
- Hitting `/auth_platform/` or UFAC web flows → manual human verification required (not automatable)

### The `challenge_required` vs `checkpoint_required` Distinction

- `ChallengeRequired`: soft anti-fraud signal. Instagram wants SMS/email code verification. Can be automated with `challenge_code_handler`.
- `CheckpointRequired`: hard escalation. Instagram has decided the account needs human intervention via web browser. Generally **not automatable** from instagrapi — page an operator.

**Detection point**: Both fire inside `pre_login_flow()` (before login returns), specifically in `instagrapi/mixins/challenge.py:87`.

### The UFAC Web Blocks (`/auth_platform/`)

The specific error: *"Manual verification required via Instagram UFAC web blocks checkpoint"* — this refers to Instagram's **User Fraud and Abuse Control (UFAC)** system. When triggered, Instagram redirects to a web-based verification challenge that:

1. Cannot be resolved via instagrapi's `challenge_resolve()` — no code to enter
2. Requires human interaction in a real browser
3. Often requires clicking verification images, not just entering a code
4. Is the escalation path when you've hit challenges repeatedly without resolving them

**Workaround**: If you hit UFAC blocks, the session is effectively burned for automation. You need to rotate to a fresh account/session that hasn't been UFAC-flagged.

---

## 2. Rate Limits for `/friendships/{user_id}/followers/` Endpoint

### Private Mobile API Limits (instagrapi)

Measured per-session (per warmed-up Instagram account) through Q1 2026:

| Action | Limit |
|---|---|
| `user/info/` (profile lookup) | ~150 req/hour per session |
| `user/followers/` (paginated) | ~30 paginated chunks/hour before degradation |
| `media/comments/` | ~80 req/hour |
| `feed/user/` | ~120 req/hour |

**Hard numbers are not officially published** — Meta's Instagram Graph API docs say 200 calls/user/hour for Business Use Case (BUC) tier, but this applies to the **official Graph API**, not the private mobile API used by instagrapi. The private API has different limits that vary by account warmth, IP quality, and endpoint.

### Practical Thresholds (DIY scraping, no managed API)

| Volume/day | Sessions needed | Notes |
|---|---|---|
| ~10K req/day | 5–10 warmed sessions | Baseline for stability |
| ~100K req/day | 50–80 sessions | Each session ~1200 req/day sustainable |
| ~1M req/day | 300+ sessions | Full operational infra |

**Rate limit response codes**:
- `HTTP 429` → IP-level rate limit, wait 5–60 min, rotate IP
- `PleaseWaitFewMinutes` (in `last_json`) → serious throttle, stop all write actions for that account, do not retry in loop
- `FeedbackRequired` → action blocked, freeze that action type for cooldown window

### Recommended request pacing per session

```
Safe sustained:  1-2 req/sec (with random variance ±200ms)
Soft limit trigger: ~3 req/sec sustained → starts throttling within minutes
```

Delays should be **randomized**, not fixed. `cl.delay_range = [1, 3]` in instagrapi adds 1-3s random delay between requests.

---

## 3. User-Agent Patterns: Accepted vs Rejected

### Valid User-Agents Instagram Accepts

Instagram validates the `User-Agent` header strictly. The mobile API (private) expects a specific format:

```
Instagram 312.0.0.34.111 Android (33/13; 420dpi; 1080x2210; samsung; SM-G991B; o1s; exynos2100; en_US; 562092456)
```

**Structure**: `Instagram <app_version> Android (<OS_version>/<SDK>; <dpi>; <resolution>; <device>; <model>; < SOC>; <locale>; <app_build>)`

For web/API requests, the `x-ig-app-id` header must be `936619743392459` (Instagram web app identifier). Wrong value = instant 403.

### What Gets Rejected

| Pattern | Result |
|---|---|
| Python default (`python-requests/x.x.x`) | Blocked at TLS layer before headers sent |
| Chrome headless default (`HeadlessChrome`) | Detected via `navigator.webdriver` |
| Generic `Mozilla/5.0` without Instagram app context | 400 Bad Request |
| UA claiming Android app but TLS fingerprint = Python | Mismatch caught at edge, returns stripped/empty data |
| UA changing mid-session | Instant flag for behavioral anomaly |

### instagrapi's device fingerprint

instagrapi ships with a built-in list of ~15 real device profiles (Samsung Galaxy, Pixel, OnePlus, etc.) and randomly selects from them on fresh `Client()` instantiation. When you persist settings with `dump_settings()`, the device UA is saved and reused. This is why session reuse is critical — it maintains a consistent UA across runs.

**Accepted UA format for iOS** (secondary):
```
Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 Instagram 12.0.0.16.90
```

---

## 4. Headless Browser Detection (navigator.webdriver, Automation Flags)

### The Detection Stack

Instagram runs JavaScript fingerprinting in the browser context. Key signals:

**Primary detection (via JavaScript execution):**
1. `navigator.webdriver === true` — set by Selenium, Playwright, Puppeteer CDP
2. `window._selenium`, `window._Selenium_IDE_Recorder`, `document.$cdc_asdjflasutopfhvcZLmcfl_` — Selenium variables in DOM
3. `navigator.userAgent.includes('HeadlessChrome')` — headless UA leak
4. Missing `chrome.runtime` object (real Chrome extensions API absent in headless)
5. Permissions API query for `'notifications'` returns `denied` in headless
6. `navigator.plugins.length === 0` AND `navigator.mimeTypes.length === 0` — real browser has plugins

**TLS/HTTP fingerprint (network layer):**
- Python `requests`/`httpx` have unique TLS handshake signatures (JA3 fingerprint) that Instagram detects as bots
- HTTP/2 frame ordering differs between real browsers and Python libraries
- Header order: real browsers send headers in specific order; scrapers often alphabetize or randomize

**Canvas/WebGL fingerprint (render layer):**
- Headless Chrome renders canvas with consistent, detectable signatures different from real GPUs
- WebGL renderer string differs in headless mode
- Font list is incomplete/missing in headless

### Fixes for Selenium/Playwright

**Selenium Stealth** (pip install selenium-stealth):
- Sets `navigator.webdriver` to false
- Replaces `HeadlessChrome` UA with real Chrome UA
- Fakes `chrome.runtime` object
- Patches permissions API
- Mocks plugins/mimeTypes arrays

**Playwright**:
- `playwright.chromium.launch(args=['--disable-blink-features=AutomationControlled'])`
- Blocks `navigator.webdriver` detection via CDP
- `--disable-web-security` can help but reduces fingerprint consistency

**curl_cffi** (best for pure HTTP):
- Mimics Chrome/Firefox TLS fingerprint
- Supports HTTP/2
- Can impersonate specific browser versions
- Used by ScrapFly under the hood

### Instagram-specific note

Instagram's anti-bot runs in the **web view context** (their website/app loads JavaScript). If you're hitting the **private mobile API** (instagrapi), headless browser detection is largely irrelevant — the detection is at the API protocol level (headers, TLS, device fingerprint). However, if you're using a browser automation approach to solve web-based challenges, the above detection vectors apply.

---

## 5. instagrapi UFAC Web Blocks — Specifics

### What causes it

The UFAC (User Fraud and Abuse Control) checkpoint is Instagram's hardest anti-bot wall. It triggers when:

1. **Repeated challenge failures**: You hit `challenge_required`, tried to resolve it via code, failed, and kept retrying
2. **IP + device fingerprint mismatch**: Logging in from a completely different network than the account's history, with a fresh device fingerprint
3. **Too many accounts from same IP**: If multiple Instagram accounts are managed from the same proxy IP and any one of them triggers a challenge, the IP itself can be UFAC-flagged
4. **Unusual velocity spikes**: An account that normally has low activity suddenly hammering API endpoints
5. **Geographic impossible travel**: Same account session used from two distant locations within a short time window

### The error message

```
instagrapi.exceptions.UnknownError: checkpoint_required
```

or in HTTP form:
```
HTTPError: 400 Client Error: Bad Request → checkpoint_required
```

Specifically the UFAC web block manifest as:
- URL in challenge response points to `/auth_platform/` or a Instagram.com URL that loads a JavaScript verification challenge
- The challenge cannot be solved with a 6-digit SMS/email code — it requires image-based verification (selecting posts, identifying friends, etc.) or is entirely manual
- `challenge_resolve()` in instagrapi cannot automate this flow

### Recovery path

1. **Do not retry the same credentials from the same IP** — it will escalate further
2. Open the challenge URL from a real browser on the account owner's device
3. Complete the verification manually
4. After manual resolution, the session is trust-rebuilt — dump settings immediately with `cl.dump_settings()`
5. If the account is UFAC-flagged server-side with no recovery path, rotate to a different account

**Prevention**: One account per stable residential proxy. Don't run multiple accounts from the same IP if any of them are doing write-heavy automation.

---

## 6. Best Practices for Scraping Instagram at Scale Without Triggering Blocks

### The Core Principle: Mimic Human Behavior + Stable Identity

Instagram's detection is multiplicative — one weakness compounds with others. You need to cover all layers simultaneously.

### Session & Identity Management

**Rule 1: One `Client()` instance = one account = one stable proxy/IP**

- Never use one `Client()` with multiple accounts interchangeably
- Never change proxy IP mid-session for the same account
- If you need multiple accounts, instantiate separate `Client()` objects with separate `settings.json` files

**Rule 2: Persist settings, never re-login from scratch**

```python
from instagrapi import Client
from pathlib import Path

session_file = Path("session.json")
cl = Client()
if session_file.exists():
    cl.load_settings(session_file)
cl.login("USERNAME", "PASSWORD")
# validate session
try:
    cl.get_timeline_feed()
except LoginRequired:
    # cookie expired, re-login but keep same device fingerprint
    old_uuids = cl.get_settings()["uuids"]
    cl.set_settings({})
    cl.set_uuids(old_uuids)
    cl.login("USERNAME", "PASSWORD")
cl.dump_settings(session_file)  # refresh after every successful login
```

**Rule 3: Warm up accounts before heavy automation**

- New accounts (<14 days old): start with read-heavy actions only
- No follows/unfollows/spam/DMs for first 3–5 days of warm-up
- First write actions: minimal volume, human-like timing
- Increase volume gradually over days, not minutes

### Request Pacing

**Rule 4: Randomized delays, always**

```python
cl.delay_range = [1, 3]  # random 1-3 seconds between requests
```

Fixed delays look like bots. Humans vary timing.

**Rule 5: Separate read and write job queues**

- Write actions (follow, like, comment, DM, post, profile edit) need stricter hygiene
- Read actions (profile scraping, media fetching) can scale further
- Run read jobs during write-cooldown periods

**Rule 6: Exponential backoff on errors**

```python
errors = {"429": 60, "PleaseWaitFewMinutes": 300, "FeedbackRequired": 600, "checkpoint_required": "STOP"}
```

Never retry in a tight loop. Each retry from a bad IP compounds the flag.

### Proxy Strategy

**Rule 7: Residential proxies only for any meaningful volume**

- Datacenter IPs (AWS, GCP, DigitalOcean, Hetzner, OVH): blocked on first request
- Residential IPs (Comcast, BT, Vodafone, AT&T): accepted, graded on behavioral consistency
- Mobile carrier IPs (T-Mobile, Verizon LTE, EE): highest trust, but 10-20x cost vs residential

**Recommended providers**:
- Bright Data: ~$8/GB, 150M+ IPs, best country targeting, sticky sessions
- Smartproxy: ~$7/GB, smaller pool but cleaner reputation
- Soax / IPRoyal: ~$4–6/GB, mixed quality

**Rule 8: Sticky sessions — don't rotate IP per request**

Use the same residential IP for 5–10 minutes, then rotate. Instant IP changes per request = bot signal.

### Error Handling

**Rule 9: Treat different error types differently**

| Error | Response |
|---|---|
| `HTTPError: 429` | Stop burst, wait 5-60 min, rotate IP |
| `PleaseWaitFewMinutes` | Stop all write actions, wait, do not retry loop |
| `FeedbackRequired` | Freeze the action type that triggered it |
| `ChallengeRequired` | Call `challenge_resolve()` if handler available, otherwise stop |
| `CheckpointRequired` | Manual intervention, page operator |
| `LoginRequired` | Relogin with same device fingerprint, validate session |

**Rule 10: Track errors per account + per proxy**

If `BadPassword` happens with a known-good password, it's an Instagram trust/risk rejection, not a credential problem. Separate credential issues from operational blocks.

---

## 7. Proxy/Residential IP Strategies That Work

### IP Quality Hierarchy (Instagram's trust scoring)

```
Mobile carrier LTE (T-Mobile, Verizon, EE)  →  highest trust, most generous limits
Residential ISP (Comcast, BT, AT&T)         →  high trust, baseline for production
ISP-hosted (some CDN/residential proxies)  →  medium trust, some scrutiny
Datacenter (AWS, GCP, DigitalOcean, etc.)   →  instant block on first request
VPN endpoints                               →  known blocklist, very high detection rate
```

### Per-Account IP Pinning

**The golden rule**: One account → one stable residential IP → same city/ASN

Instagram builds a login history per account. A US-based account logging in from a Vietnamese datacenter = instant challenge. A US-based account logging in from a US residential IP in the same metropolitan area = normal traffic.

### Proxy Configuration in instagrapi

```python
cl = Client()
before_ip = cl._send_public_request("https://api.ipify.org/")
cl.set_proxy("http://username:password@proxy.example.com:8080")
after_ip = cl._send_public_request("https://api.ipify.org/")
print(f"Before: {before_ip}, After: {after_ip}")
```

Use `socks5h://` for SOCKS proxies — this ensures DNS resolution goes through the proxy.

### Mobile Proxy Racks (self-rolled)

For maximum reliability at scale:
- Hardware: USB 4G modems ($40 each) + SIM cards ($20/mo each)
- Self-hosted: 5–20 modems in a rack
- Cost: ~$60–80/month per dedicated 4G IP
- Reliability: far exceeds purchased residential proxies (no shared IPs, no abuse history)
- Trade-off: operational complexity (hardware management, SIM health)

### IP Rotation Strategy

| Strategy | When to use | Notes |
|---|---|---|
| **Sticky (5-10 min)** | Normal scraping | Mimics real user behavior |
| **Request-level rotation** | High-volume (10K+ profiles/hr) with anti-bot bypass | Looks unnatural, only works with TLS header obfuscation |
| **Response-based rotation** | Any scale | Rotate on 429/403, continue same IP while 200 OK |
| **Geographic pinning** | Account-bound scraping | Keep requests in same country/region as account history |

---

## 8. Checkpoint Resolution Without Manual Phone Confirmation

### Automatable Challenges

**SMS or Email verification** (most common `ChallengeRequired`):
- Instagram makes the choice server-side based on verified contact methods
- You cannot force SMS vs email from the client
- instagrapi's `challenge_code_handler` callback handles this:

```python
from instagrapi import Client
from instagrapi.mixins.challenge import ChallengeChoice

def handler(username: str, choice: ChallengeChoice) -> str:
    # For SMS/email, Instagram sends a 6-digit code
    # Route to your SMS provider webhook or email inbox poller
    return get_code_from_sms_or_email(choice)

cl = Client()
cl.challenge_code_handler = handler
cl.login("USERNAME", "PASSWORD")
```

**For SMS automation**: Twilio or a real mobile number (not a virtual SMS app — Instagram maintains a blocklist of known VOIP/reseller gateways)

**For email automation**: IMAP inbox poller + 6-digit code regex extraction

### TOTP (Authenticator App) Fallback

If the account has an authenticator app set up, instagrapi can use TOTP:
```python
cl.challenge_code_handler = lambda u, c: get_totp_from_authenticator(secret)
```
Requires the TOTP secret to be stored.

### Non-Automatable Challenges

The following **cannot be resolved programmatically**:

1. **UFAC `/auth_platform/` web blocks** — image-based verification (select photos of friends, identify posts), requires human browser interaction
2. **Phone number verification** on a number you don't control
3. **Account recovery flows** (Instagram thinks the account was compromised)

**For UFAC blocks**: open the challenge URL in a real browser, complete manually, then re-establish the session programmatically. The session after manual resolution is trusted and can be dumped/loaded.

### Session Recovery After Manual Resolution

```python
cl.login("USERNAME", "PASSWORD")
cl.dump_settings("session.json")  # immediately after manual resolution
```

This is critical — without dumping settings immediately, you discard the trust proof on script exit and re-trigger the challenge on next run.

---

## 9. Session Management: Re-authentication Frequency & Cookie Refresh

### Session Lifecycle

Instagram sessions typically last:
- **Active use**: 30–90 days before requiring re-login
- **Idle**: much shorter — if you don't use an account for 2–4 weeks, Instagram will require fresh login
- **Suspicious behavior detected**: session killed immediately, `LoginRequired` raised

### The `LoginRequired` Recovery Pattern

```python
from instagrapi.exceptions import LoginRequired

cl.load_settings("session.json")
try:
    cl.login(USERNAME, PASSWORD)
    cl.get_timeline_feed()  # validate session is live
except LoginRequired:
    # Cookie expired. Relogin but PRESERVE device fingerprint
    old_settings = cl.get_settings()
    cl.set_settings({})  # reset to empty while keeping device uuids
    cl.set_uuids(old_settings["uuids"])  # keep same device identity
    cl.login(USERNAME, PASSWORD)
cl.dump_settings("session.json")
```

**Key**: `set_uuids()` preserves the device fingerprint across relogins. This prevents re-triggering `challenge_required` on the post-expiry login.

### Session Validation

Don't wait for `LoginRequired` to be raised. Validate on every run:

```python
try:
    cl.get_timeline_feed()
except LoginRequired:
    # re-authenticate
```

A lightweight `user/info/` call also works as a validation ping.

### Cookie Refresh Cadence

- **After every successful login**: dump settings (refreshes the cookie jar)
- **Every 7 days for active accounts**: force a re-login even if session appears valid, to refresh the cookie
- **After any error recovery**: dump settings after successfully recovering from any error

### Settings Object Structure (what gets persisted)

```json
{
  "device_settings": {
    "device_id": "android-xxx",
    "phone_id": "xxx",
    "uuid": "xxx",
    "client_session_id": "xxx",
    "device_brand": "Samsung",
    "device_model": "SM-G991B"
  },
  "cookies": {...},
  "token": "...",
  "uuids": {...}
}
```

This is what Instagram uses to recognize "returning device." Without it, every run looks like a new device.

### Storage Options

- **File** (`dump_settings("session.json")`): simple, good for single-instance
- **Redis**: for multi-process/multi-instance production workers
- **Postgres**: for distributed systems with session rotation across workers

See instagrapi session persistence docs for Redis/Postgres patterns.

---

## 10. Instagram GraphQL vs Private API v1 — Behavioral Differences

### The Two API Surfaces

**Private Mobile API** (`i.instagram.com/api/v1/`):
- instagrapi's primary surface
- Higher data fidelity (full user info, follower counts, stories, DMs)
- Requires session with device fingerprint
- Rate limits are per-account, enforced behaviorally
- Endpoints: `/users/{id}/info/`, `/friendships/{id}/followers/`, `/feed/timeline/`, etc.

**Web/GraphQL API** (`www.instagram.com/graphql/query/`):
- Public endpoint (works without auth for some data)
- Requires `doc_id` parameter mapping to pre-defined queries
- Returns structured data for posts, comments, hashtags, users
- Heavily rate-limited per IP for unauthenticated requests (~200 req/hour per IP)
- doc_id values change every 2–4 weeks (deliberate anti-scraping measure)
- Authenticated GraphQL sessions get higher limits but still below mobile API

**REST API** (`i.instagram.com/api/v1/users/web_profile_info/?username=`):
- Simple GET endpoint for profile data
- Works with auth headers (`x-ig-app-id: 936619743392459`)
- Returns up to 12 recent posts embedded in profile response
- Good for profile lookups; limited for granular data

### Key Differences Summary

| Aspect | Private Mobile API (instagrapi) | GraphQL Web API |
|---|---|---|
| **Auth required** | Yes (full session + device fingerprint) | Partial (some endpoints public) |
| **Data completeness** | Full payload (emails, phone, detailed metrics) | Reduced (some fields stripped) |
| **Follower data** | Full paginated list with user details | Limited/filtered |
| **Rate limits** | Per-account, behaviorally enforced | Per-IP, tighter for unauthenticated |
| **Session stability** | Stable if device fingerprint persisted | Less stable; web sessions expire faster |
| **Maintenance burden** | High (device fingerprint, challenge handling) | High (doc_id updates every 2–4 weeks) |
| **Stories/Reels** | Full support | Partial; different doc_ids |
| **Ease of use** | High (instagrapi handles protocol details) | Medium (need to discover/maintain doc_ids) |

### Practical Decision

- **Data extraction / scraping**: Private mobile API via instagrapi has higher reliability, more data, better rate limits
- **One-off queries / low volume**: GraphQL web API can work without session management overhead
- **Scale**: Both require significant maintenance — consider managed API (HikerAPI, ScrapFly, etc.) above ~50K req/day

### instagrapi's GraphQL Support

instagrapi has a `private_graphql_query_request()` method (via the `aiograpi` async variant) for private GraphQL queries. The `doc_id` problem is managed by instagrapi internally — the library maintainers update doc_ids when Instagram changes them. You still need to maintain session integrity.

---

## Quick Reference: Error Code Cheat Sheet

| Error | Class | Meaning | Recovery |
|---|---|---|---|
| `challenge_required` | `ChallengeRequired` | Anti-fraud CAPTCHA, SMS/email check needed | Wire `challenge_code_handler`, solve, dump settings |
| `checkpoint_required` | `UnknownError: checkpoint_required` | Hard escalation, human verification needed | Manual browser verification, operator page |
| `LoginRequired` | `LoginRequired` | Session/cookie expired | Re-login with same device fingerprint |
| `BadPassword` | `BadPassword` | Wrong password OR Instagram trust rejection | Verify credentials; if known-good = IP/device fingerprint issue |
| `HTTP 429` | `ClientThrottledError` | IP-level rate limit | Wait 5-60 min, rotate IP |
| `PleaseWaitFewMinutes` | `PleaseWaitFewMinutes` | Serious throttle | Stop all actions for that account, wait, investigate |
| `FeedbackRequired` | `FeedbackRequired` | Action blocked, account temporarily restricted | Freeze the triggering action, cooldown |
| `HTTP 400 on /feed/reels_tray/` | CheckpointPre-flow | Early login validation failure | Review proxy, device fingerprint, account warm-up |
| `/auth_platform/` in challenge URL | UFAC block | Manual web verification required | Cannot automate; manual resolution or rotate account |

---

## TL;DR Actionable Takeaways

1. **Always use `load_settings()` / `dump_settings()`** — this alone eliminates 80% of `challenge_required` errors
2. **One account + one stable residential proxy** — never mix or rotate mid-session
3. **Randomize delays**: `cl.delay_range = [1, 3]` minimum; fixed delays = bot
4. **Separate read from write** job queues; write actions need stricter hygiene
5. **On any error, treat different codes differently** — 429 means rotate IP, not retry immediately
6. **SMS/email challenges are automatable** with a `challenge_code_handler` callback pointing to an SMS gateway or email poller
7. **UFAC web blocks are not automatable** — if you hit them, either do manual verification or rotate the account
8. **GraphQL `doc_id` values change every 2–4 weeks** — if doing DIY GraphQL scraping, you need a monitoring/auto-update system
9. **For >50K req/day**: consider managed APIs (HikerAPI, ScrapFly) vs DIY infrastructure
10. **TLS fingerprint is checked before HTTP headers** — Python `requests` is detected instantly; use `curl_cffi` or browser automation for any approach that touches the TLS layer

---

## Sources & References

- instagrapi official docs: https://subzeroid.github.io/instagrapi/usage-guide/best-practices.html
- instagrapi challenge guide: https://instagrapi.com/guides/errors/challenge-required
- HikerAPI field reports: https://hikerapi.com/help/instagram-scraping-without-getting-blocked
- Scrapfly research: https://scrapfly.io/blog/posts/how-to-scrape-instagram
- GitHub issues: `subzeroid/instagrapi` discussions #1514, challenge.py source
- Community reports: Stack Overflow, Reddit r/Instagram, Dev.to