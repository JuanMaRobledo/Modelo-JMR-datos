'use strict';
const fs = require('node:fs');
const path = require('node:path');
const test = require('node:test');
const assert = require('node:assert/strict');

const root = path.resolve(__dirname, '../..');
const read = p => JSON.parse(fs.readFileSync(path.join(root, p), 'utf8'));

const EMPRESAS = [
  {t: 'NKE', rev: 'NKE-JMR-20261025-R5', ant: 'NKE-JMR-20261023-R4-M7', evid: 'evidencia/NKE-20261025-R5',
   hoja: '1wWS0qNCWvSrYCI53kk7H1zBshn-RJWjeKFu10sHCNWw', dcf: 35.023476792006896, mos: 22.765259914804485},
  {t: 'NVDA', rev: 'NVDA-20261025-R3', ant: 'NVDA-20261024-R2', evid: 'evidencia/NVDA-20261025-R3',
   hoja: '1gbtwORZsvjhZNCV8xlNDloHYEeE09cEbXmPZOoLJ8gY', dcf: 381.79006728063933, mos: 248.16354373241558},
];

for (const e of EMPRESAS) {
  test(`${e.t} ${e.rev}: catálogo, registro, análisis, auditoría y evidencia usan una revisión`, () => {
    const cat = read('catalogo.json');
    const file = cat.valoraciones.find(p => p.startsWith(`valoraciones/${e.t}-`));
    const an = cat.analisis.find(p => p.startsWith(`analisis/${e.t}-`));
    assert.ok(file && an, 'falta valoración o análisis vigente en catálogo');
    assert.ok(cat.auditorias.includes(`auditorias/narrativas/${e.t}.md`));
    const val = read(file), analisis = read(an);
    const rec = read(`${e.evid}/recaptura.json`), man = read(`${e.evid}/manifiesto_candidato.json`);
    assert.equal(val.revisionId, e.rev);
    assert.equal(analisis.revisionId, e.rev);
    assert.equal(analisis.linkedValuation.revisionId, e.rev);
    assert.equal(rec.revision_id, e.rev);
    assert.equal(rec.revision_anterior, e.ant);
    assert.equal(val.revisionAnterior, e.ant);
    const sha = rec.foto_despues.data_sha256;
    assert.equal(val.resultsSha256, sha);
    assert.equal(val.reviewManifest?.resultsSha256 ?? sha, sha);
    assert.equal(man.resultados_sha256, sha);
    assert.equal(val.publicationStatus, 'PUBLICADA');
    assert.equal(val.valorPrincipal, e.dcf);
    assert.equal(val.precioMOS, e.mos);
    assert.equal(val.hojaGoogle, `https://docs.google.com/spreadsheets/d/${e.hoja}/edit`);
    assert.deepEqual(analisis.linkedValuation.descuentoMultiples, val.descuentoMultiples);
    assert.equal((analisis.articleHtml.match(/<h2>/g) || []).length, 18);
    for (const [p, h] of Object.entries(man.artifacts)) {
      const sha256 = require('node:crypto').createHash('sha256').update(fs.readFileSync(path.join(root, p))).digest('hex');
      assert.equal(sha256, h.sha256, `hash distinto: ${p}`);
    }
  });
}
