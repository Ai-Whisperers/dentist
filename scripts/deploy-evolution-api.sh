#!/bin/bash
# deploy-evolution-api.sh
# Deploys Ometz Dental Evolution API stack on a Docker Swarm.

set -euo pipefail

STACK_NAME="ometsdental"
REPO_DIR="/root/dentist"
STACK_DIR="/root/ometsdental-stack"

echo "═══════════════════════════════════════════════════════"
echo "🚀 DEPLOY EVOLUTION API — Ometz Dental"
echo "═══════════════════════════════════════════════════════"
echo ""

# === 1. PRECHECKS ===
echo "1️⃣  Verificando pre-requisitos..."

if ! command -v docker >/dev/null 2>&1; then
    echo "❌ Docker no instalado. Aborta."
    exit 1
fi

if ! docker info 2>/dev/null | grep -q "Swarm: active"; then
    echo "❌ Docker Swarm no está activo. Activá primero:"
    echo "   docker swarm init"
    exit 1
fi

echo "   ✅ Docker Swarm activo"

# === 2. SECRETS ===
echo ""
echo "2️⃣  Generando secrets..."

mkdir -p "$STACK_DIR"
cd "$STACK_DIR"

if [ ! -f ".env" ]; then
    cat > .env <<EOF
# Generated 27 jul 2026 — DO NOT COMMIT
EVOLUTION_API_KEY=$(openssl rand -hex 32)
JWT_SECRET=$(openssl rand -hex 32)
WEBHOOK_HMAC_SECRET=$(openssl rand -hex 32)
REDIS_PASSWORD=$(openssl rand -hex 32)
POSTGRES_PASSWORD=$(openssl rand -hex 32)
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_SERVICE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.your-key-here
OPENAI_API_KEY=sk-your-key-here
EOF
    echo "   ✅ .env creado en $STACK_DIR/.env"
    echo "   ⚠️  Editá $STACK_DIR/.env antes de continuar (Supabase + OpenAI keys)"
    echo ""
    read -p "¿Estás listo para continuar? (y/N) " -n 1 -r
    echo ""
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Cancelado. Editá .env primero."
        exit 1
    fi
fi

# === 3. COPIAR CONFIG ===
echo ""
echo "3️⃣  Copiando config desde repo..."

cp "$REPO_DIR/08_WHATSAPP/evolution-api/evolution-api-config.json" "$STACK_DIR/evolution-api-config.json"
echo "   ✅ evolution-api-config.json copiado"

# === 4. CREAR DOCKER-COMPOSE ===
echo ""
echo "4️⃣  Generando docker-compose.yml..."

cat > docker-compose.yml <<'EOF'
version: "3.8"

services:
  evolution-api:
    image: evoapicloud/evolution-api:v2.0.0
    container_name: ometsdental-evolution-api
    restart: always
    ports:
      - "8080:8080"
    environment:
      - SERVER_PORT=8080
      - SERVER_URL=https://api.ometzdental.com
      - AUTHENTICATION_API_KEY=${EVOLUTION_API_KEY}
      - AUTHENTICATION_JWT_SECRET=${JWT_SECRET}
      - DATABASE_ENABLED=true
      - DATABASE_PROVIDER=postgresql
      - DATABASE_CONNECTION_URI=postgresql://evolution:${POSTGRES_PASSWORD}@postgres:5432/evolution
      - DATABASE_CONNECTION_DB_NAME=evolution
      - REDIS_ENABLED=true
      - REDIS_URI=redis://:${REDIS_PASSWORD}@redis:6379
      - WEBHOOK_GLOBAL_ENABLED=true
      - WEBHOOK_GLOBAL_URL=https://api.ometzdental.com/webhooks/evolution
      - WEBHOOK_GLOBAL_WEBHOOK_BY_EVENTS=true
      - WEBHOOK_GLOBAL_WEBHOOK_BASE64=false
      - LOG_LEVEL=INFO
    volumes:
      - evolution_data:/evolution/store
    networks:
      - ometsdental-net
    depends_on:
      - postgres
      - redis
    healthcheck:
      test: ["CMD-SHELL", "curl -f http://localhost:8080/health || exit 1"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 30s

  webhook-handler:
    build:
      context: /root/dentist/08_WHATSAPP/evolution-api/webhook-handler
      dockerfile: Dockerfile
    container_name: ometsdental-webhook-handler
    restart: always
    ports:
      - "8081:8080"
    env_file:
      - .env
    environment:
      - EVOLUTION_API_URL=http://evolution-api:8080
    networks:
      - ometsdental-net
    depends_on:
      - evolution-api
    healthcheck:
      test: ["CMD-SHELL", "curl -f http://localhost:8080/health || exit 1"]
      interval: 30s
      timeout: 10s
      retries: 3

  postgres:
    image: postgres:16-alpine
    container_name: ometsdental-postgres
    restart: always
    environment:
      - POSTGRES_USER=evolution
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
      - POSTGRES_DB=evolution
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - ometsdental-net
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U evolution -d evolution"]
      interval: 30s
      timeout: 10s
      retries: 3

  redis:
    image: redis:7-alpine
    container_name: ometsdental-redis
    restart: always
    command: redis-server --requirepass ${REDIS_PASSWORD}
    volumes:
      - redis_data:/data
    networks:
      - ometsdental-net
    healthcheck:
      test: ["CMD", "redis-cli", "-a", "${REDIS_PASSWORD}", "ping"]
      interval: 30s
      timeout: 10s
      retries: 3

volumes:
  evolution_data:
  postgres_data:
  redis_data:

networks:
  ometsdental-net:
    driver: overlay
EOF

echo "   ✅ docker-compose.yml generado"

# === 5. DEPLOY ===
echo ""
echo "5️⃣  Desplegando stack..."

docker stack deploy -c docker-compose.yml "$STACK_NAME"

echo "   ✅ Stack '$STACK_NAME' desplegado"

# === 6. VERIFY ===
echo ""
echo "6️⃣  Verificando servicios (esperando 30 seg)..."

sleep 30

docker service ls | grep "$STACK_NAME" || true

echo ""
echo "   Esperando que Evolution API esté healthy..."

for i in {1..10}; do
    if curl -f http://localhost:8080/health >/dev/null 2>&1; then
        echo "   ✅ Evolution API healthy"
        break
    fi
    echo "   Intento $i/10... esperando 5 seg"
    sleep 5
done

# === 7. MIGRATE SUPABASE ===
echo ""
echo "7️⃣  Aplicando schema a Supabase (opcional)..."

if [ -f "$REPO_DIR/08_WHATSAPP/evolution-api/SUPABASE-SCHEMA.sql" ]; then
    echo "   Schema en: $REPO_DIR/08_WHATSAPP/evolution-api/SUPABASE-SCHEMA.sql"
    echo "   Para aplicar:"
    echo "   1. Ir a https://supabase.com/dashboard/project/_/sql"
    echo "   2. Pegar el contenido del schema"
    echo "   3. Click 'Run'"
fi

# === 8. SUMMARY ===
echo ""
echo "═══════════════════════════════════════════════════════"
echo "✅ DEPLOY COMPLETO"
echo "═══════════════════════════════════════════════════════"
echo ""
echo "Servicios corriendo:"
echo "  - Evolution API:    http://localhost:8080"
echo "  - Webhook handler:  http://localhost:8081"
echo "  - Postgres:         localhost:5432"
echo "  - Redis:            localhost:6379"
echo ""
echo "Próximos pasos:"
echo ""
echo "1. Configurar Nginx + SSL (ver evolution-api-deployment.md fase 2)"
echo "2. Aplicar schema a Supabase (paso 7 arriba)"
echo "3. Escanear QR desde WA Business (ver evolution-api-deployment.md fase 3)"
echo "4. Test: mandar un mensaje a +595 987 126 790 desde otro celular"
echo ""
echo "Comandos útiles:"
echo "  docker service ls | grep $STACK_NAME"
echo "  docker service logs ${STACK_NAME}_evolution-api"
echo "  curl -f http://localhost:8080/health"
echo ""
echo "═══════════════════════════════════════════════════════"
