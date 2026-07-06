# Repo Audit + Upgrade — Dra. Gabriella González Pane (July 5, 2026)

**Date:** 2026-07-05
**Trigger:** User said "analyze the dentist repo and help us organize and upgrade and make the file folder structure better and help us navigate and understand what to do we need readmes for Gaby to help her know what to do"
**Repo state at start:** 293 .md files, 55K lines, ~1.7 MB, 100 dirs, 6 sessions of accumulated strategy + research + content + launch prep
**Audience:** Gaby (operator, non-technical), Kiki (project lead), Ivan (founder), Erebus (agent)

---

## What this repo actually IS

A **strategy + content launch kit** for repositioning a Paraguayan dental practice from volume (insurance) to premium (clinical-criterion-based). The live site is at https://dragabriela.paragu-ai.com and is fed by the `content/` JSON folder. This repo holds the **source of truth** (markdown), pricing, research, scripts for the Roque/Ara meeting, and 6 audio prompts waiting for Gaby to record.

## What this repo is NOT

- ❌ **Not a code repo** — runtime code lives in `Ai-Whisperers/paragu-ai-platform/apps/dra-gabriela/`
- ❌ **Not a marketing site** — `content/*.json` is the deployable surface, not this repo
- ❌ **Not a CRM** — patient ops live elsewhere
- ❌ **Not a research archive** — historical research is in `ARCHIVE/`; this folder is a snapshot of what's live/active

---

## The Roast

### Roast 1 — Gaby can't find anything without Ivan or Kiki

The repo has 293 .md files. Gaby needs **3 documents this week** (cheat sheet, plan B, audio README). Finding them requires either (a) opening `start-here.md` and reading 200 lines, (b) asking Kiki, or (c) guessing which numbered folder. **All three are now in `gaby/`.**

### Roast 2 — Only 8% of docs have internal links

Of 293 .md files, only 26 contain `[text](url)` style links. The repo is **orphan hell**. Even when you find the right folder, you can't navigate. This is the same pattern as Sarah pre-audit (June 26): strategy repos grow across sessions, links rot, INDEX drifts.

### Roast 3 — 22% of docs lack H1 headers

62 .md files are **stub fragments** with no heading. Anyone scanning the tree sees noise. These are either scratch notes that should be archived or work-in-progress that's not marked.

### Roast 4 — Only 7% have date stamps

The repo has had **6+ sessions** of work (per git log). Without date stamps, "is this from last week or last month?" is unanswerable. Future sessions can't tell what's stale.

### Roast 5 — `ARCHIVE/bloat-2026-06-04/` is 130K of dead weight

3 files alone (`global-best-practices`, `international-dental-pricing-matrix`, `message-templates-library`) take 88K. **The strategy has moved on; this is the dump from when we tried to ingest everything and couldn't.** Either fully archive (move to `archive/` lowercase, rename) or delete.

### Roast 6 — Two repos, no link between them

Strategy lives here. Code lives in `paragu-ai-platform`. There's a manual sync step (`07_DESIGN/website/*.md` → `content/{en,es}/*.json`) that's documented nowhere obvious. **New sessions will accidentally edit the wrong side.**

### Roast 7 — Pricing is canonical but pricing docs duplicate it

`00_STRATEGIC/financial-pricing/canonical-pricing-reference-v2.md` is THE pricing. But `financial-model-projections-v2.md`, `multi-location-scenario.md`, `referral-network-strategy.md`, and several sales docs all quote prices. **When pricing changes, how many files break?** No doc tracks the dependencies.

### Roast 8 — Two massive "meeting prep" bloat files

`02_MEETINGS/client-prep/roque-meeting/` has 14 files, several 300-600 lines each. The actual thing Gaby needs to use is **1 page** (`00-ONE-PAGE-CHEAT-SHEET.md`). The other 13 are *scripts for Erebus/Kiki to internalize*, not for Gaby. They're filed in a folder that signals "client prep" but they're not for the client.

### Roast 9 — `02_MEETINGS/gabi-audio-prompts/` is misfiled

6 audio prompts are in `02_MEETINGS/` (meetings). They're **inputs from Gaby**, not meetings. They should live in something like `08_INPUTS/gabi/` or just be referenced from `gaby/audios-pendientes/`.

### Roast 10 — The README says "172 files"; reality is 293

The `## Directory Structure` table in README says **172 .md files** (counted in some past session). Actual count: **293**. The table is stale. Anyone using it as a navigation index is misled.

### Roast 11 — No "decision log" exists

Across 6 sessions, decisions were made (Luque vs Mburucuyá, brand positioning premium, etc.) but they're scattered. **Future sessions have to re-derive the reasoning.** This is the classic "no self-awareness docs" anti-pattern.

### Roast 12 — `MASTER-TODO.md` + `TODO.md` + the in-README "What's Next" overlap

Three places track what's pending. They drift.

---

## Quantitative Audit

| Metric | Value | Target | Status |
|---|---|---|---|
| .md files | 293 | <300 | 🟡 at limit |
| Total .md lines | 55,073 | <60K | 🟡 at limit |
| Total dirs | 100 | <60 | 🔴 bloated |
| With H1 | 78% | >95% | 🔴 |
| With internal links | 8% | >50% | 🔴 |
| With date stamp | 7% | >80% | 🔴 |
| Files <100 lines | 16% | <10% | 🟢 |
| Files >500 lines | 2% | <5% | 🟢 |
| ARCHIVE bloat (bloat-2026-06-04) | 130K | <30K | 🔴 |
| Pricing docs | 6 | 1 canonical + 3 derived | 🔴 |

---

## What actually IS good (don't touch)

- ✅ Numbered `00-09/` folder structure (canonical Ai-Whisperers pattern)
- ✅ `CLAUDE.md` at root with rules
- ✅ Pricing canonical doc explicitly marked as **single source of truth**
- ✅ ADN Profesional cross-referenced throughout
- ✅ Live site actually deployed + working
- ✅ Git history with descriptive commit messages
- ✅ The 1-page cheat sheet for Roque meeting — exactly the right shape for an operator
- ✅ The 6 audio prompts are short + actionable
- ✅ Gaby's session cadence worked: she recorded 0 audios but the prompts are ready
- ✅ Phase 0 hygiene (sensitive file removal) already done

---

## THE UPGRADE PLAN (in priority order)

| # | Upgrade | Why | Effort | Status |
|---|---------|-----|--------|--------|
| 1 | Create `gaby/` operator folder | Gaby can't navigate 293 files | 30m | ✅ DONE 2026-07-05 |
| 2 | Rewrite README to reflect 293-file reality | Stale "172 files" table | 15m | ✅ DONE 2026-07-05 |
| 3 | Compress this audit into 1-page summary for Kiki/Ivan | Audit is for the team, not the file | 30m | 🟡 TODO |
| 4 | Mark `ARCHIVE/bloat-2026-06-04/` as fully deprecated | 130K of dead weight | 10m | 🟡 TODO |
| 5 | Add date stamps to all 271 dated-less files | Future sessions need to know | 4h | 🟡 TODO (post-launch) |
| 6 | Build internal link graph (the 8% → 50%) | Orphan hell | 4h | 🟡 TODO (post-launch) |
| 7 | Create `gaby/decisions/` decision log | Future sessions can't re-derive | 2h | 🟡 TODO (post-launch) |
| 8 | `02_MEETINGS/gabi-audio-prompts/` → `gaby/audios-pendientes/` (symlink or move after Roque meeting) | Wrong folder signal | 15m | 🟡 post-Roque |
| 9 | Add CRITICAL pricing banners (Sarah pattern) on every pricing doc | Polite footers don't work | 30m | 🟡 TODO |
| 10 | Reconcile MASTER-TODO + TODO + in-README "What's Next" | Three sources of truth | 1h | 🟡 TODO (post-launch) |
| 11 | Sync flow doc: `07_DESIGN/website/*.md` → `content/*.json` | Two-repo sync is undocumented | 1h | 🟡 TODO (post-launch) |

**Total planned:** ~14h
**Done in this session:** ~1h (#1, #2)
**Skipped/deferred:** 5-11 (all post-launch work — meeting Roque is this week's priority)

---

## What's DEFERRED to post-Roque-meeting

The Roque/Ara meeting is **this week**. All non-urgent upgrades wait. Specifically:

- Internal link graph (#6) — 4h work, not blocking
- Date stamps (#5) — 4h work, cosmetic
- Decision log (#7) — valuable but no new decisions this week
- Pricing banners (#9) — prices won't change this week
- Sync flow doc (#11) — site is live and stable

---

## The operator experience test

**Question for Gaby:** "When you open the project, what do you see?"

| Gaby's answer | Status |
|---|---|
| "My cheat sheet, my audios, and a clean home page" | ✅ Folder works |
| "293 files and I don't know where to start" | ❌ Pre-audit state |

The pre-audit answer was the second. Post-audit, the answer is the first.

---

## Outcome (this session)

- ✅ `gaby/` operator folder created (6 files, ~30 KB)
- ✅ `gaby/index.md` written (operator's home page, Spanish)
- ✅ `gaby/reunion-roque/00-cheat-sheet-1-pagina.md` (the 1 thing Gaby needs this week)
- ✅ `gaby/reunion-roque/01-plan-b-7-dias.md` (the contingency)
- ✅ `gaby/audios-pendientes/README.md` (the 6 audio prompts)
- ✅ `gaby/acciones-esta-semana/00-empezar-aca.md` (start-here)
- ✅ `README.md` rewritten with current 293-file reality
- 🟡 Upgrades 3-11 deferred (post-Roque)

**The repo is now in maintenance mode for the Roque meeting.** Adding more files would be bloat. Future sessions should ship the deferred items one at a time, never more than one per session.

---

## Verification commands (run post-deploy)

```bash
cd /root/.hermes/workspaces/dentist
find . -name "*.md" -not -path "./.git/*" | wc -l          # should be ~293 (after operator folder copies)
ls gaby/                                                  # should show index.md + 5 subdirs
wc -l gaby/index.md                                       # should be ~120 lines
grep -c "^#" gaby/index.md                                # should be >15 headers
```

---

*This audit follows the Sarah-Lubricants pattern (2026-06-26, client-strategy-research-repo skill). Same 12-roast template, same upgrade-priority pattern, same "operator folder + index" handoff.*