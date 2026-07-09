#!/bin/bash
# update-contact-info.sh
# Reemplaza TODOS los placeholders de contacto con los valores reales cuando Gaby los confirme
# Uso: ./scripts/update-contact-info.sh
# Datos a actualizar en config/variables-central.md primero

set -e

# === VALORES CONFIRMADOS (update on 8 jul 2026) ===
# WhatsApp personal de Gaby (TRANSITORIO hasta que compre Business)
OLD_PHONE_DISPLAY="+595 9XX XXX XXX"
NEW_PHONE_DISPLAY="+595 981 146 759"

OLD_PHONE_RAW="595XXXXXXXXX"
NEW_PHONE_RAW="595981146759"

# === ACTUALIZAR VARIABLES-CENTRAL ===
echo "=== Actualizando datos de contacto (WhatsApp TRANSITORIO) ==="
echo ""
echo "⚠️  USANDO +595 981 146 759 (PERSONAL DE GABY, NO BUSINESS)"
echo "    Actualizar de nuevo cuando compre Business chip"
echo ""

# Find-replace en todos los archivos relevantes
for ext in md svg html json; do
  echo "Procesando .$ext..."
  find . -type f -name "*.$ext" \
    -not -path "./.git/*" \
    -not -path "./ARCHIVE/*" \
    -not -path "./node_modules/*" \
    -exec sed -i "s/$OLD_PHONE_DISPLAY/$NEW_PHONE_DISPLAY/g" {} \;
done

OLD_EMAIL="doctora.gabi@ometsdental.com.py"
NEW_EMAIL="doctora.gabi@ometsdental.com.py"   # same value confirmed

echo "=== Actualizando info de contacto en todos los archivos ==="
echo ""

# Find-replace en todos los archivos relevantes
for ext in md svg html json; do
  echo "Procesando .$ext..."
  find . -type f -name "*.$ext" \
    -not -path "./.git/*" \
    -not -path "./ARCHIVE/*" \
    -not -path "./node_modules/*" \
    -exec sed -i "s/$OLD_PHONE_DISPLAY/$NEW_PHONE_DISPLAY/g" {} \;
done

# Para el raw phone (sin espacios)
echo ""
echo "Procesando raw phone (sin espacios)..."
for ext in md svg html json; do
  find . -type f -name "*.$ext" \
    -not -path "./.git/*" \
    -not -path "./ARCHIVE/*" \
    -not -path "./node_modules/*" \
    -exec sed -i "s/$OLD_PHONE_RAW/$NEW_PHONE_RAW/g" {} \;
done

echo ""
echo "=== Conteo de reemplazos ==="
echo "Display format ($NEW_PHONE_DISPLAY):"
grep -rl "$NEW_PHONE_DISPLAY" --include="*.md" --include="*.svg" --include="*.html" . 2>/dev/null | wc -l
echo ""
echo "Raw format ($NEW_PHONE_RAW):"
grep -rl "$NEW_PHONE_RAW" --include="*.md" --include="*.svg" --include="*.html" . 2>/dev/null | wc -l
echo ""
echo "=== ANTES de commitear, verificar manualmente: ==="
echo "1. git diff (verificar cambios visuales)"
echo "2. grep '9XX' . (debería dar 0 matches)"
echo "3. grep '595XXXXXXXXX' . (debería dar 0 matches)"
echo "4. Verificar SVGs renderizando bien en navegador"
echo "5. Si todo OK: git add . && git commit -m 'chore: update contact info'"
