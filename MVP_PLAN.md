# MVP Implementation Plan - Mystic Nails Art

## Objetivo del MVP
Crear una app móvil funcional en 4-6 semanas que permita gestionar citas y ver el dashboard financiero, reemplazando el sistema actual de Google Sheets.

---

## 📱 Pantallas del MVP (Priorizadas)

### FASE 1: Core (Semanas 1-3)
**Objetivo:** Gestión básica de citas y agenda

#### 1.1 Login Screen
- **Descripción:** Pantalla de autenticación con Google Sign-In
- **Campos:** Botón "Sign in with Google"
- **Validación:** Solo usuarios autorizados (jgchavezpanduro@gmail.com, 27supercaro@gmail.com)
- **Post-login:** Navegar a Dashboard

#### 1.2 Dashboard Screen
- **Descripción:** Vista principal con métricas del mes
- **Componentes:**
  - Selector de mes/año (default: mes actual)
  - Cards con métricas:
    - Citas totales (mes)
    - Ingresos brutos (MXN)
    - Comisiones pagadas
    - Saldo neto empresa
    - Promedio por cita
  - Botón "Ver Agenda" → CalendarScreen
  - Botón "Nueva Cita" → CreateAppointmentScreen
  - Botón "Ver Reportes" → ReportsScreen

#### 1.3 Calendar Screen (Agenda)
- **Descripción:** Vista de calendario con citas
- **Componentes:**
  - Vista mensual/semanal/diaria (tabs)
  - Lista de citas del día seleccionado
  - Cada cita muestra:
    - Hora
    - Clienta
    - Servicio
    - Manicurista
    - Estado (color-coded)
  - Tap en cita → ViewAppointmentScreen
  - FAB (Floating Action Button) "+" → CreateAppointmentScreen
- **Sync:** Leer de Google Calendar + local storage

#### 1.4 Create Appointment Screen
- **Descripción:** Formulario para crear nueva cita
- **Campos:**
  - Fecha (date picker)
  - Hora (time picker)
  - Clienta (searchable dropdown + botón "Nueva Clienta")
  - Manicurista (dropdown)
  - Servicio principal (dropdown)
  - Servicios extra (multi-select)
  - Duración (auto-calculate de servicios)
  - Tipo clienta (auto-fill de clienta, editable)
  - Descuento (number input, default: 0)
  - Depósito (number input, default: 0)
  - Método de pago (dropdown)
  - Notas (textarea)
- **Preview en tiempo real:**
  - Subtotal (por tipo clienta)
  - Desglose de comisión (manicurista / empresa / admin)
  - Total a cobrar
- **Acciones:**
  - "Guardar" → Crear en Sheets + Calendar + local
  - "Cancelar" → Volver a Calendar

#### 1.5 View Appointment Screen
- **Descripción:** Detalle de una cita existente
- **Componentes:**
  - Toda la información de la cita (read-only)
  - Botón "Editar" → EditAppointmentScreen (si no está completada)
  - Botón "Completar" → CompleteAppointmentScreen (si está confirmada)
  - Botón "Cancelar" → CancelAppointmentDialog (si está pendiente/confirmada)
  - Botón "Ver Perfil Clienta" → ClientProfileScreen
  - Foto del trabajo (si está completada)

### FASE 2: Finalización de Citas (Semana 4)
**Objetivo:** Registrar propinas, pagos y fotos al completar citas

#### 2.1 Complete Appointment Screen
- **Descripción:** Formulario al completar una cita
- **Campos:**
  - Propina real (number input)
  - Monto final pagado (auto-filled, editable)
  - Método de pago final (dropdown)
  - Foto del trabajo (camera picker o gallery upload)
  - Notas finales (textarea)
- **Preview:**
  - Comisión total (servicio + propina)
  - Desglose final (empresa / admin)
- **Acciones:**
  - "Confirmar Completado" → Update cita status to 'completada' + sync

#### 2.2 Edit Appointment Screen
- **Descripción:** Editar cita existente (similar a Create)
- **Campos:** Igual que Create Appointment, pre-filled
- **Acciones:**
  - "Guardar Cambios" → Update + sync
  - "Cancelar" → Volver

#### 2.3 Cancel Appointment Dialog
- **Descripción:** Confirmar cancelación de cita
- **Campos:**
  - Razón de cancelación (dropdown: clienta canceló, emergencia, etc.)
  - Checkbox "Aplicar cargo?" (para no-show)
- **Acciones:**
  - "Confirmar Cancelación" → Update status + cancel Calendar event

### FASE 3: Gestión de Catálogos (Semana 5)
**Objetivo:** CRUD básico de maestros

#### 3.1 Clients Screen (Listado)
- **Descripción:** Lista de todas las clientas
- **Componentes:**
  - Search bar (por nombre o teléfono)
  - Lista con cards:
    - Nombre
    - Teléfono
    - Tipo (Local/Extranjera)
    - Última visita
  - Tap en clienta → ClientProfileScreen
  - FAB "+" → CreateClientScreen

#### 3.2 Client Profile Screen
- **Descripción:** Perfil detallado de clienta
- **Componentes:**
  - Todos los datos de la clienta
  - Historial de visitas (lista de citas)
  - Total gastado
  - Fotos de trabajos anteriores (gallery)
  - Botón "Editar" → EditClientScreen
  - Botón "Nueva Cita" → CreateAppointment (pre-filled con esta clienta)

#### 3.3 Create/Edit Client Screen
- **Descripción:** Formulario de clienta
- **Campos:**
  - Nombre (*)
  - Teléfono (*)
  - Instagram
  - Tipo (dropdown: Local/Extranjera)
  - Cumpleaños (date picker)
  - Cómo te encontró (dropdown)
  - Notas / alergias (textarea)
- **Acciones:**
  - "Guardar" → Create/update + sync
  - "Cancelar" → Volver

#### 3.4 Services Screen (Listado)
- **Descripción:** Lista de servicios
- **Componentes:**
  - Lista con cards:
    - Nombre
    - Categoría
    - Precio Local / Extranjera
    - Tiempo
  - Tap en servicio → EditServiceScreen
  - FAB "+" → CreateServiceScreen

#### 3.5 Create/Edit Service Screen
- **Campos:**
  - Nombre (*)
  - Categoría (dropdown)
  - Detalle (textarea)
  - Precio Local (*)
  - Precio Extranjera (*)
  - Tiempo en minutos (*)
  - Activo (toggle)

#### 3.6 Staff Screen (Listado)
- **Descripción:** Lista de manicuristas
- **Similar a Services Screen**

#### 3.7 Create/Edit Staff Screen
- **Campos:**
  - Nombre (*)
  - Teléfono (*)
  - Modelo (dropdown: porcentaje / mixto)
  - % Manicurista (*)
  - % Empresa (*)
  - % Admin (*)
  - Si es mixto: Sueldo fijo semanal
  - Estado (toggle: activa/inactiva)
  - Notas

### FASE 4: Reportes y Finanzas (Semana 5-6)
**Objetivo:** Dashboard financiero y liquidaciones

#### 4.1 Reports Screen
- **Descripción:** Panel de reportes avanzados
- **Componentes:**
  - Selector de mes/año
  - Tabs:
    - "Resumen" → Dashboard metrics
    - "Liquidaciones" → StaffPayoutsScreen
    - "Compras" → ExpensesScreen
    - "Retención" → ClientRetentionScreen

#### 4.2 Staff Payouts Screen
- **Descripción:** Liquidaciones del mes por manicurista
- **Componentes:**
  - Selector de mes/año
  - Lista de manicuristas con cards:
    - Nombre
    - Sueldo fijo (si aplica)
    - Comisión total
    - Propinas total
    - **Total a pagar** (highlighted)
    - # citas completadas
  - Botón "Pagar" (para marcar como pagado)

#### 4.3 Expenses Screen (Compras)
- **Descripción:** Registro y listado de gastos
- **Componentes:**
  - Lista de compras del mes
  - Total del mes
  - FAB "+" → CreateExpenseScreen
  - Tap en compra → EditExpenseScreen

#### 4.4 Create/Edit Expense Screen
- **Campos:**
  - Fecha (*)
  - Concepto (*)
  - Categoría (dropdown)
  - Monto (*)
  - Proveedor
  - Método de pago
  - Quién compra
  - Notas

#### 4.5 Client Retention Screen
- **Descripción:** Análisis de retención de clientas
- **Componentes:**
  - Lista de clientas ordenadas por:
    - Última visita (más antiguas primero)
    - Frecuencia de visitas
  - Alertas de clientas que no vienen en > X días
  - Clientas nuevas del mes
  - Clientas inactivas

---

## 🏗️ Arquitectura Técnica del MVP

### Stack
- **Frontend:** React Native + Expo
- **Navegación:** React Navigation (Stack + Bottom Tabs)
- **Estado:** React Context + hooks
- **Almacenamiento:** AsyncStorage (offline) + Google Sheets (online)
- **Autenticación:** Expo Auth Session (Google Sign-In)
- **Calendar:** expo-calendar (Google Calendar integration)

### Estructura de Carpetas (Creada)
```
src/
├── types/           # Tipos TypeScript
├── models/          # Modelos de datos (para usar en la UI)
├── services/        # API services (Sheets, Calendar, Storage)
├── screens/         # Pantallas de la app
├── navigation/      # Configuración de navegación
├── components/      # Componentes reutilizables
├── utils/           # Utilidades (cálculos, formatos)
├── hooks/           # Custom React hooks
├── context/         # Context providers
└── constants/       # Constantes (colores, etc.)
```

---

## 🚀 Orden de Implementación

### Semana 1: Setup + Login + Dashboard
1. Configurar navegación (Stack + Tabs)
2. Crear servicios base (Storage, placeholder Sheets/Calendar)
3. Login Screen con Google Sign-In
4. Dashboard Screen con datos mock
5. Test: Flujo completo de login → dashboard

### Semana 2: Agenda + Crear Cita
6. Calendar Screen con mock data
7. Create Appointment Screen (sin sync todavía)
8. View Appointment Screen
9. Integrar cálculos de comisiones
10. Test: Crear cita → ver en calendario → ver detalle

### Semana 3: Sync + Google Calendar
11. Implementar sync con Google Calendar
12. Implementar sync con Google Sheets (Apps Script)
13. Modo offline (AsyncStorage)
14. Test: Crear cita → sync → verificar en Calendar/Sheets

### Semana 4: Completar Citas
15. Complete Appointment Screen
16. Edit Appointment Screen
17. Cancel Appointment Dialog
18. Subida de fotos (Drive/Storage)
19. Test: Flujo completo de cita (crear → completar → verificar finanzas)

### Semana 5: Catálogos (CRUD)
20. Clients Screens (List, Profile, Create, Edit)
21. Services Screens (List, Create, Edit)
22. Staff Screens (List, Create, Edit)
23. Test: Crear clienta → crear servicio → crear cita con ellos

### Semana 6: Reportes + Polishing
24. Reports Screen + tabs
25. Staff Payouts Screen
26. Expenses Screens
27. Client Retention Screen
28. UI/UX improvements (theme, colors, animations)
29. Testing end-to-end
30. Deploy a Expo EAS (Android + iOS)

---

## 📝 Notas Importantes

### Google Apps Script
Necesitas crear un script que exponga endpoints REST:
- `GET /clientas` → Retorna lista de clientas
- `POST /clientas` → Crea nueva clienta
- `GET /citas?mes=X&anio=Y` → Retorna citas filtradas
- `POST /citas` → Crea nueva cita
- `PUT /citas/:id` → Actualiza cita
- `DELETE /citas/:id` → Elimina cita
- (Similar para servicios, manicuristas, compras)

### Permisos de Calendar
Configurar en `app.json`:
```json
{
  "expo": {
    "ios": {
      "infoPlist": {
        "NSCalendarsUsageDescription": "Necesitamos acceso a tu calendario para gestionar las citas de Mystic Nails"
      }
    },
    "android": {
      "permissions": ["android.permission.READ_CALENDAR", "android.permission.WRITE_CALENDAR"]
    }
  }
}
```

### Theme
Colores sugeridos (negro/rosa/dorado):
- Primary: #FF69B4 (Hot Pink)
- Secondary: #FFD700 (Gold)
- Background Dark: #1A1A1A
- Background Light: #FFFFFF
- Text Dark: #1A1A1A
- Text Light: #FFFFFF
- Accent: #9370DB (Medium Purple)

---

## ✅ Criterios de Aceptación del MVP

### Mínimo Viable:
- [ ] Login con Google funciona
- [ ] Se pueden crear citas
- [ ] Se pueden ver citas en calendario
- [ ] Se pueden completar citas (registrar propina, pago, foto)
- [ ] Dashboard muestra métricas correctas del mes
- [ ] Se crean eventos en Google Calendar
- [ ] Funciona en modo offline (se sincroniza después)
- [ ] Se puede instalar en Android e iOS (via Expo Go o EAS)

### Deseable (si hay tiempo):
- [ ] CRUD de clientas
- [ ] CRUD de servicios
- [ ] CRUD de manicuristas
- [ ] Registro de compras/gastos
- [ ] Liquidaciones de manicuristas
- [ ] Reporte de retención de clientas
- [ ] Notificaciones push (24h y 1h antes)
