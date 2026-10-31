'use strict';
const test=require('node:test'),assert=require('node:assert/strict');
const fs=require('node:fs'),path=require('node:path');
const root=path.resolve(__dirname,'../..');
const read=p=>JSON.parse(fs.readFileSync(path.join(root,p),'utf8'));
const tol=(x,y)=>typeof x==='number'&&typeof y==='number'&&Math.abs(x-y)<1e-7;
const cases=[['UBER','UBER-20261030-A1'],['GOOGL','GOOGL-20261029-R5']];
for(const [ticker,revision] of cases){
 test(ticker+': no certificar anclas dependientes sin valoración externa',()=>{
  const e=read('evidencia/anclas-20261031/'+revision+'-J19.json');
  const v=read('valoraciones/'+revision+'.json');
  assert.equal(e.ticker,ticker);
  assert.equal(e.revisionId,v.revisionId);
  assert.equal(e.sourceSheetId,v.sheet_id);
  assert.equal(e.type,'EVIDENCIA_ANCLAS_NO_CERTIFICADAS');
  assert.ok(tol(e.recordedDCF,v.valorPrincipal));
  assert.equal(e.methods.length,5);
  assert.ok(e.methods.every(m=>m.certificado===false));
  assert.equal(v.estado,'EN_REVISION');
  const labels=['EVEBITDA','EVFCFF','PE','PFCFE','POCF'];
  assert.deepEqual(e.methods.map(m=>m.name),labels);
  for(const m of e.methods){
   const formula=m.sourceFormulaOrConstant,s=typeof formula==='string'?formula:'';
   const fromPrice=/Input sheet'!\$B\$22|Input sheet'!\$B\$23/.test(s);
   const fromOther=/(EVEBITDA|EVFCFF|PE|PFCFE|POCF)!\$?J\$?19/.test(s);
   if(typeof formula==='number')assert.equal(m.provenance,'CONSTANTE_SIN_SERIE_COTEJADA');
   else if(fromPrice)assert.equal(m.provenance,'LIGADA_A_PRECIO');
   else if(fromOther)assert.equal(m.provenance,'DERIVADA_DE_OTRO_MULTIPLO');
   else assert.equal(m.provenance,'FORMULA_REQUIERE_REVISION');
  }
  // Una matriz aritmética OK en Sheets no certifica el fundamento de J19.
  require('../validar_relativos_revision.cjs').validateReviewRelatives(v);
  assert.equal(v.sensibilidadMultiples.certificado,false);
  assert.equal(e.registered.matrices,0);
  assert.ok(e.methods.some(m=>m.provenance!=='CONSTANTE_SIN_SERIE_COTEJADA'));
  if(ticker==='UBER'){
    assert.ok(tol(e.registered.pesoDcf,1));
    assert.ok(tol(e.registered.pesoMultiplos,0));
    assert.ok(tol(e.sheet.pesoDcf,0.6));
    assert.ok(tol(e.sheet.pesoMultiplos,0.4));
  }
 });
}
