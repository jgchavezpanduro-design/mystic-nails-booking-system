# 🔒 Guía: Cómo Bloquear Horarios Manualmente

**Objetivo:** Bloquear horarios cuando alguien agenda por teléfono para evitar double-booking.

---

## 🎯 Método 1: Desde Google Calendar (MÁS FÁCIL)

### Cuándo Usar:
- ✅ Alguien agenda por teléfono
- ✅ Necesitas bloquear un horario específico
- ✅ Quieres agregar notas sobre el bloqueo

### Pasos:

#### Opción A: Desde Computadora (2 minutos)

1. **Abrir Google Calendar**
   - Ir a: https://calendar.google.com
   - Iniciar sesión con tu email

2. **Crear evento de bloqueo**
   - Click en la fecha y hora que quieres bloquear
   - Click en "Crear" (no "Crear reserva de Google Meet")

3. **Configurar el evento:**
   ```
   Título: 🔒 BLOQUEO - Teléfono
   
   (Opcional) Agregar más detalles:
   🔒 BLOQUEO - Teléfono
   Cliente: María González
   Teléfono: +52 984 123 4567
   Servicio: Gelish
   Nota: Agenda por llamada
   ```

4. **Configurar hora:**
   - Hora inicio: La hora del bloqueo
   - Duración: La duración del servicio (ej: 90 min para Gelish)

5. **Seleccionar calendario:**
   - Importante: Seleccionar "Mystic Nails - [Tu Nombre]"

6. **Click "Guardar"**

7. **¡Listo!** 🎉
   - El sistema web automáticamente NO mostrará ese horario
   - El evento queda registrado en tu calendario
   - Puedes editar/agregar notas después

#### Opción B: Desde Celular (1 minuto)

1. **Abrir app de Google Calendar**
2. **Click en el día y hora**
3. **Crear evento nuevo:**
   - Título: `🔒 BLOQUEO`
   - Calendario: "Mystic Nails - [Tu Nombre]"
4. **Ajustar duración** (arrastrar hacia abajo)
5. **Guardar**
6. **¡Listo!**

---

## 🎯 Método 2: Bloquear Múltiples Horarios a la Vez

### Para Bloquear Todo un Día:

1. **Crear evento de día completo**
   - Título: `🔒 CERRADO - [Motivo]`
   - Ejemplo: `🔒 CERRADO - Vacaciones`, `🔒 CERRADO - Médico`
   - Seleccionar "Todo el día"
   - Duración: Seleccionar rango de fechas
   - Guardar

### Para Bloquear Varios Slots:

1. **Crear múltiples eventos**
   - Repetir el proceso para cada horario
   - O usar "Repetir" si es un horario recurrente

---

## 🎯 Método 3: Usar el Sistema Web (FUTURO)

**Próximamente:** Podrás bloquear horarios directamente desde el panel de admin en la web.

- Click en "Admin Panel"
- Seleccionar "Bloquear Horario"
- Elegir técnica, fecha, hora
- Agregar nota
- Click en "Bloquear"

---

## ✅ Cómo Verificar que Funciona

### Test 1: Crear Bloqueo

1. En Google Calendar, bloquea las 3:00 PM hoy
2. Ve a http://localhost:8000
3. Selecciona la misma técnica
4. Selecciona hoy
5. **Verifica:** Las 3:00 PM NO aparecen como disponibles

### Test 2: Deshacer Bloqueo

1. En Google Calendar, borra el evento de bloqueo
2. Recarga la página de booking
3. **Verifica:** Las 3:00 PM ahora SÍ aparecen disponibles

---

## 🎨 Códigos de Bloqueo Útiles

Usa estos prefijos en el título del evento para identificarse fácilmente:

- `🔒 BLOQUEO` - Bloqueo genérico
- `🔒 TELÉFONO` - Agenda por teléfono
- `🔒 CERRADO` - Día cerrado
- `🔒 VACACIONES` - Vacaciones
- `🔒 MÉDICO` - Cita médica
- `🔒 PERSONAL` - Asunto personal
- `🔒 MANTENIMIENTO` - Mantenimiento
- `🔒 REUNIÓN` - Reunión

---

## 📱 Ejemplos Reales

### Ejemplo 1: Cliente Llama por Teléfono

**Situación:** María llama y agenda Gelish mañana a las 2:00 PM con Carolina

**Pasos:**
1. Abrir Google Calendar en el celular
2. Buscar mañana a las 2:00 PM
3. Crear evento:
   ```
   🔒 TELÉFONO
   Cliente: María González
   Tel: +52 984 123 4567
   Gelish - 90 min
   ```
4. Guardar
5. **Resultado:** Ese horario ya no está disponible en la web

### Ejemplo 2: Día Completo Cerrado

**Situación:** Carolina no podrá trabajar el viernes por asuntos personales

**Pasos:**
1. Abrir Google Calendar
2. Crear evento de día completo:
   ```
   🔒 CERRADO
   Motivo: Asuntos personales
   ```
3. Seleccionar viernes
4. Marcar "Todo el día"
5. Guardar
6. **Resultado:** El viernes completo no aparece disponible

### Ejemplo 3: Vacaciones

**Situación:** Montse de vacaciones del 20 al 27 de mayo

**Pasos:**
1. Abrir Google Calendar
2. Crear evento:
   ```
   🔒 VACACIONES
   Del 20 al 27 de mayo
   ```
3. Fecha inicio: 20 mayo
4. Fecha fin: 27 mayo
5. Guardar
6. **Resultado:** Ningún horario disponible en esas fechas

---

## 🔄 Sincronización

**Importante:** El sistema verifica Google Calendar en tiempo real, pero puede haber un retraso de **1-2 minutos**.

**Si necesitas bloqueo inmediato:**
1. Crea el evento en Google Calendar
2. Espera 1-2 minutos
3. Recarga la página de booking
4. Verifica que el horario ya no aparece

---

## 🛠️ Solución de Problemas

### Problema: "El horario bloqueado todavía aparece en la web"

**Soluciones:**
1. **Verificar que seleccionaste el calendario correcto** ("Mystic Nails - [Tu Nombre]")
2. **Esperar 2-3 minutos** para sincronización
3. **Recargar la página de booking** (F5)
4. **Verificar que la fecha y hora son correctas**

### Problema: "Quiero desbloquear un horario"

**Solución:**
1. Abrir Google Calendar
2. Buscar el evento de bloqueo
3. Click en el evento
4. Click en el ícono de basura 🗑️
5. Confirmar "Eliminar"
6. **Resultado:** El horario vuelve a estar disponible en 1-2 minutos

### Problema: "Bloqueé el horario equivocado"

**Solución:**
1. No te preocupes, pasa
2. Abre Google Calendar
3. Elimina el evento de bloqueo
4. Crea el bloqueo en el horario correcto

---

## 📞 Contacto

Si tienes problemas o dudas:
- **Jorge:** jgchavezpanduro@gmail.com
- **WhatsApp:** +52 984 310 8186

---

**Última actualización:** 2026-05-12
**Versión:** 1.0 - Sistema de Bloqueo de Horarios
