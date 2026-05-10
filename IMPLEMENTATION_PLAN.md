# Plan de Análisis, Diseño e Implementación E2E
## Mystic Nails Art - Mobile App

---

## 📋 TABLA DE CONTENIDOS

1. [Análisis de Requisitos](#1-análisis-de-requisitos)
2. [Arquitectura de la Información](#2-arquitectura-de-la-información)
3. [Diseño UX/UI](#3-diseño-uxui)
4. [Plan de Implementación E2E](#4-plan-de-implementación-e2e)
5. [Estrategia de Testing](#5-estrategia-de-testing)
6. [Plan de Deploy](#6-plan-de-deploy)
7. [Métricas de Éxito](#7-métricas-de-éxito)

---

## 1. ANÁLISIS DE REQUISITOS

### 1.1 Stakeholders

| Rol | Nombre | Responsabilidades | Necesidades |
|-----|--------|-------------------|-------------|
| **Admin** | Jorge (jgchavezpanduro@gmail.com) | Owner, finanzas, decisiones | Dashboard financiero, reportes, control total |
| **Co-owner** | Carolina (27supercaro@gmail.com) | Manicurista senior, gestión | Ver sus citas, comisiones, clientas |
| **Manicuristas** | Monse + otras | Realizar servicios | Ver sus citas, registrar completados |
| **Clientas** | - | Clientas del salon | (Fase 2) Reservar citas, ver historial |

### 1.2 Problemas Actuales

**Dolores principales:**
- ❌ Google Sheets no es mobile-friendly
- ❌ Cálculos manuales de comisiones propensos a errores
- ❌ No hay sincronización automática con Calendar
- ❌ Difícil usar con una mano en teléfono
- ❌ No hay notificaciones automáticas
- ❌ No hay modo offline
- ❌ No hay fotos de trabajos anteriores en la app

**Impacto:**
- Pérdida de tiempo en cálculos manuales
- Posibles errores financieros
- Mala experiencia desde smartphone
- Riesgo de perder datos sin internet

### 1.3 Objetivos del Proyecto

**Objetivo Principal:**
Reemplazar el sistema actual (Sheets + Calendar) con una app móvil nativa que sea rápida, intuitiva y funcione offline.

**Objetivos Específicos:**
1. ✅ Reducir tiempo de gestión de citas en 70%
2. ✅ Eliminar errores en cálculos de comisiones
3. ✅ Sincronización automática con Google Calendar
4. ✅ Funcionar sin conexión a internet
5. ✅ Proveer dashboard financiero en tiempo real
6. ✅ Permitir registro fotográfico de trabajos

### 1.4 Alcance del Proyecto

#### MVP (Semanas 1-6)
- ✅ Autenticación con Google
- ✅ Agenda con calendario
- ✅ Crear/editar/completar/cancelar citas
- ✅ Dashboard financiero mensual
- ✅ CRUD de clientas, servicios, manicuristas
- ✅ Registro de compras/gastos
- ✅ Liquidaciones de manicuristas
- ✅ Modo offline con sincronización

#### Fase 2 (Semanas 7-10)
- 📱 Notificaciones push (24h y 1h antes)
- 📸 Portafolio de fotos por clienta
- 📊 Reportes avanzados (retención,如何在 encontró)
- 🎨 mejoras UI/UX basadas en feedback

#### Fase 3 (Semanas 11-14)
- 🌐 Web app (responsive)
- 📋 Cierre de caja diario
- 📈 Análisis de tendencias
- 🔔 Sistema de lealtad/cumpleaños

#### Fase 4 (Futuro)
- 📱 Self-booking para clientas (WhatsApp/public link)
- 📦 Inventario básico
- 💳 Integración pagos (Stripe)
- 📊 Business Intelligence avanzado

### 1.5 Requisitos Funcionales

#### RF-001: Autenticación
- La app debe permitir login con cuenta Google
- Solo usuarios autorizados pueden acceder
- Roles: Admin (acceso total), Manicurista (acceso limitado)

#### RF-002: Gestión de Citas
- Crear cita con: fecha, hora, clienta, manicurista, servicios
- Cálculo automático de precio según tipo clienta
- Cálculo automático de comisiones según manicurista
- Estados: pendiente, confirmada, completada, cancelada, no-show
- Editar cita antes de completar
- Cancelar cita con motivo

#### RF-003: Calendario
- Vista mensual/semanal/diaria
- Mostrar citas con colores por estado
- Sincronización bidireccional con Google Calendar
- Crear evento en Calendar al crear cita
- Actualizar evento al editar cita

#### RF-004: Finalización de Cita
- Registrar propina real
- Registrar método de pago
- Subir foto del trabajo terminado
- Calcular pago total a manicurista (comisión + propina)

#### RF-005: Dashboard Financiero
- Mostrar métricas del mes seleccionado
- Citas totales, ingresos brutos, comisiones
- Saldo neto empresa, pago admin
- Promedio por cita
- Cancelaciones/no-shows

#### RF-006: Master Data (CRUD)
- Clientas: nombre, teléfono, tipo, historial
- Servicios: nombre, precios local/extranjera, tiempo
- Manicuristas: nombre, modelo de comisión, estado
- Compras: concepto, categoría, monto

#### RF-007: Liquidaciones
- Calcular pago a manicurista por periodo
- Incluir sueldo fijo (si aplica) + comisiones + propinas
- Mostrar # de citas completadas

#### RF-008: Modo Offline
- Guardar datos localmente
- Permitir crear/editar citas sin internet
- Sincronizar cuando vuelva conexión
- Mostrar indicador de sync pendiente

### 1.6 Requisitos No Funcionales

#### RNF-001: Performance
- La app debe cargar en < 3 segundos
- Las transiciones deben ser fluidas (60 FPS)
- El sync debe completarse en < 10 segundos

#### RNF-002: Usabilidad
- Debe ser posible usar con una mano
- Botones mínimos de 44x44 px (iOS) / 48x48 px (Android)
- Contraste de color WCAG AA mínimo
- Navegación intuitiva (máx 3 taps para cualquier acción)

#### RNF-003: Confiabilidad
- Disponibilidad: 99.9% uptime
- Backup automático de datos
- Recuperación ante errores de sync

#### RNF-004: Seguridad
- Autenticación requerida
- Datos financieros solo para admin
- Encriptación en tránsito (HTTPS)
- No almacenar datos sensibles localmente

#### RNF-005: Compatibilidad
- iOS 13+
- Android 8+
- Funciona en modo offline
- Responsive (varios tamaños de pantalla)

---

## 2. ARQUITECTURA DE LA INFORMACIÓN

### 2.1 Mapa del Sitio (App Structure)

```
Mystic Nails App
│
├── 🔐 Auth Flow
│   ├── Login Screen
│   └── Permissions Request
│
├── 📊 Main Tabs (After Login)
│   │
│   ├── 📅 Tab 1: Agenda
│   │   ├── Calendar Screen (Month/Week/Day views)
│   │   ├── Appointment List Screen
│   │   ├── Create Appointment Screen
│   │   ├── View Appointment Screen
│   │   ├── Edit Appointment Screen
│   │   ├── Complete Appointment Screen
│   │   └── Cancel Appointment Dialog
│   │
│   ├── 💰 Tab 2: Dashboard
│   │   ├── Dashboard Screen (Monthly metrics)
│   │   ├── Reports Screen
│   │   │   ├── Staff Payouts Screen
│   │   │   ├── Expenses Screen
│   │   │   └── Client Retention Screen
│   │   └── Create Expense Screen
│   │
│   ├── 👥 Tab 3: Clientes
│   │   ├── Clients List Screen
│   │   ├── Client Profile Screen
│   │   ├── Create Client Screen
│   │   └── Edit Client Screen
│   │
│   └── ⚙️ Tab 4: Configuración
│       ├── Settings Screen
│       ├── Services List Screen
│       ├── Service Form Screen
│       ├── Staff List Screen
│       └── Staff Form Screen
│
└── 📱 Shared Components
    ├── Search Component
    ├── Date/Time Pickers
    ├── Photo Upload Component
    ├── Currency Display Component
    └── Sync Status Indicator
```

### 2.2 Flujo de Usuarios Principales

#### Flujo 1: Crear Nueva Cita (Happy Path)

```
1. Usuario abre app
   ↓
2. Ve Calendar Screen (Tab 1)
   ↓
3. Tap en FAB "+"
   ↓
4. Create Appointment Screen
   ↓
5. Selecciona Fecha (date picker)
   ↓
6. Selecciona Hora (time picker)
   ↓
7. Busca/Selecciona Clienta (searchable dropdown)
   ↓
   [Si clienta no existe] → "Crear nueva clienta" → Create Client Screen
   ↓
8. Selecciona Manicurista (dropdown)
   ↓
9. Selecciona Servicio Principal (dropdown)
   ↓
10. [Opcional] Agrega Servicios Extra
   ↓
11. Sistema calcula automáticamente:
    - Duración total
    - Subtotal (según tipo clienta)
    - Desglose de comisiones
    ↓
12. [Opcional] Aplica Descuento
   ↓
13. [Opcional] Agrega Depósito
   ↓
14. [Opcional] Agrega Notas
   ↓
15. Preview en tiempo real:
    - Subtotal: $XXX
    - Descuento: $XX
    - Total: $XXX
    - Comisión (Manicurista): $XX (XX%)
    - Empresa: $XX (XX%)
    - Admin: $XX (XX%)
    ↓
16. Tap en "Guardar"
   ↓
17. Sistema:
    - Valida datos
    - Crea cita en Sheets
    - Crea evento en Calendar
    - Guarda localmente
    - Muestra confirmation toast
   ↓
18. Vuelve a Calendar Screen
    ↓
19. Nueva cita visible en calendario
```

#### Flujo 2: Completar Cita

```
1. Manicurista abre app
   ↓
2. Ve Calendar Screen
   ↓
3. Tap en cita "Confirmada"
   ↓
4. View Appointment Screen
   ↓
5. Tap en "Completar"
   ↓
6. Complete Appointment Screen
   ↓
7. Ingresa Propina real ($)
   ↓
8. Selecciona Método de Pago (dropdown)
   ↓
9. [Opcional] Toma foto del trabajo
   - Tap en "Tomar foto"
   - Abre cámara
   - Toma foto
   - Confirma
   ↓
10. [Opcional] Agrega Notas finales
   ↓
11. Preview final:
    - Total cobrado: $XXX
    - Comisión: $XX
    - Propina: $XX
    - Total manicurista: $XX
    ↓
12. Tap en "Confirmar Completado"
   ↓
13. Sistema:
    - Actualiza estado a "completada"
    - Guarda propina, pago, foto
    - Calcula comisiones finales
    - Actualiza Calendar (mueve evento o cancela)
    - Sincroniza con Sheets
   ↓
14. Vuelve a Calendar
   ↓
15. Cita ahora marcada como "Completada" (azul)
```

#### Flujo 3: Ver Dashboard Financiero

```
1. Admin abre app
   ↓
2. Tap en Tab 2: Dashboard
   ↓
3. Dashboard Screen
   ↓
4. Selecciona Mes/Año (default: mes actual)
   ↓
5. Sistema muestra métricas:
    ├── Citas totales: XX
    ├── Completadas: XX
    ├── Canceladas/No-show: XX
    ├── Ingresos brutos: $XXXX
    ├── Comisiones pagadas: $XXXX
    ├── Saldo neto empresa: $XXXX
    ├── Pago admin (neto): $XXXX
    ├── Promedio por cita: $XXX
    └── Propinas del mes: $XXX
   ↓
6. Tap en "Ver Reportes"
   ↓
7. Reports Screen (tabs)
   ↓
8. Tap en tab "Liquidaciones"
   ↓
9. Staff Payouts Screen
   ↓
10. Sistema muestra lista de manicuristas:
     ├── Carolina: $X,XXX (XX citas)
     ├── Monse: $X,XXX (XX citas)
     └── ...
   ↓
11. Tap en "Ver detalle" de una manicurista
    ↓
12. Sistema muestra desglose:
     ├── Sueldo fijo: $XXX
     ├── Comisiones: $XXX
     ├── Propinas: $XXX
     └── **Total a pagar: $X,XXX**
```

### 2.3 Jerarquía de Contenido

#### Nivel 1: Pantallas Principales (Tabs)
- Agenda
- Dashboard
- Clientes
- Configuración

#### Nivel 2: Pantallas Secundarias
- Calendar (vistas)
- Reportes (sub-tabs)
- Listados (Clientes, Servicios, Staff)

#### Nivel 3: Pantallas de Detalle/Formulario
- Detalle de cita
- Perfil de clienta
- Formularios de creación/edición

#### Nivel 4: Diálogos Modales
- Cancelar cita
- Confirmar eliminación
- Selector de fechas

---

## 3. DISEÑO UX/UI

### 3.1 Principios de Diseño

#### Mobile-First
- **Todo** diseñado para smartphones primero
- Interacciones touch-optimized
- One-handed operation prioritized
- Thumb-friendly zone para acciones principales

#### Simplicidad
- Minimalismo visual
- Menos es más
- Espacio negativo generoso
- Tipografía clara y legible

#### Consistencia
- Componentes reutilizables
- Patrones de interacción predecibles
- Lenguaje visual coherente

#### Feedback Inmediato
- Loading states
- Success/error messages
- Confirmations para acciones destructivas
- Indicadores de sync

### 3.2 Design System

#### Paleta de Colores

```typescript
// Primary Colors
Primary:        #FF69B4  // Hot Pink (accent, CTAs)
Primary Light:  #FFB6D9  // Light Pink (hover states)
Primary Dark:   #C71585  // Deep Pink (pressed states)

// Secondary Colors
Secondary:      #FFD700  // Gold (premium feel, highlights)
SecondaryLight: #FFE44D  // Light Gold
SecondaryDark:  #B8860B   // Dark Gold

// Neutral Colors
Background:     #1A1A1A  // Black (dark mode default)
Surface:        #2C2C2C  // Dark Gray (cards)
Text Primary:   #FFFFFF  // White
Text Secondary: #BDBDBD  // Light Gray

// Status Colors
Success:        #4CAF50  // Green (confirmada, completada)
Error:          #F44336  // Red (cancelada, error)
Warning:        #FF9800  // Orange (no-show)
Info:           #2196F3  // Blue (info)

// Client Type Colors
Local:          #4CAF50  // Green (Local clients)
Extranjera:     #2196F3  // Blue (Foreign clients)
```

#### Tipografía

```typescript
// Font Family: System Default (San Francisco para iOS, Roboto para Android)

Display Large:  32px, Bold, 1.2 lh    // Headers de pantalla
Display Medium: 24px, Bold, 1.2 lh    // Subheaders
Title Large:    20px, Medium, 1.5 lh  // Títulos de cards
Title Medium:   18px, Medium, 1.5 lh  // Títulos de sección
Body Large:     16px, Regular, 1.5 lh // Body principal
Body Medium:    14px, Regular, 1.5 lh // Body secundario
Body Small:     12px, Regular, 1.5 lh // Captions, hints
```

#### Espaciado

```typescript
// Scale: 4px base unit

XS:  4px   // Spacing entre elementos relacionados
SM:  8px   // Spacing interno de cards
MD:  16px  // Spacing estándar entre secciones
LG:  24px  // Spacing grande entre grupos
XL:  32px  // Spacing extra grande (márgenes de pantalla)
XXL: 48px  // Spacing XXL (separadores principales)
```

#### Border Radius

```typescript
SM:  4px   // Chips, tags, badgets
MD:  8px   // Cards estándar
LG:  12px  // Modals, sheets
XL:  16px  // Hero cards, featured items
Round: 999px // Botones redondeados, FAB
```

#### Sombras

```typescript
// Elevation system

Elevation 0: None (flat surfaces)
Elevation 1: 0px 2px 4px rgba(0,0,0,0.1)  // Cards
Elevation 2: 0px 4px 8px rgba(0,0,0,0.15) // Raised cards
Elevation 3: 0px 8px 16px rgba(0,0,0,0.2) // Modals, sheets
Elevation 4: 0px 12px 24px rgba(0,0,0,0.25) // FAB, dropdowns
```

### 3.3 Componentes UI Principales

#### C1: Navigation Bar (Bottom Tabs)

```
┌─────────────────────────────────────┐
│  [ICON] Agenda  │  [ICON] Dashboard│
│                                     │
│  [ICON] Clientes │  [ICON] Settings │
└─────────────────────────────────────┘
```

**Especificaciones:**
- Altura: 56px
- Background: #1A1A1A
- Iconos: 24px, color deseleccionado: #BDBDBD, seleccionado: #FF69B4
- Labels: 12px, Medium
- Sin bordes superiores
- Elevation: 4

#### C2: Header (Top Bar)

```
┌─────────────────────────────────────┐
│  ←          Título Pantalla    ⋮   │
└─────────────────────────────────────┘
```

**Especificaciones:**
- Altura: 56px
- Background: #1A1A1A
- Botón back: 24px
- Título: 20px, Medium, Left aligned
- Botón acciones: 24px
- Elevation: 2

#### C3: Card (Estándar)

```
┌─────────────────────────────────────┐
│  [Icon]  Título del Card    [→]    │
│                                     │
│  Subtítulo o descripción            │
│  Metadata adicional                 │
└─────────────────────────────────────┘
```

**Especificaciones:**
- Background: #2C2C2C
- Border Radius: 8px
- Padding: 16px
- Margin: 8px (horizontal), 4px (vertical)
- Elevation: 1
- Tap highlight: Overlay rgba(255,255,255,0.05)

#### C4: Metric Card (Dashboard)

```
┌─────────────────────────────────────┐
│  Ingresos Brutos                    │
│                                     │
│         $12,450                     │
│      +15% vs mes anterior           │
└─────────────────────────────────────┘
```

**Especificaciones:**
- Background: #2C2C2C
- Border Radius: 12px
- Padding: 20px
- Altura: 120px
- Elevation: 2
- Acento color: Borde superior 4px (usar status color)

#### C5: Calendar Card (Cita)

```
┌─────────────────────────────────────┐
│  [Color] 10:00  Maria Lopez         │
│           Manicura - Carolina       │
│           $450  [→]                │
└─────────────────────────────────────┘
```

**Especificaciones:**
- Background: #2C2C2C
- Border Radius: 8px
- Padding: 12px
- Elevation: 1
- Status indicator: Bullet 8px (left)

**Colores por estado:**
- Confirmada: #4CAF50 (Green)
- Completada: #2196F3 (Blue)
- Cancelada: #F44336 (Red)
- No-show: #FF9800 (Orange)
- Pendiente: #9370DB (Purple)

#### C6: FAB (Floating Action Button)

```
       ┌───┐
       │ + │
       └───┘
```

**Especificaciones:**
- Size: 56x56px
- Background: #FF69B4
- Icon: 24px, White
- Border Radius: 16px
- Elevation: 4
- Position: Bottom-right, 16px margin
- Pressed: Scale 0.95

#### C7: Button (Primary)

```
┌─────────────────────────────────────┐
│         GUARDAR CITA                │
└─────────────────────────────────────┘
```

**Especificaciones:**
- Height: 48px
- Background: #FF69B4
- Text: 16px, Medium, White
- Border Radius: 8px
- Horizontal padding: 24px
- Elevation: 2
- Pressed: Background #C71585

#### C8: Input Field

```
┌─────────────────────────────────────┐
│  Nombre de la clienta              │
└─────────────────────────────────────┘
```

**Especificaciones:**
- Height: 56px
- Background: #2C2C2C
- Border: 1px solid #424242
- Border Radius: 8px
- Padding: 16px horizontal
- Label: 12px, Regular, #BDBDBD
- Input: 16px, Regular, White
- Focus: Border 2px #FF69B4
- Error: Border 2px #F44336

#### C9: Date Picker Modal

```
┌─────────────────────────────────────┐
│  Selecciona Fecha         [Cancelar]│
│                                     │
│      < Mayo 2026 >                  │
│                                     │
│  D  L  M  M  J  V  S               │
│  1  2  3  4  5  6  7               │
│  8  9 10 11 12 13 14               │
│ ...                                 │
│                                     │
│              [Confirmar]            │
└─────────────────────────────────────┘
```

**Especificaciones:**
- Full screen on mobile
- Header: 56px
- Calendar: Month selector + grid
- Selected date: Circle background #FF69B4
- Today: Underline #FFD700
- Button: Full width, bottom

#### C10: Search Bar

```
┌─────────────────────────────────────┐
│  🔍 Buscar clienta...               │
└─────────────────────────────────────┘
```

**Especificaciones:**
- Height: 48px
- Background: #2C2C2C
- Border Radius: 24px
- Padding: 16px horizontal, 12px vertical
- Icon: 20px, #BDBDBD
- Placeholder: 16px, Regular, #BDBDBD
- Focus: Elevation 2

### 3.4 Layouts de Pantallas Clave

#### L1: Calendar Screen

```
┌─────────────────────────────────────┐
│  ← Agenda              Mayo 2026  → │  Header
├─────────────────────────────────────┤
│  [Mes] [Semana] [Día]               │  Segmented control
│                                     │
│  ┌───┬───┬───┬───┬───┬───┬───┐      │
│  │ D │ L │ M │ M │ J │ V │ S │      │  Calendar grid
│  ├───┼───┼───┼───┼───┼───┼───┤      │
│  │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │      │
│  └───┴───┴───┴───┴───┴───┴───┘      │
│                                     │
│  Hoy, 1 de Mayo                     │  Section header
│                                     │
│  ┌───────────────────────────────┐  │
│  │● 10:00 Maria Lopez           │  │  Appointment card
│  │  Manicura - Carolina         │  │
│  │  $450                    [→] │  │
│  └───────────────────────────────┘  │
│                                     │
│  ┌───────────────────────────────┐  │
│  │● 11:30 Ana Garcia            │  │
│  │  Pedicure - Monse            │  │
│  │  $350                    [→] │  │
│  └───────────────────────────────┘  │
│                                     │
│                        [+ FAB]       │  FAB
└─────────────────────────────────────┘
│  [Agenda] [Dash] [Clientes] [⚙️]   │  Bottom nav
└─────────────────────────────────────┘
```

#### L2: Create Appointment Screen

```
┌─────────────────────────────────────┐
│  ← Nueva Cita              [Cancelar]│  Header
├─────────────────────────────────────┤
│                                     │
│  Fecha *                            │  Label
│  ┌───────────────────────────────┐  │  Date input
│  │ 1 de Mayo de 2026         [📅] │  │
│  └───────────────────────────────┘  │
│                                     │
│  Hora *                             │
│  ┌───────────────────────────────┐  │  Time input
│  │ 10:00 AM                   [🕐] │  │
│  └───────────────────────────────┘  │
│                                     │
│  Clienta *                          │
│  ┌───────────────────────────────┐  │  Search input
│  │ 🔍 Buscar o crear...      [+] │  │
│  └───────────────────────────────┘  │
│                                     │
│  Manicurista *                      │
│  ┌───────────────────────────────┐  │  Dropdown
│  │ Carolina               [▼]    │  │
│  └───────────────────────────────┘  │
│                                     │
│  Servicio *                         │
│  ┌───────────────────────────────┐  │  Dropdown
│  │ Manicura Gel           [▼]    │  │
│  └───────────────────────────────┘  │
│                                     │
│  [+] Agregar servicio extra         │  Link button
│                                     │
│  ─────────────────────────────────  │  Divider
│                                     │
│  Resumen                            │  Section header
│  ┌───────────────────────────────┐  │  Summary card
│  │ Subtotal:           $450      │  │
│  │ Descuento:          $0        │  │
│  │ Total:              $450      │  │
│  │                             │  │
│  │ Comisión (Carolina):  $360    │  │
│  │ Empresa:            $68       │  │
│  │ Admin:              $22       │  │
│  └───────────────────────────────┘  │
│                                     │
│  Notas (opcional)                   │
│  ┌───────────────────────────────┐  │  Textarea
│  │                             │  │
│  └───────────────────────────────┘  │
│                                     │
│  ┌───────────────────────────────┐  │
│  │      GUARDAR CITA             │  │  CTA button
│  └───────────────────────────────┘  │
│                                     │
└─────────────────────────────────────┘
```

#### L3: Dashboard Screen

```
┌─────────────────────────────────────┐
│  Dashboard          Mayo 2026  [▼] │  Header
├─────────────────────────────────────┤
│                                     │
│  Resumen del Mes                    │  Section header
│                                     │
│  ┌────┐┌────┐┌────┐┌────┐          │  Metrics grid
│  │ 24 ││$12K││ $8K││$3.5K│          │
│  │Cita││Ingr││Comp││Admn │          │
│  └────┘└────┘└────┘└────┘          │
│                                     │
│  Ingresos vs Comisiones             │  Section header
│  ┌───────────────────────────────┐  │
│  │       [Chart placeholder]     │  │  Chart
│  └───────────────────────────────┘  │
│                                     │
│  Próximas citas (hoy)              │  Section header [Ver todas]
│                                     │
│  ┌───────────────────────────────┐  │
│  │● 10:00 Maria Lopez           │  │  Appointment card (compact)
│  │  Manicura - Carolina         │  │
│  └───────────────────────────────┘  │
│                                     │
│  ┌───────────────────────────────┐  │
│  │● 11:30 Ana Garcia            │  │
│  │  Pedicure - Monse            │  │
│  └───────────────────────────────┘  │
│                                     │
│  [Ver Reportes Completos]            │  Link button
│                                     │
└─────────────────────────────────────┘
│  [Agenda] [Dash] [Clientes] [⚙️]   │  Bottom nav
└─────────────────────────────────────┘
```

#### L4: Client Profile Screen

```
┌─────────────────────────────────────┐
│  ←        Maria Lopez        [Editar]│  Header
├─────────────────────────────────────┤
│                                     │
│  ┌──────┐                           │  Avatar
│  │ [📷] │  Maria Lopez              │  Name
│  └──────┘  @maria_lopez            │  Instagram
│                                     │
│  ┌───────────────────────────────┐  │  Info card
│  │ 📱 555-123-4567               │  │
│  │ 🏷️ Local                      │  │
│  │ 🎂 15 de Marzo                │  │
│  │ 🔍 Instagram                  │  │  How she found you
│  └───────────────────────────────┘  │
│                                     │
│  Notas / Alergias                   │  Section header
│  ┌───────────────────────────────┐  │  Notes card
│  │ Prefiere colores rosa y       │  │
│  │ dorado. Alergia a acrilico.   │  │
│  └───────────────────────────────┘  │
│                                     │
│  Estadísticas                       │  Section header
│  ┌────┐┌────┐┌────┐               │  Stats
│  │ 12 ││$5.4K││ 2m │               │
│  │Vis ││Gastd││Últm │               │
│  └────┘└────┘└────┘               │
│                                     │
│  Historial de Visitas               │  Section header
│                                     │
│  ┌───────────────────────────────┐  │  Visit card
│  │ 1 May 2026                    │  │
│  │ Manicura Gel - Carolina       │  │
│  │ $450                    [→]   │  │
│  └───────────────────────────────┘  │
│                                     │
│  ┌───────────────────────────────┐  │
│  │ 15 Abr 2026                   │  │
│  │ Pedicure - Monse              │  │
│  │ $350                     [→]  │  │
│  └───────────────────────────────┘  │
│                                     │
│  ┌───────────────────────────────┐  │  CTA
│  │    + NUEVA CITA               │  │
│  └───────────────────────────────┘  │
│                                     │
└─────────────────────────────────────┘
```

### 3.5 Microinteracciones

#### Animaciones de Transición
- **Screen transitions:** Slide fade (300ms)
- **Modal appearance:** Scale up (250ms) + Fade in overlay
- **Card tap:** Scale down to 0.95 + Elevation 0→2 (100ms)
- **Button press:** Scale 0.95 + Background darkening (100ms)

#### Loading States
- **Skeleton screens** para listados
- **Spinner** centrado para acciones únicas
- **Progressive loading** para imágenes

#### Feedback States
- **Success:** Toast + Checkmark icon (Green)
- **Error:** Toast + X icon (Red) + Shake animation
- **Warning:** Toast + Warning icon (Orange)
- **Info:** Toast + Info icon (Blue)

#### Gestures
- **Swipe to delete** en listas (clientes, citas)
- **Pull to refresh** en calendario y listados
- **Long press** para acciones contextuales

---

## 4. PLAN DE IMPLEMENTACIÓN E2E

### 4.1 Fase de Planificación (Semana 0-1)

#### Sprint 0: Setup y Planificación
**Objetivo:** Configurar entorno de desarrollo y planificar sprints

**Tareas:**
- [ ] Reunión de kick-off con stakeholders
- [ ] Definir prioritización de funcionalidades (MoSCoW)
- [ ] Crear backlog completo en Jira/Trello/Linear
- [ ] Configurar repositorio Git (GitHub/GitLab)
- [ ] Configurar CI/CD (GitHub Actions, Bitrise)
- [ ] Definir estrategia de branching (GitFlow)
- [ ] Configurar herramientas de diseño (Figma)
- [ ] Configurar herramientas de comunicación (Slack/Discord)
- [ ] Documentar arquitectura técnica
- [ ] Crear wiki del proyecto

**Entregables:**
- Backlog priorizado
- Repositorio configurado
- Pipeline CI/CD funcional
- Documentos de arquitectura

### 4.2 Fase de Diseño (Semana 1-2)

#### Sprint 1: Design System y Wireframes
**Objetivo:** Crear design system y wireframes de todas las pantallas

**Tareas:**
- [ ] Crear Design System en Figma
  - [ ] Paleta de colores
  - [ ] Tipografía
  - [ ] Espaciado
  - [ ] Componentes base (Button, Input, Card, etc.)
- [ ] Crear wireframes low-fidelity
  - [ ] Flujo de autenticación
  - [ ] Flujo de crear cita
  - [ ] Flujo de completar cita
  - [ ] Dashboard financiero
  - [ ] CRUD de clientes
- [ ] Revisión con stakeholders
- [ ] Iterar basado en feedback

**Entregables:**
- Design System documentado
- Wireframes revisados
- Mockups low-fidelity

#### Sprint 2: Mockups High-Fidelity
**Objetivo:** Crear mockups pixel-perfect de todas las pantallas

**Tareas:**
- [ ] Convertir wireframes a mockups high-fidelity
- [ ] Aplicar Design System
- [ ] Crear prototipo interactivo en Figma
- [ ] Diseñar estados (loading, error, empty, success)
- [ ] Diseñar componentes específicos
  - [ ] Calendar component
  - [ ] Date/time pickers
  - [ ] Photo uploader
  - [ ] Currency display
  - [ ] Sync indicator
- [ ] Revisión final con stakeholders
- [ ] Aprobación de diseños

**Entregables:**
- Mockups high-fidelity
- Prototipo interactivo
- Assets exportables (iconos, imagenes)

### 4.3 Fase de Desarrollo MVP (Semana 3-8)

#### Sprint 3: Fundación y Autenticación
**Objetivo:** Configurar arquitectura base e implementar autenticación

**Tareas:**
- [ ] Setup inicial de proyecto Expo
  - [ ] Configurar TypeScript
  - [ ] Configurar ESLint, Prettier
  - [ ] Configurar navegación (React Navigation)
- [ ] Implementar Context Providers
  - [ ] AuthContext
  - [ ] DataContext
  - [ ] ThemeContext
- [ ] Implementar servicios base
  - [ ] AsyncStorage setup
  - [ ] Google Sign-In setup
- [ ] Crear pantallas de autenticación
  - [ ] LoginScreen
  - [ ] PermissionsRequestScreen
- [ ] Implementar navegación
  - [ ] AuthNavigator
  - [ ] MainNavigator (Tabs)
- [ ] Testing unitario
- [ ] Code review

**Entregables:**
- Login funcional con Google
- Navegación base implementada
- Context providers funcionales

#### Sprint 4: Calendario y Citas (Parte 1)
**Objetivo:** Implementar pantalla de calendario y lista de citas

**Tareas:**
- [ ] Crear CalendarScreen
  - [ ] Vista mensual
  - [ ] Vista semanal
  - [ ] Vista diaria
  - [ ] Selector de mes/año
- [ ] Integrar expo-calendar
  - [ ] Solicitar permisos
  - [ ] Leer eventos de Google Calendar
  - [ ] Mostrar eventos en UI
- [ ] Crear AppointmentCard component
  - [ ] Diseño según DS
  - [ ] Estados visuales
  - [ ] Tap navigation
- [ ] Crear AppointmentListScreen
  - [ ] Lista de citas del día/semana
  - [ ] Pull to refresh
  - [ ] Empty states
- [ ] Implementar storage local para citas
- [ ] Testing integrado
- [ ] Code review

**Entregables:**
- Calendario funcional
- Lista de citas visible
- Integración con Google Calendar (lectura)

#### Sprint 5: Crear y Ver Citas
**Objetivo:** Implementar creación y visualización de citas

**Tareas:**
- [ ] Crear CreateAppointmentScreen
  - [ ] Formulario con campos requeridos
  - [ ] Date/Time pickers
  - [ ] Searchable dropdowns (clienta, manicurista, servicio)
  - [ ] Cálculo automático de precios
  - [ ] Preview de comisiones
  - [ ] Validaciones
- [ ] Crear ViewAppointmentScreen
  - [ ] Detalle completo de cita
  - [ ] Acciones disponibles según estado
  - [ ] Navegación a editar/completar/cancelar
- [ ] Implementar lógica de cálculos
  - [ ] Precios según tipo clienta
  - [ ] Comisiones según manicurista
  - [ ] Descuentos y depósitos
- [ ] Integrar con Google Sheets (create)
- [ ] Integrar con Google Calendar (create event)
- [ ] Testing integrado
- [ ] Code review

**Entregables:**
- Crear cita funcional
- Ver detalle de cita
- Cálculos automáticos funcionando

#### Sprint 6: Editar y Completar Citas
**Objetivo:** Implementar edición y finalización de citas

**Tareas:**
- [ ] Crear EditAppointmentScreen
  - [ ] Similar a Create, pre-filled
  - [ ] Validaciones de edición
- [ ] Crear CompleteAppointmentScreen
  - [ ] Registro de propina
  - [ ] Selección de método de pago
  - [ ] Foto upload
  - [ ] Preview final de comisiones
- [ ] Crear CancelAppointmentDialog
  - [ ] Confirmación
  - [ ] Razón de cancelación
  - [ ] Checkbox para aplicar cargo
- [ ] Integrar con Google Sheets (update)
- [ ] Integrar con Google Calendar (update/delete event)
- [ ] Implementar cambios de estado
- [ ] Testing integrado
- [ ] Code review

**Entregables:**
- Edición de citas funcional
- Completado de citas con foto
- Cancelación de citas

#### Sprint 7: Dashboard Financiero
**Objetivo:** Implementar dashboard y reportes básicos

**Tareas:**
- [ ] Crear DashboardScreen
  - [ ] Selector de mes/año
  - [ ] Métricas principales (cards)
  - [ ] Gráfico de ingresos vs comisiones
  - [ ] Lista de próximas citas
- [ ] Crear ReportsScreen
  - [ ] Tabs navigation
  - [ ] Tab "Liquidaciones"
  - [ ] Tab "Compras"
  - [ ] Tab "Retención"
- [ ] Crear StaffPayoutsScreen
  - [ ] Lista de manicuristas con liquidaciones
  - [ ] Desglose de pagos
  - [ ] Marcar como pagado
- [ ] Crear ExpensesScreen
  - [ ] Lista de compras
  - [ ] Crear nueva compra
- [ ] Implementar cálculos de dashboard
  - [ ] Resumen mensual
  - [ ] Liquidaciones
- [ ] Testing integrado
- [ ] Code review

**Entregables:**
- Dashboard funcional con métricas
- Reportes de liquidaciones
- Registro de compras

#### Sprint 8: Master Data CRUD
**Objetivo:** Implementar gestión de catálogos

**Tareas:**
- [ ] Crear ClientsListScreen
  - [ ] Search bar
  - [ ] Lista de clientes
  - [ ] Pull to refresh
- [ ] Crear ClientProfileScreen
  - [ ] Detalle completo
  - [ ] Historial de visitas
  - [ ] Estadísticas
  - [ ] Galería de fotos
- [ ] Crear CreateClientScreen / EditClientScreen
- [ ] Crear ServicesListScreen / ServiceFormScreen
- [ ] Crear StaffListScreen / StaffFormScreen
- [ ] Implementar storage local para master data
- [ ] Integrar con Google Sheets (CRUD completo)
- [ ] Testing integrado
- [ ] Code review

**Entregables:**
- CRUD de clientes completo
- CRUD de servicios completo
- CRUD de manicuristas completo

### 4.4 Fase de Integración y Polish (Semana 9-10)

#### Sprint 9: Modo Offline y Sync
**Objetivo:** Implementar sincronización bidireccional

**Tareas:**
- [ ] Implementar sync manager
  - [ ] Detectar cambios locales
  - [ ] Cola de sincronización
  - [ ] Reintentos automáticos
  - [ ] Conflict resolution
- [ ] Implementar sync indicator en UI
  - [ ] Icono de estado en header
  - [ ] Mensajes de sync en curso
  - [ ] Errores de sync
- [ ] Implementar offline mode
  - [ ] Detectar connectivity
  - [ ] Mostrar warning sin conexión
  - [ ] Guardar todo localmente
- [ ] Testing de sync
  - [ ] Escenario: crear sin internet
  - [ ] Escenario: editar sin internet
  - [ ] Escenario: conflicto de datos
- [ ] Performance optimization
- [ ] Code review

**Entregables:**
- Modo offline funcional
- Sincronización automática
- Indicadores visuales de sync

#### Sprint 10: Polish y Bug Fixes
**Objetivo:** Pulir UI, corregir bugs, optimizar performance

**Tareas:**
- [ ] Revisión general de UI
  - [ ] Consistencia con Design System
  - [ ] Espaciados y alineaciones
  - [ ] Estados de componentes
- [ ] Optimización de performance
  - [ ] Lazy loading de pantallas
  - [ ] Optimizar renders
  - [ ] Memoization de cálculos
- [ ] Accessibility audit
  - [ ] Contrast ratios
  - [ ] Screen readers
  - [ ] Touch targets
- [ ] Bug fixes
  - [ ] Lista de bugs conocidos
  - [ ] Priorización y fixes
- [ ] Beta testing con usuarios reales
- [ ] Iterar basado en feedback

**Entregables:**
- App pulida y optimizada
- Bugs críticos resueltos
- Feedback de beta testers

### 4.5 Fase de Deploy (Semana 11-12)

#### Sprint 11: Testing E2E y QA
**Objetivo:** Pruebas exhaustivas end-to-end

**Tareas:**
- [ ] Testing E2E automático
  - [ ] Flujo completo de cita
  - [ ] Flujo de autenticación
  - [ ] Sync offline-online
  - [ ] CRUD operations
- [ ] Manual QA
  - [ ] Test cases para cada pantalla
  - [ ] Test cases para cada flujo
  - [ ] Test cases edge cases
- [ ] Compatibility testing
  - [ ] iOS (diferentes versiones)
  - [ ] Android (diferentes versiones y tamaños)
  - [ ] Diferentes orientaciones
- [ ] Security testing
  - [ ] Autenticación
  - [ ] Permisos
  - [ ] Data encryption
- [ ] Performance testing
  - [ ] Load testing
  - [ ] Stress testing
  - [ ] Memory leaks
- [ ] Bug fixes basados en testing

**Entregables:**
- Test suite completo
- Reporte de bugs y fixes
- App lista para producción

#### Sprint 12: Deploy a Producción
**Objetivo:** Desplegar app a producción

**Tareas:**
- [ ] Configurar Expo EAS
  - [ ] Setup de proyecto
  - [ ] Configurar builds
  - [ ] Configurar submit stores
- [ ] Build Android
  - [ ] APK para testing interno
  - [ ] AAB para Play Store
- [ ] Build iOS
  - [ ] IPA para TestFlight
  - [ ] Distribución a testers
- [ ] Preparar store listings
  - [ ] Screenshots
  - [ ] Descripciones
  - [ ] Iconos
  - [ ] Políticas de privacidad
- [ ] Submit a stores
  - [ ] Google Play Store
  - [ ] Apple App Store
- [ ] Deploy del Google Apps Script
  - [ ] Deploy a producción
  - [ ] Configurar URL en app
- [ ] Documentación de deploy
- [ ] Handover a stakeholders

**Entregables:**
- App disponible en stores
- Google Apps Script en producción
- Documentación de deploy

---

## 5. ESTRATEGIA DE TESTING

### 5.1 Pirámide de Testing

```
        ▲
       /E\      E2E Tests (10%)
      /2E2\     - Flujos críticos
     /-----\    - Happy paths
    /  Unit  \  Unit Tests (70%)
   /  Tests  \ - Componentes
  /-----------\ - Utilidades
 /Integration  \ Integration Tests (20%)
/   Tests     \ - API calls
---------------  - Data flow
```

### 5.2 Unit Tests (70%)

**Qué testear:**
- Funciones de cálculo (comisiones, precios)
- Utilidades (formatCurrency, formatDate)
- Componentes puros (Button, Input, Card)
- Hooks personalizados

**Herramientas:**
- Jest
- React Native Testing Library

**Ejemplo:**
```typescript
describe('calcularComisiones', () => {
  it('debe calcular comisión de Carolina correctamente', () => {
    const result = calcularComisiones(100, carolinaManicurista);
    expect(result.comisionPesos).toBe(80);
    expect(result.empresaPesos).toBe(15);
    expect(result.adminPesos).toBe(5);
  });
});
```

### 5.3 Integration Tests (20%)

**Qué testear:**
- Integración con Google Sheets
- Integración con Google Calendar
- Integración con AsyncStorage
- Flows de navegación
- Context providers

**Herramientas:**
- Jest
- React Native Testing Library
- MSW (Mock Service Worker)

**Ejemplo:**
```typescript
describe('Create Appointment Flow', () => {
  it('debe crear cita y sincronizar con Sheets y Calendar', async () => {
    const { getByText, getByPlaceholderText } = render(<CreateAppointmentScreen />);
    // ... fill form
    await fireEvent.press(getByText('Guardar'));
    await waitFor(() => expect(createCita).toHaveBeenCalled());
    await waitFor(() => expect(createCalendarEvent).toHaveBeenCalled());
  });
});
```

### 5.4 E2E Tests (10%)

**Qué testear:**
- Flujo completo de crear cita
- Flujo de login
- Flujo de sync offline-online
- Flujos críticos de negocio

**Herramientas:**
- Detox (iOS/Android)
- Maestro (alternativa más simple)

**Ejemplo:**
```typescript
describe('Happy Path: Crear Cita', () => {
  it('debe completar el flujo de crear cita exitosamente', async () => {
    await device.launchApp();
    await element(by.id('login-button')).tap();
    await element(by.id('calendar-tab')).tap();
    await element(by.id('fab-new-appointment')).tap();
    await element(by.id('date-picker')).setDate('2026-05-01');
    await element(by.id('time-picker')).setTime('10:00');
    await element(by.id('clienta-search')).typeText('Maria');
    await element(by.label('Maria Lopez')).tap();
    await element(by.id('manicurista-dropdown')).tap();
    await element(by.label('Carolina')).tap();
    await element(by.id('servicio-dropdown')).tap();
    await element(by.label('Manicura Gel')).tap();
    await element(by.id('save-button')).tap();
    await expect(element(by.text('Cita creada'))).toBeVisible();
  });
});
```

### 5.5 Manual QA Checklist

#### Funcional Testing
- [ ] Login con Google funciona
- [ ] Se puede crear cita
- [ ] Se puede editar cita
- [ ] Se puede completar cita
- [ ] Se puede cancelar cita
- [ ] Se pueden crear/editar clientes
- [ ] Se pueden crear/editar servicios
- [ ] Se pueden crear/editar manicuristas
- [ ] Dashboard muestra métricas correctas
- [ ] Liquidaciones son correctas
- [ ] Sync con Google Sheets funciona
- [ ] Sync con Google Calendar funciona
- [ ] Modo offline funciona
- [ ] Sync automático al volver online

#### UI/UX Testing
- [ ] Todos los elementos son accesables con una mano
- [ ] Touch targets tienen mínimo 44px
- [ ] Contraste de color cumple WCAG AA
- [ ] Animaciones son fluidas (60 FPS)
- [ ] No hay crashes al rotar pantalla
- [ ] Teclado no oculta campos importantes
- [ ] Estados de loading son claros
- [ ] Errores tienen mensajes claros

#### Compatibility Testing
- [ ] iOS 13, 14, 15, 16
- [ ] Android 8, 9, 10, 11, 12, 13
- [ ] iPhone SE, iPhone 13, iPhone 14 Pro
- [ ] Android pequeño, mediano, grande
- [ ] Pantallas notch y sin notch

#### Performance Testing
- [ ] App carga en < 3 segundos
- [ ] Transiciones son fluidas
- [ ] No hay memory leaks
- [ ] Scroll es suave en listas largas
- [ ] Sync completa en < 10 segundos

---

## 6. PLAN DE DEPLOY

### 6.1 Estrategia de Release

#### Fase 1: Alpha Release (Interna)
**Público:** Solo desarrolladores y stakeholders
**Duración:** 1 semana
**Objetivo:** Probar funcionalidad básica

**Tareas:**
- [ ] Distribuir APK/IPA a equipo interno
- [ ] Configurar crash reporting (Sentry/Bugsnag)
- [ ] Configurar analytics (Mixpanel/Firebase Analytics)
- [ ] Recopilar feedback
- [ ] Fixes críticos

#### Fase 2: Beta Release (Cerrada)
**Público:** 10-20 usuarios reales seleccionados
**Duración:** 2 semanas
**Objetivo:** Probar UX y encontrar bugs

**Tareas:**
- [ ] Distribuir via TestFlight (iOS) y Play Store Internal Testing (Android)
- [ ] Onboarding a beta testers
- [ ] Recopilar feedback estructurado
- [ ] Monitorear crashes y errores
- [ ] Iterar rapidamente

#### Fase 3: Public Launch
**Público:** Todos los usuarios
**Duración:** Indefinida
**Objetivo:** Adopción masiva

**Tareas:**
- [ ] Submit a App Store y Play Store
- [ ] Esperar aprobación (puede tomar 1-3 días)
- [ ] Anunciar launch
- [ ] Monitorear métricas de launch
- [ ] Soporte post-launch

### 6.2 Checklist Pre-Production

#### Technical
- [ ] Todos los tests pasan
- [ ] Code reviews completados
- [ ] Bugs críticos resueltos
- [ ] Performance optimizada
- [ ] Security audit completado
- [ ] Crash reporting configurado
- [ ] Analytics configurados
- [ ] Push notifications configuradas
- [ ] Backend deployado y testeado
- [ ] Backup plan configurado

#### Design
- [ ] Todos los screenshots listos
- [ ] Iconos de la app listos (todos los tamaños)
- [ ] Splash screen lista
- [ ] Copy de store listings revisado
- [ ] Políticas de privacidad creadas
- [ ] Términos de uso creados

#### Business
- [ ] Cuenta de开发者 configurada (Apple, Google)
- [ ] Certificados de distribución obtenidos
- [ ] Política de precios definida (si aplica)
- [ ] Plan de comunicación listo
- [ ] Equipo de soporte capacitado
- [ ] Documentación de help desk creada

### 6.3 Proceso de Deploy

#### iOS Deploy (App Store)

1. **Preparar build en Expo EAS**
   ```bash
   eas build --platform ios --profile production
   ```

2. **Configurar en app.json**
   ```json
   {
     "expo": {
       "ios": {
         "bundleIdentifier": "com.mysticnails.app",
         "buildNumber": "1.0.0"
       }
     }
   }
   ```

3. **Submit a TestFlight**
   - Subir IPA a App Store Connect
   - Configurar información de testing
   - Invitar a beta testers

4. **Submit a App Store**
   - Completar store listing
   - Subir screenshots
   - Enviar a revisión
   - Esperar aprobación (1-3 días)

#### Android Deploy (Play Store)

1. **Preparar build en Expo EAS**
   ```bash
   eas build --platform android --profile production
   ```

2. **Configurar en app.json**
   ```json
   {
     "expo": {
       "android": {
         "package": "com.mysticnails.app",
         "versionCode": 1
       }
     }
   }
   ```

3. **Firmar APK/AAB**
   - Crear keystore
   - Configurar signing credentials

4. **Submit a Play Store**
   - Crear app en Google Play Console
   - Completar store listing
   - Subitar AAB
   - Enviar a revisión (1-7 días)

#### Backend Deploy (Google Apps Script)

1. **Actualizar configuración**
   - Reemplazar URLs de prueba con producción
   - Configurar spreadsheets correctos

2. **Deploy como Web App**
   - Nuevo deployment
   - Versión: "production"
   - Execute as: "Me"
   - Who has access: "Anyone"

3. **Testing final**
   - Probar endpoints con Postman
   - Verificar integraciones

### 6.4 Post-Launch Monitorización

#### Primeras 24 horas
- Monitorear crash reports cada 2 horas
- Revisar analytics de adopción
- Responder reviews en stores
- Estar listo para hotfix

#### Primera semana
- Monitorear crash reports diariamente
- Revisar performance metrics
- Recopilar feedback temprano
- Planificar primera actualización

#### Primer mes
- Análisis de retention
- Análisis de features más usadas
- Identificar oportunidades de mejora
- Roadmap de v1.1

---

## 7. MÉTRICAS DE ÉXITO

### 7.1 Métricas de Adopción

#### User Acquisition
- **Descargas totales** (iOS + Android)
- **Descargas por semana** (primer mes)
- **Costo por adquisición** (si hay marketing pagado)

#### User Activation
- **Tasa de registro exitoso** (% de descargas que completan login)
- **Tasa de primera cita creada** (% de usuarios que crean cita en primera semana)
- **Time to first value** (tiempo promedio para crear primera cita)

### 7.2 Métricas de Engagement

#### Daily Active Users (DAU)
- Usuarios únicos por día
- Meta: 80% de manicuristas diariamente

#### Weekly Active Users (WAU)
- Usuarios únicos por semana
- Meta: 100% de manicuristas semanalmente

#### Session Metrics
- **Sesiones por usuario por día**
- **Duración promedio de sesión**
- **Pantallas vistas por sesión**

#### Feature Usage
- **% de usuarios que usa cada feature**
  - Crear citas
  - Completar citas
  - Ver dashboard
  - Buscar clientes
- **Frecuencia de uso de cada feature**

### 7.3 Métricas de Retención

#### Retention Rates
- **Day 1 retention** (% que regresa al día siguiente)
- **Day 7 retention** (% que regresa después de 7 días)
- **Day 30 retention** (% que regresa después de 30 días)
- **Meta**: Day 1 > 60%, Day 7 > 40%, Day 30 > 20%

#### Churn Rate
- **Monthly churn** (% que deja de usar la app mensualmente)
- **Meta**: < 10% monthly churn

### 7.4 Métricas de Performance

#### Technical Performance
- **App startup time** (Meta: < 3 segundos)
- **Time to interactive** (Meta: < 5 segundos)
- **API response time** (Meta: < 1 segundo)
- **Sync time** (Meta: < 10 segundos)
- **Crash-free users** (Meta: > 99%)

#### App Performance
- **Frame rate** (Meta: 60 FPS constante)
- **Memory usage** (Meta: < 150 MB promedio)
- **Battery impact** (Meta: Bajo impacto)
- **Network usage** (Meta: < 50 MB/day)

### 7.5 Métricas de Negocio

#### Productivity Metrics
- **Reducción en tiempo de gestión de citas** (Meta: 70%)
- **Reducción en errores de cálculo** (Meta: 95%)
- **Aumento en productividad** (citas por día)

#### Financial Metrics
- **ROI del proyecto** (costo de desarrollo vs valor generado)
- **Ahorro de tiempo** (horas ahorras al mes)
- **Impacto en ingresos** (aumento en citas/mes)

#### User Satisfaction
- **NPS** (Net Promoter Score)
- **App Store rating** (Meta: > 4.5 estrellas)
- **Play Store rating** (Meta: > 4.5 estrellas)
- **Qualitative feedback** (comentarios positivos vs negativos)

### 7.6 Métricas de Calidad

#### Bug Metrics
- **Crash rate** (crashes por 1000 sesiones)
- **Bug reports por semana**
- **Time to fix** bugs críticos
- **Bugs abiertos vs cerrados**

#### UX Metrics
- **Task completion rate** (% que completa tareas exitosamente)
- **Task completion time** (tiempo promedio por tarea)
- **Error rate** (errores por tarea)
- **User errors vs system errors**

---

## 8. RIESGOS Y MITIGACIÓN

### 8.1 Riesgos Técnicos

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|-------------|---------|------------|
| Google Apps Script rate limit | Media | Alto | Implementar caching, batch requests, considerar migración a backend propio |
| Sync conflicts | Alta | Medio | Implementar strategy de "last write wins" con timestamps |
| Performance issues en dispositivos viejos | Media | Medio | Lazy loading, optimización de assets, testing en dispositivos低端 |
| Battery drain | Media | Medio | Optimizar network requests, background tasks eficientes |
| Memory leaks | Baja | Alto | Testing exhaustivo, profiling, React Strict Mode |

### 8.2 Riesgos de Usuario

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|-------------|---------|------------|
| Resistencia al cambio | Alta | Alto | Onboarding claro, entrenamiento, soporte temprano |
| Curva de aprendizaje empinada | Media | Medio | UX intuitiva, tooltips, tutorial en primera sesión |
| Abandono por bugs | Media | Alto | Beta testing extenso, crash reporting, hotfix rápido |

### 8.3 Riesgos de Negocio

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|-------------|---------|------------|
| Scope creep | Alta | Alto | MVP claro, cambio controlado, re-priorización |
| Delay en timeline | Media | Alto | Buffer en estimaciones, sprints cortos, comunicación constante |
| Costos over budget | Media | Medio | Tracking de horas, weekly budget reviews, cut features si necesario |

---

## 9. CONCLUSIÓN

Este plan E2E proporciona una roadmap completo para desarrollar Mystic Nails Art app en 12 semanas:

- **Semanas 0-2:** Planificación y Diseño
- **Semanas 3-8:** Desarrollo MVP
- **Semanas 9-10:** Integración y Polish
- **Semanas 11-12:** Testing y Deploy

**Key Success Factors:**
1. **MVP claro y enfocado** - No过度功能
2. **Design system sólido** - Consistencia UI/UX
3. **Arquitectura escalable** - Preparado para crecer
4. **Testing exhaustivo** - Calidad desde el inicio
5. **Deploy incremental** - Alpha → Beta → Public
6. **Monitorización continua** - Métricas guía mejoras

**Next Steps:**
1. Aprobar plan con stakeholders
2. Iniciar Sprint 0 (Setup)
3. Comenzar diseño en Figma
4. Configurar repositorio y CI/CD
5. ¡A programar! 🚀
