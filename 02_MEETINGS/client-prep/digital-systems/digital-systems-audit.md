# Digital Systems Audit — Dra. GP
**Purpose:** Capture requirements for new patient-facing digital systems
**Context:** SAM is her current practice management software (DOS-era, Windows, internal website). Patient portal and new systems NOT YET decided.
**Status:** Questions sent to Dra. GP — awaiting response
**Version:** 1.0 — June 2026

---

## WHAT WE KNOW

| Item | Detail |
|------|--------|
| Current software | SAM |
| Type | Practice management — internal website (doctors only) |
| Platform | Windows (latest) |
| Data export | Can export some data — details pending |
| Patient portal | None |
| Patient-facing features | None |
| SAM limitations | No patient portal, no online access, no notifications |

---

## INTERVIEW GUIDE — Questions by Category

Send via WhatsApp in groups of 3-5 questions per message.

---

### GROUP 1: What SAM Does Well
**Why:** Identify features any new system MUST replicate.

1. What do you **love** about SAM? (Things you'd lose your mind if a new system didn't do)

2. List everything SAM currently tracks or manages:
   - Patient records / charts?
   - Appointments / scheduling?
   - Billing / invoicing (SET timbrado)?
   - Treatment plans / clinical notes?
   - Radiographs / imaging?
   - Patient history timeline?
   - Insurance / seguro processing?
   - Anything else?

3. Does SAM generate invoices with SET timbrado automatically, or do you do that separately?

---

### GROUP 2: SAM Pain Points
**Why:** Every hate is a requirement for the new system.

4. What do you **hate** about SAM? (Slow, confusing, breaks, missing features — be specific)

5. What's missing that you do manually today? (e.g., "I track appointment reminders in my head", "I send x-rays via WhatsApp because SAM can't")

6. Is there something you want to SHOW patients but can't in SAM? (e.g., "I want to show them their x-ray progression but SAM doesn't display it well")

7. Does SAM ever lose data or crash? Has it ever lost patient records?

---

### GROUP 3: Patient Communication Today
**Why:** Determine what patient communication flows need to be automated or replaced.

8. How do you remind patients of upcoming appointments? (WhatsApp, phone call, SMS, nothing)

9. When an appointment changes or is delayed, how do you notify patients?

10. Do patients ever ask to see their treatment history or plan? How do you handle it?

11. Do you send post-appointment instructions or follow-up reminders? How?

12. When a patient has a question between appointments, how do they reach you? (WhatsApp, phone, walk-in)

---

### GROUP 4: SAM Technical Details
**Why:** Determine what data can be migrated and how.

13. How many patients are currently in SAM? (rough estimate: 100 / 500 / 2,000+)

14. Can SAM export patient data to Excel or CSV? (just the list — names, phones, appointment history)

15. Can SAM export or backup its full database? What's the format?

16. Does SAM have an API? (Can other systems connect to it automatically?)

17. Who installed SAM? Is there a support company? Can they help export data if needed?

18. What Windows version does it run on? (Windows 10? 11? Does she run it on her regular computer or a dedicated machine?)

---

### GROUP 5: Patient Portal Ideas
**Why:** Understand what she'd actually use — avoid building things she won't.

19. If patients could access ONE thing online, what would be most valuable?
   - See their treatment plan and history?
   - Book appointments online (with your approval)?
   - Receive automatic appointment reminders?
   - See their x-rays or photos?
   - Pay invoices online?
   - Something else?

20. What should patients **NEVER** be able to do online? (e.g., "I don't want them booking without confirming with me first")

21. Would you want patients to be able to send you messages or photos between appointments? Through what channel?

22. Would you want patients to fill out intake forms online before their first visit?

---

### GROUP 6: Her Vision
**Why:** Understand what success looks like for her.

23. In 2 years, what does a "perfect" digital experience look like for you and your patients?

24. What's the one thing that would save you the most time in your workday?

25. What data or insight do you wish you had about your patients that you don't have today? (e.g., "I have no idea how many patients come back for follow-ups")

---

## NOTES FOR FOLLOW-UP

| Topic | Status |
|-------|--------|
| SAM data export | Pending — she'll pass it when she can |
| SAM API | Unknown |
| Patient volume in SAM | Pending |
| Current appointment reminder flow | Pending |

---

## AFTER SHE RESPONDS

Compare her answers against:
- What SAM already does → replicate
- What she hates → must fix
- What's missing → must build
- What she loves → sacred, don't break

Then write a prioritized feature list for Phase 1 vs Phase 2 of the digital system.
