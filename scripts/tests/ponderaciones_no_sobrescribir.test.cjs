'use strict';
const test=require('node:test'),assert=require('node:assert/strict');
const fs=require('node:fs'),path=require('node:path');
const root=path.resolve(__dirname,'../..');
const read=p=>JSON.parse(fs.readFileSync(path.join(root,p),'utf8'));
const eq=(a,b)=>a==null&&b==null||typeof a==='number'&&typeof b==='number'&&Math.abs(a-b)<1e-9;
const entries=read('evidencia/conciliacion-descuentos-20261031.json').entries;
test('6 divergencias de ponderación: resueltas con fotografía nueva, justificación y respaldo de la revisión anterior',()=>{
 const resolved=entries.filter(e=>e.status==='CONCILIADO_20261101');
 const blocked=entries.filter(e=>e.status==='RETENER_SIN_IMPORTAR_HASTA_CONCILIAR_PESOS');
 assert.equal(resolved.length+blocked.length,6);
 for(const e of resolved){
  const v=read('valoraciones/'+e.revisionId+'.json'),d=v.descuentoMultiples||{};
  assert.equal(v.ticker,e.ticker);assert.equal(v.sheet_id,e.sourceSheetId);assert.equal(v.estado,'EN_REVISION');
  assert.ok(eq(v.valorPrincipal,e.jsonAnterior.dcfBase),'DCF de '+e.ticker+' cambió');
  assert.ok(eq(d.pesoDcf,e.resolucion.pesoDcf)&&eq(d.pesoMultiplos,e.resolucion.pesoMultiplos),'Pesos distintos de la resolución '+e.ticker);
  assert.ok(eq(d.pesoDcf,e.source.pesoDcf),'El peso DCF no coincide con la hoja '+e.ticker);
  assert.ok(Math.abs(d.pesoDcf+d.pesoMultiplos-1)<1e-9);
  for(const m of e.methods){
   const c=d.metodos?.find(x=>x.nombre===m.name);
   assert.ok(c,'Falta método '+e.ticker+'/'+m.name);
   assert.ok(eq(c.peso,m.sheetWeight),'Peso distinto de la hoja '+e.ticker+'/'+m.name);
   assert.ok(c.conservador&&c.base&&c.optimista,'Escenario sin resultado '+e.ticker+'/'+m.name);
  }
  assert.ok(typeof d.multiplesHoy?.base==='number','Falta valor de múltiplos '+e.ticker);
  assert.equal(d.integracionNativa.certificadoEconomico,false);
  assert.ok(d.integracionNativa.justificacionPesos&&d.integracionNativa.respaldoAnterior);
  assert.ok(fs.existsSync(path.join(root,e.resolucion.respaldo,e.revisionId+'.json')),'Falta respaldo de la revisión anterior '+e.ticker);
 }
 for(const e of blocked){
  const v=read('valoraciones/'+e.revisionId+'.json'),d=v.descuentoMultiples||{};
  assert.ok(eq(d.pesoDcf,e.json.pesoDcf),'Peso DCF cambió sin conciliación '+e.ticker);
  assert.ok(d.multiplesHoy==null,'No publicar valor secundario sin conciliar '+e.ticker);
 }
});
test('MSFT queda fuera del bloqueo después de reconciliación y prueba propia',()=>{
 const msft=entries.find(x=>x.ticker==='MSFT');
 assert.ok(msft && msft.jsonVsSheetWeights && msft.methodsMatch);
 const v=read('valoraciones/'+msft.revisionId+'.json');
 assert.equal(v.descuentoMultiples.integracionNativa.certificadoEconomico,false);
 assert.ok(v.descuentoMultiples.metodos.every(m=>m.base&&m.conservador&&m.optimista));
});
