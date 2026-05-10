#!/usr/bin/env node

/**
 * Script automatizado para deployar Google Apps Script
 * Mystic Nails Art - Calendar Integration
 *
 * Este script:
 * 1. Te autentica con Google (una sola vez)
 * 2. Crea el proyecto de Apps Script
 * 3. Sube el código
 * 4. Hace el deploy como Web App
 * 5. Obtiene la URL y actualiza index.html
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const SPREADSHEET_ID = '1nHvkLYt4jk2jRF_hoWKHN4Dn6lXZ3k06cy8hfN69U0Y';
const SCRIPT_CODE_PATH = path.join(__dirname, 'google-apps-script', 'Code.gs');
const INDEX_HTML_PATH = path.join(__dirname, 'index.html');

console.log('🚀 Mystic Nails Art - Auto Deploy Script\n');
console.log('═══════════════════════════════════════════════\n');

// Paso 1: Verificar archivos
console.log('📂 Paso 1: Verificando archivos...');
if (!fs.existsSync(SCRIPT_CODE_PATH)) {
  console.error('❌ Error: No se encontró el archivo Code.gs');
  process.exit(1);
}
console.log('✅ Archivo Code.gs encontrado');

// Paso 2: Verificar autenticación
console.log('\n🔐 Paso 2: Verificando autenticación con Google...');
try {
  const listResult = execSync('clasp list', { encoding: 'utf8' });
  console.log('✅ Ya estás autenticado');
} catch (error) {
  console.log('⚠️  Necesitas autenticarte');
  console.log('📝 Se abrirá un navegador para que inicies sesión\n');
  try {
    execSync('clasp login', { stdio: 'inherit' });
    console.log('✅ Autenticación exitosa');
  } catch (error) {
    console.error('❌ Error en autenticación:', error.message);
    process.exit(1);
  }
}

// Paso 3: Crear proyecto
console.log('\n📝 Paso 3: Creando proyecto de Apps Script...');
try {
  // Verificar si ya existe un proyecto .clasp.json
  if (fs.existsSync(path.join(__dirname, '.clasp.json'))) {
    console.log('⚠️  Ya existe un proyecto .clasp.json');
    console.log('📂 Contenido:');
    const claspConfig = JSON.parse(fs.readFileSync(path.join(__dirname, '.clasp.json'), 'utf8'));
    console.log(`   - Script ID: ${claspConfig.scriptId}`);
  } else {
    console.log('🆕 Creando nuevo proyecto...');
    execSync('clasp create --title "Mystic Nails Booking System" --type "sheets"', { stdio: 'inherit' });
    console.log('✅ Proyecto creado');
  }
} catch (error) {
  console.log('⚠️  Error creando proyecto, puede que ya exista');
}

// Paso 4: Subir código
console.log('\n📤 Paso 4: Subiendo código a Google Apps Script...');
try {
  execSync(`clasp push`, { stdio: 'inherit' });
  console.log('✅ Código subido exitosamente');
} catch (error) {
  console.error('❌ Error subiendo código:', error.message);
  process.exit(1);
}

// Paso 5: Hacer deploy
console.log('\n🚀 Paso 5: Creando deployment como Web App...');
console.log('⏳ Esto puede tomar 30-60 segundos...\n');

try {
  // Hacer el deploy
  const deployResult = execSync('clasp deploy', { encoding: 'utf8' });
  console.log('✅ Deploy creado');
  console.log('📋 Output:', deployResult);

  // Obtener el deployment ID
  const deployments = execSync('clasp deployments', { encoding: 'utf8' });
  console.log('\n📦 Deployments activos:');
  console.log(deployments);

  // Extraer el script ID del .clasp.json
  const claspConfig = JSON.parse(fs.readFileSync(path.join(__dirname, '.clasp.json'), 'utf8'));
  const scriptId = claspConfig.scriptId;

  // Construir la URL del Web App
  const webAppUrl = `https://script.google.com/macros/s/${scriptId}/exec`;

  console.log('\n✅ ¡DEPLOY COMPLETADO!\n');
  console.log('═══════════════════════════════════════════════\n');
  console.log('📋 URL del Web App:');
  console.log(`🔗 ${webAppUrl}\n`);

  // Paso 6: Actualizar index.html
  console.log('📝 Paso 6: Actualizando index.html...');
  let indexHtml = fs.readFileSync(INDEX_HTML_PATH, 'utf8');
  const oldUrl = "const GOOGLE_SCRIPT_URL = 'YOUR_APPS_SCRIPT_URL_HERE';";
  const newUrl = `const GOOGLE_SCRIPT_URL = '${webAppUrl}';`;

  if (indexHtml.includes(oldUrl)) {
    indexHtml = indexHtml.replace(oldUrl, newUrl);
    fs.writeFileSync(INDEX_HTML_PATH, indexHtml);
    console.log('✅ index.html actualizado con la URL');
  } else if (indexHtml.includes(webAppUrl)) {
    console.log('✅ index.html ya tiene la URL correcta');
  } else {
    console.log('⚠️  No se encontró la línea de GOOGLE_SCRIPT_URL en index.html');
    console.log('📝 Por favor actualiza manualmente la línea:');
    console.log(`   const GOOGLE_SCRIPT_URL = '${webAppUrl}';`);
  }

  console.log('\n✨ ¡TODO LISTO!\n');
  console.log('📋 Próximos pasos:');
  console.log('   1. Abre tu landing page (index.html)');
  console.log('   2. Haz una prueba de booking');
  console.log('   3. Verifica que se cree el evento en Google Calendar');
  console.log('   4. Verifica que admin y la técnica reciban la invitación\n');

} catch (error) {
  console.error('❌ Error en deploy:', error.message);
  process.exit(1);
}
