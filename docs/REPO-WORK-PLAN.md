# Dentist Repo — Full Work Plan
## Scope
`Ai-Whisperers/dentist`: strategy + launch documentation for Dra. Gabriella González Pane’s premium dental practice (Luque/Asunción, PY).

## Current baseline
- 178 active markdown documents
- Canonical pricing declared in `00_STRATEGIC/financial-pricing/canonical-pricing-reference-v2.md`
- Multiple stale values: Gs 3M thresholds, file counts (135/138/181), duplicate folder remnants
- Sensitive artifacts: xlsx trackers, JSON scrapes, `.ig_session.json`, `.cp_*.json`
- 4 competing entry-point documents: README, start-here, COMPLETE-INDEX, TODO
- No repo-level AI config (`AGENTS.md`) until today

---

## Phase 0 — Repo Hygiene & Trust (P0, must finish before any feature work)
**Owner:** Erebus  
**Duration:** 1 session  
**Exit criteria:** Repo is internally consistent; pricing tables cross-check clean; no stale "135/138/181/3M" values outside ARCHIVE.

| ID | Task | Steps | Acceptance |
|----|------|-------|-----------|
| P0.1 | Stale-value sweep | Grep `Gs 1\.5M\|Gs 3M\|~[0-9]+ files\|135 files\|138 files\|181 files` across all non-ARCHIVE .md; patch every hit to match canonical (Gs 3M threshold or live .md count) | 0 stale hits in active folders |
| P0.2 | Sensitive-data audit | Inventory `.json/.xlsx/.csv` outside ARCHIVE/.gitignore. Flag session files. Add `.gitignore` rules for `.xlsx .csv .env *.json` outside whitelisted site-config(); move ARCHIVE scrapes to private repo or add to gitignore | 0 raw session/cookie files tracked in git |
| P0.3 | ARCHIVE hygiene | Add ARCHIVE/README.md (done). Audit each JSON for PII/credentials. Either prune or keep with clear naming (no `ddgs-*` / `scrape-*` in active tree) | ARCHIVE has README, every file has a 1-line purpose note |
| P0.4 | PRICING CROSS-REFERENCE block enforcement | Find every doc with price tables; confirm top-of-file block exists; if missing, add the standard 4-line block pointing to canonical | 100% of priced docs have the block |
| P0.5 | Cross-ref validator (script) | Write `tools/validate-refs.py`: extract all markdown links (`[text](path)`) and verify target exists on disk. Run, fix broken links, commit. | 0 broken intra-repo markdown links in active folders |

---

## Phase 1 — Index & Navigation (P1)
**Owner:** Erebus  
**Duration:** 1 session  
**Exit criteria:** One click gets you from README to any doc; every folder has an accurate `00-index.md`; counts are always correct.

| ID | Task | Steps | Acceptance |
|----|------|-------|-----------|
| P1.1 | Auto-count script | `tools/repo-audit.py` with subcommand `counts` that prints per-folder .md counts and exact total. Output is deterministic. | Run: `python tools/repo-audit.py counts` |
| P1.2 | Unify entry points | Make README the single hub. start-here.md becomes "executive summary of the kit" only. COMPLETE-INDEX.md becomes machine-generated appendix from P1.1. TODO.md stays as action tracker. | README references all other entry points |
| P1.3 | Missing 00-index.md | Every folder that lacks `00-index.md` gets one: list contents + purpose + key docs to read first. Folders checked: 04_SALES, 05_OPERATIONS/clinical-routines, 05_OPERATIONS/patient-communications, 05_OPERATIONS/legal-compliance, 06_MARKETING, 07_DESIGN/brand-assets, 08_WHATSAPP/templates | No folder is missing its index |
| P1.4 | Dead-link sweep | Run P0.5 validator on full active tree. Fix every broken intra-repo link. Add to pre-commit hook (Phase 3) | 0 broken intra-repo links |
| P1.5 | Folder naming audit | Confirm no spaces remain in folder names. Confirm `06_MARKETING/` only (no `06 MARKETING/`). Rename if found. | `find . -type d -name '* *'` returns 0 results in active tree |

---

## Phase 2 — Content Alignment & Completion (P2)
**Owner:** Erebus + Kiki  
**Duration:** 2-3 sessions  
**Exit criteria:** No placeholder prices, no TODO-only sections in client-facing docs, every strategic doc covers actual content (not "fill later").

| ID | Task | Steps | Acceptance |
|----|------|-------|-----------|
| P2.1 | Pricing table completeness | For every service in `canonical-pricing-reference-v2.md`, grep across active folders and verify each service appears in at least 3 consumer-facing docs (pricing page, agreement, one-pager, website content). Add missing cross-refs. | 100% coverage |
| P2.2 | Phase 0 checklist | `00_STRATEGIC/PHASE-0-CHECKLIST-JUNE-2026.md`: expand the 7 awaiting items into sub-items with owner, data source, deadline, and evidence needed. Wire to TODO.md. | Checklist is actionable without new info |
| P2.3 | Patient journey specs | Write 3 patient profiles (insurance, private premium, expat). Map each through: first-contact → scheduling → consultation → treatment plan → payment → recall. Link existing templates to each touchpoint. | 3 de-identified journeys, template cross-refs added |
| P2.4 | Competitor battle cards | From `01_RESEARCH/market/mystery-shop-20-clinics-report.md`, extract top 3 competitors. One-pager each: positioning, price range, differentiators, weakness. Place in `01_RESEARCH/market/battle-cards/`. | 3 battle cards referencing only verified mystery-shop data |
| P2.5 | Objection library | From `08_WHATSAPP/flows/` and meeting notes, extract 20 real objections. Template replies split by channel (WhatsApp, phone, in-person). Place in `08_WHATSAPP/templates/objection-library.md`. | 20 objections, reply templates |
| P2.6 | Corporate sales tracker hygiene | `03_LAUNCH/corporate-sales/outreach/corporate-sales-tracker.xlsx`: audit columns, add status + last-contact + follow-up-date. Document the tracker structure in a companion `.md`. | Tracker is usable without explanation; doc covers schema |
| P2.7 | 3-Option reconciliation | `00_STRATEGIC/strategic-context/three-strategic-options-analysis.md` vs `03_LAUNCH/roadmap/master-launch-roadmap.md`: unify Option A/B/C definitions, risk ratings, and required investment. One source, both reference it. | Both docs point to single options definition |

---

## Phase 3 — Operational Tooling (P3)
**Owner:** Erebus  
**Duration:** 1-2 sessions  
**Exit criteria:** Repo can police itself; recurring maintenance is automated.

| ID | Task | Steps | Acceptance |
|----|------|-------|-----------|
| P3.1 | `tools/repo-audit.py` (comprehensive) | Subcommands: `counts`, `stale` (grep known stale strings), `crossrefs` (P0.5), `sizes` (largest files per folder), `summary` (all in one). Run as cron. | `python tools/repo-audit.py summary` outputs dashboard |
| P3.2 | Price propagation script | `tools/update-pricing.py`: reads `canonical-pricing-reference-v2.md`, finds all price tables in active docs, asks (interactive) for confirmations before patching. Log changes to `CHANGELOG.md`. | Dry-run shows 10+ planned changes; actual run applies + commits |
| P3.3 | Pre-commit hook | `.git/hooks/pre-commit` or `scripts/pre-commit`: run `repo-audit.py stale`; fail commit if any stale hit in non-ARCHIVE files. | Git commit blocks on P0.1/P0.2 violations |
| P3.4 | Monthly review cron | Weekly cron that runs `repo-audit.py summary`, diffs TODO.md completed vs pending vs last-week snapshot, posts summary to Telegram/n8tify. | First automated review runs and delivers summary within 30 min |

---

## Phase 4 — Client Delivery Artifacts (P4)
**Owner:** Kiki + Erebus  
**Duration:** 1 session  
**Exit criteria:** Dra. GP has a single document that tells her exactly what to do this week.

| ID | Task | Steps | Acceptance |
|----|------|-------|-----------|
| P4.1 | Dra. GP one-pager | Collapse TODO.md awaiting-items + Phase 0 checklist into a single, visually clean Markdown page. Phone-friendly formatting (tables, no long paragraphs). Place at `docs/dra-gp-status-june-2026.md`. | Fits on one mobile screen per section |
| P4.2 | Phase 0 binder | Combine TODO.md + checklist + decision tree + pricing summary into `docs/phase-0-binder.md`. Print-ready (wide margins, page-break hints). | PDF export renders correctly from Markdown |
| P4.3 | Investor summary | 1-page from `00_STRATEGIC/financial-pricing/financial-model-projections-v2.md`: ask amount, months of runway, break-even scenario, risk factors. Export-ready. | Fits 1 page; numbers match canonical |

---

## Phase 5 — Growth / Next Phase (P5)
**Owner:** Ivan + Erebus  
**Duration:** Ongoing  
**Exit criteria:** Repo supports second-location planning or corporate rollup if Phase 0 succeeds.

| ID | Task | Steps | Acceptance |
|----|------|-------|-----------|
| P5.1 | Sitemap → build manifest | From `07_DESIGN/website/`, generate `sitemap.md` listing every page with status (draft / approved / published). Wire to any future static site build. | sitemap.md is authoritative |
| P5.2 | Corporate sales SLA doc | From `04_SALES/corporate-service-agreement-full.md` + tracker, write a 1-page SLA summary (response time, coverage, escalation) for B2B clients. | SLA is ready to attach to proposal |
| P5.3 | Multi-location model | Extend `00_STRATEGIC/financial-pricing/financial-model-projections-v2.md` with a second-location scenario (Clinic B = corporate/expats, Clinic A = insurance). Validate with Ivan. | Second scenario in the same workbook |

---

## Sequencing
```
P0 (Hygiene) → P1 (Nav) → P2 (Content) → P3 (Tooling) → P4 (Delivery) → P5 (Growth)
                [Kiki reviews P1.3 indexes in parallel]
                            [Kiki feeds P2.2/P2.3 from Dra. GP data]
                                         [P4.1 uses P2.2 output]
```

Start with P0.1 now.
