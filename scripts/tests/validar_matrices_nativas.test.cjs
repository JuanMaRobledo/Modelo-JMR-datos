'use strict';
const test=require('node:test');
const assert=require('node:assert/strict');
const {validateNativeMatrices}=require('../validar_catalogo.cjs');
const names=['EV/EBITDA','EV/FCFF','P/E','P/FCFE','P/OCF','P/V','P/BV'];
function fixture(){
  const m=names.map(name=>({metodo:name,escenario:'base',ancla:'JMR',estado:'OK',
    fundamentalFY3:[1,2,3,4,5],multiploElegido:[1,2,3,4,5],
    matriz:Array.from({length:5},()=>[10,10,10,10,10]),
    centro:10,vp3Original:10}));
  return {ticker:'SHAK',revisionId:'SHAK-R2',sheet_id:'SHEET',estado:'EN_REVISION',
    descuentoMultiples:{metodos:names.map(nombre=>({nombre,peso:.1,base:{vp:[8,9,10]}}))},
    sensibilidadMultiples:{
      contrato:'base-native-five-priority-v1',revisionId:'SHAK-R2',sourceSheetId:'SHEET',
      resultadosSha256:'a'.repeat(64),estadoPublicacion:'INTEGRADO_EN_REVISION',
      controlesTecnicosAprobados:true,matrices:m
    }};
}
const clone=x=>JSON.parse(JSON.stringify(x));
test('cinco prioritarios y matrices 5x5 conciliadas aprobadas técnicamente',()=>{
  const v=fixture();
  assert.equal(validateNativeMatrices(v),true);
  assert.equal(v.estado,'EN_REVISION');
});
test('candidato, revisión falsa o centro diferente no pasan',()=>{
  const r=fixture();
  for(const change of [
    x=>x.sensibilidadMultiples.estadoPublicacion='CANDIDATO_NO_PUBLICADO',
    x=>x.sensibilidadMultiples.revisionId='OLD',
    x=>x.sensibilidadMultiples.sourceSheetId='OTHER',
    x=>x.sensibilidadMultiples.controlesTecnicosAprobados=false,
    x=>x.sensibilidadMultiples.matrices[0].matriz[2][2]=99,
    x=>x.sensibilidadMultiples.matrices.shift()
  ]){
    const v=clone(r);change(v);assert.throws(()=>validateNativeMatrices(v));
  }
});
test('un N/D prioritario bloquea, N/A justificado con peso cero es válido',()=>{
  const a=fixture(),m=a.sensibilidadMultiples.matrices[1];
  m.estado='N/D';m.matriz=null;m.centro=null;
  assert.throws(()=>validateNativeMatrices(a),/N\/D prioritario/);
  m.estado='N/A';m.motivo='Flujo FCFF negativo: múltiplo no es económicamente interpretable';
  a.descuentoMultiples.metodos[1].peso=0;
  assert.equal(validateNativeMatrices(a),true);
});
test('P/V o P/BV son complementarios sin exigir cálculo, salvo peso positivo',()=>{
  const a=fixture(),m=a.sensibilidadMultiples.matrices[6];
  m.estado='N/D';m.matriz=null;m.centro=null;
  a.descuentoMultiples.metodos[6].peso=0;
  assert.equal(validateNativeMatrices(a),true);
  a.descuentoMultiples.metodos[6].peso=.2;
  assert.throws(()=>validateNativeMatrices(a),/N\/D prioritario o con peso positivo/);
});
