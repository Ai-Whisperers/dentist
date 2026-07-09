# RESEARCH — PAGOS DIGITALES PY 2026
## Comparativa de métodos de pago + costos + setup para Ometz
**Versión:** 1.0 — 8 de julio 2026
**Para:** Kiki (ejecuta setup) + Iván (aprueba presupuesto) + Gaby (decide)

---

## 🎯 QUÉ RESUELVE ESTE DOC

Gaby necesita cobrar:
1. **Efectivo** (Gs)
2. **Transferencia bancaria** (ya hay cuenta)
3. **Tarjeta** (POS en consultorio)
4. **Link de pago** (online, para que paguen antes/después de la consulta)
5. **Cuotas** (para tratamientos grandes)

Y cada método tiene costo, integración y compliance diferente. Este doc es la decisión informada.

---

## 📊 TABLA COMPARATIVA

| Método | Costo setup | Comisión por transacción | Velocidad | Cuotas | Online | Recomendado |
|--------|-------------|---------------------------|-----------|--------|--------|-------------|
| **Efectivo** | $0 | $0 | Inmediato | No | No | ✅ Siempre |
| **Transferencia SIPAP** | $0 | $0 (puede haber costo del banco emisor) | 1-24h | No | Sí (link del banco) | ✅ Para monto alto |
| **Bancard POS** (POS físico) | Gs 800k-1.5M equipo | 3.0-5.0% | 24-48h liquidación | Sí (3-12 cuotas) | No | ✅ Pacientes en consultorio |
| **Pagopar** (link de pago) | $0 setup | 4.5-6.0% + Gs 2.500 por transacción | 1-3 días | Sí (3-12 cuotas con interés) | Sí | ✅ Cobros online + cuotas |
| **Tigo Money / Wally** | $0 | 2-3% | Inmediato | No (en algunos casos sí) | Sí | 🟡 Complementario |
| **PayPal** (expat) | $0 | 5.5% + USD 0.30 fijo | 1-3 días | Limitado | Sí | 🟡 Solo expats |
| **Stripe** | $0 | 4.9% + USD 0.30 | 1-2 días | Sí | Sí | 🟡 Alternativa PayPal |
| **Zimple** (PY) | $0 | 2.5-3.5% | 1-2 días | Sí | Sí | 🟡 Alternativa PY |

---

## 🔧 SETUP DETALLADO POR MÉTODO

### 1. BANCARD POS (recomendado principal para consultorio físico)

**Qué es:** POS físico que procesa tarjeta de débito/crédito. Los más usados en PY: POSnet, Bancard, First Data.

**Setup:**
1. Contactar Bancard: 021 249 4000 / bancard.com.py
2. Solicitar alta de comercio
3. Completar formulario de comercio (RUC, datos fiscales)
4. Adquirir POS físico (alquiler o compra)
5. Capacitación de 1 hora (básica)
6. Liquidación en 24-48h a cuenta bancaria

**Costos:**
- **Setup:** Gs 800k-1.5M (compra POS) o Gs 50-150k/mes (alquiler)
- **Comisión por transacción:** 3.0-5.0% del monto
- **Cuotas sin interés:** depende del acuerdo (3-6 cuotas típicamente)
- **Cuotas con interés:** 6-12 cuotas disponibles

**Pros:**
- Universal (Visa, Mastercard, Cabal, Bancard Check)
- Paciente ve el cargo inmediato
- Liquidación rápida
- Soporte 24/7

**Contras:**
- Requiere POS físico (no 100% mobile)
- Costo fijo de equipo
- Comisión alta en cuotas largas

**Recomendación Ometz:** ✅ **Setup prioritario mes 1**

---

### 2. PAGOPAR (recomendado principal para cobros online)

**Qué es:** Plataforma paraguaya de pagos online que permite cobrar por link, QR o checkout, con o sin cuotas.

**Setup:**
1. Registrarse en pagopar.com
2. Completar KYC (datos personales + RUC + cuenta bancaria)
3. Integrar vía API o usar link de pago
4. Tiempo de activación: 3-5 días hábiles

**Costos:**
- **Setup:** $0
- **Comisión por transacción:** 4.5-6.0% + Gs 2.500 fijo
- **Cuotas:** 3-12 cuotas (con o sin interés según acuerdo)
- **Liquidación:** 1-3 días hábiles

**Pros:**
- Sin setup
- Link de pago compartible por WhatsApp
- Cuotas automáticas
- QR para cobrar en consultorio

**Contras:**
- Comisión más alta que POS
- Cuotas con interés (3-12 cuotas 12-30% anual)
- Necesita internet

**Recomendación Ometz:** ✅ **Setup prioritario mes 1**, especialmente para:
- Cobros antes de consulta (prepago)
- Cobros de planes de tratamiento grandes (Gs 1M+)
- Cobros a distancia (expats)

---

### 3. TRANSFERENCIA BANCARIA SIPAP

**Qué es:** Sistema de pagos interbancarios de Paraguay. Cualquier banco a cualquier banco.

**Setup:**
- Cliente necesita tu CBU/alias
- No requiere integración

**Costos:** $0 para Gaby. Costo puede aplicar al banco del paciente (generalmente gratis en Banco Familiar, Itaú, Continental, Regional, GNB, BNF).

**Pros:**
- Sin costo
- Sin setup
- Universal

**Contras:**
- Lento (24-48h en acreditarse)
- No tiene protección al vendedor (si el paciente miente haber transferido)
- Difícil conciliar

**Recomendación:** ✅ Como método secundario, principalmente para pagos anticipados grandes.

---

### 4. TIGO MONEY / BILLETERAS MÓVILES

**Qué es:** Billeteras digitales populares en PY (Tigo Money, Wally, Personal Pay, Zimple).

**Setup:**
- Dar tu número Tigo/Personal/Claro a pacientes
- Verificar cada pago manualmente

**Pros:**
- Gratis
- Universal (penetración alta en PY)
- Rápido

**Contras:**
- Sin protección al vendedor
- Conciliación manual
- Límite por transacción (varía)

**Recomendación:** 🟡 Aceptar pero no promover activamente.

---

### 5. PAYPAL (solo expats)

**Qué es:** Plataforma global de pagos.

**Setup:**
- Crear cuenta PayPal Business
- Vincular cuenta bancaria PY (algunos bancos lo permiten)
- Recibir pagos vía link o checkout

**Costos:**
- **Comisión:** 5.5% + USD 0.30 por transacción
- **Conversión de divisa:** 3-4% adicional

**Pros:**
- Reconocido por expats
- Protección al vendedor
- Múltiples monedas

**Contras:**
- Caro
- Difícil de sacar a banco PY (algunos no aceptan)
- Soporte limitado en español

**Recomendación:** 🟡 Solo si hay demanda clara de expats.

---

### 6. STRIPE (alternativa a PayPal)

**Setup:**
- Crear cuenta Stripe (más PY-friendly que PayPal)
- Necesita cuenta bancaria compatible
- Integrar vía API

**Costos:**
- **Comisión:** 4.9% + USD 0.30
- Sin comisión de conversión (mejor que PayPal)

**Recomendación:** 🟡 Evaluar si PayPal presenta problemas.

---

## 🎯 ESTRATEGIA RECOMENDADA PARA OMETZ DENTAL

### Mix de métodos (mes 1)

| Para cobro de | Método |
|---------------|--------|
| **< Gs 300.000** (consulta, profilaxis) | Efectivo o transferencia |
| **Gs 300k-1M** (operatoria) | Bancard POS o transferencia |
| **> Gs 1M** (rehabilitación, plan completo) | Pagopar en cuotas + transferencia |
| **Expat (cualquier monto)** | PayPal o Stripe |
| **Prepago online** | Pagopar link |

### Setup recomendado mes 1 (prioridad)

1. ✅ **Efectivo** (ya está)
2. ✅ **Transferencia bancaria** (ya está)
3. 🔴 **Bancard POS** (1 día setup)
4. 🔴 **Pagopar** (3-5 días setup)
5. 🟡 Tigo Money (ya está si Gaby tiene línea)
6. ⚪ PayPal (cuando haya demanda expat)

### Inversión inicial estimada

| Concepto | Costo |
|----------|-------|
| POS Bancard (alquiler primer mes) | Gs 100k |
| Activación Pagopar | $0 |
| Total mes 1 | **Gs 100k** |

### Costos operativos estimados

| Concepto | Costo |
|----------|-------|
| Bancard 3% sobre Gs 5M de facturación mensual | Gs 150k/mes |
| Pagopar 5% sobre Gs 2M de cobros online | Gs 100k/mes |
| Total mensual | **Gs 250k** |

(equivale a ~USD 35/mes)

---

## 📋 CHECKLIST SETUP PAGOS

### Bancard POS
- [ ] Contactar Bancard: 021 249 4000
- [ ] Solicitar formulario de comercio
- [ ] Enviar RUC + datos fiscales
- [ ] Confirmar tiempo de activación
- [ ] Adquirir POS (compra o alquiler)
- [ ] Capacitación
- [ ] Liquidación a cuenta bancaria configurada

### Pagopar
- [ ] Registrarse en pagopar.com
- [ ] Completar KYC
- [ ] Vincular cuenta bancaria
- [ ] Generar link de pago para "Consulta general Gs 300k"
- [ ] Generar link para "Segunda opinión Gs 450k"
- [ ] Generar link para "Plan personalizado desde Gs 800k"
- [ ] Probar flujo completo con Gs 1 de prueba

### Transferencia
- [ ] CBU y alias publicados en todos los canales
- [ ] Proceso de confirmación implementado (cliente envía comprobante por WA)

---

## 🔐 SEGURIDAD Y COMPLIANCE

- [ ] **Nunca pedir datos de tarjeta** por WhatsApp (usar siempre Pagopar o Bancard)
- [ ] **Nunca compartir datos bancarios** en público (redes sociales)
- [ ] **Siempre dar recibo** escrito (físico o digital)
- [ ] **Conciliar pagos semanalmente** (no acumular sin verificar)
- [ ] **Política de devolución** clara (cuándo se devuelve, cuándo no)

---

## 🔗 CRUZAR CON OTROS DOCUMENTOS

- `00_STRATEGIC/financial-pricing/canonical-pricing-reference-v2.md`
- `00_STRATEGIC/financial-pricing/financial-model-projections-v2.md`
- `docs/MASTER-TODO-RESTANTE.md` (este batch)
- `docs/PLAN-NEXT-STEPS-BRANDING-MARKETING.md`

---

**STATUS:** v1.0 — recomendación Bancard + Pagopar. Pendiente: setup efectivo cuando Gaby tenga RUC.