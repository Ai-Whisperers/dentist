# VARIABLES CENTRALES — OMETZ DENTAL
## Single source of truth para datos que se repiten en TODOS los archivos
**Versión:** 1.0 — 8 de julio 2026

> ⚠️ **ESTOS VALORES SON PLACEHOLDER.** Se actualizarán cuando Gaby confirme los datos reales. Pero TODOS los demás archivos deben referenciar estos valores en vez de hardcodearlos.

---

## 📋 DATOS BÁSICOS DEL CONSULTORIO

```yaml
brand:
  name: "Ometz Dental"
  short_name: "Ometz"
  trademark: "אומץ"
  tagline_es: "Te escucho."
  tagline_en: "I listen."
  tagline_explanation: "Antes de mirar tu boca, miro tu historia."

location:
  street: "Auditores de la Guerra del Chaco 617"
  neighborhood: "Mburucuyá"
  city: "Asunción"
  country: "Paraguay"
  country_code: "PY"
  google_maps: "https://maps.google.com/?q=Auditores+de+la+Guerra+del+Chaco+617+Asuncion"  # placeholder
  google_maps_embed: "https://www.google.com/maps/embed?..."  # placeholder

contact:
  # WhatsApp personal Gaby confirmado 6 jul 2026 — usar HASTA que compre Business
  whatsapp_personal: "+595981146759"   # ← CONFIRMADO 6 jul 2026 (TRANSITORIO)
  whatsapp_personal_formatted: "+595 981 146 759"
  whatsapp_personal_link: "https://wa.me/595981146759?text=Hola%20Dra.%20Gaby%2C%20me%20interesa%20agendar%20una%20consulta"
  # WhatsApp Business (chip nuevo) — pendiente compra
  whatsapp_raw: "+595981146759"   # ← REEMPLAZAR CUANDO GABY CONFIRME (semana 7 jul)
  whatsapp_formatted: "+595 981 146 759"   # ← display
  whatsapp_link: "https://wa.me/595981146759?text=Hola%20Dra.%20Gaby%2C%20me%20interesa%20agendar%20una%20consulta"
  phone_alt: "+595981146759"   # mientras tanto, mismo que personal
  email_professional: "doctora.gabi@ometsdental.com.py"   # ← CONFIRMADO 28 jun 2026
  email_alternate: "dra.gp.odontologia@gmail.com"   # legacy personal
  website_es: "https://ometzdental.com"
  website_en: "https://ometzdental.com/en"

hours:
  weekdays: "Lunes a viernes · 14:30 a 19:00"
  weekdays_short: "Lun-Vie 14:30-19:00"
  saturday: "Cerrado"
  sunday: "Cerrado"

doctor:
  full_name: "Dra. Gabriella González Pane"
  short_name: "Dra. Gaby"
  english_name: "Dr. Gabriella González Pane"
  title_es: "Odontóloga · Rehabilitación Oral · Segunda Opinión"
  title_en: "Dentist · Oral Rehabilitation · Second Opinion"
  registration_mspbs: "3618"   # ← CONFIRMAR VIGENTE
  years_experience: 20
  languages: ["Español", "English"]

social:
  facebook: "https://facebook.com/ometsdental"
  facebook_handle: "@ometsdental"
  instagram: ""  # NOT active yet
  linkedin_personal: "https://linkedin.com/in/dra-gaby-ometz"
  linkedin_company: "https://linkedin.com/company/ometsdental"
  youtube: ""  # NOT active yet
  tiktok: ""   # NOT active yet

services:
  consulta_general:
    name_es: "Consulta General"
    name_en: "General Consultation"
    desc_short: "Evaluación clínica completa 45-60 min"
    price_min: 300000
    price_max: 400000
    currency: "PYG"

  segunda_opinion:
    name_es: "Segunda Opinión"
    name_en: "Second Opinion"
    desc_short: "Plan escrito formal en 2-3 días"
    price_min: 450000
    price_max: 600000
    currency: "PYG"

  profilaxis:
    name_es: "Profilaxis Completa"
    name_en: "Complete Prophylaxis"
    desc_short: "Limpieza profunda 40-50 min"
    price_min: 300000
    price_max: 400000
    currency: "PYG"

  blanqueamiento:
    name_es: "Blanqueamiento Consultorio"
    name_en: "In-Office Whitening"
    desc_short: "1 sesión 60-90 min · evaluación previa"
    price_currency_note: "Precio a confirmar en evaluación"
    currency: "PYG"

  restauracion:
    name_es: "Restauración"
    name_en: "Restoration"
    desc_short: "Resina compuesta · 30-60 min"
    price_min: 350000
    price_max: 550000
    currency: "PYG"

  rehabilitacion:
    name_es: "Plan de Rehabilitación"
    name_en: "Rehabilitation Plan"
    desc_short: "Plan escrito en fases · múltiples sesiones"
    price_min: 500000
    price_max: 800000
    currency: "PYG"

branding:
  palette:
    teal: "#1A5F5A"
    cream: "#FAFAF8"
    terracotta: "#B8860B"
    charcoal: "#2D2D2D"
    rose: "#D88C7A"
  fonts:
    primary: "Montserrat"
    hebrew: "Frank Ruhl Libre"
  fonts_weights:
    regular: "400"
    medium: "500"
    semibold: "600"
    bold: "700"
    black: "800"

competitor_benchmarks:
  implant_usd_low: 585
  pyg_to_usd: 7300
  implant_pyg_equivalent: 4200000
```

---

## 🔧 CÓMO USAR ESTAS VARIABLES

### Para SVGs y HTML
Reemplazar hardcoded values con referencias:

ANTES (hardcoded):
```html
<a href="https://wa.me/595981146759">📱 +595 981 146 759</a>
```

DESPUÉS (referencia):
```markdown
VER `config/variables-central.md` → contact.whatsapp_link + contact.whatsapp_formatted
```

### Para replacements automatizados
Si Gaby confirma el número real (ej. `+595 981 555 444`):

```bash
cd /tmp/dentist-repo
sed -i 's/+595 981 146 759/+595 981 555 444/g' $(grep -rl "9XX" --include="*.md" --include="*.svg" --include="*.html" .)
sed -i 's/595981146759/595981555444/g' $(grep -rl "595981146759" --include="*.md" --include="*.svg" --include="*.html" .)
sed -i 's/wa.me\/595981146759/wa.me\/595981555444/g' $(grep -rl "wa.me/595981146759" --include="*.md" --include="*.svg" --include="*.html" .)
```

---

## 📋 CUANDO UN DATO CAMBIA (protocol)

1. Iván/Kiki confirma el dato nuevo con Gaby
2. Iván/Kiki actualiza ESTE archivo con el dato nuevo
3. Ejecutar el script de find-replace arriba
4. Commit con mensaje: `chore(config): update {campo} → {nuevo_valor}`
5. Verificar con grep

---

## 🔗 CRUZAR CON OTROS DOCUMENTOS

- `MERGE-TODO-PENDING.md` — tarea de actualización
- `docs/ROAST-AUDIT-OMETZ-DENTAL.md` — hallazgo #4 que genera este archivo

---

**STATUS:** v1.0 — placeholder creado. Datos reales cuando Gaby responda.