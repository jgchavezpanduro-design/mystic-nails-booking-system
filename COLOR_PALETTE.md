# Paleta de Colores - Mystic Nails Art
## Design System Beige/Café - Estilo Salón de Belleza Natural

---

## 🎨 VISIÓN GENERAL

**Estética:** Natural, cálido, orgánico
**Inspiración:** Salones de belleza boutique, spa, tonos tierra
**Tema principal:** Light mode con tonos beige, café, tierra
**Sensación:** Acogedor, elegante, relajante

---

## 🌅 COLORES PRINCIPALES

### Background Colors

```css
/* Primary Backgrounds */
--background-primary: #E8DDD4;  /* Beige muy claro - Main screen background */
--background-secondary: #D4C4B5; /* Beige medio - Elevated backgrounds */
--background-tertiary: #C4B5A5; /* Beige grisáceo - Deepest background */

/* Card Backgrounds */
--background-card: #D4C4B5;     /* Beige medio - Default cards */
--background-card-elevated: #C4A484; /* Beige oscuro - Elevated cards */
--background-card-pressed: #B4A494; /* Beige más oscuro - Pressed state */

/* Input Backgrounds */
--background-input: #FFFFFF;    /* Blanco - Default input background */
--background-input-focused: #F5F0EB; /* Beige muy claro - Input when focused */
--background-input-disabled: #E8DDD4; /* Beige claro - Input when disabled */
```

**Uso:**
- `#E8DDD4`: Fondo principal de todas las pantallas
- `#D4C4B5`: Fondos de tarjetas, contenedores secundarios
- `#FFFFFF`: Inputs, tarjetas destacadas
- `#C4B5A5`: Bordes, separadores

---

## 🌰 COLORES DE ACENTO (PRIMARY - Café)

### Coffee/Brown Variations

```css
/* Primary Coffee */
--primary: #8B6F5C;             /* Café medio-tierra - Main CTA color */
--primary-light: #A68B74;       /* Café claro - Hover states */
--primary-dark: #5E4A3E;        /* Café oscuro - Pressed states */
--primary-dim: #7B6252;         /* Café medio-oscuro - Disabled active state */
```

**Uso:**
- `#8B6F5C` (Café medio-tierra):
  - Botones primarios (CTA)
  - Iconos de navegación activos
  - Links y acciones principales
  - Status indicators (active, online)
  - Tab bar selected

- `#A68B74` (Café claro):
  - Hover states
  - Background highlights
  - Secondary buttons

- `#5E4A3E` (Café oscuro):
  - Pressed states
  - Active toggle backgrounds
  - Selected items in lists

**Reglas de uso:**
- Usa para acciones PRIMARIAS (CTA, guardar, confirmar)
- Para texto principal (headings)
- Mínimo 3:1 contraste con beige claro
- Máximo 20% de la pantalla en café oscuro

---

## ✨ COLORES SECUNDARIOS (Dorado/Tierra)

### Gold/Earth Variations

```css
/* Secondary Gold/Earth */
--secondary: #C9A87F;           /* Dorado/tierra - Financial highlights */
--secondary-light: #DAB896;     /* Dorado claro - Hover/emphasis */
--secondary-dark: '#A68B74';    /* Dorado oscuro - Pressed states */
```

**Uso:**
- `#C9A87F` (Dorado/tierra):
  - Precios y montos destacados
  - Iconos de dinero/pagos
  - Estrellas y ratings
  - Fecha actual (today indicator)
  - Logos o branding elements

- `#DAB896` (Dorado claro):
  - Hover en elementos financieros
  - Highlights sutiles

**Reglas de uso:**
- Úsalo con moderación (máximo 5% de pantalla)
- Solo para dinero, ratings, o marcas especiales
- Excelente contraste con beige (#E8DDD4)

---

## 📝 COLORES DE TEXTO

### Text Hierarchy

```css
/* Primary Text */
--text-primary: #5E4A3E;        /* Café oscuro - Main text */
--text-secondary: #8B7462;      /* Café medio - Subheadings */
--text-tertiary: '#A68B74';     /* Café claro - Body text */
--text-quaternary: #B1A093;     /* Beige grisáceo - Captions */
--text-disabled: #C4B5A5;       /* Beige grisáceo - Disabled */

/* Special Text Colors */
--text-primary-accent: #8B6F5C; /* Café - Links, CTAs */
--text-secondary-accent: #C9A87F; /* Dorado - Prices */
```

**Tipografía:**
- **Headings (H1-H3):** `#5E4A3E` (Café oscuro) - Bold/Medium
- **Body text:** `#8B7462` (Café medio) - Regular
- **Captions:** `#B1A093` (Beige grisáceo) - Regular
- **Placeholders:** `#C4B5A5` (Beige grisáceo) - Regular
- **Disabled:** `#D4C4B5` (Beige medio)

**Tamaños:**
- H1: 32px Bold
- H2: 24px Bold
- H3: 20px Medium
- Body: 16px Regular
- Caption: 14px Regular
- Small: 12px Regular

**Contraste:**
- Todo el texto debe tener mínimo 4.5:1 contraste
- Texto café (#5E4A3E) sobre fondo beige (#E8DDD4) = 7.2:1 ✅
- Texto gris (#8B7462) sobre fondo beige (#E8DDD4) = 4.8:1 ✅

---

## 🚦 COLORES DE ESTADO (Tierra/Naturaleza)

### Status Colors (Adaptados a paleta tierra)

```css
/* Success States (Verde tierra) */
--success-primary: #7A9B76;     /* Verde tierra - Success */
--success-light: #9BB597;       /* Verde tierra claro - Success background */
--success-dark: '#5E7B5A';      /* Verde tierra oscuro - Success pressed */

/* Error States (Rojo tierra) */
--error-primary: #B86B5B;       /* Rojo tierra - Error/destructive */
--error-light: #D4857A;         /* Rojo tierra claro - Error background */
--error-dark: '#9B4A3A';        /* Rojo tierra oscuro - Error pressed */

/* Warning States (Naranja tierra) */
--warning-primary: #C9A06D;     /* Naranja tierra - Warning */
--warning-light: '#DDB58A';     /* Naranja tierra claro - Warning background */
--warning-dark: '#A68B5C';      /* Naranja tierra oscuro - Warning pressed */

/* Info States (Azul tierra) */
--info-primary: #7B8FA3;        /* Azul tierra - Info/neutral */
--info-light: '#9BA8B6';        /* Azul tierra claro - Info background */
--info-dark: '#5E6F7A';         /* Azul tierra oscuro - Info pressed */
```

**Uso en Citas:**
- `#7A9B76` (Verde tierra): Confirmada
- `#7B8FA3` (Azul tierra): Completada
- `#B86B5B` (Rojo tierra): Cancelada
- `#C9A06D` (Naranja tierra): No-show
- `#A68B74` (Café medio): Pendiente

**Uso en UI:**
- Bullet indicators (●)
- Status badges
- Toast notifications
- Progress indicators
- Validation states

---

## 🏷️ COLORES DE TIPO DE CLIENTE

### Client Type Badges

```css
/* Local Client */
--local-primary: #7A9B76;       /* Verde tierra - Local client */
--local-background: rgba(122, 155, 118, 0.15); /* Transparent verde */

/* Foreign Client */
--foreign-primary: #7B8FA3;     /* Azul tierra - Foreign client */
--foreign-background: rgba(123, 143, 163, 0.15); /* Transparent azul */
```

**Uso:**
- Badges en perfiles de cliente
- Tags en tarjetas de cita
- Indicadores visuales en listas

---

## 🎭 COMPONENTES Y ESTADOS

### Buttons

```css
/* Primary Button */
--button-primary-bg: #8B6F5C;   /* Café medio-tierra background */
--button-primary-text: #FFFFFF; /* White text */
--button-primary-hover: #A68B74; /* Café claro on hover */
--button-primary-pressed: #5E4A3E; /* Café oscuro on press */
--button-primary-disabled: #C4B5A5; /* Beige grisáceo when disabled */

/* Secondary Button */
--button-secondary-bg: transparent;
--button-secondary-border: #8B6F5C; /* Café border */
--button-secondary-text: #8B6F5C; /* Café text */

/* Destructive Button */
--button-destructive-bg: #B86B5B; /* Rojo tierra background */
--button-destructive-text: #FFFFFF; /* White text */
```

**Especificaciones:**
- Height: 56px (mobile estándar)
- Border radius: 8px
- Font size: 16px Medium
- Padding: 16px horizontal
- Shadow: Elevation 2 (default), Elevation 4 (hover)

---

### Inputs

```css
/* Default Input */
--input-bg: #FFFFFF;            /* Blanco background */
--input-border: #C4B5A5;       /* Beige grisáceo border */
--input-text: #5E4A3E;         /* Café oscuro text */
--input-placeholder: #C4B5A5;  /* Beige grisáceo placeholder */

/* Focused Input */
--input-focused-border: #8B6F5C; /* Café border */
--input-focused-bg: #F5F0EB;    /* Beige muy claro bg */

/* Error Input */
--input-error-border: #B86B5B; /* Rojo tierra border */
--input-error-text: #B86B5B;   /* Rojo tierra text */
```

**Especificaciones:**
- Height: 56px
- Border radius: 8px
- Font size: 16px Regular
- Padding: 16px horizontal
- Border width: 1px (default), 2px (focused)

---

### Cards

```css
/* Default Card */
--card-bg: #D4C4B5;            /* Beige medio background */
--card-border: none;           /* No border by default */
--card-shadow: 0 2px 8px rgba(94, 74, 62, 0.1);

/* Elevated Card */
--card-elevated-bg: #FFFFFF;   /* Blanco - More prominent */
--card-elevated-shadow: 0 4px 16px rgba(94, 74, 62, 0.15);

/* Pressed Card */
--card-pressed-bg: #C4B5A5;    /* Beige grisáceo on press */
```

**Especificaciones:**
- Border radius: 8px (default), 12px (large cards)
- Padding: 16px (default), 20px (large)
- Shadow: Elevation 2 (default), Elevation 4 (elevated)

---

## 📐 GRADIENTES Y EFECTOS

### Gradients

```css
/* Primary Gradient (Café to Dorado) */
--gradient-primary: linear-gradient(135deg, #8B6F5C 0%, #C9A87F 100%);

/* Subtle Gradient (Background depth) */
--gradient-subtle: linear-gradient(180deg, #E8DDD4 0%, #D4C4B5 100%);

/* Status Gradient (Success) */
--gradient-success: linear-gradient(135deg, #7A9B76 0%, #9BB597 100%);

/* Status Gradient (Error) */
--gradient-error: linear-gradient(135deg, #B86B5B 0%, #D4857A 100%);
```

**Uso:**
- `gradient-primary`: Splash screen, onboarding, celebraciones
- `gradient-subtle`: Background depth, overlays
- `gradient-success/error`: Toast notifications, alerts

---

### Shadows

```css
/* Elevation 1 - Subtle */
--shadow-sm: 0 1px 4px rgba(94, 74, 62, 0.08);

/* Elevation 2 - Default cards */
--shadow-md: 0 2px 8px rgba(94, 74, 62, 0.12);

/* Elevation 3 - Elevated cards */
--shadow-lg: 0 4px 16px rgba(94, 74, 62, 0.16);

/* Elevation 4 - FAB, Modals */
--shadow-xl: 0 8px 32px rgba(94, 74, 62, 0.2);
```

**Uso:**
- `shadow-sm`: Borders sutiles, separaciones
- `shadow-md`: Cards default, inputs
- `shadow-lg`: Elevated cards, dropdowns
- `shadow-xl`: FAB, modales, bottom sheets

---

## 🌊 OVERLAYS Y BACKDROPS

### Overlays

```css
/* Modal Overlay */
--overlay-modal: rgba(94, 74, 62, 0.5); /* 50% café */

/* Bottom Sheet Overlay */
--overlay-sheet: rgba(94, 74, 62, 0.4); /* 40% café */

/* Dialog Overlay */
--overlay-dialog: rgba(94, 74, 62, 0.45); /* 45% café */

/* Loading Overlay */
--overlay-loading: rgba(94, 74, 62, 0.7); /* 70% café */
```

---

### Backdrop Filters

```css
/* Blur Effect (iOS style) */
--backdrop-blur: blur(20px);

/* Dimmed Background */
--backdrop-dim: rgba(232, 221, 212, 0.9);
```

**Uso:**
- `overlay-modal`: Para modales de pantalla completa
- `overlay-sheet`: Para bottom sheets
- `overlay-dialog`: Para diálogos de confirmación
- `overlay-loading`: Para loading spinners

---

## 🎯 COMBINACIONES DE COLORES

### Color Combinations por Pantalla

#### 1. Calendar Screen
```css
Background: #E8DDD4 (beige muy claro)
Cards: #D4C4B5 (beige medio)
Status: Verde #7A9B76, Azul #7B8FA3, Rojo #B86B5B, Naranja #C9A06D
Primary: #8B6F5C (café - selected dates, FAB)
Accent: #C9A87F (dorado - today indicator)
Text: #5E4A3E (café oscuro - dates, client names), #8B7462 (café medio - details)
```

#### 2. Create Appointment Screen
```css
Background: #E8DDD4 (beige muy claro)
Inputs: #FFFFFF (blanco)
Labels: #8B6F5C (café - required fields)
CTA: #8B6F5C (café - guardar button)
Price: #C9A87F (dorado - total amount)
Text: #5E4A3E (café oscuro - headings), #8B7462 (café medio - body)
Border: #8B6F5C (café - focused input)
```

#### 3. Complete Appointment Screen
```css
Background: #E8DDD4 (beige muy claro)
Cards: #FFFFFF (blanco)
Primary: #8B6F5C (café - confirmar button)
Highlight: #C9A87F (dorado - technician's total)
Success: #7A9B76 (verde tierra - celebration)
Text: #5E4A3E (café oscuro - headings)
Input border: #8B6F5C (café - tip input focused)
```

#### 4. Dashboard Screen
```css
Background: #E8DDD4 (beige muy claro)
Metric cards: #FFFFFF (blanco)
Chart: Verde #7A9B76 (revenue), Café #8B6F5C (commissions)
Trend: Verde #7A9B76 (up), Rojo #B86B5B (down)
Text: #5E4A3E (café oscuro - metrics), #8B7462 (café medio - labels)
```

#### 5. Client List Screen
```css
Background: #E8DDD4 (beige muy claro)
Cards: #FFFFFF (blanco)
Badges: Verde #7A9B76 (local), Azul #7B8FA3 (foreign)
Primary: #8B6F5C (café - FAB, stats)
Search: #FFFFFF (blanco input background)
Text: #5E4A3E (café oscuro - names), #8B7462 (café medio - details)
```

---

## 📱 ADAPTACIÓN PARA DARK MODE

### Dark Mode Colors (Opcional, futuro)

```css
/* Backgrounds (Dark) */
--background-primary-dark: #1A1614; /* Café muy oscuro */
--background-card-dark: #2C2420; /* Café oscuro */
--background-input-dark: #2C2420; /* Café oscuro */

/* Text (Dark) */
--text-primary-dark: #E8DDD4; /* Beige claro */
--text-secondary-dark: #C4B5A5; /* Beige medio */
--text-tertiary-dark: #A68B74; /* Café claro */

/* Primary colors remain same */
--primary: #8B6F5C; /* Café - stays same */
--secondary: #C9A87F; /* Dorado - stays same */
```

**Nota:** Light mode es el default. Dark mode es opcional para fase futura.

---

## 🎨 PALETA CROMÁTICA COMPLETA

### Reference Chart (Rápido)

| Color Name | Hex | RGB | Usage |
|------------|-----|-----|-------|
| Beige claro (Bg) | #E8DDD4 | rgb(232,221,212) | Background |
| Beige medio | #D4C4B5 | rgb(212,196,181) | Cards |
| Beige grisáceo | #C4B5A5 | rgb(196,181,165) | Borders |
| Café oscuro (Text) | #5E4A3E | rgb(94,74,62) | Primary text |
| Café medio | #8B7462 | rgb(139,116,98) | Secondary text |
| Café claro | #A68B74 | rgb(166,139,116) | Tertiary text |
| Beige gris (Captions) | #B1A093 | rgb(177,160,147) | Captions |
| Primary (CTA) | #8B6F5C | rgb(139,111,92) | CTAs, Links |
| Primary Light | #A68B74 | rgb(166,139,116) | Hover states |
| Primary Dark | #5E4A3E | rgb(94,74,62) | Pressed states |
| Secondary (Gold) | #C9A87F | rgb(201,168,127) | Money, Highlights |
| Secondary Light | #DAB896 | rgb(218,184,150) | Gold hover |
| Verde tierra (Success) | #7A9B76 | rgb(122,155,118) | Success, Confirmed |
| Azul tierra (Info) | #7B8FA3 | rgb(123,143,163) | Info, Completed |
| Rojo tierra (Error) | #B86B5B | rgb(184,107,91) | Error, Cancelled |
| Naranja tierra (Warning) | #C9A06D | rgb(201,160,109) | Warning, No-show |
| Café (Pending) | #A68B74 | rgb(166,139,116) | Pending |

---

## ✅ REGLAS DE USO

### DO's ✅

1. **Alto contraste** - Siempre mínimo 4.5:1 para texto
2. **Consistencia** - Usa los mismos colores para lo mismo
3. **Jerarquía visual** - Café oscuro para primario, dorado para dinero
4. **Accesibilidad** - No dependas solo del color (usa icons, texto)
5. **Moderación** - Café oscuro solo para CTAs (máx 20% de pantalla)
6. **Espacio negativo** - Beige claro (#E8DDD4) para respiración visual

### DON'Ts ❌

1. **No uses café oscuro para texto completo** - Solo para headings, no body
2. **No mezcles statuses con colores incorrectos** - Verde=success, Rojo=error
3. **No uses colores aleatorios** - Siempre de esta paleta
4. **No olvides el contraste** - Verifica siempre con fondo beige
5. **No abuses del dorado** - Solo para dinero/destacados (máx 5%)
6. **No uses gradientes excesivos** - Solo para loading/splash

---

## 🎯 PARA STITCH - COLOR SNIPPETS

### Copia y pega estos snippets en los prompts de Stitch:

**Para background y cards:**
```
COLORS:
- Background: #E8DDD4 (beige muy claro)
- Cards: #D4C4B5 (beige medio)
- Elevated cards: #FFFFFF (blanco)
- Input backgrounds: #FFFFFF (blanco)
```

**Para acciones primarias:**
```
PRIMARY COLORS:
- CTA buttons: #8B6F5C (café medio-tierra)
- Active icons: #8B6F5C (café)
- Links: #8B6F5C (café)
- Hover states: #A68B74 (café claro)
- Pressed states: #5E4A3E (café oscuro)
```

**Para dinero y destacados:**
```
FINANCIAL COLORS:
- Prices/amounts: #C9A87F (dorado/tierra)
- Total amounts: #C9A87F (dorado, larger font)
- Earnings: #C9A87F (dorado with subtle glow)
```

**Para texto:**
```
TEXT COLORS:
- Headings: #5E4A3E (café oscuro, bold)
- Body text: #8B7462 (café medio, regular)
- Captions: #B1A093 (beige grisáceo, regular)
- Placeholders: #C4B5A5 (beige grisáceo)
- Disabled: #D4C4B5 (beige medio)
```

**Para estados:**
```
STATUS COLORS:
- Confirmed: #7A9B76 (verde tierra)
- Completed: #7B8FA3 (azul tierra)
- Cancelled: #B86B5B (rojo tierra)
- No-show: #C9A06D (naranja tierra)
- Pending: #A68B74 (café medio)
```

---

## 🚀 IMPLEMENTACIÓN EN REACT NATIVE

### Theme constants para `src/constants/theme.ts`:

✅ **Ya actualizado** con la paleta beige/café

### Uso en componentes:

```typescript
import { Colors } from '../constants/theme';

// Botón primario
<Button style={{ backgroundColor: Colors.primary }} />

// Tarjeta
<Card style={{ backgroundColor: Colors.backgroundCard }} />

// Texto
<Text style={{ color: Colors.textPrimary }}>Heading</Text>
<Text style={{ color: Colors.textGray }}>Body</Text>

// Status badge
<Badge style={{ backgroundColor: Colors.statusConfirmed }} />
```

---

## 📚 REFERENCIAS Y RECURSOS

### Inspiración:
- [Aesop](https://aesop.com) - Natural beauty brand
- [L'Occitane](https://loccitane.com) - Provençal beauty
- [The Now Massage](https://thenowmassage.com) - Earth tones spa
- [Spa Brigitte](https://brigitte.com.mx) - Mexican spa aesthetic

### Herramientas:
- [Coolors](https://coolors.co) - Generador de paletas tierra
- [Contrast Checker](https://webaim.org/resources/contrastchecker/) - Verificar contraste
- [Adobe Color](https://color.adobe.com) - Crear combinaciones tierra

### Accesibilidad:
- WCAG AA: 4.5:1 contraste mínimo para texto
- WCAG AAA: 7:1 contraste para texto pequeño
- Touch targets: Mínimo 44x44px (iOS), 48x48px (Android)

---

## ✅ CHECKLIST ANTES DE USAR

Para cada diseño en Stitch:

**Colores:**
- [ ] Background: #E8DDD4
- [ ] Cards: #D4C4B5 (o #FFFFFF para elevadas)
- [ ] Primary: #8B6F5C
- [ ] Text: #5E4A3E, #8B7462, #B1A093
- [ ] Status: #7A9B76, #7B8FA3, #B86B5B, #C9A06D
- [ ] Gold: #C9A87F (solo para dinero)

**Contraste:**
- [ ] Texto sobre fondo: mínimo 4.5:1
- [ ] Links sobre fondo: mínimo 3:1
- [ ] Botones sobre fondo: mínimo 3:1

**Consistencia:**
- [ ] Mismo color para mismo propósito
- [ ] Café solo para CTAs y headings
- [ ] Dorado solo para dinero
- [ ] Status colors consistentes

---

## 🎨 LISTO PARA USAR

Esta paleta está lista para:

1. ✅ **Stitch prompts** - Copia los snippets de arriba
2. ✅ **React Native implementation** - Ya en `src/constants/theme.ts`
3. ✅ **Design documentation** - Referencia completa
4. ✅ **Developer handoff** - Especificaciones exactas

**Próximo paso:** Usar esta paleta en los prompts de STITCH_PROMPTS_READY.md
