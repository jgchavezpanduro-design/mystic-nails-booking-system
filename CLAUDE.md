# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Mystic Nails Art** - A dual-component project for a private nail studio in Mexico:
1. **Static Landing Page** (root directory) - Marketing website for the business
2. **Mobile Management App** ([mystic-nails-app/](mystic-nails-app/)) - React Native Expo app to replace Google Sheets/Calendar system

### Project Structure
```
├── index.html              # Static landing page (marketing website)
├── assets/                 # Landing page assets
├── deploy.sh              # Landing page deployment script
├── mystic-nails-app/      # React Native Expo mobile app
│   ├── src/               # App source code
│   ├── package.json       # App dependencies
│   └── app.json          # Expo configuration
├── src/                   # Type definitions and utilities (legacy)
├── data/                  # Excel system reference data
└── google-apps-script/    # Backend API for Sheets integration
```

**When working on the mobile app, navigate to the app directory:**
```bash
cd mystic-nails-app
```

### Current State
This project is in the **active development phase**. The technical foundation is complete:
- ✅ Landing page created and ready for deployment
- ✅ Expo project initialized with TypeScript
- ✅ Data models and types defined
- ✅ Commission calculation logic implemented
- ✅ Service layer created (Google Sheets, Calendar, Storage)
- ✅ MVP plan detailed with 30 prioritized tasks
- 🔄 Ready to implement screens (starting with Login)

The current system runs on:
- Google Sheets (dashboard, appointments, clients, services, staff, expenses)
- Google Calendar (scheduling)
- Manual commission calculations

### Business Context

**Location:** Mexico (Currency: MXN)

**Staff & Commission Structure:**
- **Carolina** (co-owner): 80% to her, 15% Company, 5% Admin
- **Monse**: 40% to her, 35% Company, 25% Admin
- **Manicurista 3**: Fixed salary (MXN $1200/week) + 25% commission → 45% Mystic Nails / 30% Admin

**Pricing Model:**
- Most services have **Local** vs **Foreign** (Extranjera) differential pricing
- Exception: Pedicure services (same price for all)
- Commissions calculated from gross revenue, then split by percentage

**Key Data Entities:**
- **Clientas** (Clients): Name, phone, Instagram, type (Local/Foreign), birthday, how they found the salon, allergies/notes, visit history, photos of previous work
- **Servicios** (Services): Name, description, duration (min), price local, price foreign, category
- **Manicuristas** (Staff): Name, commission % or mixed model (fixed + %), phone, photo, active/inactive, notes
- **Citas** (Appointments): Date, time, client, staff, service(s), detail, estimated time, status (confirmed/completed/cancelled/no-show), discount, client type, phone, Instagram, payment method, deposit, amount paid, tip, notes
- **Compras/Gastos** (Expenses): Date, concept/category, amount, notes (deducted from company funds)

## Quick Start

**To work on the landing page:**
```bash
# Stay in root directory
python3 -m http.server 8000
# Open http://localhost:8000
```

**To work on the mobile app:**
```bash
cd mystic-nails-app
npm install
npm start
# Scan QR with Expo Go app
```

**To deploy:**
- Landing page: `./deploy.sh` (from root)
- Mobile app: `eas build --platform android` or `eas build --platform ios` (from mystic-nails-app/)

## Target Architecture

**Recommended Stack:** **React Native + Expo** (cross-platform iOS/Android/Web) with:
- **Framework:** Expo Go for development preview on device
- **Builds:** Expo EAS for Android APK/AAB, iOS IPA, and web deployment
- **Deployment:** Expo EAS (Expo Application Services) for Android APK/IPA, iOS, and web builds
- **Authentication:** Google Sign-In + Firebase Auth (Expo Auth or Firebase JS SDK)
- **Backend (Initial):** Google Sheets via Google Apps Script + Google Calendar API
- **Backend (Future):** Firebase or Supabase
- **Sync:** Bidirectional with Google Calendar, automatic write to Sheets "Citas" sheet
- **UI/UX:** Mobile-first, React Native Paper or NativeBase, dark/light mode, heavy use of cards and images, one-handed operation
- **Offline Mode:** AsyncStorage/Expo SQLite with sync when internet returns
- **Navigation:** React Navigation

## Core Features (MVP Priority)

### 1. Authentication & Roles
- Google account login (jgchavezpanduro@gmail.com, 27supercaro@gmail.com)
- Roles: Admin (full access), Manicuristas (limited read/write)
- Financial data restricted to authorized users only

### 2. Master Data (CRUD)
- Clients, Services, Staff, Expenses

### 3. Agenda & Appointments (Core)
- Calendar views (monthly/weekly/day) with **bidirectional Google Calendar sync**
- Create/edit/cancel appointments
- Auto-price based on client type (Local/Foreign)
- Real-time display of: total price, commission breakdown, company %, admin %, estimated tip
- Appointment states with cancellation/no-show reasons
- Push notifications (24h and 1h before)
- "Next 7 days" and "Today" views

### 4. Completed Appointment Registration
- Mark complete → record actual tip, payment method, final amount, discount
- Auto-calculate commission split (staff + company + admin)
- Photo upload of finished work (to Drive or app storage)

### 5. Financial Dashboard
- Monthly dashboard: total appointments, gross revenue, commissions paid, expenses, net company balance, admin net pay, average per appointment, monthly tips, cancellations/no-shows
- Staff payouts (how much owed to each manicurist this month)
- Reports filterable by month/year, staff, client

## Data Reference

Current system data is stored in `data/Mystic_Nails_Art_Sistema.xlsx` with sheets:
- Dashboard
- Citas
- Clientas
- Servicios
- Manicuristas
- Compras
- Liquidaciones
- Configuración

**Analysis Completed:** ✅ Excel file analyzed. Calculation logic extracted and implemented in `src/utils/calculations.ts`

## Development Workflow

### Landing Page Development

**Local Testing:**
```bash
# From root directory
python3 -m http.server 8000
# Open http://localhost:8000 in browser
```

**Deployment:**
```bash
# Automated deployment script
./deploy.sh

# Manual Netlify deployment
netlify deploy --prod --dir=. --site=mystic-nails-art

# Manual Vercel deployment
vercel --prod
```

**Key Files:**
- [index.html](index.html) - Main landing page
- [INSTRUCCIONES_DEPLOYMENT.md](INSTRUCCIONES_DEPLOYMENT.md) - Detailed deployment instructions

### Mobile App Development

**Navigate to app directory first:**
```bash
cd mystic-nails-app
```

**Testing:**
- Use Expo Go app on physical devices for rapid testing during development
- Test on both iOS and Android devices simultaneously

**Development Commands:**
```bash
npm start              # Start Expo development server
npm run android        # Open in Android Emulator
npm run ios            # Open in iOS Simulator
npm run web            # Open in web browser
```

**Building & Deployment:**
- **Development:** `npm start` → scan QR with Expo Go
- **Android Build:** `eas build --platform android` (APK for testing, AAB for Play Store)
- **iOS Build:** `eas build --platform ios` (IPA for TestFlight/App Store)
- **Web Build:** `npx expo export:web` or deploy to Expo-hosted web

**Key Expo Libraries to Use:**
- `expo-auth-session` or `@react-native-firebase/auth` for Google Sign-In
- `expo-calendar` for Google Calendar integration
- `expo-file-system` and `expo-media-library` for photo storage
- `expo-notifications` for push notifications
- `@react-native-async-storage/async-storage` for offline data
- `expo-localization` for MXN currency and Spanish locale
- `expo-linear-gradient` for elegant UI (black/pink/gold theme)

## Development Priorities

1. **MVP:** Agenda + Create Appointment + Basic Dashboard + Master Data
2. **Phase 2:** Offline mode, photo portfolio, reporting enhancements
3. **Future:** Client self-booking via WhatsApp/public link, inventory management

## Key Calculation Requirements

When implementing financial calculations:
- **Gross Revenue** → **Commission %** to manicurist → **Company %** → **Admin %**
- **Tips** → 100% to manicurist
- **Expenses** → Deducted from company funds only
- **Net Company Balance** = Company % - Expenses
- **Admin Net Pay** = Admin % (from each appointment)

Commission structures vary by staff member (see Business Context above).

## Project Structure

### Mobile App Structure (mystic-nails-app/)
```
mystic-nails-app/
├── src/
│   ├── types/           # TypeScript type definitions (Clienta, Cita, Servicio, etc.)
│   ├── utils/           # Business logic (commission calculations, formatting)
│   ├── services/        # API integrations (Google Sheets, Calendar, AsyncStorage)
│   ├── constants/       # Theme colors, UI constants, labels
│   ├── models/          # View models (to be created)
│   ├── screens/         # App screens (to be created - see MVP_PLAN.md)
│   ├── navigation/      # React Navigation setup (to be created)
│   ├── components/      # Reusable UI components (to be created)
│   ├── hooks/           # Custom React hooks (to be created)
│   └── context/         # Context providers (to be created)
├── assets/              # Images, icons, fonts
├── app.json            # Expo configuration
└── package.json        # App dependencies
```

### Root Directory Structure
```
├── index.html          # Landing page (marketing website)
├── assets/             # Landing page assets (images, fonts)
├── src/                # Shared types and utilities (legacy, may migrate)
├── data/               # Excel system reference data
├── google-apps-script/ # Backend API for Google Sheets integration
└── mystic-nails-app/   # Mobile app (see above)
```

## Key Files Reference

### Landing Page
- **[index.html](index.html)** - Main landing page (hero, gallery, services, testimonials)
- **[INSTRUCCIONES_DEPLOYMENT.md](INSTRUCCIONES_DEPLOYMENT.md)** - Landing page deployment instructions
- **[deploy.sh](deploy.sh)** - Automated deployment script (Netlify/Vercel)

### Mobile App (in mystic-nails-app/)
- **[mystic-nails-app/src/types/index.ts](mystic-nails-app/src/types/index.ts)** - All TypeScript interfaces and types
- **[mystic-nails-app/src/utils/calculations.ts](mystic-nails-app/src/utils/calculations.ts)** - Commission calculation functions
- **[mystic-nails-app/src/services/googleSheets.ts](mystic-nails-app/src/services/googleSheets.ts)** - Google Sheets integration (placeholder)
- **[mystic-nails-app/src/services/googleCalendar.ts](mystic-nails-app/src/services/googleCalendar.ts)** - Google Calendar integration
- **[mystic-nails-app/src/services/storage.ts](mystic-nails-app/src/services/storage.ts)** - AsyncStorage for offline mode
- **[mystic-nails-app/src/constants/theme.ts](mystic-nails-app/src/constants/theme.ts)** - Colors (black/pink/gold), typography, spacing

### Documentation
- **[MVP_PLAN.md](MVP_PLAN.md)** - Detailed implementation plan (30 tasks, 4 phases)
- **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** - Executive summary of initialization
- **[README.md](README.md)** - Project overview and quick start
- **[google-apps-script/Code.gs](google-apps-script/Code.gs)** - Google Apps Script for Sheets API
- **[google-apps-script/README.md](google-apps-script/README.md)** - Instructions for deploying Apps Script

## Google Apps Script Setup

The project includes a Google Apps Script (`google-apps-script/Code.gs`) that exposes REST endpoints for Google Sheets integration.

**To deploy:**
1. Create Apps Script project at https://script.google.com
2. Copy `Code.gs` content
3. Replace `TU_SPREADSHEET_ID_AQUI` with actual Sheet ID
4. Deploy as Web App (access: "Anyone")
5. Copy URL to `mystic-nails-app/src/services/googleSheets.ts`

See `google-apps-script/README.md` for detailed instructions.

## Testing Strategy

**Landing Page:**
- Test responsive design on mobile, tablet, and desktop
- Verify all WhatsApp links work correctly
- Test navigation and form interactions
- Validate deployment to Netlify/Vercel

**Mobile App:**
- Use Expo Go for rapid testing on physical devices
- Test on both iOS and Android simultaneously
- Test offline mode with AsyncStorage
- Verify Google Calendar sync functionality
- Test commission calculations with various scenarios

**Important:** Always test on physical devices before deploying, as some features (camera, calendar, notifications) don't work in simulators.

## Users/Contacts

- Admin: jgchavezpanduro@gmail.com
- Co-owner (Carolina): 27supercaro@gmail.com
- Business location: Mexico (use MXN currency, Spanish locale)
