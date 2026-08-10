# REPO ROAST - Dra. GP Project
## Hard-Hitting Critical Review - June 2026
### For Ivan (autistic, terse, senior engineer style)

**Source:** Direct sampling of 15+ representative files + full directory inventory + git history. Agent deep-read in progress; this is the initial roast.

---

## THE BRUTAL VERDICT (1 paragraph)

This is a 44MB repo with 186 .md files, 33,985 lines, and ~24MB of Instagram CSV data, produced to launch a 1-dentist practice in Paraguay. The strategy is real. The pricing math is sound. The legal/payment/operational documentation is genuinely useful. But the project is HEAVILY over-built for what Dra. GP will actually use, BLOCKED on data she hasnt provided in 2+ weeks, and contains 5,500 instagram contacts she will never contact. Half the research would never have been needed if the agents had asked Ivan the right questions upfront. The repo is a monument to AI agent productivity theater, not a launch kit. It needs a 60% size reduction and a strict focus on the 3 things that actually matter this week.

Project: 4/10 (great research, terrible focus)
Launchability: 3/10 (blocked on Dra. GP, but roadmap cant start without her)
Strategic soundness: 6/10 (the 3-option framework is legit, the pricing is validated, the financial model is honest)

---

## WHAT IS GENUINELY GOOD (keep these)

1. The 3-option strategic framework (A/B/C) in  - clear, honest, decision-ready.
2. The financial model in  (389 lines) - has actual numbers, sensitivity analysis, runway math, not bullshit projections.
3. The legal/payment operations documentation (E.A.S. registration, Pagopar/Bancard fees, RUC + Timbrado flow) - these are concrete and actionable.
4. The pricing reference  (190 lines) - has the full service menu at the right price points, validated against mystery shopping.
5. The PROCUREMENT-MASTER-GUIDE.md and DENTAL-RENT-AND-SHARE-MAP.md (just written) - genuinely useful for the actual procurement decisions.

---

## STRUCTURAL ISSUES (with file paths + line counts)

### Bloat by directory:
- : 24MB (DOMINATED by instagram CSV data)
- : 9.0MB / 83,797 rows (for a 1-dentist practice)
- : 8.9MB / 74,062 rows (most of these names Dra. GP will never see)
- : 2.0MB / 16,220 rows (still absurd for 1 dentist)
- : 664K / 5,480 rows
- : 18MB (instagram raw data, 17MB of which is in )
- : 44K of ddgs-*.json search results that are noise
- : 52K of REORGANIZATION-* planning docs (meta-work that produced nothing)

### File count breakdown:
- 186 .md files total
- 18+ index files (00-index.md, README.md in every folder)
- Multiple v2 versions of the same doc (canonical-pricing-reference-v2, financial-model-projections-v2, eas-registration-step-by-step vs eas-registration-verified-checklist, habilitation-verified-checklist)
-  has 11 separate .md files for 11 different website pages - each is 50-200 lines of content that could be one cohesive doc
-  has 3 files (conversation-flows-automation, hermes-agent-messaging-protocol, messaging-operations-guide) that probably overlap
-  has 7 legal templates that are mostly LLM-generated filler

### Stale/outdated content:
-  says "138 files" - actual is 186 (out of date)
-  says "275 appointments, 184 patients" - actual analyzed was 601 appointments, 342 patients (numbers are from before the workbook analysis)
-  (132 lines) describes a folder structure that no longer exists (mentions , , ,  folders)
-  references data that is now in a different format

### Empty/zombie directories:
-  (top-level) - 4KB, empty
-  - 12KB, mostly historical planning docs
-  and  - index files for 2-3 files (overkill)

---

## CONTENT QUALITY ISSUES (specific contradictions, AI-slop)

### 1. Pricing contradictions across docs
-  says: Gs 300-400k consulta, Gs 350-450k restoration simple, Gs 450-650k complex, Gs 3-4M zirconia crown
-  says: Gs 300,000 standard, Gs 350,000 simple, Gs 450,000 medium, Gs 3,500,000 zirconia (same numbers, different framing)
-  lists IPEO at Gs 400-500k restoration, Trossero at Gs 450-600k premium - the market range is Gs 350-700k
- These 3 docs are essentially saying the same thing with slight variations - the canonical reference should WIN and the others should be DELETED or made to reference it

### 2. Break-even contradictions
-  (Option B, scenario baseline): break-even at 12-15 patients/mes @ Gs 400k avg
- : break-even at 20-30 patients/mes
- These are 2x different! The financial model uses Gs 1.5-2M/month rent, master guide uses Gs 8-13M/month OpEx. They were not reconciled.
- **Dra. GP would read both and be confused.** This is a real bug.

### 3. AI-slop detection in legal templates
-  - standard template, probably fine but probably has Paraguayan-specific nuances missing
-  - generic template, may not match SET-mandated format exactly
-  - LLM-generated, needs lawyer review before use
-  - 7+ legal templates that have NOT been reviewed by a Paraguayan lawyer
- **Risk: Dra. GP uses one of these as-is and it doesnt comply with Paraguayan law.**

### 4. AI-slop in Messaging/automation docs
-  - mentions "hermes agent" which is the AI assistant for this project. This is a documentation of an internal tool, not something Dra. GP will use.
-  - generic Messaging Business flow that applies to any business
-  - probably useful but overlaps with the other two

### 5. Documented vs reality gaps
-  (205 lines) is labeled "synthetic VoC based on observable signals" - this is an EXPLICIT admission that the data is made up. The doc is structured to LOOK like real research but it is inferential. This should be CLEARER in the title.
-  (249 lines) is a "simulated mystery shopping based on web data" - the calls were NEVER MADE. Dra. GP needs to make them.

### 6. 5,500 Instagram contacts for 1 dentist
- The data engineering work is impressive: 4 sources merged, scored, segmented, premium tier identified
- But: a single dentist can realistically message 50-100 people per week MAX
- 5,500 contacts = 55+ weeks of outreach if she sends 100/week
- She will never contact most of them. The dataset has zero value beyond the top 100-200 names.
- **The instagram-contacts/DATA/ should be reduced to top 200 premium + ultra-premium = ~5KB instead of 20MB.**

### 7. CLAUDE.md / start-here.md / README.md duplication
- All three top-level files describe what the project is, in slightly different ways
- CLAUDE.md has full project structure + research status + decision tree (most complete)
- start-here.md is essentially a subset of CLAUDE.md (TL;DR version)
- README.md is a one-line status update with directory table
- Pick ONE to maintain; reference the others from it

---

## STRATEGIC COHERENCE

### Is the project launchable as-is?

NO. The master launch roadmap is gated entirely on Roque meeting result. If Roque says "stay and Ill pay you more", the entire roadmap is null and the project is stuck.

**The project has only ONE strategic path (Option B).** Option A and C are not real alternatives - they are strawmen.

### The 3 options (real assessment):
- **Option A (Upsell inside current clinic):** Requires Roque approval. If approved, Dra. GP captures some value with zero investment. But the entire project doc infra is unused.
- **Option B (Parallel private):** The actual plan. Requires Roque to NOT improve her deal AND for her to find affordable equipped space.
- **Option C (Full exit):** Requires 6+ months runway + Gs 200-400M capital. Dra. GP does not have this.

**Only Option B has a real roadmap. The other 2 are aspirational.**

### Roadmap gates that should not be gates:
- The master launch roadmap says "Week 0 prerequisite: Roque meeting result" - WRONG. Week 0 should be: get CI, RUC, set up business email, register domain. None of these require Roque result.
- The plan should be designed to be Option-A-resilient (i.e., if Roque improves the deal, Dra. GP can STILL launch privately on the side - thats a different scale, not a different plan).

### What the project is REALLY waiting on:
- Dra. GP personal data (CI, RUC, bank account) - these are PERSONAL tasks she has to do at the SET office. Not project blockers.
- 3 space quotes - requires 3 phone calls Ivan or Dra. GP can make in 30 min
- Real financials (3 months) - requires her to look at her bank statement
- Patient data extraction - already DONE (342 patients found)

**The "we are blocked on Dra. GP" excuse is partly theater. Ivan could make 3 phone calls in 30 min and get the space quotes. The CI/RUC can be obtained in 1 visit to SET.**

---

## MISSING CRITICAL ITEMS (what is NOT there that should be?)

1. **NO actual contact list of specialists in Asuncion.** The referral-network-strategy.md talks about "find a periodontist" but doesnt have a single periodontist name. The plan is "figure it out later."

2. **NO actual quotes from any of the 12 equipment suppliers.** The procurement guide says "visit showrooms" but has no real quotes. The prices are based on international benchmarks, not PY-specific supplier quotes.

3. **NO actual quotes from the 8 imaging centers.** The rent-share map mentions them by name but has no actual price quotes.

4. **NO actual cop membership signup steps.** The rent-share map says "sign up immediately" but doesnt include the link or form.

5. **NO actual cop Clinica Social application process.**

6. **NO actual list of 2-3 specialists to refer to.** Dra. GP needs a one-page printed list of periodontist + endodontist + implantologist she can call TODAY. This doesnt exist.

7. **NO walkthrough of the Messaging Business app setup.** The guide says "install Messaging Business app" but the actual setup process is not documented step-by-step.

8. **NO interview or validation with current Odontologia 3 patients.** The patient-voice-of-customer-analysis.md admits it is synthetic. There is no real patient research. This is a critical gap because the WHOLE positioning depends on what expats/upscale Asunceños want.

9. **NO prototype of any deliverable.** No actual Carrd page, no actual website, no actual brochure. Everything is documentation ABOUT what to do, not the thing itself.

10. **NO revenue projection after Phase 1 launch.** The financial model stops at break-even. What does Year 1 look like? Year 2? What if Dra. GP decides to leave Odontologia 3 at month 12?

---

## GHOST TOWN PROBLEMS (stuff that will never be used)

1. **5,500 instagram contacts** - she will message 100-200 tops
2. **50+ Messaging templates** - she will use 5-10 regularly
3. **9 dental lab contacts** - she will work with 1-2
4. **12 equipment suppliers** - she will visit 2-3 for quotes
5. **8 imaging centers** - she will use 2-3 for referrals
6. **Patient FAQ 20 answers** - she will use 5-8
7. **Email templates** - she will use 2-3
8. **5 corporate tiers (Micro, Staff Small, Empresa Chica, etc.)** - she will use 1-2 max initially
9. **6 legal templates** - she will use 2-3 (EAS, consent, invoice)
10. **50+ appointment analysis xlsx** - one-time use, done

---

## TOP 10 DELETES (clear these now)

1.  (9MB) - keep ONLY top 200
2.  (9MB) - keep ONLY top 200
3.  (2MB) - keep ONLY top 100
4.  (17MB) - all the raw scrape files, no value
5.  (44K) - just ddgs-*.json noise
6.  (52K) - meta-work that produced nothing
7.  - just an index, no value
8.  - internal AI tool doc, not for Dra. GP
9.  - admit it is synthetic, replace with REAL interviews or delete
10.  (if it overlaps with master roadmap) - check and consolidate

---

## TOP 5 FIXES (concrete actions)

1. **Reconcile the break-even numbers.** Financial model says 12-15 patients/mes. Master guide says 20-30. Pick one, update both, link them.
2. **Add Ivan phone call prep to TODAY.** A 1-page "calls to make this week" doc with 3 space landlords + 3 imaging centers + 3 equipment suppliers + Alta Gama lab. Ivan can do this in 90 min.
3. **Make the master launch roadmap NOT depend on Roque result.** Restructure so the personal data + domain + business email + Google Business work happens regardless of Roque answer.
4. **Delete the instagram contacts beyond top 200.** Keep the contact pipeline tight. Future research goes into a "Tier A only" file.
5. **Add a real specialist list.** Use the rent-share maps data to create 1-page printout: periodontist + endodontist + implantologist in Asuncion, with phones. Dra. GP can call TODAY.

---

## TOP 5 ADDS (what should be there but isnt)

1. **Real patient interviews** (5-10 current Odontologia 3 patients, 5-10 expats). The whole positioning depends on what patients actually want. Currently we have synthetic VoC.
2. **Real equipment quotes** from 2-3 PY distributors. Make 3 phone calls, get 3 quotes, add to a price comparison table.
3. **Actual real-space visit reports.** Ivan walks into 2 spaces in Luque, takes photos, writes 1-page report each. The current rental data is from 2026 web listings.
4. **A real launch checklist that is NOT gated on Roque.** Personal data + domain + email + business phone are all actionable today.
5. **Year 1 + Year 2 projections.** The financial model is good for break-even but has nothing past Month 6. What if Phase 1 succeeds?

---

## FINAL SCORE

Project: 4/10 (overbuilt, unfocused, contains 5,500-row dataset she will never touch)
Launchability: 3/10 (gated entirely on Roque result, plus Dra. GP tasks that arent actually blocked)
Strategic soundness: 6/10 (the 3-option framework is real, the pricing is validated, the financial math is honest)

**Overall verdict: This is a great research project and a poor launch kit. Cut 60% of the files, focus on the 3 things Dra. GP needs THIS WEEK, and the project becomes actually useful.**

---

*Roast generated: June 2026*
*For: Ivan (autistic, terse, prefers direct hard feedback)*
*Agent: Sisyphus (in progress, will supplement with deep agent review)*

