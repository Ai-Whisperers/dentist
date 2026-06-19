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

**Why two repos?** The dentist repo holds *strategy, research, client-side content authoring* (markdown). The platform app holds *runtime code + deployable JSON bundles*. The flow is: edit markdown here → port to JSON there → redeploy.

**Client gate (Sección 1 of `07_DESIGN/website/validacion-cliente-dra-gp.md`):** WhatsApp, phone, address, RUC, MSPBS, email are PENDING from Kiki. Until received, every ContactButton on the live site falls back to email (graceful chain: WA → phone → email → contact page).

---

## Quick Start

1. **START HERE:** `start-here.md` (5 min)
2. **Exec summary:** `docs/executive-summary.md`
3. **Work plan:** `docs/REPO-WORK-PLAN.md`
4. **Action tracker:** `TODO.md`
5. **Client validation form:** `07_DESIGN/website/validacion-cliente-dra-gp.md` (23 questions, 5 sections)

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
| `docs/REPO-WORK-PLAN.md` | Phased execution plan |

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
