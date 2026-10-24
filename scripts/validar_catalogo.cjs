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
    // Regla única de los siete múltiplos para NFLX v7 y NKE R4.
    // Control de precios y pesos, con excepción NKE P/FCFE explícita;
    // no permitir que el ponderado relativo reemplace el DCF principal.
    if (['NFLX','NKE'].includes(v.ticker)) {
      const u=v.multiplesUnificados;
      assert.ok(u && u.revisionId===v.revisionId,'Múltiplos sin revisión vigente: '+v.ticker);
      assert.equal(u.metodos.length,7);
      assert.equal(u.preciosDescontados.length,7);
      assert.equal(u.control,'7/7 métodos trazados al motor original; suma de pesos 100%; 21/21 supuestos originales preservados');
      assert.ok(Math.abs(u.pesosRelativosSuman-1)<1e-8,'Pesos 7 métodos');
      assert.ok(Math.abs(u.valorIntrinsecoDCFBase-v.valorPrincipal)<1e-8,'DCF modificado por múltiplos');
      assert.ok(v.hojas.valoracion['Financials Multiples'].includes('SUPUESTOS · 7 MÉTODOS'),'Nueva tabla fuera del Nivel 2');
      const scs=[['cons','conservador'],['base','base'],['opt','optimista']];
      for (const [short,long] of scs) {
        const total=u.preciosDescontados.reduce((s,m)=>{
          if(typeof m[short]==='number'&&Number.isFinite(m[short]))return s+m[short]*m.peso;
          assert.equal(v.ticker,'NKE','N/D inesperado en múltiplo '+m.metodo);
          assert.equal(m.metodo,'P/FCFE','Solo P/FCFE NKE puede quedar N/D');
          assert.equal(m[short],'N/D');
          assert.equal(m.peso,0,'N/D con peso positivo');
          return s;
        },0);
        assert.ok(Math.abs(total-u.ponderadoRelativo[long])<1e-7,
          'Múltiplos históricos no concilian: '+v.ticker+'/'+long);
      }
      assert.ok(u.metodos.every(x=>x.control==='SIN CAMBIOS'),'Cambio no documentado de supuesto');
      assert.equal(v.auditoria.unificacionMultiples.resultado,'OK');
      // El Visor toma los ejes en las filas FY+3 de cada pestaña real.
      // Un HTML sin identificadores de fila deja vacías las grillas, aunque
      // las cifras y fórmulas de la hoja nativa sean correctas.
      const methodTabs=['EVEBITDA','EVFCFF','PE','PFCFE','POCF','PV','PBV'];
      for(const tab of methodTabs){
        const source=v.hojas.valoracion[tab]||'';
        for(const row of [8,9,19,20,30,31])
          assert.ok(source.includes('data-row="'+row+'"'),
            'Ejes FY+3 ausentes en '+v.ticker+'/'+tab+'/'+row);
      }
      const source=v.hojas.valoracion['Sensibilidad por múltiplo']||'';
      const entries=Array.from(source.matchAll(/<tr data-row="([0-9]+)">([\s\S]*?)<\/tr>/g),
        m=>({row:Number(m[1]),html:m[2]}));
      const lookup=new Map(entries.map(x=>[x.row,x.html]));
      assert.ok(entries.length>=69,'No hay 7 bloques de grillas Base');
      const parseCells=html=>Array.from((html||'').matchAll(/<td(?: [^>]*)?>([\s\S]*?)<\/td>/g),
        m=>m[1].replace(/<[^>]*>/g,'').trim());
      let numeric=0,nd=0;
      for(let i=0;i<7;i++){
        const at=76+10*i,title=parseCells(lookup.get(at))[0]||'';
        const middle=lookup.get(at+5),status=parseCells(lookup.get(at+8))[8];
        assert.ok(title.startsWith('BASE · '),'Historia ajena en matriz de '+v.ticker+' '+i);
        assert.ok(lookup.has(at+2)&&middle&&lookup.has(at+8),'Matriz Base incompleta');
        if(status==='N/D'){
          assert.equal(v.ticker,'NKE','N/D no permitido NFLX');
          assert.equal(i,3,'P/FCFE es la única excepción de NKE');
          nd++;
        } else {
          assert.equal(status,'OK','Control de matriz '+v.ticker+' '+i);
          const cells=parseCells(middle),prices=cells.slice(1,6);
          assert.equal(prices.length,5);
          assert.ok(prices.every(x=>/^[0-9.,]+$/.test(x)),'Precio de sensibilidad no numérico');
          numeric++;
        }
      }
      assert.equal(numeric,v.ticker==='NKE'?6:7);
      assert.equal(nd,v.ticker==='NKE'?1:0);
      assert.equal(v.auditoria.sensibilidadMultiplosBase20261023.matricesPublicadas,7);

      // La vista de la app no puede mostrar una grilla ajena ni antigua.
      // Matrices relativas únicamente Base, 7 métodos con 5×5 precios,
      // reconciliadas contra VP FY+3 (sin confundirlo con VP ponderado 1–3).
      const relHtml=v.hojas.valoracion['Sensibilidad por múltiplo'];
      assert.ok(typeof relHtml==='string','No está publicada la sensibilidad Base '+v.ticker);
      const cellsByRow=new Map();
      for (const match of relHtml.matchAll(/<tr data-row="(\d+)">([\s\S]*?)<\/tr>/g)) {
        const id=Number(match[1]),cells=Array.from(
          match[2].matchAll(/<td([^>]*)>([\s\S]*?)<\/td>/g),
          x=>({
            text:x[2].replace(/<[^>]+>/g,'').trim(),
            numeric:(()=>{const z=x[1].match(/data-value="([^"]+)"/);return z?Number(z[1]):null;})()
          })
        );
        assert.ok(!cellsByRow.has(id),'Fila de grilla duplicada '+id);
        cellsByRow.set(id,cells);
      }
      const METHODS=['EV/EBITDA','EV/FCFF','P/E','P/FCFE','P/OCF','P/V','P/BV'];
      let verified=0,unavailable=0;
      for(let i=0;i<METHODS.length;i++){
        const row=76+10*i,head=cellsByRow.get(row),axis=cellsByRow.get(row+2),ctl=cellsByRow.get(row+8);
        assert.ok(head?.[0]?.text.includes('BASE')&&head[0].text.includes(METHODS[i]),
          'No es grilla Base del método '+METHODS[i]);
        assert.equal(axis?.[0]?.text,'Múltiplo / Fundamental');
        assert.ok(ctl&&ctl.length>=9);
        const center=cellsByRow.get(row+5)?.[3];
        assert.ok(center,'Centro inexistente '+METHODS[i]);
        const numeric=center.numeric;
        if(v.ticker==='NKE'&&METHODS[i]==='P/FCFE'){
          assert.equal(center.text,'N/D');
          assert.equal(ctl[8].text,'N/D');
          assert.equal(ctl[7].text,'N/D');
          unavailable++;continue;
        }
        assert.equal(ctl[8].text,'OK','Método relativo no validado: '+METHODS[i]);
        assert.ok(Number.isFinite(numeric)&&numeric>0,'Precio de centro inválido: '+METHODS[i]);
        assert.ok(Math.abs(numeric-ctl[6].numeric)<1e-8,'Centro no coincide con VP FY+3: '+METHODS[i]);
        assert.ok(Math.abs(numeric-ctl[7].numeric)<1e-8,'Centro fuera del motor relativo: '+METHODS[i]);
        for(let r=row+3;r<=row+7;r++){
          const cells=cellsByRow.get(r);
          assert.ok(cells&&cells.slice(1,6).every(x=>Number.isFinite(x.numeric)),
            'Matriz incompleta '+METHODS[i]+' / fila '+r);
        }
        verified++;
      }
      assert.equal(verified,v.ticker==='NKE'?6:7);
      assert.equal(unavailable,v.ticker==='NKE'?1:0);
      for(const method of ['EVEBITDA','EVFCFF','PE','PFCFE','POCF','PV','PBV']){
        const html=v.hojas.valoracion[method];
        assert.ok(typeof html==='string' && html.includes('data-row="19"'),
          'Faltan las filas de ejes económicos reales '+method);
      }

    }
    require('./auditar_integridad.cjs').validateRecord(v);
    assert.ok(c.auditorias.includes('auditorias/narrativas/' + v.ticker + '.md'));
    assert.ok(v.salvedades.length);
  }
  return {valoraciones: vals.length, analisis: c.analisis.length,
    auditorias: c.auditorias.length};
}
module.exports = {validate};
if (require.main === module) console.log(JSON.stringify(validate(), null, 2));
