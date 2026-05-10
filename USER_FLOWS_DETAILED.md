# Flujos de Usuario Detallados para Stitch
## Mystic Nails Art - Wireframes & Mockups

---

## 📱 ÍNDICE DE FLUJOS

1. [Flujo 1: Onboarding & Registro](#flujo-1-onboarding--registro)
2. [Flujo 2: Crear Nueva Cita](#flujo-2-crear-nueva-cita) ⭐ CRÍTICO
3. [Flujo 3: Ver Detalle de Cita](#flujo-3-ver-detalle-de-cita)
4. [Flujo 4: Completar Cita](#flujo-4-completar-cita) ⭐ CRÍTICO
5. [Flujo 5: Editar Cita](#flujo-5-editar-cita)
6. [Flujo 6: Cancelar Cita](#flujo-6-cancelar-cita)
7. [Flujo 7: Dashboard Financiero](#flujo-7-dashboard-financiero)
8. [Flujo 8: Gestión de Clientes](#flujo-8-gestión-de-clientes)
9. [Flujo 9: Calendario & Agenda](#flujo-9-calendario--agenda)
10. [Flujo 10: Configuración & Settings](#flujo-10-configuración--settings)

---

## FLUJO 1: ONBOARDING & REGISTRO

### Objetivo
Usuario nuevo se registra y configura la app por primera vez.

### Pantallas Involucradas
1. Welcome Screen
2. Google Sign-In Screen
3. Permissions Request Screen
4. Quick Tutorial (3 screens, skippable)
5. Main App (Calendar Screen)

---

### SCREEN 1.1: Welcome Screen

**Propósito:** Presentar la app y su valor

**Layout:**
```
┌─────────────────────────────────────┐
│                                     │
│         [LOGO MYSTIC NAILS]         │
│                                     │
│      Gestiona tu salón de           │
│      uñas en segundos, no horas     │
│                                     │
│  ✓ Citas inteligentes               │
│  ✓ Comisiones automáticas           │
│  ✓ Dashboard financiero             │
│  ✓ Sincronización con Calendar      │
│                                     │
│                                     │
│  ┌───────────────────────────────┐ │
│  │    COMENZAR CON GOOGLE        │ │  [Google icon]
│  └───────────────────────────────┘ │
│                                     │
│                                     │
└─────────────────────────────────────┘
```

**Elementos UI:**
- **Logo:** Centro, grande (120px), con gradiente rosa-dorado
- **Título:** "Mystic Nails Art" (32px, Bold)
- **Subtítulo:** "Gestiona tu salón en segundos" (18px, Regular, gris claro)
- **Feature list:** 
  - 4 items con checkmarks verdes
  - Texto: 16px, Medium
  - Color: #BDBDBD
- **CTA Button:**
  - Texto: "Comenzar con Google"
  - Icono de Google (20px)
  - Background: #FF69B4 (rosa)
  - Height: 56px
  - Border radius: 8px
  - Full width (menos 32px márgenes)

**Acciones:**
- Tap en CTA → Navegar a Screen 1.2 (Google Sign-In)

**Estados:**
- Normal: Mostrar pantalla completa
- Loading: Despues de tap en CTA, mostrar spinner
- Error: Toast con mensaje de error

**Transiciones:**
- Push transition (slide from right, 300ms)

---

### SCREEN 1.2: Google Sign-In Loading

**Propósito:** Mostrar progreso durante autenticación

**Layout:**
```
┌─────────────────────────────────────┐
│                                     │
│         [LOGO PEQUEÑO]              │
│                                     │
│         Iniciando sesión...         │
│                                     │
│           [SPINNER]                 │
│         Rosa, girando               │
│                                     │
│                                     │
│      Esto puede tomar unos           │
│      segundos, espera un            │
│      momento por favor              │
│                                     │
│                                     │
└─────────────────────────────────────┘
```

**Elementos UI:**
- **Logo pequeño:** 48px, centro
- **Título:** "Iniciando sesión..." (20px, Medium)
- **Spinner:** Rosa (#FF69B4), 32px, centro
- **Mensaje:** 16px, Regular, gris

**Acciones:**
- Automático → Navegar a Screen 1.3 (Permissions) si success
- Automático → Mostrar error toast si falla

**Timeout:** 15 segundos max

---

### SCREEN 1.3: Permissions Request

**Propósito:** Solicitar permisos necesarios (Calendar, Camera, Notifications)

**Layout:**
```
┌─────────────────────────────────────┐
│  ← Permisos necesarios    [Omitir] │
├─────────────────────────────────────┤
│                                     │
│  Para que Mystic Nails funcione     │
│  correctamente, necesitamos         │
│  acceso a:                          │
│                                     │
│  ┌───────────────────────────────┐ │
│  │ 📅 Calendario                 │ │
│  │ Para sincronizar tus citas    │ │
│  │            [Permitir]          │ │
│  └───────────────────────────────┘ │
│                                     │
│  ┌───────────────────────────────┐ │
│  │ 📷 Cámara                     │ │
│  │ Para subir fotos de trabajos  │ │
│  │            [Permitir]          │ │
│  └───────────────────────────────┘ │
│                                     │
│  ┌───────────────────────────────┐ │
│  │ 🔔 Notificaciones             │ │
│  │ Para recordatorios de citas   │ │
│  │            [Permitir]          │ │
│  └───────────────────────────────┘ │
│                                     │
│  ┌───────────────────────────────┐ │
│  │    CONTINUAR (3 de 3)         │ │
│  └───────────────────────────────┘ │
│                                     │
└─────────────────────────────────────┘
```

**Elementos UI:**
- **Header:**
  - Back button: "<" (24px)
  - Título: "Permisos necesarios" (20px, Medium)
  - "Omitir" button: Text link (16px, rosa)
- **Permission cards (3):**
  - Icono: 32px (Calendar, Camera, Bell)
  - Título: Bold, 18px
  - Descripción: Regular, 14px, gris
  - Button "Permitir": Outline rosa, 36px height
- **CTA principal:**
  - Texto: "CONTINUAR (3 de 3)"
  - Background: Gris si no todos permitidos
  - Background: Rosa si todos permitidos
  - Full width

**Estados de Permission Cards:**
- **Not requested:** Button "Permitir" (outline rosa)
- **Requesting:** Button con spinner
- **Granted:** Checkmark verde + "Permitido" (texto verde)

**Acciones:**
- Tap en "Permitir" → Solicitar permiso nativo
- Tap en "Omitir" → Saltar a Screen 1.4 (Tutorial)
- Tap en "CONTINUAR" → Navegar a Screen 1.4

**Validaciones:**
- CTA habilitado solo si todos los permisos están granted o skipped

---

### SCREEN 1.4: Tutorial Screen 1/3

**Propósito:** Enseñar al usuario a usar el calendario

**Layout:**
```
┌─────────────────────────────────────┐
│                                     │
│  ┌───────────────────────────────┐ │
│  │                               │ │
│  │     [ILUSTRACIÓN CALENDARIO]  │ │
│  │     (Dibujado o 3D)           │ │
│  │                               │ │
│  └───────────────────────────────┘ │
│                                     │
│        Gestiona tu Agenda          │
│                                     │
│  Ve tus citas del día, semana       │
│  o mes. Toca una cita para         │
│  ver detalles o editar.             │
│                                     │
│  ┌───────────────────────────────┐ │
│  │      Siguiente →              │ │
│  └───────────────────────────────┘ │
│                                     │
│            Omitir tutorial          │
│                                     │
└─────────────────────────────────────┘
```

**Elementos UI:**
- **Ilustración:** 240px height, centro
- **Título:** "Gestiona tu Agenda" (28px, Bold)
- **Descripción:** 16px, Regular, gris, 2 líneas max
- **CTA:** "Siguiente →" (rosa, outline)
- **Skip link:** "Omitir tutorial" (14px, gris, subrayado)

**Acciones:**
- Tap en "Siguiente" → Screen 1.5 (Tutorial 2/3)
- Tap en "Omitir" → Navegar a Calendar Screen (main app)

---

### SCREEN 1.5: Tutorial Screen 2/3

**Propósito:** Enseñar a completar citas

**Layout:**
```
┌─────────────────────────────────────┐
│                                     │
│  ┌───────────────────────────────┐ │
│  │                               │ │
│  │   [ILUSTRACIÓN COMPLETAR]     │ │
│  │   (Manicurista tomando foto)  │ │
│  │                               │ │
│  └───────────────────────────────┘ │
│                                     │
│      Completa Citas en Segundos     │
│                                     │
│  Registra propina, método de        │
│  pago y sube foto del trabajo.      │
│  ¡Todo en menos de 30 segundos!     │
│                                     │
│  ← Anterior     Siguiente →         │
│                                     │
└─────────────────────────────────────┘
```

**Elementos UI:**
- Similar a Screen 1.4
- Dos CTAs: "Anterior" (gris) y "Siguiente" (rosa)

---

### SCREEN 1.6: Tutorial Screen 3/3

**Propósito:** Enseñar a ver ganancias

**Layout:**
```
┌─────────────────────────────────────┐
│                                     │
│  ┌───────────────────────────────┐ │
│  │                               │ │
│  │   [ILUSTRACIÓN DASHBOARD]     │ │
│  │   (Gráfica de dinero)         │ │
│  │                               │ │
│  └───────────────────────────────┘ │
│                                     │
│        Mira tus Ganancias          │
│                                     │
│  Consulta tus comisiones,           │
│  propinas y liquidaciones           │
│  del mes en tiempo real.            │
│                                     │
│  ┌───────────────────────────────┐ │
│  │        ¡Comenzar!              │ │
│  └───────────────────────────────┘ │
│                                     │
└─────────────────────────────────────┘
```

**Elementos UI:**
- CTA primario: "¡Comenzar!" (rosa, solid)

**Acciones:**
- Tap en "¡Comenzar!" → Navegar a Calendar Screen (main app)

---

## FLUJO 2: CREAR NUEVA CITA ⭐ CRÍTICO

### Objetivo
Usuario crea una nueva cita con todos los campos requeridos y ve el cálculo en tiempo real.

### Pantallas Involucradas
1. Calendar Screen (punto de partida)
2. Create Appointment Screen (form principal)
3. Create Client Modal (si clienta no existe)
4. Appointment Confirmation Modal

### Trigger
- Usuario tap en FAB "+" en Calendar Screen
- O usuario tap en "Nueva Cita" desde Dashboard

---

### SCREEN 2.1: Create Appointment Screen

**Propósito:** Formulario principal para crear cita

**Layout:**
```
┌─────────────────────────────────────┐
│  ← Nueva Cita               [Cancelar]│
├─────────────────────────────────────┤
│                                     │
│  Fecha *                            │
│  ┌───────────────────────────────┐ │
│  │ 1 de Mayo de 2026         [📅] │ │
│  └───────────────────────────────┘ │
│                                     │
│  Hora *                            │
│  ┌───────────────────────────────┐ │
│  │ 10:00 AM                  [🕐] │ │
│  └───────────────────────────────┘ │
│                                     │
│  Clienta *                         │
│  ┌───────────────────────────────┐ │
│  │ 🔍 Buscar o crear...      [+] │ │
│  └───────────────────────────────┘ │
│                                     │
│  ─────────────────────────────────  │
│  ↑ Selecciona una clienta primero ↑ │
│  ─────────────────────────────────  │
│                                     │
│  Manicurista *                     │  ← Deshabilitado hasta seleccionar clienta
│  ┌───────────────────────────────┐ │
│  │ Seleccionar clienta...        │ │
│  └───────────────────────────────┘ │
│                                     │
│  Servicio *                        │  ← Deshabilitado hasta seleccionar clienta
│  ┌───────────────────────────────┐ │
│  │ Seleccionar clienta...        │ │
│  └───────────────────────────────┘ │
│                                     │
│  Servicios Extra                   │  ← Deshabilitado hasta seleccionar servicio principal
│  [+ Agregar servicio]               │
│                                     │
│  ─────────────────────────────────  │
│           RESUMEN                  │
│  ─────────────────────────────────  │
│  ┌───────────────────────────────┐ │
│  │ Subtotal:           $0        │ │
│  │ Descuento:          $0        │ │
│  │ Total:              $0        │ │
│  │                             │ │
│  │ Comisión:           $0 (0%)   │ │
│  │ Empresa:            $0 (0%)   │ │
│  │ Admin:              $0 (0%)   │ │
│  └───────────────────────────────┘ │
│                                     │
│  Notas (opcional)                   │
│  ┌───────────────────────────────┐ │
│  │                             │ │
│  └───────────────────────────────┘ │
│                                     │
│  ┌───────────────────────────────┐ │
│  │      GUARDAR CITA             │ │  ← Deshabilitado hasta completar campos requeridos
│  └───────────────────────────────┘ │
│                                     │
└─────────────────────────────────────┘
```

**Elementos UI - Detallados:**

#### 1. Header
- **Back button:** "<" (24px, left)
- **Título:** "Nueva Cita" (20px, Medium, center)
- **Cancelar:** Text link (16px, rosa, right)

#### 2. Fecha Input
- **Label:** "Fecha *" (16px, Medium, rosa)
- **Input field:**
  - Height: 56px
  - Background: #2C2C2C
  - Border radius: 8px
  - Padding: 16px horizontal
  - Text: "1 de Mayo de 2026" (16px, Regular)
  - Icon: Calendar (20px, derecha)
  - Border: 1px solid #424242
  - Focus: Border 2px solid #FF69B4
- **Tap behavior:** Abre modal de Date Picker

#### 3. Hora Input
- Similar a Fecha
- Icon: Clock (20px)
- **Tap behavior:** Abre modal de Time Picker

#### 4. Clienta Input
- **Label:** "Clienta *" (16px, Medium, rosa)
- **Search bar:**
  - Height: 56px
  - Background: #2C2C2C
  - Border radius: 28px (pill shape)
  - Icon: Search (20px, left)
  - Placeholder: "🔍 Buscar o crear..." (16px, gris)
  - Button "+": 32px, rosa, right
- **Tap en search:** Abre modal de búsqueda de clientas
- **Tap en "+":** Abre Create Client Modal

**Estado con clienta seleccionada:**
```
┌───────────────────────────────┐
│ [Avatar] Maria Lopez      [✕] │
│ @maria_lopez • Local          │
└───────────────────────────────┘
```

#### 5. Manicurista Dropdown
- **Label:** "Manicurista *" (16px, Medium, rosa)
- **Dropdown:**
  - Height: 56px
  - Background: #2C2C2C (o gris oscuro si deshabilitado)
  - Border radius: 8px
  - Chevron: "▼" (16px, derecha)
- **Tap:** Abre bottom sheet con lista de manicuristas

**Bottom Sheet - Manicuristas:**
```
┌─────────────────────────────────────┐
│  ← Seleccionar Manicurista  [✕]   │
├─────────────────────────────────────┤
│                                     │
│  ┌───────────────────────────────┐ │
│  │ [Avatar] Carolina             │ │
│  │ 80% comisión           [✓]    │ │
│  └───────────────────────────────┘ │
│                                     │
│  ┌───────────────────────────────┐ │
│  │ [Avatar] Monse                │ │
│  │ 40% comisión                  │ │
│  └───────────────────────────────┘ │
│                                     │
│  ┌───────────────────────────────┐ │
│  │ [Avatar] Ana (Inactiva)       │ │
│  │ 40% comisión                  │ │
│  └───────────────────────────────┘ │
│                                     │
└─────────────────────────────────────┘
```

#### 6. Servicio Dropdown
- Similar a Manicurista
- **Tap:** Abre bottom sheet con categorías y servicios

**Bottom Sheet - Servicios:**
```
┌─────────────────────────────────────┐
│  ← Seleccionar Servicio      [✕]  │
├─────────────────────────────────────┤
│  [Todas] [Mani] [Pedi] [Extra]     │  ← Horizontal chips
│                                     │
│  Manicura                           │  ← Category header
│  ┌───────────────────────────────┐ │
│  │ Manicura Gel            $450  │ │
│  │ 60 min                       │ │
│  └───────────────────────────────┘ │
│  ┌───────────────────────────────┐ │
│  │ Manicura Acrílica        $350  │ │
│  │ 50 min                       │ │
│  └───────────────────────────────┘ │
│                                     │
│  Pedicure                           │
│  ┌───────────────────────────────┐ │
│  │ Pedicure Spa            $300  │ │
│  │ 45 min                       │ │
│  └───────────────────────────────┘ │
│                                     │
└─────────────────────────────────────┘
```

#### 7. Servicios Extra (Opcional)
- **Link button:** "[+ Agregar servicio]" (16px, rosa)
- **Tap:** Abre mismo bottom sheet de servicios
- **Comportamiento:** Multi-select, cada agregado aparece como chip

**Estado con servicios extra:**
```
┌───────────────────────────────┐
│ ✖️ Manicura Gel          $450  │  ← Principal
│ ✖️ Diseño Simple         +$100  │  ← Extra
│ [+ Agregar otro]               │
└───────────────────────────────┘
```

#### 8. Resumen Card
- **Background:** #2C2C2C
- **Border radius:** 12px
- **Padding:** 16px
- **Label:** "RESUMEN" (12px, Medium, gris)
- **Items:**
  - Subtotal: 16px, Regular
  - Descuento: 16px, Regular (input field editable)
  - Total: 20px, Bold, blanco
  - Divider
  - Comisión breakdown: 14px, Regular, gris

**Cálculo en tiempo real:**
```
┌───────────────────────────────┐
│ Subtotal:           $550      │  ← Suma de servicios
│ Descuento:          [$0  ]    │  ← Editable
│ Total:              $550      │  ← Bold
│                             │
│ Comisión (Carolina): $440    │  ← 80%
│ Empresa:            $83      │  ← 15%
│ Admin:              $27      │  ← 5%
└───────────────────────────────┘
```

#### 9. Notas (Optional)
- **Label:** "Notas (opcional)" (16px, Medium, gris)
- **Textarea:**
  - Min height: 80px
  - Max height: 120px
  - Background: #2C2C2C
  - Border radius: 8px
  - Padding: 12px
  - Placeholder: "Alergias, preferencias, etc."
  - Font: 16px, Regular

#### 10. CTA Button
- **Texto:** "GUARDAR CITA"
- **Height:** 56px
- **Background:** #FF69B4 (rosa) o gris si deshabilitado
- **Border radius:** 8px
- **Full width**
- **Estado deshabilitado:** Gris (#424242), sin opacidad

---

### SCREEN 2.2: Date Picker Modal

**Propósito:** Seleccionar fecha

**Layout:**
```
┌─────────────────────────────────────┐
│                     [Cancelar] [✓] │
├─────────────────────────────────────┤
│                                     │
│       < Mayo 2026 >                 │
│                                     │
│  ┌──────┬──────┬──────┬──────┬────┐ │
│  │ Dom  │ Lun  │ Mar  │ Mié  │ Jue │ │
│  ├──────┼──────┼──────┼──────┼────┤ │
│  │      │  1   │  2   │  3   │  4  │ │
│  │  5   │  6   │  7   │  8   │  9  │ │
│  │ 10   │ 11   │ 12   │ 13   │ 14  │ │
│  │ 15   │ 16   │ 17   │ 18   │ 19  │ │
│  │ 20   │ 21   │ 22   │ 23   │ 24  │ │
│  │ 25   │ 26   │ 27   │ 28   │ 29  │ │
│  │ 30   │ 31   │      │      │     │ │
│  └──────┴──────┴──────┴──────┴────┘ │
│                                     │
│  ┌───────────────────────────────┐ │
│  │ HOY                            │ │  ← Button
│  └───────────────────────────────┘ │
│                                     │
└─────────────────────────────────────┘
```

**Elementos UI:**
- **Header:** "Cancelar" (izquierda, gris), "✓" (derecha, rosa)
- **Month selector:** "< Mayo 2026 >" (20px, Medium)
- **Calendar grid:**
  - Days headers: 14px, Medium, gris
  - Date cells: 36x36px, centrado
  - Selected date: Circle rosa (#FF69B4), texto blanco
  - Today: Underline dorado (#FFD700)
  - Disabled dates: Gris claro, no tappable
  - Other month dates: Transparente
- **"HOY" button:** Outline rosa, 40px height

**Acciones:**
- Tap en fecha → Selecciona y cierra modal
- Tap en "✓" → Confirma selección y cierra
- Tap en "Cancelar" → Cierra sin cambios
- Tap en "HOY" → Selecciona hoy y cierra

---

### SCREEN 2.3: Time Picker Modal

**Propósito:** Seleccionar hora

**Layout:**
```
┌─────────────────────────────────────┐
│                     [Cancelar] [✓] │
├─────────────────────────────────────┤
│                                     │
│                                     │
│           ┌───────┐                 │
│           │  10   │   AM            │
│           │  :00  │                 │
│           └───────┘                 │
│                                     │
│                                     │
│                                     │
│  ┌───────────────────────────────┐ │
│  │        Hora actual            │ │  ← Button
│  └───────────────────────────────┘ │
│                                     │
└─────────────────────────────────────┘
```

**Elementos UI:**
- **Scroll wheel:** iOS style o Android style
- **Hours:** 1-12
- **Minutes:** 00, 15, 30, 45 (intervalos de 15 min)
- **AM/PM:** Toggle

**Acciones:**
- Scroll para seleccionar
- Tap en "✓" → Confirma
- Tap en "Cancelar" → Cierra

---

### SCREEN 2.4: Client Search Modal

**Propósito:** Buscar y seleccionar clienta existente

**Layout:**
```
┌─────────────────────────────────────┐
│  ← Seleccionar Clienta        [✕]  │
├─────────────────────────────────────┤
│  ┌───────────────────────────────┐ │
│  │ 🔍 Buscar por nombre o tel   │ │
│  └───────────────────────────────┘ │
│                                     │
│  Clientas frecuentes                │
│  ┌───────────────────────────────┐ │
│  │ [M] Maria Lopez               │ │
│  │ @maria_lopez • Local          │ │
│  └───────────────────────────────┘ │
│  ┌───────────────────────────────┐ │
│  │ [A] Ana Garcia                │ │
│  │ @ana.g • Local                │ │
│  └───────────────────────────────┘ │
│  ┌───────────────────────────────┐ │
│  │ [S] Sofia Smith               │ │
│  │ @sofia • Extranjera           │ │
│  └───────────────────────────────┘ │
│                                     │
│  Todas las clientas                 │
│  [Ver lista completa →]             │
│                                     │
│  ┌───────────────────────────────┐ │
│  │      [+ CREAR NUEVA CLIENTA]  │ │  ← Secondary CTA
│  └───────────────────────────────┘ │
│                                     │
└─────────────────────────────────────┘
```

**Elementos UI:**
- **Search bar:** Sticky top, 48px height
- **Section headers:** "Clientas frecuentes" (14px, Medium, gris)
- **Client cards:**
  - Avatar: Initial o foto, 40px circular
  - Name: 18px, Medium
  - Instagram + Type: 14px, Regular, gris
  - Tap: Selecciona y cierra modal
- **"Crear nueva clienta":** Outline button, 48px height

**Acciones:**
- Tap en search → Filtra resultados mientras escribes
- Tap en client card → Selecciona y cierra
- Tap en "Crear nueva" → Abre Create Client Modal

**Estados:**
- **Empty:** "No hay clientas. Crea la primera."
- **No results:** "No se encontraron clientas. Crea una nueva."
- **Loading:** Skeleton cards

---

### SCREEN 2.5: Create Client Modal (Bottom Sheet)

**Propósito:** Crear clienta rápida sin salir del flujo

**Layout:**
```
┌─────────────────────────────────────┐
│  ← Nueva Clienta              [✕] │
├─────────────────────────────────────┤
│                                     │
│  ┌──────┐                           │
│  │ [📷] │  Nombre *                 │
│  └──────┘                           │
│  ┌───────────────────────────────┐ │
│  │ Maria Lopez                   │ │
│  └───────────────────────────────┘ │
│                                     │
│  Teléfono *                         │
│  ┌───────────────────────────────┐ │
│  │ 555-123-4567                  │ │
│  └───────────────────────────────┘ │
│                                     │
│  Instagram                          │
│  ┌───────────────────────────────┐ │
│  │ @maria_lopez                  │ │
│  └───────────────────────────────┘ │
│                                     │
│  Tipo de clienta *                  │
│  ┌───────────┬───────────┐         │
│  │  Local    │ Extranjera│  ← Segmented control
│  └───────────┴───────────┘         │
│                                     │
│  Notas (opcional)                   │
│  ┌───────────────────────────────┐ │
│  │                             │ │
│  └───────────────────────────────┘ │
│                                     │
│  ┌───────────────────────────────┐ │
│  │     GUARDAR Y SELECCIONAR      │ │
│  └───────────────────────────────┘ │
│                                     │
└─────────────────────────────────────┘
```

**Elementos UI:**
- **Avatar placeholder:** 80px circular, tap para foto
- **Input fields:** 56px height cada uno
- **Segmented control:** 48px height, seleccionado = rosa
- **CTA:** Full width, rosa, "GUARDAR Y SELECCIONAR"

**Acciones:**
- Tap en avatar → Abrir cámara/galería
- Tap en "Guardar y seleccionar" → Guarda, cierra modal, y selecciona en Create Appointment

---

### SCREEN 2.6: Confirmation Modal

**Propósito:** Confirmar creación antes de guardar

**Layout:**
```
┌─────────────────────────────────────┐
│                                     │
│         ┌───────┐                   │
│         │  ✓    │                   │
│         └───────┘                   │
│                                     │
│        ¡Cita Creada!                │
│                                     │
│  La cita ha sido guardada y         │
│  sincronizada con tu calendario.    │
│                                     │
│  ┌───────────────────────────────┐ │
│  │    VER EN CALENDARIO           │ │
│  └───────────────────────────────┘ │
│                                     │
│            [Cerrar]                 │
│                                     │
└─────────────────────────────────────┘
```

**Elementos UI:**
- **Icon:** Checkmark en círculo verde, 64px
- **Título:** "¡Cita Creada!" (24px, Bold)
- **Mensaje:** 16px, Regular, gris
- **CTA primario:** "VER EN CALENDARIO" (rosa, solid)
- **Link secundario:** "Cerrar" (gris, text)

**Acciones:**
- Auto-show después de guardar (2 segundos delay opcional)
- Tap en "Ver en calendario" → Navegar a Calendar Screen
- Tap en "Cerrar" → Volver a Calendar Screen

**Auto-dismiss:** 5 segundos o tap fuera

---

## FLUJO 3: VER DETALLE DE CITA

### Objetivo
Usuario ve todos los detalles de una cita y puede realizar acciones según el estado.

### Pantallas Involucradas
1. Calendar Screen (punto de partida)
2. Appointment Detail Screen

### Trigger
- Usuario tap en una cita en Calendar Screen

---

### SCREEN 3.1: Appointment Detail Screen

**Propósito:** Mostrar detalle completo de una cita

**Layout - Estado CONFIRMADA:**
```
┌─────────────────────────────────────┐
│  ←          Cita #1234       [⋮]   │  ← Header
├─────────────────────────────────────┤
│                                     │
│  ┌───────────────────────────────┐ │
│  │  ● CONFIRMADA                 │ │  ← Status badge
│  └───────────────────────────────┘ │
│                                     │
│  📅 1 de Mayo de 2026               │
│  🕐 10:00 AM - 11:00 AM (60 min)    │
│                                     │
│  ─────────────────────────────────  │
│                                     │
│  Clienta                            │
│  ┌───────────────────────────────┐ │
│  │ [Avatar] Maria Lopez     [→] │ │  ← Tappable
│  │ @maria_lopez • Local          │ │
│  │ 📱 555-123-4567               │ │
│  └───────────────────────────────┘ │
│                                     │
│  Servicios                          │
│  ┌───────────────────────────────┐ │
│  │ Manicura Gel                  │ │
│  │ Carolina • 60 min             │ │
│  │ $450                    [→]  │ │
│  └───────────────────────────────┘ │
│  ┌───────────────────────────────┐ │
│  │ + Diseño Simple               │ │
│  │ Carolina • 30 min             │ │
│  │ $100                          │ │
│  └───────────────────────────────┘ │
│                                     │
│  ─────────────────────────────────  │
│                                     │
│  Resumen financiero                 │
│  ┌───────────────────────────────┐ │
│  │ Subtotal:            $550     │ │
│  │ Descuento:           $0       │ │
│  │ Total:               $550     │ │
│  │                             │ │
│  │ Propina estimada:     $0      │ │
│  │                             │ │
│  │ Comisión (Carolina): $440    │ │
│  │ Empresa:             $83     │ │
│  │ Admin:               $27     │ │
│  └───────────────────────────────┘ │
│                                     │
│  Notas                              │
│  "Prefiere colores rosa y dorado"   │
│                                     │
│  Creada: 30 Abr 2026 por Jorge      │
│  Última edición: hace 2 horas       │
│                                     │
│  ┌───────────────────────────────┐ │
│  │      ✏️ EDITAR               │ │  ← Secondary
│  └───────────────────────────────┘ │
│  ┌───────────────────────────────┐ │
│  │      ✓ COMPLETAR              │ │  ← Primary (Rose)
│  └───────────────────────────────┘ │
│  ┌───────────────────────────────┐ │
│  │      ✕ CANCELAR               │ │  ← Destructive (Red)
│  └───────────────────────────────┘ │
│                                     │
└─────────────────────────────────────┘
```

**Layout - Estado COMPLETADA:**
```
┌─────────────────────────────────────┐
│  ←          Cita #1234       [⋮]   │
├─────────────────────────────────────┤
│                                     │
│  ┌───────────────────────────────┐ │
│  │  ● COMPLETADA                 │ │
│  └───────────────────────────────┘ │
│                                     │
│  [Misma información que CONFIRMADA] │
│                                     │
│  ─────────────────────────────────  │
│                                     │
│  Finalización                       │
│  ┌───────────────────────────────┐ │
│  │ Propina:             $50      │ │
│  │ Método de pago:      Efectivo │ │
│  │ Completada:          1 May    │ │
│  └───────────────────────────────┘ │
│                                     │
│  Foto del trabajo                  │
│  ┌───────┐┌───────┐                │
│  │ [📷] ││ [📷] │  ← Gallery      │
│  └───────┘└───────┘                │
│  [Ver todas las fotos →]           │
│                                     │
│  ─────────────────────────────────  │
│                                     │
│  Pagos a Carolina                   │
│  ┌───────────────────────────────┐ │
│  │ Comisión:           $440      │ │
│  │ Propina:            $50       │ │
│  │ TOTAL RECIBIDO:      $490     │ │  ← Highlighted
│  └───────────────────────────────┘ │
│                                     │
│  ┌───────────────────────────────┐ │
│  │      [Ver en calendario]      │ │
│  └───────────────────────────────┘ │
│                                     │
└─────────────────────────────────────┘
```

**Elementos UI - Detallados:**

#### 1. Status Badge
- **Colors:**
  - Confirmada: Verde #4CAF50
  - Completada: Azul #2196F3
  - Cancelada: Rojo #F44336
  - No-show: Naranja #FF9800
  - Pendiente: Púrpura #9370DB
- **Height:** 32px
- **Border radius:** 16px (pill)
- **Icon:** Circle 8px (left)
- **Text:** 14px, Medium, uppercase

#### 2. Clienta Card
- **Tappable:** Sí → Navega a Client Profile Screen
- **Avatar:** 48px circular (initial o foto)
- **Name:** 18px, Medium
- **Instagram:** 14px, Regular, gris
- **Phone:** 14px, Regular, tap para llamar
- **Arrow:** "→" (16px, right)

#### 3. Servicios Cards
- **Principal:** Background más oscuro (#383838)
- **Extra:** Background normal (#2C2C2C)
- **Duration:** Pequeño, gris
- **Price:** Derecha, bold

#### 4. Action Buttons
**Solo aparece si NO está completada:**
- **"EDITAR"**: Outline gris (secundario)
- **"COMPLETAR"**: Solid rosa (primario)
- **"CANCELAR"**: Outline rojo (destructivo)

**Si está completada:**
- **"VER EN CALENDARIO"**: Solid rosa

#### 5. Menu [⋮] (Top Right)
**Tap → Abre opciones:**
- Duplicar cita
- Ver historial de clienta
- Exportar a PDF
- Eliminar (si admin)

---

## FLUJO 4: COMPLETAR CITA ⭐ CRÍTICO

### Objetivo
Manicurista registra finalización de cita con propina, pago y foto.

### Pantallas Involucradas
1. Appointment Detail Screen (punto de partida)
2. Complete Appointment Screen
3. Success Modal

### Trigger
- Usuario tap en "COMPLETAR" en Appointment Detail Screen

---

### SCREEN 4.1: Complete Appointment Screen

**Propósito:** Registrar finalización de cita

**Layout:**
```
┌─────────────────────────────────────┐
│  ← Completar Cita            [✕]   │
├─────────────────────────────────────┤
│                                     │
│  ┌──────┐                           │
│  │ [M]  │  Maria Lopez              │
│  └──────┘  Manicura Gel             │
│            1 May 2026 • 10:00 AM    │
│                                     │
│  ─────────────────────────────────  │
│                                     │
│  Propina recibida *                 │
│  ┌───────────────────────────────┐ │
│  │           $        0          │ │  ← Keypad shown
│  └───────────────────────────────┘ │
│                                     │
│  Método de pago *                   │
│  ┌──────────┬──────────┬──────────┐│
│  │ Efectivo │ Transf. │ Tarjeta  ││  ← Segmented
│  └──────────┴──────────┴──────────┘│
│                                     │
│  ─────────────────────────────────  │
│                                     │
│  Foto del trabajo                   │
│  ┌───────────────────────────────┐ │
│  │                               │ │
│  │        [📷 Tomar foto]        │ │  ← Square placeholder
│  │                               │ │
│  │           o                   │ │
│  │    [Elegir de galería]        │ │
│  │                               │ │
│  └───────────────────────────────┘ │
│                                     │
│  ─────────────────────────────────  │
│                                     │
│  Resumen final                      │
│  ┌───────────────────────────────┐ │
│  │ Servicio:           $550      │ │
│  │ Propina:            $0        │ │  ← Updates live
│  │                             │ │
│  │ Carolina recibe:              │ │
│  │  • Comisión:         $440     │ │
│  │  • Propina:          $0       │ │
│  │  ──────────────────────────  │ │
│  │  TOTAL:              $440     │ │  ← Large, gold
│  └───────────────────────────────┘ │
│                                     │
│  Notas finales (opcional)           │
│  ┌───────────────────────────────┐ │
│  │                             │ │
│  └───────────────────────────────┘ │
│                                     │
│  ┌───────────────────────────────┐ │
│  │   CONFIRMAR COMPLETADO         │ │  ← Primary CTA
│  └───────────────────────────────┘ │
│                                     │
└─────────────────────────────────────┘
```

**Estado con propina ingresada:**
```
│  ─────────────────────────────────  │
│                                     │
│  Resumen final                      │
│  ┌───────────────────────────────┐ │
│  │ Servicio:           $550      │ │
│  │ Propina:           $100       │ │  ← Updated
│  │                             │ │
│  │ Carolina recibe:              │ │
│  │  • Comisión:         $440     │ │
│  │  • Propina:         $100      │ │  ← Added
│  │  ──────────────────────────  │ │
│  │  TOTAL:              $540     │ │  ← Updated
│  └───────────────────────────────┘ │
```

**Estado con foto tomada:**
```
│  Foto del trabajo                   │
│  ┌───────┐┌───────┐                │
│  │ [Img1]││ [📷] │  ← Show thumbnail  │
│  └───────┘└───────┘                │
│  [Cambiar foto]                    │
```

**Elementos UI - Detallados:**

#### 1. Client Info (Top)
- **Avatar:** 64px
- **Name:** 20px, Bold
- **Service + Date:** 16px, Regular, gris

#### 2. Propina Input
- **Label:** "Propina recibida *" (16px, Medium, rosa)
- **Input:**
  - Height: 80px (para mostrar keypad)
  - Font: 32px, Bold, centrado
  - Prefix: "$" (grande, izquierda)
  - Background: #2C2C2C
  - Border: 2px solid #FF69B4 (focus)
  - Keyboard: Number pad, auto-show

**Quick amount buttons:**
```
┌────────┬────────┬────────┬────────┐
│  $10   │  $20   │  $50   │  $100  │
└────────┴────────┴────────┴────────┘
```

#### 3. Método de Pago
- **Label:** "Método de pago *" (16px, Medium, rosa)
- **Segmented control:**
  - 3 opciones: Efectivo, Transferencia, Tarjeta
  - Height: 48px
  - Selected: Rosa background, texto blanco
  - Unselected: Transparente, borde gris

#### 4. Foto Upload
- **Placeholder:** 200x200px cuadrado
- **Background:** #2C2C2C, borde punteado
- **Icon:** Cámara (48px, gris)
- **Text:** "Tomar foto" (16px, Medium)
- **Secondary action:** "Elegir de galería" (14px, rosa)

**Foto state:**
- Mostrar thumbnail centrado
- Botón "Cambiar" debajo
- Tap para reemplazar

#### 5. Resumen Card
- **Background:** #2C2C2C
- **Border radius:** 12px
- **Padding:** 20px
- **Highlight:** "TOTAL" en dorado (#FFD700), 32px

#### 6. CTA Button
- **Texto:** "CONFIRMAR COMPLETADO"
- **Height:** 56px
- **Background:** #FF69B4
- **Full width**
- **Habilitado:** Cuando propina y método de pago están completos

**Validaciones:**
- Propina: Requerido (puede ser $0)
- Método de pago: Requerido
- Foto: Opcional pero altamente recomendado

---

### SCREEN 4.2: Success Celebration

**Propósito:** Celebrar completado exitoso

**Layout:**
```
┌─────────────────────────────────────┐
│                                     │
│         ╭━━╮                       │
│         ┃💰┃  ← Icon animado        │
│         ╰━━╯                       │
│                                     │
│      ¡Excelente trabajo!            │
│                                     │
│  La cita ha sido completada y       │
│  Carolina recibirá $540             │
│  ($440 + $100 de propina)           │
│                                     │
│  [Confetti animation]               │
│                                     │
│  ┌───────────────────────────────┐ │
│  │    SIGUIENTE CITA             │ │  ← Si hay más citas hoy
│  └───────────────────────────────┘ │
│                                     │
│            [Volver al calendario]   │
│                                     │
└─────────────────────────────────────┘
```

**Elementos UI:**
- **Icon:** Money bag con checkmark, 96px
- **Título:** "¡Excelente trabajo!" (24px, Bold)
- **Mensaje:** Dinero recibido por manicurista (20px, Medium)
- **Confetti:** Animación de partículas (1-2 segundos)
- **CTA:** "SIGUIENTE CITA" si hay más citas pendientes hoy
- **Secondary:** "Volver al calendario"

**Auto-dismiss:** 3 segundos o tap en cualquier parte

**Transitions:**
- Si hay próxima cita → Navegar a Complete Appointment Screen de esa cita
- Si no → Volver a Calendar Screen

---

## FLUJO 5: EDITAR CITA

### Objetivo
Usuario modifica una cita existente (solo si no está completada).

### Pantallas Involucradas
1. Appointment Detail Screen (punto de partida)
2. Edit Appointment Screen (similar a Create)

### Trigger
- Usuario tap en "EDITAR" en Appointment Detail Screen

---

### SCREEN 5.1: Edit Appointment Screen

**Propósito:** Editar cita existente

**Layout:**
```
┌─────────────────────────────────────┐
│  ← Editar Cita               [✕]   │
├─────────────────────────────────────┤
│                                     │
│  [Mismo formulario que Screen 2.1]  │
│  [Pero con datos pre-fill]          │
│                                     │
│  ┌───────────────────────────────┐ │
│  │     GUARDAR CAMBIOS           │ │  ← CTA text differs
│  └───────────────────────────────┘ │
│                                     │
└─────────────────────────────────────┘
```

**Diferencias con Create:**
- **Título:** "Editar Cita" en lugar de "Nueva Cita"
- **CTA:** "GUARDAR CAMBIOS" en lugar de "GUARDAR CITA"
- **Datos pre-fill:** Todos los campos tienen valores actuales
- **Advertencia:** Si cambia fecha/hora/manicurista, mostrar warning: "Esto actualizará el evento en Calendar"

**Restricciones:**
- No se puede editar si está COMPLETADA
- No se puede cambiar clienta (solo sus datos)
- Se puede cambiar todo lo demás

---

## FLUJO 6: CANCELAR CITA

### Objetivo
Usuario cancela cita con motivo y confirmación.

### Pantallas Involucradas
1. Appointment Detail Screen (punto de partida)
2. Cancel Confirmation Dialog

### Trigger
- Usuario tap en "CANCELAR" en Appointment Detail Screen

---

### SCREEN 6.1: Cancel Confirmation Dialog

**Propósito:** Confirmar cancelación con motivo

**Layout:**
```
┌─────────────────────────────────────┐
│                                     │
│  ┌───────────────────────────────┐ │
│  │  ¿Cancelar esta cita?         │ │
│  │                               │ │
│  │  Esta acción no se puede      │ │
│  │  deshacer.                    │ │
│  │                               │ │
│  │  Motivo de cancelación:        │ │
│  │  ┌─────────────────────────┐  │ │
│  │  │ Clienta canceló       ▼  │  │ │  ← Dropdown
│  │  └─────────────────────────┘  │ │
│  │                               │ │
│  │  ☐ Aplicar cargo por no-show  │ │  ← Checkbox
│  │                               │ │
│  │  [Cancelar]  [Confirmar]      │ │
│  └───────────────────────────────┘ │
│                                     │
└─────────────────────────────────────┘
```

**Elementos UI:**
- **Modal:** Center screen, max width 400px
- **Título:** "¿Cancelar esta cita?" (20px, Bold)
- **Mensaje:** Explicación (16px, Regular)
- **Dropdown:**
  - Clienta canceló
  - Emergencia de manicurista
  - Doble reservación
  - Otro
- **Checkbox:** "Aplicar cargo por no-show" (si se marca, se puede cobrar deposito)
- **Buttons:**
  - "Cancelar" (gris, outline) → Cerrar modal
  - "Confirmar" (rojo, solid) → Cancelar cita

**Acciones:**
- Tap en "Confirmar" →
  1. Actualiza estado a "cancelada"
  2. Elimina evento de Calendar
  3. Si checkbox marcado, registra cargo
  4. Muestra toast "Cita cancelada"
  5. Vuelve a Calendar Screen

---

## FLUJO 7: DASHBOARD FINANCIERO

### Objetivo
Admin ve métricas del mes y reportes.

### Pantallas Involucradas
1. Dashboard Screen (principal)
2. Reports Screen (tabs)
3. Staff Payouts Screen
4. Expenses Screen

### Trigger
- Usuario tap en tab "Dashboard"

---

### SCREEN 7.1: Dashboard Screen

**Propósito:** Vista general de métricas financieras

**Layout:**
```
┌─────────────────────────────────────┐
│  Dashboard       Mayo 2026      [▼]│  ← Month selector
├─────────────────────────────────────┤
│                                     │
│  Resumen del mes                    │
│                                     │
│  ┌──────┐┌──────┐                  │
│  │  24  ││ $12K │  ← Metrics grid  │
│  │ Citas││Ingres│  (2x2)           │
│  └──────┘└──────┘                  │
│  ┌──────┐┌──────┐                  │
│  │ $8.5K││ $2.7K│                  │
│  │Comis ││Admin │                  │
│  └──────┘└──────┘                  │
│                                     │
│  Ingresos vs Comisiones             │
│  ┌───────────────────────────────┐ │
│  │      [Chart placeholder]      │ │  ← Bar or line chart
│  │  $12K │                       │ │
│  │  $10K │ ▆▆▆▆▆                  │ │
│  │  $8K  │ ▆▆▆▆▆▆                 │ │
│  │  $6K  │ ▆▆▆▆▆▆▆                │ │
│  │  $4K  │ ▆▆▆▆▆▆▆▆               │ │
│  │       └─────────────────────  │ │
│  │        E F M A M J             │ │
│  └───────────────────────────────┘ │
│                                     │
│  Próximas citas (hoy)              │
│  ┌───────────────────────────────┐ │
│  │ ● 10:00 Maria Lopez           │ │
│  │   Manicura - Carolina         │ │
│  └───────────────────────────────┘ │
│  ┌───────────────────────────────┐ │
│  │ ● 11:30 Ana Garcia            │ │
│  │   Pedicure - Monse            │ │
│  └───────────────────────────────┘ │
│  [Ver agenda completa →]           │
│                                     │
│  ┌───────────────────────────────┐ │
│  │      VER REPORTES COMPLETOS    │ │  ← CTA
│  └───────────────────────────────┘ │
│                                     │
└─────────────────────────────────────┘
│ [📅] [💰] [👥] [⚙️]                 │  ← Bottom nav (Dashboard selected)
└─────────────────────────────────────┘
```

**Elementos UI - Detallados:**

#### 1. Header con Month Selector
- **Título:** "Dashboard" (20px, Medium)
- **Dropdown:** "Mayo 2026" con chevron "▼"
  - Tap → Abre mes/año picker modal
  - Default: Mes actual

#### 2. Metrics Grid (2x2)
- **Card size:** 50% width, 100px height
- **Background:** #2C2C2C
- **Border radius:** 12px
- **Padding:** 16px
- **Value:** 32px, Bold, blanco
- **Label:** 14px, Regular, gris
- **Trend indicator:** ↑↓ + small percentage (vs mes anterior)

**Metrics:**
1. Citas totales: 24
2. Ingresos brutos: $12,450
3. Comisiones pagadas: $8,537
4. Pago admin: $2,737

#### 3. Chart
- **Type:** Bar chart o Line chart
- **X-axis:** Meses (Ene, Feb, Mar, Abr, May, Jun)
- **Y-axis:** Dinero ($0K - $15K)
- **Series:**
  - Ingresos (verde)
  - Comisiones (rosa)
- **Librería recomendada:** Victory Charts o react-native-chart-kit

#### 4. Próximas Citas (Compact)
- **Section header:** "Próximas citas (hoy)"
- **Cards:** Compact version (60px height)
- **"Ver agenda completa"** → Navega a Calendar Screen

#### 5. CTA Button
- **Texto:** "VER REPORTES COMPLETOS"
- Full width, rosa outline
- Tap → Navega a Reports Screen

---

### SCREEN 7.2: Reports Screen

**Propósito:** Reportes detallados con tabs

**Layout:**
```
┌─────────────────────────────────────┐
│  ← Reportes             Mayo 2026  │
├─────────────────────────────────────┤
│  [Liquidaciones] [Gastos] [Retención]│  ← Tabs
│                                     │
│  ┌───────────────────────────────┐ │
│  │ [Avatar] Carolina             │ │
│  │ Sueldo:             $0        │ │
│  │ Comisiones:         $8,800    │ │
│  │ Propinas:           $1,200    │ │
│  │ ─────────────────────────────│ │
│  │ TOTAL A PAGAR:      $10,000   │ │  ← Large, gold
│  │ 12 citas completadas          │ │
│  │           [Pagar]      [→]   │ │
│  └───────────────────────────────┘ │
│                                     │
│  ┌───────────────────────────────┐ │
│  │ [Avatar] Monse                │ │
│  │ Sueldo:             $4,800    │ │
│  │ Comisiones:         $2,200    │ │
│  │ Propinas:           $600      │ │
│  │ ─────────────────────────────│ │
│  │ TOTAL A PAGAR:      $7,600    │ │
│  │ 6 citas completadas           │ │
│  │           [Pagar]      [→]   │ │
│  └───────────────────────────────┘ │
│                                     │
│  Total del mes: $17,600             │
│                                     │
└─────────────────────────────────────┘
```

**Tabs:**
1. **Liquidaciones** (Staff payouts)
2. **Gastos** (Expenses)
3. **Retención** (Client retention)

**Staff Payout Card:**
- **Avatar:** 48px circular
- **Name:** 20px, Medium
- **Breakdown:**
  - Sueldo fijo (si aplica)
  - Comisiones
  - Propinas
- **TOTAL:** Large, gold (#FFD700), 32px
- **Info:** "# citas completadas" (14px, gris)
- **Actions:**
  - "[Pagar]" (outline rosa)
  - "[→]" (arrow para ver detalle)

---

### SCREEN 7.3: Staff Payout Detail Screen

**Propósito:** Desglose de liquidación de una manicurista

**Layout:**
```
┌─────────────────────────────────────┐
│  ← Liquidación de Carolina    [⋮]   │
├─────────────────────────────────────┤
│                                     │
│  ┌──────┐                           │
│  │ [C]  │  Carolina                 │
│  └──────┘  Mayo 2026                │
│                                     │
│  ─────────────────────────────────  │
│                                     │
│  Resumen de pagos                   │
│  ┌───────────────────────────────┐ │
│  │ Sueldo fijo:        $0        │ │
│  │ Comisiones (80%):   $8,800    │ │
│  │ Propinas (100%):    $1,200    │ │
│  │ ─────────────────────────────│ │
│  │ TOTAL A PAGAR:       $10,000   │ │
│  └───────────────────────────────┘ │
│                                     │
│  Historial de citas                 │
│  ┌───────────────────────────────┐ │
│  │ 1 May - Maria Lopez           │ │
│  │ Manicura Gel           $700   │ │  ← $550 + $150 propina
│  └───────────────────────────────┘ │
│  ┌───────────────────────────────┐ │
│  │ 30 Abr - Ana Garcia           │ │
│  │ Manicura Acrílica       $530  │ │
│  └───────────────────────────────┘ │
│  ...                               │
│                                     │
│  ┌───────────────────────────────┐ │
│  │      MARCAR COMO PAGADO        │ │  ← Primary CTA
│  └───────────────────────────────┘ │
│                                     │
└─────────────────────────────────────┘
```

---

### SCREEN 7.4: Expenses Screen

**Propósito:** Registro de gastos del negocio

**Layout:**
```
┌─────────────────────────────────────┐
│  ← Gastos                 Mayo 2026│
├─────────────────────────────────────┤
│                                     │
│  Total del mes: $3,450              │
│                                     │
│  ┌──────┐┌──────┐                  │
│  │Productos│ Herram│  ← By category│
│  │$1,500 │ $800  │                 │
│  └──────┘└──────┘                  │
│  ┌──────┐┌──────┐                  │
│  │Market│  Otro │                 │
│  │$750  │ $400  │                 │
│  └──────┘└──────┘                  │
│                                     │
│  Historial de gastos                │
│  ┌───────────────────────────────┐ │
│  │ 15 May - Productos            │ │
│  │ Gel, pinceles, limas          │ │
│  │ $1,200               [✏️][✕] │ │
│  └───────────────────────────────┘ │
│  ┌───────────────────────────────┐ │
│  │ 10 May - Renta                │ │
│  │ Renta mayo                    │ │
│  │ $3,000               [✏️][✕] │ │
│  └───────────────────────────────┘ │
│  ...                               │
│                                     │
│                        [+ FAB]       │  ← Add expense
└─────────────────────────────────────┘
```

**FAB:** "+" button, bottom-right, rosa
**Tap:** Abre Create Expense Screen

---

## FLUJO 8: GESTIÓN DE CLIENTES

### Objetivo
Admin ver lista de clientes, crear nuevos, ver perfil.

### Pantallas Involucradas
1. Clients List Screen
2. Client Profile Screen
3. Create/Edit Client Screen

### Trigger
- Usuario tap en tab "Clientes"

---

### SCREEN 8.1: Clients List Screen

**Propósito:** Lista de todas las clientas

**Layout:**
```
┌─────────────────────────────────────┐
│  Clientas          [⋮]              │
├─────────────────────────────────────┤
│  ┌───────────────────────────────┐ │
│  │ 🔍 Buscar clienta...          │ │  ← Search bar, sticky
│  └───────────────────────────────┘ │
│                                     │
│  [Todas] [Local] [Extranjera]       │  ← Filter chips
│                                     │
│  ┌───────────────────────────────┐ │
│  │ [M] Maria Lopez          [→] │ │  ← Client card
│  │ @maria_lopez • Local          │ │
│  │ Última: 1 May 2026            │ │
│  │ 12 visitas • $5,450 gastados  │ │
│  └───────────────────────────────┘ │
│                                     │
│  ┌───────────────────────────────┐ │
│  │ [A] Ana Garcia           [→] │ │
│  │ @ana.g • Local                │ │
│  │ Última: 28 Abr 2026           │ │
│  │ 8 visitas • $2,800 gastados   │ │
│  └───────────────────────────────┘ │
│  ┌───────────────────────────────┐ │
│  │ [S] Sofia Smith           [→] │ │
│  │ @sofia • Extranjera           │ │
│  │ Última: 15 Abr 2026           │ │
│  │ 5 visitas • $1,750 gastados   │ │
│  └───────────────────────────────┘ │
│  ...                               │
│                                     │
│                        [+ FAB]       │
└─────────────────────────────────────┘
│ [📅] [💰] [👥] [⚙️]                 │
└─────────────────────────────────────┘
```

**Elementos UI:**
- **Search bar:** 48px, rounded, sticky top
- **Filter chips:** Horizontal scroll, "Todas" "Local" "Extranjera"
- **Client cards:**
  - Avatar: Initial o foto, 48px circular
  - Name: 18px, Medium
  - Instagram + Type: 14px, Regular, gris
  - Última visita: 12px, Regular, gris
  - Estadísticas: 14px, Medium
  - Swipe left → Delete (con confirmación)
  - Tap → Client Profile Screen

**Sorting:** Por última visita (más reciente primero)

**Empty state:**
```
┌─────────────────────────────────────┐
│                                     │
│         [Illustration]              │
│                                     │
│      No hay clientas aún            │
│                                     │
│  Crea tu primera clienta para       │
│  empezar a gestionar citas.         │
│                                     │
│  ┌───────────────────────────────┐ │
│  │      + CREAR CLIENTA          │ │
│  └───────────────────────────────┘ │
│                                     │
└─────────────────────────────────────┘
```

---

### SCREEN 8.2: Client Profile Screen

**Propósito:** Ver perfil completo de clienta

**Layout:**
```
┌─────────────────────────────────────┐
│  ←      Maria Lopez          [✏️]  │  ← Edit button
├─────────────────────────────────────┤
│                                     │
│  ┌────────┐                          │
│  │ [Photo]│  Maria Lopez             │
│  │  80px  │  @maria_lopez            │
│  └────────┘                           │
│                                     │
│  ┌───────────────────────────────┐ │
│  │ 📱 555-123-4567               │ │  ← Tappable (call)
│  │ 🏷️ Local                      │ │
│  │ 🎂 15 de Marzo                │ │  ← Birthday
│  │ 🔍 Instagram                  │ │  ← How found
│  └───────────────────────────────┘ │
│                                     │
│  Notas / Alergias                   │
│  ┌───────────────────────────────┐ │
│  │ Prefiere colores rosa y       │ │
│  │ dorado. Alergia a acrilico.   │ │
│  └───────────────────────────────┘ │
│                                     │
│  ─────────────────────────────────  │
│                                     │
│  Estadísticas                       │
│  ┌──────┐┌──────┐┌──────┐          │
│  │  12  ││ $5.4K││  2m  │          │  ← 3-column grid
│  │Visitas││ Gastó││Última│          │
│  └──────┘└──────┘└──────┘          │
│                                     │
│  ─────────────────────────────────  │
│                                     │
│  Historial de Visitas               │
│  [Ver todas las visitas →]           │
│                                     │
│  ┌───────────────────────────────┐ │
│  │ 1 May 2026                    │ │
│  │ Manicura Gel - Carolina       │ │
│  │ $450                    [→]   │ │  ← Tap para cita detail
│  │ [Photo thumbnail]              │ │
│  └───────────────────────────────┘ │
│  ┌───────────────────────────────┐ │
│  │ 15 Abr 2026                   │ │
│  │ Pedicure Spa - Monse          │ │
│  │ $300                     [→]  │ │
│  │ [Photo thumbnail]              │ │
│  └───────────────────────────────┘ │
│  ...                               │
│                                     │
│  ─────────────────────────────────  │
│                                     │
│  Portafolio de trabajos             │
│  ┌──────┬──────┬──────┬──────┐     │
│  │ [Img1]│ [Img2]│ [Img3]│[Img4]│     │  ← Photo grid
│  └──────┴──────┴──────┴──────┘     │
│  [Ver galería completa →]           │
│                                     │
│  ┌───────────────────────────────┐ │
│  │      + NUEVA CITA             │ │  ← Primary CTA
│  └───────────────────────────────┘ │
│                                     │
└─────────────────────────────────────┘
```

**Elementos UI:**
- **Avatar:** 80px circular, tap para cambiar foto
- **Info card:** Íconos + datos
- **Stats grid:** 3 columnas, números grandes
- **Visit cards:** Reverse chronological (más reciente primero)
- **Photo grid:** 2 columnas, 4 fotos mostradas

**Actions:**
- Tap en teléfono → Llamar
- Tap en "✏️ Editar" → Edit Client Screen
- Tap en "+ NUEVA CITA" → Create Appointment (pre-fill con esta clienta)

---

## FLUJO 9: CALENDARIO & AGENDA

### Objetivo
Ver calendario con citas y navegación.

### Pantallas Involucradas
1. Calendar Screen (vistas month/week/day)

### Trigger
- Usuario tap en tab "Agenda" (default home)

---

### SCREEN 9.1: Calendar Screen (Month View)

**Propósito:** Vista mensual del calendario

**Layout:**
```
┌─────────────────────────────────────┐
│           Mayo 2026          [▼]   │  ← Month selector
├─────────────────────────────────────┤
│  [Mes] [Semana] [Día]               │  ← View toggle
│                                     │
│  ┌──┬──┬──┬──┬──┬──┬──┐            │
│  │ D│ L│ M│ M│ J│ V│ S│            │  ← Calendar grid
│  ├──┼──┼──┼──┼──┼──┼──┤            │
│  │  │  │  │  │  │ 1│ 2│            │
│  │ 3│ 4│ 5│ 6│ 7│ 8│ 9│            │
│  │10│11│12│13│14│15│16│            │
│  │17│18│19│20│21│22│23│            │
│  │24│25│26│27│28│29│30│            │
│  │31│  │  │  │  │  │  │            │
│  └──┴──┴──┴──┴──┴──┴──┘            │
│                                     │
│  Hoy, 1 de Mayo                     │  ← Section header
│                                     │
│  ┌───────────────────────────────┐ │
│  │ ● 10:00 Maria Lopez           │ │  ← Appointment card
│  │   Manicura - Carolina         │ │
│  │   $450                    [→] │ │
│  └───────────────────────────────┘ │
│                                     │
│  ┌───────────────────────────────┐ │
│  │ ● 11:30 Ana Garcia            │ │
│  │   Pedicure - Monse            │ │
│  │   $350                    [→] │ │
│  └───────────────────────────────┘ │
│  ...                               │
│                                     │
│                        [+ FAB]       │
└─────────────────────────────────────┘
│ [📅] [💰] [👥] [⚙️]                 │
└─────────────────────────────────────┘
```

**Calendar Grid:**
- **Selected date:** Circle rosa (#FF69B4)
- **Today:** Underline dorado (#FFD700)
- **Date with appointments:** Small dot (3px) below date
  - Green dot = All confirmed
  - Red dot = Any cancelled/no-show
  - Mixed = Multiple colored dots
- **Other month dates:** Gris claro

**Appointment Cards:**
- **Status indicator:** "●" (8px bullet)
  - Green = Confirmada
  - Blue = Completada
  - Red = Cancelada
  - Orange = No-show
- **Time:** 14px, Medium
- **Client:** 18px, Medium
- **Service + Technician:** 14px, Regular, gris
- **Price:** 16px, Medium, derecha
- **Tap:** → Appointment Detail Screen

**FAB:** Floating Action Button "+" (bottom-right)

---

### SCREEN 9.2: Calendar Screen (Week View)

**Propósito:** Vista semanal con timeline

**Layout:**
```
┌─────────────────────────────────────┐
│  < Semana 20, 2026        >        │
├─────────────────────────────────────┤
│  Lun 27 Mar | Mar 28 | Mié 29 ...  │  ← Horizontal scroll days
│                                     │
│  ┌───────────────────────────────┐ │
│  │ 10:00                         │ │
│  │ ┌─────────────────────────┐  │ │
│  │ │ Maria Lopez             │  │ │  ← Appointment block
│  │ │ Manicura Gel - Carolina │  │ │
│  │ │ 60 min                   │  │ │
│  │ └─────────────────────────┘  │ │
│  │ 11:00                         │ │
│  │ ┌─────────────────────────┐  │ │
│  │ │ Ana Garcia              │  │ │
│  │ │ Pedicure - Monse         │  │ │
│  │ │ 45 min                   │  │ │
│  │ └─────────────────────────┘  │ │
│  │ 12:00                        │ │
│  │                              │ │
│  └───────────────────────────────┘ │
│                                     │
│  ← Scroll vertical para más horas → │
│                                     │
└─────────────────────────────────────┘
```

**Week view:**
- **Days:** Horizontal scrollable (7 days)
- **Hours:** Vertical scroll (8 AM - 8 PM)
- **Appointment blocks:** Coloreados según estado
  - Width: 100%
  - Height: Proporcional a duración
  - Rounded corners

---

### SCREEN 9.3: Calendar Screen (Day View)

**Propósito:** Vista diaria detallada

**Layout:**
```
┌─────────────────────────────────────┐
│  < 1 de Mayo de 2026        >      │
├─────────────────────────────────────┤
│                                     │
│  ┌───────────────────────────────┐ │
│  │ 10:00 - 11:00                │ │
│  │ ┌─────────────────────────┐  │ │
│  │ │ Maria Lopez             │  │ │
│  │ │ Manicura Gel - Carolina │  │ │
│  │ │ ● Confirmada             │  │ │
│  │ │ $450                    [→]│  │ │
│  │ └─────────────────────────┘  │ │
│  │                               │ │
│  │ 11:00 - 11:45                │ │
│  │ ┌─────────────────────────┐  │ │
│  │ │ Ana Garcia              │  │ │
│  │ │ Pedicure - Monse         │  │ │
│  │ │ ● Confirmada             │  │ │
│  │ │ $350                    [→]│  │ │
│  │ └─────────────────────────┘  │ │
│  │                               │ │
│  │ 12:00 - 12:30                │ │
│  │ ┌─────────────────────────┐  │ │
│  │ │ DISPONIBLE              │  │ │  ← Empty slot
│  │ │ [+ Crear cita]          │  │ │
│  │ └─────────────────────────┘  │ │
│  │                               │ │
│  │ 12:30 - 13:00                │ │
│  │ ...                           │ │
│  └───────────────────────────────┘ │
│                                     │
└─────────────────────────────────────┘
```

**Day view:**
- **Full timeline:** 8 AM - 8 PM (configurable)
- **Appointment blocks:** Full width, coloreados
- **Empty slots:** Gris claro, "[+ Crear cita]" button

---

## FLUJO 10: CONFIGURACIÓN & SETTINGS

### Objetivo
Admin configura servicios, manicuristas, y settings.

### Pantallas Involucradas
1. Settings Screen (main)
2. Services List Screen
3. Staff List Screen
4. Service/Staff Form Screens

### Trigger
- Usuario tap en tab "Configuración"

---

### SCREEN 10.1: Settings Screen

**Propósito:** Configuración general de la app

**Layout:**
```
┌─────────────────────────────────────┐
│  Configuración                      │
├─────────────────────────────────────┤
│                                     │
│  Jorge Chavez                       │  ← User info
│  jgchavezpanduro@gmail.com          │
│  [Admin]                           │
│                                     │
│  ─────────────────────────────────  │
│                                     │
│  Catálogos                          │
│  ┌───────────────────────────────┐ │
│  │ Servicios                [→] │ │  → Services List
│  └───────────────────────────────┘ │
│  ┌───────────────────────────────┐ │
│  │ Manicuristas             [→] │ │  → Staff List
│  └───────────────────────────────┘ │
│                                     │
│  ─────────────────────────────────  │
│                                     │
│  Ajustes                            │
│  ┌───────────────────────────────┐ │
│  │ Modo oscuro               [ON]│ │  ← Toggle
│  └───────────────────────────────┘ │
│  ┌───────────────────────────────┐ │
│  │ Notificaciones            [ON]│ │
│  └───────────────────────────────┘ │
│  ┌───────────────────────────────┐ │
│  │ Idioma                   [ES] │ │
│  └───────────────────────────────┘ │
│                                     │
│  ─────────────────────────────────  │
│                                     │
│  Sync                               │
│  ┌───────────────────────────────┐ │
│  │ Última sync: Hace 5 min       │ │
│  │ [Sincronizar ahora]            │ │
│  └───────────────────────────────┘ │
│                                     │
│  ─────────────────────────────────  │
│                                     │
│  Ayuda                              │
│  ┌───────────────────────────────┐ │
│  │ Tutorial de la app         [→] │ │
│  └───────────────────────────────┘ │
│  ┌───────────────────────────────┐ │
│  │ Contactar soporte           [→] │ │
│  └───────────────────────────────┘ │
│  ┌───────────────────────────────┐ │
│  │ Términos y privacidad        [→] │ │
│  └───────────────────────────────┘ │
│                                     │
│  ─────────────────────────────────  │
│                                     │
│  Versión 1.0.0                      │
│                                     │
│  ┌───────────────────────────────┐ │
│  │        CERRAR SESIÓN           │ │  ← Destructive
│  └───────────────────────────────┘ │
│                                     │
└─────────────────────────────────────┘
```

---

## 🎨 GLOSARIO VISUAL

### Colores de Estado
- **Confirmada:** 🟢 Verde #4CAF50
- **Completada:** 🔵 Azul #2196F3
- **Cancelada:** 🔴 Rojo #F44336
- **No-show:** 🟠 Naranja #FF9800
- **Pendiente:** 🟣 Púrpura #9370DB

### Tipos de Clienta
- **Local:** 🟢 Verde #4CAF50
- **Extranjera:** 🔵 Azul #2196F3

### Iconos Principales
- 📅 Calendario
- 🕐 Reloj (hora)
- 👤 Clienta
- 💅 Manicurista
- 💰 Finanzas
- 📷 Cámara
- ✏️ Editar
- ✓ Completar/Confirmar
- ✕ Cancelar/Eliminar
- ➕ Añadir/Crear
- → Navegar/Ver detalle
- ⋮ Más opciones
- 🔔 Notificaciones
- ⚙️ Configuración

---

## 📏 ESPECIFICACIONES TÉCNICAS

### Dimensión de Componentes
- **Buttons:** 56px height (primary), 48px (secondary)
- **Inputs:** 56px height
- **Cards:** Padding 16px, Border radius 8-12px
- **Touch targets:** Minimum 44x44px (iOS), 48x48px (Android)
- **FAB:** 56x56px

### Espaciado
- **XS:** 4px
- **SM:** 8px
- **MD:** 16px
- **LG:** 24px
- **XL:** 32px

### Tipografía
- **Display:** 32px, Bold
- **H1:** 24px, Bold
- **H2:** 20px, Medium
- **H3:** 18px, Medium
- **Body Large:** 16px, Regular
- **Body:** 14px, Regular
- **Caption:** 12px, Regular

### Animaciones
- **Screen transition:** 300ms, slide from right
- **Modal appear:** 250ms, scale up + fade
- **Button press:** 100ms, scale down to 0.95
- **Loading:** Spinner rosa, 20fps

---

## ✅ CHECKLIST PARA STITCH

Antes de generar en Stitch, verifica:

**Para cada pantalla:**
- [ ] Propósito claro
- [ ] Todos los elementos UI listados
- [ ] Acciones definidas
- [ ] Estados (empty, loading, error) considerados
- [ ] Transiciones especificadas
- [ ] Colores exactos (#hex)
- [ ] Tamaños en px
- [ ] Jerarquía visual clara

**Para el flujo completo:**
- [ ] Screens en orden lógico
- [ ] Navegación clara (back, next, dismiss)
- [ ] Validaciones especificadas
- [ ] Edge cases manejados
- [ ] Microinteracciones descritas

---

## 🚀 CÓMO USAR ESTE DOCUMENTO

1. **Elige un flujo** (empieza con Flujo 2: Crear Cita - es el más crítico)
2. **Copia la descripción de la pantalla** a Stitch
3. **Genera el mockup**
4. **Refina basado en las especificaciones**
5. **Repite con la siguiente pantalla**
6. **Conecta las pantallas en un prototipo**

**Recomendación:** Genera primero las 3 pantallas críticas:
1. Create Appointment Screen (Flujo 2)
2. Calendar Screen (Flujo 9)
3. Complete Appointment Screen (Flujo 4)

Luego genera las secundarias.
