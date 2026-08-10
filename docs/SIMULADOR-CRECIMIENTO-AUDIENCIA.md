<parameter name="content"># SIMULADOR DE CRECIMIENTO DE AUDIENCIA
## Modelo predictivo para Ometz Dental
**Versión:** 1.0 — 8 de julio 2026
**Para:** Iván + Kiki (planning)

---

## 🎯 QUÉ RESUELVE

Predecir **cuán rápido crecerá la audiencia digital de Ometz** según escenarios de inversión en marketing.

---

## 📊 INPUTS DEL MODELO

### Escenario CONSERVADOR
- Inversión Meta Ads: USD 100/mes
- Frecuencia posting: 3/semana
- Engagement rate: 3%
- Crecimiento orgánico: bajo (sin viralidad)

### Escenario BASE
- Inversión Meta Ads: USD 300/mes
- Frecuencia posting: 5/semana (incluye Stories)
- Engagement rate: 5%
- Crecimiento orgánico: medio

### Escenario AGRESIVO
- Inversión Meta Ads: USD 600/mes
- Frecuencia posting: 1/día
- Engagement rate: 6%
- Inversión en Reels + boost

---

## 📈 PROYECCIÓN DE FOLLOWERS FACEBOOK

### Mes 0 → Mes 12 (conservador)

| Mes | Followers FB | Mes | Followers FB |
|-----|--------------|-----|--------------|
| 0 | 0 | 7 | 280 |
| 1 | 50 | 8 | 340 |
| 2 | 95 | 9 | 410 |
| 3 | 140 | 10 | 480 |
| 4 | 180 | 11 | 555 |
| 5 | 220 | 12 | 630 |
| 6 | 250 | | |

### Mes 0 → Mes 12 (base)

| Mes | Followers FB | Mes | Followers FB |
|-----|--------------|-----|--------------|
| 0 | 0 | 7 | 720 |
| 1 | 80 | 8 | 880 |
| 2 | 200 | 9 | 1050 |
| 3 | 330 | 10 | 1230 |
| 4 | 460 | 11 | 1420 |
| 5 | 580 | 12 | 1620 |
| 6 | 650 | | |

### Mes 0 → Mes 12 (agresivo)

| Mes | Followers FB | Mes | Followers FB |
|-----|--------------|-----|--------------|
| 0 | 0 | 7 | 1450 |
| 1 | 150 | 8 | 1820 |
| 2 | 380 | 9 | 2230 |
| 3 | 620 | 10 | 2700 |
| 4 | 870 | 11 | 3200 |
| 5 | 1100 | 12 | 3750 |
| 6 | 1270 | | |

---

## 💬 MESSAGING MESSAGES / MES

### Modelo

```
mensajes_mes = (follower_base × 0.5% conversion_wa) + ads_wa_clicks
```

### Mensajes proyectados

| Mes | Conservador | Base | Agresivo |
|-----|-------------|------|----------|
| 1 | 50 | 100 | 180 |
| 3 | 70 | 200 | 380 |
| 6 | 100 | 300 | 650 |
| 9 | 130 | 400 | 900 |
| 12 | 160 | 500 | 1100 |

---

## 🎯 CONVERSIÓN A CITA

### Asumimos:
- Conservador: 20% WA → cita efectiva
- Base: 30% WA → cita efectiva
- Agresivo: 40% WA → cita efectiva

### Citas agendadas / mes

| Mes | Conservador | Base | Agresivo |
|-----|-------------|------|----------|
| 1 | 10 | 30 | 72 |
| 3 | 14 | 60 | 152 |
| 6 | 20 | 90 | 260 |
| 9 | 26 | 120 | 360 |
| 12 | 32 | 150 | 440 |

### Tasa de no-show asumida: 15%

### Pacientes nuevos / mes (desde digital)

| Mes | Conservador | Base | Agresivo |
|-----|-------------|------|----------|
| 1 | 8 | 25 | 60 |
| 3 | 12 | 50 | 130 |
| 6 | 17 | 75 | 220 |
| 9 | 22 | 100 | 305 |
| 12 | 27 | 125 | 375 |

---

## 💰 ROI POR ESCENARIO

### Año 1

| Escenario | Inversión marketing | Pacientes | Revenue | ROI |
|-----------|---------------------|-----------|---------|-----|
| Conservador | USD 1,800 | 50-70 | Gs 130-180M | 73-100x |
| Base | USD 5,400 | 120-150 | Gs 250-340M | 46-63x |
| Agresivo | USD 10,800 | 250-350 | Gs 600-800M | 55-74x |

(conservador y agresivo tienen ROI similar porque agresivo también gasta mucho)

---

## 🚦 TRIGGERS DE PIVOTEO

| Señal | Acción |
|-------|--------|
| <50 followers a fin de mes 2 | Aumentar posting + boost |
| <20 mensajes Messaging mes 3 | Cambiar creative |
| <10 citas/mes | Activar referidos + alianzas |
| ROAS <1.5x | Pausar ads no rentables |

---

## 🔗 CRUZAR CON OTROS DOCUMENTOS

- `docs/PLAN-NEGOCIO-ANO-1-OKR-MENSUALES.md`
- `06_MARKETING/digital-marketing-playbook.md`
- `docs/GAP-ANALYSIS-COMPLETO-ADS-LOCATIONS.md`

---

**STATUS:** v1.0 — modelo inicial. Recalibrar con datos reales mes 3+.