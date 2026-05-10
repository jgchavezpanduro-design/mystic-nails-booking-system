# Google Apps Script - Mystic Nails Art

Este script expone endpoints REST para interactuar con Google Sheets desde la app móvil.

## 🚀 Cómo Deployar

### Paso 1: Crear el Script
1. Ve a https://script.google.com
2. Crea un nuevo proyecto
3. Copia el contenido de `Code.gs` en el editor
4. Reemplaza `TU_SPREADSHEET_ID_AQUI` con el ID de tu Google Sheet

### Paso 2: Obtener el Spreadsheet ID
1. Abre tu Google Sheet (Mystic_Nails_Art_Sistema.xlsx)
2. Copia el ID de la URL:
   ```
   https://docs.google.com/spreadsheets/d/SPREADSHEET_ID_AQUI/edit
   ```

### Paso 3: Deployar como Web App
1. En el editor de Apps Script, haz clic en **"Deploy"** → **"New deployment"**
2. Selecciona **"Web app"**
3. Configura:
   - **Description:** "Mystic Nails Art API"
   - **Execute as:** "Me (jgchavezpanduro@gmail.com)"
   - **Who has access:** "Anyone" (importante para evitar problemas de autenticación)
4. Haz clic en **"Deploy"**
5. Copia la **Web app URL** que aparece

### Paso 4: Configurar la App
1. Abre `src/services/googleSheets.ts` en el proyecto Expo
2. Reemplaza `YOUR_APPS_SCRIPT_URL` con la URL que copiaste:
   ```typescript
   const SHEETS_API_BASE_URL = 'https://script.google.com/macros/s/XXXXX/exec';
   ```

## 📡 Endpoints Disponibles

### Clientas
- `GET /clientas` - Lista todas las clientas
- `GET /clientas?id=ID` - Obtiene una clienta específica
- `POST /clientas` - Crea nueva clienta
- `PUT /clientas?id=ID` - Actualiza clienta
- `DELETE /clientas?id=ID` - Elimina clienta

### Servicios
- `GET /servicios` - Lista todos los servicios
- `POST /servicios` - Crea nuevo servicio
- `PUT /servicios?id=ID` - Actualiza servicio
- `DELETE /servicios?id=ID` - Elimina servicio

### Manicuristas
- `GET /manicuristas` - Lista todas las manicuristas
- `POST /manicuristas` - Crea nueva manicurista
- `PUT /manicuristas?id=ID` - Actualiza manicurista
- `DELETE /manicuristas?id=ID` - Elimina manicurista

### Citas
- `GET /citas?mes=5&anio=2026` - Lista citas del periodo
- `GET /citas?id=ID` - Obtiene una cita específica
- `POST /citas` - Crea nueva cita
- `PUT /citas?id=ID` - Actualiza cita
- `DELETE /citas?id=ID` - Elimina cita

### Compras
- `GET /compras?mes=5&anio=2026` - Lista compras del periodo
- `POST /compras` - Crea nueva compra

### Google Calendar
- `POST /calendar/create-event` - Crea evento en Google Calendar e invita a admin y técnica

  **Body:**
  ```json
  {
    "clientName": "Maria Lopez",
    "clientPhone": "+52 984 XXX XXXX",
    "technician": "Carolina",
    "service": "Gelish",
    "date": "2026-05-15",
    "startTime": "14:00",
    "durationMinutes": 90,
    "includeRemoval": false,
    "specialRequests": "Nail art requested"
  }
  ```

  **Respuesta:**
  ```json
  {
    "success": true,
    "data": {
      "success": true,
      "eventId": "xxx",
      "message": "Event created successfully",
      "guests": ["admin@email.com", "technician@email.com"]
    }
  }
  ```

## 🧪 Testing

### Probar con Curl
```bash
# Obtener clientas
curl "https://script.google.com/macros/s/TU_URL/exec?path=clientas"

# Crear clienta
curl -X POST "https://script.google.com/macros/s/TU_URL/exec?path=clientas" \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "Maria Lopez",
    "telefono": "5551234567",
    "tipo": "Local"
  }'
```

### Probar con Postman
1. Crea un nuevo request
2. Método: GET o POST
3. URL: `https://script.google.com/macros/s/TU_URL/exec?path=clientas`
4. Para POST: Agrega body en formato JSON

## 🔧 Troubleshooting

### Error: "Script function not found"
- Verifica que el nombre de la función (`doGet`, `doPost`, etc.) sea correcto
- Verifica que el parámetro `path` esté incluido en la URL

### Error: "You do not have permission"
- Ve a Deploy → Deployments → Edit
- Cambia "Who has access" a "Anyone"
- Redeploya

### Error: "Spreadsheet not found"
- Verifica que el SPREADSHEET_ID sea correcto
- Verifica que el Sheet esté compartido con tu cuenta de Google

## 📝 Notas Importantes

1. **CORS:** Google Apps Script maneja CORS automáticamente
2. **Rate Limit:** No hay rate limit estricto, pero Google puede limitar si hay demasiadas requests
3. **Autenticación:** "Anyone" permite acceso sin autenticación. Para producción, considera implementar autenticación propia.
4. **IDs:** Los IDs se generan como base64 de timestamp + random

## 🔐 Seguridad

Para producción, considera:
1. Implementar autenticación con API keys
2. Validar datos de entrada
3. Rate limiting
4. HTTPS (ya viene por defecto en Apps Script)

## 📚 Recursos

- [Google Apps Script Documentation](https://developers.google.com/apps-script)
- [Web Apps Guide](https://developers.google.com/apps-script/guides/web)
- [REST API Pattern](https://developers.google.com/apps-script/guides/web#using_web_apps_as_api)
