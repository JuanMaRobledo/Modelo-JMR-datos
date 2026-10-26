'use strict';
const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const {validateRecord} = require('../auditar_integridad.cjs');

const root = path.resolve(__dirname, '../..');
const read = file => JSON.parse(fs.readFileSync(path.join(root, file), 'utf8'));
const catalog = read('catalogo.json');
// Seguir el catálogo: una recaptura cambia el nombre, pero conserva el contrato.
// Cada prueba recibe una copia para no compartir las mutaciones negativas.
function record() {
  const file = catalog.valoraciones.find(file => /^valoraciones\/NKE-/.test(file));
  assert.ok(file, 'NKE debe estar en el catálogo de prueba');
  return read(file);
}

test('acepta cálculo con advertencias económicas', () => {
  const r = record();
  assert.ok(r.salvedades.length > 0);
  assert.doesNotThrow(() => validateRecord(r));
});

test('rechaza contar celdas N/D como matrices', () => {
  const r = record();
  r.sensibilidadMultiples.noDisponibles = 255;
  assert.throws(() => validateRecord(r), assert.AssertionError);
});

test('rechaza MOS sobre el ponderado', () => {
  const r = record();
  r.precioMOS = r.valorPresentePonderado.base * (1 - r.mos);
  assert.throws(() => validateRecord(r), /MOS diferente/);
});

test('rechaza cifras ausentes aunque el texto diga OK', () => {
  const r = record();
  const active = r.descuentoMultiples.metodos.find(m => m.peso > 0);
  assert.ok(active);
  active.base.vp[2] = null;
  assert.throws(() => validateRecord(r), /sin cifras/);
});

// Caso sintético del contrato SOTP: no restaurar empresas archivadas a producción.
function holding() {
  const r = record();
  r.ticker = 'TEST-HOLDING';
  r.metodoPrincipal = 'SOTP';
  r.valorPrincipal = 100;
  r.precioMOS = 100 * (1 - r.mos);
  r.valoracionHolding = {
    nav: {base: 100},
    umbralMOS: r.precioMOS,
    metodos: [{nombre: 'SOTP', peso: 1}, {nombre: 'DCF opcional pendiente', peso: 0}],
  };
  delete r.descuentoMultiples;
  return r;
}

test('SOTP no depende de la aprobación del DCF opcional', () => {
  assert.doesNotThrow(() => validateRecord(holding()));
});

test('SOTP rechaza dar peso al DCF opcional', () => {
  const r = holding();
  r.valoracionHolding.metodos[1].peso = 0.1;
  assert.throws(() => validateRecord(r), assert.AssertionError);
});
