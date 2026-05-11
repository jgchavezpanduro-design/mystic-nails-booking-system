# 📸 Instrucciones para Descargar Imágenes de Instagram

## Opción 1: Script Automático (Recomendado)

### Paso 1: Instalar Instaloader
```bash
pip3 install instaloader
```

### Paso 2: Ejecutar el script
```bash
cd "/Users/jorgechavez/Documents/mystic nails antigravity"
python3 download_instagram_images.py
```

El script descargará hasta 50 imágenes de @mysticnailsart y las guardará en `assets/imagenes/watermarked/` con nombres como `Instagram_001.jpg`, `Instagram_002.jpg`, etc.

---

## Opción 2: Manual

Si el script no funciona, sigue estos pasos:

### 1. Abrir Instagram Web
https://www.instagram.com/mysticnailsart/

### 2. Descargar imágenes individualmente
- Abre cada post/foto
- Haz clic derecho en la imagen → "Guardar imagen como..."
- Guarda en: `assets/imagenes/watermarked/`

### 3. Renombrar archivos
Nombra las imágenes secuencialmente:
- `Instagram_001.jpg`
- `Instagram_002.jpg`
- `Instagram_003.jpg`
- etc.

---

## Opción 3: Usar herramientas online

### ImgInn (anteriormente imginn)
1. Ve a: https://imginn.com/
2. Busca: @mysticnailsart
3. Descarga las imágenes
4. Mueve a `assets/imagenes/watermarked/`

### Picuki
1. Ve a: https://picuki.com/
2. Busca: @mysticnailsart
3. Descarga las imágenes
4. Mueve a `assets/imagenes/watermarked/`

---

## Después de descargar las imágenes

El script actualizará automáticamente el array `allGalleryImages` en `index.html` para incluir las nuevas imágenes.

Si descargas manualmente, avísame para que actualice el código.
