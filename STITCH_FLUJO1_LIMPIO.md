# 📱 FLUJO 1: CREATE APPOINTMENT SCREEN
## Prompt para Stitch - Copiar y Pegar

```
Design a mobile app screen for "Create Appointment" in a natural beauty nail salon management app called "Mystic Nails Art".

CONTEXT:
- Target user: Nail technician in Mexico
- Used while working on clients (one-handed operation)
- Light mode theme with earth tones (beige background with coffee accents)

SCREEN LAYOUT:

HEADER:
- Back button "<" (24px) on left
- Title: "Nueva Cita" (20px, Medium) centered
- "Cancelar" button (16px, coffee color text) on right

FORM FIELDS (vertical stack, top to bottom):

1. DATE INPUT:
   - Label: "Fecha *" (16px, Medium, coffee color #8B6F5C)
   - Input field: 56px height, white background (#FFFFFF), rounded corners 8px
   - Text: "1 de Mayo de 2026" (16px, Regular, coffee dark #5E4A3E)
   - Calendar icon on right (20px)
   - Full width minus 32px margins

2. TIME INPUT:
   - Label: "Hora *" (16px, Medium, coffee color #8B6F5C)
   - Input field: Same style as date
   - Text: "10:00 AM"
   - Clock icon on right (20px)

3. CLIENTA INPUT:
   - Label: "Clienta *" (16px, Medium, coffee color #8B6F5C)
   - Search bar: 56px height, pill shape (rounded 28px), white background
   - Search icon on left (20px)
   - Placeholder: "🔍 Buscar o crear..." (16px, beige gray #C4B5A5)
   - "+" button on right (32px, coffee background #8B6F5C)

4. MANICURISTA DROPDOWN:
   - Label: "Manicurista *" (16px, Medium, coffee color #8B6F5C)
   - Dropdown: 56px height, white background, rounded 8px
   - Placeholder: "Seleccionar clienta primero..." (beige gray #C4B5A5, disabled state)
   - Chevron "▼" on right (16px)

5. SERVICIO DROPDOWN:
   - Label: "Servicio *" (16px, Medium, coffee color #8B6F5C)
   - Same style as manicurista dropdown

6. SERVICIOS EXTRA (optional):
   - Link button: "[+ Agregar servicio]" (16px, coffee color text)
   - Below service dropdown

SUMMARY CARD (below form fields):
- Background: #D4C4B5 (beige medio)
- Rounded corners: 12px
- Padding: 16px
- Title: "RESUMEN" (12px, Medium, coffee medium #8B7462)
- Content:
  * Subtotal: $0 (16px, Regular, coffee dark #5E4A3E)
  * Descuento: $0 (16px, Regular, editable input)
  * Total: $0 (20px, Bold, gold/earth #C9A87F)
  * Divider line
  * Comisión breakdown (14px, Regular, coffee medium #8B7462):
    - Comisión (Carolina): $0 (0%)
    - Empresa: $0 (0%)
    - Admin: $0 (0%)

NOTAS FIELD (optional):
- Label: "Notas (opcional)" (16px, Medium, coffee medium #8B7462)
- Textarea: Min height 80px, max 120px, white background, rounded 8px
- Placeholder: "Alergias, preferencias, etc." (16px, beige gray #C4B5A5)

CTA BUTTON (bottom, fixed):
- Text: "GUARDAR CITA" (16px, Medium, white)
- Height: 56px, full width
- Background: #8B6F5C (coffee)
- Rounded corners: 8px
- Disabled state: Beige medium #D4C4B5 (until all required fields are filled)

COLOR PALETTE (importante - usa estos colores exactos):
- Background: #E8DDD4 (beige muy claro) - Main screen background
- Inputs: #FFFFFF (white) - Input field backgrounds
- Primary CTA: #8B6F5C (coffee) - "Guardar Cita" button
- Labels: #8B6F5C (coffee) - Field labels with asterisk
- Text headings: #5E4A3E (coffee dark) - Client name, service name
- Text body: #8B7462 (coffee medium) - Secondary information
- Text captions: #B1A093 (beige gray) - Notes, descriptions
- Border (focused): #8B6F5C (coffee, 2px) - Input border when focused
- Border (default): #C4B5A5 (beige gray) - Input border default
- Price/Total: #C9A87F (gold/earth) - Summary total amount
- Disabled button: #D4C4B5 (beige medium) - CTA when form incomplete

DESIGN STYLE:
- Natural beauty aesthetic (light mode con tonos tierra, minimalist, elegant)
- High contrast for readability (WCAG AA compliance)
- Card-based UI with rounded corners (8px standard, 12px for summary)
- Thumb-friendly zone: All inputs in bottom half of screen
- One-handed operation optimized
- Color palette: Beige (#E8DDD4), Coffee (#8B6F5C), Gold/Earth (#C9A87F)

INTERACTIONS:
- Tap date/time input → Open picker modal
- Tap clienta search → Open search modal
- Tap manicurista/servicio dropdown → Open bottom sheet with options
- Real-time calculation: Update summary card as user selects services
- Tap CTA → Validate and save appointment
```

---

## 🎨 PALETA DE COLORES RÁPIDA

Para referencia visual mientras diseñas:

```css
Background: #E8DDD4 (beige muy claro)
Inputs: #FFFFFF (blanco)
Primary button: #8B6F5C (café)
Gold/Money: #C9A87F (dorado/tierra)
Text headings: #5E4A3E (café oscuro)
Text body: #8B7462 (café medio)
Text captions: #B1A093 (beige gris)
Borders: #C4B5A5 (beige gris)
```

---

## 📋 Instrucciones

1. **Copia** todo el código entre las comillas `` `...` `` arriba
2. **Abre** Stitch (o tu herramienta de diseño AI)
3. **Pega** el prompt completo
4. **Genera** el diseño
5. **Refina** si es necesario

---

## ✅ Qué debe incluir el diseño

- [ ] Background beige claro (#E8DDD4)
- [ ] Inputs blancos (#FFFFFF)
- [ ] Botón "GUARDAR CITA" en café (#8B6F5C)
- [ ] Labels en café (#8B6F5C)
- [ ] Texto headings en café oscuro (#5E4A3E)
- [ ] Resumen con precio en dorado (#C9A87F)
- [ ] Tarjeta de resumen en beige medio (#D4C4B5)
- [ ] Espaciado para una mano (todo en mitad inferior)
- [ ] Bordes redondeados (8px)
- [ ] Sombras sutiles

---

## 🎯 Resultado esperado

Un diseño limpio, natural y orgánico con:
- Fondo beige claro acogedor
- Inputs blancos prominentes
- Botones café que contrasten
- Texto café oscuro legible
- Precios destacados en dorado
- Sensación de spa/salón boutique
