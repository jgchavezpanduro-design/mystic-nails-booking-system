import AsyncStorage from '@react-native-async-storage/async-storage';
import { Clienta, Servicio, Manicurista, Cita, Compra, Configuracion } from '../types';

/**
 * Servicio de almacenamiento local para modo offline
 * Usa AsyncStorage para persistir datos en el dispositivo
 */

const STORAGE_KEYS = {
  CLIENTAS: '@mystic_nails:clientas',
  SERVICIOS: '@mystic_nails:servicios',
  MANICURISTAS: '@mystic_nails:manicuristas',
  CITAS: '@mystic_nails:citas',
  COMPRAS: '@mystic_nails:compras',
  CONFIGURACION: '@mystic_nails:config',
  LAST_SYNC: '@mystic_nails:last_sync'
};

// ============================================
// CLIENTAS
// ============================================

export async function saveClientasLocal(clientas: Clienta[]): Promise<void> {
  try {
    await AsyncStorage.setItem(STORAGE_KEYS.CLIENTAS, JSON.stringify(clientas));
  } catch (error) {
    console.error('Error saving clientas locally:', error);
    throw error;
  }
}

export async function getClientasLocal(): Promise<Clienta[]> {
  try {
    const data = await AsyncStorage.getItem(STORAGE_KEYS.CLIENTAS);
    return data ? JSON.parse(data) : [];
  } catch (error) {
    console.error('Error fetching clientas locally:', error);
    return [];
  }
}

// ============================================
// SERVICIOS
// ============================================

export async function saveServiciosLocal(servicios: Servicio[]): Promise<void> {
  try {
    await AsyncStorage.setItem(STORAGE_KEYS.SERVICIOS, JSON.stringify(servicios));
  } catch (error) {
    console.error('Error saving servicios locally:', error);
    throw error;
  }
}

export async function getServiciosLocal(): Promise<Servicio[]> {
  try {
    const data = await AsyncStorage.getItem(STORAGE_KEYS.SERVICIOS);
    return data ? JSON.parse(data) : [];
  } catch (error) {
    console.error('Error fetching servicios locally:', error);
    return [];
  }
}

// ============================================
// MANICURISTAS
// ============================================

export async function saveManicuristasLocal(manicuristas: Manicurista[]): Promise<void> {
  try {
    await AsyncStorage.setItem(STORAGE_KEYS.MANICURISTAS, JSON.stringify(manicuristas));
  } catch (error) {
    console.error('Error saving manicuristas locally:', error);
    throw error;
  }
}

export async function getManicuristasLocal(): Promise<Manicurista[]> {
  try {
    const data = await AsyncStorage.getItem(STORAGE_KEYS.MANICURISTAS);
    return data ? JSON.parse(data) : [];
  } catch (error) {
    console.error('Error fetching manicuristas locally:', error);
    return [];
  }
}

// ============================================
// CITAS
// ============================================

export async function saveCitasLocal(citas: Cita[]): Promise<void> {
  try {
    await AsyncStorage.setItem(STORAGE_KEYS.CITAS, JSON.stringify(citas));
  } catch (error) {
    console.error('Error saving citas locally:', error);
    throw error;
  }
}

export async function getCitasLocal(): Promise<Cita[]> {
  try {
    const data = await AsyncStorage.getItem(STORAGE_KEYS.CITAS);
    return data ? JSON.parse(data) : [];
  } catch (error) {
    console.error('Error fetching citas locally:', error);
    return [];
  }
}

export async function addCitaLocal(cita: Cita): Promise<void> {
  try {
    const citas = await getCitasLocal();
    citas.push(cita);
    await saveCitasLocal(citas);
  } catch (error) {
    console.error('Error adding cita locally:', error);
    throw error;
  }
}

export async function updateCitaLocal(id: string, updates: Partial<Cita>): Promise<void> {
  try {
    const citas = await getCitasLocal();
    const index = citas.findIndex(c => c.id === id);
    if (index !== -1) {
      citas[index] = { ...citas[index], ...updates };
      await saveCitasLocal(citas);
    }
  } catch (error) {
    console.error('Error updating cita locally:', error);
    throw error;
  }
}

export async function deleteCitaLocal(id: string): Promise<void> {
  try {
    const citas = await getCitasLocal();
    const filtered = citas.filter(c => c.id !== id);
    await saveCitasLocal(filtered);
  } catch (error) {
    console.error('Error deleting cita locally:', error);
    throw error;
  }
}

// ============================================
// COMPRAS
// ============================================

export async function saveComprasLocal(compras: Compra[]): Promise<void> {
  try {
    await AsyncStorage.setItem(STORAGE_KEYS.COMPRAS, JSON.stringify(compras));
  } catch (error) {
    console.error('Error saving compras locally:', error);
    throw error;
  }
}

export async function getComprasLocal(): Promise<Compra[]> {
  try {
    const data = await AsyncStorage.getItem(STORAGE_KEYS.COMPRAS);
    return data ? JSON.parse(data) : [];
  } catch (error) {
    console.error('Error fetching compras locally:', error);
    return [];
  }
}

// ============================================
// CONFIGURACIÓN
// ============================================

export async function saveConfigLocal(config: Configuracion): Promise<void> {
  try {
    await AsyncStorage.setItem(STORAGE_KEYS.CONFIGURACION, JSON.stringify(config));
  } catch (error) {
    console.error('Error saving config locally:', error);
    throw error;
  }
}

export async function getConfigLocal(): Promise<Configuracion | null> {
  try {
    const data = await AsyncStorage.getItem(STORAGE_KEYS.CONFIGURACION);
    return data ? JSON.parse(data) : null;
  } catch (error) {
    console.error('Error fetching config locally:', error);
    return null;
  }
}

// ============================================
// SINCRONIZACIÓN
// ============================================

export async function getLastSyncTime(): Promise<Date | null> {
  try {
    const data = await AsyncStorage.getItem(STORAGE_KEYS.LAST_SYNC);
    return data ? new Date(data) : null;
  } catch (error) {
    console.error('Error fetching last sync time:', error);
    return null;
  }
}

export async function saveLastSyncTime(date: Date): Promise<void> {
  try {
    await AsyncStorage.setItem(STORAGE_KEYS.LAST_SYNC, date.toISOString());
  } catch (error) {
    console.error('Error saving last sync time:', error);
    throw error;
  }
}

/**
 * Limpia todos los datos locales (útil para logout o reset)
 */
export async function clearAllLocalData(): Promise<void> {
  try {
    await AsyncStorage.multiRemove(Object.values(STORAGE_KEYS));
  } catch (error) {
    console.error('Error clearing local data:', error);
    throw error;
  }
}

/**
 * Verifica si hay datos pendientes de sincronizar
 */
export async function hasPendingSync(): Promise<boolean> {
  try {
    const lastSync = await getLastSyncTime();
    if (!lastSync) return true;

    // Si han pasado más de 1 hora desde la última sincronización
    const oneHourAgo = new Date(Date.now() - 60 * 60 * 1000);
    return lastSync < oneHourAgo;
  } catch (error) {
    console.error('Error checking pending sync:', error);
    return true;
  }
}
