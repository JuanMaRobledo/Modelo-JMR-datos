'use strict';
const assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
const finite=x=>typeof x==='number'&&Number.isFinite(x);
const near=(a,b)=>finite(a)&&finite(b)&&Math.abs(a-b)<=Math.max(1e-6,Math.abs(b)*1e-8);
function validateReviewRelatives(v,{root=path.resolve(__dirname,'..'),verifySource=true}={}){
 const s=v.sensibilidadMultiples;
 assert.equal(s?.contrato,'review-relative-v1');
 assert.equal(v.estado,'EN_REVISION');assert.equal(v.version_metodo,'A-1.2');
 assert.equal(s.revisionId,v.revisionId);assert.equal(s.sourceSheetId,v.sheet_id);
 assert.equal(s.estadoPublicacion,'INTEGRADO_EN_REVISION');
 assert.equal(s.controlesTecnicosAprobados,true);assert.equal(s.certificado,false);
 assert.equal(s.certificacionEconomica,'NO_CERTIFICADA');assert.equal(s.pesoEnDCFPrincipal,0);
 assert.ok(typeof s.advertencia==='string'&&s.advertencia.length>40);
 assert.match(s.resultadosSha256,/^[a-f0-9]{64}$/);
 assert.ok(s.sourcePath.startsWith('evidencia/relativos-revision-20261031/')&&!s.sourcePath.includes('..'));
 if(verifySource){
  const raw=fs.readFileSync(path.join(root,s.sourcePath));
  assert.equal(crypto.createHash('sha256').update(raw).digest('hex'),s.resultadosSha256,'Fuente alterada');
  const e=JSON.parse(raw);assert.equal(e.revisionId,v.revisionId);assert.equal(e.sheetId,v.sheet_id);
  assert.deepEqual(e.matrices,s.matrices,'Matrices distintas de evidencia');
 }
 const required=s.tipo==='MULTIPLOS_BANCARIOS'?['P/E','P/FCFE','P/BV']:['EV/EBITDA','EV/FCFF','P/E','P/FCFE','P/OCF'];
 assert.equal(new Set(s.matrices.map(m=>m.metodo)).size,s.matrices.length);
 for(const n of required)assert.ok(s.matrices.some(m=>m.metodo===n),'Falta método '+n);
 for(const m of s.matrices){
  assert.equal(m.escenario,'base');assert.equal(m.estado,'OK');assert.equal(m.peso,0);
  assert.equal(m.anclaCertificada,false);assert.ok(m.fuenteAncla?.length>20);assert.ok(m.limitacion?.length>20);
  assert.ok(m.origen?.length>10);assert.equal(m.unidadResultado,'USD/accion');
  const nums=a=>Array.isArray(a)&&a.length===5&&a.every(finite);
  assert.ok(nums(m.fundamentalFY3)&&nums(m.multiploElegido));
  assert.ok(Array.isArray(m.matriz)&&m.matriz.length===5&&m.matriz.every(nums));
  const f=m.formula;assert.equal(f.tipo,'affine-product');assert.ok(finite(f.factor)&&f.factor>0&&finite(f.constante));
  m.matriz.forEach((r,i)=>r.forEach((z,j)=>assert.ok(near(z,f.factor*m.multiploElegido[i]*m.fundamentalFY3[j]+f.constante),'Fórmula/celda no concilia')));
  assert.ok(near(m.matriz[2][2],m.centro)&&near(m.centro,m.vp3Original),'Centro no concilia');
  const d=v.descuentoMultiples?.metodos?.find(x=>x.nombre===m.metodo);
  assert.equal(d?.peso,0);assert.ok(near(d.base?.vp?.[2],m.centro),'VP3 distinto del registro');
 }
 assert.ok(near(v.precioMOS,v.valorPrincipal*(1-v.mos)),'DCF/MOS');
 return true;
}
module.exports={validateReviewRelatives};
