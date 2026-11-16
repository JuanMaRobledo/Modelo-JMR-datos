#!/usr/bin/env node
// Comprobación estructural e integridad de la publicación V2. No calcula valores ni modifica expedientes.
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import {createHash} from 'node:crypto';
import {gunzipSync} from 'node:zlib';

const dir = path.resolve(process.argv[2] || new URL('../jmr-v2/', import.meta.url).pathname);
const manifest = JSON.parse(fs.readFileSync(path.join(dir, 'biblioteca.json'), 'utf8'));
let contenido;
if (manifest.schemaVersion === 'jmr-biblioteca-gzip-1') {
  assert.equal(manifest.app, 'jmr-v2', 'Manifiesto de otra aplicación');
  assert.match(manifest.sha256 || '', /^[a-f0-9]{64}$/, 'SHA-256 inválido');
  assert.equal(manifest.archive, `biblioteca-${manifest.sha256}.json.gz`, 'Archivo no vinculado al SHA');
  contenido = gunzipSync(fs.readFileSync(path.join(dir, manifest.archive)), {maxOutputLength: 64 * 1024 * 1024});
  assert.equal(createHash('sha256').update(contenido).digest('hex'), manifest.sha256, 'Biblioteca alterada');
} else {
  assert.equal(manifest.schemaVersion, 'jmr-biblioteca-1', 'Formato desconocido');
  contenido = Buffer.from(JSON.stringify(manifest));
}
const libro = JSON.parse(contenido.toString('utf8'));
assert.equal(libro.schemaVersion, 'jmr-biblioteca-1');
assert.equal(libro.app, 'jmr-v2', 'Biblioteca de otra aplicación');
assert.ok(libro.files && typeof libro.files === 'object' && !Array.isArray(libro.files));
const catalogo = libro.files['catalogo.json'];
assert.equal(catalogo?.schemaVersion, 'jmr-v2-catalogo-1', 'Catálogo V2 inválido');
assert.ok(Array.isArray(catalogo.empresas) && catalogo.empresas.length > 0, 'Catálogo vacío');
const tickers = new Set();
for (const empresa of catalogo.empresas) {
  const ticker = empresa.ticker;
  assert.match(ticker || '', /^[A-Z0-9.-]{1,18}$/, 'Ticker inválido');
  assert.ok(!tickers.has(ticker), `Ticker duplicado: ${ticker}`);
  tickers.add(ticker);
  assert.equal(empresa.archivo, `empresas/${ticker}.json`, `Ruta incorrecta: ${ticker}`);
  assert.equal(libro.files[empresa.archivo]?.ticker, ticker, `Expediente ausente o incoherente: ${ticker}`);
  const analisis = libro.files[`analisis/${ticker}.json`];
  if (analisis) assert.equal(analisis.ticker, ticker, `Análisis incorrecto: ${ticker}`);
}
for (const ruta of Object.keys(libro.files)) {
  assert.match(ruta, /^(?:catalogo\.json|(?:empresas|analisis)\/[A-Z0-9.-]{1,18}\.json)$/, `Ruta extraña: ${ruta}`);
  if (ruta !== 'catalogo.json') assert.ok(tickers.has(ruta.split('/')[1].slice(0,-5)), `Archivo fuera del catálogo: ${ruta}`);
}
console.log(`V2 íntegra: ${catalogo.empresas.length} empresas, ${Object.keys(libro.files).length} archivos, formato ${manifest.schemaVersion}.`);
