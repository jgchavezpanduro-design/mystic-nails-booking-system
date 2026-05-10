/**
 * Theme colors y constantes para Mystic Nails Art
 * Paleta: Beige, Café, Tierra (estilo salón de belleza natural)
 */

export const Colors = {
  // Primary colors (Café oscuro para CTAs y acciones principales)
  primary: '#8B6F5C',         // Café medio-tierra
  primaryLight: '#A68B74',     // Café claro
  primaryDark: '#5E4A3E',      // Café oscuro

  // Secondary colors (Dorado/tierra para destacados)
  secondary: '#C9A87F',        // Dorado/tierra
  secondaryLight: '#DAB896',   // Dorado claro
  secondaryDark: '#A68B74',    // Dorado oscuro

  // Accent (Beige para elementos sutiles)
  accent: '#C4A484',           // Beige oscuro
  accentLight: '#D4B494',      // Beige claro

  // Background
  backgroundDark: '#E8DDD4',   // Beige muy claro (fondo principal)
  backgroundLight: '#FFFFFF',  // Blanco
  backgroundCard: '#D4C4B5',   // Beige medio (tarjetas)
  backgroundCardLight: '#F5F0EB', // Beige muy claro (tarjetas light mode)

  // Text
  textDark: '#5E4A3E',         // Café oscuro (texto principal)
  textLight: '#FFFFFF',        // Blanco
  textGray: '#8B7462',         // Café medio (texto secundario)
  textGrayLight: '#B1A093',    // Beige grisáceo (captions)

  // Status colors (adaptados a paleta tierra)
  success: '#7A9B76',          // Verde tierra (suave)
  error: '#B86B5B',            // Rojo tierra (apagado)
  warning: '#C9A06D',          // Naranja tierra
  info: '#7B8FA3',             // Azul tierra (muted)

  // Appointment status colors
  statusConfirmed: '#7A9B76',  // Verde tierra (confirmada)
  statusCompleted: '#7B8FA3',  // Azul tierra (completada)
  statusCancelled: '#B86B5B',  // Rojo tierra (cancelada)
  statusNoShow: '#C9A06D',     // Naranja tierra (no-show)
  statusPending: '#A68B74',    // Café medio (pendiente)

  // Client type colors
  local: '#7A9B76',            // Verde tierra (local)
  extranjera: '#7B8FA3',       // Azul tierra (extranjera)

  // UI elements
  border: '#C4B5A5',           // Beige grisáceo (bordes)
  borderDark: '#8B7462',       // Café medio (bordes oscuros)
  shadow: 'rgba(94, 74, 62, 0.1)', // Sombra café
  overlay: 'rgba(94, 74, 62, 0.5)', // Overlay café
};

export const Typography = {
  // Font sizes
  fontSizeXs: 12,
  fontSizeSm: 14,
  fontSizeMd: 16,
  fontSizeLg: 18,
  fontSizeXl: 24,
  fontSizeXxl: 32,

  // Font weights
  fontWeightRegular: '400' as const,
  fontWeightMedium: '500' as const,
  fontWeightBold: '700' as const,

  // Line heights
  lineHeightTight: 1.2,
  lineHeightNormal: 1.5,
  lineHeightLoose: 1.8,
};

export const Spacing = {
  // Padding/Margin
  xs: 4,
  sm: 8,
  md: 16,
  lg: 24,
  xl: 32,
  xxl: 48,

  // Border radius
  radiusSm: 4,
  radiusMd: 8,
  radiusLg: 12,
  radiusXl: 16,
  radiusRound: 9999,
};

export const Shadows = {
  small: {
    shadowColor: Colors.shadow,
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 2,
  },
  medium: {
    shadowColor: Colors.shadow,
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.15,
    shadowRadius: 8,
    elevation: 4,
  },
  large: {
    shadowColor: Colors.shadow,
    shadowOffset: { width: 0, height: 8 },
    shadowOpacity: 0.2,
    shadowRadius: 16,
    elevation: 8,
  },
};

export const Theme = {
  light: {
    ...Colors,
    background: Colors.backgroundLight,
    card: Colors.backgroundCardLight,
    text: Colors.textDark,
    border: Colors.border,
  },
  dark: {
    ...Colors,
    background: Colors.backgroundDark,
    card: Colors.backgroundCard,
    text: Colors.textDark,
    border: Colors.borderDark,
  },
};

export type ThemeMode = 'light' | 'dark' | 'auto';

export const StatusLabels = {
  confirmada: 'Confirmada',
  completada: 'Completada',
  cancelada: 'Cancelada',
  'no-show': 'No Show',
  pendiente: 'Pendiente',
};

export const ClienteTipoLabels = {
  Local: 'Local',
  Extranjera: 'Extranjera',
};

export const MetodoPagoLabels = {
  efectivo: 'Efectivo',
  transferencia: 'Transferencia',
  tarjeta: 'Tarjeta',
  otro: 'Otro',
};

export const ServicioCategoriaLabels = {
  Manicura: 'Manicura',
  Pedicure: 'Pedicure',
  ManiPedi: 'Mani-Pedi',
  Extra: 'Extra',
  Otro: 'Otro',
};

export const CompraCategoriaLabels = {
  productos: 'Productos',
  herramientas: 'Herramientas',
  marketing: 'Marketing',
  renta: 'Renta',
  servicios: 'Servicios',
  otro: 'Otro',
};

export const ManicuristaEstadoLabels = {
  activa: 'Activa',
  inactiva: 'Inactiva',
};

export const ManicuristaModeloLabels = {
  porcentaje: 'Porcentaje',
  mixto: 'Mixto (Fijo + %)',
};
