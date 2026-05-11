#!/usr/bin/env python3
"""
Script para descargar imágenes de Instagram usando Instaloader con login interactivo
"""

import subprocess
import sys

def main():
    print("=" * 80)
    print("📸 DESCARGADOR DE IMÁGENES DE INSTAGRAM")
    print("=" * 80)
    print()
    print("Este script descargará imágenes de @mysticnailsart")
    print()
    print("⚠️ NECESITAS:")
    print("   - Usuario de Instagram: jgchavezpanduro@gmail.com")
    print("   - Tu contraseña de Instagram")
    print()
    print("🔒 TU CONTRASEÑA ESTÁ SEGURA:")
    print("   - Solo se usa para hacer login en Instagram")
    print("   - No se guarda en ningún lado")
    print("   - Se transmite directamente a Instagram")
    print()
    print("=" * 80)
    print()

    # Preguntar si quiere continuar
    response = input("¿Quieres continuar? (s/n): ").lower()

    if response != 's':
        print("❌ Cancelado")
        return

    print()
    print("🔐 Iniciando proceso de descarga...")
    print()

    # Ejecutar el script con login
    try:
        result = subprocess.run(
            [sys.executable, 'download_instagram_images_with_login.py'],
            cwd='/Users/jorgechavez/Documents/mystic nails antigravity',
            capture_output=False,
            text=True
        )

        if result.returncode == 0:
            print()
            print("=" * 80)
            print("✅ DESCARGA COMPLETADA")
            print("=" * 80)
            print()
            print("📁 Las imágenes están en: assets/imagenes/watermarked/")
            print()
            print("💡 Avísame para que actualice el código index.html")
            print()
        else:
            print()
            print("❌ Hubo un error durante la descarga")
            print()

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
