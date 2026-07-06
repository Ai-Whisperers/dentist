# Dra. Gabriella González Pane — Strategic Repositioning Project

**Status:** P0–P5 complete (strategic + content). Site live, awaiting Kiki validation (Sección 1 of `07_DESIGN/website/validacion-cliente-dra-gp.md`).
**Last updated:** 2026-07-05 (audit + operator-folder pass)

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
| **Hoja de la reunión (lo único que Gaby va a usar)** | [`gaby/reunion-roque/00-cheat-sheet-1-pagina.md`](gaby/reunion-roque/00-cheat-sheet-1-pagina.md) | ✅ Lista |
| **Plan B si la reunión sale mal** | [`gaby/reunion-roque/01-plan-b-7-dias.md`](gaby/reunion-roque/01-plan-b-7-dias.md) | ✅ Lista |
| **Audio prompts para Gaby** | [`gaby/audios-pendientes/README.md`](gaby/audios-pendientes/README.md) | 🟡 Esperando que grabe |
| **Burucuyá (Luque) ≠ Mburucuyá (Asunción)** | `00_STRATEGIC/strategic-context/burucuya-vs-mburucuya-clarity.md` | ✅ Aclarado |
| **6 opciones de espacio en Luque** | `01_RESEARCH/locations/luque-space-shortlist-v2.md` | ✅ Priorizada amiga Burucuyá |
| **⭐ Repo audit (this session)** | [`docs/REPO-AUDIT-2026-07-05.md`](docs/REPO-AUDIT-2026-07-05.md) | ✅ Done |

**Why two repos?** The dentist repo holds *strategy, research, client-side content authoring* (markdown). The platform app holds *runtime code + deployable JSON bundles*. The flow is: edit markdown here → port to JSON there → redeploy.

**Client gate (Sección 1 of `07_DESIGN/website/validacion-cliente-dra-gp.md`):** WhatsApp, phone, address, RUC, MSPBS, email are PENDING from Kiki. Until received, every ContactButton on the live site falls back to email (graceful chain: WA → phone → email → contact page).

---

## ⭐ Gaby's home page (start here if you're Gaby)

**[`gaby/index.md`](gaby/index.md)** — operator-facing home page, in Spanish. Print it, bookmark it, share with Kiki.

Contains:
- 🔴 What to do THIS WEEK (Roque meeting cheat sheet + Plan B)
- 🎤 6 audio prompts waiting to be recorded
- 📋 Site validation (blocked in Sección 1)
- 📚 Reference docs (only when needed)

---

## Quick Start (for Kiki / Ivan / Erebus)

1. **Gaby's home page:** [`gaby/index.md`](gaby/index.md) (operator view, Spanish)
2. **Repo audit:** [`docs/REPO-AUDIT-2026-07-05.md`](docs/REPO-AUDIT-2026-07-05.md) (this session)
3. **Project overview:** [`start-here.md`](start-here.md) (5 min)
4. **Exec summary:** [`docs/executive-summary.md`](docs/executive-summary.md)
5. **Work plan:** [`docs/REPO-WORK-PLAN.md`](docs/REPO-WORK-PLAN.md)
6. **Action tracker:** [`TODO.md`](TODO.md)
7. **Client validation form:** [`07_DESIGN/website/validacion-cliente-dra-gp.md`](07_DESIGN/website/validacion-cliente-dra-gp.md) (23 preguntas, 5 secciones) — **bloqueada en Sección 1**
8. **Client validation MÍNIMA:** [`07_DESIGN/website/validacion-minima-viable.md`](07_DESIGN/website/validacion-minima-viable.md) (6 preguntas, destraba en 5 min)

---

## Project Summary

Reposicionamiento del modelo de práctica dental — del modelo volumen (seguros) al modelo basado en valor y criterio clínico.

**El problema:** El seguro extrae ~85% del valor que ella genera.
**La oportunidad:** Mercado premium + expats + "Dental CIO" como servicio diferenciador.

---

## Directory Structure (current — July 5, 2026)

| Folder | Content | Files |
|--------|---------|-------|
| `gaby/` | ⭐ Operator-facing curated view for Gaby | 6 |
| `00_STRATEGIC/` | Strategic, financials, positioning | 16 |
| `01_RESEARCH/` | Market, pricing, legal, competition, locations, equipment | 60 |
| `02_MEETINGS/` | Kiki sessions, client prep, archives | 42 |
| `03_LAUNCH/` | Roadmap, sales playbooks, website, institutional | 40 |
| `04_SALES/` | Corporate agreements | 3 |
| `05_OPERATIONS/` | Clinical routines, comms, legal | 25 |
| `06_MARKETING/` | Digital presence, blog posts, SEO | 14 |
| `07_DESIGN/` | Brand + website | 31 |
| `08_WHATSAPP/` | Automation, templates | 9 |
| `09_TEMPLATES/` | Patient + questionnaire templates | 14 |
| `ARCHIVE/` | Historical / staged-out materials | 18 |
| `docs/` | Planning, indexes, executive summary, audit | 13 |
| `content/` | Deployable JSON bundles (es/en) — synced to platform | 36 JSON |
| Root MD | README, TODO, start-here, agents, audit, cheat sheet | 8 |
| **TOTAL** | | **299 .md + 36 JSON** |

---

## Entry Points

| Doc | Purpose |
|-----|---------|
| [`gaby/index.md`](gaby/index.md) | ⭐ **Gaby's home page (operator-facing, Spanish)** |
| `start-here.md` | Project overview + option summary |
| `docs/executive-summary.md` | Current status and next block |
| `TODO.md` | Phase tracker (P0–P5) |
| `docs/REPO-WORK-PLAN.md` | Phased execution plan |
| [`docs/REPO-AUDIT-2026-07-05.md`](docs/REPO-AUDIT-2026-07-05.md) | Repo audit (this session) |

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
- **P2.8: operator-facing folder for Gaby** (`gaby/`, 2026-07-05) ✅ NEW
- **P2.9: repo audit + upgrade pass** (`docs/REPO-AUDIT-2026-07-05.md`, 2026-07-05) ✅ NEW

## What's Next

- **P3.0: Reunión Roque** (this week — Gaby + Ara)
- P3.1: wire validator into pre-commit + CI
- P4: client delivery artifacts
- P5: growth / next phase items
- **P5.5 (post-Roque): internal link graph (8% → 50%)** — see audit #6
- **P5.6 (post-Roque): date stamps on 271 dated-less files** — see audit #5
- **P5.7 (post-Roque): ARCHIVE/bloat-2026-06-04/ cleanup** — see audit #5

See `TODO.md` and `docs/REPO-AUDIT-2026-07-05.md` for detail.

---

## Operator Handoff (for Gaby)

> Hola Gaby 👋
>
> Tu nueva página de inicio es **[`gaby/index.md`](gaby/index.md)**.
>
> Está en español, tiene solo lo que necesitás hacer, y no cambia.
> Los archivos originales siguen en `00-09/` por si Kiki/Erebus los necesita.
>
> Si tenés una pregunta, pedíselo a Kiki primero.

---

*This README is the canonical entry point for Kiki, Ivan, and Erebus. For Gaby, see [`gaby/index.md`](gaby/index.md).*