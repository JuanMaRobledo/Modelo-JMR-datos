'use strict';
const test=require('node:test'),assert=require('node:assert/strict');
const fs=require('node:fs'),path=require('node:path');
const root=path.resolve(__dirname,'../..');
const rev='MSFT-20261028-R1';
const read=p=>JSON.parse(fs.readFileSync(path.join(root,p),'utf8'));
const near=(a,b)=>typeof a==='number'&&typeof b==='number'&&Math.abs(a-b)<=Math.max(1e-6,Math.abs(b)*1e-8);
test('MSFT: 15 descuentos nativos, fórmulas y 3 consolidados sin cambios de DCF',()=>{
 const original=read('evidencia/descuentos-nativos-20261031/'+rev+'/registro_antes.json');
 const evidence=read('evidencia/descuentos-nativos-20261031/'+rev+'/valores-y-formulas.json');
 const active=read('valoraciones/'+rev+'.json');
 assert.equal(evidence.sourceSheetId,original.sheet_id);
 assert.equal(evidence.revisionId,original.revisionId);
 assert.equal(active.revisionId,original.revisionId);
 assert.equal(active.estado,'EN_REVISION');
 assert.equal(active.valorPrincipal,original.valorPrincipal);
 assert.equal(active.precioMOS,original.precioMOS);
 assert.deepEqual(
   Object.fromEntries(Object.entries(active).filter(([k])=>k!=='descuentoMultiples')),
   Object.fromEntries(Object.entries(original).filter(([k])=>k!=='descuentoMultiples')));
 const d=active.descuentoMultiples,old=original.descuentoMultiples;
 assert.equal(d.pesoDcf,old.pesoDcf);
 assert.equal(d.pesoMultiplos,old.pesoMultiplos);
 assert.deepEqual(d.dcfHoy,old.dcfHoy);
 assert.equal(d.integracionNativa.certificadoEconomico,false);
 const rows=evidence.values,formula=evidence.formulas;
 for(const [s,base,c] of [['conservador',10,2],['base',19,3],['optimista',28,4]]){
   assert.ok(near(d.dcfHoy[s],rows[37][c]));
   assert.ok(near(d.multiplesHoy[s],rows[38][c]));
   assert.ok(near(d.ponderadoHoy[s],rows[39][c]));
   assert.ok(near(d.ponderadoHoy[s],d.pesoDcf*d.dcfHoy[s]+d.pesoMultiplos*d.multiplesHoy[s]));
   let weighted=0;
   for(let i=0;i<5;i++){
     const m=d.metodos[i],r=rows[base+i],fr=formula[base+i];
     assert.equal(m.nombre,r[0]);
     assert.equal(m.peso,old.metodos[i].peso);
     assert.ok(near(m.peso,r[1]));
     assert.equal(r[10],'OK');
     assert.deepEqual(m[s].fy,r.slice(3,6));
     assert.deepEqual(m[s].vp,r.slice(6,9));
     assert.ok(near(m[s].consolidado,r[9]));
     assert.ok(fr.slice(3,10).every(x=>typeof x==='string'&&x.startsWith('=')));
     weighted+=m.peso*m[s].consolidado;
   }
   assert.ok(near(weighted/d.pesoMultiplos,d.multiplesHoy[s]));
 }
});