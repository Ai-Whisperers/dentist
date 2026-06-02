# FINANCIAL TRACKER — MONTHLY
## Dra. Gabriella González Pane
**Version:** 1.0 — June 2026

---

## PURPOSE

Track revenue, expenses, and net income monthly. Know if the practice is sustainable and growing.

---

## SETUP

Create a Google Sheet named "DraGP — Financials"

Tabs:
1. Monthly Tracker
2. Annual Summary
3. Patient Revenue Log

---

## TAB 1: MONTHLY TRACKER

### Header Row (Row 1)
| | A | B | C | D | E | F | G | H | I | J | K | L | M |
|---|------|------|------|------|------|------|------|------|------|------|------|------|------|

### Column Headers (Row 2)
| Month | Revenue | # Patients | Avg Ticket | OpEx | Rent | Supplies | Marketing | Admin | Utilities | Net | vs Last Month | Cumulative |

### Data Rows (Starting Row 3)
Fill in each month:

| Month | Revenue | # Patients | Avg Ticket | OpEx | Rent | Supplies | Marketing | Admin | Utilities | Net | vs Last Month | Cumulative |
|-------|---------|-----------|-----------|------|------|----------|-----------|-------|---------|-----|--------------|------------|

### Formulas
- **Avg Ticket**: =Revenue/# Patients
- **Net**: =Revenue - OpEx
- **vs Last Month**: =(This Month - Last Month)/Last Month
- **Cumulative**: =Running sum of Net

---

## TAB 2: ANNUAL SUMMARY

### Header Row
| | A | B | C | D | E | F | G | H | I | J | K |
|---|---|---|---|---|---|---|---|---|---|---|---|

### Column Headers
| | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec | TOTAL |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

### Data Rows
| Revenue | | | | | | | | | | | | | SUM |
| OpEx | | | | | | | | | | | | | SUM |
| Net | | | | | | | | | | | | | SUM |

### Year-End Summary
- Total Revenue: SUM
- Total OpEx: SUM
- Total Net: SUM
- Best Month: MAX(Net)
- Worst Month: MIN(Net)
- Avg Monthly Net: AVERAGE(Net)

---

## TAB 3: PATIENT REVENUE LOG

### Every patient payment logged here

| Date | Patient Name | Service | Amount | Payment Method | Invoice # | Notes |
|------|--------------|---------|--------|---------------|------------|-------|
| 2026-06-15 | María González | Restauración complex | Gs 485,000 | Pagopar 6x | 001-001-00001 | |
| 2026-06-15 | Juan Pérez | Second Opinion | Gs 400,000 | Cash | 001-001-00002 | |

### Monthly Total Formula
=SUMIF(A:A,">=2026-06-01",D:D) - SUMIF(A:A,">2026-06-30",D:D)

---

## WHAT TO LOG EVERY MONTH

### Revenue (inflow)
| Source | What to log |
|--------|-------------|
| Patient payments (cash) | Date, name, amount, service |
| Patient payments (card/Pagopar) | Same + payment method |
| Patient payments (transfer) | Same + bank reference |
| Referral credits used | Date, name, amount credited |
| Any other income | Date, source, amount |

### Expenses (outflow)
| Category | What to log |
|----------|-------------|
| Rent | Monthly amount, which space |
| Supplies (dental materials) | Date, vendor, amount, what bought |
| Equipment maintenance | Date, equipment, amount |
| Marketing | Date, what (Google ads, printing, etc.) |
| Admin (accountant, software) | Date, what, amount |
| Utilities (if separate) | Phone, internet, electricity if office separate |
| Timbrado/ SET | Annual cost, amortized monthly |
| COP membership | Annual cost, amortized monthly |
| Hermes agent | Monthly cost if using API |

---

## MONTHLY FINANCIAL REVIEW CHECKLIST

### Every Month End:
1. [ ] Log all patient revenues in Tab 3
2. [ ] Total revenue from Tab 3 = should match Tab 1
3. [ ] Log all expenses in Tab 1
4. [ ] Calculate Net = Revenue - OpEx
5. [ ] Compare to last month — what's the trend?
6. [ ] Is Net positive? (Revenue > OpEx)
7. [ ] Do we have enough runway? (Cash / Monthly OpEx)
8. [ ] Any anomalies? (Revenue spike/drop, unusual expense)

### Questions to Ask Monthly:
1. Did revenue grow vs last month?
2. Is OpEx under control?
3. Are we hitting our revenue target?
4. Is the practice cash-flow positive?
5. Do we need to adjust pricing?
6. Do we need to reduce OpEx?

---

## RUNWAY CALCULATION

Simple: Cash in bank ÷ Monthly OpEx = Months of runway

Example:
- Cash: Gs 10,000,000
- Monthly OpEx: Gs 2,000,000
- Runway: 10M / 2M = 5 months

**Minimum runway target: 6 months**
**Target for security: 12 months**

---

## PRICING VERIFICATION (Monthly)

After each month, check:

| Metric | Current | Target |
|--------|---------|---------|
| Avg ticket | Gs X | > Gs 400,000 |
| % revenue from second opinions | X% | > 20% |
| % revenue from restorations | X% | < 50% |
| % revenue from referrals | X% | > 30% |

---

## FINANCIAL TARGETS

### Minimum Viable (Break-even)
- Revenue: Gs 2,500,000/month
- Patients: 8-10/month
- Avg ticket: Gs 300,000

### Healthy Practice
- Revenue: Gs 5,000,000/month
- Patients: 15-20/month
- Avg ticket: Gs 350,000

### Thriving Practice
- Revenue: Gs 10,000,000/month
- Patients: 25-30/month
- Avg ticket: Gs 400,000+

---

## CASH FLOW RULES

1. **Never spend revenue before you have it** — wait for payment to clear
2. **Keep 3 months OpEx in reserve** — don't spend it
3. **Reinvest profits until runway is 12 months** — then take profit
4. **Track every expense** — no matter how small
5. **Reconcile monthly** — bank statement vs. your log

---

## TIMING

| When | What |
|------|------|
| Daily | Log patient payments in Tab 3 |
| Weekly | Check cash flow — any unusual payments? |
| Monthly (last day) | Close out month — total revenue, expenses, net |
| Monthly (first day) | Review previous month, plan this month |

---

**STATUS:** Ready to use. Start logging from Day 1 of first patient.