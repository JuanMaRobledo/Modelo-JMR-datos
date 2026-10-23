'use strict';
const fs = require('node:fs');
const path = require('node:path');
const test = require('node:test');
const assert = require('node:assert/strict');

const root = path.resolve(__dirname, '../..');
const read = p => JSON.parse(fs.readFileSync(path.join(root, p), 'utf8'));

test('NKE R3: catálogo, libro, artículo, auditoría y manifiesto usan una revisión', () => {
  const cat = read('catalogo.json');
  const rel = read('evidencia/NKE-20261023-R3/release.json');
  const fase = read('documentos/NKE-20261023-R3/fases_ejecucion.json');
  const file = cat.valoraciones.find(p => p.startsWith('valoraciones/NKE-'));
  assert.ok(file, 'No hay valoración NKE vigente en catálogo');
  const val = read(file);
  const an = cat.analisis.find(p => p.startsWith('analisis/NKE-'));
  assert.ok(an, 'No hay análisis NKE vigente');
  const analisis = read(an);
  for (const ref of [val, rel, fase, analisis]) {
    assert.equal(ref.revisionId, 'NKE-JMR-20261023-R3');
  }
  assert.equal(val.reviewManifest.resultsSha256, rel.resultsSha256);
  assert.equal(fase.resultsSha256, rel.resultsSha256);
  assert.equal(fase.analysis.consumedResultsSha256, rel.resultsSha256);
  assert.equal(fase.audit.consumedResultsSha256, rel.resultsSha256);
  assert.equal(val.auditoria.revisionId, rel.revisionId);
  assert.equal(val.publicationStatus, 'PUBLICADA');
  assert.equal(rel.publicationStatus, val.publicationStatus);
  assert.equal(fase.publication.status, val.publicationStatus);
  assert.equal(rel.verificationStatus, 'PENDIENTE',
    'No declarar certificación integral sin ejecutar el gate completo');
  assert.equal(fase.audit.status, 'CON HALLAZGOS');
  assert.equal(rel.estado, 'CON HALLAZGOS');
  assert.equal(rel.valoracion, file);
  assert.equal(rel.analisis, an);
  assert.ok(cat.auditorias.includes(rel.auditoria));
});
