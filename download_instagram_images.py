#!/usr/bin/env python3
"""
Script para descargar imágenes de Instagram de @mysticnailsart
Requiere: pip install instaloader
"""

import instaloader
import os
import shutil

def download_instagram_images():
    """Descargar imágenes de @mysticnailsart"""

    # Crear instancia de Instaloader
    L = instaloader.Instaloader(download_videos=False, download_video_thumbnails=False, download_geotags=False, download_comments=False, save_metadata=False, compress_json=False)

    username = "mysticnailsart"

    print(f"📸 Descargando imágenes de @{username}...")
    print("⚠️ Si aparece login, usa las credenciales de jgchavezpanduro@gmail.com")

    try:
        # Descargar perfil (sin login para perfiles públicos)
        profile = instaloader.Profile.from_username(L.context, username)

        # Contador
        count = 0
        max_images = 50  # Máximo de imágenes a descargar

        # Crear carpeta de destino
        target_dir = "assets/imagenes/watermarked"
        os.makedirs(target_dir, exist_ok=True)

        # Directorio temporal de instaloader
        temp_dir = username

        # Descargar posts
        for post in profile.get_posts():
            if count >= max_images:
                break

            if post.typename == 'GraphSidecar' or post.is_video_pseudo():
                # Skip carruseles y videos para simplificar
                continue

            try:
                L.download_post(post, target=username)
                count += 1
                print(f"✅ Descargada {count}/{max_images}")
            except Exception as e:
                print(f"❌ Error descargando post: {e}")
                continue

        print(f"\n📁 Total descargadas: {count}")

        # Mover archivos a la carpeta watermarked
        print(f"\n📂 Moviendo archivos a {target_dir}...")

        if os.path.exists(temp_dir):
            files = os.listdir(temp_dir)
            jpg_files = [f for f in files if f.endswith('.jpg')]

            for i, file in enumerate(jpg_files, start=1):
                src = os.path.join(temp_dir, file)
                dst = os.path.join(target_dir, f"Instagram_{i:03d}.jpg")
                shutil.move(src, dst)
                print(f"📸 Movido: {file} -> Instagram_{i:03d}.jpg")

            # Eliminar carpeta temporal
            shutil.rmtree(temp_dir)
            print(f"\n✅ Proceso completado!")
            print(f"📁 {len(jpg_files)} imágenes listas en {target_dir}")

        else:
            print(f"❌ No se encontró la carpeta temporal {temp_dir}")

    except Exception as e:
        print(f"❌ Error: {e}")
        print("\n💡 Si el perfil es privado, necesitas hacer login:")
        print("   L.login(jgchavezpanduro@gmail.com, 'TU_PASSWORD')")

if __name__ == "__main__":
    download_instagram_images()
