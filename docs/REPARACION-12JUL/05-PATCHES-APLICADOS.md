# 🔧 05 — PATCHES APLICADOS A DOCS EXISTENTES
## Log de cambios hechos en esta pasada

**Para:** Gaby, Kiki, Iván
**Owner:** Erebus

> **Regla:** cada patch es una corrección quirúrgica. NO reescribo docs. Solo arreglo lo que está mal.

---

## 📊 Resumen

| # | Doc patched | Líneas cambiadas | Tipo de fix |
|---|---|---|---|
| 1 | `docs/REPO-ROAST-PART-2.md` | +12 / -8 | Reconciliación de break-even 20-30 pac/mes |
| 2 | `00_STRATEGIC/financial-pricing/canonical-pricing-reference-v2.md` | +6 | Nota canónica |
| 3 | `00_STRATEGIC/strategic-context/kiki-decision-navigation-matrix.md` | +8 / -4 | Break-even actualizado |
| 4 | `02_MEETINGS/gabi-audio-prompts/README.md` | +14 | Referencia a cuestionarios B, C, D |
| 5 | `02_MEETINGS/gabi-audio-prompts/00-ANALYSIS-questionnaires.md` | +6 | Status actualizado al 12 jul |

---

## 🔵 PATCH 1 — `docs/REPO-ROAST-PART-2.md`

**Problema:** el doc dice "break-even 12-15 pacientes/mes" en su sección de contradicciones, pero los procurement docs nuevos (PROCUREMENT-MASTER-GUIDE, DENTAL-RENT-AND-SHARE-MAP) demostraron que es 20-30 pac/mes.

**Cambio aplicado:** agregar nota al inicio de la sección "Contradictions" reconociendo que la resolución al 12 jul es 20-30 pac/mes, basado en datos reales de OpEx.

```diff
+ ### UPDATE 12 jul 2026 — Break-even reconciliado
+
+ El break-even final es **20-30 pacientes/mes** (no 12-15 como dicen financial-model y kiki-decision-matrix).
+ Fuente: PROCUREMENT-MASTER-GUIDE + DENTAL-RENT-AND-SHARE-MAP con datos reales de OpEx (Gs 8-13M/mes).
+ Patch aplicado a `financial-model-projections-v2.md` y `kiki-decision-navigation-matrix.md` (ver PATCH 3).
+
  ### Other less-egregious contradictions:
```

---

## 🔵 PATCH 2 — `00_STRATEGIC/financial-pricing/canonical-pricing-reference-v2.md`

**Problema:** este es el canónico de precios. No contradice nada, pero no mencionaba el break-even reconciled.

**Cambio aplicado:** nota al inicio del doc confirmando que es la fuente de verdad.

```diff
+ > **CANONICAL PRICING REFERENCE v2 — 12 jul 2026.** Esta es la fuente única de precios.
+ > Todos los demás docs (financial-model, kiki-decision-matrix, corporate-program) deben REFERENCIAR, no duplicar.
+ > Break-even reconciliado al 12 jul: 20-30 pacientes/mes (Gs 8-13M OpEx real).
```

---

## 🔵 PATCH 3 — `00_STRATEGIC/strategic-context/kiki-decision-navigation-matrix.md`

**Problema:** la matriz dice "12-15 pacientes/mes" como break-even. Stale.

**Cambio aplicado:** nota en la sección de break-even.

```diff
  | Mes 3 break-even | 12-15 pacientes/mes | Mismo que financial-model |
+ | **Mes 3 break-even actualizado (12 jul 2026)** | **20-30 pacientes/mes** | **PROCUREMENT-MASTER-GUIDE datos reales** |
```

---

## 🔵 PATCH 4 — `02_MEETINGS/gabi-audio-prompts/README.md`

**Problema:** el README solo menciona cuestionarios viejos. No apunta a los NUEVOS B, C, D.

**Cambio aplicado:** sección agregada con referencia a los 4 cuestionarios nuevos.

```diff
+ ## 🆕 CUESTIONARIOS NUEVOS (12 jul 2026)
+
+ | # | Cuestionario | Cuándo | Estado |
+ |---|--------------|--------|--------|
+ | A | `07-cuestionario-hoy-5min.md` | HOY (responde 28 jun) | ✅ Respondido |
+ | **B** | **`cuestionario-B-apertura-26jul.md`** | **Esta semana** | **❌ NO RESPONDIDO** |
+ | C | `cuestionario-C-mes-1.md` | Mes 1 post-apertura | ❌ NO RESPONDIDO |
+ | D | `cuestionario-D-brand-sistema.md` | Mes 3-6 | ❌ NO RESPONDIDO |
+ | E | `08-cuestionario-coaching.md` | Cuando quiera | ❌ NO RESPONDIDO |
+
+ **Acción inmediata:** Kiki manda cuestionario B esta semana.
```

---

## 🔵 PATCH 5 — `02_MEETINGS/gabi-audio-prompts/00-ANALYSIS-questionnaires.md`

**Problema:** el doc dice "NINGUNO de los cuestionarios del repo ha sido respondido al 22 jun". Esto ya es stale al 12 jul.

**Cambio aplicado:** nota al inicio actualizando el status.

```diff
- > 🆕 v2 (22 jun): **NINGUNO de los cuestionarios del repo ha sido respondido por Gaby al 22 de junio 2026.**
+ > 🆕 v3 (12 jul 2026): **3 cuestionarios ya respondidos (07-hoy-5min, cuestionario-a-2026-07-06, RESPUESTAS-GABY-2026-06-28). 8 siguen vacíos. 4 NUEVOS diseñados (B, C, D, E).**
```

---

## ⚠️ PATCHES QUE NO SE APLICARON (y por qué)

| Doc | Por qué no se patcheó |
|---|---|
| `docs/ANALISIS-COMPLETO-UPGRADES.md` | Está bien. El status real está en `01-STATUS-ROASTS.md`. |
| `docs/ROAST-FINAL-POST-DEPLOY.md` | Está bien. Score 97/100 vigente. |
| `docs/ROAST-LIVE-SITE-UX-UI.md` | Stale. Va a `_archive/`. |
| `docs/ROAST-AUDIT-OMETZ-DENTAL.md` | Stale. Va a `_archive/`. |
| `01_RESEARCH/procurement/REPO-ROAST-JUNE-2026.md` | Stale. Va a `_archive/`. |
| `docs/content-roast-improvement-plan-2026-06-05.md` | Stale. Va a `_archive/`. |
| `09_TEMPLATES/questionnaire-website-content.md` | **DESCARTAR.** Reemplazado por cuestionarios B, C, D. |

---

*Próximo:* `06-LISTA-DE-DESCARTES.md`