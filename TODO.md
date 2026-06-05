# TODO — Dra. Gabriella González Pane

**Última actualización:** June 5, 2026 — post P0/P1/P2.1 repo hygiene

---

## PRICING CROSS-REFERENCE (June 2026)

> Service prices in this document are NOT authoritative. The master reference is:
> `00_STRATEGIC/financial-pricing/canonical-pricing-reference-v2.md`
>
> Any price update should happen in the canonical file only.

---

## P0 — Hygiene & Trust ✅ COMPLETE

- [x] Stale-value sweep finished (0 stale hits)
- [x] Sensitive files removed from git tree (14 files)
- [x] `.gitignore` hardened for leads/sessions/xlsx/json lead data
- [x] 00-index added for every folder including `00_STRATEGIC/`
- [x] `docs/COMPLETE-INDEX.md` regenerated as auto-generated index
- [x] `tools/validate-refs.py` added — `links`, `stale`, `prices`, `all`
- [x] `tools/repo-audit.py` fixed for inline-code false positives
- [x] Pre-commit hook pending (P3.3)
- [x] Cross-ref validator not wired to CI yet (P3.3)

Validation after P0:
- `tools/repo-audit.py summary` → 171 .md, 0 stale, 0 broken intra-repo links
- `tools/validate-refs.py all` → links ✅ stale ✅ prices ✅

---

## P1 — Index & Navigation ✅ COMPLETE

- [x] `tools/repo-audit.py counts` live per-folder counts
- [x] README unified hub (`README.md`)
- [x] `start-here.md` redirect summary
- [x] `docs/COMPLETE-INDEX.md` auto-generated appendix
- [x] All folders have accurate `00-index.md`
- [x] Dead-link sweep done via `tools/validate-refs.py links`

---

## P2 — Content Alignment & Completion

### P2.1 Pricing table completeness ✅ COMPLETE
- [x] Canonical services cross-checked across consumer-facing docs
- [x] `04_SALES/corporate-service-agreement-full.md` has pricing cross-ref
- [x] Consumer docs verified: start-here.md, roadmap, website content, corporate program

### P2.2 Phase 0 checklist — actionable for Dra. GP ⏸️ PENDING
- Owner: Kiki + Dra. GP
- Needs: personal data, real 3-month financials, 3 Luque space quotes (real), Roque decision

### P2.3 Patient journey specs ⏸️ PENDING
- 3 profiles: insurance, private premium, expat
- Link existing templates per touchpoint

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

## P3 — Operational Tooling

- [x] `tools/repo-audit.py` counts/stale/sizes/crossrefs/summary
- [x] `tools/validate-refs.py` links/stale/prices/all
- [ ] `tools/update-pricing.py` dry-run + commit (P3.2)
- [ ] `.git/hooks/pre-commit` or `scripts/pre-commit` runs `validate-refs.py stale` (P3.3)
- [ ] Cron for monthly `repo-audit.py summary` delivery (P3.4)

---

## P4 — Client Delivery Artifacts

- [ ] `docs/dra-gp-status-june-2026.md` — one-pager status (P4.1)
- [ ] `docs/phase-0-binder.md` — printable Phase 0 bundle (P4.2)
- [ ] Investor summary 1-pager from financial-model-projections-v2 (P4.3)

---

## P5 — Growth / Next Phase

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

**STATUS ACTUAL:** Repo limpio, auditoría complete, pricing block validado. Siguiente hito concreto: P2.6 (tracker schema) y P2.7 (options reconciliation) antes de P4.
