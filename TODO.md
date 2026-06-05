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

### P2.4 Competitor battle cards ⏸️ PENDING
- Source: `01_RESEARCH/market/mystery-shop-20-clinics-report.md`
- Top 3 competitors — one-pager each

### P2.5 Objection library ⏸️ PENDING
- Source: `08_WHATSAPP/flows/` + meeting notes
- 20 objections with reply templates per channel

### P2.6 Corporate sales tracker hygiene ⏸️ PENDING
- xlsx tracker structure documented in companion `.md`
- Action: `03_LAUNCH/corporate-sales/outreach/outreach-tracker.md` → schema companion

### P2.7 3-Option reconciliation ⏸️ PENDING
- Unify Option A/B/C definitions across:
  - `00_STRATEGIC/strategic-context/three-strategic-options-analysis.md`
  - `03_LAUNCH/roadmap/master-launch-roadmap.md`

---

## P3 Operational Readiness

### P3 Tools & CI
- [x] `tools/repo-audit.py` provided: `summary`, `counts`, `stale`, `crossrefs`, `sizes`
- [x] `tools/validate-refs.py` provided: `links`, `stale`, `prices`, `all`
- [x] Validation confirmed: 0 stale, 0 broken links
- [ ] Pre-commit hook wiring (manual step: configure Git hook if needed)
- [ ] CI workflow for automated checks on push

---

## P4 Client Delivery Artifacts
- [ ] `docs/dra-gp-status-june-2026.md` — one-pager status (P4.1)
- [ ] `docs/phase-0-binder.md` — printable Phase 0 bundle (P4.2)
- [ ] Investor summary 1-pager from financial-model-projections-v2 (P4.3)

---

## P5 Growth / Next Phase
- [ ] Sitemap → build manifest from `07_DESIGN/website/` (P5.1)
- [ ] Corporate sales SLA doc 1-pager (P5.2)
- [ ] Multi-location financial scenario extension (P5.3)

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