'use strict';
const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');

function validate(root = path.join(__dirname, '..')) {
  const c = JSON.parse(fs.readFileSync(path.join(root, 'catalogo.json'), 'utf8'));
  const inventory = dir => fs.readdirSync(path.join(root, dir), {withFileTypes: true})
    .flatMap(e => e.isDirectory() ? inventory(dir + '/' + e.name)
      : e.name === '.gitkeep' ? [] : [dir + '/' + e.name]).sort();

  // Solo las auditorías narrativas vigentes participan en el catálogo público.
  // Las carpetas de archivo/históricas se conservan como evidencias, sin contaminar la app.
  for (const group of ['valoraciones', 'analisis']) {
    assert.deepEqual(inventory(group), c[group].slice().sort(), 'Inventario: ' + group);
  }
  assert.deepEqual(inventory('auditorias/narrativas'), c.auditorias.slice().sort(),
    'Inventario: auditorias vigentes');
  assert.ok(c.auditorias.every(p => p.startsWith('auditorias/narrativas/')),
    'Auditoría histórica no puede ser vigente');

  const vals = c.valoraciones.map(p => ({
    path: p, record: JSON.parse(fs.readFileSync(path.join(root, p)))
  }));
  for (const p of c.analisis) {
    const a = JSON.parse(fs.readFileSync(path.join(root, p)));
    const v = vals.find(x => x.path === a.linkedValuation?.sourcePath);
    assert.ok(v, 'Análisis sin valoración');
    assert.equal(a.ticker, v.record.ticker);
    // El artículo puede publicarse después de su valoración sin cambiar el DCF.
    const isoDate = x => typeof x === 'string' &&
      /^[0-9]{4}-[0-9]{2}-[0-9]{2}$/.test(x);
    assert.ok(isoDate(a.date) && isoDate(v.record.fecha) && a.date >= v.record.fecha,
      'La fecha editorial no puede preceder la valoración');
    if (a.revisionId && v.record.revisionId)
      assert.equal(a.revisionId, v.record.revisionId, 'Revisión financiera distinta');
    if (a.linkedValuation?.revisionId && v.record.revisionId)
      assert.equal(a.linkedValuation.revisionId, v.record.revisionId,
        'Enlace a revisión distinta');
    assert.equal(a.remotePath, p);
    assert.deepEqual(a.linkedValuation.descuentoMultiples, v.record.descuentoMultiples);
    const headings = [...a.articleHtml.matchAll(/<h2(?:\\s[^>]*)?>(.*?)<\\/h2>/gs)]
      .map(x => x[1].replace(/<[^>]*>/g, '').trim());
    // Nivel 1: exactamente 18 encabezados numerados 1..18 en orden.
    // Notas posteriores/no numeradas no sustituyen una sección del artículo.
    const editorial = headings.filter(h => /^[0-9]{1,2}\\.\\s/.test(h));
    assert.deepEqual(editorial.map(h => Number(h.match(/^([0-9]+)/)[1])),
      Array.from({length: 18}, (_, i) => i + 1),
      'Análisis: faltan o sobran secciones principales numeradas 1–18');
    if (a.controlCobertura) {
      if (Array.isArray(a.controlCobertura.entradas)) {
        assert.equal(a.controlCobertura.entradas.length, 25,
          'Cobertura editorial v5 debe documentar 25 puntos');
        assert.equal(a.controlCobertura.resueltas + a.controlCobertura.limitadas, 25);
      } else {
        // Contrato editorial v5 de META R4-A2: 18 secciones + nivel 2 + 3 sensibilidades + 4 historias.
        assert.equal(a.controlCobertura.secciones, 18, 'Faltan secciones editoriales');
        assert.equal(a.controlCobertura.nivel2, true, 'Falta nivel 2');
        assert.equal(a.controlCobertura.matricesDCF, 3, 'Faltan matrices DCF');
        assert.equal(a.controlCobertura.escenarios, 4, 'Faltan historias');
      }
      assert.ok(a.editorialRevisionId, 'Falta identificación de revisión editorial');
    }
  }
  for (const {record: v} of vals) {
    require('./auditar_integridad.cjs').validateRecord(v);
    assert.ok(c.auditorias.includes('auditorias/narrativas/' + v.ticker + '.md'));
    assert.ok(v.salvedades.length);
  }
  return {valoraciones: vals.length, analisis: c.analisis.length,
    auditorias: c.auditorias.length};
}
module.exports = {validate};
if (require.main === module) console.log(JSON.stringify(validate(), null, 2));
