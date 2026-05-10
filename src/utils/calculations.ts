import {
  ClienteTipo,
  Servicio,
  Manicurista,
  Cita,
  CitaServicio,
  ComisionConfig,
  ModeloMixto
} from '../types';

// ============================================
// CÁLCULO DE PRECIOS
// ============================================

/**
 * Calcula el precio de un servicio según el tipo de clienta
 */
export function calcularPrecioServicio(
  servicio: Servicio,
  tipoClienta: ClienteTipo
): number {
  return tipoClienta === 'Local' ? servicio.precioLocal : servicio.precioExtranjera;
}

/**
 * Calcula el subtotal de un servicio (precio × cantidad)
 */
export function calcularSubtotalServicio(
  servicio: Servicio,
  tipoClienta: ClienteTipo,
  cantidad: number = 1
): CitaServicio {
  const precioUnitario = calcularPrecioServicio(servicio, tipoClienta);
  const subtotal = precioUnitario * cantidad;

  return {
    servicioId: servicio.id,
    servicioNombre: servicio.nombre,
    cantidad,
    precioUnitario,
    subtotal
  };
}

// ============================================
// CÁLCULO DE COMISIONES
// ============================================

/**
 * Calcula el desglose de comisiones de una cita
 *
 * REGLAS DE NEGOCIO:
 * - Carolina: 80% ella, 15% Empresa, 5% Admin
 * - Monse: 40% ella, 35% Empresa, 25% Admin
 * - Modelo mixto: Sueldo fijo + 25% extra → ajustar a 45% Mystic Nails / 30% Admin
 */
export function calcularComisiones(
  montoBase: number, // Subtotal antes de descuento
  manicurista: Manicurista
): {
  comisionPorcentaje: number;
  empresaPorcentaje: number;
  adminPorcentaje: number;
  comisionPesos: number;
  empresaPesos: number;
  adminPesos: number;
} {
  const comision = manicurista.comision;

  // Calcular montos en pesos
  const comisionPesos = montoBase * (comision.porcentajeManicurista / 100);
  const empresaPesos = montoBase * (comision.porcentajeEmpresa / 100);
  const adminPesos = montoBase * (comision.porcentajeAdmin / 100);

  return {
    comisionPorcentaje: comision.porcentajeManicurista,
    empresaPorcentaje: comision.porcentajeEmpresa,
    adminPorcentaje: comision.porcentajeAdmin,
    comisionPesos,
    empresaPesos,
    adminPesos
  };
}

/**
 * Calcula el total que se paga a una manicurista (comisión + propina)
 * NOTA: Las propinas son 100% para la manicurista
 */
export function calcularPagoManicurista(
  comisionPesos: number,
  propina: number
): number {
  return comisionPesos + propina;
}

// ============================================
// CÁLCULO DE TOTALES DE CITA
// ============================================

/**
 * Calcula el total de una cita
 */
export function calcularTotalCita(
  servicioPrincipal: CitaServicio,
  serviciosExtra: CitaServicio[],
  descuento: number,
  deposito: number
): {
  subtotal: number;
  descuento: number;
  subtotalConDescuento: number;
  deposito: number;
  total: number;
} {
  // Sumar todos los servicios
  const subtotalServicios = serviciosExtra.reduce(
    (total, servicio) => total + servicio.subtotal,
    servicioPrincipal.subtotal
  );

  // Aplicar descuento
  const subtotalConDescuento = subtotalServicios - descuento;

  // Restar depósito (el depósito ya fue pagado, se resta del total)
  const total = subtotalConDescuento - deposito;

  return {
    subtotal: subtotalServicios,
    descuento,
    subtotalConDescuento,
    deposito,
    total
  };
}

// ============================================
// CÁLCULO DE DASHBOARD MENSUAL
// ============================================

export interface ResumenMensual {
  citasTotales: number;
  citasCompletadas: number;
  citasCanceladasNoShow: number;
  ingresosBrutos: number;
  comisionesPagadas: number;
  propinasTotal: number;
  comprasTotal: number;
  saldoNetoEmpresa: number;
  pagoNetoAdmin: number;
  promedioPorCita: number;
}

/**
 * Calcula el resumen mensual del dashboard
 */
export function calcularResumenMensual(
  citas: Cita[],
  compras: { monto: number }[],
  mes: number,
  anio: number
): ResumenMensual {
  // Filtrar citas del mes
  const citasDelMes = citas.filter(cita => {
    const fecha = new Date(cita.fecha);
    return fecha.getMonth() + 1 === mes && fecha.getFullYear() === anio;
  });

  // Solo citas completadas para cálculos financieros
  const citasCompletadas = citasDelMes.filter(cita => cita.estado === 'completada');

  // Cálculos
  const citasTotales = citasDelMes.length;
  const citasCompletadasCount = citasCompletadas.length;
  const citasCanceladasNoShow = citasDelMes.filter(
    cita => cita.estado === 'cancelada' || cita.estado === 'no-show'
  ).length;

  const ingresosBrutos = citasCompletadas.reduce((sum, cita) => sum + cita.totalCobrado, 0);
  const comisionesPagadas = citasCompletadas.reduce((sum, cita) => sum + cita.comisionPesos, 0);
  const propinasTotal = citasCompletadas.reduce((sum, cita) => sum + cita.propina, 0);
  const comprasTotal = compras.reduce((sum, compra) => sum + compra.monto, 0);

  // Saldo neto empresa = suma de empresaPorcentaje - compras
  const saldoNetoEmpresa = citasCompletadas.reduce((sum, cita) => sum + cita.empresaPesos, 0) - comprasTotal;

  // Pago neto admin = suma de adminPorcentaje
  const pagoNetoAdmin = citasCompletadas.reduce((sum, cita) => sum + cita.adminPesos, 0);

  const promedioPorCita = citasCompletadasCount > 0
    ? ingresosBrutos / citasCompletadasCount
    : 0;

  return {
    citasTotales,
    citasCompletadas: citasCompletadasCount,
    citasCanceladasNoShow,
    ingresosBrutos,
    comisionesPagadas,
    propinasTotal,
    comprasTotal,
    saldoNetoEmpresa,
    pagoNetoAdmin,
    promedioPorCita
  };
}

// ============================================
// CÁLCULO DE LIQUIDACIÓN DE MANICURISTA
// ============================================

/**
 * Calcula cuánto se le debe pagar a una manicurista en un periodo
 */
export function calcularLiquidacionManicurista(
  manicurista: Manicurista,
  citas: Cita[],
  mes: number,
  anio: number
): {
  sueldoFijo: number;
  comisionTotal: number;
  propinasTotal: number;
  totalAPagar: number;
  numCitasCompletadas: number;
} {
  // Filtrar citas completadas de la manicurista en el periodo
  const citasDelPeriodo = citas.filter(cita => {
    const fecha = new Date(cita.fecha);
    const esPeriodoCorrecto = fecha.getMonth() + 1 === mes && fecha.getFullYear() === anio;
    const esManicuristaCorrecta = cita.manicuristaId === manicurista.id;
    const estaCompletada = cita.estado === 'completada';
    return esPeriodoCorrecto && esManicuristaCorrecta && estaCompletada;
  });

  // Calcular sueldo fijo (si tiene modelo mixto)
  const sueldoFijo = manicurista.modelo === 'mixto' && manicurista.modeloMixto
    ? manicurista.modeloMixto.sueldoFijoSemanal * 4 // Asumimos 4 semanas al mes
    : 0;

  // Sumar comisiones
  const comisionTotal = citasDelPeriodo.reduce((sum, cita) => sum + cita.comisionPesos, 0);

  // Sumar propinas (100% para la manicurista)
  const propinasTotal = citasDelPeriodo.reduce((sum, cita) => sum + cita.propina, 0);

  return {
    sueldoFijo,
    comisionTotal,
    propinasTotal,
    totalAPagar: sueldoFijo + comisionTotal + propinasTotal,
    numCitasCompletadas: citasDelPeriodo.length
  };
}

// ============================================
// UTILIDADES DE FORMATO
// ============================================

/**
 * Formatea un monto a moneda MXN
 */
export function formatCurrency(amount: number): string {
  return new Intl.NumberFormat('es-MX', {
    style: 'currency',
    currency: 'MXN'
  }).format(amount);
}

/**
 * Formatea un porcentaje
 */
export function formatPercentage(value: number): string {
  return `${value}%`;
}
