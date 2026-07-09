# RESEARCH — AUTOMATIZACIONES IA + HERRAMIENTAS OPERATIVAS
## Stack tecnológico para consultorio dental PY 2026
**Versión:** 1.0 — 8 de julio 2026

---

## 🎯 PROPÓSITO

Mapear herramientas IA que pueden ayudar a Gaby/Kiki a automatizar tareas administrativas del consultorio. **No reemplazar a las personas**, sino quitar trabajo repetitivo.

---

## 📊 CATEGORÍAS DE HERRAMIENTAS

### 1. AGENDAMIENTO Y RECORDATORIOS

| Herramienta | Qué hace | Costo PY | Para Ometz |
|-------------|----------|----------|-----------|
| **Calendly** | Pacientes agendan online desde web | $0-12/mes | ✅ Sí |
| **Cal.com** | Open-source, alternativa a Calendly | $0-15/mes | ✅ Sí |
| **Setmore** | Scheduling con recordatorio | $0-12/mes | ✅ Sí |
| **Google Calendar + WA manual** | Manual pero gratis | $0 | 🔶 Mes 1 |

### 2. CHATBOT IA EN WHATSAPP

| Herramienta | Qué hace | Costo |
|-------------|----------|-------|
| **WATI** | Chatbot WA para PYMEs | USD 40/mes |
| **1msg.com.py** | WA API para PY | USD 5-20/mes |
| **Callbell** | WA multiagente | USD 25/mes |
| **Evolution API** + n8n (self-hosted) | Custom WA bot | $10-50 server |

**Recomendación Ometz mes 1:** Manual (Kiki contesta con quick replies). Mes 3+: evolucionar a WATI o similar.

### 3. RECORDATORIOS AUTOMÁTICOS

| Herramienta | Qué hace | Costo |
|-------------|----------|-------|
| **1msg** | SMS + WA recordatorio 24h antes | USD 5-20/mes |
| **PatientPop** | Recordatorios completos | USD 100+/mes |
| **Practo Ray** | Diseño + recordatorios | Variable |

**Acción:** investigar 1msg en PY.

### 4. SEGUIMIENTO DE PACIENTES (CRM LIVIANO)

| Herramienta | Qué hace | Costo |
|-------------|----------|-------|
| **Notion** | Base de datos simple | $0 |
| **Airtable** | Similar pero más visual | $0-20/mes |
| **HubSpot Free** | CRM básico con contactos | $0 hasta 1M contactos |
| **Google Sheets + Forms** | DIY | $0 |
| **Smile Snap** | Diseñado para dental | $0-300/mes |

**Recomendación:** Google Sheets mes 1, Notion o Airtable mes 3+.

### 5. FACTURACIÓN Y PAGOS

| Herramienta | Qué hace | Costo |
|-------------|----------|-------|
| **Bancard POS** | Datáfono físico | Gs 800k-1.5M setup + 3-5% tx |
| **Pagopar** | Link pago online | 4.5-6% tx |
| **Stripe** | Internacional | 4.9% + USD 0.30 |
| **Tigo Money / Personal Pay** | Billeteras PY | 2-3% tx |

(Ver `01_RESEARCH/payments/research-pagos-digitales-py-2026.md`)

### 6. SOFTWARE DE GESTIÓN DENTAL INTEGRADO

| Herramienta | Qué hace | Costo |
|-------------|----------|-------|
| **Dentisoft** | Historia clínica + agenda + facturación | USD 30-80/mes |
| **CloudDent** | Cloud completo | USD 25-50/mes |
| **Doctoralia Pro** | Discovery + agenda | Variable |
| **Dentidesk** | HIS completo | USD 50+/mes |

(Ver `01_RESEARCH/operational/research-software-gestion-dental-py-2026.md`)

### 7. GENERACIÓN DE CONTENIDO

| Herramienta | Qué hace | Costo |
|-------------|----------|-------|
| **ChatGPT Plus / Claude Pro** | Copy + ideas | USD 20/mes |
| **Canva Pro** | Diseño + scheduling | USD 13/mes |
| **CapCut Pro** | Edición video | USD 8/mes |
| **Midjourney / Flux / DALL-E** | Imágenes AI | USD 10-30/mes |
| **Captions / Opus Clip** | Subtítulos auto + clips | USD 20/mes |

(Ver `07_DESIGN/brand-assets/ai-photo-prompts.md`)

### 8. EMAIL MARKETING

| Herramienta | Qué hace | Costo |
|-------------|----------|-------|
| **Mailchimp** | Email automation | $0-15/mes hasta 500 contacts |
| **MailerLite** | Alternativa limpia | $0-10/mes |
| **Brevo (ex-Sendinblue)** | Ilimitado en plan free | $0 |
| **ConvertKit** | Para creadores | $0-29/mes |

**Recomendación Ometz:** Brevo (gratis y soporta español +py).

### 9. MONITOREO Y ANALYTICS

| Herramienta | Qué hace | Costo |
|-------------|----------|-------|
| **Google Analytics 4** | Tráfico web | $0 |
| **Google Search Console** | SEO | $0 |
| **Meta Business Suite** | FB/IG analytics | $0 |
| **Hotjar** | Heatmaps web | $0-32/mes |
| **Microsoft Clarity** | Heatmaps gratuito | $0 |

### 10. IA PARA ESCUCHAR Y RESPONDER

| Herramienta | Qué hace | Costo |
|-------------|----------|-------|
| **Otter.ai** | Transcripción meetings | $0-20/mes |
| **Fathom** | Grabador meetings + AI notes | $0-24/mes |
| **Granola** | AI-powered meeting notes | $0 |
| **ChatGPT Whisper API** | Transcripción local | $0.006/min |

---

## 🎯 STACK RECOMENDADO PARA OMETZ DENTAL

### Mes 1 (esencial)
- WhatsApp Business + quick replies (gratis) — comunicación pacientes
- Google Calendar + Sheets (gratis) — agenda + fichas
- Canva (gratis) — creativos sociales
- Meta Business Suite (gratis) — publicar y medir
- Google Analytics (gratis) — web

**Costo total mes 1: ~USD 0.**

### Mes 3 (escalar)
- Brevo (gratis) — newsletter
- CapCut (gratis) — edición video
- Calendly gratis — agendar online
- Mailchimp free — emails transaccionales

**Costo total mes 3: ~USD 0.**

### Mes 6+ (profesional)
- Canva Pro (USD 13/mes) — Brand Kit
- Mailchimp paid o Brevo paid (USD 30/mes)
- Meta Ads activo (USD 100-300/mes)
- CloudDent o Dentisoft (USD 30-80/mes)
- Stripe para recibir en USD (4.9% + USD 0.30)

**Costo total mes 6+: ~USD 200-400/mes.**

---

## 🔮 IA QUE VA A CAMBIAR ODONTOLOGÍA EN 12 MESES

### Tendencias a observar

1. **AI en radiografías** — detección de caries automática
2. **AI en planificación ortodóntica** — simulación de resultados
3. **AI chatbots** — captura de pacientes 24/7
4. **Voice AI** — Kiki usa AI para transcribir reuniones y resumir
5. **Document AI** — procesar consentimientos firmados
6. **Predictivo** — anticipar qué pacientes no vuelven

### Para Ometz específicamente

| Solución | Aplicabilidad | Cuándo |
|----------|---------------|--------|
| Chatbot IA en WA | Media — clientes PY prefieren humano | Mes 6+ opcional |
| AI radiografía | Baja — sin equipo Rx | No |
| AI notas clínicas | Alta — ahorra tiempo Gaby | Mes 3 si hay app PY compatible |
| AI transcription audios Kiki | Alta | Mes 1 (gratis con Whisper) |
| AI assistant para Kiki | Alta — ChatGPT para redactar respuestas | Mes 1 |

---

## ✅ CHECKLIST MES 1 (lo que se puede configurar ahora)

- [ ] Crear WhatsApp Business con foto + descripción
- [ ] Cargar 12 quick replies (ya existen)
- [ ] Crear Google Calendar compartido
- [ ] Crear Google Sheet para fichas clínicas
- [ ] Crear Google Drive cifrado para backups
- [ ] Configurar Canva gratis
- [ ] Activar Meta Business Suite
- [ ] Crear cuenta ChatGPT para Kiki (si no tiene)

---

## 🔗 LINKS

- Repo: https://github.com/Ai-Whisperers/dentist
- WhatsApp: https://raw.githubusercontent.com/Ai-Whisperers/dentist/master/08_WHATSAPP/templates/final/quick-replies-v2-final.md
- Software dental: https://raw.githubusercontent.com/Ai-Whisperers/dentist/master/01_RESEARCH/operational/research-software-gestion-dental-py-2026.md
- Pagos: https://raw.githubusercontent.com/Ai-Whisperers/dentist/master/01_RESEARCH/payments/research-pagos-digitales-py-2026.md

---

**STATUS:** v1.0 — research listo. Implementación gradual según presupuesto.