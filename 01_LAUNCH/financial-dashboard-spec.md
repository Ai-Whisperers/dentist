# FINANCIAL DASHBOARD SPEC
## Dra. GP - Visual Google Sheets Dashboard
**Version:** 1.0 - June 2026

---

## PURPOSE

A visual Google Sheets dashboard that shows at a glance:
- Revenue trend (is it growing or declining?)
- Patient volume by source (where are patients coming from?)
- Average ticket (are we hitting target?)
- Runway (how many months can we survive?)

One look to know if the practice is healthy.

---

## SETUP: CREATE THE SHEET

1. Create new Google Sheet named "DraGP - Dashboard"
2. Create these tabs:
- Monthly Tracker (main data entry)
- Dashboard (visual overview)
- Revenue Log (all patient payments)
- Annual Summary (12-month view)

---

## TAB 1: MONTHLY TRACKER (Data Entry)

COLUMN HEADERS (Row 2):
Month | Revenue | # Patients | Avg Ticket | OpEx | Rent | Supplies | Marketing | Admin | Net | vs Last Month | Cumulative

DATA ROWS (starting row 3):
Each month fill in:
- Revenue (from Revenue Log tab)
- # Patients (count from Revenue Log)
- Avg Ticket = Revenue / # Patients
- OpEx = sum of expenses below
- Rent = monthly rent payment
- Supplies = dental materials, supplies
- Marketing = ads, printing, etc.
- Admin = accountant, software, misc
- Net = Revenue - OpEx
- vs Last Month = (This - Last) / Last
- Cumulative = running sum of Net

PRE-FILL FORMULAS:
- Avg Ticket: =B3/C3
- Net: =B3-E3
- vs Last Month: =(B3-B2)/B2
- Cumulative: =D3+D2

SAMPLE DATA (copy this structure):
Jun 2026 | 5,200,000 | 14 | 371,429 | 2,200,000 | 1,500,000 | 350,000 | 100,000 | 250,000 | 3,000,000 | +15% | 3,000,000

---

## TAB 2: DASHBOARD (Visual Overview)

SETUP: Use IMPORTANGE to pull from Monthly Tracker

CREATE THESE CHARTS:

CHART 1: Revenue Trend (Line Chart)
- Data range: Monthly Tracker A:B (Month + Revenue)
- Title: "Monthly Revenue"
- Show last 6 months

CHART 2: Patient Volume (Column Chart)
- Data range: Monthly Tracker A:C (Month + # Patients)
- Title: "Patients per Month"

CHART 3: Revenue vs Expenses (Combo Chart)
- Data range: Monthly Tracker A:B:E (Month + Revenue + OpEx)
- Title: "Revenue vs Expenses"

CHART 4: Avg Ticket Over Time (Line Chart)
- Data range: Monthly Tracker A:D (Month + Avg Ticket)
- Title: "Average Ticket Trend"
- Reference line at Gs 400,000 (target)

TEXT SUMMARY (update monthly manually or with formulas):

LAST MONTH SUMMARY:
- Revenue: [FROM MONTHLY TRACKER]
- Patients: [FROM MONTHLY TRACKER]
- Avg Ticket: [FROM MONTHLY TRACKER]
- Net: [FROM MONTHLY TRACKER]
- Runway: [Cash / Monthly OpEx] months

KEY METRICS TO TRACK:

| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| Revenue | [VALUE] | > Gs 5M/mo | [GREEN/YELLOW/RED] |
| Patients | [VALUE] | > 15/mo | [GREEN/YELLOW/RED] |
| Avg Ticket | [VALUE] | > Gs 400k | [GREEN/YELLOW/RED] |
| Net | [VALUE] | > Gs 2M/mo | [GREEN/YELLOW/RED] |
| Runway | [VALUE] | > 6 months | [GREEN/YELLOW/RED] |

CONDITIONAL FORMATTING:
- Revenue > 5M = GREEN
- Revenue 3-5M = YELLOW
- Revenue < 3M = RED

---

---

## TAB 3: REVENUE LOG (Detailed Entry)

Every patient payment logged here.

COLUMN HEADERS (Row 2):
Date | Patient Name | Service | Amount (Gs) | Payment Method | Invoice # | Source | Notes

SOURCES (for tracking where patients come from):
- whatsapp_direct
- referral
- corporate
- institutional
- expat_forum
- google_maps
- other

This is the detailed record. Monthly Tracker pulls from here.

---

## TAB 4: ANNUAL SUMMARY

See financial-tracker.md for full annual summary structure.

---

## GOOGLE SHEETS TIPS

- Use COLOR CODE for sources:
  - whatsapp = blue
  - referral = green
  - corporate = orange
  - institutional = purple
  - expat = teal
- Sort revenue log by date (newest first)
- Use filter views for patient lookup
- Share with accountant (read-only)

---

## FINANCIAL TARGETS (Reference)

MINIMUM (Break-even):
- Revenue: Gs 2.5M/month
- Patients: 8-10/month
- Avg Ticket: Gs 300,000

HEALTHY:
- Revenue: Gs 5M/month
- Patients: 15-20/month
- Avg Ticket: Gs 350,000

THRIVING:
- Revenue: Gs 10M/month
- Patients: 25-30/month
- Avg Ticket: Gs 400,000+

---

**Created:** June 2, 2026
