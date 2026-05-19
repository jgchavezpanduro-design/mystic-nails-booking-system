# 🗓️ CONFIGURACIÓN DE CALENDLY - MYSTIC NAILS ART

**Fecha:** 2026-05-19
**Versión:** 1.0
**Estado:** Pendiente de Configuración

---

## 🎯 OBJETIVO

Integrar Calendly con la UI actual de Mystic Nails Art para:
- Mantener el diseño personalizado
- Automatizar sincronización con Google Calendar
- Manejar lógica de reservas automáticamente
- Mantener control sobre UX

---

## 📋 PASO 1: CREAR CUENTA CALENDLY (10 min)

1. **Ir a:** https://calendly.com/
2. **Click en:** "Sign up" (registrarse)
3. **Opciones:**
   - Continuar con Google (recomendado)
   - Usar email
4. **Completar perfil:**
   - Nombre: Mystic Nails Art
   - Email: jgchavezpanduro@gmail.com
   - Contraseña: (crear una segura)

---

## 📋 PASO 2: CREAR EVENT TYPES (15 min)

Cada Event Type = Una manicurista con sus servicios disponibles

### **Event Type 1: Carolina**
1. Click en "Event Types" → "Create" → "One-on-One"
2. **Nombre:** "Carolina - Gelish & Manicure"
3. **Ubicación:**
   - Location: "Mystic Nails Art"
   - Address: Calle 16 Nte entre 35 y 40, Centro, 77720 Playa del Carmen, Q.R.
4. **Duración:** 90 min (ajustable por cita)
5. **Color:** #a977db (purple)
6. **Descripción:** "Reserva tu cita con Carolina - Especialista en Gelish y Manicure"

### **Event Type 2: Montse**
1. Click "Create" → "One-on-One"
2. **Nombre:** "Montse - Rubber Base & Pedicure"
3. **Misma ubicación**
4. **Duración:** 60-120 min (ajustable)
5. **Color:** #f472b6 (pink)
6. **Descripción:** "Reserva tu cita con Montse - Especialista en Rubber Base y Pedicure"

### **Event Type 3: Diana**
1. Click "Create" → "One-on-One"
2. **Nombre:** "Diana - Polygel & Extensions"
3. **Misma ubicación**
4. **Duración:** 120-180 min (ajustable)
5. **Color:** #a977db (purple)
6. **Descripción:** "Reserva tu cita con Diana - Especialista en Polygel y Extensiones"

---

## 📋 PASO 3: CONFIGURAR AVAILABILITY (10 min)

### **Para cada Event Type:**

1. **Abrir Event Type** → "Availability"
2. **Configurar horarios:**
   
   **Carolina:**
   - Lunes a Domingo: 9:00 AM - 5:00 PM
   - Configurar días y horas específicas

   **Montse:**
   - Lunes a Domingo: 12:00 PM - 4:00 PM
   - Configurar días y horas específicas

   **Diana:**
   - Lunes: 9:00 AM - 12:00 PM
   - Martes: 9:00 AM - 8:00 PM
   - Miércoles: DESCANSO
   - Jueves: 9:00 AM - 12:00 PM
   - Viernes/Sábado: 3:30 PM - 8:00 PM
   - Domingo: 3:30 PM - 8:00 PM

3. **Configurar fechas bloqueadas:**
   - Días libres
   - Vacaciones
   - Eventos especiales

---

## 📋 PASO 4: OBTENER API KEY (5 min)

### **Opción A: Token OAuth (Recomendado para Producción)**

1. Ir a: https://calendly.com/integrations
2. Crear nueva integración
3. Seleccionar "OAuth & API Keys"
4. Configurar permisos
5. Obtener Client ID y Client Secret

### **Opción B: API Key Simple (Para Desarrollo)**

1. Ir a: https://calendly.com/settings/api
2. Generar Personal Access Token
3. Guardar token de forma segura

---

## 📋 PASO 5: CONFIGURAR WEBHOOK (OPCIONAL)

Para recibir notificaciones cuando se agenda:

1. Ir a: https://calendly.com/integrations
2. Crear webhook
3. URL de tu servidor o n8n (automatización)
4. Eventos a escuchar: "Invitee Created"

---

## 🔗 INTEGRACIÓN CON GOOGLE CALENDAR

### **Automático (Calendly):**

1. Ir a: https://calendly.com/integrations
2. Conectar: "Google Calendar"
3. Seleccionar calendario principal
4. Configurar:
   - Calendar ID principal
   - Calendarios de cada técnica (si existen)

**Resultado:**
- ✅ Citas en Calendly → automáticamente en Google Calendar
- ✅ Sin configuración adicional necesaria

---

## 📋 PASO 6: PROBAR SISTEMA (10 min)

### **Test Flow:**

1. **Abrir Calendly**
2. **Seleccionar Event Type (Carolina)**
3. **Elegir fecha y hora**
4. **Llenar formulario**
5. **Confirmar**

### **Verificar:**
- ✅ Evento aparece en Google Calendar
- ✅ Recibes email de confirmación
- �️ Cliente recibe email de confirmación
- ✅ Horario correctamente bloqueado

---

## 📋 PASO 7: OBTENER LINKS DE CALENDLY

### **Para cada técnica:**

Una vez creados los Event Types, obtén los links:

1. **Carolina:** https://calendly.com/[tu-usuario]/carolina
2. **Montse:** https://calendly.com/[tu-usuario]/montse
3. **Diana:** https://calendly.com/[tu-usuario]/diana

**Estos links se integrarán en tu web actual.**

---

## ✅ CHECKLIST FINAL

### **Configuración:**
- [ ] Cuenta Calendly creada
- [ ] Event Types creados (3 técnicas)
- [ ] Availability configurada
- [ ] API Key obtenida
- [ ] Google Calendar conectado
- [ ] Webhook configurado (opcional)
- [ ] Links obtenidos

### **Integración:**
- [ ] Links integrados en mysticnailsplaya.com
- [ ] Sistema de depósito configurado
- [ ] Test flow completo funcionando
- [ ] Google Calendar sincronizando

---

## 📞 SOPORTE

**¿Problemas?**
- **Jorge:** jgchavezpanduro@gmail.com
- **WhatsApp:** +52 984 310 8186
- **Calendly Help:** https://calendly.com/support

---

**Última actualización:** 2026-05-19
**Versión:** 1.0 - Calendly Integration
