#!/usr/bin/env python3
"""
Intentar descargar imágenes de Instagram usando servicios públicos
"""

import requests
from bs4 import BeautifulSoup
import re
import time

def try_public_services():
    """Intentar obtener imágenes de servicios públicos"""

    username = "mysticnailsart"
    image_urls = []

    # Lista de servicios a intentar
    services = [
        f"https://imginn.com/{username}/",
        f"https://picuki.com/profile/{username}",
        f"https://dumpor.com/v/{username}",
        f"https://imggram.net/{username}/",
    ]

    for service_url in services:
        print(f"📡 Intentando: {service_url}")

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        }

        try:
            response = requests.get(service_url, headers=headers, timeout=10)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')

                # Buscar todas las etiquetas img
                imgs = soup.find_all('img')

                for img in imgs:
                    src = img.get('src', '')
                    if 'instagram' in src or 'cdninstagram' in src:
                        if src not in image_urls:
                            image_urls.append(src)
                            print(f"  ✅ Encontrada: {src[:80]}...")

                if image_urls:
                    print(f"  📸 Total encontradas: {len(image_urls)}")
                    break
                else:
                    print(f"  ⚠️ No se encontraron imágenes")

            time.sleep(2)  # Esperar entre requests

        except Exception as e:
            print(f"  ❌ Error: {e}")
            continue

    if image_urls:
        print()
        print("=" * 80)
        print(f"✅ ENCONTRADAS {len(image_urls)} IMÁGENES")
        print("=" * 80)
        print()

        # Guardar URLs
        with open('instagram_image_urls_found.txt', 'w') as f:
            for url in image_urls:
                f.write(f"{url}\n")

        print("💾 URLs guardadas en 'instagram_image_urls_found.txt'")
        print()
        print("💡 Para descargar las imágenes, ejecuta:")
        print("   wget -i instagram_image_urls_found.txt -P assets/imagenes/watermarked/")
        print()

        # Intentar descargar automáticamente
        print("📥 Descargando imágenes...")
        print()

        os.makedirs("assets/imagenes/watermarked", exist_ok=True)

        for i, url in enumerate(image_urls[:50], 1):
            try:
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    filename = f"assets/imagenes/watermarked/Instagram_{i:03d}.jpg"
                    with open(filename, 'wb') as f:
                        f.write(response.content)
                    print(f"✅ [{i}/{min(50, len(image_urls))}] {filename}")
                time.sleep(0.5)  # Esperar un poco entre descargas
            except Exception as e:
                print(f"❌ Error descargando {url}: {e}")

        print()
        print("✅ Descarga completada!")
        print()
    else:
        print()
        print("❌ No se pudieron encontrar imágenes públicas")
        print()
        print("💡 Única opción: Usar el script con login")
        print("   Ejecuta: ./descargar_instagram.sh")
        print()

if __name__ == "__main__":
    try_public_services()
