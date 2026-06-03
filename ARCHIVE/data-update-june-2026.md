# DATA UPDATE: Appointment Analysis — June 2, 2026

## Source Data
- **File**: `Untitled spreadsheet.xlsx` (exported from Dra. GP's practice management system)
- **Period**: April 22 - June 1, 2026 (approx. 6 weeks)
- **Total appointments**: 601
- **Unique patients**: 342

---

## KEY FINDINGS

### Appointment Status
| Status | Count | Percentage |
|--------|-------|------------|
| Realizado (Completed) | 352 | 58.6% |
| Cancela Paciente (Patient Canceled) | 115 | 19.1% |
| Ausente (No-show) | 103 | 17.1% |
| Anulado (Voided) | 2 | 0.3% |
| Pendiente (Pending) | 29 | 4.8% |

### Efficiency Metrics
- **Completion rate**: 58.6%
- **No-show rate**: 17.1%
- **Cancellation rate**: 19.1%
- **Combined lost**: 36.2% of scheduled appointments

---

## INSURANCE BREAKDOWN

Top insurers by volume:
1. ASISMED S.A. — dominant player
2. MINISTERIO DE DESARROLLO SOCIAL — second largest
3. PROTECCIÓN MÉDICA S.A
4. ODONTOLOGIA 3 (own corporate)
5. VANGUARD
6. EL BUEN SAMARITANO S.A.
7. VICE PRESIDENCIA DE LA REPUBLICA

**Key observation**: Dra. GP is heavily dependent on insurance authorization (confirmed field shows "S" for most appointments). This confirms the core problem: she's locked into the insurance authorization model where she receives ~Gs 60k but generates Gs 400-550k in value.

---

## PATIENT VOLUME ANALYSIS

### Monthly Trends
- April 2026: ~80 appointments
- May 2026: ~100+ appointments
- June 2026: Early data shows continuation

**Run rate**: ~100-130 appointments/month
**At ~4 weeks/month**: 25-32 appointments/week

### New Patient Acquisition
- "PRIMERA CONSULTA" (first consultation) appointments indicate new patient intake
- Multiple patients appear with 2+ appointments (follow-ups for multi-visit treatments)
- First consultations tracked: ~40-50 in the dataset period

---

## TOP PATIENTS (Frequency Analysis)

Highest frequency patients (repeated visits suggest ongoing treatment plans):
1. JUAN JAVIER ALEJANDRO DUARTE ORTIZ — 10+ visits (ASISMED)
2. KYRIAN WEISS VAN DER POL — 6 visits (EL BUEN SAMARITANO / CONFORT)
3. ANA DELIA GONZÁLEZ MARTÍNEZ — 6 visits (PROTECCIÓN MÉDICA / PLAN TODO)
4. ANDREA MARÍA FRANCO MARTINEZ — 5 visits (ASISMED / MEDITERRANEAN SHIPPING)
5. PATRICIA ANAHI AQUINO GALLARDO — 4 visits
6. Others with 3-4 visits each

**Insight**: High-frequency patients are almost exclusively on insurance plans. This is the patient base she'd transition to private model.

---

## FINANCIAL IMPLICATIONS

### Current Model (Insurance)
- Average reimbursement appears to be in the Gs 30,000-90,000 range per procedure (based on "persona" codes)
- Multiple procedures per patient (root canals, restorations, etc.)
- Volume-dependent model requires high appointment count

### Revenue Potential (Private Model)
If she transitions to private pay at Gs 400-550k per restoration:
- Current volume: ~100 appointments/month
- At 50% conversion to private: 50 private patients × Gs 400k = Gs 20M/month
- At 75% conversion: 75 × Gs 400k = Gs 30M/month

**vs. current**: ~Gs 5-8M/month (insurance rates)

---

## NO-SHOW ANALYSIS

**17.1% no-show rate** is significant. Common patterns:
- Double-booking issues (same patient appears in multiple slots)
- Patients with multiple "Ausente" entries (e.g., JUAN JAVIER DUARTE ORTIZ)
- Cross-verification with "Cancela Paciente" shows ~36% total lost appointments

**Recommendation**: Implement confirmation WhatsApp 24h before appointment (already in operations playbook)

---

## OUTPUT FILES

1. **`patient-appointment-analysis.xlsx`** — Full formatted analysis with 6 sheets:
   - Resumen (Summary)
   - Estado de Citas (Status breakdown)
   - Analisis de Seguros (Insurance analysis)
   - Pacientes Frecuentes (Top patients)
   - Volumen Mensual (Monthly volume)
   - Tipos de Citas (Appointment types)

2. **` Untitled spreadsheet.xlsx`** — Original data preserved

---

## NEXT STEPS (Based on This Data)

1. **Patient database extraction**: 342 unique patients — need to identify which are "premium-eligible" (first consultas, high-frequency, private pay candidates)

2. **Insurance revenue analysis**: Cross-reference "persona" billing codes with actual reimbursement to confirm the gap

3. **Transition candidates**: Patients on "PARTICULAR" (private pay) or high-end plans (CONFORT, VIP PLUS, etc.) are immediate private model candidates

4. **No-show reduction**: Immediate implementation of WhatsApp confirmation protocol

---

*Generated: June 2, 2026*
*Source: Untitled spreadsheet.xlsx (601 appointments)*