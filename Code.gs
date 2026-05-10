/**
 * Google Apps Script para Mystic Nails Art
 * Este script expone endpoints REST para interactuar con Google Sheets
 *
 * INSTRUCCIONES:
 * 1. Crea un nuevo Google Apps Script en https://script.google.com
 * 2. Copia este código en Code.gs
 * 3. Deploya como "Web App" (Publish → Deploy as Web App)
 * 4. Configura: "Who can access: Anyone" (para evitar autenticación compleja)
 * 5. Copia la URL del deploy y pégala en src/services/googleSheets.ts
 */

const SPREADSHEET_ID = '1nHvkLYt4jk2jRF_hoWKHN4Dn6lXZ3k06cy8hfN69U0Y'; // Mystic_Nails_Art_Sistema
const SHEETS = {
  CITAS: 'Citas',
  CLIENTAS: 'Clientas',
  SERVICIOS: 'Servicios',
  MANICURISTAS: 'Manicuristas',
  COMPRAS: 'Compras',
  CONFIGURACION: 'Configuración'
};

// Emails de las técnicas y admin
const TECHNICIAN_EMAILS = {
  'Carolina': '27supercaro@gmail.com',
  'Montse': 'Mrqz.mntse25@gmail.com',
  'Diana': 'Dianamejia2825@gmail.com'
};

const ADMIN_EMAILS = ['jgchavezpanduro@gmail.com']; // Agregar más admins si es necesario

// Horarios de las técnicas
const TECHNICIAN_SCHEDULES = {
  'Carolina': {
    'Monday': ['09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00'],
    'Tuesday': ['09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00'],
    'Wednesday': ['09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00'],
    'Thursday': ['09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00'],
    'Friday': ['09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00'],
    'Saturday': ['09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00'],
    'Sunday': ['09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00']
  },
  'Montse': {
    'Monday': ['12:00', '13:00', '14:00', '15:00'],
    'Tuesday': [], // Descanso
    'Wednesday': ['12:00', '13:00', '14:00', '15:00'],
    'Thursday': ['12:00', '13:00', '14:00', '15:00'],
    'Friday': ['12:00', '13:00', '14:00', '15:00'],
    'Saturday': ['12:00', '13:00', '14:00', '15:00'],
    'Sunday': ['12:00', '13:00', '14:00', '15:00']
  },
  'Diana': {
    'Monday': ['09:00', '10:00', '11:00'],
    'Tuesday': ['09:00', '10:00', '11:00'], // Solo hasta 12 PM (tiene cita a las 4:30 PM)
    'Wednesday': [], // Descanso
    'Thursday': ['09:00', '10:00', '11:00'],
    'Friday': ['15:30', '16:30', '17:30', '18:30', '19:30'],
    'Saturday': ['15:30', '16:30', '17:30', '18:30', '19:30'],
    'Sunday': ['15:30', '16:30', '17:30', '18:30', '19:30']
  }
};

// ============================================
// UTILIDADES
// ============================================

function getSheet(name) {
  const ss = SpreadsheetApp.openById(SPREADSHEET_ID);
  return ss.getSheetByName(name);
}

function getDataAsObjects(sheet) {
  const data = sheet.getDataRange().getValues();
  if (data.length === 0) return [];

  const headers = data[0];
  const rows = data.slice(1);

  return rows.map(row => {
    const obj = {};
    headers.forEach((header, index) => {
      obj[header] = row[index];
    });
    return obj;
  });
}

function findRowIndex(sheet, id, idColumn = 'ID') {
  const data = sheet.getDataRange().getValues();
  const headers = data[0];
  const idIndex = headers.indexOf(idColumn);

  for (let i = 1; i < data.length; i++) {
    if (data[i][idIndex] == id) {
      return i + 1; // 1-based index
    }
  }
  return -1;
}

function jsonResponse(data, error = null) {
  return ContentService.createTextOutput(JSON.stringify({
    success: !error,
    data: data,
    error: error
  })).setMimeType(ContentService.MimeType.JSON);
}

// ============================================
// ENDPOINTS HTTP
// ============================================

function doGet(e) {
  const path = e.parameter.path;
  const params = e.parameter;

  try {
    switch (path) {
      case 'clientas':
        return jsonResponse(getClientas(params));
      case 'servicios':
        return jsonResponse(getServicios());
      case 'manicuristas':
        return jsonResponse(getManicuristas());
      case 'citas':
        return jsonResponse(getCitas(params));
      case 'compras':
        return jsonResponse(getCompras(params));
      default:
        return jsonResponse(null, 'Endpoint not found: ' + path);
    }
  } catch (error) {
    return jsonResponse(null, error.toString());
  }
}

function doPost(e) {
  try {
    const body = JSON.parse(e.postData.contents);
    const path = e.parameter.path;

    switch (path) {
      case 'clientas':
        return jsonResponse(createClienta(body));
      case 'servicios':
        return jsonResponse(createServicio(body));
      case 'manicuristas':
        return jsonResponse(createManicurista(body));
      case 'citas':
        return jsonResponse(createCita(body));
      case 'compras':
        return jsonResponse(createCompra(body));
      case 'calendar/create-event':
        return jsonResponse(createCalendarEvent(body));
      default:
        return jsonResponse(null, 'Endpoint not found: ' + path);
    }
  } catch (error) {
    return jsonResponse(null, error.toString());
  }
}

function doPut(e) {
  try {
    const body = JSON.parse(e.postData.contents);
    const path = e.parameter.path;
    const id = e.parameter.id;

    switch (path) {
      case 'clientas':
        return jsonResponse(updateClienta(id, body));
      case 'servicios':
        return jsonResponse(updateServicio(id, body));
      case 'manicuristas':
        return jsonResponse(updateManicurista(id, body));
      case 'citas':
        return jsonResponse(updateCita(id, body));
      default:
        return jsonResponse(null, 'Endpoint not found: ' + path);
    }
  } catch (error) {
    return jsonResponse(null, error.toString());
  }
}

function doDelete(e) {
  try {
    const path = e.parameter.path;
    const id = e.parameter.id;

    switch (path) {
      case 'clientas':
        return jsonResponse(deleteClienta(id));
      case 'servicios':
        return jsonResponse(deleteServicio(id));
      case 'manicuristas':
        return jsonResponse(deleteManicurista(id));
      case 'citas':
        return jsonResponse(deleteCita(id));
      default:
        return jsonResponse(null, 'Endpoint not found: ' + path);
    }
  } catch (error) {
    return jsonResponse(null, error.toString());
  }
}

// ============================================
// CLIENTAS
// ============================================

function getClientas(params) {
  const sheet = getSheet(SHEETS.CLIENTAS);
  let data = getDataAsObjects(sheet);

  // Filtrar si se proporciona ID
  if (params && params.id) {
    data = data.filter(c => c['ID'] == params.id);
  }

  return data.map(c => ({
    id: c['ID'],
    nombre: c['Nombre'],
    telefono: c['Teléfono'],
    instagram: c['Instagram'],
    tipo: c['Tipo'],
    cumpleanos: c['Cumpleaños'],
    comoEncontro: c['Cómo te encontró'],
    notasAlergias: c['Notas / alergias'],
    primeraVisita: c['Primera visita'],
    ultimaVisita: c['Última visita'],
    numVisitas: c['# Visitas'],
    totalGastado: c['Total gastado']
  }));
}

function createClienta(data) {
  const sheet = getSheet(SHEETS.CLIENTAS);
  const id = Utilities.base64Encode(`${Date.now()}-${Math.random()}`);

  const newRow = [
    id,
    data.nombre,
    data.telefono,
    data.instagram || '',
    data.tipo,
    data.cumpleanos || '',
    data.comoEncontro || '',
    data.notasAlergias || '',
    data.primeraVisita || new Date().toISOString().split('T')[0],
    '',
    0,
    0
  ];

  sheet.appendRow(newRow);
  return { id, ...data };
}

function updateClienta(id, data) {
  const sheet = getSheet(SHEETS.CLIENTAS);
  const rowIndex = findRowIndex(sheet, id);

  if (rowIndex === -1) {
    throw new Error('Clienta not found');
  }

  // Actualizar fila (simplificado - adaptar según necesites)
  const row = sheet.getRange(rowIndex, 1, 1, 12);
  const values = row.getValues()[0];

  values[1] = data.nombre || values[1]; // Nombre
  values[2] = data.telefono || values[2]; // Teléfono
  values[3] = data.instagram || values[3]; // Instagram
  values[4] = data.tipo || values[4]; // Tipo
  // ... actualizar otros campos según necesites

  row.setValues([values]);
  return { id, ...data };
}

function deleteClienta(id) {
  const sheet = getSheet(SHEETS.CLIENTAS);
  const rowIndex = findRowIndex(sheet, id);

  if (rowIndex === -1) {
    throw new Error('Clienta not found');
  }

  sheet.deleteRow(rowIndex);
  return { id };
}

// ============================================
// SERVICIOS
// ============================================

function getServicios() {
  const sheet = getSheet(SHEETS.SERVICIOS);
  const data = getDataAsObjects(sheet);

  return data.map(s => ({
    id: s['ID'],
    categoria: s['Categoría'],
    nombre: s['Servicio'],
    detalle: s['Detalle'],
    precioLocal: s['Precio Local'],
    precioExtranjera: s['Precio Extranjera'],
    tiempoMinutos: s['Tiempo (min)'],
    activo: true
  }));
}

function createServicio(data) {
  const sheet = getSheet(SHEETS.SERVICIOS);
  const id = Utilities.base64Encode(`${Date.now()}-${Math.random()}`);

  const newRow = [
    id,
    data.categoria,
    data.nombre,
    data.detalle,
    data.precioLocal,
    data.precioExtranjera,
    data.tiempoMinutos
  ];

  sheet.appendRow(newRow);
  return { id, ...data };
}

function updateServicio(id, data) {
  // Similar a updateClienta - adaptar según necesites
  throw new Error('Not implemented');
}

function deleteServicio(id) {
  // Similar a deleteClienta - adaptar según necesites
  throw new Error('Not implemented');
}

// ============================================
// MANICURISTAS
// ============================================

function getManicuristas() {
  const sheet = getSheet(SHEETS.MANICURISTAS);
  const data = getDataAsObjects(sheet);

  return data.map(m => ({
    id: m['ID'],
    nombre: m['Nombre'],
    modelo: m['Sueldo Fijo Semanal'] > 0 ? 'mixto' : 'porcentaje',
    comision: {
      porcentajeManicurista: m['% Manicurista'],
      porcentajeEmpresa: m['% Empresa'],
      porcentajeAdmin: m['% Admin']
    },
    modeloMixto: m['Sueldo Fijo Semanal'] > 0 ? {
      sueldoFijoSemanal: m['Sueldo Fijo Semanal'],
      porcentajeExtra: 25 // Ajustar según necesites
    } : undefined,
    estado: m['Activa'].toLowerCase() === 'sí' ? 'activa' : 'inactiva',
    telefono: '',
    notas: m['Notas']
  }));
}

function createManicurista(data) {
  const sheet = getSheet(SHEETS.MANICURISTAS);
  const id = Utilities.base64Encode(`${Date.now()}-${Math.random()}`);

  const newRow = [
    id,
    data.nombre,
    data.comision.porcentajeManicurista,
    data.comision.porcentajeEmpresa,
    data.comision.porcentajeAdmin,
    data.modeloMixto ? data.modeloMixto.sueldoFijoSemanal : 0,
    data.estado === 'activa' ? 'Sí' : 'No',
    data.notas || ''
  ];

  sheet.appendRow(newRow);
  return { id, ...data };
}

function updateManicurista(id, data) {
  throw new Error('Not implemented');
}

function deleteManicurista(id) {
  throw new Error('Not implemented');
}

// ============================================
// CITAS
// ============================================

function getCitas(params) {
  const sheet = getSheet(SHEETS.CITAS);
  let data = getDataAsObjects(sheet);

  // Filtrar por mes/año si se proporciona
  if (params && params.mes && params.anio) {
    data = data.filter(c => {
      const fecha = new Date(c['Fecha']);
      return (fecha.getMonth() + 1) == params.mes && fecha.getFullYear() == params.anio;
    });
  }

  return data.map(c => ({
    id: c['ID Cita'],
    fecha: c['Fecha'],
    horaInicio: c['Hora Inicio'],
    duracionMinutos: c['Duración (min)'],
    clientaId: '', // Mapear desde Clientas
    clientaNombre: c['Clienta'],
    clientaTipo: c['Tipo (auto)'],
    manicuristaId: '', // Mapear desde Manicuristas
    manicuristaNombre: c['Manicurista'],
    servicioPrincipal: {
      servicioId: '',
      servicioNombre: c['Servicio Principal'],
      cantidad: 1,
      precioUnitario: c['Precio servicio (auto)'],
      subtotal: c['Subtotal (auto)']
    },
    serviciosExtra: [],
    descuento: c['Descuento'] || 0,
    propina: c['Propina'] || 0,
    deposito: c['Depósito'] || 0,
    totalCobrado: c['Total cobrado (auto)'],
    metodoPago: c['Método pago'],
    estado: c['Estado'],
    notas: c['Notas'],
    fotoDriveLink: c['Foto Drive (link)'],
    comisionPorcentaje: c['% Manicurista (auto)'],
    empresaPorcentaje: c['% Empresa (auto)'],
    adminPorcentaje: c['% Admin (auto)'],
    comisionPesos: c['Comisión $ (auto)'],
    empresaPesos: c['Empresa $ (auto)'],
    adminPesos: c['Admin $ (auto)'],
    pagoManicuristaTotal: c['Pago manicurista total (auto)']
  }));
}

function createCita(data) {
  const sheet = getSheet(SHEETS.CITAS);
  const id = Utilities.base64Encode(`${Date.now()}-${Math.random()}`);

  // Calcular campos automáticos
  const subtotal = data.servicioPrincipal.subtotal;
  const comision = calcularComision(subtotal, data.manicuristaNombre);

  const newRow = [
    id,
    data.fecha,
    data.horaInicio,
    data.duracionMinutos,
    data.clientaNombre,
    data.clientaTipo,
    data.manicuristaNombre,
    data.servicioPrincipal.servicioNombre,
    '', // Detalle del servicio
    '', // Servicios extras
    data.servicioPrincipal.precioUnitario,
    0, // Cobro extras
    subtotal, // Subtotal
    data.descuento,
    data.propina,
    data.deposito,
    data.totalCobrado,
    data.totalCobrado, // Saldo día
    data.metodoPago,
    data.estado,
    data.notas,
    comision.porcentajeManicurista,
    comision.porcentajeEmpresa,
    comision.porcentajeAdmin,
    comision.comisionPesos,
    comision.empresaPesos,
    comision.adminPesos,
    comision.comisionPesos + data.propina, // Pago manicurista total
    '' // Foto Drive
  ];

  sheet.appendRow(newRow);
  return { id, ...data };
}

function calcularComision(monto, manicuristaNombre) {
  // Ajustar según las comisiones reales de tus manicuristas
  if (manicuristaNombre === 'Carolina') {
    return {
      porcentajeManicurista: 80,
      porcentajeEmpresa: 15,
      porcentajeAdmin: 5,
      comisionPesos: monto * 0.8,
      empresaPesos: monto * 0.15,
      adminPesos: monto * 0.05
    };
  } else {
    // Monse u otros
    return {
      porcentajeManicurista: 40,
      porcentajeEmpresa: 35,
      porcentajeAdmin: 25,
      comisionPesos: monto * 0.4,
      empresaPesos: monto * 0.35,
      adminPesos: monto * 0.25
    };
  }
}

function updateCita(id, data) {
  throw new Error('Not implemented');
}

function deleteCita(id) {
  throw new Error('Not implemented');
}

// ============================================
// COMPRAS
// ============================================

function getCompras(params) {
  const sheet = getSheet(SHEETS.COMPRAS);
  let data = getDataAsObjects(sheet);

  // Filtrar por mes/año si se proporciona
  if (params && params.mes && params.anio) {
    data = data.filter(c => {
      const fecha = new Date(c['Fecha']);
      return (fecha.getMonth() + 1) == params.mes && fecha.getFullYear() == params.anio;
    });
  }

  return data.map(c => ({
    id: c['ID'],
    fecha: c['Fecha'],
    concepto: c['Concepto'],
    categoria: c['Categoría'],
    monto: c['Monto'],
    proveedor: c['Proveedor'],
    metodoPago: c['Método pago'],
    quienCompra: c['Quien compra'],
    notas: c['Notas']
  }));
}

function createCompra(data) {
  const sheet = getSheet(SHEETS.COMPRAS);
  const id = Utilities.base64Encode(`${Date.now()}-${Math.random()}`);

  const newRow = [
    id,
    data.fecha,
    data.concepto,
    data.categoria,
    data.monto,
    data.proveedor || '',
    data.metodoPago,
    data.quienCompra || '',
    data.notas || ''
  ];

  sheet.appendRow(newRow);
  return { id, ...data };
}

// ============================================
// GOOGLE CALENDAR INTEGRATION
// ============================================

function createCalendarEvent(data) {
  try {
    // Parse dates and times
    const startDate = new Date(`${data.date}T${data.startTime}:00`);
    const endDate = new Date(startDate.getTime() + data.durationMinutes * 60 * 1000);

    // Build guest list
    const guests = [...ADMIN_EMAILS];
    const technicianEmail = TECHNICIAN_EMAILS[data.technician];
    if (technicianEmail) {
      guests.push(technicianEmail);
    }

    // Create event description
    const description = `📅 APPOINTMENT DETAILS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

👤 Client: ${data.clientName}
📱 Phone: ${data.clientPhone}
👩‍🎨 Technician: ${data.technician}
💅 Service: ${data.service}
⏱️ Duration: ${data.durationMinutes} minutes
💅 Removal: ${data.includeRemoval ? 'Yes' : 'No'}

${data.specialRequests ? '📝 Notes: ' + data.specialRequests + '%0A' : ''}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚠️ IMPORTANT: CLIENT MUST SEND NAIL DESIGN PHOTO
Please contact client to request a photo of their desired nail design BEFORE the appointment.

⚠️ NOTE ABOUT AI-GENERATED DESIGNS:
If the client's design inspiration is from an AI-generated image (Midjourney, DALL-E, etc.), please verify what's realistically achievable and inform the client.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Booking created via Mystic Nails Art website`;

    // Create calendar event
    const calendar = CalendarApp.getDefaultCalendar();
    const event = calendar.createEvent(
      `💅 ${data.service} - ${data.technician}`,
      startDate,
      endDate,
      {
        description: description,
        location: 'Mystic Nails Art, Playa del Carmen',
        guests: guests.join(','),
        sendInvites: true
      }
    );

    return {
      success: true,
      eventId: event.getId(),
      message: 'Event created successfully',
      guests: guests
    };

  } catch (error) {
    throw new Error('Error creating calendar event: ' + error.toString());
  }
}
