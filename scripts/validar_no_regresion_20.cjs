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
const ALLOWED_NEW_FIELDS=new Set(['descuentoMultiples','sensibilidadMultiples']);
function safeCore(v) {
  // El peso de cada método en `metodos` se deriva de descuentoMultiples (categoría de la hoja): puede cambiar al integrar pesos.
  // Cualquier otro campo de `metodos` sigue protegido.
  const core=Object.fromEntries(Object.entries(v).filter(([k])=>!ALLOWED_NEW_FIELDS.has(k)));
  if(Array.isArray(core.metodos))core.metodos=core.metodos.map(m=>{const {peso,...rest}=m||{};return rest;});
  return core;
}
function run(){
  const cat=read('catalogo.json');
  const aEntries=Object.entries(cat.controlModeloA?.empresas||{}).filter(([,v])=>v.metodo==='A-1.2');
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
  const NUEVAS={META:'META-20261101-A12-R1',NVDA:'NVDA-20261101-A12-R1',XP:'XP-20261031-A12-R1',INTU:'INTU-20261101-A12-R1'};
  const nuevas=Object.entries(NUEVAS).filter(([t,r])=>aEntries.some(([name,v])=>name===t&&path.basename(v.rutaValoracion).startsWith(r))).length;
  assert.equal(aEntries.length,20-DEGRADADAS.length+nuevas,'Se perdieron revisiones A-1.2 originales');
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
    const matches=cat.analisis.filter(p=>path.basename(p).startsWith(ticker+'-'));
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
      assert.deepStrictEqual(safeCore(val),safeCore(previous),
        ticker+': REGRESIÓN: cambió algún campo ajeno a descuentos/matrices (DCF, ROIC, crecimiento, escenarios, precio, MOS o historia). No fusionar.');
      snapshots++;
    }else withoutSnapshot.push(ticker);
  }
  assert.ok(snapshots>=16,'Desaparecieron fotografías financieras de control');
  console.log('PASS no regresión: '+htmlPairs+'/'+aEntries.length+' expedientes vinculados; '+snapshots+
    ' fotografías financieras sin cambios fuera de descuentos y matrices.');
  console.log('Sin fotografía antigua integral: '+withoutSnapshot.join(', ')+
    '. Requieren cotejo con Google Sheets antes de completar matrices.');
  console.log('Este PASS no acredita fórmulas, datos posteriores ni QA visual.');
  return {htmlPairs,snapshots,withoutSnapshot};
}
if(require.main===module)run();
module.exports={run,safeCore};
