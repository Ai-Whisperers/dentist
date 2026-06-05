# DENTAL SOFTWARE LANDSCAPE — PARAGUAY (2026)
> AI research | June 2026 | Human trial + selection required

**Paraguay dental market** | Clinic management software comparison | Sources: Turnito, DenPro, Dentalink, AgendaPro, Dentidesk

---

## Purpose
Map the available practice-management software landscape so Dra. GP can
either integrate with existing DW/SAM or migrate to a platform that supports
WhatsApp, online booking, reminders, and compliance with Paraguayan law.

---

## Top 5 Platforms (ranked by PY fit)

### 1. Turnito App — Best for agenda + WhatsApp automation
- **Pricing**: Free plan for agenda only; premium = subscription or 5% commission
  on collected payments (no fixed cost if no payments). No hidden fees.
- **Key features**: WhatsApp + Telegram reminders (critical for PY no-show
  reduction), online booking 24/7, Google Meet teleconsult links, upfront
  deposits via MercadoPago / AstroPay / PayPal.
- **SET compliance**: Not built-in; basic invoicing only.
- **Clinical depth**: Low — no odontogram, no treatment plan builder. Agenda
  only, not full clinical record.
- **Best for**: Solo dentists who want no-show reduction + online booking fast.
- **Gap vs SAM**: No odontogram, no clinical history module. Would require
  parallel record-keeping in SAM for clinical depth.

### 2. DenPro — Best for local compliance + clinical module
- **Pricing**: Basic ₲ 199,000/mo (~USD 25); Team ₲ 299,000/mo (~USD 38).
  15% annual discount. No setup fees.
- **Key features**: SET Factura Electrónica integration (unique), RUC
  management, odontograma digital FDI, historia clínica digital compliant
  with Ley 1682/01, SMS + WhatsApp reminders, prescriptions.
- **SET compliance**: Built-in — this is the strongest PY compliance story.
- **Clinical depth**: Medium — odontogram, histories, prescriptions, basic
  scheduling. No advanced implant planning.
- **Best for**: Clinics that need SET compliance + clinical record in one tool
  + no heavy admin overhead.
- **Gap vs SAM**: Would require migrating SAM data out; SAM-specific custom
  fields may not transfer cleanly. Data migration support offered (1–3 days).

### 3. Dentalink — Best for multi-specialty / groups
- **Pricing**: Esencial ~USD 29/mo; Pro and Titanium = custom quote.
- **Key features**: 45M+ appointments managed/year across 20+ countries,
  advanced 3D odontogram, patient education 3D viewer, orthodontics module,
  facial esthetics, multi-locale billing, payroll/commissions.
- **SET compliance**: Not built-in for PY specifically; primarily LATAM
  regional billing.
- **Clinical depth**: High — deep specialty modules, charting, imaging, videos.
- **Best for**: Multi-doctor clinics, specialist-heavy practices, ortho +
  esthetics.
- **Gap vs SAM**: Overkill for solo practice; cost unknown beyond basic; SET
  gap would require custom invoice bridge.

### 4. AgendaPro — Best for marketing + CRM
- **Pricing**: Custom quote; 14-day trial. Not listed publicly.
- **Key features**: CRM, email marketing, satisfaction surveys, POS/caja,
  inventory control, commission tracking, online booking.
- **SET compliance**: Unknown.
- **Clinical depth**: Low-to-medium — not dental-native.
- **Best for**: Clinics whose main pain is patient retention + marketing.
- **Gap vs SAM**: Weak clinical module; overkill if you only need reminders.

### 5. Dentidesk — Best for extreme clinical depth / inventory control
- **Pricing**: Lite ~USD 100/yr; regular ~USD 50/mo.
- **Key features**: Specialized modules (endo, perio, ortho, orthognathic),
  desktop app (Mac/Windows), detailed medical history, inventory tracking.
- **SET compliance**: Unknown.
- **Clinical depth**: Highest in the list.
- **Best for**: Specialist clinics or solo practitioners who want deep records.
- **Gap vs SAM**: No WhatsApp depth, no SET integration.

---

## Side-by-Side Comparison

| Criterion | Turnito | DenPro | Dentalink | AgendaPro | Dentidesk |
|-----------|---------|--------|-----------|-----------|-----------|
| PY native | High | Very high | Medium | Low | Low |
| SET invoice integration | ❌ | ✅ | ❌ | ? | ? |
| Odontogram | ❌ | ✅ | ✅ (3D) | ❌ | ✅ |
| WhatsApp reminders | ✅ | ✅ | Unknown | ❌ | ❌ |
| Online booking | ✅ | ✅ | ✅ | ✅ | ✅ |
| Teleconsult | ✅ | ❌ | ✅ | ❌ | ❌ |
| Payment collection | ✅ | ❌ | ? | ❌ | ❌ |
| Customer support | Chat | Email + chat | Regional | Email | Email |
| Price (solo starter) | Free/0% | ₲199K/mo | $29/mo | Custom | ~$8/mo |

---

## Data Migration Considerations (if switching from SAM)

- SAM contract terms must be reviewed — can data be exported?
- Field mapping: SAM clinical notes → new system's schema
- Historical data Jan-May 2026 (601 appointments, 342 patients) as baseline
- Patient communication: mass message explaining switch + opt-in
- Downtime: expect 1–2 days for import validation

---

## Recommended Path for Dra. GP

### Phase 0 (current)
- Continue using SAM for clinical records (already in use, compliance assumed)
- Layer Turnito on top for online booking + WhatsApp reminders (free to start)

### Phase 1 (if SAM confirms API)
- Build WhatsApp bot calling SAM directly — no software change
- Grey area: SAM-assistant manual entry sufficient until booking volume
  justifies integration cost

### Phase 2 (migration trigger)
- Only switch if: (a) SAM contract prohibits API use; (b) SAM is being
  sunset; (c) SAM billing/SET integration is missing and creating admin cost
- Recommended destination: **DenPro** (PY compliance + clinical depth)
  or **Dentalink** if practice grows to 2+ dentists

---

## Doctoralia PRO — PY Pricing Assessment

From public sources (Doctoralia AR pricing, Jun 2026):

| Plan | ARS/mo (annual) | USD equiv | Features |
|------|-----------------|-----------|----------|
| Starter | 18,000 ARS | ~$18 | Online booking, email reminders, SMS (300/mo), basic profile |
| Plus | 22,000 ARS | ~$22 | + electronic records, SMS reminders, teleconsult |
| VIP | 30,000 ARS | ~$30 | + profile design, waitlist, mass ops, 5000 SMS/mo |

Add-ons: Página web profesional 4,000 ARS/mo (~$4).

**PY market inference**: Doctoralia PY likely follows similar regional pricing.
At ~USD 18–30/mo, it is cheaper than Turnito commission model at scale.
The "Página web" add-on is irrelevant for Dra. GP (own website coming).

**Recommendation**: Skip Doctoralia until GBP is dominant and international
patients ask for it. The WHOLE directory positioning advantage is weak in PY
where GBP is the actual local discovery layer. Add it only as channel #3.

---

## Human Tasks

| Task | Why |
|------|-----|
| Sign up for Turnito free trial + test booking flow | Hands-on validation |
| Call DenPro sales: "Can DenPro import SAM data?" | Migration decision gate |
| Ask SAM support: API? export format? contract restrictions | Integration path |
| Ask IPEO / Risus: "What dental software do you use?" | Competitive benchmark |
| Trial Dentalink for 14-day comparison if DenPro seems wrong fit | Validation |

---

*Research: denpro.com.py, turnito.app, dentalink.com, agendapro.com,
dentidesk.com, turnito.app/blog (comparative ranking), pro.doctoralia.com.*
