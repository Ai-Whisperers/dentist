# Additional Organization Improvements & Suggestions

---

## 1. GROUP ROOT-LEVEL PLANNING DOCS INTO `/planning/` SUBFOLDER

Currently 3 reorganization documents clutter the root:
```
REORGANIZATION-PLAN.md
REORGANIZATION-INVENTORY.md
REORGANIZATION-FOLDER-RENAME-PLAN.md
```

**Proposal:** Move all three into `planning/` subfolder. After execution, these become historical reference, not active docs.

---

## 2. ROOT-LEVEL FILE CLEANUP

| File | Action |
|------|--------|
| `tee` | ❌ DELETE — accidental artifact |
| `COMPLETE-INDEX.md` | Merge into `README.md` — eliminate duplication |
| `README.md` | Expand to be sole index page |
| `TODO.md` | Move to `planning/TODO.md` — active sprint items |
| `REORGANIZATION-*.md` | Move to `planning/` |
| `CHANGELOG.md` | Create or move to `planning/` |

---

## 3. CONSOLIDATE README + COMPLETE-INDEX

**Current problem:**
- `README.md` has a directory structure table (outdated)
- `COMPLETE-INDEX.md` has the same info + pricing + channels + status

**Proposal:** Keep only `README.md` as the single entry point. Integrate:
- Directory structure (auto-updated)
- Quick-start links
- Pricing summary
- Project status
- Delete `COMPLETE-INDEX.md` after merge

---

## 4. ADD `planning/00-PLAN-INDEX.md` — Navigation for the Planning Docs

After reorganization, create:
```
planning/
├── 00-PLAN-INDEX.md          # What all these planning docs are + navigation
├── REORGANIZATION-PLAN.md     # Keep as historical record
├── REORGANIZATION-INVENTORY.md
└── REORGANIZATION-FOLDER-RENAME-PLAN.md
```

---

## 5. INTRODUCE GROUPING PREFIXES FOR SUBFOLDERS (Already in Plan)

The plan already groups subfolders well. One additional suggestion — use **2-digit prefixes** for subfolders to enforce order within each parent:

```
01_RESEARCH/
├── 01-market/
├── 02-pricing/
├── 03-legal-compliance/
├── 04-payments/
├── 05-locations/
├── 06-community/
└── 07-equipment/

03_LAUNCH/
├── 01-roadmap/
├── 02-institutional-sales/
├── 03-corporate-sales/
├── 04-referral-program/
├── 05-crm-systems/
├── 06-whatsapp-outreach/
└── 07-website-content/
```

**Benefit:** Subfolders always sort in intended order, even if someone adds new ones later.

---

## 6. ADD `docs/` FOLDER FOR PROJECT DOCUMENTATION

Move all root docs that aren't user-facing into a `docs/` folder:
```
docs/
├── CLAUDE.md              # Agent instructions
├── CHANGELOG.md          # Version history
├── TODO.md               # Sprint tracking
└── planning/             # (from suggestion #1)
    ├── REORGANIZATION-PLAN.md
    ├── REORGANIZATION-INVENTORY.md
    └── REORGANIZATION-FOLDER-RENAME-PLAN.md
```

**Root would then only contain:**
- `README.md` (user entry point)
- `start-here.md` (quick start)
- `docs/` (agent + planning materials)
- `.gitignore`, `.opencode/`, `.swarm/`, `.firecrawl/` (system)

---

## 7. CONSIDER: SPLIT `04_SALES/` INTO TWO?

Currently `04_SALES/` has only 3 files:
- `corporate-service-agreement-full.md`
- `institutional-referral-agreement.md`
- `agreements/` (subfolder with 1 file)

**Option A:** Keep flat — 3 files is fine
**Option B:** Merge agreements back into root and delete `agreements/` subfolder
**Option C:** Add more sales docs (pipeline tracking, lead tracking, etc.)

Recommendation: **Option B** — `agreements/` subfolder is overkill for 3 files.

---

## 8. CONSIDER: `03_LAUNCH/website-additions/` → `07_DESIGN/website/content/`

The website content modules (`social-proof-trust-signals-content.md`, etc.) are design/content specs, not launch items. Move them under `07_DESIGN/website/content/` instead of `03_LAUNCH/website-additions/`.

This puts all website-related content in one place:
```
07_DESIGN/
├── brand-assets/
└── website/
    ├── content/          # (moved from 03_LAUNCH/website-additions/)
    ├── home-page-content.md
    ├── about-page-content.md
    └── ...
```

---

## 9. MERGE `01_LAUNCH/website-spec.md` INTO `06_MARKETING/website-full-specification.md`

Currently both exist:
- `01_LAUNCH/website-spec.md`
- Plan: `06_MARKETING/website-full-specification.md`

They should be **one file**. Consolidate and put in `06_MARKETING/`.

---

## 10. ADD `ARCHIVE/` FOLDER FOR OLD VERSIONS

When files are superseded (e.g., `phone-mystery-shop-report.md` vs `phone-mystery-shop-FRESH.md`), move the older version to `ARCHIVE/` instead of deleting. Keeps git history accessible but clear.

```
ARCHIVE/
├── phone-mystery-shop-report.md
├── luque-rental-research.md
├── eas-registration-walkthrough.md
└── ...
```

---

## REVISED ROOT STRUCTURE (Final Recommendation)

```
dentist/
├── README.md                           # Single entry point (merged)
├── start-here.md                      # 5-min quick start
│
├── docs/                              # Project management
│   ├── CLAUDE.md
│   ├── CHANGELOG.md
│   ├── TODO.md
│   └── planning/
│       ├── 00-PLAN-INDEX.md
│       ├── REORGANIZATION-PLAN.md
│       ├── REORGANIZATION-INVENTORY.md
│       └── REORGANIZATION-FOLDER-RENAME-PLAN.md
│
├── 00_STRATEGIC/                      # Strategic decisions
├── 01_RESEARCH/                       # Market & competitive intelligence
├── 02_MEETINGS/                       # Meeting prep
├── 03_LAUNCH/                         # Launch execution
├── 04_SALES/                          # Corporate/institutional deals
├── 05_OPERATIONS/                     # Day-to-day practice
├── 06_MARKETING/                      # Digital presence
├── 07_DESIGN/                         # Brand + website
├── 08_WHATSAPP/                       # WhatsApp automation
├── 09_TEMPLATES/                      # Patient-facing templates
│
└── ARCHIVE/                           # Superseded files (optional)
```

**Root goes from 10 folders + 10 files → 10 folders + 2 files (README + start-here)**

---

## RECOMMENDED ADDITIONAL ACTIONS

| # | Action | Benefit |
|---|--------|---------|
| 1 | Move reorganization docs to `planning/` | Cleaner root |
| 2 | Delete `tee` | Remove artifact |
| 3 | Merge COMPLETE-INDEX into README | Single source of truth |
| 4 | Add 2-digit prefixes to subfolders | Enforced sort order |
| 5 | Move `website-additions/` to `07_DESIGN/website/content/` | Cohesive website folder |
| 6 | Consolidate `website-spec.md` | One spec, one location |
| 7 | Add `ARCHIVE/` for superseded files | Preserves history, clears clutter |
| 8 | Add `docs/planning/00-PLAN-INDEX.md` | Navigation for planning docs |

---

## IMPACT SUMMARY

| Change | Files Affected |
|--------|---------------|
| Move planning docs to `planning/` | 3 files |
| Delete `tee` | 1 file |
| Merge COMPLETE-INDEX into README | 1 file deleted |
| Rename subfolders (add 2-digit prefixes) | ~25 folders |
| Move website-additions → design | 6 files |
| Merge website-spec duplicates | 1 file deleted |
| Create ARCHIVE/ and move old versions | ~5 files |
| **Total changes** | **~42 items** |