#!/usr/bin/env python3
"""
Script simple para obtener URLs de imágenes de Instagram sin login
Usa selenium para acceder al perfil público
"""

import time
import re
import requests
from bs4 import BeautifulSoup

def get_instagram_images_simple():
    """Intenta obtener URLs de imágenes del perfil público"""

    username = "mysticnailsart"
    url = f"https://www.instagram.com/{username}/"

    print(f"📸 Accediendo a {url}...")

    # Headers para simular un navegador real
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code == 200:
            print("✅ Página accedida exitosamente")

            # Buscar URLs de imágenes en el HTML
            # Instagram usa URLs como: https://scontent-xxx.cdninstagram.com/v/t51.2885-15/....jpg

            image_pattern = r'https://scontent-[^"]+\.jpg'
            images = re.findall(image_pattern, response.text)

            # Eliminar duplicados manteniendo el orden
            unique_images = list(dict.fromkeys(images))

            print(f"\n📸 Encontradas {len(unique_images)} imágenes únicas:")
            print("=" * 80)

            # Guardar URLs en archivo
            with open('instagram_image_urls.txt', 'w') as f:
                for i, img_url in enumerate(unique_images[:50], 1):  # Máximo 50
                    print(f"{i}. {img_url}")
                    f.write(f"{img_url}\n")

            print("=" * 80)
            print(f"\n✅ URLs guardadas en 'instagram_image_urls.txt'")
            print(f"\n💡 Para descargar las imágenes, ejecuta:")
            print(f"   wget -i instagram_image_urls.txt -P assets/imagenes/watermarked/")

            return unique_images[:50]
        else:
            print(f"❌ Error {response.status_code}: No se pudo acceder al perfil")
            return []

    except Exception as e:
        print(f"❌ Error: {e}")
        return []

if __name__ == "__main__":
    get_instagram_images_simple()
