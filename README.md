# Mystic Nails Art - Mobile App

App móvil para gestión de un estudio de uñas en México, hecha con React Native + Expo.

## 🚀 Quick Start

### Prerrequisitos
- Node.js 18+
- npm o yarn
- Cuenta de Google (para autenticación)
- Expo Go app en tu teléfono (iOS/Android)

### Instalación

```bash
# Instalar dependencias
npm install

# Iniciar servidor de desarrollo
npm start
```

### Correr en tu dispositivo

1. Abre Expo Go en tu teléfono
2. Escanea el código QR que aparece en la terminal
3. ¡Listo! La app se cargará en tu teléfono

### Comandos disponibles

```bash
npm start          # Inicia servidor de desarrollo
npm run android    # Abre en Android Emulator
npm run ios        # Abre en iOS Simulator
npm run web        # Abre en navegador web
```

---

## 📂 Estructura del Proyecto

```
├── src/
│   ├── types/           # Tipos TypeScript (Clienta, Cita, etc.)
│   ├── models/          # Modelos de datos
│   ├── services/        # Servicios (Google Sheets, Calendar, Storage)
│   ├── screens/         # Pantallas de la app
│   ├── navigation/      # Configuración de navegación
│   ├── components/      # Componentes reutilizables
│   ├── utils/           # Utilidades (cálculos, formatos)
│   ├── hooks/           # Custom React hooks
│   ├── context/         # Context providers
│   └── constants/       # Constantes (colores, etc.)
├── data/                # Archivos de datos (Excel original)
├── App.tsx              # Componente principal
└── package.json
```

---

## 📋 Qué está listo

### ✅ Completado

1. **Análisis del sistema actual**
   - Estructura de datos del Excel analizada
   - Lógica de comisiones documentada
   - Modelos de datos definidos en TypeScript

2. **Proyecto Expo inicializado**
   - React Native + TypeScript configurado
   - Dependencias instaladas (navegación, calendar, storage, etc.)
   - Estructura de carpetas creada

3. **Tipos y modelos de datos**
   - [src/types/index.ts](src/types/index.ts) - Todos los tipos del sistema
   - Clienta, Servicio, Manicurista, Cita, Compra, etc.

4. **Servicios core**
   - [src/utils/calculations.ts](src/utils/calculations.ts) - Funciones de cálculo de comisiones
   - [src/services/googleSheets.ts](src/services/googleSheets.ts) - Integración con Google Sheets (placeholder)
   - [src/services/googleCalendar.ts](src/services/googleCalendar.ts) - Integración con Google Calendar
   - [src/services/storage.ts](src/services/storage.ts) - Almacenamiento local para modo offline

5. **Plan del MVP**
   - [MVP_PLAN.md](MVP_PLAN.md) - Plan detallado de 6 semanas
   - 30 tareas priorizadas
   - Pantallas definidas con wireframes textuales

---

## 🎯 Próximos pasos (Semanas 1-3)

1. **Configurar navegación**
   ```bash
   # Crear archivos de navegación
   - src/navigation/AppNavigator.tsx
   - src/navigation/AuthNavigator.tsx
   ```

2. **Crear primera pantalla (Login)**
   ```bash
   - src/screens/LoginScreen.tsx
   - Integrar Google Sign-In con Expo Auth Session
   ```

3. **Crear Dashboard**
   ```bash
   - src/screens/DashboardScreen.tsx
   - src/components/DashboardCard.tsx
   - Conectar con servicios de datos
   ```

4. **Crear Calendar Screen**
   ```bash
   - src/screens/CalendarScreen.tsx
   - Integrar con expo-calendar
   - Mostrar citas del día/semana/mes
   ```

5. **Crear Appointment Screens**
   ```bash
   - src/screens/CreateAppointmentScreen.tsx
   - src/screens/ViewAppointmentScreen.tsx
   - src/screens/CompleteAppointmentScreen.tsx
   - Integrar cálculos de comisiones
   ```

---

## 🔧 Configuración pendiente

### Google Sign-In
1. Crear proyecto en Google Cloud Console
2. Configurar OAuth 2.0 credentials
3. Agregar Client ID en `app.json`

### Google Calendar
1. Habilitar Calendar API en Google Cloud Console
2. Configurar permisos en `app.json`
3. Solicitar permisos al usuario en runtime

### Google Sheets Integration
1. Crear Google Apps Script con endpoints REST
2. Deployar como Web App
3. Configurar URL en `src/services/googleSheets.ts`

### Push Notifications
1. Configurar Expo Notifications
2. Crear canal de notificaciones
3. Programar notificaciones 24h y 1h antes de citas

---

## 📱 MVP Roadmap

### Fase 1: Core (Semanas 1-3)
- [ ] Login con Google
- [ ] Dashboard con métricas del mes
- [ ] Calendar con citas
- [ ] Crear citas
- [ ] Ver detalle de citas

### Fase 2: Finalización (Semana 4)
- [ ] Completar citas (propina, pago, foto)
- [ ] Editar citas
- [ ] Cancelar citas

### Fase 3: Catálogos (Semana 5)
- [ ] CRUD de Clientas
- [ ] CRUD de Servicios
- [ ] CRUD de Manicuristas

### Fase 4: Reportes (Semanas 5-6)
- [ ] Liquidaciones de manicuristas
- [ ] Registro de compras/gastos
- [ ] Reporte de retención de clientas
- [ ] Dashboard financiero completo

---

## 🎨 Theme Colors

```typescript
const colors = {
  primary: '#FF69B4',      // Hot Pink
  secondary: '#FFD700',    // Gold
  accent: '#9370DB',       // Medium Purple
  darkBg: '#1A1A1A',       // Black
  lightBg: '#FFFFFF',      // White
  darkText: '#1A1A1A',     // Black text
  lightText: '#FFFFFF',    // White text
  success: '#4CAF50',      // Green
  error: '#F44336',        // Red
  warning: '#FF9800',      // Orange
};
```

---

## 📄 Documentación

- [MVP_PLAN.md](MVP_PLAN.md) - Plan detallado de implementación
- [CLAUDE.md](CLAUDE.md) - Guía para desarrolladores
- [dataset.md](dataset.md) - Especificación original del proyecto
- [data/excel-analysis.json](data/excel-analysis.json) - Análisis del Excel actual

---

## 🤝 Autores

- **Jorge Chavez** - Project Lead & Developer
- **Carolina** - Co-owner (Carolina: 27supercaro@gmail.com)
- **Mystic Nails Art** - Business Owner (jgchavezpanduro@gmail.com)

---

## 📄 Licencia

Privado - Mystic Nails Art
