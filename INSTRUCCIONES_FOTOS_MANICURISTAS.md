# 📸 Instrucciones: Fotos de las Manicuristas

**Fecha:** 2026-05-13
**Ubicación:** `assets/images/`

---

## 🎯 Objetivo

Agregar fotos profesionales de las manicuristas para el sistema de booking.

---

## 📁 Estructura de Archivos

```
assets/images/
├── carolina.jpg    ← Foto de Carolina
├── montse.jpg      ← Foto de Montse
└── diana.jpg       ← Foto de Diana
```

---

## 📸 Requisitos de las Fotos

### **Tamaño y Formato:**
- **Formato:** JPG o PNG
- **Tamaño recomendado:** 500x500 px (mínimo 300x300 px)
- **Relación de aspecto:** 1:1 (cuadrada)
- **Tamaño máximo:** 2 MB

### **Estilo de la Foto:**
- ✅ Primer plano de la cara (desde los hombros hacia arriba)
- ✅ Buena iluminación
- ✅ Fondo neutro o limpio
- ✅ Sonriendo natural
- ✅ Ropa profesional
- ✅ Enfoque nítido

### **Posición:**
- ✅ Mirando directamente a la cámara
- ✅ Cara centrada
- ✅ No recortar la cabeza

### **Evitar:**
- ❌ Fotos borrosas
- ❌ Contraluces
- ❌ Fondos muy ocupados
- ❌ Fotos con otras personas
- ❌ Gafas de sol
- ❌ Filtros excesivos

---

## 🔄 Cómo Agregar las Fotos

### **Método 1: Desde la Computadora**

1. **Preparar la foto:**
   - Asegúrate de que la foto cumpla los requisitos
   - Recortar a formato cuadrado si es necesario
   - Cambiar el tamaño a 500x500 px (opcional)

2. **Renombrar el archivo:**
   - Carolina: `carolina.jpg`
   - Montse: `montse.jpg`
   - Diana: `diana.jpg`

3. **Copiar al directorio:**
   - Abrir: `/Users/jorgechavez/Documents/mystic nails antigravity/assets/images/`
   - Copiar los archivos allí

4. **Verificar:**
   - Abrir: http://localhost:8000
   - Ir a "Book Now"
   - Verificar que las fotos aparezcan

### **Método 2: Desde el Celular**

1. **Enviar la foto:**
   - Enviar la foto por WhatsApp a Jorge (+52 984 310 8186)
   - O enviar por email: jgchavezpanduro@gmail.com

2. **Jorge la sube:**
   - Descargar la foto
   - Recortar/cambiar tamaño si es necesario
   - Guardar en `assets/images/`

---

## 🎨 Fallback (Mientras No Hay Fotos)

Si las fotos no existen, el sistema mostrará automáticamente:
- **Carolina:** 👩‍🎨 (emoji)
- **Montse:** 💅 (emoji)
- **Diana:** ✨ (emoji)

Esto es temporal hasta que agreguen las fotos reales.

---

## 📱 Ejemplo de Código

**El HTML ya está configurado:**

```html
<img src="assets/images/carolina.jpg"
     alt="Carolina"
     style="width: 100%; height: 100%; object-fit: cover;"
     onerror="this.style.display='none'; this.parentElement.innerHTML='👩‍🎨';">
```

**Funcionamiento:**
1. Intenta cargar `assets/images/carolina.jpg`
2. Si la foto existe → la muestra
3. Si la foto NO existe → muestra emoji 👩‍🎨

---

## ✅ Checklist

### **Carolina:**
- [ ] Foto lista
- [ ] Renombrada a `carolina.jpg`
- [ ] Copiada a `assets/images/`
- [ ] Verificada en el sitio web

### **Montse:**
- [ ] Foto lista
- [ ] Renombrada a `montse.jpg`
- [ ] Copiada a `assets/images/`
- [ ] Verificada en el sitio web

### **Diana:**
- [ ] Foto lista
- [ ] Renombrada a `diana.jpg`
- [ ] Copiada a `assets/images/`
- [ ] Verificada en el sitio web

---

## 🛠️ Herramientas Recomendadas

### **Para Recortar Fotos:**
- **Online:** https://www.remove.bg/ (elimina fondo)
- **Online:** https://www.photopea.com/ (editor gratis como Photoshop)
- **Mac:** Preview (aplicación preinstalada)
- **Windows:** Paint

### **Para Cambiar Tamaño:**
- **Online:** https://www.iloveimg.com/resize-image
- **Mac:** Preview → Tools → Adjust Size
- **Windows:** Paint → Resize

---

## 🎯 Tip Profesional

**Para fotos consistentes:**
1. Usar la misma iluminación para todas
2. Usar el mismo fondo
3. Misma posición de la cámara
4. Mismo estilo de ropa
5. Esto crea una imagen más profesional

---

## 📞 Soporte

**Necesitas ayuda?**
- **Jorge:** jgchavezpanduro@gmail.com
- **WhatsApp:** +52 984 310 8186

---

**Última actualización:** 2026-05-13
**Versión:** 1.0
