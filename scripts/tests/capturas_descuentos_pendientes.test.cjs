'use strict';
const test=require('node:test'),assert=require('node:assert/strict');
const fs=require('node:fs'),path=require('node:path');
const root=path.resolve(__dirname,'../..');
const read=p=>JSON.parse(fs.readFileSync(path.join(root,p),'utf8'));
const names=['EV/EBITDA','EV/FCFF','P/E','P/FCFE','P/OCF'];
const cases=[
 ['EPAM','EPAM-20261029-R1'],['NKE','NKE-20261029-R1'],
 ['NVO','NVO-20261029-R1'],['ONON','ONON-20261029-R1'],
 ['PYPL','PYPL-20261029-R1'],['ZTS','ZTS-20261029-R1']
];
const near=(a,b)=>Number.isFinite(a)&&Number.isFinite(b)&&
 Math.abs(a-b)<=Math.max(1e-5,Math.abs(b)*1e-8);
test('seis fotos relativas con 90 filas de método: guardadas y sin publicación ni modificación del DCF',()=>{
 const manifest=read('evidencia/conciliacion-descuentos-20261031.json');
 let count=0,formulas=0;
 for(const [ticker,revision] of cases){
  const e=read('evidencia/capturas-descuentos-pendientes-20261031/'+revision+'.json');
  const v=read('valoraciones/'+revision+'.json');
  const d=v.descuentoMultiples||{},record=manifest.entries.find(x=>x.ticker===ticker);
  assert.ok(record,'falta registro de divergencia '+ticker);
  assert.equal(e.kind,'CAPTURA_DESCUENTOS_NO_PUBLICADA_PESOS_DIVERGENTES');
  assert.equal(e.ticker,ticker);assert.equal(e.revisionId,v.revisionId);
  assert.equal(e.sourceSheetId,v.sheet_id);
  assert.equal(e.dcfPreserved,true);
  assert.equal(e.integrated,false);assert.equal(e.economicAudit,false);
  assert.equal(v.estado,'EN_REVISION');
  assert.ok(near(e.sourceValues[37][3],v.valorPrincipal));
  assert.ok(near(record.json.dcfBase,v.valorPrincipal));
  assert.equal(d.pesoDcf??null,e.oldWeightDcf);
  assert.equal(d.pesoMultiplos??null,e.oldWeightMultiples);
  assert.ok(near(e.newWeightDcf+e.newWeightMultiples,1));
  const checks=e.methodChecks||[];
  assert.equal(checks.length,15);
  for(const [s,start] of [['conservador',10],['base',19],['optimista',28]]){
   for(let i=0;i<5;i++){
    const row=e.sourceValues[start+i],fr=e.sourceFormulas[start+i];
    const chk=checks.find(x=>x.method===names[i]&&x.scenario===s);
    const m=d.metodos[i];
    assert.ok(chk);
    assert.equal(chk.sourceRow,start+i+1);
    assert.equal(row[0],names[i]);assert.equal(row[10],'OK');
    assert.ok(row.slice(3,10).every(Number.isFinite));
    assert.ok(fr.slice(3,10).every(x=>typeof x==='string'&&x.startsWith('=')));
    assert.ok(near(chk.sourceWeight,row[1]));
    assert.equal(chk.jsonWeight,m.peso);
    if(s==='base'){
      assert.ok(near(m.base.vp[2],row[8]));
      assert.ok(near(m.base.consolidado,row[9]));
    }
    count++;formulas+=7;
   }
  }
  // El objetivo relativo de estas seis revisiones NO está integrado.
  assert.equal(d.multiplesHoy,null);
  assert.ok(d.metodos.every(m=>m.conservador===null&&m.optimista===null));
 }
 assert.equal(count,90);assert.equal(formulas,630);
});