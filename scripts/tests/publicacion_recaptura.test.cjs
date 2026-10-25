'use strict';
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const test = require('node:test');
const assert = require('node:assert/strict');

const root = path.resolve(__dirname, '../..');
const read = p => JSON.parse(fs.readFileSync(path.join(root, p), 'utf8'));
const cat = read('catalogo.json');
const sha = p => crypto.createHash('sha256').update(fs.readFileSync(path.join(root, p))).digest('hex');

// Toda valoración vigente que venga de una recaptura (campo evidenciaRecaptura) debe ser coherente de punta a punta.
const recapturas = cat.valoraciones.map(p => ({p, v: read(p)})).filter(x => x.v.evidenciaRecaptura);

test('hay al menos una recaptura publicada en el catálogo', () => {
  assert.ok(recapturas.length >= 1);
});

for (const {p, v} of recapturas) {
  test(`${v.ticker} ${v.revisionId}: registro, análisis, auditoría y evidencia coinciden`, () => {
    const an = cat.analisis.find(x => x.startsWith(`analisis/${v.ticker}-`));
    const analisis = read(an);
    const rec = read(`${v.evidenciaRecaptura}/recaptura.json`);
    const man = read(`${v.evidenciaRecaptura}/manifiesto_candidato.json`);
    assert.ok(cat.auditorias.includes(`auditorias/narrativas/${v.ticker}.md`));
    assert.equal(v.publicationStatus, 'PUBLICADA');
    assert.equal(analisis.revisionId, v.revisionId);
    assert.equal(analisis.linkedValuation.revisionId, v.revisionId);
    assert.equal(rec.revision_id, v.revisionId);
    assert.equal(rec.revision_anterior, v.revisionAnterior);
    assert.equal(v.resultsSha256, rec.foto_despues.data_sha256);
    assert.equal(man.resultados_sha256, rec.foto_despues.data_sha256);
    assert.deepEqual(analisis.linkedValuation.descuentoMultiples, v.descuentoMultiples);
    assert.equal(v.cierreTecnico.estado, 'CONTROLES_SIN_FALLAS');
    assert.ok(man.artifacts[p], 'el registro debe estar en el manifiesto');
    for (const [f, h] of Object.entries(man.artifacts)) assert.equal(sha(f), h.sha256, `hash distinto: ${f}`);
  });
}
