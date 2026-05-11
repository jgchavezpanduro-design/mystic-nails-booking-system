#!/usr/bin/env python3
"""
Script para descargar imágenes de Instagram de @mysticnailsart con login
Requiere: pip install instaloader
"""

import instaloader
import os
import shutil
import getpass

def download_instagram_images():
    """Descargar imágenes de @mysticnailsart"""

    # Crear instancia de Instaloader
    L = instaloader.Instaloader(
        download_videos=False,
        download_video_thumbnails=False,
        download_geotags=False,
        download_comments=False,
        save_metadata=False,
        compress_json=False
    )

    username = "mysticnailsart"

    print(f"📸 Descargando imágenes de @{username}...")

    # Intentar hacer login
    try:
        print("\n🔐 Necesitas hacer login en Instagram")
        print("📧 Email: jgchavezpanduro@gmail.com")

        # Solicitar password de forma segura
        password = getpass.getpass("🔑 Password de Instagram: ")

        L.login("jgchavezpanduro@gmail.com", password)
        print("✅ Login exitoso!")
    except Exception as e:
        print(f"⚠️ Error en login: {e}")
        print("Intentando sin login (solo para perfiles públicos)...")
        try:
            profile = instaloader.Profile.from_username(L.context, username)
        except Exception as e2:
            print(f"❌ No se pudo acceder al perfil: {e2}")
            return

    try:
        profile = instaloader.Profile.from_username(L.context, username)

        # Contador
        count = 0
        max_images = 50

        # Crear carpeta de destino
        target_dir = "assets/imagenes/watermarked"
        os.makedirs(target_dir, exist_ok=True)

        # Directorio temporal de instaloader
        temp_dir = username

        print(f"\n📥 Descargando posts...")

        # Descargar posts
        for post in profile.get_posts():
            if count >= max_images:
                break

            # Descargar todos los tipos de posts incluyendo GraphSidecar
            try:
                L.download_post(post, target=username)
                count += 1
                print(f"✅ Descargada {count}/{max_images}")
            except Exception as e:
                print(f"⚠️ Error descargando post: {e}")
                continue

        print(f"\n📁 Total descargadas: {count}")

        # Mover archivos a la carpeta watermarked
        print(f"\n📂 Moviendo archivos a {target_dir}...")

        if os.path.exists(temp_dir):
            files = sorted(os.listdir(temp_dir))
            image_files = [f for f in files if f.endswith(('.jpg', '.jpeg', '.png'))]

            for i, file in enumerate(image_files, start=1):
                src = os.path.join(temp_dir, file)
                new_name = f"Instagram_{i:03d}.jpg"
                dst = os.path.join(target_dir, new_name)
                shutil.move(src, dst)
                print(f"📸 {file} -> {new_name}")

            # Eliminar carpeta temporal
            shutil.rmtree(temp_dir)
            print(f"\n✅ Proceso completado!")
            print(f"📁 {len(image_files)} imágenes listas en {target_dir}")
            print(f"\n⚠️ IMPORTANTE: Avísame para que actualice el código index.html")

        else:
            print(f"❌ No se encontró la carpeta temporal {temp_dir}")

    except Exception as e:
        print(f"❌ Error: {e}")
        print("\n💡 Soluciones:")
        print("1. Verifica que el usuario y contraseña sean correctos")
        print("2. Puede que necesites un código de verificación (2FA)")
        print("3. Descarga manualmente desde: https://www.instagram.com/mysticnailsart/")

if __name__ == "__main__":
    download_instagram_images()
