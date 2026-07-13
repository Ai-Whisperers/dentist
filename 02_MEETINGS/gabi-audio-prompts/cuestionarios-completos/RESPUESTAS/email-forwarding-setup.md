# 📧 EMAIL FORWARDING SETUP — doctura.gabi@ometsdental.com.py
## Setup técnico · 13 jul 2026

---

## 🎯 Decisión Gaby

**P25 del cuestionario 13:** Gaby eligió "Gmail gratis basta" en vez de Google Workspace (USD 6.17/mes).

**Solución:** configurar email profesional `doctura.gabi@ometsdental.com.py` con **forwarding hacia Gmail personal**, no Google Workspace.

---

## ⚙️ Setup técnico

### Opción A — Email forwarding desde Cloudflare (recomendada)

**Costo:** Gs 0 (Cloudflare Email Routing ya está incluido en plan free de ometzdental.com)

**Setup:**

1. **DNS records en Cloudflare:**
   ```
   Tipo: MX
   Nombre: ometzdental.com.py
   Prioridad: 10
   Contenido: route1.mx.cloudflare.net
   
   Tipo: MX
   Nombre: ometzdental.com.py
   Prioridad: 20
   Contenido: route2.mx.cloudflare.net
   
   Tipo: MX
   Nombre: ometzdental.com.py
   Prioridad: 30
   Contenido: route3.mx.cloudflare.net
   ```

2. **Cloudflare Email Routing** (ya disponible en dash):
   - Crear regla: `doctura.gabi@ometsdental.com.py` → `gaby.personal@gmail.com`
   - Crear regla: `contacto@ometsdental.com.py` → `kiki@gmail.com` (gestión contenido)
   - Crear regla: `ivan@ometsdental.com.py` → `ivan@ai-whisperers.com`

3. **Gaby setup Gmail:**
   - Configurar "Send mail as" en Gmail: `doctura.gabi@ometsdental.com.py`
   - Verificar con email de confirmación
   - Ahora puede enviar como profesional Y recibir en su Gmail personal

### Opción B — Zoho Mail free tier (alternativa)

- 5 usuarios gratis
- Webmail + IMAP
- Más profesional pero requiere aprender nuevo panel

**Recomendación:** Opción A (Cloudflare + Gmail forwarding).

---

## 📧 Direcciones a configurar

| Email | Forward a | Uso |
|---|---|---|
| `doctura.gabi@ometsdental.com.py` | gaby.personal@gmail.com | Email principal Gaby |
| `contacto@ometsdental.com.py` | kiki@gmail.com | Formulario sitio, consultas generales |
| `presupuestos@ometsdental.com.py` | gaby.personal@gmail.com | Emails automáticos presupuestos |
| `ivan@ometsdental.com.py` | ivan@ai-whisperers.com | Iván (técnico) |
| `no-reply@ometsdental.com.py` | descartar | Solo envío, no recibir |

---

## 🔧 Configuración Gmail "Send mail as"

### Paso a paso (Gaby):

1. Gmail → ⚙️ Configuración → Ver toda la configuración
2. Pestaña "Cuentas e importación"
3. Sección "Enviar correo como" → "Añadir otra dirección de correo electrónico"
4. Nombre: `Dra. Gabriella González Pane`
5. Email: `doctura.gabi@ometsdental.com.py`
6. Servidor SMTP: `smtp.gmail.com`
7. Puerto: 587
8. Usuario: gaby.personal@gmail.com
9. Contraseña: contraseña de aplicación de Gmail (no la contraseña normal)
10. **Marcar:** "Tratar como alias" (responde desde la dirección que recibe)

### Generar contraseña de aplicación:

1. Google Account → Seguridad → Verificación en 2 pasos (activar primero)
2. Contraseñas de aplicaciones → Generar nueva
3. Nombre: "Ometz Dental Email"
4. Usar esa contraseña en el paso 9 de arriba

---

## ⚠️ Notas importantes

- **2FA obligatorio en Gmail de Gaby** (bloqueante — `RESPUESTAS-13-tecnologia` P43 marcada como No, hay que cambiar)
- **No usar la misma contraseña** en Gmail y Cloudflare
- **Bitwarden** para guardar contraseñas (P44 ya confirmado)
- **Email no es para HIPAA/GDPR compliance estricto** — datos sensibles de pacientes van por WA Business cifrado, no email

---

## 📋 Próximos pasos

| Paso | Dueño | Fecha |
|---|---|---|
| 1. Configurar DNS MX en Cloudflare | Iván | 14 jul |
| 2. Configurar Email Routing en Cloudflare | Iván | 14 jul |
| 3. Verificar forwards funcionando | Iván + Gaby | 15 jul |
| 4. Configurar "Send mail as" en Gmail Gaby | Gaby (con guía Iván) | 16 jul |
| 5. Documentar procedimiento | Iván | 17 jul |

---

## 🚨 Si después Gaby quiere Google Workspace completo

Costo: USD 6.17/mes = Gs ~45k/mes = Gs ~540k/año

Setup:
1. Comprar Google Workspace desde admin.google.com
2. Verificar dominio (DNS TXT record)
3. Crear usuarios: gaby@ometsdental.com.py, kiki@ometsdental.com.py
4. Migrar correo progresivamente

**Beneficio real:** Gaby@gmail personal queda separado de Ometz. Pero el forwarding cubre 95% del caso.