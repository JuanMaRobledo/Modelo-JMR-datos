'use strict';
const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');

const CORE_NATIVE=['EV/EBITDA','EV/FCFF','P/E','P/FCFE','P/OCF'];
const MAYBE_NATIVE=['P/V','P/BV'];
const finiteNative=x=>typeof x==='number'&&Number.isFinite(x);
const nearNative=(a,b)=>finiteNative(a)&&finiteNative(b)&&Math.abs(a-b)<=Math.max(1e-6,Math.abs(b)*1e-8);
/**
 * Puerta de datos estructurados A. La matriz candidata NO basta:
 * exige origen/revisión, integridad, centros VP3 y estado de integración
 * explícito. La auditoría económica independiente se realiza después.
 */
function validateNativeMatrices(v){
  const s=v.sensibilidadMultiples||{};
  assert.equal(s.contrato,'base-native-five-priority-v1','Formato de matrices A no vigente');
  assert.equal(s.revisionId,v.revisionId,'Revisión de matriz diferente');
  assert.equal(s.sourceSheetId,v.sheet_id,'ID de hoja diferente');
  assert.match(String(s.resultadosSha256||''),/^[0-9a-f]{64}$/,'Foto financiera sin SHA256');
  assert.equal(s.estadoPublicacion,'INTEGRADO_EN_REVISION',
    'CANDIDATO_NO_PUBLICADO nunca acredita matrices oficiales');
  assert.equal(s.controlesTecnicosAprobados,true,'Revisión técnica de matrices pendiente');
  const items=s.matrices;
  assert.ok(Array.isArray(items),'Matriz de múltiplos no publicada');
  const names=new Set(items.map(x=>x?.metodo));
  assert.equal(names.size,items.length,'Matrices repetidas');
  for(const name of CORE_NATIVE)assert.ok(names.has(name),'Falta prioritario: '+name);
  for(const m of items){
    assert.ok(CORE_NATIVE.includes(m.metodo)||MAYBE_NATIVE.includes(m.metodo),
      'Método no reconocido');
    assert.equal(m.escenario,'base','Solo sensibilidad de Base');
    assert.equal(m.ancla,'JMR','Ancla de la hoja oficial');
    const chosen=(v.descuentoMultiples?.metodos||[]).find(x=>x.nombre===m.metodo);
    const vp3=chosen?.base?.vp?.[2];
    if(finiteNative(vp3))assert.ok(nearNative(vp3,m.vp3Original),
      m.metodo+': VP3 no coincide con descuento oficial');
    if(m.estado==='OK'){
      assert.ok(Array.isArray(m.matriz)&&m.matriz.length===5&&m.matriz.every(r=>
        Array.isArray(r)&&r.length===5&&r.every(finiteNative)),m.metodo+': no es 5x5 numérica');
      assert.ok(Array.isArray(m.fundamentalFY3)&&m.fundamentalFY3.length===5&&m.fundamentalFY3.every(finiteNative));
      assert.ok(Array.isArray(m.multiploElegido)&&m.multiploElegido.length===5&&m.multiploElegido.every(finiteNative));
      assert.ok(nearNative(m.matriz[2][2],m.centro)&&nearNative(m.centro,m.vp3Original),
        m.metodo+': centro no concilia');
    }else if(m.estado==='N/A'){
      assert.equal(m.matriz,null,m.metodo+': N/A con matriz numérica');
      assert.ok(typeof m.motivo==='string'&&m.motivo.trim().length>=20,
        m.metodo+': falta justificación económica N/A');
      assert.ok(!chosen||!finiteNative(chosen.peso)||chosen.peso===0,
        m.metodo+': un método no aplicable no puede tener peso positivo');
    }else if(m.estado==='N/D' && MAYBE_NATIVE.includes(m.metodo) &&
             (!chosen || !finiteNative(chosen.peso) || chosen.peso===0)){
      // P/V y P/BV son opcionales y no bloquean si no se utilizan.
      assert.equal(m.matriz,null,m.metodo+': N/D opcional no lleva matriz');
    }else{
      assert.fail(m.metodo+': N/D prioritario o con peso positivo no puede pasar como aprobado');
    }
  }
  return true;
}

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
    // El catálogo es la fuente de identidad: admite ruta o revisión explícita.
    // Una revisión sin vínculo interno (AFYA) permanece EN_REVISION, nunca
    // se declara completa por inferencia.
    const status = a.status || a.estado || a.publicationStatus;
    const refPath = typeof a.linkedValuation === 'string'
      ? a.linkedValuation : a.linkedValuation?.sourcePath;
    const candidates = vals.filter(x =>
      refPath ? x.path === refPath ||
        (x.record.revisionId === refPath && x.record.ticker === a.ticker)
        : x.record.revisionId === a.revisionId && x.record.ticker === a.ticker);
    assert.equal(candidates.length, 1,
      a.ticker + ': valoración del catálogo ausente o ambigua para ' +
      (refPath || a.revisionId));
    const v = candidates[0];
    if (!refPath) {
      assert.equal(status, 'EN_REVISION',
        a.ticker + ': falta vínculo explícito en un análisis no provisional');
      console.warn('PENDIENTE_VINCULO: '+a.ticker+
        ' resuelto solo por ticker y revisión oficial; completar vínculo antes del cierre.');
    }
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
    if (a.remotePath !== undefined) assert.equal(a.remotePath, p);
    else {
      assert.equal(status, 'EN_REVISION',
        a.ticker + ': ruta remota ausente de expediente no provisional');
      console.warn('PENDIENTE_RUTA: '+a.ticker+
        ' sin remotePath embebido; ruta vigente solo en catálogo.');
    }
    // Algunos análisis nuevos enlazan el resultado en vez de duplicar todo el
    // bloque financiero. Una referencia compacta no es un error de cálculo;
    // el expediente oficial sigue siendo la única fuente del cálculo.
    // Cuando hay copia embebida, sí debe coincidir íntegramente.
    const linked = a.linkedValuation;
    if (linked == null) {
      assert.equal(status, 'EN_REVISION',
        a.ticker + ': sin vínculo financiero explícito no puede cerrarse');
    } else if (typeof linked === 'string') {
      assert.ok(linked === v.path || linked === v.record.revisionId,
        a.ticker + ': ruta o ID de revisión no corresponde al expediente');
      assert.equal(status, 'EN_REVISION',
        a.ticker + ': referencia simple no acredita conciliación financiera');
      console.warn('VINCULO_REFERENCIA: '+a.ticker+
        ' usa ruta o revisión oficial; sin copia interna de múltiplos.');
    } else if (Object.prototype.hasOwnProperty.call(linked, 'descuentoMultiples')) {
      assert.deepEqual(linked.descuentoMultiples, v.record.descuentoMultiples,
        a.ticker + ': múltiplos embebidos distintos de la valoración oficial');
    } else {
      assert.ok(typeof linked.revisionId === 'string' && linked.revisionId,
        a.ticker + ': vínculo compacto sin revisión financiera');
      assert.ok(Number.isFinite(linked.valorPrincipal),
        a.ticker + ': vínculo compacto sin valor Base numérico');
      assert.equal(linked.valorPrincipal, v.record.valorPrincipal,
        a.ticker + ': valor Base del análisis difiere de la valoración');
      if (linked.metodo_valoracion !== undefined)
        assert.equal(linked.metodo_valoracion, v.record.metodo_valoracion,
          a.ticker + ': método del análisis difiere de la valoración');
      if (linked.version_metodo !== undefined)
        assert.equal(linked.version_metodo, v.record.version_metodo,
          a.ticker + ': versión del método difiere de la valoración');
      console.warn('VINCULO_COMPACTO: ' + a.ticker +
        ' usa la valoración como fuente única de múltiplos; sin copia embebida.');
    }
    // Contrato editorial 2026-10-30: Nivel 1 = 14 capítulos, ciclos independientes.
    // Los expedientes anteriores siguen siendo visibles, pero NO se certifican
    // como migrados. Solo tres revisiones históricas publicadas tienen excepción.
    const h2 = [...a.articleHtml.matchAll(/<h2[^>]*>([\s\S]*?)<\/h2>/gi)]
      .map(m => m[1].replace(/<[^>]+>/g, '').trim());
    const numbers = h2
      .map(h => /^(\d+)\.\s+/.exec(h))
      .filter(Boolean).map(m => Number(m[1]));
    const numberedSequence = n => JSON.stringify(numbers) ===
      JSON.stringify(Array.from({length:n}, (_,i) => i+1));
    const is14 = numberedSequence(14);
    const legacy13 = numberedSequence(13);
    const legacy18 = numberedSequence(18);
    const historicalRevisions = {
      META: 'META-20261025-R5',
      NVDA: 'NVDA-20261025-R4',
      XP: 'XP-JMR-20261026-R2'
    };
    const frozenHistorical = historicalRevisions[a.ticker] === a.revisionId;
    if (is14) {
      assert.ok(h2.some(h => /ciclos?/i.test(h) && /macro|mercado/i.test(h)),
        a.ticker + ': falta capítulo propio de ciclos');
      if (a.controlCobertura?.secciones != null)
        assert.equal(a.controlCobertura.secciones, 14,
          a.ticker + ': metadatos editoriales deben contar 14 capítulos');
    } else if (legacy13) {
      assert.ok(status === 'EN_REVISION' || frozenHistorical,
        a.ticker + ': no publicar como nuevo un informe de 13 capítulos');
      console.warn('PENDIENTE_EDITORIAL: ' + a.ticker +
        ' conserva 13 capítulos; separar ciclos antes de certificar Nivel 1 (14).');
    } else if (legacy18 && frozenHistorical && a.ticker === 'XP') {
      console.warn('LEGADO_HISTORICO: XP conserva 18 capítulos por revisión archivada; ' +
        'no corresponde al nuevo Nivel 1 de 14.');
    } else {
      assert.fail(a.ticker + ': índice inválido: estándar=14, ' +
        'legado de 13 solo EN_REVISION o revisión histórica congelada');
    }
    if (a.ticker==='META' && /^META-/.test(a.revisionId||'')) {
      assert.ok(h2.filter(h => !/^[0-9]+[.] /.test(h))
        .every(h => /^Adenda /.test(h)), 'META: h2 extra no identificado como adenda');
      assert.equal(a.controlCobertura?.matricesDCF,8);
      assert.equal(a.controlCobertura?.centrosDCFValidados,8);
      assert.ok(a.calculationHtml?.length>1000,'META: falta nivel 2');
      assert.ok(a.editorialRevisionId,'META: falta revisión editorial');
    } else if (a.controlCobertura) {
      // Las revisiones EN_REVISION pueden tener indicadores anteriores (13/18
      // apartados) o una ficha de capítulos sin inventario de 25 entradas.
      // Solo afirmar cobertura v5 cuando el inventario de 25 existe realmente.
      const cov = a.controlCobertura;
      if (Array.isArray(cov.entradas) && cov.entradas.length === 25) {
        assert.equal(cov.resueltas + cov.limitadas, 25,
          a.ticker + ': inventario de 25 puntos sin conciliación');
        assert.ok(a.editorialRevisionId, 'Falta identificación de revisión editorial');
      } else {
        assert.equal(status, 'EN_REVISION',
          a.ticker + ': cobertura incompleta o legado no permite cierre editorial');
        console.warn('PENDIENTE_COBERTURA: '+a.ticker+
          ' no acredita las 25 entradas editoriales vigentes.');
      }
    }
  }
  for (const {record: v} of vals) {
    // Regla única de los siete múltiplos para NFLX v7 y NKE R4.
    // Control de precios y pesos, con excepción NKE P/FCFE explícita;
    // no permitir que el ponderado relativo reemplace el DCF principal.
    if (['NFLX','NKE'].includes(v.ticker) && v.multiplesUnificados) {
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
      assert.ok(u.metodos.every(x=>x.control==='CALCULADO'),'Método incompleto');
      assert.equal(v.cierreMultiplos?.methodsCalculated,7);
      assert.ok(u.preciosDescontados.every(x=>['cons','base','opt'].every(k=>Number.isFinite(x[k]))),'Los siete métodos deben tener tres precios');
      assert.equal(v.auditoria.unificacionMultiples.resultado,'OK');

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
      assert.equal(verified,7);
      assert.equal(unavailable,0);
      for(const method of ['EVEBITDA','EVFCFF','PE','PFCFE','POCF','PV','PBV']){
        const html=v.hojas.valoracion[method];
        assert.ok(typeof html==='string' && html.includes('data-row="19"'),
          'Faltan las filas de ejes económicos reales '+method);
      }

    }
    // CI técnico no equivale a publicar resultados. Si una revisión carece de
    // sensibilidad por múltiplos, fallar EXPLÍCITAMENTE en vez de pasar el
    // registro como si estuviera auditado o dejar un TypeError opaco.
    const contratoA = c.controlModeloA?.empresas?.[v.ticker]?.metodo === 'A-1.2';
    if (contratoA) {
      const s = v.sensibilidadMultiples;
      const grids = Array.isArray(s?.matrices) ? s.matrices : [];
      // Método A vigente: sensibilidades de múltiplos SOLO Base, matrices 5x5
      // por método prioritario aplicable. P/S y P/BV son opcionales.
      // Los centros sueltos de SHAK o los N/D de UBER no sustituyen grillas.
      assert.ok(grids.length > 0,
        v.ticker + ': BLOQUEO_FINANCIERO: faltan matrices Base 5x5 ' +
        'exportadas desde la hoja oficial al JSON (matrices: ' +
        grids.length + ', controles de centro: ' + (s?.controles?.length ?? 0) +
        '). Verificar anclas, centros FY+3 y origen; N/A con causa cuando ' +
        'no aplique. No exponer 21/28 controles legados como requisito del Método A.');
      validateNativeMatrices(v);
    } else if (v.ticker !== 'META') {
      // Únicamente para revisiones históricas anteriores al Método A.
      const s = v.sensibilidadMultiples;
      const traditional = s?.methods === 7 &&
        s.scenarios?.length === 3 && s.disrupcionFuera &&
        s.controles?.length === 21;
      const twoAnchors = s?.contract === 'base-two-anchors-two-families-v1' &&
        s.matrices?.length === 28 && s.controles?.length === 28;
      assert.ok(traditional || twoAnchors,
        v.ticker + ': sensibilidad histórica no concilia con 21/28 controles.');
    }
    require('./auditar_integridad.cjs').validateRecord(v);
    assert.ok(c.auditorias.includes('auditorias/narrativas/' + v.ticker + '.md'));
    assert.ok(v.salvedades.length);
  }
  return {valoraciones: vals.length, analisis: c.analisis.length,
    auditorias: c.auditorias.length};
}
module.exports = {validate,validateNativeMatrices};
if (require.main === module) console.log(JSON.stringify(validate(), null, 2));
