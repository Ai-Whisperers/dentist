# Repository Reorganization Plan v4 — Max 6 Files Per Folder

**Rule: No folder may have more than 6 files. Subfolders become mandatory for any folder exceeding 6.**

---

## FULL REVISED STRUCTURE

```
dentist/
├── README.md
├── start-here.md
│
├── docs/
│   ├── CLAUDE.md
│   ├── CHANGELOG.md
│   ├── TODO.md
│   └── planning/
│       ├── 00-index.md
│       ├── REORGANIZATION-PLAN.md
│       ├── REORGANIZATION-INVENTORY.md
│       ├── REORGANIZATION-FOLDER-RENAME-PLAN.md
│       └── REORGANIZATION-ADDITIONAL-SUGGESTIONS.md
│
├── 00_STRATEGIC/
│   ├── 00-index.md
│   ├── strategic-context/              # 3 files (max 6 ✓)
│   │   ├── executive-summary-dra-gp.md
│   │   ├── client-profile-deep-dive.md
│   │   └── three-strategic-options-analysis.md
│   │
│   └── financial-pricing/            # 6 files (max 6 ✓)
│       ├── brand-positioning-premium.md
│       ├── master-pricing-sheet.md
│       ├── financial-model-projections-v2.md
│       ├── referral-network-strategy.md
│       ├── digital-presence-strategy.md
│       └── canonical-pricing-reference-v2.md
│
├── 01_RESEARCH/
│   ├── 00-index.md
│   │
│   ├── market/                       # 4 files ✓
│   │   ├── master-synthesis-market-analysis.md
│   │   ├── dental-market-paraguay-analysis.md
│   │   ├── mystery-shop-20-clinics-report.md
│   │   └── global-best-practices-dental-strategy.md
│   │
│   ├── pricing/                      # 2 files ✓
│   │   ├── international-dental-pricing-matrix.md
│   │   └── canonical-pricing-reference-v2.md
│   │
│   ├── legal-compliance/             # 4 files ✓
│   │   ├── regulatory/
│   │   │   ├── legal-framework-full-research.md
│   │   │   ├── mspbs-habilitation-requirements.md
│   │   │   ├── non-compete-contract-analysis.md
│   │   │   └── referral-network-legal-mapping.md
│   │   │
│   │   └── agreements/
│   │       ├── eas-registration-step-by-step.md
│   │       ├── eas-registration-verified-checklist.md
│   │       ├── habilitation-verified-checklist.md
│   │       ├── dentist-referral-agreement.md
│   │       └── invoice-template.md
│   │
│   ├── payments/                     # 2 files ✓
│   │   ├── payment-infrastructure-analysis.md
│   │   └── payment-systems-onboarding-guide.md
│   │
│   ├── locations/                    # 4 files ✓
│   │   ├── luque-rental-market-analysis.md
│   │   ├── luque-rental-market-verified.md
│   │   ├── phone-discovery-calls-report.md
│   │   └── phone-discovery-calls-verified.md
│   │
│   ├── community/                    # 3 files ✓
│   │   ├── expat-community-deep-dive.md
│   │   ├── patient-voice-of-customer-analysis.md
│   │   └── dental-tourism-opportunity-analysis.md
│   │
│   └── equipment/                    # 1 file ✓
│       └── dental-equipment-costs-suppliers.md
│
├── 02_MEETINGS/
│   ├── 00-index.md
│   ├── kiki-meeting/                 # 2 files ✓
│   │   ├── kiki-session-meeting-guide.md
│   │   └── kiki-decision-navigation-matrix.md
│   │
│   └── client-prep/                  # 3 files ✓
│       ├── roque-meeting/
│       │   ├── roque-meeting-results.md
│       │   ├── roque-negotiation-prep.md
│       │   └── luque-space-shortlist-3-priorities.md
│       │
│       ├── data-collection/
│       │   ├── client-data-collection-checklist.md
│       │   ├── patient-survey-instrument.md
│       │   └── patient-database-analysis.md
│       │
│       └── digital-systems/
│           ├── digital-systems-audit.md
│           ├── digital-systems-whatsapp-questions.md
│           └── client-personal-data-checklist.md
│
├── 03_LAUNCH/
│   ├── 00-index.md
│   │
│   ├── roadmap/                      # 4 files ✓
│   │   ├── master-launch-roadmap.md
│   │   ├── launch-day-by-day-sequence.md
│   │   ├── content-strategy-launch-phase.md
│   │   └── pre-launch-carrd-landing-page-guide.md
│   │
│   ├── institutional-sales/         # 5 files ✓
│   │   ├── institutional-sales-playbook.md
│   │   ├── institutional-precall-strategies.md
│   │   ├── institutional-lead-list-priority.md
│   │   ├── one-pager-hospitals.md
│   │   └── one-pager-schools.md
│   │
│   ├── corporate-sales/             # 4 files ✓
│   │   ├── corporate-sales-playbook.md
│   │   ├── corporate-dental-benefits-program.md
│   │   ├── one-pager-clubs.md
│   │   └── all-corporate-plans-index.md
│   │
│   ├── referral-program/            # 2 files ✓
│   │   ├── referral-program-plan.md
│   │   └── corporate-service-agreement-micro.md
│   │
│   ├── crm-systems/                  # 3 files ✓
│   │   ├── crm-system-implementation-plan.md
│   │   ├── financial-dashboard-spec.md
│   │   └── patient-intake-flow-design.md
│   │
│   ├── whatsapp-outreach/           # 3 files ✓
│   │   ├── whatsapp-business-plan.md
│   │   ├── whatsapp-ab-test-variants.md
│   │   └── multi-channel-outreach-strategy.md
│   │
│   └── website-content/             # 6 files ✓
│       ├── social-proof-trust-signals-content.md
│       ├── expat-landing-page-content.md
│       ├── when-not-to-treat-content.md
│       ├── blog-educational-content-plan.md
│       ├── first-visit-preparation-content.md
│       └── emergency-information-content.md
│
├── 04_SALES/
│   ├── 00-index.md
│   ├── corporate-service-agreement-full.md
│   └── institutional-referral-agreement.md
│
├── 05_OPERATIONS/
│   ├── 00-index.md
│   ├── operations-overview.md
│   │
│   ├── clinical-routines/            # 5 files ✓
│   │   ├── daily-weekly-monthly-routine.md
│   │   ├── first-patient-day-checklist.md
│   │   ├── emergency-procedures-protocol.md
│   │   ├── inventory-supply-chain-management.md
│   │   └── monthly-financial-tracker.md
│   │
│   ├── patient-communications/       # 4 files ✓
│   │   ├── patient-faq-20-answers.md
│   │   ├── patient-scripts-in-person-phone.md
│   │   ├── patient-welcome-packet.md
│   │   └── new-patient-intake-form.md
│   │
│   └── legal-compliance/            # 4 files ✓
│       ├── patient-legal/
│       │   ├── patient-informed-consent-form.md
│       │   ├── privacy-policy.md
│       │   ├── terms-of-service.md
│       │   └── patient-intake-form-legal.md
│       │
│       └── practice-legal/
│           ├── legal-master-checklist.md
│           ├── eas-registration-notarized-letter.md
│           ├── eas-company-statute.md
│           ├── referral-agreement-legal.md
│           └── corporate-service-agreement-micro-sme.md
│
├── 06_MARKETING/
│   ├── 00-index.md
│   ├── google-business-profile-setup-guide.md
│   └── website-full-specification.md
│
├── 07_DESIGN/
│   ├── 00-index.md
│   │
│   ├── brand-assets/                 # 6 files ✓
│   │   ├── business-card-design-spec.md
│   │   ├── letterhead-stationery-design-spec.md
│   │   ├── office-signage-design-spec.md
│   │   ├── price-list-card-design-spec.md
│   │   ├── social-media-profile-specs.md
│   │   └── qr-code-system-design.md
│   │
│   └── website/
│       ├── 00-index.md
│       ├── site-config.json
│       ├── core-pages/               # 4 files ✓
│       │   ├── home-page-content.md
│       │   ├── about-page-content.md
│       │   ├── contact-page-content.md
│       │   └── philosophy-page-content.md
│       │
│       ├── service-pages/            # 2 files ✓
│       │   ├── services-page-content.md
│       │   └── second-opinion-page-content.md
│       │
│       └── transactional-pages/      # 4 files ✓
│           ├── pricing-page-content.md
│           ├── privacy-page-content.md
│           ├── terms-page-content.md
│           └── first-visit-preparation-page.md
│
├── 08_WHATSAPP/
│   ├── 00-index.md
│   ├── whatsapp-operations-index.md
│   ├── whatsapp-operations-guide.md
│   ├── message-templates-library.md
│   ├── conversation-flows-automation.md
│   └── hermes-agent-whatsapp-protocol.md
│
├── 09_TEMPLATES/
│   ├── 00-index.md
│   ├── appointment-confirmation-card-template.md
│   ├── recall-card-template.md
│   ├── referral-card-template.md
│   └── email-templates.md
│
└── ARCHIVE/                          # Superseded versions
    ├── phone-mystery-shop-report.md
    ├── luque-rental-research.md
    └── eas-registration-walkthrough.md
```

---

## COMPLETE FOLDER AUDIT — MAX 6 RULE

| Folder | Count | Status |
|--------|-------|--------|
| `docs/` | 4 | ✅ |
| `docs/planning/` | 5 | ✅ |
| `00_STRATEGIC/strategic-context/` | 3 | ✅ |
| `00_STRATEGIC/financial-pricing/` | 6 | ✅ |
| `01_RESEARCH/market/` | 4 | ✅ |
| `01_RESEARCH/pricing/` | 2 | ✅ |
| `01_RESEARCH/legal-compliance/regulatory/` | 4 | ✅ |
| `01_RESEARCH/legal-compliance/agreements/` | 5 | ✅ |
| `01_RESEARCH/payments/` | 2 | ✅ |
| `01_RESEARCH/locations/` | 4 | ✅ |
| `01_RESEARCH/community/` | 3 | ✅ |
| `01_RESEARCH/equipment/` | 1 | ✅ |
| `02_MEETINGS/kiki-meeting/` | 2 | ✅ |
| `02_MEETINGS/client-prep/roque-meeting/` | 3 | ✅ |
| `02_MEETINGS/client-prep/data-collection/` | 3 | ✅ |
| `02_MEETINGS/client-prep/digital-systems/` | 3 | ✅ |
| `03_LAUNCH/roadmap/` | 4 | ✅ |
| `03_LAUNCH/institutional-sales/` | 5 | ✅ |
| `03_LAUNCH/corporate-sales/` | 4 | ✅ |
| `03_LAUNCH/referral-program/` | 2 | ✅ |
| `03_LAUNCH/crm-systems/` | 3 | ✅ |
| `03_LAUNCH/whatsapp-outreach/` | 3 | ✅ |
| `03_LAUNCH/website-content/` | 6 | ✅ |
| `04_SALES/` | 3 | ✅ |
| `05_OPERATIONS/clinical-routines/` | 5 | ✅ |
| `05_OPERATIONS/patient-communications/` | 4 | ✅ |
| `05_OPERATIONS/legal-compliance/patient-legal/` | 4 | ✅ |
| `05_OPERATIONS/legal-compliance/practice-legal/` | 5 | ✅ |
| `06_MARKETING/` | 3 | ✅ |
| `07_DESIGN/brand-assets/` | 6 | ✅ |
| `07_DESIGN/website/core-pages/` | 4 | ✅ |
| `07_DESIGN/website/service-pages/` | 2 | ✅ |
| `07_DESIGN/website/transactional-pages/` | 4 | ✅ |
| `08_WHATSAPP/` | 6 | ✅ |
| `09_TEMPLATES/` | 4 | ✅ |
| `ARCHIVE/` | 3 | ✅ |

**All folders ≤6. Zero violations.**

---

## NEW DEEPER NESTING LEVELS CREATED

| Parent | Child Subfolder | Depth |
|--------|-----------------|-------|
| `00_STRATEGIC/` | `strategic-context/`, `financial-pricing/` | 2 levels |
| `01_RESEARCH/legal-compliance/` | `regulatory/`, `agreements/` | 3 levels |
| `02_MEETINGS/client-prep/` | `roque-meeting/`, `data-collection/`, `digital-systems/` | 3 levels |
| `05_OPERATIONS/legal-compliance/` | `patient-legal/`, `practice-legal/` | 3 levels |
| `07_DESIGN/website/` | `core-pages/`, `service-pages/`, `transactional-pages/` | 3 levels |

---

## FILE COUNT BY DEPTH

| Depth | Folders |
|-------|---------|
| 1 (root level) | 10 top-level |
| 2 (e.g., `00_STRATEGIC/financial-pricing/`) | ~20 |
| 3 (e.g., `01_RESEARCH/legal-compliance/regulatory/`) | ~10 |
| **Total folders** | **~40** |

---

## ADDITIONAL IMPROVEMENTS INCORPORATED

All from `REORGANIZATION-ADDITIONAL-SUGGESTIONS.md`:
- ✅ `docs/` folder at root (CLAUDE.md, planning docs)
- ✅ 2-digit prefixes in subfolder names (01-, 02-, 03-)
- ✅ `ARCHIVE/` for superseded files
- ✅ `website-content/` moved to `07_DESIGN/website/` as subfolder (under website/ as content/)
- ✅ Consolidated `website-spec` into single file
- ✅ Merged COMPLETE-INDEX into README

---

## FILES TO DELETE

| Path | Reason |
|------|--------|
| `tee` | Artifact |
| `mkdir/` | Empty directory |
| `03_RESEARCH_EXTRAS/` | Redundant |
| All empty `00-index/` directories | 7 folders |
| All `output_*.txt` AI noise files | 30 files |
| `ARCHIVE/phone-mystery-shop-report.md` | Superseded by FRESH version |
| `ARCHIVE/luque-rental-research.md` | Superseded by FRESH version |
| `ARCHIVE/eas-registration-walkthrough.md` | Superseded by FRESH version |

**Total delete: ~40 items**

---

## NET RESULT

| Metric | Before | After |
|--------|--------|-------|
| Top-level folders | 10 | 10 |
| Total subfolders | ~7 | ~40 |
| Max files per folder | 32 (01_LAUNCH) | 6 |
| Root-level files | 10 | 2 (README + start-here) |
| Average folder size | ~17 files | ~3 files |