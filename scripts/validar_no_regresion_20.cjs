#!/usr/bin/env node
'use strict';
/**
 * Gate NO DESTRUCTIVO: prueba que la integración de múltiples no alteró los
 * supuestos, DCF, estados históricos, identidad o contenido de los niveles.
 * No toca hojas, JSON activos ni estados de publicación.
 */
const fs=require('node:fs');
const path=require('node:path');
const assert=require('node:assert/strict');
const root=path.resolve(__dirname,'..');
const read=p=>JSON.parse(fs.readFileSync(path.join(root,p),'utf8'));
const exists=p=>fs.existsSync(path.join(root,p));
// historiasNumeros (REGLAS v31-v32): copia informativa de la sección historias → números; no cambia DCF, MOS ni probabilidades.
const ALLOWED_NEW_FIELDS=new Set(['descuentoMultiples','sensibilidadMultiples','dcfFCFE','historiasNumeros']);
function safeCore(v) {
  // El peso de cada método en `metodos` se deriva de descuentoMultiples (categoría de la hoja): puede cambiar al integrar pesos.
  // Cualquier otro campo de `metodos` sigue protegido.
  const core=Object.fromEntries(Object.entries(v).filter(([k])=>!ALLOWED_NEW_FIELDS.has(k)));
  if(Array.isArray(core.metodos))core.metodos=core.metodos.map(m=>{const {peso,...rest}=m||{};return rest;});
  return core;
}
function run(){
  const cat=read('catalogo.json');
  const selections=process.env.JMR_CI_ARCHIVO_LEGADO?cat.archivoFloyd.controlModeloA:cat.controlModeloA?.empresas;
  const aEntries=Object.entries(selections||{}).filter(([,v])=>v.metodo==='A-1.2');
  // 1-nov-2026 (autorizado por el usuario): INTU y NU pasan a CANDIDATO por no tener DCF nativo (A-1.2 punto 9).
  // No se pierden: deben estar fuera del catálogo y sus archivos conservados con la marca de degradación.
  const DEGRADADAS=['INTU','NU'];
  for(const t of DEGRADADAS){
    const rev=t+'-20261029-R1',d='candidatos/valoraciones/'+rev+'/';
    // La revisión degradada no vuelve al catálogo; una revisión nueva del mismo ticker sí puede entrar (INTU-20261101-A12-R1).
    assert.ok(!aEntries.some(([,v])=>v.rutaValoracion==='valoraciones/'+rev+'.json'),t+': la revisión degradada sigue en el catálogo activo');
    assert.ok(!cat.valoraciones.includes('valoraciones/'+rev+'.json'),t+': valoración degradada en catálogo');
    assert.ok(!cat.analisis.some(p=>path.basename(p).includes(rev)),t+': análisis degradado en catálogo');
    const cand=read(d+'VALORACION_A12_EN_REVISION.json');
    assert.ok(cand.degradadoACandidato&&cand.degradadoACandidato.fecha,t+': falta la marca de degradación');
    assert.ok(Number.isFinite(cand.valorPrincipal)&&cand.valorPrincipal>0,t+': candidato perdió el DCF Base');
    read(d+'ANALISIS_A12_EN_REVISION.json');
  }
  const NUEVAS={META:'META-20261101-A12-R1',NVDA:'NVDA-20261101-A12-R1',XP:'XP-20261031-A12-R1',INTU:'INTU-20261101-A12-R1',DPZ:'DPZ-20261101-A1',NU:'NU-20261102-A12-R3'};
  const nuevas=Object.entries(NUEVAS).filter(([t,r])=>aEntries.some(([name,v])=>name===t&&path.basename(v.rutaValoracion).startsWith(r))).length;
  // Altas explícitas y acotadas AMZN R5, PAGS R1 y AAPL R1. Se preservan las revisiones anteriores y solo se admiten rutas canónicas.
  const ADICIONALES={AMZN:'AMZN-20261102-A12-R5',PAGS:'PAGS-20261030-A12-R1',AAPL:'AAPL-20261103-A12-R1',LULU:'LULU-20261103-A12-R1',KO:'KO-20261103-A12-R1'};
  const extra=Object.entries(ADICIONALES).filter(([ticker,revision])=>
    aEntries.some(([name,item])=>name===ticker&&item.rutaValoracion==='valoraciones/'+revision+'.json')).length;
  const lulu=aEntries.find(([ticker])=>ticker==='LULU');
  if(lulu){
    assert.equal(lulu[1].rutaValoracion,'valoraciones/LULU-20261103-A12-R1.json',
      'LULU: solo una nueva valoración oficial A-1.2 R1, no una captura de rango');
    const f=read(lulu[1].rutaValoracion);
    assert.equal(f.revisionId,'LULU-20261103-A12-R1');
    assert.equal(f.sensibilidadMultiples?.sourceSheetId,f.sheet_id);
    assert.equal(f.sensibilidadMultiples?.matrices?.filter(m=>m.prioritario&&m.estado==='OK').length,5,
      'LULU: se exigen las cinco grillas Base nativas completas');
    assert.equal(f.sensibilidadDCF?.matrices?.filter(m=>m.centroConciliado).length,3,
      'LULU: se exigen las tres sensibilidades DCF 5x5 conciliadas');
  }
  const ko=aEntries.find(([ticker])=>ticker==='KO');
  if(ko){
    // Alta por solicitud expresa: exactamente KO R1, con fuente nativa y artículos vinculados.
    const rel='valoraciones/KO-20261103-A12-R1.json';
    assert.equal(ko[1].rutaValoracion,rel,'KO: alta R1 no corresponde con contrato oficial');
    const v=read(rel);
    const a=read('analisis/KO-research-KO-20261103-A12-R1.json');
    assert.equal(v.revisionId,'KO-20261103-A12-R1');
    assert.equal(a.revisionId,v.revisionId);
    assert.equal(v.sensibilidadMultiples?.sourceSheetId,v.sheet_id);
    assert.equal(v.sensibilidadMultiples?.matrices?.filter(m=>m.prioritario&&m.estado==='OK').length,5);
    assert.equal(v.sensibilidadDCF?.matrices?.filter(m=>m.centroConciliado).length,3);
    assert.ok((a.controlCobertura?.palabrasNivel1||0)>=7500,'KO: artículo no pasa profundidad');
    assert.equal(a.controlCobertura?.nivel2Apartados,12);
  }
  const floyd=Object.entries(cat.controlModeloA?.empresas||{})
    .filter(([,item])=>item.metodo==='Floyd' && item.rutaValoracion && read(item.rutaValoracion).contratoLibros==='floyd-h1-h2-separados-v1'); // solo legado F1–F5; Floyd R1–R6 se valida por contrato aparte
  // Revisiones Floyd integradas de forma explícita (una por emisor), cada una con su
  // antecedente A-1.2 preservado (archivo y huella de hoja de origen intactos).
  const FLOYD_ESPERADO={
    UBER:{ruta:'valoraciones/UBER-FLOYD-3T26.json',original:'valoraciones/UBER-20261030-A1.json',
      originalRevision:'UBER-20261030-A1',originalSheet:'1i0B9cPX-z5G7GtqGmU3lVbJP0l6AyhhYhF0x8pQ8B58',
      analisis:'analisis/UBER-research-UBER-FLOYD-3T26.json',valorOriginal:91.13793738151752},
    CMG:{ruta:'valoraciones/CMG-FLOYD-20261108-R1.json',original:'valoraciones/CMG-20261028-A3.json',
      originalRevision:'CMG-20261028-A3',originalSheet:'1JnByF8jZrxq7dk0opV29wugI19c9HWkifljzUFpkD9c',
      analisis:'analisis/CMG-research-CMG-FLOYD-20261108-R1.json',valorOriginal:25.246494601933065}};
  let floydHistoricoProtegido=0;
  assert.ok(floyd.length<=Object.keys(FLOYD_ESPERADO).length,'No permitir altas Floyd desconocidas');
  for(const [ticker,item] of floyd){
    const exp=FLOYD_ESPERADO[ticker];
    assert.ok(exp,'Alta Floyd no identificada: '+ticker);
    assert.equal(item.rutaValoracion,exp.ruta);
    const original=read(exp.original);
    const current=read(item.rutaValoracion);
    const analysis=read(exp.analisis);
    assert.equal(original.revisionId,exp.originalRevision,'Histórico '+ticker+' fue modificado');
    assert.equal(original.sheet_id,exp.originalSheet,
      'Huella de origen A-1.2 no preservada');
    assert.ok(Math.abs(original.valorPrincipal-exp.valorOriginal)<1e-7,
      'El valor A-1.2 histórico de '+ticker+' fue alterado');
    floydHistoricoProtegido++; // la fotografía A-1.2 sustituida sigue protegida
    assert.equal(current.perfil_valoracion,'Floyd');
    assert.equal(current.version_metodo,'Floyd');
    assert.equal(current.sensibilidadMultiples?.matrices?.length,5);
    assert.equal(current.sensibilidadDCF?.matrices?.length,3);
    assert.equal(analysis.linkedValuation?.sourcePath,item.rutaValoracion);
    assert.equal(analysis.revisionId,current.revisionId);
  }
  const expectedLegacy=Object.entries(cat.archivoFloyd?.controlModeloA||{})
    .filter(([ticker,v])=>v.metodo==='A-1.2' && (process.env.JMR_CI_ARCHIVO_LEGADO || cat.controlModeloA.empresas[ticker]?.metodo==='A-1.2')).length;
  assert.equal(aEntries.length,expectedLegacy,
    'El archivo A-1.2 y sus selecciones vigentes temporales no concilian');
  let snapshots=0,htmlPairs=0;
  const withoutSnapshot=[];
  for(const [ticker,item] of aEntries){
    const vp=item.rutaValoracion;
    assert.ok(cat.valoraciones.includes(vp),ticker+': valoración fuera del catálogo');
    const val=read(vp);
    assert.equal(val.ticker,ticker,ticker+': ticker financiero equivocado');
    assert.equal(val.estado,'EN_REVISION',ticker+': estado financiero modificado');
    assert.equal(val.publicationStatus,'EN_REVISION',ticker+': publicationStatus modificado');
    assert.equal(val.version_metodo,'A-1.2',ticker+': método alterado');
    assert.ok(Number.isFinite(val.valorPrincipal)&&val.valorPrincipal>0,ticker+': DCF Base inválido');
    assert.ok(Number.isFinite(val.precioMOS)&&val.precioMOS>=0,ticker+': MOS inválido');
    const matches=cat.analisis.filter(p=>path.basename(p).startsWith(ticker+'-')&&read(p).revisionId===val.revisionId);
    assert.equal(matches.length,1,ticker+': falta expediente único en catálogo');
    const a=read(matches[0]);
    assert.equal(a.ticker,ticker,ticker+': ticker narrativo distinto');
    assert.equal(a.revisionId,val.revisionId,ticker+': revisiones diferentes');
    assert.equal(a.estado,'EN_REVISION',ticker+': análisis dejó EN_REVISION');
    // publicationAuthorized habilita la ficha EN_REVISION en algunas revisiones
    // históricas; no es evidencia de publicación final ni de QA completado.
    assert.notEqual(a.status,'PUBLICADO',ticker+': documento publicado sin control');
    assert.ok(a.articleHtml&&a.calculationHtml,ticker+': faltan los dos niveles');
    assert.equal(a.html,a.articleHtml+a.calculationHtml,ticker+': HTML N1 + N2 desincronizado');
    htmlPairs++;
    const linked=a.linkedValuation;
    if(typeof linked==='string')
      assert.ok(linked===vp||linked===val.revisionId,ticker+': enlace corto a otra revisión');
    else{
      assert.ok(linked&&linked.sourcePath===vp&&linked.revisionId===val.revisionId,
        ticker+': enlace estructurado a otra revisión');
      if(linked.valorPrincipal!==undefined)
        assert.ok(Math.abs(linked.valorPrincipal-val.valorPrincipal)<1e-7,
          ticker+': DCF vinculado no concilia');
    }
    const originalBaseline='evidencia/integracion-nativa-20261030/'+val.revisionId+'/registro_antes.json';
    const shakBaseline='evidencia/captura-completa-candidata-20261031/'+val.revisionId+'/registro_antes.json';
    const meliBaseline='evidencia/descuentos-candidatos-20261031/'+val.revisionId+'-registro_antes.json';
    const baseline=exists(originalBaseline)?originalBaseline:exists(shakBaseline)?shakBaseline:meliBaseline;
    if(exists(baseline)){
      const previous=read(baseline);
      assert.equal(previous.revisionId,val.revisionId,ticker+': foto de otra revisión');
      assert.equal(previous.sheet_id,val.sheet_id,ticker+': foto de otra hoja');
      // Excepción contractual acotada: 3-nov-2026 el usuario autorizó expresamente
      // revaluar CMG A3 y conservar la MISMA hoja. No reescribir la foto previa.
      // Solo pasa la recalibración EXACTA sustentada por el 10-Q 3T26, no futuras
      // alteraciones arbitrarias ni otras empresas.
      if(ticker==='CMG' && val.revisionId==='CMG-20261028-A3'
        && val.fechaRevision==='2026-11-03'){
        const near=(a,b)=>typeof a==='number'&&Number.isFinite(a)&&Math.abs(a-b)<1e-7;
        assert.ok(near(previous.valorPrincipal,23.20885152),'CMG: baseline histórica se modificó');
        assert.equal(previous.sheet_id,val.sheet_id,'CMG: debe preservarse la hoja original');
        assert.equal(previous.revisionId,val.revisionId,'CMG: identidad alterada');
        assert.equal(previous.ticker,val.ticker);
        assert.equal(previous.version_metodo,val.version_metodo);
        assert.equal(val.fechaCorteContable,'2026-09-30');
        assert.equal(val.precioReferenciaFecha,'2026-11-02');
        assert.ok(near(val.precio,32.91),'CMG: precio de cierre no coincide');
        assert.ok(near(val.valorPrincipal,25.246494601933065),'CMG: DCF Base no es el recalculado');
        assert.ok(near(val.precioMOS,.65*val.valorPrincipal),'CMG: MOS no se calcula sobre DCF Base');
        assert.ok(near(val.valorEsperado.historias[0].crecimiento,.08398429666167662));
        assert.ok(near(val.valorEsperado.historias[0].margen,.17));
        assert.ok(near(val.valorEsperado.historias[0].s2c,2.2));
        assert.ok(near(val.valorEsperado.historias[0].s2c610,2.05));
        assert.ok(near(val.valorEsperado.historias[0].roicTerminal,.19));
        assert.ok(near(val.sensibilidadDCF.centro,val.valorPrincipal));
        assert.ok(val.fuentes_supuestos.some(s=>s.includes('cmg-20260930.htm')));
        assert.equal(val.auditoriaEconomica,'NO_REALIZADA');
        const matrices=val.sensibilidadMultiples?.matrices||[];
        assert.equal(matrices.filter(m=>m.prioritario).length,5,
          'CMG: cinco matrices prioritarias obligatorias');
        assert.ok(matrices.filter(m=>m.prioritario).every(m=>
          m.estado==='OK'&&Array.isArray(m.matriz)&&m.matriz.length===5&&
          m.matriz.every(row=>row.length===5&&row.every(Number.isFinite))&&
          near(m.matriz[2][2],m.vp3Original)),
          'CMG: matrices prioritarias no conciliadas');
        assert.ok(val.sensibilidadMultiples.metodosPendientes.includes('P/BV'),
          'CMG: no declarar P/BV calculado cuando la hoja lo muestra N/D');
      }else{
        assert.deepStrictEqual(safeCore(val),safeCore(previous),
          ticker+': REGRESIÓN: cambió algún campo ajeno a descuentos/matrices (DCF, ROIC, crecimiento, escenarios, precio, MOS o historia). No fusionar.');
      }
      snapshots++;
    }else withoutSnapshot.push(ticker);
  }
  // DUOL R2 reemplaza la revisión A1 tras el 8-K 3T26, con libro oficial distinto.
  // La foto de A1 permanece como archivo histórico real: no se compara R2 contra
  // supuestos A1 (impediría toda actualización legítima), ni se rebaja el umbral.
  const duolQ3=aEntries.find(([ticker])=>ticker==='DUOL');
  let duolHistoricalProtected=0;
  if(duolQ3 && duolQ3[1].rutaValoracion==='valoraciones/DUOL-20261103-A12-R2.json'){
    const historical=read('valoraciones/DUOL-20261029-A1.json');
    const current=read(duolQ3[1].rutaValoracion);
    assert.equal(historical.revisionId,'DUOL-20261029-A1','La A1 historica no se conserva');
    assert.equal(historical.sheet_id,'14kzULOEY6QFSNF86yCBDZdiE8TNMSiY3abGWg4OH3Ts',
      'Se alteró la hoja de origen de A1');
    assert.ok(Math.abs(historical.valorPrincipal-136.6764524)<1e-7,
      'El DCF de la fotografía A1 fue reescrito');
    assert.equal(current.revisionId,'DUOL-20261103-A12-R2');
    assert.equal(current.sheet_id,'1_-Rxwq04iuXvS1FNpYuwlaAkGEeBxUsuyblIZAx_Oqc');
    assert.ok(Math.abs(current.valorPrincipal-139.10868578744447)<1e-7,
      'No coincide DCF Q3 registrado');
    assert.ok(Math.abs(current.precioMOS-current.valorPrincipal*.65)<1e-7,
      'DUOL: MOS35% no concilia');
    assert.ok(current.sensibilidadMultiples?.matrices?.filter(m=>
      m.prioritario&&m.estado==='OK'&&Array.isArray(m.matriz)&&
      m.matriz.length===5&&m.matriz.every(row=>
        row.length===5&&row.every(Number.isFinite))&&
      Math.abs(m.matriz[2][2]-m.vp3Original)<1e-7).length===5,
      'DUOL R2: cinco matrices Base prioritarias no conciliadas');
    duolHistoricalProtected=1;
  }
  // Nueva revisión DUOL Atlas R1: se preservan íntegramente las fotografías
  // oficiales anteriores A1 y R2. La promoción legítima cambia solo la
  // selección del catálogo; jamás recalcula ni sobrescribe las anteriores.
  if(duolQ3 && duolQ3[1].rutaValoracion==='valoraciones/DUOL-20261105-ATLAS-R1.json'){
    const a1=read('valoraciones/DUOL-20261029-A1.json');
    const r2=read('valoraciones/DUOL-20261103-A12-R2.json');
    const atlas=read(duolQ3[1].rutaValoracion);
    assert.equal(a1.revisionId,'DUOL-20261029-A1');
    assert.equal(a1.sheet_id,'14kzULOEY6QFSNF86yCBDZdiE8TNMSiY3abGWg4OH3Ts');
    assert.ok(Math.abs(a1.valorPrincipal-136.6764524)<1e-7);
    assert.equal(r2.revisionId,'DUOL-20261103-A12-R2');
    assert.equal(r2.sheet_id,'1_-Rxwq04iuXvS1FNpYuwlaAkGEeBxUsuyblIZAx_Oqc');
    assert.ok(Math.abs(r2.valorPrincipal-139.10868578744447)<1e-7,
      'DUOL R2 histórica se reescribió');
    assert.equal(atlas.revisionId,'DUOL-20261105-ATLAS-R1');
    assert.equal(atlas.sheet_id,'1K0yBSETJQkWjdAHRy6Os-3iQ5dmHW_bc88LTMXhUxYU');
    assert.ok(Math.abs(atlas.valorPrincipal-108.22722652829991)<1e-7,
      'DUOL Atlas Base no corresponde a hoja fuente');
    assert.ok(Math.abs(atlas.precioMOS-atlas.valorPrincipal*.65)<1e-7,
      'DUOL Atlas MOS35% incorrecto');
    const grids=atlas.sensibilidadMultiples?.matrices?.filter(m=>
      m.prioritario&&m.estado==='OK'&&Array.isArray(m.matriz)&&
      m.matriz.length===5&&m.matriz.every(row=>
        row.length===5&&row.every(Number.isFinite))&&
      Math.abs(m.matriz[2][2]-m.vp3Original)<1e-7);
    assert.equal(grids?.length,5,'DUOL Atlas: cinco matrices Base sin conciliar');
    const d=atlas.descuentoMultiples;
    assert.ok(Math.abs(d.pesoDcf-.6)<1e-10&&Math.abs(d.pesoMultiplos-.4)<1e-10);
    assert.ok(Math.abs(d.ponderadoHoy.base-
      (d.dcfHoy.base*.6+d.multiplesHoy.base*.4))<1e-7,
      'DUOL Atlas: ponderación no concilia');
    duolHistoricalProtected=1; // foto A1/R2 conservadas y R1 validada
  }
  // La transición Floyd R5 preserva el Uber F1-F5 en archivo-v1 y en el árbol
  // original no activo. Sigue contando como fotografía protegida, pero solo
  // tras verificar igualdad exacta y el valor Base de la revisión histórica.
  if(cat.controlModeloA?.empresas?.UBER?.rutaValoracion==='valoraciones/UBER-REBOOT-3T26-R1.json'){
    const prev=read('valoraciones/UBER-FLOYD-3T26.json');
    const archived=read('archivo-v1/valoraciones/UBER-FLOYD-3T26.json');
    const archivedAnalysis=read('archivo-v1/analisis/UBER-research-UBER-FLOYD-3T26.json');
    assert.deepEqual(archived,prev,'Se alteró la fotografía Floyd anterior');
    assert.equal(prev.revisionId,'UBER-FLOYD-3T26');
    assert.ok(Math.abs(prev.valorPrincipal-100.19381867706664)<1e-8,'Floyd previo cambió de valor');
    assert.equal(archivedAnalysis.revisionId,prev.revisionId,'Floyd previo sin su análisis');
    assert.ok(cat.archivoFloyd.valoraciones.includes('archivo-v1/valoraciones/UBER-FLOYD-3T26.json'));
    floydHistoricoProtegido++;
  }
  assert.ok(snapshots+duolHistoricalProtected+floydHistoricoProtegido>=16,
    'Desaparecieron fotografías financieras de control');
  console.log('PASS no regresión: '+htmlPairs+'/'+aEntries.length+' expedientes vinculados; '+snapshots+
    ' fotografías de baseline y '+duolHistoricalProtected+
    ' fotografía DUOL A1 conservada con R2 verificada; sin relajar mínimos.');
  console.log('Sin fotografía antigua integral: '+withoutSnapshot.join(', ')+
    '. Requieren cotejo con Google Sheets antes de completar matrices.');
  console.log('Este PASS no acredita fórmulas, datos posteriores ni QA visual.');
  return {htmlPairs,snapshots,withoutSnapshot};
}
if(require.main===module)run();
module.exports={run,safeCore};
