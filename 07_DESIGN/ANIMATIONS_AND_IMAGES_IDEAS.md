# 15 Animation Ideas — Ometz Dental
**Para:** Iván + Gaby
**Status:** Elegí las que te gusten, marcalas con ✅

---

## Micro-interacciones (hover, click, scroll)

### 1. **Botón WhatsApp pulse** ✅ recomendado
El botón flotante de WhatsApp pulsa suavemente cada 3s para llamar la atención sin ser molesto. Animación de scale 1 → 1.05 → 1 con opacidad de un halo.

### 2. **Cards hover lift**
Las tarjetas de servicios/subtemas se elevan 4px con shadow más profunda al pasar el mouse. Sutil, no brusco.

### 3. **Icon rotate on hover**
Los íconos de servicios rotan 15° al hover. Les da vida sin ser excesivo.

### 4. **Underline grow en nav links**
Los links del nav tienen un underline que crece de izquierda a derecha al hover (200ms).

### 5. **Number counter en stats**
Los números en "20+ años / <24h reply" cuentan desde 0 cuando entran al viewport.

---

## Scroll-triggered (cuando el usuario scrollea)

### 6. **Fade-in-up en secciones** ✅ recomendado
Cada sección aparece con `opacity 0 → 1` + `translateY 20px → 0` cuando entra al viewport. Stagger de 100ms entre hijos.

### 7. **Parallax sutil en hero**
El hero tiene un background gradient que se mueve 20% más lento que el scroll. Da profundidad sin marear.

### 8. **Sticky navbar shrink**
La navbar reduce su altura de 80px → 60px cuando scrolleas más allá del hero. Logo y links se ajustan.

### 9. **Step number reveal en "How it works"**
Los números 1-2-3-4 de los pasos aparecen uno a uno con un pequeño bounce cuando entran al viewport.

### 10. **Testimonial fade carousel**
Si hay varios testimonios, rotan automáticamente cada 6s con fade in/out.

---

## Page load (primera impresión)

### 11. **Logo draw-in**
El logo "OMETZ" se "dibuja" letra por letra con un stroke animation al cargar la página. Toma ~800ms.

### 12. **Hero text stagger**
"Hola, soy la Dra. Gaby" aparece palabra por palabra (300ms total).

### 13. **Floating dental icons background**
Íconos dentales muy tenues (tooth, mirror) flotan lentamente en el background del hero. Opacity 0.05, animation infinita de 20s.

---

## Transiciones de página

### 14. **Smooth page transitions** ✅ recomendado
Al navegar entre páginas, fade-out → fade-in (200ms) en lugar del salto brusco default.

### 15. **Loading skeleton en imágenes**
Mientras las imágenes cargan, muestran un skeleton shimmer (gradient que se mueve). Evita layout shift.

---

## Cuáles recomiendo para arrancar (low cost, high impact)

- ✅ **#1 WhatsApp pulse** — 5 min, alto impacto
- ✅ **#6 Fade-in-up secciones** — 10 min, alto impacto
- ✅ **#14 Smooth page transitions** — 15 min, alto impacto
- ✅ **#2 Cards hover lift** — 5 min, sutil

**Total implementación recomendada:** 4 animaciones, ~35 min de trabajo.

---

# 6 Ideas de Imágenes

## 1. **Hero principal — Foto de Gaby atendiendo (con paciente o sola)**
- **Plano medio**: Gaby de pie, sin bata, scrubs coloridos (los que ella usa), sonriendo levemente
- **Fondo**: Consultorio difuminado pero visible (luz natural, plantas, sillón dental)
- **Mensaje implícito**: "Soy una dentista real, cercana, estoy acá"
- **Alternativa IA**: Generar imagen con `image_generate` (DALL-E/FAL) con prompt: "Female dentist in colorful scrubs, warm smile, standing in modern dental office with natural light, Mburucuyá Asunción Paraguay"

## 2. **Clínica exterior — Fachada**
- **Plano general**: Fachada del consultorio en Auditores de la Guerra del Chaco 617
- **Mostrar**: Cartel de "Ometz Dental" si existe, entrada limpia, calle visible
- **Por qué**: Para Google Business + sección "Cómo llegar"

## 3. **Clínica interior — Sala de espera + consultorio**
- **2 fotos mínimo**: Sala de espera (sillón, planta, luz natural) + consultorio (sillón dental, luz Valo, sin paciente)
- **Por qué**: Reduce ansiedad del paciente nuevo. "Ya sé cómo es el lugar antes de ir"

## 4. **Retrato profesional de Gaby**
- **Plano medio corto**: Solo ella, fondo limpio (consultorio o pared blanca)
- **Vestimenta**: Smart casual o scrubs coloridos según la paleta que elija
- **Por qué**: Página "Sobre mí", sección author de Schema.org

## 5. **Antes/después — Casos documentados**
- **Mínimo 3 casos** (con consentimiento escrito del paciente): restauración, estética, rehabilitación
- **Formato**: Split image (antes | después) o slider interactivo
- **Por qué**: Demuestra expertise concreto, no solo palabras

## 6. **Foto "personal" de Gaby — Lifestyle fuera del consultorio**
- **Contexto**: Leyendo un libro, caminando, con un mate, en su casa
- **Por qué**: Humaniza. "Es una persona, no solo una doctora"
- **Sugerencia**: Café o parque, sonriendo, vestimenta casual

---

## Cuáles son prioritarios para el 26 jul (apertura)

| Prioridad | Imagen | Status |
|---|---|---|
| 🔴 Alta | #4 Retrato profesional | Necesario para Sobre mí + Schema |
| 🔴 Alta | #1 Hero principal | Sin esto el hero se ve vacío |
| 🟡 Media | #2 Fachada | Para Google Business |
| 🟡 Media | #3 Interior consultorio | Para sección "Conocé el consultorio" |
| 🟢 Post-apertura | #5 Antes/después | Después de tener 3+ pacientes |
| 🟢 Post-apertura | #6 Personal lifestyle | Nice-to-have |

**Acción inmediata (esta semana):**
- Sesión de fotos con Gaby (2 horas) → genera #1, #3, #4
- Sacar foto de la fachada con celular (#2) → la sacás vos cuando vayas

**IA como fallback**: si no podés sacar fotos reales esta semana, usamos `image_generate` con prompts descriptivos para tener placeholders decentes.