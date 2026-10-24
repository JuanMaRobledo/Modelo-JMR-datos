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
  // El catálogo es la lista blanca explícita de publicación, no la carpeta completa.
  // Archivos de otros procesos/PRs no se importan implícitamente y no deben bloquear
  // la validación de una revisión financiera independiente. Registrar huérfanos en logs.
  for (const group of ['valoraciones', 'analisis', 'auditorias']) {
    const folder = group === 'auditorias' ? 'auditorias/narrativas' : group;
    const seen = inventory(folder);
    const declared = c[group].slice().sort();
    for (const p of declared) assert.ok(seen.includes(p),
      'Archivo publicado ausente: '+p);
    const extra=seen.filter(p=>!declared.includes(p));
    if(extra.length) console.warn('AVISO: Archivos no incluidos en catálogo; NO publicados ('+
      group+'): '+extra.join(', '));
  }
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
    if(a.ticker==='META' && a.revisionId==='META-20261023-r4'){
      const headings=a.articleHtml.split('<h2>').slice(1).map(h=>h.split('</h2>')[0].replace(/<[^>]+>/g,'').trim());
      assert.equal(headings.filter(h=>/^[0-9]+[.] /.test(h)).length,18,'META: 18 secciones numeradas');
      assert.ok(headings.filter(h=>!/^[0-9]+[.] /.test(h)).every(h=>/^Adenda /.test(h)),'META: h2 extra no identificado como adenda');
      assert.equal(a.controlCobertura?.secciones,18);
      assert.equal(a.controlCobertura?.matricesDCF,8);
      assert.equal(a.controlCobertura?.centrosDCFValidados,8);
      assert.ok(a.calculationHtml?.length>1000,'META: falta nivel 2');
      assert.ok(a.editorialRevisionId,'META: falta revisión editorial');
    } else {
      assert.equal((a.articleHtml.match(/<h2>/g) || []).length, 18);
      if (a.controlCobertura) {
        assert.equal(a.controlCobertura.entradas.length, 25,
          'Cobertura editorial v5 debe documentar 25 puntos');
        assert.equal(a.controlCobertura.resueltas + a.controlCobertura.limitadas, 25);
        assert.ok(a.editorialRevisionId, 'Falta identificación de revisión editorial');
      }
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
