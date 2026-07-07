# Dra. Gabriella Gonzalez Pane - Strategic Repositioning Project

**Status:** P0–P5 complete (strategic + content). Site live, awaiting Kiki validation (Sección 1 of `07_DESIGN/website/validacion-cliente-dra-gp.md`).
**Last updated:** June 19, 2026

---

## 🌐 Live site & platform link

The actual website is **deployed and live** — this repo is the **strategic + content source of truth**, not the runtime code.

| What | Where | Status |
|---|---|---|
| **Live site** | https://dragabriela.paragu-ai.com | ✅ Live (1/1 swarm replica) |
| Production code | [`Ai-Whisperers/paragu-ai-platform`](https://github.com/Ai-Whisperers/paragu-ai-platform) → `apps/dra-gabriela/` | ✅ Deployed on Docker Swarm |
| Swarm service | `dra-gabriela_web` (1/1, `dra-gabriela:prod-013ea3b-20260618-1326`) | ✅ Converged |
| Traefik routing | `Host(dragabriela.paragu-ai.com)` + `dra-gabriela.com.py` (pending DNS) | ✅ Active |
| **Content sync flow** | `dentist/07_DESIGN/website/*.md` → `paragu-ai-platform/apps/dra-gabriela/content/{en,es}/*.json` | This repo is authoritative; platform app consumes JSON |
| Canonical pricing | `00_STRATEGIC/financial-pricing/canonical-pricing-reference-v2.md` | ✅ Single source of truth |
| **Reunión Roque** | 🆕 v2 con Ara como decision-maker — ver `02_MEETINGS/client-prep/roque-meeting/` | 🟡 Pendiente, fecha TBD |
| **Hoja de la reunión (lo único que Gaby va a usar)** | `02_MEETINGS/client-prep/roque-meeting/00-ONE-PAGE-CHEAT-SHEET.md` | ✅ Lista |
| **Plan B si la reunión sale mal** | `02_MEETINGS/client-prep/roque-meeting/13-emergency-plan-7-days.md` | ✅ Lista |
| **Audio prompts para Gaby** | `02_MEETINGS/gabi-audio-prompts/` (6 audios + README) | 🟡 Esperando que grabe |
| **Burucuyá (Luque) ≠ Mburucuyá (Asunción)** | `00_STRATEGIC/strategic-context/burucuya-vs-mburucuya-clarity.md` | ✅ Aclarado |
| **6 opciones de espacio en Luque** | `01_RESEARCH/locations/luque-space-shortlist-v2.md` | ✅ Priorizada amiga Burucuyá |

**Why two repos?** The dentist repo holds *strategy, research, client-side content authoring* (markdown). The platform app holds *runtime code + deployable JSON bundles*. The flow is: edit markdown here → port to JSON there → redeploy.

**Client gate (Sección 1 of `07_DESIGN/website/validacion-cliente-dra-gp.md`):** WhatsApp, phone, address, RUC, MSPBS, email are PENDING from Kiki. Until received, every ContactButton on the live site falls back to email (graceful chain: WA → phone → email → contact page).

---

## Quick Start

1. **REUNIÓN CON ROQUE ESTA SEMANA:** `02_MEETINGS/client-prep/roque-meeting/00-ONE-PAGE-CHEAT-SHEET.md` (1 cara, lo único que Gaby va a usar)
2. **AUDIO PROMPTS para Gaby:** `02_MEETINGS/gabi-audio-prompts/README.md` (6 audios, empezar por el de la pregunta clave)
3. **START HERE:** `start-here.md` (5 min)
4. **Exec summary:** `docs/executive-summary.md` (v2 con Ara + Plan B)
5. **Work plan:** `docs/REPO-WORK-PLAN.md` (repo hygiene P0-P5) + **`docs/MASTER-PLAN-COMPLETE-2026.md`** ⭐ NEW 7 jul 2026 — comprehensive master plan covering research, upgrades, business ideas, execution plans, considerations
6. **Action tracker:** `TODO.md`
7. **Client validation form:** `07_DESIGN/website/validacion-cliente-dra-gp.md` (23 preguntas, 5 secciones) — **bloqueada en Sección 1**
8. **Client validation MÍNIMA:** `07_DESIGN/website/validacion-minima-viable.md` (6 preguntas, destraba en 5 min)

---

## Project Summary

Reposicionamiento del modelo de práctica dental — del modelo volumen (seguros) al modelo basado en valor y criterio clínico.

El problema: El seguro extrae ~85% del valor que ella genera.
La oportunidad: Mercado premium + expats + "Dental CIO" como servicio diferenciador.

---

## Directory Structure

| Folder | Content | Files |
|--------|---------|-------|
| `00_STRATEGIC/` | Strategic, financials, positioning | 12 |
| `01_RESEARCH/` | Market, pricing, legal, competition | 30 |
| `02_MEETINGS/` | Kiki sessions, client prep, archives | 11 |
| `03_LAUNCH/` | Roadmap, sales playbooks, website | 34 |
| `04_SALES/` | Corporate agreements | 3 |
| `05_OPERATIONS/` | Clinical routines, comms, legal | 22 |
| `06_MARKETING/` | Digital presence | 8 |
| `07_DESIGN/` | Brand + website | 18 |
| `08_WHATSAPP/` | Automation, templates | 4 |
| `09_TEMPLATES/` | Patient templates | 5 |
| `ARCHIVE/` | Historical / staged-out materials | 16 |
| `docs/` | Planning, indexes, executive | 3 |
| Root MD | README, TODO, start-here, agents | 6 |
| **TOTAL** | | **172** |

---

## Entry Points

| Doc | Purpose |
|-----|---------|
| `start-here.md` | Project overview + option summary |
| `docs/executive-summary.md` | Current status and next block |
| `TODO.md` | Phase tracker (P0–P5) |
| `docs/MASTER-PLAN-COMPLETE-2026.md` | ⭐ Master plan: research + upgrades + business ideas + execution + KPIs |

---

## Tooling

| Script | Commands |
|--------|----------|
| `tools/repo-audit.py` | `summary`, `counts`, `stale`, `crossrefs`, `sizes` |
| `tools/validate-refs.py` | `links`, `stale`, `prices`, `all` |

Both scripts are executable and pass on current tree.

---

## What's Done

- P0: hygiene, sensitive-file removal, audit tooling
- P1: indexes, README hub, cross-ref cleanup
- P2.1: canonical pricing validation
- P2.2: placeholder inventory (`00_STRATEGIC/PLACEHOLDER-INVENTORY.md`)
- P2.3: Phase 0 placeholder docs archived (3 files)
- P2.6: executive summary (`docs/executive-summary.md`)
- P2.7: README validated and normalized

## What's Next

- P3: wire validator into pre-commit + CI
- P4: client delivery artifacts
- P5: growth / next phase items

See `TODO.md` for detail.
