# Prompts para Stitch - Listos para Usar
## Copia y pega directamente en Stitch

**📁 Paleta de colores completa:** Ver [COLOR_PALETTE.md](./COLOR_PALETTE.md) para la especificación detallada de todos los colores.

**🎨 Estilo:** Natural, orgánico, tonos tierra (beige, café, dorado)

---

## 🎯 CÓMO USAR ESTE DOCUMENTO

1. Abre Stitch (o tu herramienta de diseño AI)
2. Selecciona el flujo que quieres diseñar
3. Copia el prompt completo (incluyendo la sección de colores)
4. Pégalo en Stitch
5. Genera y refina

---

## 🎨 PALETA DE COLORES BASE (Beige/Café)

**Todos los prompts incluyen esta paleta de colores:**

```css
/* BACKGROUND & CARDS */
Background (main): #E8DDD4 (beige muy claro)
Cards (default): #D4C4B5 (beige medio)
Cards (elevated): #FFFFFF (blanco)
Inputs: #FFFFFF (blanco) with #8B6F5C border when focused

/* PRIMARY COLORS (Coffee/Brown) */
Primary (CTA, Links, Active): #8B6F5C (café medio-tierra)
Primary Hover: #A68B74 (café claro)
Primary Pressed: #5E4A3E (café oscuro)

/* SECONDARY COLORS (Gold/Earth) */
Secondary (Money, Prices, Highlights): #C9A87F (dorado/tierra)
Secondary Hover: #DAB896 (dorado claro)

/* TEXT HIERARCHY */
Headings (H1-H3): #5E4A3E (café oscuro, bold)
Body text: #8B7462 (café medio, regular)
Captions: #B1A093 (beige grisáceo, regular)
Placeholders: #C4B5A5 (beige grisáceo)
Disabled: #D4C4B5 (beige medio)

/* STATUS COLORS (Earth tones) */
Confirmed/Success: #7A9B76 (verde tierra)
Completed/Info: #7B8FA3 (azul tierra)
Cancelled/Error: #B86B5B (rojo tierra)
No-show/Warning: #C9A06D (naranja tierra)
Pending: #A68B74 (café medio)

/* CLIENT TYPE BADGES */
Local: #7A9B76 (verde tierra)
Foreign/Extranjera: #7B8FA3 (azul tierra)

/* SPECIAL HIGHLIGHTS */
Today indicator: #C9A87F (dorado underline)
Selected items: #8B6F5C (café background or border)
Focused inputs: #8B6F5C (café border, 2px)
```

**Estilo visual:** Natural beauty aesthetic, light mode with earth tones, minimalist, card-based UI with subtle shadows, rounded corners (8-12px), high contrast for readability (WCAG AA 4.5:1). Sensación: Acogedor, elegante, relajante.

---

## 📱 FLUJO 1: CREATE APPOINTMENT SCREEN (Más crítico)

**🎨 PALETA DE COLORES PARA ESTA PANTALLA:**
```css
Background: #E8DDD4 (beige muy claro)
Form Cards/Inputs: #D4C4B5 (beige medio)
Input Border (Focused): #FF69B4 (pink, 2px)
Labels (Required fields): #8B6F5C (café)
Text (White): #FFFFFF for headings
Text (Gray): #E0E0E0 for body, #BDBDBD for captions
CTA Button: #8B6F5C (café) with #FFFFFF white text
Summary Card: #D4C4B5 background
Price/Total: #C9A87F (dorado/tierra) for final amount
Disabled Button: #D4C4B5 (dark gray)
Placeholder Text: #C4B5A5 (beige grisáceo)
```

**📝 PROMPT PARA STITCH:**

```
Design a mobile app screen for "Create Appointment" in a premium nail salon management app called "Mystic Nails Art".

CONTEXT:
- Target user: Nail technician in Mexico
- Used while working on clients (one-handed operation)
- Light mode theme (beige background with coffee accents)

SCREEN LAYOUT:

HEADER:
- Back button "<" (24px) on left
- Title: "Nueva Cita" (20px, Medium) centered
- "Cancelar" button (16px, pink text) on right

FORM FIELDS (vertical stack, top to bottom):

1. DATE INPUT:
   - Label: "Fecha *" (16px, Medium, pink #FF69B4)
   - Input field: 56px height, dark gray background (#D4C4B5), rounded corners 8px
   - Text: "1 de Mayo de 2026" (16px, Regular)
   - Calendar icon on right (20px)
   - Full width minus 32px margins

2. TIME INPUT:
   - Label: "Hora *" (16px, Medium, pink)
   - Input field: Same style as date
   - Text: "10:00 AM"
   - Clock icon on right (20px)

3. CLIENTA INPUT:
   - Label: "Clienta *" (16px, Medium, pink)
   - Search bar: 56px height, pill shape (rounded 28px), dark gray background
   - Search icon on left (20px)
   - Placeholder: "🔍 Buscar o crear..." (16px, gray)
   - "+" button on right (32px, pink)

4. MANICURISTA DROPDOWN:
   - Label: "Manicurista *" (16px, Medium, pink)
   - Dropdown: 56px height, dark gray background, rounded 8px
   - Placeholder: "Seleccionar clienta primero..." (gray, disabled state)
   - Chevron "▼" on right (16px)

5. SERVICIO DROPDOWN:
   - Label: "Servicio *" (16px, Medium, pink)
   - Same style as manicurista dropdown

6. SERVICIOS EXTRA (optional):
   - Link button: "[+ Agregar servicio]" (16px, pink text)
   - Below service dropdown

SUMMARY CARD (below form fields):
- Background: #D4C4B5 (beige medio)
- Rounded corners: 12px
- Padding: 16px
- Title: "RESUMEN" (12px, Medium, gray)
- Content:
  * Subtotal: $0 (16px, Regular)
  * Descuento: $0 (16px, Regular, editable input)
  * Total: $0 (20px, Bold)
  * Divider line
  * Comisión breakdown (14px, Regular, gray):
    - Comisión (Carolina): $0 (0%)
    - Empresa: $0 (0%)
    - Admin: $0 (0%)

NOTAS FIELD (optional):
- Label: "Notas (opcional)" (16px, Medium, gray)
- Textarea: Min height 80px, max 120px, dark gray background, rounded 8px
- Placeholder: "Alergias, preferencias, etc." (16px)

CTA BUTTON (bottom, fixed):
- Text: "GUARDAR CITA" (16px, Medium, white)
- Height: 56px, full width
- Background: #8B6F5C (café)
- Rounded corners: 8px
- Disabled state: Gray #D4C4B5 (until all required fields are filled)

**COLOR PALETTE (importante - usa estos colores exactos):**
- Background: #E8DDD4 (beige muy claro) - Main screen background
- Cards/Inputs: #D4C4B5 (beige medio) - Card backgrounds
- Primary CTA: #8B6F5C (café) - "Guardar Cita" button
- Labels: #8B6F5C (café) - Field labels with asterisk
- Text headings: #5E4A3E (café oscuro) - Client name, service name
- Text body: #8B7462 (café medio) - Secondary information
- Text captions: #B1A093 (beige grisáceo) - Notes, descriptions
- Border (focused): #FF69B4 (pink, 2px) - Input border when focused
- Border (default): #D4C4B5 (dark gray) - Input border default
- Price/Total: #C9A87F (dorado/tierra) - Summary total amount
- Disabled button: #D4C4B5 (dark gray) - CTA when form incomplete

**DESIGN STYLE:**
- Natural beauty aesthetic (light mode con tonos tierra, minimalist, elegant)
- High contrast for readability (WCAG AA compliance)
- Card-based UI with rounded corners (8px standard, 12px for summary)
- Thumb-friendly zone: All inputs in bottom half of screen
- One-handed operation optimized

**INTERACTIONS:**
- Tap date/time input → Open picker modal
- Tap clienta search → Open search modal
- Tap manicurista/servicio dropdown → Open bottom sheet with options
- Real-time calculation: Update summary card as user selects services
- Tap CTA → Validate and save appointment

DESIGN STYLE:
- Minimalist, clean
- Mobile-first (one-handed use)
- Thumb-friendly zone: All critical actions in bottom half of screen
- High contrast for readability
- Card-based UI with subtle shadows
```

---

## 📅 FLUJO 2: CALENDAR SCREEN

**🎨 PALETA DE COLORES PARA ESTA PANTALLA:**
```css
Background: #E8DDD4 (beige muy claro)
Appointment Cards: #D4C4B5 (beige medio)
Selected Date: #8B6F5C (café) - Circle background
Today Indicator: #C9A87F (dorado/tierra) - Underline
Status Dots: Green #4CAF50, Blue #2196F3, Red #F44336, Orange #FF9800
FAB (Floating Button): #8B6F5C (café)
Tab Bar: #1A1A1A background, #FF69B4 active icon, #BDBDBD inactive
Text: #FFFFFF (white - dates, client names), #E0E0E0 (gray - details)
```

**📝 PROMPT PARA STITCH:**

```
Design a mobile calendar screen for "Mystic Nails Art" premium nail salon app.

CONTEXT:
- Used by nail technicians daily to view their appointments
- Light mode with earth tones
- Must show appointments clearly with color-coded status

SCREEN LAYOUT:

HEADER:
- Month selector: "Mayo 2026" with chevron "▼" (20px, Medium)
- Or arrow buttons "<" ">" for previous/next month

VIEW TOGGLE (below header):
- Horizontal segmented control: [Mes] [Semana] [Día]
- Height: 32px
- Selected: Pink background (#FF69B4), white text
- Unselected: Transparent, gray text

CALENDAR GRID (Month view):
- 7 columns (Dom - Sáb)
- Date cells: 36x36px each, centered
- Header row: Day names (14px, Medium, gray)
- Selected date: Circle background #FF69B4, white text
- Today: Underline #C9A87F (dorado/tierra)
- Dates with appointments: Small dot (3px) below date
  - Green dot = All appointments confirmed
  - Red dot = Any cancelled/no-show
  - Multiple dots = Mixed statuses
- Other month dates: Light gray, not tappable

SECTION HEADER (below calendar):
- Text: "Hoy, 1 de Mayo" (18px, Medium)

APPOINTMENT CARDS (list below section header):

Card style:
- Height: 80px
- Background: #D4C4B5 (beige medio)
- Rounded corners: 8px
- Padding: 12px
- Left border: Status indicator bullet (● 8px)

Card content:
- Status bullet (left):
  * Green #4CAF50 = Confirmada
  * Blue #2196F3 = Completada
  * Red #F44336 = Cancelada
  * Orange #FF9800 = No-show
- Time: "10:00" (14px, Medium)
- Client name: "Maria Lopez" (18px, Medium)
- Service + Technician: "Manicura - Carolina" (14px, Regular, gray)
- Price: "$450" (16px, Medium, right-aligned)
- Arrow "→" (16px, right)

APPOINTMENT CARD EXAMPLE:
┌───────────────────────────────┐
│ ● 10:00 Maria Lopez           │
│   Manicura - Carolina         │
│   $450                    [→] │
└───────────────────────────────┘

EMPTY STATE:
- Illustration: Calendar icon
- Text: "No hay citas para este día"
- CTA: "Crear primera cita" (pink button)

FAB (Floating Action Button):
- Position: Bottom-right corner
- Size: 56x56px
- Icon: "+" (24px, white)
- Background: #8B6F5C (café)
- Rounded corners: 16px
- Shadow: Elevation 4

BOTTOM NAVIGATION:
- 4 tabs: [📅 Agenda] [💰 Dashboard] [👥 Clientes] [⚙️ Configuración]
- Height: 56px
- Background: #1A1A1A
- Selected tab icon: Pink #FF69B4
- Unselected tab icon: Gray #BDBDBD

**COLOR PALETTE (usa estos colores exactos):**
- Background: #E8DDD4 (beige muy claro) - Main calendar background
- Appointment cards: #D4C4B5 (beige medio) - Card background
- Selected date: #8B6F5C (café) - Circle around selected date
- Today underline: #C9A87F (dorado/tierra) - Underline today's date
- Status indicators:
  * Green #4CAF50: Confirmed appointments
  * Blue #2196F3: Completed appointments
  * Red #F44336: Cancelled appointments
  * Orange #FF9800: No-show appointments
- FAB button: #8B6F5C (café) - Floating action button
- Tab bar: #1A1A1A background, #FF69B4 (active tab icon), #BDBDBD (inactive)
- Text hierarchy:
  * #5E4A3E (café oscuro) - Dates, client names (headings)
  * #8B7462 (café medio) - Service, technician names
  * #B1A093 (beige grisáceo) - Day names, captions

**DESIGN STYLE:**
- Clean, minimalist calendar interface
- Color-coded appointment status for quick scanning
- Large touch targets for one-handed use
- High contrast for readability in bright salon environments

**INTERACTIONS:**
- Tap date → Filter appointment list by selected date
- Tap appointment card → Open appointment detail screen
- Tap FAB → Open create appointment screen
- Pull down to refresh
- Swipe left on appointment card → Quick actions (edit, cancel)
```

---

## ✅ FLUJO 3: COMPLETE APPOINTMENT SCREEN (Más crítico)

**🎨 PALETA DE COLORES PARA ESTA PANTALLA:**
```css
Background: #E8DDD4 (beige muy claro)
Cards/Inputs: #D4C4B5 (beige medio)
Primary CTA: #8B6F5C (café) - "Confirmar Completado" button
Input Border (Focused): #FF69B4 (pink, 2px) - Tip input
Labels: #8B6F5C (café) - Required field labels
Text Headings: #5E4A3E (café oscuro) - Client name, service
Text Body: #8B7462 (café medio) - Details
Text Captions: #B1A093 (beige grisáceo) - Labels
Technician Total: #C9A87F (dorado/tierra) - Large, prominent
Success: #7A9B76 (verde tierra) - Celebration, checkmark
Payment Method (Selected): #FF69B4 (pink background)
Payment Method (Unselected): #D4C4B5 (gray border)
```

**📝 PROMPT PARA STITCH:**

```
Design a mobile screen for "Complete Appointment" in a premium nail salon app.

CONTEXT:
- Used by technician after finishing a nail service
- Need to record tip, payment method, and photo quickly
- Should be fast (under 30 seconds)

SCREEN LAYOUT:

HEADER:
- Back button "<" (left)
- Title: "Completar Cita" (20px, Medium)
- Close button "✕" (right)

CLIENT INFO (top section):
- Avatar: 64px circular (initial or photo)
- Client name: "Maria Lopez" (20px, Bold)
- Service: "Manicura Gel" (16px, Regular)
- Date/Time: "1 May 2026 • 10:00 AM" (14px, Regular, gray)

DIVIDER

TIP INPUT (critical, prominent):
- Label: "Propina recibida *" (16px, Medium, pink #FF69B4)
- Input field:
  * Height: 80px (show number keypad)
  * Font: 32px, Bold, centered
  * Prefix: "$" (large, left)
  * Background: #D4C4B5
  * Border: 2px solid #FF69B4 (focused)
  * Placeholder: "0"

QUICK AMOUNT BUTTONS (below input):
- Horizontal row: [$10] [$20] [$50] [$100]
- Height: 40px each
- Outline style, rounded 20px
- Tap to fill amount

PAYMENT METHOD (below tip):
- Label: "Método de pago *" (16px, Medium, pink)
- Segmented control: [Efectivo] [Transferencia] [Tarjeta]
- Height: 48px
- Selected: Pink background #FF69B4, white text
- Unselected: Gray border, gray text

DIVIDER

PHOTO UPLOAD (highly encouraged):
- Label: "Foto del trabajo" (16px, Medium, gray)
- Square placeholder: 200x200px
- Background: #D4C4B5, dashed border
- Icon: Camera (48px, gray)
- Text: "Tomar foto" (16px, Medium)
- Secondary text: "o elegir de galería" (14px, Regular, pink)
- Tap to open camera/gallery

DIVIDER

SUMMARY CARD (bottom section, important):
- Background: #D4C4B5
- Rounded corners: 12px
- Padding: 20px
- Title: "Resumen final" (16px, Medium)
- Content:
  * Servicio: $550 (16px, Regular)
  * Propina: $0 (16px, Regular) - updates live as user enters tip
  * Divider
  * "Carolina recibe:" (14px, Regular, gray)
  * • Comisión: $440 (16px, Regular)
  * • Propina: $0 (16px, Regular) - appears when tip entered
  * Double divider
  * TOTAL: $440 (32px, Bold, gold #C9A87F)

OPTIONAL NOTES:
- Label: "Notas finales (opcional)" (16px, Medium, gray)
- Textarea: Min height 60px, dark gray background

CTA BUTTON (fixed at bottom):
- Text: "CONFIRMAR COMPLETADO" (16px, Medium, white)
- Height: 56px, full width
- Background: #8B6F5C (café)
- Disabled until tip and payment method are selected

SUCCESS STATE (after submission):
- Checkmark icon in green circle (64px)
- Title: "¡Excelente trabajo!" (24px, Bold)
- Message: "La cita ha sido completada y Carolina recibirá $540"
- Confetti animation (1-2 seconds)
- Auto-dismiss after 3 seconds or tap anywhere

**COLOR PALETTE (importante - technician total must be prominent):**
- Background: #E8DDD4 (beige muy claro) - Main screen
- Cards: #D4C4B5 (beige medio) - Info cards, summary
- Primary CTA: #8B6F5C (café) - "CONFIRMAR COMPLETADO" button
- Tip input (focused): #FF69B4 (pink, 2px border) - Prominent
- Payment method (selected): #FF69B4 (pink background, white text)
- Payment method (unselected): #D4C4B5 (gray border, gray text)
- Technician total: #C9A87F (dorado/tierra) - MUST BE LARGE AND PROMINENT (32px font)
- Service total: #8B7462 (café medio) - Smaller than technician total
- Text headings: #5E4A3E (café oscuro) - Client name, service name
- Text body: #8B7462 (café medio) - Details, dates
- Text captions: #B1A093 (beige grisáceo) - Labels like "Carolina recibe:"
- Success celebration: #7A9B76 (verde tierra) - Checkmark, confetti

**VISUAL HIERARCHY (crucial):**
1. MOST PROMINENT: Technician's total (#C9A87F, 32px Bold, gold) - This is what they care about most
2. SECONDARY: Tip input field (#FF69B4 border, 32px centered)
3. TERTIARY: CTA button (#FF69B4 pink, full width, 56px height)
4. QUATERNARY: Payment method selector, photo upload

**DESIGN STYLE:**
- Fast, focused interface for busy technicians
- Celebratory tone (confetti, success animation)
- Large, thumb-friendly touch targets
- Real-time calculation updates visible immediately

**INTERACTIONS:**
- Auto-focus tip input on screen load
- Show number keypad automatically
- Real-time calculation of total as tip changes
- Tap photo placeholder → Open camera
- Tap quick amount buttons → Fill tip input
- Tap confirm → Show success, auto-dismiss
```

---

## 📋 FLUJO 4: APPOINTMENT DETAIL SCREEN

**🎨 PALETA DE COLORES PARA ESTA PANTALLA:**
```css
Background: #E8DDD4 (beige muy claro)
Default Cards: #D4C4B5 (beige medio)
Elevated Cards: #FFFFFF (blanco) - Main service card
Status Badges: Green #4CAF50 (Confirmed), Blue #2196F3 (Completed)
Text: #FFFFFF (white - headings), #E0E0E0 (light gray - body), #BDBDBD (gray - captions)
Prices: #E0E0E0 (service), #C9A87F (gold - commission totals)
Buttons: Primary #8B6F5C (café), Destructive #B86B5B (rojo tierra), Secondary outline
```

**📝 PROMPT PARA STITCH:**

```
Design a mobile screen for "Appointment Detail" in a premium nail salon app.

CONTEXT:
- Shows all information about an appointment
- Different layouts based on appointment status (Confirmed vs Completed)
- User can edit, complete, or cancel from here

SCREEN LAYOUT - CONFIRMED STATUS:

HEADER:
- Back button "<" (left)
- Appointment ID: "Cita #1234" (16px, Medium, center)
- Menu button "⋮" (right)

STATUS BADGE (top, prominent):
- Background: Green #4CAF50 (rounded pill, 32px height)
- Icon: "●" (8px circle, left)
- Text: "CONFIRMADA" (14px, Medium, uppercase, white)

DATE/TIME SECTION:
- Icon + Text: "📅 1 de Mayo de 2026" (16px, Regular)
- Icon + Text: "🕐 10:00 AM - 11:00 AM (60 min)" (16px, Regular)

DIVIDER

CLIENTA CARD (tappable):
- Avatar: 48px circular (initial or photo)
- Name: "Maria Lopez" (18px, Medium)
- Instagram + Type: "@maria_lopez • Local" (14px, Regular, gray)
- Phone: "📱 555-123-4567" (14px, Regular) - tap to call
- Arrow "→" (16px, right)
- Background: #D4C4B5
- Rounded corners: 8px
- Padding: 12px
- Full width

SERVICIOS SECTION:

Main service card:
- Background: #383838 (darker than extra services)
- Name: "Manicura Gel" (18px, Medium)
- Technician + Duration: "Carolina • 60 min" (14px, Regular, gray)
- Price: "$450" (18px, Medium, right) or arrow "→"
- Padding: 12px, rounded 8px

Extra services (if any):
- Background: #D4C4B5
- "+ Diseño Simple" (16px, Regular)
- "Carolina • 30 min" (14px, Regular, gray)
- "$100" (16px, Regular, right)

DIVIDER

RESUMEN FINANCIERO:
- Section title: "Resumen financiero" (16px, Medium)
- Card: Background #D4C4B5, rounded 12px, padding 16px
- Content:
  * Subtotal: $550 (16px, Regular)
  * Descuento: $0 (16px, Regular)
  * Total: $550 (20px, Bold)
  * Divider
  * Propina estimada: $0 (14px, Regular, gray)
  * Divider
  * Comisión breakdown:
    - Comisión (Carolina): $440 (14px, Regular)
    - Empresa: $83 (14px, Regular)
    - Admin: $27 (14px, Regular)

NOTAS SECTION:
- Label: "Notas" (16px, Medium, gray)
- Text: "Prefiere colores rosa y dorado" (14px, Regular)
- Quote marks or italic

METADATA:
- "Creada: 30 Abr 2026 por Jorge" (12px, Regular, gray)
- "Última edición: hace 2 horas" (12px, Regular, gray)

ACTION BUTTONS (bottom, fixed):

If CONFIRMED status:
1. EDITAR (secondary) - Outline gray, 56px height
2. COMPLETAR (primary) - Solid pink #FF69B4, 56px height
3. CANCELAR (destructive) - Outline red #F44336, 56px height

If COMPLETED status:
- Single button: "VER EN CALENDARIO" (solid pink)

SCREEN LAYOUT - COMPLETED STATUS:

(Same header, date/time, client card, services sections)

ADDITIONAL SECTIONS FOR COMPLETED:

FINALIZACIÓN SECTION:
- Label: "Finalización" (16px, Medium, gray)
- Card: Background #D4C4B5, rounded 8px
  * Propina: "$50" (16px, Regular)
  * Método de pago: "Efectivo" (16px, Regular)
  * Completada: "1 May" (14px, Regular, gray)

FOTO DEL TRABAJO:
- Label: "Foto del trabajo" (16px, Medium, gray)
- Photo grid: 2 columns, 2-4 thumbnails (80x80px each)
- Tap thumbnail → Open full-screen lightbox
- "Ver todas las fotos →" link

PAGOS A MANICURISTA:
- Label: "Pagos a Carolina" (16px, Medium, gray)
- Card: Background #383838, rounded 12px, padding 16px
  * Comisión: $440 (16px, Regular)
  * Propina: $50 (16px, Regular)
  * Double divider
  * TOTAL RECIBIDO: $490 (24px, Bold, gold #C9A87F)

**COLOR PALETTE:**
- Background: #E8DDD4 (beige muy claro) - Main screen
- Default cards: #D4C4B5 (beige medio) - Client card, extra services
- Elevated cards: #FFFFFF (blanco) - Main service card (more prominent)
- Status badge (Confirmed): #7A9B76 (verde tierra) - Pill background
- Status badge (Completed): #7B8FA3 (azul tierra) - Pill background
- Text headings: #5E4A3E (café oscuro) - Client name, service name
- Text body: #8B7462 (café medio) - Details
- Text captions: #B1A093 (beige grisáceo) - Secondary info
- Prices (service): #8B7462 (café medio) - Regular amounts
- Commission totals: #8B7462 (café medio) - Breakdown amounts
- Admin/Technician totals: #C9A87F (dorado/tierra) - Only if very prominent
- Action buttons:
  * COMPLETAR: #FF69B4 (pink, solid)
  * EDITAR: Outline with #E0E0E0 (light gray border)
  * CANCELAR: Outline with #F44336 (red border)
  * VER EN CALENDARIO: #FF69B4 (pink, solid)

**INTERACTIONS:**
- Tap client card → Open client profile screen
- Tap service → Open service detail
- Tap phone number → Initiate call
- Tap menu "⋮" → Open options (duplicate, export, delete)
- Tap EDITAR → Open edit appointment screen
- Tap COMPLETAR → Open complete appointment screen
- Tap CANCELAR → Open cancel confirmation dialog
- Tap photo thumbnail → Open lightbox viewer
```

---

## 💰 FLUJO 5: DASHBOARD SCREEN (Owner view)

**🎨 PALETA DE COLORES PARA ESTA PANTALLA:**
```css
Background: #E8DDD4 (beige muy claro)
Metric Cards: #D4C4B5 (beige medio)
Chart: Green #4CAF50 (revenue bars), Pink #FF69B4 (commissions bars)
Trend Indicators: Green #4CAF50 (up arrow), Red #F44336 (down arrow)
Text (Metrics): #5E4A3E (café oscuro) - Large numbers
Text (Labels): #B1A093 (beige grisáceo) - Small labels
Text (Headings): #5E4A3E (café oscuro) - Section titles
Appointment Cards: #D4C4B5 (beige medio) with status bullets
```

**📝 PROMPT PARA STITCH:**

```
Design a mobile dashboard screen for "Mystic Nails Art" premium nail salon app.

CONTEXT:
- Used by salon owner to view monthly financial metrics
- Light mode with earth tones
- Should give quick overview in under 10 seconds

SCREEN LAYOUT:

HEADER:
- Title: "Dashboard" (20px, Medium)
- Month selector dropdown: "Mayo 2026" with chevron "▼"
- Full width header bar: 56px height

METRICS GRID (top section, prominent):
- 2x2 grid (4 cards total)
- Each card: 50% width, 100px height
- Background: #D4C4B5 (beige medio)
- Rounded corners: 12px
- Padding: 16px

Card layout:
- Value: Large number (32px, Bold, white)
- Label: Small text below (14px, Regular, gray)
- Trend indicator: Small arrow ↑↓ + percentage (12px)

METRICS:
1. Citas totales: "24" + "↑ 15% vs mes anterior"
2. Ingresos brutos: "$12,450" + "↑ 8% vs mes anterior"
3. Comisiones pagadas: "$8,537" + "↑ 12% vs mes anterior"
4. Pago admin: "$2,737" + "↑ 10% vs mes anterior"

Trend colors:
- Green ↑ = Positive
- Red ↓ = Negative

CHART SECTION (below metrics):
- Section title: "Ingresos vs Comisiones" (16px, Medium)
- Chart container: Height 200px, background #D4C4B5, rounded 12px
- Chart type: Bar chart or Line chart
- X-axis: Months (Ene, Feb, Mar, Abr, May, Jun)
- Y-axis: Money ($0K - $15K)
- Two series:
  * Ingresos (Green #4CAF50 bars or line)
  * Comisiones (Pink #FF69B4 bars or line)

PRÓXIMAS CITAS SECTION:
- Section title: "Próximas citas (hoy)" (16px, Medium)
- "Ver agenda completa →" link (14px, pink, right-aligned)

Compact appointment cards (60px height each):
- Status bullet (● 8px) - Green
- Time: "10:00" (14px, Medium)
- Client: "Maria Lopez" (16px, Regular)
- Service: "Manicura - Carolina" (12px, gray)
- Arrow "→" (14px, right)

Max 3 cards shown, then link to full agenda

CTA BUTTON (above bottom nav):
- Text: "VER REPORTES COMPLETOS" (16px, Medium, white)
- Height: 56px, full width
- Background: #8B6F5C (café)
- Border radius: 8px
- Outline style (border only, transparent background)

BOTTOM NAVIGATION:
- Same as calendar screen
- Dashboard tab selected (pink icon)

**COLOR PALETTE (data visualization focus):**
- Background: #E8DDD4 (beige muy claro) - Main dashboard
- Metric cards: #D4C4B5 (beige medio) - 2x2 grid cards
- Chart container: #D4C4B5 (beige medio) - Background for chart
- Chart colors:
  * Revenue bars: #7A9B76 (verde tierra) - Gross income
  * Commissions bars: #8B6F5C (café) - Staff payouts
  * X/Y axis: #BDBDBD (gray) - Grid lines, labels
- Trend indicators:
  * Up arrow: #7A9B76 (verde tierra) - Positive growth
  * Down arrow: #B86B5B (rojo tierra) - Negative decline
- Metric values: #5E4A3E (café oscuro) - Large numbers (32px)
- Metric labels: #B1A093 (beige grisáceo) - Small text below numbers
- Section headings: #5E4A3E (café oscuro) - "Dashboard", "Ingresos vs Comisiones"
- Appointment cards: #D4C4B5 (beige medio) with status bullets
- CTA button: #8B6F5C (café) - "VER REPORTES COMPLETOS" (outline style)

**VISUAL HIERARCHY:**
1. Metrics grid (most prominent) - Large white numbers on dark gray cards
2. Chart section (secondary) - Green/pink bars for easy comparison
3. Upcoming appointments (tertiary) - Compact list

**INTERACTIONS:**
- Tap month selector → Open month/year picker modal
- Tap metric card → Drill down to detail (optional)
- Tap appointment card → Open appointment detail
- Tap "Ver agenda completa" → Navigate to calendar screen
- Tap "VER REPORTES COMPLETOS" → Navigate to reports screen
- Pull down to refresh metrics

EMPTY STATE (first month, no data):
- Illustration: Chart or money icon
- Text: "No hay datos este mes"
- CTA: "Crear primera cita" (pink button)
```

---

## 👥 FLUJO 6: CLIENT LIST SCREEN

**🎨 PALETA DE COLORES:**
```css
Background: #E8DDD4 (beige muy claro)
Client Cards: #D4C4B5 (beige medio)
Search Bar: #D4C4B5 (beige medio)
Filter Chips: Selected #FF69B4 (pink bg), Unselected #D4C4B5 (gray border)
Badges: Local #7A9B76 (verde tierra), Foreign #7B8FA3 (azul tierra)
FAB: #8B6F5C (café)
Text: #FFFFFF (names), #E0E0E0 (details), #BDBDBD (captions)
Stats: #8B6F5C (café) - "12 visitas • $5,450 gastados"
```

**📝 PROMPT PARA STITCH:**

```
Design a mobile screen for "Client List" in a premium nail salon app.

CONTEXT:
- Shows all clients in the salon
- Used to view profiles and create appointments
- Search and filter functionality

SCREEN LAYOUT:

HEADER:
- Title: "Clientas" (20px, Medium)
- Menu button "⋮" (right)
- Height: 56px

SEARCH BAR (sticky, below header):
- Height: 48px
- Pill shape (rounded 24px)
- Background: #D4C4B5 (beige medio)
- Search icon: Left (20px, gray)
- Placeholder: "🔍 Buscar clienta..." (16px, gray)
- Full width minus 32px margins
- Sticky at top when scrolling

FILTER CHIPS (below search bar):
- Horizontal scrollable row
- 3 chips: [Todas] [Local] [Extranjera]
- Height: 32px each
- Selected: Pink background #FF69B4, white text
- Unselected: Gray border, gray text
- Rounded 16px

CLIENT CARDS (vertical list, main content):

Card layout:
- Height: Auto (approx 80px)
- Background: #D4C4B5 (beige medio)
- Rounded corners: 8px
- Padding: 12px
- Left avatar + Right content

Card content:
- Avatar: 48px circular (initial letter or photo)
- Name: "Maria Lopez" (18px, Medium)
- Instagram + Type: "@maria_lopez • Local" (14px, Regular, gray)
- Last visit: "Última: 1 May 2026" (12px, Regular, gray)
- Stats: "12 visitas • $5,450 gastados" (14px, Medium, pink)
- Arrow "→" (16px, right)

Client type badge:
- Local: Green #4CAF50
- Extranjera: Blue #2196F3
- Small pill (20px height, rounded 10px)

Card example:
┌───────────────────────────────┐
│ [M] Maria Lopez          [→] │
│ @maria_lopez • Local          │
│ Última: 1 May 2026            │
│ 12 visitas • $5,450 gastados  │
└───────────────────────────────┘

SWIPE ACTIONS (on client cards):
- Swipe left → Delete button (red background)
- Swipe right → Create appointment button (pink background)

EMPTY STATE (no clients):
- Illustration: People or user icon
- Title: "No hay clientas aún" (20px, Medium)
- Message: "Crea tu primera clienta para empezar a gestionar citas" (16px, Regular, gray)
- CTA Button: "+ CREAR CLIENTA" (pink, 56px height)

FAB (Floating Action Button):
- Position: Bottom-right corner
- Size: 56x56px
- Icon: "+" (24px, white)
- Background: #8B6F5C (café)
- Shadow: Elevation 4

BOTTOM NAVIGATION:
- 4 tabs: [📅] [💰] [👥] [⚙️]
- Clientes tab selected (pink icon)

**COLOR PALETTE:**
- Background: #1A1A1A, Cards: #D4C4B5, Search: #D4C4B5
- Badges: Local #4CAF50, Foreign #2196F3
- FAB: #FF69B4, Stats: #FF69B4
- Text: #FFFFFF (names), #E0E0E0 (details), #BDBDBD (captions)

**INTERACTIONS:**
- Tap search bar → Show keyboard, filter list as you type
- Tap filter chip → Filter list by client type
- Tap client card → Open client profile screen
- Swipe left on card → Show delete button (tap to delete with confirmation)
- Swipe right on card → Show "Crear cita" button (tap to create appointment pre-filled)
- Tap FAB → Open create client modal
- Pull down to refresh

SORTING:
- Default: By last visit (most recent first)
- Alternative options in menu: Sort by name, sort by total spent
```

---

## 👤 FLUJO 7: CLIENT PROFILE SCREEN

**🎨 PALETA DE COLORES:**
```css
Background: #E8DDD4 (beige muy claro)
Info/History Cards: #D4C4B5 (beige medio)
Stats Grid: Transparent (no background)
CTA: #8B6F5C (café)
Badge (Local): #7A9B76 (verde tierra)
Text: #FFFFFF (name, stats), #E0E0E0 (details), #BDBDBD (captions)
```

**📝 PROMPT PARA STITCH:**

```
Design a mobile screen for "Client Profile" in a premium nail salon app.

CONTEXT:
- Shows complete information about a client
- Displays visit history and photos
- Quick access to create new appointment

SCREEN LAYOUT:

HEADER:
- Back button "<" (left)
- Spacer (center - no title)
- Edit button "✏️" (right, pink text)

AVATAR SECTION (top, centered):
- Avatar: 80px circular (photo or initial letter)
- Name: "Maria Lopez" (24px, Bold)
- Instagram: "@maria_lopez" (16px, Regular, gray)
- Tap avatar → Change photo (if editing)

INFO CARD (below avatar):
- Background: #D4C4B5 (beige medio)
- Rounded corners: 12px
- Padding: 16px
- Full width

Info items (vertical stack):
- Phone: "📱 555-123-4567" (16px, Regular) - tap to call
- Type: "🏷️ Local" (16px, Regular) - green badge
- Birthday: "🎂 15 de Marzo" (16px, Regular)
- Source: "🔍 Instagram" (16px, Regular, gray)

NOTAS / ALERGIAS SECTION:
- Label: "Notas / Alergias" (16px, Medium, gray)
- Card: Background #D4C4B5, rounded 8px, padding 12px
- Text: "Prefiere colores rosa y dorado. Alergia a acrilico." (14px, Regular)

DIVIDER

STATS GRID (3 columns):
- Background: Transparent
- 3 equal columns (33% width each)

Stat item:
- Value: Large number (28px, Bold, white)
- Label: Small text below (12px, Regular, gray)

Stats:
1. Visitas: "12" + "Visitas"
2. Gastado: "$5.4K" + "Gastado"
3. Última: "2m" + "Última"

DIVIDER

HISTORIAL DE VISITAS SECTION:
- Section header: "Historial de Visitas" (16px, Medium)
- "Ver todas las visitas →" link (14px, pink, right-aligned)

Visit cards (reverse chronological - most recent first):
- Background: #D4C4B5
- Rounded corners: 8px
- Padding: 12px
- Height: Auto (approx 100px)

Visit card content:
- Date: "1 May 2026" (16px, Medium)
- Service: "Manicura Gel - Carolina" (14px, Regular)
- Price: "$450" (16px, Medium, right)
- Arrow "→" (14px, right)
- Photo thumbnail: 60x40px (below text, left-aligned)

Visit card example:
┌───────────────────────────────┐
│ 1 May 2026                    │
│ Manicura Gel - Carolina       │
│ $450                     [→]  │
│ [Photo thumb]                 │
└───────────────────────────────┘

PORTAFOLIO SECTION (if photos exist):
- Section header: "Portafolio de trabajos" (16px, Medium)
- Photo grid: 2 columns, 4 thumbnails (100x100px each)
- "Ver galería completa →" link (14px, pink)

DIVIDER

CTA BUTTON (above bottom nav):
- Text: "+ NUEVA CITA" (16px, Medium, white)
- Height: 56px, full width
- Background: #8B6F5C (café)
- Border radius: 8px

BOTTOM NAVIGATION:
- Same as other screens
- Clientes tab selected

**COLOR PALETTE:**
- Background: #1A1A1A, Cards: #D4C4B5
- CTA: #FF69B4, Badge: #4CAF50
- Text: #FFFFFF (headings), #E0E0E0 (body), #BDBDBD (captions)

**INTERACTIONS:**
- Tap avatar → Open camera/gallery (if edit mode)
- Tap phone number → Initiate call
- Tap info card → Copy info to clipboard
- Tap visit card → Open appointment detail screen
- Tap photo thumbnail → Open full-screen lightbox
- Tap "Ver galería completa" → Open photo gallery screen
- Tap "+ NUEVA CITA" → Open create appointment screen (pre-filled with this client)
- Tap "✏️ Editar" → Open edit client screen

EMPTY STATE (no visits yet):
- Illustration: Calendar or clock icon
- Text: "Esta clienta aún no tiene visitas"
- CTA: "Crear primera cita" (pink button)
```

---

## 📅 FLUJO 8: DATE PICKER MODAL

**🎨 PALETA DE COLORES:**
```css
Modal Background: #E8DDD4 (beige muy claro)
Selected Date: #8B6F5C (café) - Circle background
Today Indicator: #C9A87F (dorado/tierra) - Underline
Appointment Dots: Green #4CAF50, Red #F44336
Text: #FFFFFF (selected), #BDBDBD (unselected), #757575 (disabled)
Overlay: rgba(0,0,0,0.5) - Semi-transparent black
Today Button: #FF69B4 (pink border), white text
```

**📝 PROMPT PARA STITCH:**

```
Design a modal for "Date Picker" in a premium nail salon app.

CONTEXT:
- Used when creating or editing appointments
- Must be fast and easy to use
- Light mode with earth tones

MODAL LAYOUT:

MODAL STYLE:
- Full screen (on mobile) or sheet (bottom 70% of screen)
- Slide up animation (250ms)
- Background overlay: Semi-transparent black (50% opacity)

HEADER:
- Left: "Cancelar" button (16px, gray text)
- Right: "✓" button (20px, pink)
- Height: 56px
- Background: #E8DDD4 (beige muy claro)

MONTH SELECTOR (below header):
- Centered: "< Mayo 2026 >" (20px, Medium)
- Tap arrows to change month
- Tap month name to open month/year picker

CALENDAR GRID:
- 7 columns for day headers (Dom - Sáb)
- 6 rows for dates

Day headers:
- Height: 32px
- Text: Day initials (14px, Medium, gray)
- Centered in each column

Date cells:
- Size: 36x36px each
- Centered text (16px, Regular)
- Today's date: Underline #C9A87F (gold, 2px)
- Selected date: Circle background #8B6F5C (café), white text
- Disabled dates: Light gray #757575, not tappable (e.g., past dates)
- Other month dates: Very light gray #BDBDBD
- Today (when not selected): White text, gold underline

Dots for appointments (below date text):
- Green dot #4CAF50: All appointments confirmed
- Red dot #F44336: Any cancelled/no-show
- Multiple dots: Mixed statuses
- Dot size: 3px circle

BOTTOM SECTION:
- "HOY" button:
  * Height: 40px
  * Outline style (pink border)
  * Rounded 20px (pill)
  * Text: "HOY" (16px, Medium, pink)
  * Centered horizontally
  * Margin bottom: 20px

**COLOR PALETTE:**
- Modal bg: #1A1A1A, Selected: #FF69B4, Today: #C9A87F (underline)
- Dots: Green #4CAF50, Red #F44336
- Text: #FFFFFF (selected), #BDBDBD (unselected), #757575 (disabled)
- Overlay: rgba(0,0,0,0.5), Today button: #FF69B4 border

**INTERACTIONS:**
- Tap date → Select date and close modal
- Tap "✓" → Confirm selection and close
- Tap "Cancelar" → Close modal without changes
- Tap "<" or ">" → Change month
- Tap "HOY" → Select today and close modal
- Swipe left/right → Change month

ANIMATIONS:
- Modal appear: Slide up from bottom (250ms)
- Modal disappear: Slide down to bottom (250ms)
- Month change: Fade transition (150ms)
- Date selection: Scale animation (100ms)

TODAY BUTTON LOGIC:
- If today is already selected → Disabled (gray)
- If today is not selected → Active (pink outline)
- Tap today → Selects today and closes modal immediately

```

---

## 🕐 FLUJO 9: TIME PICKER MODAL

**🎨 PALETA DE COLORES:**
```css
Modal Background: #E8DDD4 (beige muy claro)
Selected Text: #8B6F5C (café) - Centered in wheel
Unselected Text: #BDBDBD (gray, 50% opacity)
Selected Background: #D4C4B5 (beige medio)
Current Time Button: #FF69B4 (pink border), white text
Overlay: rgba(0,0,0,0.5) - Semi-transparent black
```

**📝 PROMPT PARA STITCH:**

```
Design a modal for "Time Picker" in a premium nail salon app.

CONTEXT:
- Used when creating appointments
- Must be quick (technicians are busy)
- 15-minute intervals

MODAL LAYOUT:

MODAL STYLE:
- Same as date picker (full screen or sheet)
- Background overlay: Semi-transparent black

HEADER:
- Left: "Cancelar" button (16px, gray text)
- Right: "✓" button (20px, pink)
- Height: 56px

TIME WHEEL (iOS style) OR SCROLL LIST (Android style):

iOS WHEEL LAYOUT:
- Three columns: [Hour] : [Minute] [AM/PM]
- Wheel height: 200px
- Selected item: Centered, highlighted background
- Unselected items: Dimmed (50% opacity)
- Curved wheel effect (3D)

Column 1 - HOUR:
- Values: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
- Font: 24px, Regular
- Selected: Pink text #FF69B4

Column 2 - MINUTE:
- Values: 00, 15, 30, 45 (15-minute intervals)
- Font: 24px, Regular
- Selected: Pink text

Column 3 - AM/PM:
- Values: AM, PM
- Font: 24px, Medium
- Selected: Pink text

SEPARATOR:
- ":" (colon) between hour and minute columns
- Font: 32px, Bold, gray

BOTTOM SECTION:
- "Hora actual" button:
  * Height: 40px
  * Outline style (pink border)
  * Text: "Hora actual" (16px, Medium, pink)
  * Centered
  * Margin bottom: 20px

COLOR PALETTE:
- Background: #E8DDD4 (beige muy claro)
- Selected text: #8B6F5C (café)
- Unselected text: #BDBDBD (gray, 50% opacity)
- Selected background: #D4C4B5 (beige medio)
- Border: #8B6F5C (café)

INTERACTIONS:
- Scroll wheel → Select value
- Tap "✓" → Confirm and close
- Tap "Cancelar" → Close without changes
- Tap "Hora actual" → Select current time and close

ALTERNATIVE: ANDROID DROP-DOWN STYLE:
- Three dropdowns instead of wheels
- Each dropdown: 56px height, dark gray background
- Tap to open bottom sheet with options
- Selected value shown in dropdown
- Chevron "▼" on right

```

---

## ⚠️ FLUJO 10: CANCEL APPOINTMENT DIALOG

**🎨 PALETA DE COLORES:**
```css
Dialog Background: #D4C4B5 (beige medio)
Overlay: rgba(0,0,0,0.6) - Semi-transparent black
Warning Icon: #C9A06D (naranja tierra) or #B86B5B (rojo tierra)
Confirm Button: #B86B5B (rojo tierra) - Destructive action
Cancel Button: Transparent, #BDBDBD (gray text)
Checkbox: #8B6F5C (café) when checked, gray border when unchecked
Text: #FFFFFF (white title), #E0E0E0 (light gray body), #BDBDBD (gray captions)
```

**📝 PROMPT PARA STITCH:**

```
Design a confirmation dialog for "Cancel Appointment" in a premium nail salon app.

CONTEXT:
- Shown when user taps "Cancelar" on appointment detail
- Must prevent accidental cancellations
- Collect reason for analytics

DIALOG LAYOUT:

DIALOG STYLE:
- Centered modal (not full screen)
- Max width: 400px (90% of screen width)
- Background: #D4C4B5 (beige medio)
- Rounded corners: 16px
- Shadow: Elevation 4 (large shadow)
- Fade in animation (200ms)

HEADER:
- Icon: Warning triangle "⚠️" (32px, orange #FF9800)
- Or "X" circle (32px, red #F44336)
- Centered at top

TITLE:
- Text: "¿Cancelar esta cita?" (20px, Bold)
- Centered
- Margin top: 16px

MESSAGE:
- Text: "Esta acción no se puede deshacer." (16px, Regular, gray)
- Centered
- Max 2 lines

DROPDOWN (below message):
- Label: "Motivo de cancelación:" (14px, Medium, gray)
- Dropdown: 48px height, dark gray background
- Border radius: 8px
- Chevron "▼" (16px, right)
- Placeholder text: "Seleccionar motivo..." (16px, gray)

Dropdown options (when opened):
- Clienta canceló
- Emergencia de manicurista
- Doble reservación
- Otro

CHECKBOX (below dropdown):
- Label: "☐ Aplicar cargo por no-show" (16px, Regular)
- Checkbox: 24x24px (square)
- Checked: Pink background #FF69B4, white checkmark
- Unchecked: Gray border, empty

INFO TEXT (below checkbox):
- Text: "ℹ️ Se cobrará el depósito a la clienta" (12px, Regular, gray)
- Only shows when checkbox is checked

BUTTONS (bottom, horizontal):

Two buttons, equal width:
1. CANCELAR (left):
   - Text: "Cancelar" (16px, Medium, gray)
   - Height: 48px
   - Background: Transparent
   - Border: None

2. CONFIRMAR (right):
   - Text: "Confirmar" (16px, Medium, white)
   - Height: 48px
   - Background: #B86B5B (rojo tierra)
   - Border radius: 8px

DIVIDER between buttons

**COLOR PALETTE (warning/danger focus):**
- Dialog background: #D4C4B5 (beige medio) - Centered modal
- Overlay: rgba(0, 0, 0, 0.6) - Semi-transparent black backdrop
- Warning icon: #C9A06D (naranja tierra) or #B86B5B (rojo tierra) - Top of dialog
- Destructive button: #B86B5B (rojo tierra) - "CONFIRMAR" button (RIGHT)
- Secondary button: Transparent - "Cancelar" button (LEFT)
- Checkbox (checked): #8B6F5C (café) - Pink background with white checkmark
- Checkbox (unchecked): #D4C4B5 (gray border) - Empty
- Text title: #5E4A3E (café oscuro) - "¿Cancelar esta cita?"
- Text body: #8B7462 (café medio) - "Esta acción no se puede deshacer."
- Text captions: #BDBDBD (gray) - Labels, info text

**VISUAL EMPHASIS:**
- Red color (#F44336) for destructive action to prevent accidental taps
- Warning icon (orange or red) at top for immediate recognition
- Gray secondary action to reduce visual weight of cancel option

**INTERACTIONS:**
- Tap outside dialog → Close (no action)
- Tap "Cancelar" → Close dialog
- Tap "Confirmar" → Cancel appointment, close dialog, show toast
- Tap dropdown → Open bottom sheet with reasons
- Tap checkbox → Toggle checked state

TOAST (after confirmation):
- Icon: Checkmark or trash can
- Message: "Cita cancelada correctamente" (16px, Regular)
- Background: #D4C4B5
- Auto-dismiss after 3 seconds

ANIMATIONS:
- Dialog appear: Scale up + fade in (200ms)
- Dialog disappear: Scale down + fade out (200ms)
- Button press: Scale down to 0.95 (100ms)

```

---

## 🎯 TIPS PARA OBTENER MEJORES RESULTADOS

### Si Stitch no entiende algo:

1. **Simplifica el prompt** - Elimina detalles complejos
2. **Usa ejemplos visuales** - ASCII art ayuda mucho
3. **Sé específico con medidas** - "56px height" no "medium height"
4. **Menciona apps de referencia** - "Similar a iOS Calendar"
5. **Describe interacciones** - No solo layouts, también acciones

### Si el diseño no se ve bien:

1. **Ajusta colores** - Prueba con más contraste
2. **Simplifica layout** - Elimina elementos secundarios
3. **Reduce texto** - Usa labels más cortos
4. **Aumenta espaciado** - Más whitespace se ve mejor
5. **Prueba otra vista** - Month → Week → Day

### Para iterar rápido:

1. **Genera una pantalla a la vez** - No todas juntas
2. **Refina en Stitch** - Usa las herramientas de edición
3. **Exporta y ajusta** - Si puedes exportar código, hazlo
4. **Pide feedback** - Muestra a usuarios reales

---

## ✅ CHECKLIST ANTES DE GENERAR

Para cada pantalla, verifica:

**Contenido:**
- [ ] Propósito claro
- [ ] Todos los elementos incluidos
- [ ] Jerarquía visual definida
- [ ] Estados (empty, loading) considerados

**Especificaciones:**
- [ ] Colores en #hex
- [ ] Tamaños en px
- [ ] Espaciado definido
- [ ] Tipografía especificada

**Interacciones:**
- [ ] Acciones de cada elemento
- [ ] Navegación clara
- [ ] Transiciones descritas
- [ ] Validaciones definidas

---

## 🚀 EMPEZAR A DISEÑAR

**Orden recomendado:**
1. Create Appointment Screen (Flujo 1) - Más crítico
2. Calendar Screen (Flujo 2) - Segundo más importante
3. Complete Appointment Screen (Flujo 3) - Tercero crítico
4. Appointment Detail Screen (Flujo 4)
5. Dashboard Screen (Flujo 5)
6. Client List y Profile (Flujo 6-7)
7. Modales (Flujo 8-10)

**Consejo final:** Genera las 3 primeras pantallas primero, revísalas, ajusta, y luego continua con las demás. ¡No intentes generar todo de una vez!
