> **PRICING CROSS-REFERENCE:** All prices reference `00_STRATEGIC/financial-pricing/canonical-pricing-reference-v2.md` unless explicitly noted.

# CORPORATE SALES TRACKER — SCHEMA & FIELD GUIDE
## `corporate-sales-tracker.xlsx` companion
**File:** `03_LAUNCH/corporate-sales/outreach/corporate-sales-tracker.xlsx`
**Generated:** June 5, 2026

---

## PURPOSE

This file is the **operating system** for B2B corporate dental outreach. It is structured to be used by Ivan or Dra. GP without explanation. Sheets are divided into **pipeline** (what to do now) and **reference** (static source data).

---

## SHEET MAP

| Sheet | Type | Use |
|-------|------|-----|
| `Gym-Spa Outreach` | Pipeline | Active deals: companies to contact + follow |
| `Premium Outreach` | Pipeline | A-tier premium leads for immediate outreach |
| `Gym-Spa Leads` | Source | Full gym/spa universe (638) |
| `Premium Leads` | Source | Full premium universe (326) |
| `Stage Definitions` | Reference | Pipeline stage glossary |
| `Message Templates` | Reference | Outbound message copy |

---

## FIELD DICTIONARY

### Gym-Spa Outreach

| Column | Description | Validation | Example |
|--------|-------------|------------|---------|
| # | Row sequence, 1..N | Int, unique | 1 |
| Company | Display name from source leads | Required | Global Fitness Paraguay |
| Category | Gym/General/Spa split for halo choice | Enum: Gimnasio/Fitness, Spa/Wellness | Spa/Wellness |
| City | Geography for territory routing | Enum: Asunción, Luque | Asunción |
| Phone | WhatsApp-capable number | Max 20 chars | 0981 205329 |
| Stage | Forward-only state | Stage Definitions enum | Prospecting |

### Premium Outreach

| Column | Description | Validation | Example |
|--------|-------------|------------|---------|
| # | Row sequence, 1..N | Int | 1 |
| Company | Display name | Required | Crecer Inmobiliaria |
| Category | Business vertical | Free text | inmobiliaria |
| City | City | Free text / null | |
| Phone | Direct line | Free text | (021) 338 1199 |
| Website | URL | URL | http://www.crecer.com.py/ |
| Rating | Google Maps rating | Float 1..5 | 4.8 |
| Reviews | Review count | Int >= 0 | 297 |
| Score | Corporate fit score | Int 0..100 | 80 |

### Gym-Spa Leads / Premium Leads

Treat these sheets as **read-only**. Do not edit by hand. They are generated from the scrape/analysis pipeline in `03_LAUNCH/corporate-sales/leads/`.

---

## PIPELINE RULES

1. **Stage transitions are one-way forward.** Once a company moves from `Prospecting` → `Contacted`, do not revert.
2. **Last contact date** is implicit from tracker edits; for full audit, log into `outreach-tracker.md` per row.
3. **Copy rows** from source sheets into the Outreach sheet, then move them forward as the deal progresses.

---

## WORKFLOW (Day-Use)

### Daily workflow for outreach agent

1. Open `Gym-Spa Outreach` and `Premium Outreach`.
2. Filter by `Stage = Prospecting`.
3. For each row:
   - Send first contact via WhatsApp (or LinkedIn for premium).
   - Update `Stage`, `Phone` check.
4. If response:
   - Move to `Interested` or `Meeting Scheduled`.
5. If no response after 3 days:
   - Send follow-up (from Message Templates).
   - Add row to `outreach-tracker.md`.

### Conversion targets

| Metric | Target |
|--------|--------|
| Contacted → Interested | 15-20% |
| Interested → Meeting Scheduled | 40% |
| Meeting Scheduled → Proposal Sent | 60% |
| Proposal Sent → Closed | 25% |

---

## MESSAGE TEMPLATES MAP

| Template name | Source sheet | Best channel |
|---------------|--------------|--------------|
| INITIAL CONTACT (Gym/Spa) | Message Templates | WhatsApp |
| FOLLOW-UP (if no response after 3 days) | Message Templates | WhatsApp |
| SECOND OPINION outreach | whatsapp-operations-guide.md | WhatsApp |

For channel-specific objection handling, see `08_WHATSAPP/templates/objection-library.md`.

---

## AUDIT NOTES (2026-06-05)

- `Gym-Spa Outreach` currently shows `Stage = Prospecting` for all listed companies. Outreach has not started.
- `Premium Outreach` top 7 are Tier-A leads from `premium-leads.csv`. Expand as leads are processed.
- Hidden fields exist in source sheets (`deep_score`, `priority`, `corporate_score`) but are not surfaced in outreach views by design.
- All price references inside this workbook should follow canonical pricing via `00_STRATEGIC/financial-pricing/canonical-pricing-reference-v2.md`.

---

## MAINTENANCE cadence

- Weekly: move completed follow-ups to higher stage; add new week's prospects.
- Monthly: audit scoring thresholds in source sheets (`Gym-Spa Leads`, `Premium Leads`) against outreach performance.
