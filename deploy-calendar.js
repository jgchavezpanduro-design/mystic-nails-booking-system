#!/usr/bin/env node

/**
 * Script automatizado para deployar Google Apps Script
 * Mystic Nails Art - Calendar Integration
 */

const https = require('https');
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const SPREADSHEET_ID = '1nHvkLYt4jk2jRF_hoWKHN4Dn6lXZ3k06cy8hfN69U0Y';
const SCRIPT_CODE_PATH = path.join(__dirname, 'google-apps-script', 'Code.gs');

console.log('🚀 Mystic Nails Art - Google Apps Script Deploy\n');

// Paso 1: Verificar que el archivo existe
console.log('📂 Paso 1: Verificando archivos...');
if (!fs.existsSync(SCRIPT_CODE_PATH)) {
  console.error('❌ Error: No se encontró el archivo Code.gs');
  process.exit(1);
}
console.log('✅ Archivo Code.gs encontrado');

// Paso 2: Leer el código
console.log('\n📖 Paso 2: Leyendo código...');
const code = fs.readFileSync(SCRIPT_CODE_PATH, 'utf8');

// Verificar que el SPREADSHEET_ID esté configurado
if (!code.includes(SPREADSHEET_ID)) {
  console.error('❌ Error: El SPREADSHEET_ID no está configurado correctamente');
  process.exit(1);
}
console.log('✅ Código leído correctamente');
console.log(`   - SPREADSHEET_ID: ${SPREADSHEET_ID}`);
console.log(`   - Tamaño: ${code.length} caracteres`);

// Paso 3: Abrir Google Apps Script en el navegador
console.log('\n🌐 Paso 3: Abriendo Google Apps Script...');
console.log('📋 INSTRUCCIONES:\n');
console.log('Se abrirá Google Apps Script en tu navegador.');
console.log('Por favor sigue estos pasos:\n');
console.log('1. Clic en "New project"');
console.log('2. Borra el código de ejemplo');
console.log('3. Copia y pega el código que está en: google-apps-script/Code.gs');
console.log('4. Guarda el proyecto (⌘+S / Ctrl+S)');
console.log('5. Clic en "Deploy" → "New deployment"');
console.log('6. Selecciona "Web app"');
console.log('7. Configura:');
console.log('   - Description: "Mystic Nails Booking API"');
console.log('   - Execute as: "Me"');
console.log('   - Who has access: "Anyone"');
console.log('8. Clic en "Deploy"');
console.log('9. Autoriza los permisos (Google Sheets + Calendar)');
console.log('10. Copia la URL del Web App');
console.log('\n⏳ Abriendo navegador...');

// Abrir Google Apps Script
try {
  execSync('open https://script.google.com', { stdio: 'inherit' });
} catch (error) {
  console.log('❌ No se pudo abrir el navegador automáticamente');
  console.log('🔗 Abre manualmente: https://script.google.com');
}

console.log('\n\n⚠️  IMPORTANTE:');
console.log('Cuando tengas la URL del Web App (se ve así:)');
console.log('   https://script.google.com/macros/s/AKfycbxXXXXX/exec');
console.log('\nEjecuta este comando para actualizar index.html:');
console.log(`   node update-script-url.js "PEGAR_AQUI_LA_URL"`);

console.log('\n📚 Necesitas ayuda? Revisa: INSTRUCCIONES_GOOGLECalendar.md\n');
