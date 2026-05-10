const XLSX = require('xlsx');
const fs = require('fs');

// Read the Excel file
const workbook = XLSX.readFile('./data/Mystic_Nails_Art_Sistema.xlsx');

// Get all sheet names
const sheetNames = workbook.SheetNames;

console.log('📊 SHEETS FOUND:', sheetNames);
console.log('\n' + '='.repeat(80) + '\n');

// Analyze each sheet
const analysis = {};

sheetNames.forEach(sheetName => {
  const worksheet = workbook.Sheets[sheetName];
  const data = XLSX.utils.sheet_to_json(worksheet, { header: 1 });

  console.log(`📋 SHEET: "${sheetName}"`);
  console.log(`   Total rows: ${data.length}`);
  console.log(`   Total columns: ${data[0] ? data[0].length : 0}`);

  if (data.length > 0) {
    // Headers are usually the first row
    const headers = data[0];
    console.log(`   📌 Columns:`, headers);

    // Show first few data rows
    console.log(`   📄 Sample data (first 3 rows):`);
    const sampleRows = data.slice(1, 4);
    sampleRows.forEach((row, idx) => {
      console.log(`      Row ${idx + 1}:`, row);
    });
  }

  console.log('\n' + '='.repeat(80) + '\n');

  analysis[sheetName] = {
    rowCount: data.length,
    colCount: data[0] ? data[0].length : 0,
    headers: data[0] || [],
    sampleData: data.slice(1, 4)
  };
});

// Save analysis to JSON
fs.writeFileSync('./data/excel-analysis.json', JSON.stringify(analysis, null, 2));
console.log('✅ Analysis saved to: ./data/excel-analysis.json');
