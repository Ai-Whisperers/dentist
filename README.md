# OMETZ DENTAL — אומץ

**Status:** Branding + content completo. **Apertura del consultorio bloqueada en 6 datos de Gaby** (ver `docs/MASTER-TODO-RESTANTE.md`).  
**Last updated:** 8 de julio 2026 (Erebus)

---

## 🌐 Live site & live repo

- **Sitio live (operativo):** https://ometzdental.com/es · https://ometzdental.com/en
- **Este repo:** Source of truth estratégico + content. NO es runtime del sitio.

## 🎯 Qué hay aquí

Repo estratégico + operativo de **Ometz Dental** — práctica de odontología conservadora con foco en rehabilitación oral y segunda opinión escrita. Marca diferenciada por **אומץ** (hebreo: coraje) y el claim **"Te escucho."**

Estrategia fundada en cliente real (Dra. Gabriella González Pane, 20+ años de práctica, MSPBS 3618) con base en Mburucuyá, Asunción, Paraguay.

## 📁 Estructura

```
ROOT
├── docs/                  ← Todos los planes, master trackers, audits (preferido)
├── 00_STRATEGIC/          ← ADN, pricing, financial model
├── 01_RESEARCH/           ← Research: market, competitors, compliance, content
├── 02_MEETINGS/           ← Análisis de audios/preguntas de Gaby (incl. legacy Roque)
├── 03_LAUNCH/             ← GTM: corporate, institutional, referrals, roadmap
├── 04_SALES/              ← CRM y pipelines
├── 05_OPERATIONS/         ← Clínica: clinical routines, legal, biosecurity
├── 06_MARKETING/          ← Marketing: FB, GBP, blog, calendar, Reels, HTML emails
├── 07_DESIGN/             ← Branding: SVGs, photography, website specs
├── 08_WHATSAPP/           ← WhatsApp Business: templates, automation
├── 09_TEMPLATES/          ← Templates paciente: appointment, recall, referral
├── ARCHIVE/               ← (git-ignored) — contenido obsoleto
├── content/               ← JSONs para deploy live site
└── config/                ← Variables centrales (phone, email, address)
```

## 🔗 Empezar por

| Quiero... | Archivo |
|-----------|---------|
| Entender TODO lo que falta hoy | `docs/MASTER-TODO-RESTANTE.md` |
| Ver el plan estratégico del año 1 | `docs/PLAN-NEGOCIO-ANO-1-OKR-MENSUALES.md` |
| Entender gaps de ads + locations | `docs/GAP-ANALYSIS-COMPLETO-ADS-LOCATIONS.md` |
| Ver el audit brutal | `docs/ROAST-AUDIT-OMETZ-DENTAL.md` |
| Auditar la estructura del repo | `bash scripts/audit-structure.py` |
| Actualizar teléfono/email real | `bash scripts/update-contact-info.sh` |

## 🔧 Scripts útiles

| Script | Propósito |
|--------|-----------|
| `scripts/audit-structure.py` | Cuenta archivos, densidad, archivos grandes |
| `scripts/update-contact-info.sh` | Actualiza phone en 159 archivos cuando Gaby confirma |

## 🏷️ Variables centrales

Ver `config/variables-central.md` — single source of truth para teléfono, email, dirección, branding, precios.

---

**Owner:** Iván (decisiones) + Kiki (ejecución) + Gaby (cliente)  
**Ecosistema:** ai-whisperers / hermes-agent
