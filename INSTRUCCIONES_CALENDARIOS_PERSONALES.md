# 📅 Guía: Crear Calendarios Personales para Manicuristas

**Objetivo:** Crear calendarios Google Calendar personales para cada técnica (Carolina, Montse, Diana) para que todas sus citas se registren automáticamente en sus propios calendarios.

---

## 🎯 Beneficios

✅ Cada técnica tiene SU PROPIO calendario con todas sus citas
✅ Sincronización automática con Google Calendar
✅ Notificaciones en móvil/desktop de cada técnica
✅ Historial completo de citas por técnica
✅ Fácil de gestionar y compartir

---

## 📋 Paso 1: Crear Calendarios Personales

### Para Carolina (27supercaro@gmail.com)

1. **Iniciar sesión** en Google Calendar con: `27supercaro@gmail.com`
2. **Crear nuevo calendario:**
   - Click en el `+` junto a "Otros calendarios" (o "Settings")
   - Select **"Crear nuevo calendario"**
   - **Nombre del calendario:** "Mystic Nails - Citas Carolina"
   - **Descripción:** "Calendario personal de citas de manicura"
   - **Zona horaria:** `America/Cancun` (muy importante)
   - Click **"Crear calendario"**

3. **Obtener el ID del calendario:**
   - En el panel izquierdo, buscar "Mystic Nails - Citas Carolina"
   - Click en los **3 puntos verticales** (⋮) junto al nombre
   - Select **"Configuración y uso compartido"**
   - Bajar a la sección **"Integrar el calendario"**
   - Copiar el **"ID del calendario"** (se ve como: `abcdefgh1234567890@group.calendar.google.com`)
   - **GUARDAR ESTE ID**

### Para Montse (Mrqz.mntse25@gmail.com)

Repetir los mismos pasos:
1. Iniciar sesión con: `Mrqz.mntse25@gmail.com`
2. Crear calendario: "Mystic Nails - Citas Montse"
3. Zona horaria: `America/Cancun`
4. Copiar el ID del calendario

### Para Diana (Dianamejia2825@gmail.com)

Repetir los mismos pasos:
1. Iniciar sesión con: `Dianamejia2825@gmail.com`
2. Crear calendario: "Mystic Nails - Citas Diana"
3. Zona horaria: `America/Cancun`
4. Copiar el ID del calendario

---

## 🔗 Paso 2: Compartir Calendarios con Admin

Cada técnica debe compartir su calendario con el admin (jgchavezpanduro@gmail.com):

### Desde el calendario de Carolina:

1. **Configuración del calendario:**
   - Click en los **3 puntos (⋮)** junto a "Mystic Nails - Citas Carolina"
   - Select **"Configuración y uso compartido"**

2. **Compartir con personas específicas:**
   - En la sección **"Compartir con personas específicas"**
   - Click **"+ Agregar personas"**
   - Email: `jgchavezpanduro@gmail.com`
   - **Permisos:** Select **"¿Pueden hacer cambios en los eventos?"** → **Sí**
   - Click **"Enviar"**

### Repetir para Montse y Diana

---

## 📝 Paso 3: Actualizar el Google Apps Script

1. **Abrir el Google Apps Script:**
   - Ir a: https://script.google.com
   - Abrir el proyecto `Mystic Nails Booking System`

2. **Editar el archivo `Code.gs`:**

Buscar las líneas:
```javascript
const TECHNICIAN_CALENDAR_IDS = {
  'Carolina': 'primary',
  'Montse': 'primary',
  'Diana': 'primary'
};
```

3. **Reemplazar con los IDs reales:**

```javascript
const TECHNICIAN_CALENDAR_IDS = {
  'Carolina': 'COPIAR_AQUI_ID_CALENDARIO_CAROLINA',
  'Montse': 'COPIAR_AQUI_ID_CALENDARIO_MONTSE',
  'Diana': 'COPIAR_AQUI_ID_CALENDARIO_DIANA'
};
```

**Ejemplo:**
```javascript
const TECHNICIAN_CALENDAR_IDS = {
  'Carolina': 'abcdefgh1234567890@group.calendar.google.com',
  'Montse': 'ijklmnop9876543210@group.calendar.google.com',
  'Diana': 'qrstuvwy1239874560@group.calendar.google.com'
};
```

---

## 🚀 Paso 4: Deployar Nueva Versión

1. **Guardar cambios:**
   - Click **"Guardar"** (icono de disquete 💾) o `Ctrl + S`

2. **Deployar nueva versión:**
   - Click en **"Implementar"** → **"Nueva implementación"**
   - **Descripción:** "Añadidos calendarios personales para técnicas"
   - Click **"Implementar"**

3. **Verificar:**
   - Copy la **URL del web app** (termina en `/exec`)
   - Actualizar en `index.html` si cambió

---

## ✅ Paso 5: Testing

### Prueba 1: Booking con Carolina

1. Ir a: http://localhost:8000
2. Click en "Book Now"
3. Seleccionar: **Carolina**
4. Seleccionar servicio
5. Seleccionar fecha y hora
6. Completar booking

**Verificar:**
- ✅ Email de invitación llega a `jgchavezpanduro@gmail.com`
- ✅ Email de invitación llega a `27supercaro@gmail.com`
- ✅ El evento aparece en el calendario **"Mystic Nails - Citas Carolina"**
- ✅ El evento también aparece en el calendario del admin

### Prueba 2: Booking con Montse

Repetir el proceso con Montse y verificar su calendario.

### Prueba 3: Booking con Diana

Repetir el proceso con Diana y verificar su calendario.

---

## 🎨 Paso 6: Configurar Colores (Opcional)

Cada técnica puede personalizar el color de su calendario:

1. En Google Calendar
2. Click en los **3 puntos (⋮)** junto al calendario
3. Select **"Configuración y uso compartido"**
4. Buscar **"Color del calendario"**
5. Seleccionar un color:
   - Carolina: Rosa/Magenta
   - Montse: Azul/Cian
   - Diana: Verde/Turquesa

---

## 📱 Paso 7: Configurar Notificaciones (Opcional)

### Para recibir alertas en móvil:

1. **Instalar Google Calendar app** en cada teléfono
2. **Iniciar sesión** con su email correspondiente
3. **Activar notificaciones:**
   - Abrir Google Calendar app
   - Click en las **3 barras horizontales** (☰)
   - Select **"Configuración"**
   - **"Notificaciones"**
   - Activar: "Notificaciones de calendario"
   - Activar: "Recordatorios de eventos"

### Configurar recordatorios:

1. En Google Calendar (web)
2. Configuración del calendario
3. **"Notificaciones"**
4. Agregar:
   - **1 día antes** (10:00 AM)
   - **1 hora antes**
   - **15 minutos antes**

---

## 🔄 ¿Cómo Funciona Ahora?

### Flujo Completo:

1. **Cliente hace booking** en la web
2. **JavaScript envía datos** al Google Apps Script
3. **Apps Script crea evento:**
   - ✅ En el calendario personal de la técnica (ej: "Mystic Nails - Citas Carolina")
   - ✅ En el calendario del admin (backup)
4. **Invitaciones automáticas:**
   - ✅ Email a admin (jgchavezpanduro@gmail.com)
   - ✅ Email a la técnica
5. **Sincronización:**
   - ✅ Calendario de técnica se sincroniza con su móvil
   - ✅ Notificaciones push en celular
   - ✅ Recordatorios configurados

---

## 🛠️ Solución de Problemas

### Problema: "No tengo permiso para acceder al calendario"

**Solución:**
1. Verificar que compartiste el calendario con `jgchavezpanduro@gmail.com`
2. Verificar que diste permiso de "Puede hacer cambios"
3. Esperar 5-10 minutos para que se propaguen los permisos

### Problema: "El evento no aparece en mi calendario"

**Solución:**
1. Verificar que el ID del calendario en `Code.gs` es correcto
2. Verificar que deployaste la nueva versión del script
3. Revisar la página de "Implementaciones" en Apps Script para ver errores

### Problema: "No recibo notificaciones"

**Solución:**
1. Verificar que instalaste la app de Google Calendar
2. Verificar que iniciaste sesión con el email correcto
3. Verificar que las notificaciones están activadas en configuración

### Problema: "El evento aparece en el calendario equivocado"

**Solución:**
1. Verificar que el nombre de la técnica en `index.html` coincide exactamente con la clave en `TECHNICIAN_CALENDAR_IDS`
2. Ejemplo: Si en la web es "Carolina", en el objeto debe ser `'Carolina': '...'`

---

## 📞 Soporte

Si tienes problemas:
1. Revisar los logs de ejecución en Google Apps Script
2. Verificar que todos los permisos están correctamente configurados
3. Revisar que los emails son correctos
4. Contactar a jgchavezpanduro@gmail.com

---

**Última actualización:** 2026-05-12
**Versión:** 1.0 - Calendarios Personales
