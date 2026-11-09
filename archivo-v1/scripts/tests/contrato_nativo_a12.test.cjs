'use strict';
const test=require('node:test'),assert=require('node:assert/strict');
const fs=require('node:fs'),path=require('node:path');
const root=path.resolve(__dirname,'../..');
const {validateRecord}=require('../auditar_integridad.cjs');
const val=()=>JSON.parse(fs.readFileSync(path.join(root,'valoraciones/SHAK-20261029-A12-R2.json'),'utf8'));
test('Método A admite Base nativa con cinco 5x5 y dos N/A con peso cero',()=>{
 const r=val();assert.equal(r.estado,'EN_REVISION');
 assert.doesNotThrow(()=>validateRecord(r));
});
test('A rechaza modificación del centro, método, ponderación y estado de integración',()=>{
 const mutate=[
  v=>v.sensibilidadMultiples.matrices[0].matriz[2][2]+=1,
  v=>v.sensibilidadMultiples.matrices[1].estado='N/D',
  v=>v.sensibilidadMultiples.matrices[1].motivo='',
  v=>v.descuentoMultiples.metodos.find(m=>m.nombre==='EV/FCFF').peso=.2,
  v=>v.sensibilidadMultiples.estadoPublicacion='CANDIDATO_NO_PUBLICADO',
  v=>v.sensibilidadMultiples.matrices[0].origen='otro',
  v=>v.precioMOS+=1
 ];
 for(const fn of mutate){const r=val();fn(r);assert.throws(()=>validateRecord(r));}
});
test('gate no permite pasar método A como estructura histórica sin matrices',()=>{
 const r=val();delete r.sensibilidadMultiples.contrato;
 assert.throws(()=>validateRecord(r),/BLOQUEO_FINANCIERO/);
});
