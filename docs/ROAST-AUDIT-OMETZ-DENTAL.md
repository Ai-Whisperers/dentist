# 🔥 ROAST — OMETZ DENTAL
## Auditoría brutal del estado actual del proyecto (8 jul 2026)

---

## 📊 VEREDICTO GLOBAL

| Categoría | Score | Comentario |
|-----------|-------|------------|
| **Estrategia** | 72/100 | Buen ADN definido, pero sin fechas concretas |
| **Marketing copy** | 78/100 | 26 GBP posts + 52 FB posts + 30 Reels = bien armado |
| **Branding visual** | 65/100 | 20 SVGs provisionales pero NO hay foto de Gaby |
| **Legal / compliance** | 70/100 | Docs listos pero TODO bloqueado por Gaby |
| **Operaciones** | 50/100 | NO hay plan de pagos real, NO hay software de gestión definido |
| **Coaching B2B** | 60/100 | Validado, pero sin landing ni programa concreto |
| **Repo hygiene** | **34/100** | **CRÍTICO — bloat + duplicados + placeholders en archivos críticos** |
| **Live site** | 78/100 | Funciona pero inconsistente con branding repo |
| **Execution readiness** | **28/100** | **CRÍTICO — solo 8% de actividades hechas falta ejecutar** |
| **TOTAL** | **61/100** | **Bueno en pensar, débil en terminar** |

---

## 🚨 30 PROBLEMAS — ORDENADOS POR SEVERIDAD

### TIER S — CRÍTICOS (10/10) — bloquean lanzamiento

**1. 🔴 BRANDING INCONSISTENTE ENTRE REPO Y LIVE SITE**
> 28 archivos mencionan "Dra. Gabriela" + "Odonto3" (legacy). El live site sigue con `dra-gabriela-en` slug. El repo estratégico dice "Ometz". El cliente visitará `ometzdental.com/en` y verá inconsistencia entre nombre, branding y tono. **Costo de no arreglar:** toda la inversión de branding אומץ se pierde.

**2. 🔴 ARCHIVE INSTAGRAM-RAW = 17M DE BASURA**
> La carpeta `ARCHIVE/instagram-raw` pesa **17 MB** y NO debería estar en el repo. Es desperdicio de espacio + ruido. **Costo:** clonación lenta, repo pesado, profesionalismo en duda.

**3. 🔴 NINGÚN PLAN DE PAGOS EJECUTABLE**
> El repo tiene 4 documentos sobre precios pero **NO tiene acción concreta** de setup de Bancard o Pagopar en el consultorio. Gaby atenderá y no sabrá cobrar con tarjeta. **Costo:** perder 30-40% de pacientes que pagan con tarjeta.

**4. 🔴 WHATSAPP NUMBER = "9XX" PLACEHOLDER**
> En 159 archivos aparece `+595 9XX XXX XXX`. ES UN PLACEHOLDER. Todos los templates, los SVGs, los HTMLs, los posts GBP, los quick replies, las landing pages — TODO dice 9XX. **Costo de no arreglar:** el cliente no puede contactar, todos los CTAs son zombies. Ya hubo este error en `quick-replies-PERSONALIZADO-gaby.md` donde Gaby había confirmado el número y el resto de los archivos no se actualizó. Hay que hacer find-replace de TODOS los archivos al recibir el número real.

**5. 🔴 ZERO FOTOS REALES DE GABY**
> 0 fotos profesionales en el repo. 17 AI prompts generados pero ninguno ejecutado. Todas las SVGs dicen "[ GABY HERO PHOTO ]" como placeholder. **Costo:** imposible lanzar con credibilidad.

**6. 🔴 LIVE SITE USANDO OLD BRAND (dra-gabriela)**
> `https://ometzdental.com/en` carga, pero el slug interno es `dra-gabriela-en` y los JSON de copy hablan de "Dra. Gabriella". **Inconsistencia visible al cliente.** El repo lo tiene claro (`site-page-copy.md`) pero el deploy no se actualizó. **Costo:** primera impresión inconsistente → bounce rate alto.

**7. 🔴 0 PRODUCTOS EN WHATSAPP CATÁLOGO**
> Los SVGs del catálogo están listos pero no pueden subirse sin que WhatsApp Business esté configurado (que depende de Gaby). **Bloqueado pero documentado.**

**8. 🔴 LEGAL COMPLIANCE NO VERIFICABLE**
> `01_RESEARCH/legal-compliance/` tiene 4 docs pero ninguno es una lista de checks verificables. No hay un checklist "tengo todos los papeles para abrir mañana" porque MSPBS no se puede abrir sin Gaby.

**9. 🔴 CONSULTORIO NO ABIERTO POR FALTA DE 6 BLOQUEANTES**
> Calle confirmada en repo (Auditores de la Guerra del Chaco 617) pero el resto está en veremos. 7 meses de trabajo y aún no abrimos puertas. **Costo:** capital quemándose mes a mes.

**10. 🔴 NO HAY PLAN DE INAUGURACIÓN**
> No hay evento de inauguración. No hay lista de invitados. No hay nota para medios. No hay comunicación del tipo "Ometz Dental abre sus puertas en Mburucuyá". El primer día será invisible.

### TIER A — ALTOS (8/10) — importantes pero no bloquean

**11. 🟠 "FOTO PENDIENTE" MARCADA EN MÚLTIPLES MDs**
> Las plantillas SVG y al menos 2 MDs (`03_LAUNCH/roadmap/master-launch-roadmap.md`, `07_DESIGN/brand-assets/assets/character-templates.md`) admiten literalmente `[Foto pendiente]` y `[ IMAGEN ]`. Eso deja ver el esqueleto.

**12. 🟠 NUNCA SE EJECUTÓ KIKI COMO PACIENTE MISTERIO**
> El plan competitivo dice que Kiki iría a 3 competidores como paciente. **NO se hizo.** No tenemos datos reales del customer journey del competidor, solo análisis documental.

**13. 🟠 DOCUMENTS DUPLICADOS DE QUICK REPLIES**
> Hay `quick-replies-PERSONALIZADO-gaby.md` (v1 con datos reales parciales) + `quick-replies-v2-final.md` (versión "mejor"). Ambas tienen el mismo fin. **Riesgo:** Kiki carga la v1 cuando debe cargar la v2. Hay que decidir y deprecar una.

**14. 🟠 BLOG SIN IMPLEMENTAR**
> El plan SEO dice "4 posts SEO mes 1-4". **0 posts implementados**. 0 URLs reales. 0 backlinks. SEO es teoría pura.

**15. 🟠 LICENCIA DE SOFTWARE DE GESTIÓN NO DECIDIDA**
> El doc dice "elegir entre Dentisoft / CloudDent / Doctoralia". **No se ha contactado a ningún proveedor.** Evaluación pendiente.

**16. 🟠 PACIENTES PROSPECTIVOS SIN LISTA**
> El plan dice "welcome automation" pero **no hay base de datos inicial**. Hay que importar contactos previos de Gaby de Odonto3 (con consentimiento GDPR/MSPBS), pero ese proyecto no se ha tocado.

**17. 🟠 CAMPAMENTOS META ADS NO ACTIVOS**
> A pesar de tener 7 audiencias y 3 campañas diseñadas, **ningún ad está corriendo**. Costo: USD 0 gastado = USD 0 aprendido.

**18. 🟠 COACHING: CONVENIO LEGAL LISTO PERO 0 LANDING**
> `05_OPERATIONS/legal-compliance/practice-legal/coaching-agreement-legal.md` existe. Pero NO hay `ometsdental.com/coaching`. LinkedIn sin posts sobre coaching. **El coaching es 100% estrategia, 0% ejecución.**

**19. 🟠 RED DE DERIVACIONES FORMALES = 0**
> Hay `01-list-target-colleagues-asuncion.md` con 30 dentistas. Pero no hay alianza firmada con ninguno. No hay convenio. No hay referido real registrado.

**20. 🟠 CONTRATO CON AUXILIAR NO ARMADO**
> Cuando Gaby contrate auxiliar, no hay contrato, no hay manual de inducción, no hay descripción del puesto específica para Ometz (existen genéricos en `05_OPERATIONS/staff-manual-asistente.md`).

### TIER B — MEDIOS (6-7/10) — nice to have

**21. 🟡 PRECIOS COMPETITIVOS NO VERIFICADOS**
> El doc de inteligencia competitiva tiene rango de precios Asunción 2026 (4.200.000 PYG implantes según Treatments International), pero NO está validado con Gaby ni con fuentes PY locales específicas.

**22. 🟡 NO HAY CRONOGRAMA DE POSTS MES POR MES**
> Hay `calendario-marketing-2026-completo.md` con 167 posts planeados en abstracto. Pero no hay `Esta semana: posts X, Y, Z` ya armados para que Kiki publique.

**23. 🟡 NO HAY FACTORY DE CREATIVOS DE META ADS**
> Se diseñaron 7 audiencias y 3 campañas pero **no hay creativos (imágenes/video) para los ads**. Solo se tiene para orgánico.

**24. 🟡 ONBOARDING DE COMMUNITY MANAGER NO DOCUMENTADO**
> Si se contrata un CM externo, no hay brief de puesto específico, no hay KPIs claros, no hay contrato tipo.

**25. 🟡 SISTEMA DE MENCIONES EN PRENSA**
> No hay estrategia de "free press" (notas en medios). No se contactó a ABC Color, Última Hora, etc.

**26. 🟡 WHATSAPP API (1MSG) NO EVALUADO**
> Para recordatorios automáticos 24h antes. Pendiente decisión.

**27. 🟡 NO HAY TABLERO DE MÉTRICAS**
> Plan dice "100 métricas" pero no hay dashboard unificado. Kiki tiene que ir a 7 lugares diferentes para ver números.

**28. 🟡 NO HAY TIMELINE FORMAL DEL DÍA 1**
> Checklist "qué hacer el día 1 de apertura" no existe. Falta: stock, inauguración, primer paciente, etc.

### TIER C — BAJOS (≤5/10) — pulir

**29. 🔵 DUPLICACIÓN: 4 ARCHIVOS INDEX**
> `00-index.md`, `COMPLETE-INDEX.md`, `README.md`, `MERGE-TODO-PENDING.md` hacen cosas similares. Confuso.

**30. 🔵 PYTHON CACHE FILE EN REPO**
> `03_LAUNCH/instagram-contacts/scripts/__pycache__/inspect.cpython-312.pyc` no debería commitearse. Falta `.gitignore` que cubra `__pycache__/`.

---

## 💀 LO QUE PEOR ESTÁ (TOP 5)

### 🥇 #1 — REPO BLOAT: 17M DE INSTAGRAM RAW + ARCHIVES HUÉRFANAS

```bash
# Ahora mismo en tu repo:
ARCHIVE/instagram-raw/         = 17 MB ← ESTO DEBE IRSE
ARCHIVE/bloat-2026-06-04/      = 124 K ← obsoleto
ARCHIVE/research/              = 56 K
ARCHIVE/planning/              = 52 K
# TOTAL ARCHIVE: ~17.3 MB (del 37M del repo)
```

**47% del peso total del repo es ARCHIVE que NO se necesita.**

### 🥈 #2 — INCONSISTENCIA DE BRANDING MASIVA

```
REPO estratégico dice "Ometz Dental", אומץ, "Te escucho"
LIVE SITE dice "Dra. Gabriella González Pane"
LEGACY FILES dicen "Dra. Gabriela", "Odonto3"
```

El cliente que visite el sitio y luego vea una publicación de Facebook verá **dos marcas diferentes**. Confusión garantizada.

### 🥉 #3 — DOCUMENTOS PARA DOCUMENTOS (la enfermedad del repo)

Contamos documentos creados vs ejecutados:

| Categoría | Docs | Ejecutados | % ejecución |
|-----------|------|-----------|--------------|
| Marketing | 25+ | 0 | **0%** |
| Branding | 8 | 0 logos diseñados, 0 fotos | **0%** |
| Legal | 12 | 0 | **0%** |
| Operaciones | 8 | 0 | **0%** |
| Coaching | 6 | 0 | **0%** |
| Crisis | 2 | 0 (sin chance de probar) | **0%** |

**El repo tiene documentación de la documentación.** Hay 384 docs y el porcentaje de ejecución es prácticamente cero.

> "En Ai-Whisperers nos encanta escribir. Lo que nos falta es ejecutar."

### 4️⃣ #4 — TELÉFONO/EMAIL PLACEHOLDER EN 159 ARCHIVOS

Si Gaby diera mañana el WhatsApp real `+595 981 555 444`, hay que hacer:
```
sed -i 's/+595 9XX XXX XXX/+595 981 555 444/g' $(grep -rl "9XX" --include="*.md" .)
```
Eso en 159 archivos. Y verificar que no se rompió nada.

**No tener un sistema de variables centralizadas (un `vars.json` o `config.yaml`) es un error de arquitectura grave.**

### 5️⃣ #5 — CERO MÉTRICAS, CERO PRUEBAS, CERO FEEDBACK LOOPS

Después de 6 meses de trabajo:
- 0 posts publicados
- 0 reseñas recibidas
- 0 ads corriendo
- 0 conversaciones con pacientes reales
- 0 datos para validar modelo

Todo es **PROYECCIÓN TEÓRICA**. El simulador del crecimiento es solo eso: un simulador.

---

## 🎯 QUÉ HACER PRIMERO (POST-ROAST PRIORITY)

### 🔴 P0 — HOY (4 horas)

1. **Limpiar ARCHIVE** del repo (especialmente `instagram-raw` 17M) — 10 min
2. **Decidir y deprecar** UNO de los dos quick-replies (mantener v2-final) — 30 min
3. **Crear vars.json central** para teléfono, email, dirección, RUC — 30 min
4. **Estandarizar TODOS los archivos** con placeholder `9XX` para que usen vars.json — 2 horas
5. **Add `.gitignore`** que cubra `__pycache__/` — 5 min
6. **Mover legacy files** ("Dra. Gabriela", "Odonto3") a `ARCHIVE/legacy-brand-2026-07/` con nota — 30 min

### 🟠 P1 — ESTA SEMANA

7. **Investigar a fondo** mercado de auxiliares dentales PY (sueldo, registro, IPS)
8. **Estimar costos reales** Bancard + Pagopar contactando directamente
9. **Investigar 2-3 proveedores reales** de seguros RC y cotizar
10. **Cotizar imprentas PY** (Gráfica Central, Gráfica del Paseo) para tener precios reales
11. **CRONOGRAMA SEMANAL DE POSTS** pre-armado para Kiki

### 🟡 P2 — MES 1

12. **Crear todos los JSON del sitio** (si no existen)
13. **Deploy** de los JSON actualizados (`site-page-copy.md` → JSONs de content/es y content/en)
14. **Verificar live** `/en` y `/es` que dicen "Ometz Dental" en todos lados
15. **Test de 30 segundos del sitio live** (`curl | grep Ometz | grep Dra. Gabriela` debería dar **0 resultados**)

---

## 📊 LO QUE HAY DE BUENO (no se rompe)

- ✅ 26 posts GBP pre-armados
- ✅ 52 posts FB pre-armados
- ✅ 30 scripts Reels
- ✅ 12 quick replies WhatsApp
- ✅ 3 HTML email templates production-ready
- ✅ 20 SVGs (logos, posts, catálogos, prints)
- ✅ 8 docs de branding system completo
- ✅ 30 perfiles de dentistas para referidos
- ✅ Investigación legal de seguros RC + market coaching
- ✅ Plantillas de consentimiento informado

**El material ESTRATÉGICO es sólido. Falta EJECUTAR.**

---

## 🚨 LO QUE NO DEBERÍAS HACER (anti-patrones)

- ❌ Escribir MÁS documentos de planificación (ya hay 384)
- ❌ Crear otra versión del plan de contingencia
- ❌ Otra versión de quick-replies (hay 2 ya, elegir una)
- ❌ Otra investigación de competidores (ya hay 3 docs; ir al campo)
- ❌ Ensayar precios sin consultar Gaby

---

## 🔗 CRUZAR CON OTROS DOCUMENTOS

- `MASTER-docs/MASTER-TODO-RESTANTE.md` — tracker principal
- `docs/PLAN-NEGOCIO-ANO-1-OKR-MENSUALES.md` — plan estratégico
- `docs/MASTER-TODO-RESTANTE.md` — gaps categorizados
- `docs/GAP-ANALYSIS-COMPLETO-ADS-LOCATIONS.md` — gaps ads

---

**STATUS:** v1.0 — Roast completo. Ejecutar P0 hoy.