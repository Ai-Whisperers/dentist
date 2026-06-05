## PRICING CROSS-REFERENCE (June 2026)

> Service prices in this document are NOT authoritative. The master reference is:
> `00_STRATEGIC/financial-pricing/canonical-pricing-reference-v2.md`
>
> Any price update should happen in the canonical file only.

---

# CRM SYSTEM DESIGN
## Dra. Gabriella González Pane
**Phase:** Planning (not building)
**Version:** 1.0 — June 2026

---

## PURPOSE

Track every person who contacts Dra. GP, from first inquiry through booking, treatment, and referral. No patient data stored — just the sales pipeline and referral tracking.

**Why CRM matters at this stage:**
- She currently tracks nothing systematically
- Every lead that goes untracked is potential revenue lost
- Referral program needs to track who sends who
- Need to know what's generating inquiries to optimize

---

## WHAT THIS CRM IS NOT

- NOT a clinical EHR/system (keep patient records separate, in whatever system she uses at Odontología 3)
- NOT an appointment scheduling system (that lives in her personal calendar for now)
- NOT a marketing automation platform

---

## PIPELINE STAGES

Every prospect goes through these stages:

```
[New Inquiry]
    ↓
[Responded — Awaiting Response]
    ↓
[Appointment Scheduled] ←→ [Not Yet Scheduled]
    ↓
[Attended Consultation]
    ↓
[Planning/Treatment In Progress]
    ↓
[Completed — Satisfied]
    ↓
[Ongoing Care / Recall]
```

---

## PROSPECT TYPES

| Source | Description | How to Tag |
|--------|-------------|------------|
| `direct_search` | Found her via Google Search | Tag: organic |
| `google_maps` | Found her via Google Maps | Tag: maps |
| `whatsapp_direct` | Messaged directly on WhatsApp | Tag: whatsapp |
| `referred` | Sent by an existing patient | Tag: referral_(name) |
| `specialist` | Referred by specialist | Tag: specialist_(name) |
| `expat_forum` | Found via expat group | Tag: expat |
| `instagram` | From Instagram (if she posts) | Tag: instagram |
| `cold_start` | Doesn't remember how they found her | Tag: unknown |

---

## DATA TO COLLECT PER CONTACT

### Minimum (Launch)
| Field | Type | Example |
|-------|------|---------|
| Name | Text | María González |
| First contact date | Date | 2026-06-10 |
| Source | Tag | whatsapp_direct |
| Referred by | Text | (blank or Dra. Sofía) |
| Last contact date | Date | 2026-06-12 |
| Last message summary | Text | " Asked about pricing. Sent quote for second opinion." |
| Status | Stage | responded_awaiting |
| Next action | Date + Text | "Follow up June 15 if no response" |
| Appointments scheduled | Count | 1 |
| Appointments attended | Count | 0 |
| Treatments completed | Count | 0 |
| Revenue generated | Number | 0 |

### Once treated (add):
| Field | Type | Example |
|-------|------|---------|
| Treatment type | Text | Second opinion + restoration |
| Total revenue | Number | Gs 550,000 |
| Payment method | Tag | pagopar_12x / cash / bancard |
| Last visit | Date | 2026-07-03 |
| Next recall | Date | 2027-01-03 |

---

## TOOL OPTIONS

### Option 1: Google Sheets (Free, Launch)
**Pros:** Zero cost, accessible from any device, no setup, familiar interface
**Cons:** Manual, no automation, limited visibility

**Structure:**
- Sheet 1: Pipeline (all prospects, sorted by status)
- Sheet 2: Referrals (who referred whom, outcomes)
- Sheet 3: Monthly metrics (inquiries, conversions, revenue)

### Option 2: Notion (Free, Launch+)
**Pros:** More structured, visual board view, relational, better for scaling
**Cons:** Slightly more setup time

**Structure:**
- Database: All contacts
- Properties: Name, Source, Status, Last Contact, Referred By
- Board view: Kanban by pipeline stage
- Calendar view: follow-up dates

### Option 3: Airtable (Free tier, Scale)
**Pros:** Most powerful, form integration, collaboration
**Cons:** Learning curve, overkill at launch

---

## RECOMMENDATION

**Launch with Google Sheets.** Simple, no learning curve, she can move to Notion when it feels limiting.

Template structure below.

---

## GOOGLE SHEETS TEMPLATE STRUCTURE

### Tab 1: Pipeline

| Date | Name | Phone | Source | Referred By | Last Contact | Summary | Stage | Next Action | Appts Scheduled | Appts Attended | Treatments Done | Revenue |
|------|------|-------|--------|-------------|--------------|---------|-------|-------------|-----------------|----------------|-----------------|---------|

**Status options:**
- `new` — new inquiry, not yet responded
- `responded_awaiting` — responded, waiting for reply
- `not_interested` — decided not to proceed
- `appoint_scheduled` — has an appointment booked
- `attended` — came in for consultation
- `treated` — completed treatment
- `ongoing` — in active treatment/recall care

### Tab 1: Pipeline — Companies (add for corporate accounts)

| Date | Company | Contact | Phone | Headcount | Tier | Stage | Source | Monthly Fee | Contract Start | Notes |
|------|---------|---------|-------|-----------|------|-------|--------|-------------|----------------|-------|

**Source options:**
- `Individual` — individual patient
- `Corporate` — company via B2B program
- `Institutional` — school, club, association
- `Expat` — expat community referral
- `Referral` — patient referral
- `Google` — via Google Search/Maps

### Tab 2: Referrals

| Date | Referrer Name | Referred Person | Source | Outcome | Discount Given |
|------|---------------|-----------------|--------|---------|----------------|

### Tab 3: Monthly Metrics (calculated from pipeline)

| Month | New Inquiries | Responded | Appts Scheduled | Appts Attended | Treatments | Revenue | Referrals Sent |
|-------|---------------|-----------|-----------------|----------------|------------|---------|----------------|

This auto-calculates from the pipeline with simple formulas.

---

## ACTIVITY TRACKING LOG (within pipeline)

For each interaction with a prospect, add a row in a separate Log tab:

| Date | Contact Name | Action | Notes |
|------|--------------|--------|----|
| 2026-06-10 | María González | Initial message | Asked about second opinion pricing |
| 2026-06-12 | María González | Follow-up sent | Sent detailed pricing + offered appointment |
| 2026-06-15 | María González | Appointment booked | June 20 at 10am |

This prevents lost context when following up weeks later.

---

## AUTOMATIC REMINDERS

Manual reminders for now. Use phone calendar to remind:
- If no response in 48h after first contact → follow-up message
- If appointment scheduled → reminder 24h before
- If patient completed treatment → follow-up 1 week after
- If recall due (e.g., cleaning every 6 months) → send WhatsApp when due

**Forward-looking automation (Phase 2):**
Notion can send reminders automatically. Google Calendar + Slack notification can do this. But manual is fine at launch.

---

## INSIGHTS TO TRACK MONTHLY

What she should review once a month:

1. **Where are inquiries coming from?** (Which source tag appears most)
2. **What's the response rate?** (How many of new inquiries got a response)
3. **What's the booking rate?** (How many responded → scheduled appointment)
4. **What's the show rate?** (How many scheduled → actually attended)
5. **What's the conversion rate?** (How many attended → completed treatment)
6. **What's the referral rate?** (How many treated patients referred someone)
7. **Revenue per patient** (Average revenue from completed treatment)
8. **Revenue per source** (Which channel produces the most revenue)

---

## REFERRAL PROGRAM TRACKING

Special attention for referrals:

| Referrer | Number of Referrals | Outcome | Discounts Given | Value Generated |
|----------|--------------------|---------|-----------------|----------------|

When a referral comes in:
1. Ask "How did you hear about me?" (if not already stated)
2. Tag the new person with `referral_[referrer name]`
3. Add row to Referrals tab
4. If referral completes treatment → send referrer a thank-you + small discount on next visit (Gs 100k or equivalent)

---

## WHAT HAPPENS WHEN SHE'S AT CAPACITY

If she's fully booked 3+ weeks out:
- Add a `waitlist` status in pipeline
- When she cancels a regularly-scheduled patient and the slot frees up
- Alert waitlisted patients in order of inquiry date
- Document waitlist position and reason for interest
- Use this data to justify expanding hours or days if recurring

---

## DATA BACKUP

- Google Sheets auto-saves to Google Drive
- Download as CSV monthly as physical backup
- Copy to local drive on personal computer

---

## PRIVACY AND SECURITY

IMPORTANT: This CRM should never contain:
- Patient clinical data (diagnoses, X-rays, treatment details)
- ID numbers or national IDs
- Insurance information

It's a sales and operations tool, not a medical record system. Keep those separate.

---

## IMPLEMENTATION CHECKLIST

- [ ] Create Google Account if not already for business
- [ ] Create Google Sheet named "DraGP Pipeline"
- [ ] Set up three tabs: Pipeline, Referrals, Metrics
- [ ] Add column headers per specification above
- [ ] Create first test entry (fake contact)
- [ ] Test sorting and filtering
- [ ] Add shortcut to phone home screen for quick access
- [ ] Review with Dra. GP — train on how to use
- [ ] Establish habit: enter every inquiry within 24h

---

**STATUS:** Planning complete. Ready for implementation documentation. Google Sheets can be created in under 1 hour.
