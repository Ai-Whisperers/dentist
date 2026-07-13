# 🗄️ 06 — LISTA DE DESCARTES
## 12 docs que van a `_archive/` porque stale, peligroso o sin valor

**Para:** Gaby, Kiki, Iván
**Owner:** Erebus

> **Criterio para archivar:**
> 1. **Stale:** doc escrito en jun/2026, contexto pre-apertura, ya no aplica.
> 2. **Reemplazado:** hay una versión más reciente (en `REPARACION-12JUL/` o `STAFFING-Y-ORGANIZACION/`).
> 3. **Peligroso:** tiene preguntas/afirmaciones que pueden comprometer legalmente a Gaby.
> 4. **Sin valor residual:** docs de auditoría que ya no se actualizan.

---

## 📊 Lista de los 12 docs a archivar

| # | Path | Categoría | Por qué |
|---|---|---|---|
| 1 | `docs/ROAST-LIVE-SITE-UX-UI.md` | Stale | Reemplazado por ROAST 3 + 1 |
| 2 | `docs/ROAST-AUDIT-OMETZ-DENTAL.md` | Stale | Reemplazado por ROAST 1 |
| 3 | `01_RESEARCH/procurement/REPO-ROAST-JUNE-2026.md` | Stale | Reemplazado por ROAST 1 + 2 |
| 4 | `docs/content-roast-improvement-plan-2026-06-05.md` | Stale | Reemplazado por 03-STATUS-IMPROVEMENTS |
| 5 | `docs/dra-gp-status-june-2026.md` | Stale | Reemplazar con versión jul-2026 |
| 6 | `09_TEMPLATES/questionnaire-website-content.md` | Peligroso + Reemplazado | Tiene Sección 4 Pregunta 1 y Sección 8 artículo 1 que pueden comprometer a Gaby |
| 7 | `ARCHIVE/legacy-roque-jun-2026/roque-meeting/roque-meeting/06-response-playbook-by-scenario.md` | Stale | Reunión Roque ya cerrada |
| 8 | `ARCHIVE/legacy-roque-jun-2026/roque-meeting/roque-meeting/04-conversation-script-by-act.md` | Stale | Ídem |
| 9 | `ARCHIVE/legacy-roque-jun-2026/roque-meeting/roque-meeting/05-red-lines-and-walk-away.md` | Stale | Ídem |
| 10 | `ARCHIVE/legacy-roque-jun-2026/roque-meeting/roque-meeting/02-roque-decision-matrix.md` | Stale | Ídem |
| 11 | `ARCHIVE/legacy-roque-jun-2026/roque-meeting/roque-meeting/GEMINI-VOICE-ROLE-PLAY-PROMPT.md` | Stale | Ídem |
| 12 | `08_WHATSAPP/templates/message-templates-library.md` | Sin valor residual | 681 líneas para agent que no existe. Stripped to 8 quick replies v2 |

---

## 🚫 ACCIÓN NO TOMADA — Eliminar archivos

> **Decisión:** **NO eliminamos nada.** Solo movemos a `_archive/`. Si en el futuro alguien necesita la versión vieja, está.

---

## 📂 Estructura de `_archive/`

```
/root/dentist/_archive/
├── 2026-06-pre-apertura/
│   ├── roasts/
│   │   ├── ROAST-LIVE-SITE-UX-UI.md
│   │   ├── ROAST-AUDIT-OMETZ-DENTAL.md
│   │   ├── REPO-ROAST-JUNE-2026.md
│   │   └── content-roast-improvement-plan-2026-06-05.md
│   ├── status/
│   │   └── dra-gp-status-june-2026.md
│   ├── roque-meeting/
│   │   ├── 06-response-playbook-by-scenario.md
│   │   ├── 04-conversation-script-by-act.md
│   │   ├── 05-red-lines-and-walk-away.md
│   │   ├── 02-roque-decision-matrix.md
│   │   └── GEMINI-VOICE-ROLE-PLAY-PROMPT.md
│   └── whatsapp/
│       └── message-templates-library.md
└── 2026-07-replaced-questionnaires/
    └── questionnaire-website-content.md
```

---

## ⚠️ DECISIONES DE SEGURIDAD — Documentos peligrosos

### `09_TEMPLATES/questionnaire-website-content.md`

**Por qué peligroso:**
- **Sección 4 Pregunta 1:** "¿Algo específico que te motivó a dejar Odontología 3?"
  - Si la respuesta queda por escrito, es prueba de intención de irse.
  - Si llega a manos de Roque, es prueba de "traición".
- **Sección 8 Artículo 1:** "Por qué dejé el seguro médico después de 13 años"
  - Título solo ya es declaración de guerra contra Roque.

**Acción:** archivar a `_archive/2026-07-replaced-questionnaires/` con nota:

> **DESCARTADO 12 jul 2026.** Reemplazado por cuestionarios B, C, D. Las preguntas filosóficas y los títulos de blog de este doc son riesgos legales. NO usar.

### `02_MEETINGS/gabi-audio-prompts/04-quejas-contrato-y-plan-de-salida.md`

**Por qué peligroso (potencial):**
- Habla de "quejas" contra Roque.
- Si Gaby responde por escrito, queda evidencia.

**Acción:** mantener (no archivar) pero Kiki NO debe mandarlo a Gaby sin filtro previo.

---

## 🎯 ACCIÓN OPERATIVA

1. **Mover los 12 archivos** a `_archive/` con `git mv` (preserva historial).
2. **Commit único** con mensaje explicativo.
3. **Push a GitHub.**

Esta acción la puede hacer Iván o yo cuando me autorice.

---

*Próximo:* `EXECUTIVE-SUMMARY.md`