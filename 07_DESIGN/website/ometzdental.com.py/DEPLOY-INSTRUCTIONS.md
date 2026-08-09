# Ometz Dental — Deploy Script

## Current State

✅ **Repo ready:**
- `/home/ai-whisperers/dentist/07_DESIGN/website/ometzdental.com.py/index.html` — full ES content with real WA +595 981 146 759, email DrGabriellaGonzalez@ometzdental.com, address Auditores de la Guerra del Chaco 617
- `/home/ai-whisperers/dentist/07_DESIGN/website/ometzdental.com.py/index-en.html` — full EN translation
- ✅ Pushed to `Ai-Whisperers/dentist` on GitHub (commit `a6f70da`)

❌ **Live site still serving placeholder** — Cloudflare Pages has not auto-rebuilt.

## What's blocking live deploy

The Cloudflare Pages project for `ometzdental.com` is either:
1. Connected to a different repo/branch than `Ai-Whisperers/dentist@master`
2. Has GitHub integration disabled
3. Requires manual trigger

## Three ways to deploy

### Option A: Cloudflare Dashboard (5 min, manual)

1. Go to https://dash.cloudflare.com → Pages → `ometzdental` (or `ometzdental.com`)
2. **Settings → Builds → Configure**
3. Confirm:
   - Production branch: `master` (or `main`)
   - Build command: (none — static HTML)
   - Build output: `/07_DESIGN/website/ometzdental.com.py/`
4. **Deployments → Trigger deploy → Deploy site**
5. Wait ~1 min → verify at https://ometzdental.com/es

### Option B: Wrangler CLI (2 min, if you have CF_API_TOKEN)

```bash
export CLOUDFLARE_API_TOKEN="your-token-with-pages-write"
cd /home/ai-whisperers/dentist/07_DESIGN/website/ometzdental.com.py/
wrangler pages deploy . --project-name=ometzdental --branch=master
```

To find your project name, check `wrangler pages project list` after auth:
```bash
wrangler login  # OAuth browser flow
wrangler pages project list
```

### Option C: Direct upload via Dashboard (3 min)

1. Cloudflare Dashboard → Pages → ometzdental → **Create deployment**
2. Drag-drop the folder: `/home/ai-whisperers/dentist/07_DESIGN/website/ometzdental.com.py/`
3. Set production branch, deploy

## Verification after deploy

```bash
# Should show 'Te escucho' and 595981146759
curl -sL https://ometzdental.com/es | grep -E "Te escucho|595981146759|Auditores"

# Should show 'I listen' and same WA
curl -sL https://ometzdental.com/en | grep -E "I listen|595981146759|Auditores"
```

## If CF Pages isn't connected to this repo

There's likely an older Pages project with manual uploads. To verify:

1. Dashboard → Pages → list all projects
2. Find the one with custom domain `ometzdental.com`
3. Check its source — if "Direct Upload" only, use Option C above

## Alternative: Deploy the Next.js app (longer, full features)

The full-featured Next.js app is at:
`/home/ai-whisperers/paragu-ai-platform/apps/dra-gabriela/`

It has 22+ routes, i18n, theme switcher, JSON-LD, etc.

Deploy:
```bash
cd /home/ai-whisperers/paragu-ai-platform/apps/dra-gabriela/
pnpm install
NEXT_BUILD_WORKERS=1 pnpm run build  # Turbopack single-worker race workaround
docker build -t dra-gabriela:prod -f Dockerfile ../..
docker service update --image dra-gabriela:prod dra-gabriela_web
# OR for Cloudflare Pages:
wrangler pages deploy .next/standalone/apps/dra-gabriela/.next/static --project-name=ometzdental
```

This requires the swarm manager to be running and is the "real" production target.
