#!/bin/bash

echo "================================================================================"
echo "📸 DESCARGADOR DE IMÁGENES DE INSTAGRAM"
echo "================================================================================"
echo ""
echo "Este script descargará hasta 50 imágenes de @mysticnailsart"
echo ""
echo "⚠️ NECESITAS:"
echo "   - Usuario de Instagram: jgchavezpanduro@gmail.com"
echo "   - Tu contraseña de Instagram"
echo ""
echo "🔒 TU CONTRASEÑA ESTÁ SEGURA - No se guarda en ningún lado"
echo ""
echo "================================================================================"
echo ""

read -p "¿Quieres continuar? (s/n): " respuesta

if [ "$respuesta" != "s" ]; then
    echo "❌ Cancelado"
    exit 0
fi

echo ""
echo "🔐 Iniciando descarga..."
echo ""

cd "/Users/jorgechavez/Documents/mystic nails antigravity"
python3 download_with_instagrapi.py

echo ""
echo "================================================================================"
echo "✅ PROCESO TERMINADO"
echo "================================================================================"
echo ""
echo "📁 Las imágenes descargadas están en: assets/imagenes/watermarked/"
echo ""
echo "💡 AVÍSAme para que actualice el código index.html"
echo ""
