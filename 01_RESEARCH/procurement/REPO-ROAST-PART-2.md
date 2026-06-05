# REPO ROAST PART 2 - More Critical Findings
## Continuation of REPO-ROAST-JUNE-2026.md

**Source:** Deep read of strategic options, decision matrix, corporate program, WhatsApp templates, dental tourism analysis.

---

## CRITICAL FINDING #1: The Decision Rule Will Never Fire

The Kiki decision matrix (lines 231-234) says:

**THE ONE-SENTENCE DECISION RULE:**
"If Roque didnt offer real improvement AND space is available at Gs 3M/mo or less: START OPTION B THIS WEEK."

BUT the procurement data shows:
- Only ONE truly equipped space in the project: San Lorenzo at Gs 3M/mes (DOUBLE the threshold)
- All other verified Luque options are BARE (no equipment) at Gs 1.65M-4M
- Almate (shared revenue) exists but has unknown cost structure

**The decision rule was written before the procurement research was done. The threshold (Gs 3M) was a hope, not a fact.**

**Implication:** Option B CANNOT start this week even if Roque said no, because no space meets the criteria. The decision rule needs to be re-written to Gs 3M threshold OR a different space needs to be found.

**This is a real bug that no agent caught.** It would only surface when Dra. GP actually tried to act on the decision rule.

---

## CRITICAL FINDING #2: The 3-Option Framework Contradicts Itself

three-strategic-options-analysis.md (lines 142-148) recommends:
- **Fase 1: Validar con Opcion A**
- **Fase 2: Escalar a Opcion B**
- **Fase 3: Evaluar Opcion C**

BUT the actual execution docs (master launch roadmap, financial model) are entirely about Option B. Option A is mentioned but no plan exists. Option C is not built out.

**Two different stories about what to do. The strategic doc says "start with A, escalate to B". The execution doc says "go straight to B".**

Recommendation: Update the strategic options doc to match the actual execution plan, OR build out the Option A plan that the strategic doc recommends.

---

## CRITICAL FINDING #3: The Corporate B2B Math Does Not Pencil Out

corporate-dental-benefits-program.md proposes 3 tiers:
- Tier 1 (5-20 employees): Gs 150,000/employee/month
- Tier 2 (21-100): Gs 130,000/employee/month
- Tier 3 (100+): Gs 110,000/employee/month

**Per-service economics for Tier 1 (Empresa Chica):**
- 5 employees x Gs 150,000 = Gs 750,000/month revenue
- Services provided per year: 5 x (2 consult + 4 checkups + 1 cleaning) = 35 services
- Gs 9M annual / 35 services = Gs 257,000 per service
- Subtract: Dra. GP chair cost, materials, lab, time, WhatsApp comms
- **NET per service is probably Gs 50-100k. Total annual NET: Gs 1.75-3.5M. Not enough.**

The corporate model is marketed as a Gs 50M/month opportunity, but the per-service economics make this impossible for small/medium companies. Only the largest 100+ employee companies (Tier 3) might approach profitability per service, and even then the company pays LESS per employee.

**Implication:** The corporate program should be reframed as a SUPPLEMENT to individual patient revenue, not a primary channel. The financial projections in the doc are misleading.

---

## CRITICAL FINDING #4: 50+ WhatsApp Templates for an Agent That Does Not Exist

message-templates-library.md (681 lines, 50+ templates) is organized for the "Hermes agent" to use:
"The Hermes agent selects the appropriate template based on message classification."
"Agent NEVER improvises. If a situation is not covered here, agent escalates to Dra. GP."

**The Hermes agent does not exist.** This is internal AI tooling documentation, not customer-facing material. Dra. GP (a human) will use maybe 5-10 templates, not 50. The 681 lines of templates are LLM-generated filler organized for a build that will not happen in the next 12 months.

**Recommendation: Strip the file to 5-10 essential templates. Delete the agent framework language. Make it usable for a human.**

---

## CRITICAL FINDING #5: The Corporate Program Requires a B2B Sales Team

The corporate program requires:
- Outreach to 964 leads (638 gym/spa + 326 premium)
- Discovery calls (30-60 min each)
- Proposals within 48 hours
- Contract negotiation (12-month minimum)
- Quarterly utilization reports to HR
- On-site health screening days (1x/year per company)
- Dedicated WhatsApp contact for HR

**For 1 dentist working evenings (2-3 sessions/week), this is operationally impossible.** A solo dentist can do B2B SALES for 5-10 hours per week MAX. That is 1-2 discovery calls per week, 1-2 proposals per week, 1 close per week at best. 5 corporate clients takes months.

**The corporate program is designed for a 3-person dental operation with a dedicated B2B sales person. Dra. GP does not have that.**

**Recommendation: Either (a) reduce scope to "1 corporate client in Year 1, no B2B team needed" or (b) hire a part-time B2B person OR (c) delete the entire program.**

---

## CRITICAL FINDING #6: The Corporate Tracker Has Stale Data

corporate-sales/README.md says "54 companies tracked with stage, contact, response" in the Excel tracker.
**But the tracker was likely generated by a previous AI agent and the data is from that agents work, not from real outreach.**

**Risk:** If Dra. GP opens the Excel and starts cold-calling from it, she will be calling companies that have been called before (or that dont exist) - a real credibility risk.

**Recommendation: Verify the tracker data. Start fresh outreach with a small, focused list.**

---

## CRITICAL FINDING #7: dental-tourism-opportunity-analysis.md is Excellent but Has Strategic Conflict

The dental tourism doc (163 lines) is one of the BEST docs in the project:
- Real competitor analysis (5 specific clinics named)
- Real expat community data (specific Facebook groups cited)
- Specific referral channel inventory (InterNations, embassies, medical tourism aggregators)
- Real market gap identified (no one owns "ethical + bilingual + planning")
- Concrete recommendations

BUT: it also recommends "Medical tourism agency outreach" and "Embassy connections" which are the same high-friction B2B channel that the rest of the project cant support.

**The content is great. The scope is unrealistic for 1 dentist.** This doc should be edited to focus on the LOW-FRICTION tactics:
- Facebook group presence (free, 30 min/week)
- expatsettle.com listing (free or cheap)
- YouTube video content (medium effort, high SEO value)
- USD pricing page (1 afternoon to build)
- Patient referral program (organic, low cost)

Cut the high-friction items: medical tourism agencies, embassy formalization.

---

## MORE BLOAT IDENTIFIED (with line counts)

| File | Lines | Issue |
|------|------:|-------|
| 08_WHATSAPP/templates/message-templates-library.md | 681 | 50+ templates for non-existent agent |
| 03_LAUNCH/corporate-sales/programs/corporate-dental-benefits-program.md | 422 | B2B program for solo dentist |
| 02_MEETINGS/kiki-meeting/kiki-decision-navigation-matrix.md | 298 | Decision rule threshold (3M) contradicts research (3M actual) |
| 00_STRATEGIC/strategic-context/three-strategic-options-analysis.md | 159 | Recommends "start with A, escalate to B" but execution doc is only B |
| 06_MARKETING/website-full-specification.md | 450+ | 7-page spec for website that hasnt been built |
| 08_WHATSAPP/automation/hermes-agent-whatsapp-protocol.md | 384 | Internal AI tooling, not for Dra. GP |
| 08_WHATSAPP/automation/conversation-flows-automation.md | 418 | 50-state automation for dentist without WhatsApp Business yet |
| 08_WHATSAPP/automation/whatsapp-operations-guide.md | 350+ | Operations guide for product not yet deployed |
| 09_TEMPLATES/email-templates.md | 368 | Generic email templates |
| 05_OPERATIONS/patient-communications/patient-faq-20-answers.md | 250+ | 20 FAQs for 0 patients |

Total: ~3,500+ lines of "preparation theater" that Dra. GP will never use.

---

## CONTRADICTIONS NOT YET DOCUMENTED (Part 2)

### Per-procedure pricing contradictions:
| Procedure | canonical-pricing | financial-model | kiki-decision-matrix | corporate-program |
|-----------|-------------------|-----------------|---------------------|-------------------|
| Consulta general | Gs 300,000 | Gs 300-400k | Gs 300-400k | Gs 280-300k (corporate) |
| Second opinion | Gs 450,000 | Gs 400-600k | Gs 400-600k | n/a (bundled in tier) |
| Simple restoration | Gs 350,000 | Gs 350-450k | Gs 350-450k | Gs 280-400k (corporate) |
| Complex restoration | Gs 550,000 | Gs 450-650k | Gs 450-650k | Gs 280-400k (corporate) |
| Cleaning | Gs 280,000 | Gs 350-450k | n/a | Gs 200-250k (corporate) |

Three different prices for the SAME service across FOUR documents. The canonical-pricing-reference is the designated master but nobody follows it.

### Break-even patient count contradictions:
| Document | Break-even | Calculation basis |
|----------|-----------|-------------------|
| financial-model-projections-v2.md line 112 | 12-15 patients/mes | Assumes Gs 1.5-2M rent |
| kiki-decision-navigation-matrix.md line 128 | 12-15 patients/mes | Same as financial model |
| PROCUREMENT-MASTER-GUIDE.md (just written) | 20-30 patients/mes | Uses Gs 8-13M OpEx |
| DENTAL-RENT-AND-SHARE-MAP.md (just written) | 20-30 patients/mes | Uses Gs 8-13M OpEx |

Two numbers (12-15 vs 20-30) - the newer procurement docs are CORRECT because they use the actual OpEx from the procurement research. The financial model and decision matrix are STALE because they were written before the procurement research was complete.

**Action: Update financial-model-projections-v2.md and kiki-decision-navigation-matrix.md to use 20-30 patients/mes break-even (consistent with actual OpEx data).**

### Other less-egregious contradictions:
- Equipment recommendations in 2 files: dental-equipment-costs-suppliers.md (line 59) says "portable equipment for Phase 1 rented space" but Phase 1 is renting EQUIPPED space - no equipment needed. Doc is written for a future state.
- Phasing in 3 files: three-strategic-options says "Phase 1 = A, Phase 2 = B, Phase 3 = C"; master-launch-roadmap says "Phase 1 = B (parallel private)"; financial-model says "Phase 3 = full exit". Three different phasing.
- Habilitación timeline: eas-registration-step-by-step says 30-60 days; mspbs-habilitation-requirements says 30-60 days. CONSISTENT here.
- Cop membership: 01_RESEARCH/procurement/DENTAL-RENT-AND-SHARE-MAP.md says Gs 400,000/year. No other doc mentions COP membership cost. CONSISTENT but missing from other docs.

---

## MISSING CRITICAL ITEMS (Part 2)

1. **No prototype of any deliverable.** No actual Carrd page, no actual brochure, no actual email template that has been used. Everything is documentation ABOUT what to do.

2. **No decision between the strategic-options phased approach vs. the master-roadmap direct-to-B approach.** Two stories.

3. **No update mechanism for the placeholder files.** roque-meeting-results.md, luque-space-shortlist-3-priorities.md, client-data-collection-checklist.md are empty/placeholder. They will stay that way until Dra. GP actually does the work.

4. **No accountability for the corporate program.** Who runs the B2B outreach? Dra. GP alone? When? 5-10 hours per week? This is unaddressed.

5. **No measurement framework.** Which KPIs matter? How often reviewed? What triggers a pivot? The TODO.md has "Metrics a seguir" section but it is not connected to the actual plan execution.

6. **No legal review of the legal templates.** The 7 templates in 05_OPERATIONS/legal-compliance/practice-legal/ have NOT been reviewed by a Paraguayan lawyer. If Dra. GP uses them as-is, she could be exposed to legal issues.

7. **No backup plan if Roque fires her for planning to leave.** The Kiki decision matrix mentions this scenario in a table but does not detail what the response should be.

8. **No budget for the marketing launch.** The financial model has monthly OpEx but no launch marketing budget. Facebook/Instagram ads, Google Business setup, Carrd Pro, etc. are all separate costs.

---

## GHOST TOWN PROBLEM EXPANDED (Part 2)

Items that look like real work but will not be used:

1. **50+ WhatsApp templates** (681 lines) - Dra. GP will use 5-10, not 50
2. **20-question patient FAQ** (250+ lines) - she has 0 patients asking questions yet
3. **5 corporate tiers pricing schedule** (Micro, Staff Small, Empresa Chica, Empresa Mediana, Empresa Grande) - 5 tiers for 1 dentist who will sign 1-2 corporate clients max in Year 1
4. **3 corporate tier brochure specs** (clubs, schools, hospitals one-pagers) - 3 different institutional sales materials for channels that will get 0 time in Year 1
5. **Dental tourism analysis** - 163 lines for a market that requires embassy connections and medical tourism agency partnerships (unrealistic scope)
6. **Hospital O.R. rental research** - one paragraph, never used
7. **Multi-channel outreach strategy** (12k bytes) - WhatsApp + email + Instagram + Facebook + LinkedIn + Google + 5 corporate tiers. 7+ channels for 1 dentist.
8. **20 landing page content files** in 03_LAUNCH/website-content/ - the website hasnt been built. These are 20+ content drafts that will need to be re-edited when the actual site is built.
9. **11 separate website page content files** in 07_DESIGN/website/ - same as above, redundant with 03_LAUNCH/website-content/
10. **9 WhatsApp/Instagram outreach trackers and templates** - for 1 dentist who will use 1 channel for 1 type of patient outreach.

Total ghost-town content: ~3,000+ lines of LLM-generated text that will be re-edited or never used.

---

## TOP 5 DELETES (PART 2)

1.  (681 lines) - 50 templates for non-existent agent
2.  (3 files, ~1,150 lines) - internal AI tooling, not for Dra. GP
3.  (422 lines) - B2B program requiring sales team
4.  (368 lines) - generic email templates, not Paraguay-specific
5.  (250+ lines) - 20 FAQs for 0 patients

**Combined savings: ~3,000 lines + significant bloat**

---

## TOP 5 FIXES (PART 2)

1. **Reconcile the 3 break-even numbers.** Pick 20-30 patients/mes (procurement data). Update financial model + decision matrix. This is a 5-minute fix.

2. **Reconcile the 4 different per-service prices.** Pick canonical-pricing-reference. Update financial model + corporate program + WhatsApp templates. This is a 30-minute fix.

3. **Fix the decision rule.** "If Roque didnt offer real improvement AND space is available at Gs 3M/mo or less: START OPTION B THIS WEEK." Update to reflect actual procurement data.

4. **Reconcile the 2 phasing strategies.** Three-strategic-options says "start with A, escalate to B". Master-roadmap says "go to B". Pick one. Update the loser.

5. **Decide on the corporate program scope.** Either (a) commit 5-10 hrs/week for 6 months to sign 3-5 corporate clients, or (b) delete the program. The current state is "comprehensive B2B playbook for someone who will not execute it."

---

## THE PROFOUND ISSUE: AI AGENT PRODUCTIVITY THEATER

**Most of this project is a monument to AI agent productivity.**

Over the past 2+ weeks, AI agents have produced:
- 186 .md files
- 33,985 lines
- 44MB+ of data
- 50+ WhatsApp templates
- 5,500 Instagram contacts
- 964 corporate leads
- 19 dental lab contacts
- 12 equipment suppliers
- 8 imaging centers
- 9 legal templates

**What the agents have NOT produced:**
- 1 real phone call made to a landlord
- 1 real Carrd page built
- 1 real email sent to a corporate prospect
- 1 real legal review
- 1 actual contact added to the corporate tracker
- 1 piece of placeholder data filled in (roque-meeting-results.md is still empty)

**The agents are optimizing for "looking complete" not for "actually launching".** This is the AI-slop equivalent of work: it produces artifacts that look like work but do not move the needle.

**Fix: make the agents do work, not produce documentation about work. Make them make phone calls, build pages, send emails, fill placeholder docs.**

---

## WHAT IS GENUINELY GOOD (Part 2)

1. **kiki-decision-navigation-matrix.md** (298 lines) - has the right structure, scenarios, decision logic. Just needs the Gs 3M threshold updated to Gs 3M.

2. **dental-tourism-opportunity-analysis.md** (163 lines) - real competitor data, real channels, real market gap. Just needs scope reduction to low-friction tactics.

3. **The DENTAL-RENT-AND-SHARE-MAP.md (just written)** - genuinely useful. Will be used in actual procurement decisions.

4. **The PROCUREMENT-MASTER-GUIDE.md (just written)** - with proper caveats about lab pricing, this is the best document in the project for actual decision-making.

5. **The financial-model-projections-v2.md structure** - has sensitivity analysis, runway math, scenarios. Just needs numbers calibrated to actual OpEx.

---

## ADJUSTED SCORES (after Part 2)

| Dimension | Part 1 | Part 2 | Notes |
|-----------|-------:|-------:|-------|
| Comprehensiveness | 4/10 | 3/10 | Even more bloat identified |
| Launchability | 2/10 | 2/10 | Decision rule contradiction makes it un-launchable as-is |
| Strategic soundness | 5/10 | 4/10 | 3-option framework contradicts execution, B2B program is fantasy |
| Content quality | 5/10 | 4/10 | Multiple pricing contradictions, 4 different prices per service |
| Bloat ratio | 2/10 | 1/10 | Even worse than Part 1 - 3,000 more lines of ghost-town content |
| **Overall** | **3.5/10** | **2.8/10** | **Actually worse after deeper review** |

---

## THE HARD TRUTH FOR IVAN

**If you do nothing else this week, do these 3 things:**

1. **Open the financial model, find the break-even calc, and fix the 12-15 vs 20-30 inconsistency.** 5 minutes.

2. **Open the kiki decision matrix, find the Gs 3M threshold, and change to Gs 3M.** 2 minutes. (Or actually call Roque.)

3. **Make 3 phone calls: San Lorenzo + 2 backup landlords. Get 3 real quotes. Fill in the placeholder file.** 30 minutes.

**Then delete 50% of the files in this repo. The project will be more useful with less, not more.**

---

*Roast Part 2 generated: June 2026*
*For: Ivan (autistic, terse, prefers direct hard feedback)*
*Agent: Sisyphus + background critic agent*

