#!/bin/bash
# update-contact-info.sh
# Reemplaza el número de Messaging en TODOS los archivos del repo
# Uso: ./scripts/update-contact-info.sh <OLD_NUMBER> <NEW_NUMBER>
# Ejemplo: ./scripts/update-contact-info.sh "+595 981 146 759" "+595 987 126 790"
#
# Por defecto, idempotente: si ejecutas con el número ya actualizado, no rompe nada.
# Single source of truth: config/variables-central.md

set -e

# === ARGUMENTOS ===
OLD_NUMBER="${1:-}"
NEW_NUMBER="${2:-}"

if [ -z "$OLD_NUMBER" ] || [ -z "$NEW_NUMBER" ]; then
    echo "❌ Uso: $0 <OLD_NUMBER> <NEW_NUMBER>"
    echo "   Ejemplo: $0 '+595 981 146 759' '+595 987 126 790'"
    echo ""
    echo "📌 Número actual (Gaby Business): +595 987 126 790"
    echo ""
    echo "Para verificar el estado actual sin cambiar nada:"
    echo "   grep -r '595987126790' config/variables-central.md"
    exit 1
fi

# === VARIABLES DERIVADAS ===
# Genera las variantes (raw sin espacios, formatted con espacios, wa.me link)
OLD_RAW=$(echo "$OLD_NUMBER" | tr -d ' +')
NEW_RAW=$(echo "$NEW_NUMBER" | tr -d ' +')

OLD_WAME="wa.me/$OLD_RAW"
NEW_WAME="wa.me/$NEW_RAW"

# Variantes con espacios opcionales
OLD_SPACED=$(echo "$OLD_RAW" | sed -E 's/^(\+?[0-9]{3})([0-9]{3})([0-9]{3})([0-9]{3})$/\1 \2 \3 \4/')
NEW_SPACED=$(echo "$NEW_RAW" | sed -E 's/^(\+?[0-9]{3})([0-9]{3})([0-9]{3})([0-9]{3})$/\1 \2 \3 \4/')

echo "======================================"
echo "🔄 ACTUALIZACIÓN DE CONTACTO MASIVA"
echo "======================================"
echo ""
echo "OLD → NEW"
echo "  Display: '$OLD_NUMBER' → '$NEW_NUMBER'"
echo "  Raw:     '$OLD_RAW' → '$NEW_RAW'"
echo "  Link:    '$OLD_WAME' → '$NEW_WAME'"
echo ""

# === CONFIRMACIÓN ===
read -p "¿Continuar? (y/N) " -n 1 -r
echo ""
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "❌ Cancelado."
    exit 0
fi

# === FIND-REPLACE MASIVO ===
# En todos los formatos: raw, formatted, link
EXTENSIONS=(md svg html json ts tsx js xml yam yml)

count_total=0
count_files=0

replace_in_file() {
    local file="$1"
    local pattern="$2"
    local replacement="$3"
    if [ -f "$file" ] && grep -q "$pattern" "$file" 2>/dev/null; then
        local before=$(grep -c "$pattern" "$file" 2>/dev/null || echo 0)
        sed -i "s|$pattern|$replacement|g" "$file"
        local after=$(grep -c "$pattern" "$file" 2>/dev/null || echo 0)
        local changed=$((before - after))
        if [ $changed -gt 0 ]; then
            count_total=$((count_total + changed))
            echo "  ✅ $file  ($changed cambios)"
        fi
    fi
}

# Recolectar archivos a modificar
FILES_TO_EDIT=$(find . -type f \( -name "*.md" -o -name "*.svg" -o -name "*.html" -o -name "*.json" -o -name "*.ts" -o -name "*.tsx" -o -name "*.js" -o -name "*.xml" -o -name "*.yaml" -o -name "*.yml" \) \
    -not -path "./.git/*" \
    -not -path "./ARCHIVE/*" \
    -not -path "./node_modules/*" \
    -not -path "./.next/*" \
    -not -path "./content/*"  2>/dev/null)

# Reemplazar en 3 formatos: raw, formatted, link
for file in $FILES_TO_EDIT; do
    replace_in_file "$file" "$OLD_RAW" "$NEW_RAW"
    replace_in_file "$file" "$OLD_NUMBER" "$NEW_NUMBER"
    replace_in_file "$file" "$OLD_WAME" "$NEW_WAME"
done

# === VERIFICACIÓN POST-CAMBIO ===
echo ""
echo "======================================"
echo "📊 RESULTADO"
echo "======================================"
echo ""
echo "Total reemplazos: $count_total"
echo ""

# Verificar 0 matches del número viejo
remaining_old=$(grep -r "$OLD_RAW" . --include="*.md" --include="*.svg" --include="*.html" --include="*.json" --include="*.ts" --include="*.tsx" 2>/dev/null | grep -v "^./.git" | wc -l)
echo "Ocurrencias restantes del número viejo ($OLD_RAW): $remaining_old"
if [ "$remaining_old" -gt 0 ]; then
    echo "  ⚠️  Aún hay referencias antiguas. Investigar:"
    grep -rl "$OLD_RAW" . --include="*.md" --include="*.svg" --include="*.html" --include="*.json" 2>/dev/null | grep -v "^./.git" | head -5
fi

echo ""
echo "Ocurrencias del número nuevo ($NEW_RAW):"
grep -r "$NEW_RAW" . --include="*.md" --include="*.svg" --include="*.html" --include="*.json" 2>/dev/null | grep -v "^./.git" | wc -l

echo ""
echo "======================================"
echo "✅ PRÓXIMOS PASOS"
echo "======================================"
echo ""
echo "1. Revisar diff:  git diff"
echo "2. Si todo OK:  git add . && git commit -m 'chore(config): update Messaging $OLD_NUMBER → $NEW_NUMBER'"
echo "3. Verificar live site:  curl -s https://ometzdental.com/es | grep -o '595[0-9]*'"
echo "4. Actualizar config/variables-central.md si no lo hiciste antes"
