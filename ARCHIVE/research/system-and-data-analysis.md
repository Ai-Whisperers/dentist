# System Analysis: SAM Dental Practice Management System + Appointment Data
## Dra. Gabriella González Pane — Odontología 3, Asunción

**Date:** June 2, 2026
**Status:** Complete

---

## Document Overview

This document captures two parallel analysis streams:
1. **System Architecture** — mapping SAM software modules, data structures, and extraction pathways
2. **Appointment Data Analysis** — statistical findings from 275 appointment records (Jan–May 2026)

---

## Part I: SAM System Analysis

### 1.1 System Identification

The clinic operates **SAM (Fichero Médico)** — a desktop dental practice management application configured for **Odontología 3**.

Key visible configuration:
- Clinic: **Odontología 3, Casa Central** ( Asunción, Paraguay)
- User: **gpane** (Gabriella González Pane)
- Insurance integrations: ASISMED, VANGUARD, PROTECCIÓN MÉDICA, SANTA CLARA, MDS, PARTIULAR, SENACSA
- Currency: Guaraníes (Gs.)

### 1.2 SAM Module Map

| Module | Spanish Name | Function |
|--------|--------------|----------|
| Patient Records + Billing | Fichas | CRM, demographics, insurance, procedure ledger |
| Insurance Coverage Matrix | Cobertura Procedimientos | Per-plan coverage % for each procedure |
| Appointments | Citas / Cronograma de Citas | Weekly calendar + daily list view |
| Raw Export | Bloc de notas | TSV text export of appointment DB |

### 1.3 Data Structures

#### Fichas Module (Patient Records)
```
Paciente (internal ID, e.g., 89.230)
├── Cédula Id.
├── Nombre completo
├── Fecha de nacimiento / Edad
├── Dirección, Emails, Teléfonos
├── Grupo Sanguíneo
├── Seguro Médico (e.g., ASISMED S.A.)
├── Plan de Seguro (e.g., CONSULTA Y DESCUENTO 50%)
└── Comentario Administrativo (ledger)
    ├── Factura (invoice number)
    ├── Fecha
    ├── Procedimiento (e.g., RESTAURACIÓN, ENDODONCIA DIENTE PREMOLAR)
    └── Costo (Gs.)
```

#### Cobertura Module (Insurance Coverage Matrix)
```
Filter hierarchy: Plan → Seguro → Médico (Odontología 3)
└── Procedimiento → % Cobertura Seguro / % Cobertura Paciente
```

Example entries visible:
- CONSULTA Y DESCUENTO 50% plan: 50% covered by insurance, 50% patient co-pay
- COBERTURA TOTAL FUNCIONARIOS: 100% insurance coverage
- BÁSICA + LUZ: basic coverage with lumen allowance

#### Citas Module (Appointments)
```
Primary key: cita (integer)
Columns: fecha, hora, persona, estado, desc_estado_cita, comentario,
          nombre_completo, cedula_identidad, descripcion, tipo_cita,
          con_turno, hora_llegada, v_nombre_dia, v_seguro,
          desc_plan_de_seguro, confirmado, nombre_medico, v_telefonos,
          nombre_sucursal, origen_cancelacion, suspendido, v_contrato,
          dias_atraso_vanguard, ind_hora_llegada
```

### 1.4 Data Export Capabilities

**Cleanest export path:** The raw TSV text file (bloc de notas) — no OCR required, directly parseable.

**Alternative:** High-resolution screenshots + multimodal LLM to extract key-value pairs from Fichas and Cobertura modules.

### 1.5 Data Completeness Gaps

| Gap | Implication |
|-----|------------|
| No direct DB access visible | Can only export via SAM UI or manual TSV dump |
| Fichas ledger is per-patient, not aggregated | Revenue analysis requires manual cross-referencing |
| Coverage matrix is plan-level, not patient-level | Actual reimbursement depends on patient-specific utilization |
| Appointment export is the only complete dataset we have | Financial modeling limited to appointment volume, not procedure revenue |

---

## Part II: Appointment Data Analysis

**Dataset:** 275 appointment records exported from SAM Citas module, Jan–May 2026.
**Patients:** 184 unique individuals (cedula != 0, excluding PROVISORIO CP)

### 2.1 Overall Performance Metrics

| Metric | Count | % |
|--------|------:|---:|
| **Total appointments** | 275 | 100% |
| **Realizado (completed)** | 172 | 62.5% |
| **Cancela Paciente (patient cancelled)** | 55 | 20.0% |
| **Ausente (no-show)** | 36 | 13.1% |
| **Anulado (system voided)** | 12 | 4.4% |
| **Cancela Profesional (professional cancelled)** | 0 | 0% |

**Showdown rate: 37.5%** — more than 1 in 3 appointments are lost.
**Completion rate: 62.5%** — room for significant improvement.

### 2.2 Late Arrivals

| Metric | Count | % |
|--------|------:|---:|
| **Arrived late (ind_hora_llegada=1)** | 106 | 38.5% |

Nearly 4 in 10 patients arrive after their scheduled time. This is an operational bottleneck affecting chair utilization and next-patient wait times.

### 2.3 Insurance Breakdown

| Insurer | Total Appts | Completed | Rate | Assessment |
|---------|------------:|----------:|-----:|------------|
| ASISMED S.A. | 134 | 81 | 60.4% | Volume leader, decent rate |
| MINISTERIO DE DESARROLLO SOCIAL (MDS) | 51 | 33 | 64.7% | Good volume + rate |
| VANGUARD | 30 | 27 | **90.0%** | ⭐ Best performer |
| PROTECCIÓN MÉDICA S.A | 29 | 17 | 58.6% | Below average |
| SANTA CLARA S.A. | 12 | 5 | 41.7% | Poor |
| PARTICULAR | 8 | 2 | **25.0%** | Worst payer |
| ODONTOLOGIA 3 (SENACSA) | 7 | 6 | 85.7% | Strong |
| VICE PRESIDENCIA DE LA REPÚBLICA | 1 | 1 | 100% | n=1 |

**Key finding:** VANGUARD patients complete 90% of appointments — nearly all are regular ortho/brace patients (ORTODONCIA ADEP-COFUDEP, DUAL plan). ASISMED dominates volume (134 appts, 48.7% of all) but at only 60.4% completion.

### 2.4 Top Insurance Plans by Volume

| Plan | Total | C | Rate |
|------|------:|---:|-----:|
| INDEFINIDO | 74 | 37 | 50.0% |
| CONSULTA Y DESCUENTO 50% | 29 | 22 | 75.9% |
| DUAL (VANGUARD) | 11 | 10 | 90.9% |
| ORTODONCIA ADEP-COFUDEP (VANGUARD) | 10 | 10 | **100%** |
| COBERTURA TOTAL FUNCIONARIOS | 8 | 7 | 87.5% |
| BANCO CONTINENTAL - BÁSICA + LUZ | 8 | 4 | 50.0% |
| ASOC. EMPLEADOS DE TELECEL - BÁSICA + LUZ + ENDO | 8 | 2 | 25.0% |
| SALUD PRIMORDIAL (PROTECCIÓN) | 7 | 7 | **100%** |
| SENACSA PLAN CORPORATIVO | 7 | 6 | 85.7% |

**INDEFINIDO is the largest single category (74 appts, 27%)** — this means 1 in 4 appointments don't have a clearly classified insurance plan. Risk of revenue leakage here.

### 2.5 Appointment Type Analysis

| Type | Description | Total | C | Rate |
|------|-------------|------:|---:|-----:|
| 1 | CONSULTA (follow-up) | 208 | 136 | 65.4% |
| 6 | PRIMERA CONSULTA (first visit) | 66 | 35 | **53.0%** |
| 3 | URGENCIAS (emergency) | 1 | 1 | 100% |

**First visits convert at 12 points lower than follow-ups.** This gap is expected but represents a clear improvement area.

### 2.6 Monthly Trend

| Month | Total | Completed | Rate |
|-------|------:|----------:|-----:|
| January 2026 | — | — | No data |
| February 2026 | 8 | 6 | 75.0% |
| March 2026 | 18 | 7 | **38.9%** ⬇️ |
| April 2026 | 19 | 12 | 63.2% |
| May 2026 | 31 | 19 | 61.3% |

**March anomaly:** 38.9% completion rate is significantly below baseline. Possible cause: rainy season / weather, end-of-quarter insurance churn, or a specific event. Needs investigation if pattern repeats.

### 2.7 Top 10 Most Frequent Patients

| Rank | Patient | CI | Insurer | Plan | Total Appts | Completed | Rate |
|-----:|---------|-----|---------|------|------------:|----------:|-----:|
| 1 | FREDI ARIEL GÓMEZ GIMENEZ | 3981678 | VANGUARD | ORTODONCIA ADEP-COFUDEP | 10 | 10 | **100%** |
| 2 | DEYSI ROSSANA CORONEL | 4691914 | VANGUARD | DUAL | 9 | 8 | 89% |
| 3 | PATRICIA ANAHI AQUINO GALLARDO | 4549647 | MDS | INDEFINIDO | 8 | 5 | 63% |
| 4 | PAOLA NOEMÍ JARA FERNÁNDEZ | 5285083 | PROTECCIÓN | SALUD PRIMORDIAL | 7 | 7 | **100%** |
| 5 | LIZ GABRIELA GARCÍA MENDIETA | 2684784 | ASISMED | CONSULTA Y DESCUENTO 50% | 7 | 7 | **100%** |
| 6 | HECTOR JOSE MARTIN BENITEZ ZUBIZARRETA | 2114726 | ASISMED | COBERTURA TOTAL FUNCIONARIOS | 6 | 6 | **100%** |
| 7 | FHERNANDO JOSE CALDERON GONZALEZ | 5096534 | MDS | INDEFINIDO | 4 | 2 | 50% |
| 8 | MARIA BEATRIZ ROMAN LOZANTOS | 4482564 | PROTECCIÓN | MINISTERIO DE AGRICULTURA | 4 | 2 | 50% |
| 9 | CLAUDIA GIANNINA CACERES DUARTE | 4438852 | ASISMED | TELECEL plan | 4 | 0 | **0%** |
| 10 | PABLO AUGUSTO TURRINI RUIZ DIAZ | 959912 | ASISMED | VIP PLUS SUPERIOR | 3 | 0 | **0%** |

**Observations:**
- FREDI ARIEL (VANGUARD ortho) is the most reliable patient — 10 appointments, 100% show rate
- PATRICIA AQUINO (MDS) is the highest-volume patient outside VANGUARD, but has a 63% show rate
- CLAUDIA CACERES and PABLO TURRINI have 4 and 3 appointments respectively with 0% completion — these are chronic no-shows consuming schedule slots

### 2.8 Patient Interest Signals (From Comments)

Keywords identified in `comentario` field:

| Keyword | Occurrences | Patients |
|---------|------------:|----------|
| "estética" / "estetica" | 2 | Stephanie Petta |
| "interesada" | 4 | Stephanie Petta, Jazmin Clarissa Marecos Escurra, Liz Dahiana Mercado Rojas |
| "corona" | 1 | Liz Dahiana Mercado Rojas |
| "limpieza" | 1 | Jazmin Clarissa Marecos Escurra |
| "blanqueamiento" | 0 | — |

**Interpretation:** Despite only 7 keyword matches, these represent a specific cohort actively seeking aesthetic services (whitening, crowns, cleaning). This is a leading indicator of demand for premium/cosmetic services. Given the strategy goal of repositioning Dra. GP toward value-based care, this cohort is the prime target for upsell conversations.

### 2.9 Profitability Classification

| Class | Total | C | Rate | Revenue Potential |
|-------|------:|---:|-----:|-------------------|
| Cobertura Total | 8 | 7 | **87.5%** | ⭐ Highest |
| 50% descuento | 36 | 27 | **75.0%** | High |
| Other | 74 | 56 | **75.7%** | Moderate |
| Básica | 83 | 45 | **54.2%** | Low |
| INDEFINIDO | 74 | 37 | **50.0%** | ⚠️ Risky |
| PARTICULAR | 8 | 2 | **25.0%** | ⚠️ Very Low |

**Highest margin procedures:** Cobertura Total (87.5% completion) and 50% descuento plans (patient pays half, clinic receives full minus insurer portion).

### 2.10 Chronic No-Shows (Requiring Action)

| Patient | CI | Appts | C | Rate | Risk |
|---------|-----|------:|---:|-----:|------|
| CLAUDIA GIANNINA CACERES DUARTE | 4438852 | 4 | 0 | 0% | Blocks schedule |
| PABLO AUGUSTO TURRINI RUIZ DIAZ | 959912 | 3 | 0 | 0% | Blocks schedule |
| JOSE OSMAR BOGADO PAREDES | 5445197 | 7+ | multiple | ~50% | High cancel rate |

**Recommendation:** Consider implementing a confirmation protocol (SMS/call) for patients with <50% historical show rate.

---

## Part III: Strategic Implications

### 3.1 Revenue Leakage Points

1. **37.5% showdown rate** → if each missed appointment has an average revenue value, significant annual leakage
2. **INDEFINIDO (27% of appointments)** → unclear insurance handling = likely undercharging or non-collection
3. **38.5% late arrivals** → chair idle time, reduced daily patient capacity
4. **53% first-visit conversion** → first appointments are effectively lost revenue when they don't return

### 3.2 Insurance Portfolio Health

| Tier | Insurers | Action |
|------|----------|--------|
| **Grow** | VANGUARD, ODONTOLOGIA 3 (SENACSA) | Maintain high-touch, ensure these patients stay |
| **Optimize** | ASISMED, MDS | Volume is there; work on show rate improvement |
| **Reconsider** | PARTICULAR, SANTA CLARA | Very low completion, collection difficulty |
| **Investigate** | PROTECCIÓN MÉDICA | Below-average rate (58.6%), check coverage matrix |

### 3.3 Premium/Aesthetic Demand Validation

The comment keyword analysis confirms:
- Real patients are explicitly asking about estética, corona, limpieza
- Cohort size appears small (~3-4 patients in this dataset) but represents high-value cases
- These patients should be fast-tracked to a premium service offering (see strategy docs on Option B parallel brand)

### 3.4 Data Assets for Financial Modeling

The appointment TSV gives volume data. To build accurate revenue projections, the following are needed from SAM:

| Needed Data | Source Module | Priority |
|-------------|---------------|----------|
| Procedure-level revenue per appointment | Fichas ledger (Comentario Admin) | 🔴 High |
| Coverage matrix (% paid by insurer vs patient) | Cobertura module | 🔴 High |
| Patient lifetime value by insurance plan | Fichas → Citas cross-link | 🟡 Medium |
| Historical collection rate by plan | Fichas ledger (Fact. amounts) | 🟡 Medium |

---

## Appendix: Data Files

| File | Source | Rows |
|------|--------|------:|
| `research/appointment-analysis.md` | SAM Citas TSV export | 275 |

---

## Document History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | June 2, 2026 | Initial full documentation |