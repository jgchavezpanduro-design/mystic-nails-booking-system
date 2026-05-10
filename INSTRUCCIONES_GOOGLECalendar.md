# 🔗 Instrucciones para Conectar Google Calendar

## 📋 Resumen

El sistema de booking ahora creará automáticamente eventos en Google Calendar cuando un cliente agende una cita. Los eventos se crearán en:
- ✅ Tu calendario de admin (jgchavezpanduro@gmail.com)
- ✅ El calendario de la técnica asignada (Carolina/Montse/Diana)

---

## 🚀 Paso a Paso (30 minutos)

### **Paso 1: Abrir Google Apps Script**
1. Ve a https://script.google.com
2. Clic en **"New project"**
3. Se abrirá el editor de código

### **Paso 2: Copiar el Código**
1. Abre el archivo: [`google-apps-script/Code.gs`](google-apps-script/Code.gs)
2. Copia **todo** el contenido del archivo
3. Pégalo en el editor de Apps Script (reemplaza el código que está ahí)

### **Paso 3: Configurar el Spreadsheet ID**
1. Abre tu Google Sheet del sistema (Mystic_Nails_Art_Sistema.xlsx)
2. Copia el ID de la URL (es la parte larga entre `/d/` y `/edit`):
   ```
   https://docs.google.com/spreadsheets/d/ESTE_ES_EL_ID/edit
   ```
3. En el código de Apps Script, busca esta línea (línea 13):
   ```javascript
   const SPREADSHEET_ID = 'TU_SPREADSHEET_ID_AQUI';
   ```
4. Reemplaza `TU_SPREADSHEET_ID_AQUI` con el ID que copiaste:
   ```javascript
   const SPREADSHEET_ID = '1aBcDeFgHiJkLmNoPqRsTuVwXyZ'; // Ejemplo
   ```

### **Paso 4: Agregar Email de Diana (opcional)**
Si ya tienes el email de Diana, agrégalo en la línea 28:
```javascript
const TECHNICIAN_EMAILS = {
  'Carolina': '27supercaro@gmail.com',
  'Montse': 'Mrqz.mntse25@gmail.com',
  'Diana': 'diana@email.com' // ← Agregar aquí
};
```

### **Paso 5: Guardar y Deployar**
1. Clic en el icono de **💾 Save** (o Ctrl+S)
2. Nombre del proyecto: "Mystic Nails Booking System"
3. Clic en **"Deploy"** → **"New deployment"**
4. Se abrirá un modal, clic en el ícono de ⚙️ (Settings)
5. Selecciona **"Web app"**
6. Configura:
   - **Description:** "Mystic Nails Booking API"
   - **Execute as:** "Me (jgchavezpanduro@gmail.com)"
   - **Who has access:** "Anyone" ← ¡MUY IMPORTANTE!
7. Clic en **"Deploy"**
8. Te pedirá autorizar los permisos:
   - Clic en **"Review permissions"**
   - Selecciona tu cuenta de Google
   - Clic en **"Advanced"** → **"Go to Mystic Nails Booking System (unsafe)"**
   - Clic en **"Allow"**

### **Paso 6: Copiar la URL del Web App**
1. Después de deployar, verás una **Web app URL** que se ve así:
   ```
   https://script.google.com/macros/s/AKfycbxXXXXX/exec
   ```
2. Clic en el botón **"Copy"** para copiarla

### **Paso 7: Conectar con la Landing Page**
1. Abre el archivo [`index.html`](index.html)
2. Busca esta línea (línea ~1863):
   ```javascript
   const GOOGLE_SCRIPT_URL = 'YOUR_APPS_SCRIPT_URL_HERE';
   ```
3. Reemplaza con la URL que copiaste:
   ```javascript
   const GOOGLE_SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbxXXXXX/exec';
   ```
4. Guarda el archivo

---

## ✅ Cómo Funciona Ahora

### **Cuando un cliente agenda una cita:**

1. **Cliente selecciona:** Técnica + Servicio + Fecha + Hora
2. **Sistema valida:** Mínimo 2 horas de anticipación
3. **Al confirmar:**
   - ✅ Crea evento automáticamente en Google Calendar
   - ✅ Invita a admin (jgchavezpanduro@gmail.com)
   - ✅ Invita a la técnica (Carolina/Montse/Diana)
   - ✅ Envía mensaje de WhatsApp al cliente
   - ✅ Pide foto del diseño de uñas

### **El evento en Google Calendar incluye:**
- 📅 Título: "💅 Gelish - Carolina"
- ⏰ Fecha y hora correctas (con duración calculada)
- 👤 Nombre y teléfono del cliente
- 💅 Servicio seleccionado
- 📱 Duración del servicio
- 💅 Incluye remoción o no
- 📍 Location: "Mystic Nails Art, Playa del Carmen"

---

## 🧪 Cómo Probarlo

### **Opción 1: Desde la Landing Page**
1. Abre `index.html` en tu navegador
2. Haz clic en "Book Your Appointment"
3. Completa todos los pasos
4. Al confirmar, revisa:
   - Tu calendario de Google
   - El calendario de Carolina/Montse
   - El WhatsApp que se envió

### **Opción 2: Con Postman o Curl**
```bash
curl -X POST "https://script.google.com/macros/s/TU_URL/exec?path=calendar/create-event" \
  -H "Content-Type: application/json" \
  -d '{
    "clientName": "Maria Lopez",
    "clientPhone": "+52 984 123 4567",
    "technician": "Carolina",
    "service": "Gelish",
    "date": "2026-05-16",
    "startTime": "15:00",
    "durationMinutes": 90,
    "includeRemoval": false,
    "specialRequests": "Nail art requested"
  }'
```

---

## 🔄 Cómo Actualizar el Script

Si necesitas hacer cambios al código:

1. Ve a https://script.google.com
2. Abre el proyecto "Mystic Nails Booking System"
3. Haz los cambios necesarios
4. Guarda (💾)
5. **IMPORTANTE:** Deploy de nuevo:
   - Deploy → Deployments → Edit
   - Clic en "Deploy"
   - La URL se mantiene igual

---

## ⚠️ Troubleshooting

### **Problema: "No se crea el evento en calendar"**
- **Solución:** Verifica que la URL en `index.html` sea correcta
- Abre la consola del navegador (F12) para ver errores

### **Problema: "Error: Script function not found"**
- **Solución:** Verifica que hayas copiado TODO el código de `Code.gs`

### **Problema: "No llegan las invitaciones a las técnicas"**
- **Solución:** Verifica que los emails en `TECHNICIAN_EMAILS` sean correctos
- Las técnicas deben aceptar la invitación la primera vez

### **Problema: "Permission denied"**
- **Solución:** Ve a Deploy → Deployments → Edit
- Cambia "Who has access" a "Anyone"
- Deploy de nuevo

### **Problema: "El cliente ve el popup de Google Calendar"**
- **Solución:** Esto ya está arreglado en el nuevo código
- El cliente solo ve WhatsApp
- El evento se crea automáticamente en backend

---

## 📧 Emails Configurados Actualmente

| Técnica | Email |
|---------|-------|
| Carolina | 27supercaro@gmail.com |
| Montse | Mrqz.mntse25@gmail.com |
| Diana | (Agregar cuando se tenga) |

**Admin:** jgchavezpanduro@gmail.com

---

## 📚 Recursos Útiles

- [Google Apps Script Documentation](https://developers.google.com/apps-script)
- [Calendar Service](https://developers.google.com/apps-script/reference/calendar)
- [Web Apps Guide](https://developers.google.com/apps-script/guides/web)

---

## ✨ Lista de Verificación

Antes de declarar "terminado", verifica:

- [ ] Spreadsheet ID configurado correctamente
- [ ] Emails de técnicas actualizados
- [ ] Script deployado como Web App
- [ ] Permisos otorgados ("Anyone")
- [ ] URL copiada y pegada en `index.html`
- [ ] Probado end-to-end (booking → calendar + WhatsApp)
- [ ] Técnicas reciben invitaciones
- [ ] Admin recibe invitaciones

---

**¿Necesitas ayuda?** Revisa el archivo [`google-apps-script/README.md`](google-apps-script/README.md) para más detalles técnicos.
