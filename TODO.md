# TODO — Dra. Gabriella González Pane

**Última actualización:** June 5, 2026 — post P0/P1/P2/P3

---

## P0 — Hygiene & Trust ✅ COMPLETE
- [x] Stale-value sweep finished (0 stale hits)
- [x] Sensitive files removed from git tree (14 files)
- [x] `.gitignore` hardened for leads/sessions/xlsx/json lead data
- [x] 00-index added for every folder including `00_STRATEGIC/`
- [x] `docs/COMPLETE-INDEX.md` regenerated as auto-generated index
- [x] `tools/validate-refs.py` added — `links`, `stale`, `prices`, `all`
- [x] `tools/repo-audit.py` fixed for inline-code false positives
- [x] Pre-commit hook wiring (P3)
- [x] Cross-ref validator wired to CI (P3)

Validation after P0:
- `tools/repo-audit.py summary` → 172 .md, 0 stale, 0 broken intra-repo links
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

### P2.2 Placeholder inventory ✅ COMPLETE
- [x] Inventory created at `00_STRATEGIC/PLACEHOLDER-INVENTORY.md`
- [x] 20 files with template fields mapped to owners

### P2.3 Archive Phase 0 placeholder docs ✅ COMPLETE
- [x] `02_MEETINGS/ARCHIVE-roque-phase1-june2026/roque-meeting-results.md`
- [x] `02_MEETINGS/ARCHIVE-roque-phase1-june2026/luque-space-shortlist-3-priorities.md`
- [x] `02_MEETINGS/ARCHIVE-roque-phase1-june2026/client-data-collection-checklist.md`
- Archivo centralizado, raw docs preservados para auditoría.

### P2.4 Stale-value sweep ✅ COMPLETE
- [x] 0 stale hits (validator pass)

### P2.5 Link verification ✅ COMPLETE
- [x] 0 broken intra-repo links (validator pass)

### P2.6 Executive summary ⏸️ PENDING
- [ ] `docs/dra-gp-status-june-2026.md` — one-pager status
- [ ] Calibrar contenido: mapear documentos completos vs placeholders pendientes

### P2.7 Final README/docs validation ⏸️ PENDING
- [ ] Validar que README y start-here reflejen estado real del repo
- [ ] Remover referencias a archivos archivados

---

## P3 — Operational Tooling

### P3.1 Audit tooling ✅ COMPLETE
- [x] `tools/repo-audit.py` counts/stale/sizes/crossrefs/summary
- [x] `tools/validate-refs.py` links/stale/prices/all
- [x] Path bug fixed for cross-platform execution

### P3.2 Pre-commit hook ✅ COMPLETE
- [x] Hook created at `.git/hooks/pre-commit`
- [x] Hook runs `tools/validate-refs.py all`
- [x] Hook blocks commit on validation failure

### P3.3 CI validation ⏸️ PENDING
- [ ] GitHub Actions workflow (si repo tiene CI)
- [ ] `.github/workflows/repo-validation.yml`

### P3.4 Monthly audit cron ⏸️ PENDING
- [ ] Cron for monthly `repo-audit.py summary` delivery

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

**STATUS ACTUAL:** Repo limpio, auditoría completa, pricing block validado, placeholders inventariados, docs Roque archivados. Siguiente hito: P2.6 (status doc) y P2.7 (README/final docs).