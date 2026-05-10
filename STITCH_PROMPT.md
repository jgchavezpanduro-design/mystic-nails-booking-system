# Prompt para Stitch - Mystic Nails Art App UX Design

---

## 🎨 PROMPT PRINCIPAL (Copiar y pegar en Stitch)

```
Design a mobile app UX/UI for "Mystic Nails Art", a premium nail studio management app for small beauty businesses in Mexico. The app is used by nail technicians (manicurists) and the salon owner to manage appointments, clients, and finances.

TARGET USERS:
- Primary: Nail technicians (Carolina, Monse, others) who use the app daily to see their appointments, complete services, and record tips
- Secondary: Salon owner (Jorge) who views financial dashboards, reports, and manages the business
- Clients: Future phase - will book appointments and view their service history

USER CONTEXT:
- Fast-paced salon environment
- Technicians are often working on clients while using the app
- Need to use with one hand (thumb-friendly zone)
- Quick interactions are critical
- Mexico location (Spanish language, MXN currency)

CORE USER JOURNEYS:
1. Create appointment: Select date/time → Choose client → Choose technician → Choose services → See price breakdown → Save
2. Complete appointment: Open appointment → Record tip → Select payment method → Upload photo of work → Save
3. View calendar: See daily/weekly/monthly view → Tap appointment to see details → Edit/complete/cancel
4. Dashboard (owner): Select month → See revenue, commissions, expenses → View staff payouts → Manage expenses

DESIGN PRINCIPLES:
- Mobile-first: Everything designed for smartphones
- One-handed operation: Critical actions in bottom half of screen, thumb-friendly zone (bottom 1/3)
- Minimalist: Clean, uncluttered interfaces, generous whitespace
- Fast: Reduce taps to minimum (3 taps max for common actions)
- Visual hierarchy: Important info (price, time, status) prominent
- Feedback: Clear loading states, success/error messages, confirmation dialogs

VISUAL STYLE:
- Premium beauty aesthetic (elegance, sophistication)
- Dark mode primary (black background)
- Color palette: Black (#1A1A1A), Hot Pink (#FF69B4), Gold (#FFD700)
- High contrast for readability
- Card-based UI with subtle shadows
- Rounded corners (8-12px)
- Photos of nail work as visual elements (portfolios)

KEY SCREENS TO DESIGN:

1. CALENDAR SCREEN (Agenda)
   - Month/Week/Day view toggle (horizontal tabs)
   - Calendar grid showing appointment dots
   - Daily appointment list with color-coded status:
     * Green: Confirmed
     * Blue: Completed
     * Red: Cancelled
     * Orange: No-show
   - Each appointment card shows: Time, Client name, Service, Technician, Price
   - Floating Action Button (FAB) "+" at bottom-right for new appointment
   - Bottom tab navigation (4 tabs)

2. CREATE APPOINTMENT SCREEN
   - Date picker (calendar modal)
   - Time picker (scrollable wheel)
   - Searchable client dropdown with "+" to create new client
   - Technician dropdown (avatar + name)
   - Service dropdown with category icons
   - Real-time price calculator card showing:
     * Subtotal
     * Discount field
     * Total
     * Commission breakdown (Technician / Company / Admin percentages)
   - Optional notes field
   - Primary CTA "Guardar Cita" at bottom
   - One-handed friendly: All inputs in bottom half, easy thumb reach

3. APPOINTMENT DETAIL SCREEN
   - Large status indicator (colored badge)
   - Client info card (name, phone, Instagram, photo)
   - Service details (name, duration, price)
   - Technician info (name, avatar, commission split)
   - Action buttons based on status:
     * If confirmed: "Completar" (primary), "Editar" (secondary), "Cancelar" (destructive)
     * If completed: Show final breakdown with tip, photo gallery
   - Swipe gestures for quick actions

4. COMPLETE APPOINTMENT SCREEN
   - Tip amount input (large, prominent)
   - Payment method selector (Cash, Transfer, Card)
   - Photo upload (camera/gallery) with preview
   - Final breakdown card:
     * Service total
     * Tip
     * Technician's total earnings (commission + tip)
   - "Confirmar Completado" CTA
   - Celebration animation on success

5. DASHBOARD SCREEN (Owner only)
   - Month/year selector (dropdown)
   - Metrics grid (2x2):
     * Total appointments
     * Gross revenue
     * Commissions paid
     * Net company balance
   - Revenue vs Commissions chart (line or bar)
   - "Next 7 days" upcoming appointments list (compact)
   - "View Full Reports" link

6. CLIENT LIST SCREEN
   - Search bar at top (rounded, sticky)
   - Client cards showing:
     * Avatar (initial or photo)
     * Name
     * Phone
     * Client type badge (Local/Foreign)
     * Last visit date
   - FAB "+" for new client
   - Swipe left to delete

7. CLIENT PROFILE SCREEN
   - Large avatar with camera icon to edit
   - Name, phone, Instagram handle
   - Client type badge (Local/Foreign)
   - Stats cards: Total visits, Total spent, Last visit
   - "New Appointment" CTA (pre-filled with this client)
   - Visit history timeline (reverse chronological)
   - Photo gallery of previous work (if any)

8. SETTINGS/CONFIG SCREENS
   - Services list with prices
   - Technicians list with commission structures
   - Expense categories
   - Theme toggle (Dark/Light)

INTERACTION PATTERNS:
- Bottom navigation: 4 tabs (Calendar, Dashboard, Clients, Settings)
- Primary CTAs: Bottom of screen, full width, prominent pink color
- Secondary actions: Top right header (⋯ menu)
- Back navigation: Top left arrow
- Modals: Slide up from bottom (sheet style)
- Loading: Skeleton screens for lists, spinner for actions
- Empty states: Friendly illustrations with clear CTAs
- Success: Toast messages with checkmark icons
- Errors: Red toast with retry action

COMPONENT LIBRARY:
- Cards: Rounded (8px), dark gray (#2C2C2C), subtle shadow
- Buttons:
  * Primary: Pink (#FF69B4), 48px height, rounded
  * Secondary: Outline pink, same height
  * Destructive: Red outline
- Inputs: 56px height, dark background, pink border on focus
- Dropdowns: Bottom sheet style with search
- Date/time pickers: Custom modal with large touch targets
- Status badges: Colored dots with labels
- Metrics: Large numbers, small labels, trend indicators (↑↓)

ACCESSIBILITY:
- WCAG AA contrast ratios
- Touch targets minimum 44x44px (iOS) / 48x48px (Android)
- Screen reader support for all icons
- Font sizes: Minimum 16px body, 12px captions

ONBOARDING FLOW:
1. Welcome screen with app value prop
2. Google Sign-In button
3. Permissions request (Calendar, Camera, Notifications)
4. Quick tutorial (3 screens, skippable):
   - "Manage your calendar"
   - "Complete appointments in seconds"
   - "Track your earnings"

Please create a cohesive mobile app design that feels premium, elegant, and specifically tailored for nail technicians who need to manage their business efficiently while working on clients. Focus on the calendar, appointment creation, and completion flows as these are the most critical user journeys.

Reference apps for inspiration: Calendly (calendar), Square Point of Sale (speed), Fresha (beauty salon booking), but with a darker, more premium aesthetic like a luxury beauty brand.
```

---

## 📝 VARIACIONES DEL PROMPT

### Variación 1: Enfocada en Calendar Screen

```
Design a mobile calendar screen for a nail salon appointment management app called "Mystic Nails Art". The calendar is used by nail technicians to view their daily appointments.

REQUIREMENTS:
- Three view modes: Month, Week, Day (horizontal tab toggle at top)
- Month view: Calendar grid with colored dots indicating appointments
- Week view: Horizontal scrollable days with time slots
- Day view: Vertical timeline of appointments (most detailed)
- Appointment cards showing:
  * Time (10:00 AM)
  * Client name (Maria Lopez)
  * Service (Manicura Gel)
  * Technician (Carolina)
  * Price ($450)
  * Status indicator (colored bullet left: Green=Confirmed, Blue=Completed, Red=Cancelled)
- Floating "+" button at bottom-right for new appointment
- Bottom navigation bar with 4 tabs

COLORS:
- Background: Black (#1A1A1A)
- Cards: Dark gray (#2C2C2C)
- Accent: Hot pink (#FF69B4) for CTAs
- Status: Green #4CAF50, Blue #2196F3, Red #F44336

INTERACTION:
- Tap appointment card → View detail screen
- Pull down to refresh
- Scroll to load more days

The design should be optimized for one-handed use (thumb-friendly zone in bottom half of screen).
```

### Variación 2: Enfocada en Appointment Creation Flow

```
Design a multi-step "New Appointment" flow for a nail salon mobile app. The flow is: Select Date/Time → Choose Client → Choose Technician → Choose Services → Review & Save.

SCREEN 1 - Date & Time:
- Large calendar picker (month view)
- Time picker wheel (hour : minute AM/PM)
- "Next" CTA at bottom (pink, full width)

SCREEN 2 - Choose Client:
- Search bar (rounded, "Buscar clienta...")
- Client list with avatars, names, phone numbers
- "+" button to create new client
- "Next" CTA at bottom

SCREEN 3 - Choose Technician:
- Horizontal scrollable cards of technicians
- Each card: Avatar, Name, Commission %
- Single selection (radio button style)
- "Next" CTA at bottom

SCREEN 4 - Choose Services:
- Service categories (Manicura, Pedicure, Mani-Pedi, Extras)
- Multi-select chips for services
- Real-time price calculation card:
  * Subtotal: $XXX
  * Duration: XX min
- "Next" CTA at bottom

SCREEN 5 - Review & Save:
- Summary card with all details
- Commission breakdown (Technician: $XX, Company: $XX, Admin: $XX)
- Optional notes field
- "Guardar Cita" primary CTA at bottom

COLORS & STYLE:
- Black background (#1A1A1A)
- Pink accent (#FF69B4)
- Dark gray cards (#2C2C2C)
- Rounded corners (8-12px)
- Progress indicator at top (Step 3 of 5)

The flow should be optimized for speed (minimize taps) and one-handed use (all controls in bottom half of screen).
```

### Variación 3: Enfocada en Dashboard Financiero

```
Design a financial dashboard screen for a nail salon owner to view monthly business metrics.

CONTENT:
- Header: "Dashboard" + Month/Year dropdown (default: current month)
- Metrics grid (2x2 cards):
  * Total Appointments (large number, small label)
  * Gross Revenue (large number with $, trend indicator ↑↓ vs last month)
  * Commissions Paid (large number, breakdown by technician)
  * Net Company Balance (highlighted, most important)
- Chart: Revenue vs Commissions (bar or line chart, monthly trend)
- "Staff Payouts" section:
  * List of technicians with amounts owed
  * Each row: Avatar, Name, Amount, [Pay] button
- Upcoming section: "Next 7 days" compact appointment list

VISUAL HIERARCHY:
- Net Company Balance most prominent (gold border/background)
- Trend indicators (green ↑ for positive, red ↓ for negative)
- Use chart to show pattern over time

COLORS:
- Background: Black (#1A1A1A)
- Cards: Dark gray (#2C2C2C)
- Accent 1: Hot pink (#FF69B4) for CTAs
- Accent 2: Gold (#FFD700) for financial highlights
- Green: Positive trends
- Red: Negative trends or high expenses

The dashboard should give the owner a quick overview of business health in under 10 seconds.
```

### Variación 4: Enfocada en Client Profile

```
Design a client profile screen for a nail salon app showing client details and service history.

HEADER SECTION:
- Large circular avatar (initial or photo)
- Name (large, bold)
- Instagram handle (@username)
- Client type badge (Local / Foreign) with color coding

INFO CARD:
- Phone number (tappable to call)
- Birthday (with cake icon)
- "How they found us" (source: Instagram, Facebook, Referral)
- Notes/Allergies (if any)

STATS SECTION (3 columns):
- Total visits (count)
- Total spent (MXN $)
- Last visit (date)

ACTION SECTION:
- Primary CTA: "+ New Appointment" (full width, pink)
- Secondary: "Edit Profile" (text link)

HISTORY SECTION:
- "Service History" header
- Reverse chronological timeline
- Each visit:
  * Date
  * Service (name, technician)
  * Price
  * Photo thumbnail (if available)
  * Tap to see details

PHOTO GALLERY (if photos exist):
- Grid of work photos (2 columns)
- Full-screen lightbox on tap
- Date stamps on photos

COLORS:
- Background: Black (#1A1A1A)
- Cards: Dark gray (#2C2C2C)
- Accent: Pink (#FF69B4)
- Client type: Green for Local, Blue for Foreign

The profile should help technicians quickly understand client preferences and history before an appointment.
```

### Variación 5: Enfocada en Appointment Completion Flow

```
Design the "Complete Appointment" flow for nail technicians to record finished services.

SCREEN LAYOUT:
- Header: "Completar Cita" + Back button
- Client info card (small): Name, Service, Date/Time
- Large tip input field (prominent, keypad-friendly)
- Payment method selector: Cash | Transfer | Card (horizontal toggle)
- Photo upload section:
  * Large square with camera icon
  * "Take photo" or "Choose from gallery"
  * Preview once uploaded
- Optional notes field ("Notas finales")
- Summary card (bottom):
  * Service total: $XXX
  * Tip: $XX
  * Technician's total: $XXX (highlighted)
- "Confirmar Completado" primary CTA (pink, full width, bottom)

INTERACTIONS:
- Auto-focus on tip field when screen opens
- Number keypad defaults to tip input
- Camera opens directly on tap
- Success celebration (confetti or checkmark animation)
- Auto-navigate back to calendar after 2 seconds

VISUAL FEEDBACK:
- Technician's total amount grows larger when tip is entered
- Real-time calculation of total
- Photo preview with crop tool

COLORS:
- Background: Black (#1A1A1A)
- Accent: Pink (#FF69B4) for CTA
- Success: Green (#4CAF50) for confirmation
- Gold (#FFD700) for the total earnings highlight

This screen should be the fastest interaction in the app - technicians use it multiple times per day.
```

---

## 🎯 CONSEJOS PARA OBTENER MEJORES RESULTADOS EN STITCH

### 1. Sé Específico con Colores
```
✅ BUENO: "Black background #1A1A1A, hot pink accent #FF69B4, dark gray cards #2C2C2C"
❌ MAL: "Dark theme with pink accents"
```

### 2. Describe Interacciones, No Solo Pantallas
```
✅ BUENO: "Floating action button at bottom-right, tap opens modal sheet"
❌ MAL: "Button to add new items"
```

### 3. Menciona Patrones de Referencia
```
✅ BUENO: "Similar to iOS Calendar app but with dark theme"
❌ MAL: "Make it look modern"
```

### 4. Especifica Tamaños y Espaciados
```
✅ BUENO: "Buttons 48px height, rounded 8px corners, 16px padding"
❌ MAL: "Normal sized buttons"
```

### 5. Prioriza la Jerarquía Visual
```
✅ BUENO: "Net Company Balance most prominent (large font, gold border), other metrics smaller"
❌ MAL: "Show all metrics equally"
```

### 6. Menciona Estados (Loading, Error, Empty)
```
✅ BUENO: "Empty state: Illustration of calendar with 'No appointments yet', CTA 'Create first appointment'"
❌ MAL: "Handle empty states"
```

### 7. Considera One-Handed Use
```
✅ BUENO: "All primary actions in bottom half of screen, thumb-friendly zone"
❌ MAL: "Easy to use"
```

### 8. Sé Específico sobre Navegación
```
✅ BUENO: "Bottom tab navigation with 4 tabs: Calendar (icon), Dashboard (chart), Clients (people), Settings (gear)"
❌ MAL: "Standard navigation"
```

---

## 🔄 FLUJO DE TRABAJO RECOMENDADO

### Paso 1: Generar Pantallas Individuales
Usa las variaciones del prompt para generar cada pantalla por separado:
1. Calendar Screen
2. Create Appointment Flow (5 screens)
3. Appointment Detail Screen
4. Complete Appointment Screen
5. Dashboard Screen
6. Client List & Profile Screens

### Paso 2: Revisar y Refinar
- Revisar coherencia entre pantallas
- Asegurar consistencia de componentes
- Verificar que los colores se mantengan
- Validar que la navegación sea lógica

### Paso 3: Crear Component Library
- Extraer componentes reutilizables (Buttons, Cards, Inputs)
- Documentar variaciones (primary, secondary, disabled states)
- Crear guía de estilos

### Paso 4: Prototipo Interactivo
- Conectar pantallas en prototipo
- Definir transiciones
- Agregar microinteracciones
- Probar con usuarios reales

---

## 📱 EXPORTAR E IMPLEMENTAR

Una vez que tengas los diseños de Stitch:

### Opción A: Exportar a Código
- Si Stitch exporta código React Native, úsalo como base
- Refactor para seguir la arquitectura del proyecto
- Integrar con los servicios ya creados

### Opción B: Implementar Manualmente
- Usa los diseños como referencia visual
- Implementa componentes en React Native
- Sigue el Design System creado
- Usa las constantes de `src/constants/theme.ts`

### Opción C: Híbrida
- Exporta assets desde Stitch
- Usa los diseños como guía
- Implementa lógica de negocio manualmente

---

## ✅ CHECKLIST ANTES DE USAR STITCH

- [ ] Tener clara la funcionalidad principal de la pantalla
- [ ] Definir elementos que deben estar vs opcional
- [ ] Saber qué acciones son primarias vs secundarias
- [ ] Tener referencia visual (apps similares)
- [ ] Conocer restricciones técnicas (pantalla pequeña, una mano)
- [ ] Definir paleta de colores exacta
- [ ] Saber qué datos se mostrarán (mock data)
- [ ] Considerar estados vacíos y de error
- [ ] Pensar en accesibilidad (contraste, tamaños)
- [ ] Considerar diferentes idiomas (español)

---

## 🚀 LISTO PARA USAR

Copia y pega cualquiera de estos prompts en Stitch según lo que necesites diseñar. El prompt principal cubre toda la app, mientras que las variaciones son útiles para enfocarte en pantallas específicas.

**Recomendación:** Empieza con las pantallas críticas (Calendar → Create Appointment → Complete Appointment) antes de pasar a las secundarias.
