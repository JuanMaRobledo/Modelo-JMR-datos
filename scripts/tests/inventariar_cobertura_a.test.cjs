'use strict';
const test=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const os=require('node:os');
const path=require('node:path');
const {inspect,matrix5x5,chapterCount}=require('../inventariar_cobertura_a.cjs');
const CORE=['EV/EBITDA','EV/FCFF','P/E','P/FCFE','P/OCF'];
test('banca usa tres métodos propios sin exigir los cinco industriales',t=>{
  const {root,put}=fixture();t.after(()=>fs.rmSync(root,{force:true,recursive:true}));
  const v=JSON.parse(fs.readFileSync(path.join(root,'valoraciones/A.json'),'utf8'));
  v.metodoPrincipal='DCF FCFE bancario regulatorio';
  v.descuentoMultiples.metodos=['P/E','P/FCFE','P/BV'].map(nombre=>({nombre}));put('valoraciones/A.json',v);
  const item=inspect(root).empresas.find(x=>x.ticker==='A');
  assert.deepEqual(item.metodosPrioritariosRequeridos,['P/E','P/FCFE','P/BV']);
  assert.equal(item.metodosPrioritariosEnDescuento,3);
  assert.equal(item.excepcionSectorial,'FCFE_BANCARIO');
  assert.ok(!item.issues.some(x=>x.startsWith('Faltan métodos prioritarios')));
});
function fixture(){
  const root=fs.mkdtempSync(path.join(os.tmpdir(),'jmr-inventory-'));
  const put=(p,obj)=>{const dest=path.join(root,p);fs.mkdirSync(path.dirname(dest),{recursive:true});fs.writeFileSync(dest,JSON.stringify(obj));};
  const cat={valoraciones:['valoraciones/A.json','valoraciones/B.json'],analisis:['analisis/A-research.json','analisis/B-research.json'],
    controlModeloA:{empresas:{
      A:{rutaValoracion:'valoraciones/A.json',metodo:'A-1.2',estado:'INCOMPLETA_EN_REVISION',multiplos:'PRINCIPALES_REGISTRADOS_PENDIENTE_AUDITORIA'},
      B:{rutaValoracion:'valoraciones/B.json',metodo:'ANTERIOR',estado:'EXCLUIDA_HASTA_REHACER_A',multiplos:'FUERA_DE_ALCANCE_MODELO_A'}
    }}
  };
  put('catalogo.json',cat);
  put('valoraciones/A.json',{ticker:'A',revisionId:'A-R1',estado:'EN_REVISION',valorPrincipal:100,hojaGoogle:'https://docs.google.com/example',
    descuentoMultiples:{metodos:CORE.map(nombre=>({nombre}))},
    sensibilidadMultiples:{controles:[{metodo:'P/E',escenario:'base',estado:'OK',centro:20,vp3Original:20}],matrices:[]}});
  put('valoraciones/B.json',{ticker:'B',revisionId:'B-R0',valorPrincipal:30});
  put('analisis/A-research.json',{ticker:'A',revisionId:'A-R1',estado:'EN_REVISION',
    linkedValuation:{sourcePath:'valoraciones/A.json',revisionId:'A-R1',valorPrincipal:100},
    remotePath:'analisis/A-research.json',
    articleHtml:Array.from({length:14},(_,i)=>'<h2>'+(i+1)+'. capítulo</h2>').join(''),calculationHtml:'Nivel 2'});
  put('analisis/B-research.json',{ticker:'B',revisionId:'B-R0',linkedValuation:'B-R0',
    articleHtml:Array.from({length:13},(_,i)=>'<h2>'+(i+1)+'. capítulo</h2>').join('')});
  return {root,put};
}
test('cuenta matrices con 25 números, no solo encabezados o centros',()=>{
  assert.equal(matrix5x5({values:Array.from({length:5},()=>[1,2,3,4,5])}),true);
  assert.equal(matrix5x5({values:Array.from({length:5},()=>[1,2,3,4,null])}),false);
  assert.equal(matrix5x5({centro:10}),false);
  assert.equal(chapterCount({articleHtml:'<h2>1. Uno</h2><h2>2. Dos</h2>'}),2);
  assert.equal(chapterCount({articleHtml:'<h2>2. Dos</h2><h2>1. Uno</h2>'}),0);
});
test('separa A incompleta del legado sin fingir homologación ni modificar datos',t=>{
  const {root}=fixture();t.after(()=>fs.rmSync(root,{force:true,recursive:true}));
  const before=fs.readFileSync(path.join(root,'valoraciones/A.json'),'utf8');
  const result=inspect(root);
  assert.equal(result.catalogoTotal,2);
  assert.equal(result.metodoA,1);
  assert.equal(result.legados,1);
  assert.equal(result.metodoAConMatrices5x5,0);
  const a=result.empresas.find(x=>x.ticker==='A');
  assert.equal(a.metodosPrioritariosEnDescuento,5);
  assert.equal(a.controlesBase,1);
  assert.equal(a.matrices5x5Estructurales,0);
  assert.equal(a.nivel1Capitulos,14);
  assert.equal(a.enlace,'REFERENCIA_ESTRUCTURADA');
  assert.equal(a.estadoInventario,'PENDIENTE_EXPORTACION_Y_CONCILIACION');
  assert.equal(result.empresas.find(x=>x.ticker==='B').estadoInventario,'LEGADO_FUERA_MODELO_A');
  assert.equal(fs.readFileSync(path.join(root,'valoraciones/A.json'),'utf8'),before);
});
test('detecta discrepancia numérica de vínculo sin convertirla en cierre',t=>{
  const {root,put}=fixture();t.after(()=>fs.rmSync(root,{force:true,recursive:true}));
  put('analisis/A-research.json',{ticker:'A',revisionId:'A-R1',estado:'EN_REVISION',
    linkedValuation:{sourcePath:'valoraciones/A.json',revisionId:'A-R1',valorPrincipal:85},
    articleHtml:'<h2>1. Inicio</h2>'});
  const a=inspect(root).empresas.find(x=>x.ticker==='A');
  assert.ok(a.issues.includes('Valor principal divergente en vínculo'));
  assert.equal(a.estadoInventario,'PENDIENTE_EXPORTACION_Y_CONCILIACION');
});

test('captura de rango se cuenta como evidencia, nunca como matriz integrada',t=>{
  const {root,put}=fixture();t.after(()=>fs.rmSync(root,{force:true,recursive:true}));
  const vp='valoraciones/A.json',v=JSON.parse(fs.readFileSync(path.join(root,vp),'utf8'));
  v.sheet_id='SHEET-A';put(vp,v);
  const file='candidatos/hoja-multiples/A-R1-captura-rango.json';
  const candidate={tipo:'CAPTURA_ACOTADA_NO_PUBLICADA',ticker:'A',revisionId:'A-R1',
    sourceSheetId:'SHEET-A',hashFotografiaCompleta:null,
    metodos:CORE.map(metodo=>({metodo,prioritario:true,estadoHoja:'OK',
      matriz:Array.from({length:5},()=>[1,2,3,4,5])}))};
  put(file,candidate);
  const result=inspect(root);
  assert.equal(result.metodoAConCapturaParcial,1);
  assert.equal(result.metodoAConCincoMatricesPrioritariasEnCaptura,1);
  assert.equal(result.metodoAConMatrices5x5,0,
    'no declarar matriz oficial solo porque hay captura de rango');
  assert.equal(result.empresas.find(x=>x.ticker==='A').capturaParcialEsSoloCandidata,true);
  candidate.sourceSheetId='OTHER';put(file,candidate);
  const bad=inspect(root);
  assert.equal(bad.metodoAConCapturaParcial,0);
  assert.ok(bad.empresas.find(x=>x.ticker==='A').issues.some(x=>x.includes('Captura parcial sin identidad')));
});

