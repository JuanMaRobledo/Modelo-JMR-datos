'use strict';
const test=require('node:test');
const assert=require('node:assert/strict');
const {validateNativeMatrices}=require('../validar_catalogo.cjs');
const names=['EV/EBITDA','EV/FCFF','P/E','P/FCFE','P/OCF','P/V','P/BV'];
function fixture(){
  const m=names.map((name,i)=>({metodo:name,escenario:'base',ancla:'JMR',estado:'OK',
    origen:"'Sensibilidad por múltiplo'!A"+(76+10*i)+':I'+(84+10*i),
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
    x=>delete x.sensibilidadMultiples.matrices[0].origen,
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
test('N/A derivado de N/D de la hoja exige flujo FY+3 negativo real y peso cero',()=>{
  const make=()=>{
    const v=fixture(),m=v.sensibilidadMultiples.matrices[1];
    m.estado='N/A';m.estadoFuente='N/D';m.matriz=null;m.centro=null;m.vp3Original=-3;
    m.motivo='Flujo FY+3 negativo y descuento negativo: método no aplicable con peso cero';
    const d=v.descuentoMultiples.metodos[1];
    d.peso=0;d.estado='N/A: flujo negativo';d.base={fy:[-2,-3,-4],vp:[-1,-2,-3]};
    return v;
  };
  assert.equal(validateNativeMatrices(make()),true);
  for(const change of [
    v=>v.descuentoMultiples.metodos[1].base.fy[2]=4,
    v=>v.descuentoMultiples.metodos[1].base.vp[2]=3,
    v=>v.descuentoMultiples.metodos[1].peso=.1,
    v=>v.descuentoMultiples.metodos[1].estado='PENDIENTE',
    v=>v.sensibilidadMultiples.matrices[1].vp3Original=100
  ]){
    const v=make();change(v);
    assert.throws(()=>validateNativeMatrices(v));
  }
});

test('P/V o P/BV son complementarios sin exigir cálculo, salvo peso positivo',()=>{
  const a=fixture(),m=a.sensibilidadMultiples.matrices[6];
  m.estado='N/D';m.matriz=null;m.centro=null;
  a.descuentoMultiples.metodos[6].peso=0;
  assert.equal(validateNativeMatrices(a),true);
  a.descuentoMultiples.metodos[6].peso=.2;
  assert.throws(()=>validateNativeMatrices(a),/N\/D prioritario o con peso positivo/);
});

test('NU rechaza expresamente una matriz industrial aunque contenga P/E, P/FCFE y P/BV',()=>{
  const v=fixture();
  v.ticker='NU';v.revisionId='NU-R1';
  v.metodoPrincipal='DCF FCFE bancario regulatorio — Método A-1.2';
  v.sensibilidadMultiples.revisionId='NU-R1';
  assert.throws(()=>validateNativeMatrices(v),/contrato bancario requerido/);
});

test('contrato bancario sintético exige tres fuentes y VP3 descontado con Ke',()=>{
  const v=fixture();
  v.ticker='NU';v.revisionId='NU-R1';
  v.metodoPrincipal='DCF FCFE bancario regulatorio — Método A-1.2';
  const sources=[['P/E','PE'],['P/FCFE','PFCFE'],['P/BV','PBV']];
  v.descuentoMultiples.metodos=sources.map(([nombre])=>({
    nombre,peso:1/3,base:{vp:[8,9,10]}
  }));
  v.sensibilidadMultiples={
    contrato:'bank-relative-ke-v1',tipo:'MULTIPLOS_BANCARIOS',
    revisionId:'NU-R1',sourceSheetId:'SHEET',
    resultadosSha256:'b'.repeat(64),estadoPublicacion:'INTEGRADO_EN_REVISION',
    controlesTecnicosAprobados:true,certificado:false,
    matrices:sources.map(([metodo,tab])=>({
      metodo,escenario:'base',ancla:'JMR_BANCARIO',estado:'OK',
      origen:"'"+tab+"'!A1:F6",
      anclaHistoricaValidada:true,
      fuenteAncla:'Fuente independiente por cierre fiscal: prueba sintética sin publicación',
      fundamentalFY3:[1,2,3,4,5],multiploElegido:[1,2,3,4,5],
      matriz:Array.from({length:5},()=>[10,10,10,10,10]),
      centro:10,vp3Original:10
    }))
  };
  assert.equal(validateNativeMatrices(v),true);
  for(const change of [
    x=>x.sensibilidadMultiples.matrices[2].origen="'Sensibilidad por múltiplo'!A136:I144",
    x=>x.sensibilidadMultiples.matrices[2].anclaHistoricaValidada=false,
    x=>x.sensibilidadMultiples.matrices[2].estado='N/D',
    x=>x.sensibilidadMultiples.matrices[0].matriz[2][2]=9,
    x=>x.sensibilidadMultiples.matrices.pop(),
    x=>x.descuentoMultiples.metodos[1].base.vp[2]=9
  ]){
    const invalid=clone(v);change(invalid);
    assert.throws(()=>validateNativeMatrices(invalid));
  }
});
