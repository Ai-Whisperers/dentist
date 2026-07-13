# 📋 07 — DOCUMENTOS BASE POR ROL
## Los 30+ documentos que necesitan existir ANTES de cada hire / acuerdo

**Versión:** 1.0 — 12 jul 2026

> **Filosofía:** No se puede雇佣 bien sin paperwork. Los docs base son los que permiten que Gaby se siente con un candidato, le explique las reglas, le muestre el manual, le firme el contrato, y arranque sin caos. La mayoría YA EXISTE en el repo. Lo que falta es saber cuáles usar para cada rol y cuáles crear nuevos.

---

## 📊 Matriz documentos × roles

Leyenda: ✅ existe · ⚠️ existe borrador, falta pulir · ❌ falta crear

| Documento | Contador | Abogado | RC | Lab | Radiólogo | Auxiliar | CM Jr | Dentista Jr | Co-mentor | Paciente |
|---|---|---|---|---|---|---|---|---|---|---|
| Contrato de honorarios | ⚠️ | ⚠️ | ✅ (póliza) | ❌ | ❌ | — | ❌ | — | ❌ | — |
| NDA / Confidencialidad | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ⚠️ | ⚠️ |
| Acuerdo de derivación ética | — | ⚠️ | — | — | — | — | — | — | — | — |
| Manual de procedimientos | — | — | — | — | — | ✅ | ⚠️ | ⚠️ | ⚠️ | ⚠️ |
| Protocolo de bioseguridad | — | — | — | — | — | ✅ | — | ✅ | — | ✅ |
| Sistema de documentación clínica | — | — | — | — | — | ✅ | — | ✅ | — | ✅ |
| Quick replies + tono | — | — | — | — | — | — | ✅ | — | — | — |
| Brand book | — | — | — | — | — | — | ✅ | — | ⚠️ | — |
| Manual del auxiliar | — | — | — | — | — | ✅ | — | — | — | — |
| Política de reemplazos/ausencias | ❌ | — | — | ❌ | ❌ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | — |
| Onboarding checklist | ❌ | ❌ | — | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | — |
| Carta de oferta | ⚠️ | ⚠️ | — | ❌ | ❌ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | — |
| Acuerdo de revenue share | — | ⚠️ | — | — | — | — | — | ⚠️ | ⚠️ | — |
| Contrato de confidencialidad paciente | ✅ | ✅ | ✅ | — | — | ✅ | — | ✅ | ⚠️ | ✅ |
| Política de crisis reputacional | — | ⚠️ | — | — | — | — | ⚠️ | — | — | — |
| Cronograma de onboarding (2 semanas) | — | — | — | — | — | ❌ | ❌ | ❌ | ⚠️ | — |
| Métricas de los primeros 30/60/90 días | ❌ | — | — | — | — | ❌ | ❌ | ❌ | ⚠️ | — |
| Proceso de feedback mensual | — | — | — | — | — | ❌ | ⚠️ | ⚠️ | ⚠️ | — |
| Proceso de despido | — | ❌ | — | — | — | ❌ | ❌ | ❌ | — | — |
| Carta de推荐 del puesto anterior | ❌ | ❌ | — | — | — | ❌ | ❌ | ❌ | — | — |

---

## 📝 Detalle de los 10 documentos más críticos a tener listos

### 1. Contrato de honorarios profesionales (contador, abogado, lab, radiólogo, co-mentor)
**Dónde:** NO existe formal. Hay 2 plantillas en `05_OPERATIONS/legal-compliance/practice-legal/` (coaching-agreement y referral-agreement) que sirven como modelo.
**Qué tiene que tener:**
- Servicios específicos
- Honorarios (mensuales o por acto)
- Forma de pago (transferencia, efectivo, Bancard)
- Confidencialidad
- Causales de rescisión
- Fecha + firmas

**Acción:** crear `09_TEMPLATES/contrato-honorarios-profesionales.md` (5 min, copiar el referral-agreement).

### 2. NDA / Confidencialidad
**Dónde:** NO existe formal. Hay cláusula en algunos contratos pero no documento standalone.
**Qué tiene que tener:**
- Definición de información confidencial
- Obligaciones del firmante
- Duración (típico 2 años post-relación)
- Excepciones (información pública)
- Penalidad por incumplimiento

**Acción:** crear `09_TEMPLATES/nda-confidencialidad.md` (10 min).

### 3. Acuerdo de derivación ética
**Dónde:** `05_OPERATIONS/legal-compliance/practice-legal/referral-agreement-legal.md` existe como plantilla.
**Qué tiene que tener:**
- Relación entre derivante y derivado
- Sistema de seguimiento del caso
- Política de comisiones (CERO — esto ya está claro)
- Confidencialidad del paciente
- Causales de rescisión

**Acción:** pulir el documento existente, agregar versión 1.1 con cláusulas de calidad (1 vez).

### 4. Manual del auxiliar dental
**Dónde:** `05_OPERATIONS/staff-manual-asistente.md` ✅ existe.
**Estado:** 70% completo. **Falta:**
- Sección de "qué hacer si el paciente se queja"
- Sección de "cómo manejar instrumental dañado"
- Sección de "tu rol en la bioseguridad" (más específico)
- Glosario de términos odontológicos

**Acción:** Iván/Kiki en 1h lo dejan listo.

### 5. Sistema de documentación clínica
**Dónde:** `05_OPERATIONS/sistema-documentacion-clinica.md` ✅ existe.
**Estado:** 80% completo. Falta:
- Versión digital vs papel (qué queda en qué)
- Tiempo de retención (10 años mínimo legal)
- Acceso (quién ve qué)

**Acción:** actualizar con decisiones Gaby.

### 6. Quick replies + tono (community manager / WA Business)
**Dónde:** `08_WHATSAPP/templates/final/quick-replies-v2-final.md` ✅ existe (8 quick replies).
**Estado:** listo. Falta configurar en WA Business + testear.

### 7. Brand book
**Dónde:** `07_DESIGN/brand-assets/` tiene múltiples archivos (moodboards, decisión framework, paleta). NO hay brand book consolidado.
**Acción:** consolidar en un solo documento (siguiente archivo a crear).

### 8. Política de crisis reputacional
**Dónde:** `05_OPERATIONS/guia-crisis-reputacional.md` ✅ existe borrador.
**Falta:**
- Trigger explícito de "esto es crisis, esto no"
- Roles y responsables
- Tiempos de respuesta
- Comunicación con pacientes afectados

**Acción:** actualizar con Gaby e Iván.

### 9. Protocolo de bioseguridad
**Dónde:** `05_OPERATIONS/clinical-routines/biosecurity-checklist-mspbs.md` ✅ existe.
**Estado:** completo. Sólo falta firma de la auxiliar cuando entre.

### 10. Contrato de trabajo (auxiliar, dentista junior) — RELACIÓN DE DEPENDENCIA
**Dónde:** NO existe plantilla en repo. CRÍTICO.
**Qué tiene que tener:**
- Sueldo mensual
- Horario
- Funciones específicas
- IPS, aguinaldo, vacaciones (Paraguay: 12 días vacaciones tras 1 año)
- Preaviso (30 días)
- Cláusula de confidencialidad
- Causales de despido justificado (Art. 81 Código Laboral PY)

**Acción:** abogado redacta plantilla (Gs 1.5-2M, una vez).

---

## 🆕 5 documentos NUEVOS a crear (no existen)

### 11. Onboarding checklist (genérico, 2 semanas)
Para cada hire nuevo:
- Día 1: firma de contrato, tour, lectura del manual
- Día 2-3: observación sin tarea
- Día 4-7: tarea supervisada
- Día 8-14: tarea autónoma con feedback diario
- Día 15-30: autónoma con feedback semanal
- Día 30: evaluación de período de prueba

### 12. Carta de oferta (genérica)
Para extender oferta formal:
- Posición
- Sueldo bruto
- Fecha de inicio
- Período de prueba
- Beneficios
- "Pendiente de firma de contrato"

### 13. Acuerdo de revenue share
Para合伙人, dentista con alquiler de sillón, co-mentores:
- Distribución % clara
- Costos compartidos
- Forma de distribución (mensual)
- Causales de salida
- No competencia (duración limitada)

### 14. Métricas de los primeros 30/60/90 días
Para cada rol:
- Mes 1: qué se espera
- Mes 2: qué se espera
- Mes 3: evaluación formal
- Triggers de "no está funcionando"

### 15. Proceso de despido
Checklist legal:
- Causales justificadas (Art. 81)
- Preaviso (30 días)
- Indemnización
- Carta documento
- Entrevista final
- Devolución de activos (llaves, instrumental, etc.)
- NDA sigue vigente

---

## 📅 Plan de creación de documentos (cronograma)

| Semana | Documentos a crear |
|---|---|
| Esta (12-19 jul) | #1 honorarios, #2 NDA, #11 onboarding checklist, #12 carta de oferta |
| Mes 1 (jul-ago) | #3 derivación ética (pulir), #6 quick replies ya está |
| Mes 2 (ago) | #4 manual auxiliar (completar), #10 contrato雇佣 (con abogado) |
| Mes 3 (sep) | #5 sistema clínico (completar), #8 crisis reputacional |
| Mes 4 (oct) | #13 revenue share, #14 métricas, #15 despido (con abogado) |
| Mes 5 (nov) | #7 brand book consolidado, #9 bioseguridad firmado |

---

## 🎯 Lo que se puede hacer HOY en la oficina con Gaby

1. Revisar lista de "✅ existe" — confirmar que están vigentes.
2. Revisar lista de "⚠️ existe borrador" — priorizar cuáles completar primero.
3. Identificar cuáles de los 5 NUEVOS son los más críticos para el 26 jul:
   - **#11 onboarding** (cuando雇佣)
   - **#12 carta de oferta** (cuando雇佣)
   - **#1 honorarios** (cuando firme con contador o lab)
   - **#2 NDA** (cuando firme con cualquier aliado externo)
   - **#10 contrato雇佣** (cuando auxiliar llegue mes 3)

---

*Próximo:* `08-brand-book-operativo.md`