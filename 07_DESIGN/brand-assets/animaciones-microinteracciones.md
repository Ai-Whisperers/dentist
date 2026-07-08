# ANIMACIONES Y MICRO-INTERACCIONES — OMETZ DENTAL
## Sistema de movimiento + plan de implementación
**Versión:** 1.0 — Julio 2026

---

## 🎯 OBJETIVO

Definir un **sistema de movimiento coherente** para todos los touchpoints digitales de Ometz Dental. Las animaciones comunican **personalidad**: demasiado = distractoras, muy poco = anticuadas. El sweet spot es **animaciones sutiles que premian al usuario sin pedirle atención**.

> **Principio guía:** cada animación debe tener un propósito (feedback, jerarquía, narrativa). Sin propósito = ruido.

---

## 📚 SISTEMA DE ANIMACIÓN EN 4 CAPAS

### Capa 1 — HOVER STATES (mouse sobre elemento)
**Duración:** 150-250ms
**Easing:** `ease-out`
**Uso:** botones, links, cards interactivas

| Elemento | Animación |
|----------|-----------|
| **Botón primario** | Fondo se oscurece 10% + ligero translate-y (-2px) |
| **Botón secundario** | Borde aparece + color texto cambia |
| **Link de texto** | Subrayado aparece de izquierda a derecha |
| **Card de servicio** | Sombra se intensifica + ligero scale (1.02) |
| **Imagen** | Escala 1.05 + filtro de saturación +5% |

### Capa 2 — ENTRADA (elementos aparecen en viewport)
**Duración:** 400-700ms
**Easing:** `cubic-bezier(0.16, 1, 0.3, 1)` (curva "out-expo", da sensación premium)
**Trigger:** scroll into view (IntersectionObserver)

| Elemento | Animación |
|----------|-----------|
| **Heading principal** | Fade-in + translate-y (20px → 0) |
| **Subheading** | Fade-in + translate-y (10px → 0) con delay 100ms |
| **Card de servicio** | Fade-in + translate-y (30px → 0) con stagger 80ms entre cards |
| **Imagen hero** | Fade-in lento + scale (1.05 → 1) |
| **Lista de items** | Fade-in stagger 60ms |

### Capa 3 — NARRATIVA (transiciones entre pantallas/estados)
**Duración:** 500-1000ms
**Easing:** `cubic-bezier(0.65, 0, 0.35, 1)` (curva "in-out")
**Uso:** navegación entre páginas, modales, cambios de estado

| Elemento | Animación |
|----------|-----------|
| **Cambio de página** | Fade-out página actual (200ms) → fade-in página nueva (300ms) |
| **Modal abierto** | Backdrop fade-in (200ms) + modal scale (0.95 → 1) + fade-in (300ms) |
| **Modal cerrado** | Modal scale (1 → 0.95) + fade-out (200ms) → backdrop fade-out (200ms) |
| **Tab switch** | Underline animado a la nueva tab (300ms) + content fade-in (200ms) |

### Capa 4 — FEEDBACK (respuesta a acciones del usuario)
**Duración:** 100-300ms
**Easing:** `ease-out`
**Uso:** confirmaciones, errores, loading

| Elemento | Animación |
|----------|-----------|
| **Botón submit** | Spinner aparece + texto cambia a "Enviando..." |
| **Confirmación éxito** | Check aparece con scale + bounce |
| **Error validación** | Shake horizontal (3 oscilaciones) + mensaje aparece |
| **WhatsApp button click** | Pulse + redirect inmediato |
| **Hover icon** | Rotate 360° (subtle, no molesto) |

---

## 🚫 LO QUE NO VAMOS A HACER

| Anti-patrón | Por qué evitarlo |
|-------------|------------------|
| ❌ **Video autoplay con sonido** | Mata mobile, molesta, baja PageSpeed |
| ❌ **Parallax extremo** | Mareante en mobile, baja performance |
| ❌ **Animaciones que bloquean interacción** (>500ms) | Usuario impaciente, se va |
| ❌ **Bouncy / elástico en elementos serios** | Inadecuado para salud |
| ❌ **Texto que se escribe solo (typewriter)** | Cliche, distrae |
| ❌ **Cursor custom** | Solo confunde en desktop |
| ❌ **Loader infinito sin escape** | Usuario frustrado |
| ❌ **Animaciones en cada scroll** | Mareante, mata performance |
| ❌ **3D / WebGL innecesario** | Cuesta performance, distrae del mensaje |
| ❌ **Skeleton screens parpadeando** | Ansiedad, baja UX |

---

## 🎬 ANIMACIONES POR CONTEXTO

### Sitio web (Next.js)

#### Hero (primera impresión)
```javascript
// Implementación Tailwind + Framer Motion
// Hero fade-in inicial al cargar
const heroVariants = {
  hidden: { opacity: 0, y: 20 },
  visible: {
    opacity: 1,
    y: 0,
    transition: {
      duration: 0.8,
      ease: [0.16, 1, 0.3, 1], // out-expo
      staggerChildren: 0.1
    }
  }
};
```
- ✅ Foto de Gaby fade-in + scale sutil (1 → 1.02 → 1)
- ✅ "Te escucho." fade-in + translate-y (20px → 0)
- ✅ Subhead fade-in + delay 200ms
- ✅ CTA button fade-in + delay 400ms + scale pulse

#### Sección "Meet the doctor"
- ✅ Scroll into view: cards fade-in stagger
- ✅ Foto de Gaby slide-in desde izquierda
- ✅ Bio fade-in desde derecha

#### Sección "Differentiation table" (Dr. Gabriella vs Typical clinic)
- ✅ Headers sticky al scroll
- ✅ Rows highlight on hover (background fade-in 150ms)
- ✅ Columna "Dra. Gabriella" tiene fondo teal permanente

#### Sección FAQ
- ✅ Click en pregunta: answer slide-down (300ms)
- ✅ Icono + rota a 45° (se vuelve ×)
- ✅ Hover en pregunta: background color fade

#### WhatsApp button (sticky)
- ✅ Aparece después de scroll 200px (fade-in + slide-up)
- ✅ Pulse animation cada 5s para llamar atención
- ✅ Hover: scale 1.05 + sombra más fuerte

#### Footer
- ✅ Background fade-in al cargar
- ✅ Links hover: underline animado izquierda → derecha

### Redes sociales (estáticas)

**FB/IG no soporta animaciones complejas en posts**, pero:
- ✅ **Videos cortos** (Reels/Stories) con texto overlay animado
- ✅ **Carousel posts** con micro-transición entre slides
- ✅ **Stories stickers** (encuesta, pregunta, slider)
- ❌ **NO usar Boomerang / animaciones de IG** en feed (se ven amateur)

### WhatsApp Business

- ❌ **NO enviar videos animados** (la mayoría de planes no lo soportan)
- ✅ **Enviar imagen PNG/JPG** para mensajes visuales
- ✅ **Documentos PDF** para planes de tratamiento
- ✅ **Stickers oficiales** de WhatsApp (cuando haya para empresas)

### Email

- ✅ **GIFs animados sutiles** en hero del email (máximo 1, <500KB)
- ✅ **Botón CTA con hover state animado**
- ❌ **NO usar parallax** (no funciona en todos los clientes email)
- ❌ **NO usar video embed** (Outlook no lo soporta)

---

## 🛠️ IMPLEMENTACIÓN TÉCNICA WEB

### Stack recomendado

| Necesidad | Librería | Por qué |
|-----------|----------|---------|
| Animaciones simples | **CSS + Tailwind transitions** | Cero JS, performance óptimo |
| Animaciones de scroll | **Framer Motion** (Next.js) | API declarativa, accesible |
| Animaciones SVG | **Lottie React** | Animaciones vectoriales escalables |
| Animaciones de carga | **next/image** + skeleton | Built-in Next.js |
| Page transitions | **Framer Motion AnimatePresence** | Maneja exit + enter |

### Ejemplo — botón con hover animado

```jsx
// components/Button.jsx
import { motion } from 'framer-motion';

export const Button = ({ children, onClick, variant = 'primary' }) => {
  const variants = {
    primary: 'bg-teal-600 text-white hover:bg-teal-700',
    secondary: 'border border-teal-600 text-teal-600 hover:bg-teal-50',
  };

  return (
    <motion.button
      whileHover={{ y: -2, scale: 1.02 }}
      whileTap={{ scale: 0.98 }}
      transition={{ duration: 0.2, ease: 'easeOut' }}
      className={`px-6 py-3 rounded-lg font-semibold transition-colors ${variants[variant]}`}
      onClick={onClick}
    >
      {children}
    </motion.button>
  );
};
```

### Ejemplo — sección con scroll reveal

```jsx
// components/RevealSection.jsx
import { motion } from 'framer-motion';

export const RevealSection = ({ children, delay = 0 }) => (
  <motion.div
    initial={{ opacity: 0, y: 30 }}
    whileInView={{ opacity: 1, y: 0 }}
    viewport={{ once: true, margin: '-100px' }}
    transition={{
      duration: 0.7,
      ease: [0.16, 1, 0.3, 1],
      delay,
    }}
  >
    {children}
  </motion.div>
);
```

---

## ♿ ACCESIBILIDAD (WCAG 2.2 AA)

### Respetar `prefers-reduced-motion`

Usuarios con sensitivities necesitan que se respete su preferencia de OS:

```css
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

```jsx
// Framer Motion respeta automáticamente con useReducedMotion
import { useReducedMotion } from 'framer-motion';

const Component = () => {
  const prefersReducedMotion = useReducedMotion();
  // ...
};
```

### Otras reglas

- ✅ **Foco visible siempre** — outline 2px teal cuando se tabula
- ✅ **Contraste suficiente** — texto animado debe seguir siendo legible
- ✅ **NO animar información crítica** — no se puede pausar mensajes importantes
- ✅ **Subtítulos en todo video** — para usuarios sordos

---

## 📊 PERFORMANCE BUDGET

| Métrica | Objetivo | Herramienta |
|---------|----------|-------------|
| **First Contentful Paint** | <1.5s | Lighthouse |
| **Largest Contentful Paint** | <2.5s | Lighthouse |
| **Cumulative Layout Shift** | <0.1 | Lighthouse |
| **Total Blocking Time** | <200ms | Lighthouse |
| **JS bundle size** | <100KB gzipped | Webpack Analyzer |
| **Animations on first load** | Máximo 3 | Manual review |

> **Regla:** si la animación impacta el LCP o CLS, **sacarla**.

---

## 📋 CHECKLIST DE IMPLEMENTACIÓN

### Para cada nueva página del sitio:
- [ ] Hero animado al cargar (máximo 1s)
- [ ] Secciones con scroll-reveal staggered
- [ ] Hover states en todos los elementos interactivos
- [ ] Sticky WhatsApp button con pulse
- [ ] Footer con links animados
- [ ] Respeta `prefers-reduced-motion`
- [ ] Lighthouse Performance > 90
- [ ] Lighthouse Accessibility > 95

### Para cada nuevo post de redes:
- [ ] Sin animaciones pesadas (es feed estático)
- [ ] Si es Story/Reel: motion design intencional, no aleatorio
- [ ] Subtítulos si tiene voz
- [ ] Duración <30s (Reels), <15s (Stories)

---

## 🎯 PRIORIDAD DE IMPLEMENTACIÓN (orden recomendado)

### Sprint 1 (semana 1-2 post-aprobación)
1. ✅ Hover states en botones principales
2. ✅ WhatsApp button sticky con pulse
3. ✅ Hero fade-in al cargar
4. ✅ Respeta `prefers-reduced-motion`

### Sprint 2 (semana 3-4)
5. ✅ Scroll-reveal en secciones
6. ✅ FAQ accordion animado
7. ✅ Modal animado (form de contacto)
8. ✅ Page transitions entre rutas

### Sprint 3 (mes 2)
9. ✅ Micro-interacciones avanzadas en cards
10. ✅ Loading states elegantes
11. ✅ Lottie animations para iconos especiales
12. ✅ Animación especial de אומץ (sutil)

---

## 🔗 CRUZAR CON OTROS DOCUMENTOS

- `07_DESIGN/brand-assets/assets/character-templates.md` — sistema visual
- `07_DESIGN/brand-assets/moodboards-3-direcciones-visuales.md` — mood
- `06_MARKETING/website-full-specification.md` — web spec
- `06_MARKETING/calendar/calendario-marketing-2026-completo.md` — calendario
- `06_MARKETING/digital-marketing-playbook.md` — playbook

---

**STATUS:** v1.0 — sistema definido. Pendiente: implementar cuando se apruebe la dirección visual.