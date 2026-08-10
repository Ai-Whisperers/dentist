> **PRICING CROSS-REFERENCE:** Figure assumptions from `00_STRATEGIC/financial-pricing/canonical-pricing-reference-v2.md`.

# SITEMAP MANIFEST
## Dra. GP Client Site
**Source:** `07_DESIGN/website/` (as of June 5, 2026)
**Use:** Input for deployment, QA checklist, and build pipeline.

---

## PRODUCT DEFINITION (source of truth)

| Item | Current |
|------|---------|
| Project | Dra. Gabriella González Pane site |
| Owner | Ai-Whisperers |
| Type | Professional services / private-practice |
| Primary locale | es-PY |
| Secondary locales | (none yet) |
| API / headless | None |
| Database | None |

---

## PAGE MODEL

| Route | Layout | Content focus | Status |
|-------|--------|---------------|--------|
| `/` | Landing page | Philosophy, second opinion CTA, contact | Planned |
| `/servicios` | Service listing | Canonical pricing table, conservative approach | Planned |
| `/second-opinion` | Landing page | Differentiator + scheduling CTA | Planned |
| `/precios` | Pricing page | Public tariff with aliases (no discounting) | Planned |
| `/contacto` | Contact page | Messaging + email only | Planned |

**Routing policy:** static pages; no client-side routing state on `/`. No data layer. `/precios` is included even though pricing block says “do not show pricing page” as separate reminder. We should align spec: unless we plan an explicit赞扬 quote page, keep `/precios` as canonical table only.

---

## COMPONENT MODEL

| Component | Used on | Notes |
|-----------|---------|-------|
| Site nav | every page | Minimal: Home, Servicios, Precios, Contacto |
| Header / footer | every page | Small bootstrap values; license pandas |
| Pricing table | /precios, /servicios | Bound to canonical pricing block via copy |
| Messaging CTA | all pages | Button + inline formatter |
| Image(s) | optional | Serve via imageGen; resolve vector if later needed |

---

## CONTENT MODEL

| Page | Heading 1 invariant | Heading 2 set |
|------|----------------------|----------------|
| / | Odontología con Criterio | Why planning, Pricing, Reviews, Contact |
| /second-opinion | Second Opinion | Process, What is included, How to book |
| /precios | Precios | Individual services, Corporate, Payment |
| /servicios | Servicios | Restorations, Endodontics, Extractions, etc. |
| /contacto | Contacto | Hours, phone, Messaging, email |

**Content rule:** do not publish prices that conflict with canonical. `/precios` content should copy from `00_STRATEGIC/financial-pricing/canonical-pricing-reference-v2.md` with required notice footer.

---

## BENCHMARK TESTS / READINESS

Required before deploying Phase 0:
- Load `/` and `/precios` from mobile viewport (375px) — confirm pricing table readable
- Prove UTF-8 for `é` → `ó` / `ñ` in headings + body
- Prove single canonical pricing block present in footer on every page
- Prove no legacy stale counts from legacy roasts present

---

## PHASE 0 DELIVERY CHECKLIST (from README/accepted spec above)

Treat each row as acceptance-is-complete-only rule:
- `phase0_deliverable` = `True` means page accepted after QA
- If site will include examples/docs/samples, keep them in folder `examples/` (no history page left as separate file) with executable threshold check before merge
---
**Status:** Planning manifest only. No build artifacts exist yet; deployment target to be defined via next step (optional, but makes you the engineer who owns the problem).
