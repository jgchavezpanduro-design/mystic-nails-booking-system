// Tipos base del sistema

export type ClienteTipo = 'Local' | 'Extranjera';

export type CitaEstado = 'confirmada' | 'completada' | 'cancelada' | 'no-show' | 'pendiente';

export type MetodoPago = 'efectivo' | 'transferencia' | 'tarjeta' | 'otro';

export type ServicioCategoria = 'Manicura' | 'Pedicure' | 'ManiPedi' | 'Extra' | 'Otro';

export type ManicuristaEstado = 'activa' | 'inactiva';

export type CompraCategoria = 'productos' | 'herramientas' | 'marketing' | 'renta' | 'servicios' | 'otro';

// ============================================
// CLIENTA
// ============================================
export interface Clienta {
  id: string;
  nombre: string;
  telefono: string;
  instagram?: string;
  tipo: ClienteTipo;
  cumpleanos?: string; // YYYY-MM-DD
  comoEncontro?: string; // Cómo te encontró (Instagram, Facebook, Amiga, etc.)
  notasAlergias?: string;
  primeraVisita?: string; // YYYY-MM-DD
  ultimaVisita?: string; // YYYY-MM-DD
  numVisitas: number;
  totalGastado: number;
  fotos?: string[]; // URLs a fotos en Drive/storage
}

// ============================================
// SERVICIO
// ============================================
export interface Servicio {
  id: string;
  categoria: ServicioCategoria;
  nombre: string;
  detalle: string;
  precioLocal: number;
  precioExtranjera: number;
  tiempoMinutos: number;
  activo: boolean;
}

// ============================================
// MANICURISTA
// ============================================
export interface ComisionConfig {
  porcentajeManicurista: number; // 40, 80, etc.
  porcentajeEmpresa: number; // 15, 35, etc.
  porcentajeAdmin: number; // 5, 25, etc.
}

export interface ModeloMixto {
  sueldoFijoSemanal: number; // MXN 1200
  porcentajeExtra: number; // 25% extra
}

export type ManicuristaModelo = 'porcentaje' | 'mixto';

export interface Manicurista {
  id: string;
  nombre: string;
  telefono: string;
  modelo: ManicuristaModelo;
  comision: ComisionConfig;
  modeloMixto?: ModeloMixto;
  estado: ManicuristaEstado;
  foto?: string; // URL a foto
  notas?: string;
}

// ============================================
// CITA
// ============================================
export interface CitaServicio {
  servicioId: string;
  servicioNombre: string;
  cantidad: number;
  precioUnitario: number;
  subtotal: number;
}

export interface Cita {
  id: string;
  fecha: string; // YYYY-MM-DD
  horaInicio: string; // HH:MM
  duracionMinutos: number;
  clientaId: string;
  clientaNombre: string;
  clientaTipo: ClienteTipo; // Para cálculo automático de precio
  manicuristaId: string;
  manicuristaNombre: string;
  servicioPrincipal: CitaServicio;
  serviciosExtra: CitaServicio[];
  descuento: number;
  propina: number;
  deposito: number;
  totalCobrado: number;
  metodoPago: MetodoPago;
  estado: CitaEstado;
  notas?: string;
  fotoDriveLink?: string; // Link a foto del trabajo terminado

  // Campos calculados (auto)
  comisionPorcentaje: number; // % según manicurista
  empresaPorcentaje: number;
  adminPorcentaje: number;
  comisionPesos: number;
  empresaPesos: number;
  adminPesos: number;
  pagoManicuristaTotal: number; // Comisión + propina
}

// ============================================
// COMPRA/GASTO
// ============================================
export interface Compra {
  id: string;
  fecha: string; // YYYY-MM-DD
  concepto: string;
  categoria: CompraCategoria;
  monto: number;
  proveedor?: string;
  metodoPago: MetodoPago;
  quienCompra?: string;
  notas?: string;
}

// ============================================
// DASHBOARD MENSUAL
// ============================================
export interface DashboardMensual {
  mes: number; // 1-12
  anio: number;
  citasTotales: number;
  ingresosBrutos: number;
  comisionesPagadas: number;
  compras: number;
  saldoNetoEmpresa: number;
  pagoNetoAdmin: number;
  promedioPorCita: number;
  propinasDelMes: number;
  cancelacionesNoShow: number;
  liquidacionesPorManicurista: Liquidacion[];
}

// ============================================
// LIQUIDACIÓN (PAYMENT TO STAFF)
// ============================================
export interface Liquidacion {
  manicuristaId: string;
  manicuristaNombre: string;
  periodoMes: number;
  periodoAnio: number;
  sueldoFijo: number;
  comisionTotal: number;
  propinasTotal: number;
  totalAPagar: number;
  numCitasCompletadas: number;
}

// ============================================
// CONFIGURACIÓN
// ============================================
export interface Configuracion {
  periodoActual: {
    mes: number;
    anio: number;
  };
  notificaciones: {
    citaProxima24h: boolean;
    citaProxima1h: boolean;
  };
  moneda: 'MXN';
  idioma: 'es';
  tema: 'light' | 'dark' | 'auto';
}
