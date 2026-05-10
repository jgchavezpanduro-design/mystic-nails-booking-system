Eres un arquitecto de productos y lead developer especializado en apps móviles para pequeños negocios de belleza (nail studios). 

El cliente tiene un estudio privado de uñas llamado **Mystic Nails Art** en México (moneda: MXN). Actualmente maneja todo con Google Sheets + Google Calendar + un panel web simple. Quiere migrar a una **aplicación móvil nativa o PWA** (prioridad alta en usabilidad desde smartphone) que funcione offline cuando sea posible y se sincronice con Google Drive/Sheets y Google Calendar.

### Contexto actual (del Excel/Sheets adjunto):
- Hay un Dashboard mensual.
- Hojas principales: Dashboard, Citas, Clientas, Servicios, Manicuristas, Compras, Liquidaciones, Configuración.
- Precios diferenciales: la mayoría de servicios tienen **precio Local** vs **precio Extranjera** (excepto Pedicure, que es el mismo).
- Comisiones variables por manicurista:
  - Carolina (co-owner): 80% para ella, 15% Empresa, 5% Admin.
  - Monse: 40% para ella, 35% Empresa, 25% Admin.
  - Manicurista 3: similar a Monse o modelo mixto (sueldo fijo semanal de $1200 + 25% comisión → ajustar reparto a 45% Mystic Nails / 30% Admin).
- Se calcula: Ingresos brutos, comisiones a manicuristas, % Empresa, % Admin (tú), propinas (100% a manicurista), descuentos, compras/gastos que restan del fondo de empresa, saldo neto, pago neto al admin.
- Campos clave por cita: Fecha, Hora, Clienta, Manicurista, Servicio, Detalle del servicio, Tiempo estimado, Estado (confirmada, completada, cancelada, no-show), Descuento, Tipo clienta (Local/Extranjera), Teléfono, Instagram, Método de pago (efectivo/transferencia), Depósito, Monto pagado, Propina, Notas.

### Objetivo de la App
Crear una app móvil (Flutter recomendado por cross-platform iOS/Android + buena integración con Google) o PWA que reemplace y mejore el flujo actual. Debe ser **simple, rápida y visual** (muchas fotos de uñas, colores elegantes tipo negro/rosa/dorado).

### Requerimientos Funcionales (User Stories principales)

**1. Autenticación y Roles**
- Login con cuenta Google (usando el calendario jgchavezpanduro@gmail.com y compartir con 27supercaro@gmail.com).
- Roles: Admin (tú) y Manicuristas (lectura/escritura limitada).

**2. Maestros / Catálogos (CRUD)**
- **Clientas**: Nombre, Teléfono, Instagram, Tipo (Local/Extranjera), Fecha de cumpleaños, Cómo te encontró, Alergias/Notas, Historial de visitas, Fotos de trabajos anteriores (link a Drive o subida directa).
- **Servicios**: Nombre, Descripción, Duración (minutos), Precio Local, Precio Extranjera, Categoría (Mani, Pedi, etc.). Pedicure sin diferencia de precio.
- **Manicuristas**: Nombre, % comisión (o modelo mixto fijo + %), Teléfono, Foto, Activa/Inactiva, Notas.
- **Compras/Gastos**: Fecha, Concepto/Categoría, Monto, Notas (restan del fondo de empresa).

**3. Agenda y Citas (core de la app)**
- Vista de calendario (mensual/semanal/día) sincronizada bidireccional con **Google Calendar**.
- Crear/Editar/Cancelar cita: seleccionar clienta (búsqueda rápida), manicurista, servicio(s), hora, duración, tipo clienta (auto-precio), descuento, depósito, notas.
- Mostrar en tiempo real: precio total, desglose de comisión (según manicurista), % Empresa, % Admin, propina estimada.
- Estados de cita + razones de cancelación/no-show.
- Recordatorios automáticos (push notifications 24h y 1h antes).
- Vista "Próximas 7 días" y "Hoy".

**4. Registro de Citas Completadas (Fin de servicio)**
- Marcar como completada → registrar propina real, método de pago, monto final pagado, descuento aplicado.
- Cálculo automático de reparto (comisión manicurista + empresa + admin).
- Foto del trabajo terminado (subir a Drive o storage de la app).

**5. Finanzas y Reportes**
- Dashboard mensual (como el actual): Citas totales, Ingresos brutos, Comisiones pagadas, Compras, Saldo neto empresa, Tu pago neto (admin), Promedio por cita, Propinas del mes, Cancelaciones/No-shows.
- Liquidaciones por manicurista (cuánto se les debe este mes).
- Reportes filtrables por mes/año, por manicurista, por clienta.
- Historial de retención de clientas.

**6. Otras funcionalidades**
- Búsqueda rápida de clientas y servicios.
- Notificaciones push.
- Modo offline (guardar localmente y sincronizar cuando vuelva internet).
- Exportar reportes a PDF/Excel.
- Inventario básico opcional (productos que se usan).

### Recomendaciones Técnicas que debes incluir en el diseño:
- **Backend ligero**: Google Sheets como base de datos inicial (vía Google Apps Script + Webhooks o API personalizada) + Google Calendar API. En el futuro migrar a Firebase o Supabase si crece.
- **Autenticación**: Google Sign-In + Firebase Auth.
- **Sincronización**: Bidireccional con Calendar. Escritura automática en hoja "Citas" del Sheets.
- **UI/UX**: Diseño limpio, mobile-first, dark/light mode, mucho uso de tarjetas e imágenes. Fácil de usar con una mano.
- **Seguridad**: Solo los usuarios autorizados ven datos financieros.

### Otras recomendaciones que propongo agregar:
- Tracking de retención (última visita, frecuencia).
- Loyalty / Cumpleaños (alertas y promos).
- Portafolio de fotos por clienta.
- Análisis simple de "cómo te encontró" para marketing.
- Posibilidad de que clientas reserven por WhatsApp o link público (futuro).
- Cierre de caja diario/semanal (comparar efectivo vs sistema).

---

**Tarea para ti (desarrollador):**
1. Analiza el archivo adjunto **Mystic_Nails_Art_Sistema - Dashboard.csv** (y el Google Sheet completo) para extraer la lógica exacta de cálculos de precios y comisiones.
2. Define la **arquitectura completa** (frontend, backend, sincronización).
3. Crea los **maestros (Data Models)** en código: Clienta, Cita, Servicio, Manicurista, Compra, etc. (incluye todos los campos necesarios).
4. Propón el stack tecnológico recomendado (Flutter + Firebase/Apps Script o alternativa).
5. Diseña los flujos principales con wireframes o descripción detallada de pantallas.
6. Prioriza MVP: Agenda + Crear cita + Dashboard básico + Maestros.

Pregúntame cualquier duda para refinar. El objetivo es tener una app usable en 4-6 semanas que mejore mucho la experiencia actual desde el teléfono.

Adjunta el archivo CSV/Sheets actual para referencia.