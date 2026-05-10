#!/bin/bash

# Mystic Nails Art - Deployment Script
# Uso: ./deploy.sh

echo "🚀 Mystic Nails Art - Deployment Launcher"
echo "=========================================="
echo ""

# Check if Netlify CLI is installed
if ! command -v netlify &> /dev/null; then
    echo "📦 Instalando Netlify CLI..."
    npm install -g netlify-cli
fi

echo "✅ Netlify CLI listo"
echo ""
echo "Selecciona opción de deployment:"
echo "1) Deployment GRATIS en Netlify (recomendado)"
echo "2) Deployment en Vercel (alternativa gratis)"
echo "3) Solo preview local"
echo ""
read -p "Opción (1-3): " choice

case $choice in
    1)
        echo "🌐 Deployando en Netlify..."
        netlify deploy --prod --dir=. --site=mystic-nails-art
        echo "✅ Sitio live en: https://mystic-nails-art.netlify.app"
        ;;
    2)
        if ! command -v vercel &> /dev/null; then
            echo "📦 Instalando Vercel CLI..."
            npm install -g vercel
        fi
        echo "🌐 Deployando en Vercel..."
        vercel --prod
        ;;
    3)
        echo "🔍 Iniciando servidor local..."
        echo "Abre http://localhost:8000 en tu navegador"
        python3 -m http.server 8000
        ;;
    *)
        echo "❌ Opción no válida"
        exit 1
        ;;
esac

echo ""
echo "✨ Deployment completado!"
echo "📝 No olvidar:"
echo "   1. Actualizar número de WhatsApp en el HTML"
echo "   2. Verificar dirección y horarios"
echo "   3. Testear en móvil antes de compartir"