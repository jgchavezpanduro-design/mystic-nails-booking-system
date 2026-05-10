import * as Calendar from 'expo-calendar';
import { Cita } from '../types';

/**
 * Servicio para integración con Google Calendar
 *
 * NOTA: Esta es una implementación placeholder usando expo-calendar.
 * Para producción, necesitas:
 * 1. Configurar permisos de calendario en app.json
 * 2. Solicitar permisos al usuario
 * 3. Acceder al calendario específico de Google Calendar
 */

const CALENDAR_ID = 'primary'; // ID del calendario de Google Calendar

// ============================================
// CONFIGURACIÓN
// ============================================

/**
 * Inicializa el acceso al calendario y solicita permisos
 */
export async function initCalendarAccess(): Promise<boolean> {
  try {
    const { status } = await Calendar.requestCalendarPermissionsAsync();
    if (status === 'granted') {
      console.log('Calendar permissions granted');
      return true;
    } else {
      console.log('Calendar permissions denied');
      return false;
    }
  } catch (error) {
    console.error('Error requesting calendar permissions:', error);
    return false;
  }
}

/**
 * Obtiene el calendario por defecto
 */
export async function getDefaultCalendar(): Promise<Calendar.Calendar | null> {
  try {
    const calendars = await Calendar.getCalendarsAsync(Calendar.EntityTypes.EVENT);
    const defaultCalendar = calendars.find(
      cal => cal.accessLevel === 'owner' && cal.source.type === 'com.google'
    ) || calendars[0];

    return defaultCalendar || null;
  } catch (error) {
    console.error('Error getting default calendar:', error);
    return null;
  }
}

// ============================================
// EVENTOS
// ============================================

interface CalendarEvent {
  id: string;
  title: string;
  startDate: Date;
  endDate: Date;
  location?: string;
  notes?: string;
  reminders?: Calendar.Reminder[];
}

/**
 * Crea un evento de cita en Google Calendar
 */
export async function createCalendarEvent(cita: Cita): Promise<string> {
  try {
    const calendar = await getDefaultCalendar();
    if (!calendar) {
      throw new Error('No calendar found');
    }

    const startDate = new Date(`${cita.fecha}T${cita.horaInicio}`);
    const endDate = new Date(startDate.getTime() + cita.duracionMinutos * 60000);

    const eventId = await Calendar.createEventAsync(calendar.id, {
      title: `${cita.clientaNombre} - ${cita.servicioPrincipal.servicioNombre}`,
      startDate,
      endDate,
      location: 'Mystic Nails Art',
      notes: `Manicurista: ${cita.manicuristaNombre}\nNotas: ${cita.notas || ''}`,
      reminders: [
        { minutes: 24 * 60, method: Calendar.ReminderMethod.EMAIL },
        { minutes: 60, method: Calendar.ReminderMethod.EMAIL }
      ]
    });

    console.log('Calendar event created:', eventId);
    return eventId;
  } catch (error) {
    console.error('Error creating calendar event:', error);
    throw error;
  }
}

/**
 * Actualiza un evento en Google Calendar
 */
export async function updateCalendarEvent(
  eventId: string,
  cita: Cita
): Promise<void> {
  try {
    const calendar = await getDefaultCalendar();
    if (!calendar) {
      throw new Error('No calendar found');
    }

    const startDate = new Date(`${cita.fecha}T${cita.horaInicio}`);
    const endDate = new Date(startDate.getTime() + cita.duracionMinutos * 60000);

    await Calendar.updateEventAsync(eventId, {
      title: `${cita.clientaNombre} - ${cita.servicioPrincipal.servicioNombre}`,
      startDate,
      endDate,
      location: 'Mystic Nails Art',
      notes: `Manicurista: ${cita.manicuristaNombre}\nNotas: ${cita.notas || ''}`
    });

    console.log('Calendar event updated:', eventId);
  } catch (error) {
    console.error('Error updating calendar event:', error);
    throw error;
  }
}

/**
 * Elimina un evento de Google Calendar
 */
export async function deleteCalendarEvent(eventId: string): Promise<void> {
  try {
    await Calendar.deleteEventAsync(eventId);
    console.log('Calendar event deleted:', eventId);
  } catch (error) {
    console.error('Error deleting calendar event:', error);
    throw error;
  }
}

/**
 * Obtiene eventos de un rango de fechas
 */
export async function getEventsInRange(
  startDate: Date,
  endDate: Date
): Promise<Calendar.Event[]> {
  try {
    const calendar = await getDefaultCalendar();
    if (!calendar) {
      throw new Error('No calendar found');
    }

    const events = await Calendar.getEventsAsync(
      [calendar.id],
      startDate,
      endDate
    );

    return events;
  } catch (error) {
    console.error('Error fetching events:', error);
    throw error;
  }
}

// ============================================
// SINCRONIZACIÓN
// ============================================

/**
 * Sincroniza una cita con Google Calendar
 * - Si no tiene eventId, crea el evento
 * - Si tiene eventId, actualiza el evento
 * - Si está cancelada/no-show, elimina el evento
 */
export async function syncCitaWithCalendar(cita: Cita): Promise<void> {
  try {
    if (cita.estado === 'cancelada' || cita.estado === 'no-show') {
      // Eliminar evento si existe
      if (cita.calendarEventId) {
        await deleteCalendarEvent(cita.calendarEventId);
      }
    } else if (cita.calendarEventId) {
      // Actualizar evento existente
      await updateCalendarEvent(cita.calendarEventId, cita);
    } else {
      // Crear nuevo evento
      const eventId = await createCalendarEvent(cita);
      // Aquí deberías guardar el eventId en la cita en tu backend
    }
  } catch (error) {
    console.error('Error syncing cita with calendar:', error);
    throw error;
  }
}

/**
 * Sincroniza múltiples citas con Google Calendar
 */
export async function syncMultipleCitasWithCalendar(citas: Cita[]): Promise<void> {
  for (const cita of citas) {
    try {
      await syncCitaWithCalendar(cita);
    } catch (error) {
      console.error(`Error syncing cita ${cita.id}:`, error);
      // Continuar con la siguiente cita
    }
  }
}
