'use strict';
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const METHODS=['EV/EBITDA','EV/FCFF','P/E','P/FCFE','P/OCF','P/V','P/BV'],SCENARIOS=['conservador','base','optimista'];
// Older records serialize derived per-share values to six decimals.
// Preserve that precision while rejecting differences material at the model's 0.001 tolerance.
const finite=x=>typeof x==='number'&&Number.isFinite(x),near=(a,b)=>finite(a)&&finite(b)&&Math.abs(a-b)<=Math.max(1e-6,Math.abs(b)*1e-10);
function validateLedger(s,{optional=false}={}){
 const ledger=s.controles||[];assert.ok(optional&&ledger.length===0||ledger.length===21,'Debe haber 21 controles por matriz');
 const ids=new Set();for(const x of ledger){assert.ok(METHODS.includes(x.metodo)&&SCENARIOS.includes(x.escenario));const key=x.metodo+'/'+x.escenario;assert.ok(!ids.has(key),'Control duplicado');ids.add(key);assert.ok(['OK','N/D'].includes(x.estado),'Error de matriz');if(x.estado==='OK')assert.ok(finite(x.centro));else assert.equal(x.centro,null);}
 assert.equal(s.controlesOK,ledger.filter(x=>x.estado==='OK').length,'Contador OK no deriva de bloques');assert.equal(s.noDisponibles,ledger.filter(x=>x.estado==='N/D').length,'Contador N/D no deriva de bloques');assert.equal(s.errores||0,0);
}
function validateRecord(j){
 const s=j.sensibilidadMultiples;
 if(s?.contract==='base-two-anchors-two-families-v1'){
  assert.equal(s.methods,7);assert.deepEqual(s.scenarios,['base']);assert.ok(s.disrupcionFuera);assert.equal(s.matrices.length,28);assert.equal(s.controles.length,28);
  const ids=new Set();let ok=0,nd=0;const aliases={EVEBITDA:'EV/EBITDA',EVFCFF:'EV/FCFF',PE:'P/E',PFCFE:'P/FCFE',POCF:'P/OCF',PV:'P/V',PBV:'P/BV'};
  for(let i=0;i<s.matrices.length;i++){
   const m=s.matrices[i],c=s.controles[i],key=m.method+'/'+m.anchor+'/'+m.family;assert.ok(!ids.has(key));ids.add(key);
   assert.ok(METHODS.includes(aliases[m.method]));assert.ok(['JMR','Observado'].includes(m.anchor));assert.ok(['Tradicional','Económica'].includes(m.family));
   assert.equal(m.x.length,5);assert.equal(m.y.length,5);assert.equal(m.values.length,5);assert.ok(m.values.every(r=>r.length===5));
   assert.equal(c.metodo,aliases[m.method]);assert.equal(c.escenario,'base');assert.equal(c.ancla,m.anchor);assert.equal(c.familia,m.family);
   if(m.expected==null){assert.equal(m.method,'PFCFE');assert.equal(m.anchor,'JMR');assert.ok(m.values.flat().every(v=>v===null));assert.equal(c.estado,'N/D');nd++;}
   else{assert.ok(m.values.flat().every(finite));assert.ok(near(m.values[2][2],m.expected));assert.ok(near(c.centro,m.expected));assert.equal(c.estado,'OK');ok++;}
  }
  assert.equal(ok,s.controlesOK);assert.equal(nd,s.noDisponibles);assert.equal(ok+nd,28);assert.equal(s.errores,0);
 }else{
  assert.ok(s&&s.methods===7&&s.scenarios?.length===3&&s.disrupcionFuera);validateLedger(s);validateLedger(s.economica||{},{optional:true});assert.equal(s.controlesOK+s.noDisponibles,21);
 }
 const principal=j.valorPrincipal;assert.ok(finite(principal)&&finite(j.mos)&&j.mos>=0&&j.mos<1);assert.ok(near(j.precioMOS,principal*(1-j.mos)),'MOS diferente del Base principal');
 if(j.valoracionHolding){assert.equal(j.metodoPrincipal,'SOTP');assert.ok(near(principal,j.valoracionHolding.nav.base));assert.ok(near(j.precioMOS,j.valoracionHolding.umbralMOS));assert.ok(!(j.valoracionHolding.metodos||[]).some(m=>/DCF/i.test(m.nombre||'')&&(m.peso||0)>0));return;}
 const dm=j.descuentoMultiples;assert.equal(dm?.metodos?.length,7);assert.ok(near(j.metodos.reduce((a,m)=>a+(m.peso||0),0),1),'Pesos no suman 100%');const dcf=j.metodos.find(m=>/DCF/i.test(m.nombre));assert.ok(dcf&&near(dcf.peso,dm.pesoDcf));assert.ok(near(dm.pesoDcf+dm.pesoMultiplos,1));
 for(const m of dm.metodos){const saved=j.metodos.find(x=>x.nombre===m.nombre),sel=j.seleccionMultiples?.metodos?.find(x=>x.nombre===m.nombre);assert.ok(saved&&sel&&near(saved.peso,m.peso)&&near(saved.peso,sel.pesoVigente),'Pesos duplicados no concilian');if(m.peso>0){assert.equal(sel.controlCalculo,'OK');assert.ok(!/^N\/D/.test(sel.control));}
  for(const sc of SCENARIOS){const x=m[sc];assert.ok(x&&x.fy?.length===3&&x.vp?.length===3);if(m.peso>0)assert.ok(x.fy.every(finite)&&x.vp.every(finite)&&finite(x.consolidado),'Método activo sin cifras');if(x.vp.every(finite))assert.ok(near(dm.criterio==='Solo 3 años'?x.vp[2]:x.vp.reduce((a,b)=>a+b,0)/3,x.consolidado),'Horizonte incompatible: '+m.nombre);}
 }
 for(const sc of SCENARIOS){const rel=dm.metodos.filter(m=>m.peso>0).reduce((a,m)=>a+m.peso*m[sc].consolidado,0)/dm.pesoMultiplos;assert.ok(near(rel,dm.multiplesHoy[sc]),'Múltiplos no concilian');assert.ok(near(dm.dcfHoy[sc]*dm.pesoDcf+rel*dm.pesoMultiplos,dm.ponderadoHoy[sc]),'Combinación no concilia');}assert.ok(near(principal,dm.dcfHoy.base));
}
function main(){const root=path.join(__dirname,'..'),catalog=JSON.parse(fs.readFileSync(path.join(root,'catalogo.json'),'utf8')),files=catalog.valoraciones.map(p=>path.basename(p));let ok=0,nd=0,total=0;for(const file of files){const j=JSON.parse(fs.readFileSync(path.join(root,'valoraciones',file),'utf8'));try{validateRecord(j);}catch(e){e.message=j.ticker+': '+e.message;throw e;}ok+=j.sensibilidadMultiples.controlesOK;nd+=j.sensibilidadMultiples.noDisponibles;total+=j.sensibilidadMultiples.contract==='base-two-anchors-two-families-v1'?28:21;}assert.equal(ok+nd,total);console.log(JSON.stringify({estado:'OK',empresas:files.length,matricesOK:ok,matricesND:nd,mosSobrePrincipal:true},null,2));}
module.exports={validateRecord,validateLedger};if(require.main===module)main();

