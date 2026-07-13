# ⚙️ SETUP REDES SOCIALES + TRACKING
## Ometz Dental · 14-18 julio 2026
### Ejecutado por: Iván (Ai-Whisperers) + Kiki (operativo)

---

## 🔴 ESTA SEMANA — TODO LIST

### A. Facebook Page Ometz Dental

**Owner:** Iván + Kiki

**Pasos:**

1. Ir a https://business.facebook.com
2. Crear cuenta Meta Business Suite si no existe (usar ivan@ai-whisperers.com como owner)
3. Crear Fan Page: "Ometz Dental"
4. Username: `@ometsdental`
5. Categoría: "Dentist" + "Medical & Health"
6. Logo: provisional (placeholder hasta sesión fotos martes 15 jul)
7. Cover: 1200×630px. Texto: "Ometz Dental · Odontología con criterio · Te escucho" + CTA "WA Business"
8. Bio (155 char máx):
   > "Ometz Dental — Odontología boutique en Asunción. Criterio + conservación + planificación. Dra. Gaby González Pane. אומץ — coraje para tu boca."
9. Botón CTA: "Send WhatsApp Message" → vincular al número dedicado (cuando Gaby compre chip)
10. Info:
    - Dirección: [completar con dirección del consultorio]
    - Horario: Lun-Vie 14:30-19:00
    - Web: https://ometzdental.com
    - Email: contacto@ometsdental.com.py
    - WA: [cuando chip listo]
11. URL: facebook.com/ometsdental

**Tiempo:** 30 min

---

### B. Instagram @ometsdental

**Owner:** Kiki

**Pasos:**

1. Crear cuenta profesional (no personal) en app IG
2. Username: `@ometsdental`
3. Nombre mostrado: "Ometz Dental · Dra. Gaby González Pane"
4. Bio:
   > "אומץ — coraje para tu boca.
   > Odontología con criterio · conservadora · planificada.
   > +20 años · Asunción 🇵🇾
   > ⬇️ Agendá tu cita"
5. Foto perfil: círculo con logo
6. Link en bio: https://linktr.ee/ometsdental (linktree gratis con links a WA, web, Maps)
7. Cuenta profesional (no Creator)
8. Categoría: "Dentist"

**Tiempo:** 15 min

---

### C. Google Business Profile (GBP)

**Owner:** Iván (tiene acceso a VPS)

**Pasos:**

1. Ir a https://business.google.com
2. Reclamar o crear perfil "Ometz Dental"
3. Verificación por postcard (Google envía carta con PIN a dirección)
4. Categoría principal: "Dentist"
5. Categorías secundarias: "Cosmetic Dentist", "Dental Clinic", "Oral Surgeon"
6. Horario: Lun-Vie 14:30-19:00
7. Descripción (750 char):
   > "Ometz Dental es un consultorio odontológico boutique en Asunción. Ofrecemos atención con criterio clínico, conservadora y planificada. Especialidad en rehabilitación oral, segunda opinión formal, operatoria dental y estética. La Dra. Gabriella González Pane tiene más de 20 años de experiencia. אומץ — coraje para tu boca. Te escuchamos."
8. Atributos:
   - Identifica como: "mujer-owned" (no aplicar si no querés)
   - Accesibilidad: "wheelchair accessible"
   - Servicios: "limpieza", "blanqueamiento", "rehabilitación oral", "operatoria"
9. Fotos: fachada, interior, equipo, logo (cargar 5-10 mínimo)
10. Pedir reseñas: a pacientes satisfechos vía WA + QR en consultorio

**Tiempo:** 1h (más 2-4 semanas para verificación postcard)

---

### D. Pixel Meta instalado en sitio

**Owner:** Iván

**Pasos:**

1. https://business.facebook.com → Events Manager → Crear Pixel
2. Nombre: "Ometz Dental Pixel"
3. Instalar en sitio (ometzdental.com) vía GTM o directo
4. Eventos a trackear:
   - PageView (todas las páginas)
   - Lead (cuando alguien llena formulario)
   - Contact (cuando hace clic en WA)
   - Schedule (cuando usa Calendly)
5. Verificar con Meta Pixel Helper (Chrome extension)

**Snippet ejemplo (header del sitio):**
```html
<!-- Meta Pixel Code -->
<script>
!function(f,b,e,v,n,t,s)
{if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', '[PIXEL_ID]');
fbq('track', 'PageView');
</script>
<noscript><img height="1" width="1" alt="" src="https://www.facebook.com/tr?id=[PIXEL_ID]&ev=PageView&noscript=1"/></noscript>
<!-- End Meta Pixel Code -->
```

**Tiempo:** 1-2h

---

### E. Google Analytics 4 (GA4) instalado en sitio

**Owner:** Iván

**Pasos:**

1. https://analytics.google.com → Crear propiedad
2. Nombre: "Ometz Dental Web"
3. URL: https://ometzdental.com
4. Zona horaria: America/Asuncion
5. Moneda: PYG
6. Crear stream "Web"
7. Copiar Measurement ID (formato: G-XXXXXXXXXX)
8. Instalar vía GTM o directo

**Snippet ejemplo (header del sitio):**
```html
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', 'G-XXXXXXXXXX');
</script>
```

**Configuración adicional recomendada:**
- Enhanced Measurement activado (scroll, click, etc)
- Eventos custom:
  - `wa_click` cuando hace clic en botón WA
  - `form_submit` cuando envía formulario
  - `phone_click` cuando hace clic en teléfono

**Tiempo:** 1-2h

---

### F. Google Search Console

**Owner:** Iván

**Pasos:**

1. https://search.google.com/search-console
2. Agregar propiedad: `https://ometzdental.com`
3. Verificar (vía DNS TXT o archivo HTML)
4. Submit sitemap: https://ometzdental.com/sitemap.xml
5. Configurar dominio preferido: ometzdental.com (sin www)

**Tiempo:** 30 min

---

### G. Meta Business Suite ↔ Instagram vinculado

**Owner:** Kiki

**Pasos:**

1. https://business.facebook.com → Settings → Accounts → Instagram accounts
2. Connect Instagram @ometsdental
3. Aceptar permisos
4. Verificar que IG se pueda gestionar desde Meta Business Suite

**Tiempo:** 15 min

---

### H. WhatsApp Business ↔ Facebook vinculado

**Owner:** Iván (cuando chip listo)

**Pasos:**

1. WA Business app → Settings → Business tools → Facebook & Instagram
2. Conectar con Fan Page
3. Activar "Click-to-WA" ads (cuando hagamos Ads)

**Tiempo:** 15 min

---

## 📋 CHECKLIST EJECUCIÓN

| # | Tarea | Owner | Tiempo | Status |
|---|---|---|---|---|
| A | Facebook Page | Iván + Kiki | 30 min | 🟡 Pendiente |
| B | Instagram @ometsdental | Kiki | 15 min | 🟡 Pendiente |
| C | GBP | Iván | 1h + 2-4 sem | 🟡 Pendiente |
| D | Pixel Meta | Iván | 1-2h | 🟡 Pendiente |
| E | GA4 | Iván | 1-2h | 🟡 Pendiente |
| F | Search Console | Iván | 30 min | 🟡 Pendiente |
| G | Meta Suite ↔ IG | Kiki | 15 min | 🟡 Pendiente |
| H | WA Business ↔ FB | Iván | 15 min | 🟡 Pendiente chip |

**Total estimado:** 5-7h de trabajo técnico de Iván + 1h de Kiki

---

## 🚨 BLOQUEANTES para esta semana

1. **Chip dedicado WA Business** (lo compra Gaby)
2. **Logo Ometz** (lo diseña Luana — usar placeholder hasta entonces)
3. **Dirección exacta del consultorio** (completar Gaby)
4. **Fotos fachada + interior** (las toma Iván al ir al consultorio o Gaby)

---

## 📋 Una vez todo configurado

1. ✅ Probar que cada link funciona
2. ✅ Probar Pixel con Meta Pixel Helper
3. ✅ Probar GA4 con Google Tag Assistant
4. ✅ GBP: esperar postcard (2-4 semanas)
5. ✅ Publicar primer post FB + IG según calendario de contenido
6. ✅ Configurar respuestas automáticas WA Business (quick replies v2)
7. ✅ Kiki monitorea primer día de actividad

---

*Setup técnico · Iván (Ai-Whisperers) · 13 jul 2026*
*Pendiente: ejecutar esta semana*