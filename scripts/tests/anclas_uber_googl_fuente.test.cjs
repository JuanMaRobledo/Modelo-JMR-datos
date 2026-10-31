'use strict';
const test=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs'),path=require('node:path');
const root=path.resolve(__dirname,'../..');
const read=p=>JSON.parse(fs.readFileSync(path.join(root,p),'utf8'));
test('UBER/GOOGL: no aprobar 5 matrices dependientes sin anclas relativas independientes',()=>{
 const doc=read('evidencia/diagnostico-anclas-uber-googl-20261031.json');
 assert.equal(doc.kind,'ANCLAS_LEIDAS_NO_CERTIFICADAS');
 assert.equal(doc.records.length,2);
 for(const [ticker,revision] of [['UBER','UBER-20261030-A1'],['GOOGL','GOOGL-20261029-R5']]){
  const e=doc.records.find(z=>z.ticker===ticker);
  const v=read('valoraciones/'+revision+'.json');
  assert.ok(e);
  assert.equal(e.revisionId,v.revisionId);
  assert.equal(e.sourceSheetId,v.sheet_id);
  assert.equal(e.dcfUnchanged,v.valorPrincipal);
  assert.equal(v.estado,'EN_REVISION');
  assert.equal(e.relativeUncertified,true);
  assert.equal(e.method.length,5);
  let derived=0,priceAnchored=0;
  for(const m of e.method){
   assert.equal(m.reviewRequired,true);
   assert.ok(m.positiveHistoricalPoints<2,
     'Hay nuevos datos; revalidar fuentes, no reutilizar una captura vieja');
   assert.ok(m.anchorRange.endsWith('!J19'));
   assert.ok(m.historicalRange.endsWith('!D8:E8'));
   if(m.derivedFromAnotherMultiple){
    assert.match(m.anchorFormulaOrLiteral,/\b(EVEBITDA|EVFCFF|PE|PFCFE|POCF)!\$?J\$?19/);
    derived++;
   }
   if(m.dependsOnCurrentSharePrice){
    assert.match(m.anchorFormulaOrLiteral,/'Input sheet'!\$B\$2[23]/);
    priceAnchored++;
   }
  }
  assert.ok(derived>=3,'Deben explicarse las dependencias de anclas');
  assert.ok(priceAnchored>0||ticker==='GOOGL');
  // Mientras las únicas anclas registradas sean las de esta fotografía,
  // no se permite convertir estas matrices en una certificación económica.
  // La corrección posterior exige nueva evidencia independiente por método
  // y reemplazar este test por la validación de esa fuente.
  assert.ok(!(v.sensibilidadMultiples?.matrices?.length>0),
    ticker+': matrices incorporadas sin revisar la evidencia de anclas');
  const secondary=v.descuentoMultiples?.ponderadoHoy;
  // En revisiones existentes, UBER conserva un objeto con tres null;
  // GOOGL conserva null. Ninguna salida numérica puede estar publicada.
  assert.ok(secondary==null ||
    (typeof secondary==='object' && !Array.isArray(secondary) &&
      ['conservador','base','optimista'].every(s=>secondary[s]==null) &&
      Object.values(secondary).every(n=>n==null)),
    ticker+': valoración relativa numérica publicada sin fuentes independientes');
 }
});
