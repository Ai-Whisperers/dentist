# Cuestionario A — Respuestas de Gaby (WhatsApp, 6 jul 2026)

**Respondido por:** Dra. Gabriella González Pane
**Recibido vía:** WhatsApp de Kiki
**Fecha:** 6 jul 2026
**Procesado por:** Erebus (Hermes)
**Versión del cuestionario:** `07_DESIGN/website/validacion-minima-viable.md` (6 preguntas — aunque Kiki envió una variante con preguntas ligeramente distintas, las respuestas cubren los mismos datos críticos)

---

## Las 6 respuestas (transcripción literal)

### 1. Calle exacta del consultorio en Mburucuyá
> "auditores de la guerra del chaco 617"

**Interpretación normalizada:** `Auditores de la Guerra del Chaco 617, Barrio Mburucuyá, Asunción, Paraguay`
- Calle: **Auditores de la Guerra del Chaco**
- Número: **617**
- Sin piso/depto mencionado (asumimos casa/consultorio en planta baja — confirmar si hay unidad)

### 2. ¿La línea de WhatsApp Business ya la tenés o la comprás esta semana?
> "la compro en la semana la compro la semana que viene"

**Interpretación:** NO la tiene aún. La compra la semana del **7 jul 2026**.
- **Acción para Erebus:** el sitio debe seguir mostrando el WhatsApp actual (`+595 981 146 759` — su línea personal) hasta que compre la Business. Cuando compre, hacer swap atómico en `content/{en,es}/site.json` + redeploy.
- **Acción para Kiki:** recordarle a Gaby el viernes 10 jul si ya la compró, para hacer el swap antes del día 1.

### 3. ¿El RUC 1375421-1 está activo y al día?
> "si esta al dia"

**Interpretación:** ✅ RUC `1375421-1` confirmado activo y al día.
- **Acción para Erebus:** cambiar `site.json` → `registrations.ruc.state` de `"in-process"` a `"active"` y publicar el número `1375421-1` (en footer o página `/legal` para facturación).

### 4. ¿El registro MSPBS 3618 está vigente?
> "si esta vigente"

**Interpretación:** ✅ MSPBS `3618` confirmado vigente.
- **Acción para Erebus:** cambiar `site.json` → `registrations.mspbs.state` de `"in-process"` a `"active"` y publicar el número `3618` (en footer).

### 5. ¿Tenés seguro de responsabilidad civil profesional?
> "si supongo no se como esod debe ser0"

**Interpretación:** ⚠️ **No lo tiene.** Gaby interpretó "si supongo" como "sí, supongo que sí lo necesito" pero al final del audio reconoció que **no sabe cómo es eso** y lo dejó caer.
- **Acción para Kiki/Erebus:** AGREGAR A PENDIENTES CRÍTICOS. Sin seguro de RC profesional no debería atender. Bloquea la apertura formal.
- **Investigación a hacer:**
  - Aseguradoras en PY que cubran RC profesional odontológica (probablemente Mapfre, La Consolidada, Seguros Asunción)
  - Costo típico mensual
  - Cobertura mínima recomendable
- **Output esperado:** instructivo paso-a-paso `05_OPERATIONS/legal/seguro-responsabilidad-civil-guia.md` + agendado en P0 de Kiki para Gaby.

### 6. ¿Cuándo querés abrir formalmente?
> "antes de hmmm 26 de julio por ahi"

**Interpretación:** Target de apertura formal = **antes del 26 de julio de 2026** (le quedan ~20 días desde hoy 6 jul).
- **Acción para Erebus:** actualizar `site.json` → `launch.target_display` con countdown al 26 jul. Hoy + 20 días.
- **Acción para Kiki:** armar plan día 1 que apunte a esa fecha. Considerar semana anterior (20-25 jul) para soft launch con pacientes piloto (4-5 pacientes).

---

## Resumen — qué bloqueantes se destrabaron vs siguen abiertos

| # | Bloqueante | Estado |
|---|---|---|
| 1 | Calle exacta | ✅ **DESTRABADO** — Auditores de la Guerra del Chaco 617, Mburucuyá, Asunción |
| 2 | WhatsApp Business | ⏳ **Pendiente** — compra la semana del 7 jul |
| 3 | RUC activo | ✅ **DESTRABADO** — 1375421-1 confirmado al día |
| 4 | MSPBS vigente | ✅ **DESTRABADO** — 3618 confirmado vigente |
| 5 | Seguro RC profesional | ❌ **BLOQUEANTE NUEVO** — no lo tiene, no sabe qué es, hay que guiarle |
| 6 | Fecha de apertura | ⏳ **Target = antes del 26 jul 2026** (~20 días) |
| 7 | EAS + Timbrado | ❌ Sigue pendiente (no preguntado en cuestionario A) |
| 8 | ¿Community manager? | ❌ Sigue pendiente (no preguntado en cuestionario A) |

**4 de 6 destrabados. 1 bloqueo nuevo (seguro RC). 1 pendiente (WhatsApp Business).**

---

## Acciones generadas por este cuestionario

### Inmediato (commit hoy en `dentist`)
- ✅ Confirmar `site-config.json` con la calle, RUC, MSPBS, fecha
- ✅ Confirmar `business-card-design-spec.md` con la dirección
- ✅ Confirmar `social-media-profile-specs.md` con la dirección
- ✅ Crear este archivo como evidencia auditable

### Inmediato (commit hoy en `paragu-ai-platform`)
- ⏭ Portar calle, RUC, MSPBS, target date a `apps/dra-gabriela/content/{en,es}/site.json`
- ⏭ Rebuild + redeploy

### Esta semana (Kiki)
- 🟡 Recordatorio viernes 10 jul: ¿Gaby compró WhatsApp Business?
- 🔴 **NUEVO** — enviar guía de seguro RC profesional odontológico en PY

### Próxima semana (cuando compre WhatsApp Business)
- 🟢 Swap atómico del número en `site.json` + redeploy
- 🟢 Configurar quick replies v1 con la línea nueva

---

## Notas de auditoría

- Las respuestas vienen de audio de WhatsApp transcrito manualmente. Hay typos ("auditores" sin mayúscula, "esod" en vez de "eso") — son transcripción fiel, no se corrigieron.
- El cuestionario que Kiki envió a Gaby NO es exactamente el de `validacion-minima-viable.md` actual — la versión que Kiki usó tiene "calle", "WhatsApp", "RUC", "MSPBS", "seguro RC", "fecha apertura" en vez de las 6 del archivo actual ("WhatsApp", "teléfono", "dirección", "RUC", "MSPBS", "email"). El archivo actual tiene `email`; la versión que Kiki envió reemplazó email por "seguro RC" — **mejor pregunta, lo mantengo**.
- El email `doctora.gabi@ometzdental.com.py` ya está público en el sitio (del commit `2c6e6f3` + anteriores), no se pregunta acá pero ya está validado.