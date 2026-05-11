#!/usr/bin/env python3
"""
Script para descargar imágenes de Instagram usando instagrapi
Biblioteca más moderna que instaloader
"""

import asyncio
import getpass
from instagrapi import Client
import os
import shutil

def download_with_instagrapi():
    """Descargar imágenes usando instagrapi"""

    username = "mysticnailsart"

    print("=" * 80)
    print("📸 DESCARGADOR DE IMÁGENES DE INSTAGRAM (INSTAGRAPI)")
    print("=" * 80)
    print()

    # Crear cliente
    client = Client()

    print("🔐 Necesitas hacer login en Instagram")
    print("📧 Email: jgchavezpanduro@gmail.com")
    print()

    try:
        # Solicitar password
        password = getpass.getpass("🔑 Password de Instagram: ")

        # Hacer login
        print("\n🔄 Haciendo login...")
        client.login("jgchavezpanduro@gmail.com", password)
        print("✅ Login exitoso!")

        # Obtener perfil
        print(f"\n📥 Accediendo al perfil @{username}...")
        user_id = client.user_id_from_username(username)
        profile = client.user_info(user_id)

        print(f"✅ Perfil encontrado: {profile.username}")
        print(f"📸 {profile.media_count} posts disponibles")

        # Crear carpeta de destino
        target_dir = "assets/imagenes/watermarked"
        os.makedirs(target_dir, exist_ok=True)

        # Descargar medias
        medias = client.user_medias(user_id, amount=50)

        print(f"\n📥 Descargando {len(medias)} imágenes...")

        count = 0
        for media in medias:
            try:
                if media.media_type == 1:  # Photo
                    # Descargar imagen
                    image_path = client.photo_download(media.pk, target_dir)

                    # Renombrar a formato secuencial
                    if image_path and os.path.exists(image_path):
                        new_name = os.path.join(target_dir, f"Instagram_{count+1:03d}.jpg")
                        shutil.move(image_path, new_name)
                        count += 1
                        print(f"✅ [{count}/{len(medias)}] {new_name}")

                elif media.media_type == 8:  # Carousel
                    # Descargar primer slide del carousel
                    try:
                        image_path = client.photo_download(media.pk, target_dir)
                        if image_path and os.path.exists(image_path):
                            new_name = os.path.join(target_dir, f"Instagram_{count+1:03d}.jpg")
                            shutil.move(image_path, new_name)
                            count += 1
                            print(f"✅ [{count}/{len(medias)}] {new_name} (carousel)")
                    except:
                        pass

            except Exception as e:
                print(f"⚠️ Error descargando media {media.pk}: {e}")
                continue

        print()
        print("=" * 80)
        print(f"✅ DESCARGA COMPLETADA: {count} imágenes")
        print("=" * 80)
        print(f"📁 Ubicación: {target_dir}")
        print()
        print("💡 Avísame para que actualice el código index.html")
        print()

    except Exception as e:
        print(f"\n❌ Error: {e}")
        print()
        print("💡 Soluciones posibles:")
        print("   1. Verifica que el usuario y contraseña sean correctos")
        print("   2. Puede que necesites un código de verificación (2FA)")
        print("   3. Instagram podría estar bloqueando el acceso temporalmente")
        print()

if __name__ == "__main__":
    download_with_instagrapi()
