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
  // Método A no usa el contador histórico de 21 celdas: rechazar que
  // un múltiplo prioritario OK se convierta en N/D sin matriz.
  r.sensibilidadMultiples.matrices[0].estado = 'N/D';
  r.sensibilidadMultiples.matrices[0].matriz = null;
  assert.throws(() => validateRecord(r), assert.AssertionError);
});

test('rechaza MOS sobre el ponderado', () => {
  const r = record();
  r.precioMOS = r.valorPrincipal * (1 - r.mos) + 1;
  assert.throws(() => validateRecord(r), /MOS no corresponde a DCF Base/);
});

test('rechaza cifras ausentes aunque el texto diga OK', () => {
  const r = record();
  // Faltante en una cuadrícula 5x5 Base declarada OK.
  r.sensibilidadMultiples.matrices[0].matriz[2][2] = null;
  assert.throws(() => validateRecord(r), /matriz numérica 5x5/);
});

// Caso sintético del contrato SOTP: no restaurar empresas archivadas a producción.
function holding() {
  // Usar el expediente histórico FCFE (contrato anterior), no etiquetar
  // un registro A-1.2 industrial como SOTP sintético.
  const vp = catalog.valoraciones.find(p => /^valoraciones\/XP-/.test(p));
  assert.ok(vp, 'XP histórico necesario para el caso SOTP');
  const r = read(vp);
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
