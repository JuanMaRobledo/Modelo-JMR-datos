'use strict';
const test=require('node:test'),assert=require('node:assert/strict');
const fs=require('node:fs'),path=require('node:path');
const root=path.resolve(__dirname,'../..');
const read=p=>JSON.parse(fs.readFileSync(path.join(root,p),'utf8'));
const eq=(a,b)=>a==null&&b==null||typeof a==='number'&&typeof b==='number'&&Math.abs(a-b)<1e-9;
const entries=read('evidencia/conciliacion-descuentos-20261031.json').entries;
test('6 divergencias de ponderación: prohibido sobreescribir la revisión aprobada por captura actual',()=>{
 const blocked=entries.filter(e=>e.status==='RETENER_SIN_IMPORTAR_HASTA_CONCILIAR_PESOS');
 assert.equal(blocked.length,6);
 for(const e of blocked){
  const v=read('valoraciones/'+e.revisionId+'.json'),d=v.descuentoMultiples||{};
  assert.equal(v.ticker,e.ticker);
  assert.equal(v.sheet_id,e.sourceSheetId);
  assert.equal(v.estado,'EN_REVISION');
  assert.ok(eq(v.valorPrincipal,e.json.dcfBase),'DCF de '+e.ticker+' cambió');
  assert.ok(eq(d.pesoDcf,e.json.pesoDcf),'Peso DCF cambió sin conciliación '+e.ticker);
  assert.ok(eq(d.pesoMultiplos,e.json.pesoMultiplos),'Peso relativo cambió '+e.ticker);
  for(const m of e.methods){
   const current=d.metodos?.find(x=>x.nombre===m.name);
   assert.ok(current,'Falta método '+e.ticker+'/'+m.name);
   assert.ok(eq(current.peso,m.jsonWeight),'Peso alterado sin autorización '+e.ticker+'/'+m.name);
   assert.equal(current.conservador,null);
   assert.equal(current.optimista,null);
  }
  assert.equal(d.multiplesHoy,null,'No publicar valor secundario sin conciliar '+e.ticker);
  assert.ok(!e.jsonVsSheetWeights||!e.methodsMatch,'No pertenece al grupo de seis excepciones');
 }
});
test('MSFT queda fuera del bloqueo después de reconciliación y prueba propia',()=>{
 const msft=entries.find(x=>x.ticker==='MSFT');
 assert.ok(msft && msft.jsonVsSheetWeights && msft.methodsMatch);
 const v=read('valoraciones/'+msft.revisionId+'.json');
 assert.equal(v.descuentoMultiples.integracionNativa.certificadoEconomico,false);
 assert.ok(v.descuentoMultiples.metodos.every(m=>m.base&&m.conservador&&m.optimista));
});
