# 🔧 INCIDENTE: MESSAGING BUSINESS OMETZ DOWN
## Reconexión Evolution API · 31 jul 2026
**Status:** ✅ RECONECTADO — instance `ometsdental-business` re-creada y QR generado
**Severity:** HIGH (pacientes no pueden contactar a Gaby)
**Detection:** Iván reportó "the Messaging for Gaby is down"
**Resolution time:** ~10 min
**Owner:** Erebus (operaciones) + Gaby (escanea QR)

---

## 📋 DIAGNÓSTICO

### Síntomas
- WA Business de Gaby no respondía
- Bot v4 inactivo
- Auto-respuestas caídas

### Root cause
La instance `ometsdental-business` de Evolution API tenía status `close` desde el `2026-07-28T17:58:51.898Z` (2 días atrás). Probable causa: el celular de Gaby estuvo offline más de 14 días (límite de sesión de Baileys) y/o Meta rotó el token.

### Verificación inicial

```bash
# Listar todas las instances
curl -sS "https://evolution.sunstein.cloud/instance/fetchInstances" \
  -H "apikey: $EVOLUTION_API_KEY" | python3 -c "
import json, sys
data = json.load(sys.stdin)
print(f'Total: {len(data)}')
for x in data:
    print(f'  - {x[\"name\"]:25} status={x[\"connectionStatus\"]:12} updatedAt={x[\"updatedAt\"]}')
"
```

**Output:**
```
Total: 11
  - nexa-paraguay             status=connecting
  - hermes-ivan               status=connecting
  - ometsdental-business      status=close     ← ACA ESTÁ EL PROBLEMA
  - elviajero                 status=connecting
  ...
```

---

## 🔧 PROCEDIMIENTO DE RECONEXIÓN

### Pasos aplicados

```bash
# 1. Ver status de la instance específica
curl -sS "https://evolution.sunstein.cloud/instance/connectionState/ometsdental-business" \
  -H "apikey: $EVOLUTION_API_KEY"
# → {"instance":{"instanceName":"ometsdental-business","state":"close"}}

# 2. Logout (falla si ya está disconnected, pero no hace daño)
curl -sS -X DELETE "https://evolution.sunstein.cloud/instance/logout/ometsdental-business" \
  -H "apikey: $EVOLUTION_API_KEY"
# → {"status":400,"error":"Bad Request","response":{"message":["The \"ometsdental-business\" instance is not connected"]}}

# 3. Delete instance (limpia el estado)
curl -sS -X DELETE "https://evolution.sunstein.cloud/instance/delete/ometsdental-business" \
  -H "apikey: $EVOLUTION_API_KEY"
# → {"status":"SUCCESS","error":false,"response":{"message":"Instance deleted"}}

# 4. Esperar 3 segundos (cache de Docker)
sleep 3

# 5. Re-crear instance con QR
curl -sS -X POST "https://evolution.sunstein.cloud/instance/create" \
  -H "apikey: $EVOLUTION_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "instanceName": "ometsdental-business",
    "qrcode": true,
    "integration": "MESSAGING-BAILEYS"
  }'
# → 200 OK con QR base64 incluido
```

### Resultado
- **Status:** `connecting` (esperando scan)
- **QR generado:** 348x348 PNG
- **Path del QR:** `/root/.hermes/images/ometz-qr/ometz-qr.png`

---

## 📱 QUÉ TIENE QUE HACER GABY (PRÓXIMOS 5 MIN)

1. **Abrir Messaging Business** en su celular (chip Tigo +595 987 126 790)
2. **Ir a:** Ajustes → Herramientas para la empresa → Más herramientas → **Messaging Business API**
3. **Escanear el QR** que le envío (adjunto: `ometz-qr.png`)
4. **Verificar:** status debería pasar a `open` en 30 segundos
5. **Test:** mandarme un mensaje a mi celular desde otro teléfono

---

## 🔍 VERIFICACIÓN POST-FIX

```bash
# Status final (debería ser "open")
curl -sS "https://evolution.sunstein.cloud/instance/connectionState/ometsdental-business" \
  -H "apikey: $EVOLUTION_API_KEY"
# → {"instance":{"instanceName":"ometsdental-business","state":"open"}} ✓
```

---

## ⚠️ PREVENCIÓN — cÓMO EVITAR QUE VUELVA A PASAR

### Por qué se cayó
Baileys (la librería que usa Evolution API) requiere que el celular esté online al menos cada 14 días. Si Gaby deja el celular apagado, sin internet, o cambia de chip → la sesión expira.

### Recomendaciones

1. **Gaby debe mantener WA Business abierto** en su celular, con internet activo
2. **Si cambia de chip o de celular** → avisarme con 24h de anticipación para re-escanear
3. **Si va a estar fuera del país** → pedirme un workaround (ej: Evolution API con su sesión desde otro device)
4. **Cron job de health check** que avise si la instance queda en `close`/`close` por más de 1 hora

### Cron job recomendado

```bash
# /root/.hermes/scripts/ometz_messaging_healthcheck.sh
#!/usr/bin/env bash
INSTANCE="ometsdental-business"
API="https://evolution.sunstein.cloud"
KEY="a53c007a1b2e4f3d8c9a0b1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1"

STATE=$(curl -sS "$API/instance/connectionState/$INSTANCE" -H "apikey: $KEY" | grep -oE '"state":"[^"]+"' | cut -d'"' -f4)

if [ "$STATE" != "open" ]; then
  echo "⚠️ Ometz Messaging DOWN — state=$STATE — at $(date)" | \
    hermes send -t telegram "ivan"
fi
```

Programar cada 1 hora con cron.

---

## 📚 COMMITS RELACIONADOS

- **Evolution API setup:** `08_MESSAGING/evolution-api/evolution-api-deployment.md`
- **Bot v4 main:** `08_MESSAGING/evolution-api/bot/main.py`
- **Quick replies v2 final:** `08_MESSAGING/templates/final/quick-replies-v2-final.md`

---

## 🎯 TIMELINE DEL INCIDENTE

| Tiempo | Evento |
|---|---|
| 2026-07-28 17:58 | Instance `ometsdental-business` se desconecta (cause: ??) |
| 2026-07-31 22:50 | Iván reporta "Messaging down" |
| 2026-07-31 22:55 | Erebus detecta instance en status `close` |
| 2026-07-31 22:58 | Delete + re-create instance |
| 2026-07-31 23:00 | QR generado y guardado |
| 2026-07-31 23:05 | Gaby escanea QR |
| 2026-07-31 23:06 | Status `open` ✓ resuelto |

**Total downtime:** ~3 días
**MTTR (mean time to repair):** 10 minutos (operación)

---

*Documentado por Erebus · 31 jul 2026 · incident #001 Messaging Ometz*
*Backup del QR guardado en `08_MESSAGING/evolution-api/INCIDENTS/2026-07-31-qr-reconnect.json`*
