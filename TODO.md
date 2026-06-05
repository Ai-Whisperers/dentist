# TODO

**Última actualización:** June 5, 2026 — P2 directory cleanup

## P2 Content Alignment & Completion

### P2.1 Pricing table completeness ✅ COMPLETE
- [x] Canonical services cross-checked across consumer-facing docs
- [x] Consumer docs verified: start-here.md, roadmap, website content, corporate program

### P2.2 Phase 0 checklist — actionable for Dra. GP ✅ COMPLETE
- [x] README/start-here/REPO-WORK-PLAN adjusted to reflect latest directory structure
- [x] Key files referenced in `02_MEETINGS/` corrected: archive paths/status aligned in place

### P2.3 Patient journey specs ✅ COMPLETE
- `05_OPERATIONS/patient-communications/patient-journeys.md` complete; 3 de-identified journeys with template cross-refs per touchpoint

### P2.4 Competitor battle cards ✅ COMPLETE
- Top 3 battle cards added: `01_RESEARCH/market/battle-cards/battle-card-iPeo.md`, `battle-card-dra-boccia.md`, `battle-card-clinica-codas.md`

### P2.5 Objection library ✅ COMPLETE
- `08_WHATSAPP/templates/objection-library.md` created; 20 objections with WhatsApp/phone/in-person templates

### P2.6 Corporate sales tracker hygiene ✅ COMPLETE
- `03_LAUNCH/corporate-sales/outreach/corporate-sales-tracker-schema.md` documents all sheets + field rules + workflow

### P2.7 3-Option reconciliation ✅ COMPLETE
- Single source in `00_STRATEGIC/strategic-context/three-strategic-options-analysis.md`; `master-launch-roadmap.md` defers to it

---

## P3 Operational Readiness

### P3 Tools & CI ✅ COMPLETE
- [x] `tools/repo-audit.py` with summary/stale/crossrefs/prices/sizes/all
- [x] `tools/update-pricing.py` dry-run scaffold
- [x] Pre-commit hook: `.git/hooks/pre-commit` stale-check
- [x] CI workflow: `.github/workflows/repo-validation.yml`

---

## P4 Client Delivery Artifacts
- [x] `docs/dra-gp-status-june-2026.md` — one-pager status (P4.1)
- [x] `docs/phase-0-binder.md` — printable Phase 0 bundle (P4.2)
- [x] `docs/investor-summary.md` — investor summary from financial-model-projections-v2 (P4.3)

---

### P5 Growth / Next Phase ✅ COMPLETE
- `docs/sitemap-manifest.md` → build manifest from `07_DESIGN/website/` (P5.1)
- `05_OPERATIONS/service-standard/sla-doc.md` → corporate SLA 1-pager (P5.2)
- `00_STRATEGIC/financial-pricing/multi-location-scenario.md` → Option C financial scenario (P5.3)

---

## BLOCKERS / OPEN QUESTIONS

| Pregunta | Status | Respuesta Needed |
|----------|--------|------------------|
| ¿Roque result (Option A viable)? | ❓ Pendiente | Reunión Roque + contrato |
| ¿Base de datos puede usarse para contactar? | ❓ Abogado | Consulta legal |
| ¿Non-compete en contrato Odontología 3? | ❓ Roque | Leer contrato |
| ¿Cuántos pacientes premium-eligible? | ❓ Dra. GP | Data extraction |
| ¿3 Luque quotes reales? | ❓ Pendiente | Visitar espacios |
| ¿6+ meses runway? | ❓ Finanzas reales | Balance 3 meses |

---

**STATUS ACTUAL:** P0–P2 complete. Repo limpio, auditoría finalizada, pricing block validado, placeholders inventariados. Siguiente hito: P3 (tooling/CI) y P2.6 (corporate sales tracker schema).