'use strict';
const test=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path');
const root=path.resolve(__dirname,'../..'),read=p=>JSON.parse(fs.readFileSync(path.join(root,p),'utf8')),has=p=>fs.existsSync(path.join(root,p));
const {validateRebootRecord,validateRebootAnalysis}=require('../validar_reboot.cjs'),v=read('valoraciones/UBER-REBOOT-3T26-R1.json'),a=read('analisis/UBER-research-UBER-REBOOT-3T26-R1.json'),c=read('catalogo.json');
test('UBER R5 único Floyd y seis documentos',()=>{
  assert.equal(validateRebootRecord(v),true);
  assert.ok(validateRebootAnalysis(a,v)>=3000);
  assert.deepEqual(c.valoraciones.filter(x=>x.startsWith('valoraciones/UBER-')),['valoraciones/UBER-REBOOT-3T26-R1.json']);
  assert.deepEqual(c.analisis.filter(x=>x.startsWith('analisis/UBER-')),['analisis/UBER-research-UBER-REBOOT-3T26-R1.json']);
});
test('EV/FCFF: N/D solo con peso cero y sin matriz ficticia; si OK, matriz 5×5',()=>{
  const m=v.sensibilidadMultiples.matrices.find(x=>x.metodo==='EV/FCFF');
  if(m.estado==='N/D'){assert.equal(m.peso,0);assert.equal(m.matriz,null);assert.equal(m.centro,null);}
  else{assert.equal(m.estado,'OK');assert.equal(m.matriz.length,5);}
});
test('Floyd antiguo de UBER archivado y fuera del catálogo',()=>{
  assert.ok(!has('valoraciones/UBER-FLOYD-3T26.json'));
  assert.ok(has('archivo-v1/valoraciones/UBER-FLOYD-3T26.json'));
  assert.ok(has('archivo-v1/analisis/UBER-research-UBER-FLOYD-3T26.json'));
  assert.ok(!c.valoraciones.includes('valoraciones/UBER-FLOYD-3T26.json'));
});
