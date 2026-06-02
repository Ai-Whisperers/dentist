# Folder Renaming Plan — Complete Mapping

---

## TOP-LEVEL FOLDER RENAME/REORGANIZATION

| Current | New | Rationale |
|---------|-----|-----------|
| `00_PROJECT/` | `00_STRATEGIC/` | Reflects content — strategic decisions, not project management |
| `01_LAUNCH/` | `03_LAUNCH/` | Repositioned after RESEARCH and MEETINGS |
| `02_RESEARCH/` | `01_RESEARCH/` | Should come before LAUNCH |
| `03_RESEARCH_EXTRAS/` | **DELETE** | Empty, redundant — absorbed into 01_RESEARCH/ |
| `04_MEETINGS/` | `02_MEETINGS/` | Should come before LAUNCH |
| `05_OPERATIONS/` | `05_OPERATIONS/` | Keep same number, but restructure subfolders |
| `06_MARKETING/` | `06_MARKETING/` | Keep same number |
| `07_DESIGN/` | `07_DESIGN/` | Keep same number, but restructure subfolders |
| `08_WHATSAPP/` | `08_WHATSAPP/` | Keep same number |
| `09_TEMPLATES/` | `09_TEMPLATES/` | Keep same number |

---

## SUBFOLDER RENAME PLAN

### 01_RESEARCH/ — New Subfolder Names

| Current Subfolder | New Subfolder | Files |
|-------------------|---------------|-------|
| (root level, no subfolder) | `market/` | 4 |
| (root level, no subfolder) | `pricing/` | 2 |
| (root level, no subfolder) | `legal-compliance/` | 7 |
| (root level, no subfolder) | `payments/` | 2 |
| (root level, no subfolder) | `locations/` | 4 |
| (root level, no subfolder) | `community/` | 3 |
| (root level, no subfolder) | `equipment/` | 1 |
| `00-index/` | **DELETE** | — |

### 03_LAUNCH/ — New Subfolder Names

| Current Subfolder | New Subfolder | Files |
|-------------------|---------------|-------|
| (root level, many files) | `roadmap/` | 4 |
| (root level, many files) | `institutional-sales/` | 5 |
| (root level, many files) | `corporate-sales/` | 4 |
| (root level, many files) | `referral-program/` | 2 |
| (root level, many files) | `crm-systems/` | 3 |
| (root level, many files) | `whatsapp-outreach/` | 3 |
| `website-additions/` | `website-additions/` | 6 (cleaned) |
| `00-index/` | **DELETE** | — |

### 02_MEETINGS/ — Subfolder Rename (No Change)

| Current | New | Rationale |
|---------|-----|-----------|
| `client/` | `client-prep/` | More descriptive |
| `kiki/` | `kiki-meeting/` | More descriptive |

### 05_OPERATIONS/ — New Subfolder Names

| Current Subfolder | New Subfolder | Files |
|-------------------|---------------|-------|
| (root level, many files) | `clinical-routines/` | 5 |
| (root level, many files) | `patient-communications/` | 4 |
| (root level, many files) | `legal-compliance/` | 9 |
| `00-index/` | **DELETE** | — |

### 07_DESIGN/ — Subfolder Rename

| Current | New | Rationale |
|---------|-----|-----------|
| (root level, many files) | `brand-assets/` | Group all print/branding specs |
| `website/` | `website/` | Keep same — already well named |
| `00-index/` | **DELETE** | — |

### 08_WHATSAPP/ — Subfolder Structure (No New Subfolders)

| Current | New | Rationale |
|---------|-----|-----------|
| `00-index/` | **DELETE** | — |

---

## COMPLETE FOLDER TREE TRANSFORMATION

### Before (Current State)

```
dentist/
├── 00_PROJECT/
├── 01_LAUNCH/
│   ├── 00-index/          (empty)
│   └── website-additions/ (30 files + noise)
├── 02_RESEARCH/
│   └── 00-index/          (empty)
├── 03_RESEARCH_EXTRAS/    (1 file — DELETE)
├── 04_MEETINGS/
│   ├── client/
│   └── kiki/
├── 05_OPERATIONS/
│   ├── 00-index/          (empty)
│   └── (25 files root)
├── 06_MARKETING/
├── 07_DESIGN/
│   ├── 00-index/           (empty)
│   └── website/
├── 08_WHATSAPP/
│   └── 00-index/           (empty)
└── 09_TEMPLATES/
    └── 00-index/           (empty)
```

### After (Target State)

```
dentist/
├── 00_STRATEGIC/                  # renamed from 00_PROJECT
├── 01_RESEARCH/
│   ├── market/
│   ├── pricing/
│   ├── legal-compliance/
│   ├── payments/
│   ├── locations/
│   ├── community/
│   └── equipment/
├── 02_MEETINGS/
│   ├── kiki-meeting/
│   └── client-prep/
├── 03_LAUNCH/
│   ├── roadmap/
│   ├── institutional-sales/
│   ├── corporate-sales/
│   ├── referral-program/
│   ├── crm-systems/
│   ├── whatsapp-outreach/
│   └── website-additions/
├── 04_SALES/                      # NEW — split from LAUNCH
│   └── agreements/
├── 05_OPERATIONS/
│   ├── clinical-routines/
│   ├── patient-communications/
│   └── legal-compliance/
├── 06_MARKETING/
├── 07_DESIGN/
│   ├── brand-assets/
│   └── website/
├── 08_WHATSAPP/
└── 09_TEMPLATES/
```

---

## FOLDER COUNT CHANGE

| Metric | Before | After |
|--------|--------|-------|
| Top-level folders | 10 | 10 |
| Subfolders (non-empty) | ~7 | ~25 |
| Empty directories | 7 | 0 |
| Folders to DELETE | 8 | — |
| Folders to CREATE | — | ~25 |

---

## EXECUTION ORDER

1. `mkdir` all new subfolders under each top-level folder
2. `git mv` files into new subfolders (preserves git history)
3. Delete empty directories
4. `git mv` top-level renames last (00_PROJECT → 00_STRATEGIC, etc.)

**Note:** `git mv` preserves full file history — all blame/log will still work after reorganization.
