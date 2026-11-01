'use strict';
const test=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path');
const {validateReviewRelatives}=require('../validar_relativos_revision.cjs');
const root=path.resolve(__dirname,'../..');
const cat=JSON.parse(fs.readFileSync(path.join(root,'catalogo.json')));
for(const ticker of ['UBER','GOOGL','INTU','NU']){
 // INTU y NU son CANDIDATO (fuera del catálogo) desde el 1-nov-2026; se siguen validando desde candidatos/.
 const rel=cat.valoraciones.find(p=>p.startsWith('valoraciones/'+ticker+'-'))||'candidatos/valoraciones/'+ticker+'-20261029-R1/VALORACION_A12_EN_REVISION.json';
 const v=JSON.parse(fs.readFileSync(path.join(root,rel)));
 test(ticker+': contrastes provisionales trazables, sin certificación ni peso DCF',()=>assert.equal(validateReviewRelatives(v),true));
 test(ticker+': rechaza corrupción, pesos, certificación, moneda y MOS',()=>{
  for(const mutate of [x=>x.sensibilidadMultiples.matrices[0].matriz[0][0]+=1,x=>x.sensibilidadMultiples.matrices[0].peso=.1,x=>x.sensibilidadMultiples.certificado=true,x=>x.sensibilidadMultiples.matrices[0].unidadResultado='BRL/accion',x=>x.precioMOS+=.01,x=>x.sensibilidadMultiples.sourceSheetId='otro',x=>x.sensibilidadMultiples.resultadosSha256='0'.repeat(64)]){
   const x=structuredClone(v);mutate(x);assert.throws(()=>validateReviewRelatives(x));
  }
 });
}
test('MOS histórico redondeado es válido; diferencia de un centavo se rechaza',()=>{
 const {validateRecord}=require('../auditar_integridad.cjs');
 for(const t of ['CELH','NFLX']){
  const v=JSON.parse(fs.readFileSync(path.join(root,cat.valoraciones.find(p=>p.startsWith('valoraciones/'+t+'-')))));
  validateRecord(v);v.precioMOS+=.01;assert.throws(()=>validateRecord(v),/MOS/);
 }
});
