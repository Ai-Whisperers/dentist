#!/bin/bash
# test-whatsapp-business.sh
# Test procedure para Gaby validar que el WhatsApp Business está bien configurado
# Ejecutar desde cualquier celular con WA normal.
#
# Pasos:
# 1. Desde tu celular personal, mandá un WhatsApp al número nuevo: +595 987 126 790
# 2. El chip nuevo debería recibir el mensaje
# 3. WA Business muestra el nombre "Ometz Dental" (no tu nombre personal)
# 4. WA Business NO debe mostrar tu foto de perfil personal (debe ser el logo אומץ)
# 5. Respondete a vos misma con /hola (debe expandir al mensaje de bienvenida)
# 6. Respondete con /precio (debe expandir al menú de precios)
# 7. Respondete con /direccion (debe expandir la dirección)
# 8. Mandá un mensaje a las 23:00 (fuera de horario) — debe llegar el mensaje de ausencia
# 9. Probá el catálogo: tocá el ícono de tienda en el perfil → deben aparecer 5 servicios
#
# Si todos los pasos funcionan, el setup está completo.

set -e

PHONE="+595 987 126 790"
PHONE_RAW="595987126790"
WA_URL="https://wa.me/${PHONE_RAW}"

echo "═══════════════════════════════════════════════════════"
echo "🧪 TEST WHATSAPP BUSINESS — Ometz Dental"
echo "═══════════════════════════════════════════════════════"
echo ""
echo "📱 Número a testear: $PHONE"
echo "🔗 Link directo: $WA_URL"
echo ""
echo "Antes de empezar, asegurate de tener:"
echo "  ✓ WhatsApp Business instalado en el celular con el chip Tigo nuevo"
echo "  ✓ El chip está dentro del celular con señal (4G/5G)"
echo "  ✓ Otro celular con tu WhatsApp personal (para hacer las pruebas)"
echo ""
echo "═══════════════════════════════════════════════════════"
echo "TEST 1: NOMBRE Y FOTO DE PERFIL"
echo "═══════════════════════════════════════════════════════"
echo ""
echo "Desde tu celular personal, mandá un WhatsApp al $PHONE."
echo "Cuando se abra la conversación, debería verse:"
echo "  • Nombre: 'Ometz Dental' (NO tu nombre personal)"
echo "  • Foto: el logo אומץ (NO tu cara)"
echo "  • Categoría: 'Clínica dental'"
echo "  • Descripción: 'Odontología conservadora...'"
echo ""
read -p "¿El nombre y foto se ven bien? (y/n) " -n 1 -r
echo ""
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "❌ Revisá: Perfil Business → Ajustes → Herramientas para la empresa → Perfil de la empresa"
    exit 1
fi

echo ""
echo "═══════════════════════════════════════════════════════"
echo "TEST 2: QUICK REPLIES (RESPUESTAS RÁPIDAS)"
echo "═══════════════════════════════════════════════════════"
echo ""
echo "En la conversación del WA Business, escribí /hola y tocá enviar."
echo "Debería expandirse al mensaje de bienvenida completo."
echo ""
read -p "¿/hola funcionó? (y/n) " -n 1 -r
echo ""
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "❌ Revisá: Ajustes → Herramientas para la empresa → Respuestas rápidas"
    echo "   Atajo: /hola"
    echo "   Verificá que esté pegado el texto completo de la v2"
    exit 1
fi

echo ""
echo "Ahora probá /precio, /direccion, y /cita."
echo "Si todos funcionan, las 12 quick replies están bien cargadas."
echo ""
read -p "¿Las 4 quick replies básicas (/hola, /precio, /direccion, /cita) funcionan? (y/n) " -n 1 -r
echo ""
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "❌ Alguna quick reply no está bien cargada. Volvé a verificar."
    exit 1
fi

echo ""
echo "═══════════════════════════════════════════════════════"
echo "TEST 3: MENSAJE DE AUSENCIA"
echo "═══════════════════════════════════════════════════════"
echo ""
echo "Mandá un mensaje desde tu celular personal a las 14:30 hs (estás en consultorio)."
echo "Si NO estás disponible, debería llegar el mensaje de ausencia."
echo ""
echo "Alternativa: cambiá temporalmente el horario de atención en el perfil Business"
echo "para que figure 'Cerrado' y mandate un mensaje."
echo ""
read -p "¿El mensaje de ausencia llega automáticamente? (y/n) " -n 1 -r
echo ""
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "❌ Revisá: Ajustes → Herramientas para la empresa → Mensaje de ausencia"
    echo "   Verificá que esté activado y el horario configurado"
    exit 1
fi

echo ""
echo "═══════════════════════════════════════════════════════"
echo "TEST 4: CATÁLOGO"
echo "═══════════════════════════════════════════════════════"
echo ""
echo "En la conversación del WA Business, tocá el nombre 'Ometz Dental' arriba."
echo "Debería abrir el perfil del negocio. Tocá el ícono de 'Catálogo' (o tienda)."
echo "Deberían aparecer 5 servicios:"
echo "  1. Consulta General — Desde Gs 300.000"
echo "  2. Segunda Opinión Escrita — Desde Gs 450.000"
echo "  3. Profilaxis Completa — Desde Gs 300.000"
echo "  4. Blanqueamiento Consultorio — Consultar"
echo "  5. Restauración en Resina — Desde Gs 350.000"
echo ""
read -p "¿El catálogo tiene los 5 servicios? (y/n) " -n 1 -r
echo ""
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "❌ Revisá: Ajustes → Herramientas para la empresa → Catálogo"
    echo "   Verificá que estén los 5 servicios con precios"
    exit 1
fi

echo ""
echo "═══════════════════════════════════════════════════════"
echo "TEST 5: ETIQUETAS"
echo "═══════════════════════════════════════════════════════"
echo ""
echo "En la conversación del WA Business, mantené presionado el mensaje que te mandaste."
echo "Debería aparecer un menú para asignar etiquetas."
echo ""
echo "Si NO ves ninguna etiqueta, hay que crearlas:"
echo "  Ajustes → Herramientas para la empresa → Etiquetas"
echo "  Crear: New Contact, Pricing Inquiry, Wants Appointment, Second Opinion,"
echo "         Booked, Attended, Treated, Cold Lead, Complaint, Urgent"
echo ""
read -p "¿Las etiquetas están disponibles? (y/n) " -n 1 -r
echo ""
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "❌ Creá las 10 etiquetas según el instructivo"
    exit 1
fi

echo ""
echo "═══════════════════════════════════════════════════════"
echo "✅ TODOS LOS TESTS PASARON"
echo "═══════════════════════════════════════════════════════"
echo ""
echo "El WhatsApp Business está 100% configurado."
echo ""
echo "Próximos pasos:"
echo "  1. Imprimir el QR/placard de entrada: 07_DESIGN/brand-assets/print/whatsapp-placard-entrance.svg"
echo "  2. Plastificar y colocar en la entrada del consultorio"
echo "  3. Mandar el número a 5-10 ex-pacientes O3"
echo "  4. Pedirles que te dejen 5 reseñas Google"
echo "  5. Kiki reclama el Google Business Profile (tarda 5-7 días)"
echo ""
echo "📞 Si algo falla: revisá 08_WHATSAPP/templates/whatsapp-setup-configuration-guide.md"
echo ""
