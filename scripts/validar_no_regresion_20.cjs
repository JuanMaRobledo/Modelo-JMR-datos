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
  return Object.fromEntries(Object.entries(v).filter(([k])=>!ALLOWED_NEW_FIELDS.has(k)));
}
function run(){
  const cat=read('catalogo.json');
  const aEntries=Object.entries(cat.controlModeloA?.empresas||{}).filter(([,v])=>v.metodo==='A-1.2');
  assert.equal(aEntries.length,20,'Cambió cantidad de revisiones Método A activas');
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
    assert.equal(a.publicationAuthorized,false,ticker+': análisis autorizado sin QA');
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
    const baseline='evidencia/integracion-nativa-20261030/'+val.revisionId+'/registro_antes.json';
    if(exists(baseline)){
      const previous=read(baseline);
      assert.equal(previous.revisionId,val.revisionId,ticker+': foto de otra revisión');
      assert.equal(previous.sheet_id,val.sheet_id,ticker+': foto de otra hoja');
      assert.deepStrictEqual(safeCore(val),safeCore(previous),
        ticker+': REGRESIÓN: cambió algún campo ajeno a descuentos/matrices (DCF, ROIC, crecimiento, escenarios, precio, MOS o historia). No fusionar.');
      snapshots++;
    }else withoutSnapshot.push(ticker);
  }
  assert.ok(snapshots>=14,'Desaparecieron fotografías financieras de control');
  console.log('PASS no regresión: '+htmlPairs+'/20 expedientes vinculados; '+snapshots+
    ' fotografías financieras sin cambios fuera de descuentos y matrices.');
  console.log('Sin fotografía antigua integral: '+withoutSnapshot.join(', ')+
    '. Requieren cotejo con Google Sheets antes de completar matrices.');
  console.log('Este PASS no acredita fórmulas, datos posteriores ni QA visual.');
  return {htmlPairs,snapshots,withoutSnapshot};
}
if(require.main===module)run();
module.exports={run,safeCore};
