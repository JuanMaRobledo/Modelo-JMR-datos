'use strict';
const test=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs'),path=require('node:path');
const root=path.resolve(__dirname,'../..');
const read=p=>JSON.parse(fs.readFileSync(path.join(root,p),'utf8'));
const fmt=n=>n.toFixed(3).replace('.',',');
const near=(a,b)=>Number.isFinite(a)&&Number.isFinite(b)&&Math.abs(a-b)<=Math.max(1e-8,Math.abs(b)*1e-9);
test('NU Nivel 2: reconciliar capital requerido/FCFE y 25 celdas sin tocar Nivel 1 ni valoración',()=>{
 const v=read('valoraciones/NU-20261029-R1.json');
 const a=read('analisis/NU-research-NU-20261029-R1.json');
 const original=read('evidencia/nu-fcfe-bancario-20261031/NU-20261029-R1-analisis_antes.json');
 const src=read('evidencia/nu-fcfe-bancario-20261031/NU-20261029-R1-sensibilidad-25-formulas.json');
 assert.equal(v.revisionId,a.revisionId);
 assert.equal(v.revisionId,src.revisionId);
 assert.equal(a.estado,'EN_REVISION');
 assert.equal(v.estado,'EN_REVISION');
 assert.deepEqual(a.articleHtml,original.articleHtml,'Nivel 1 no se debe modificar');
 assert.deepEqual(
   Object.fromEntries(Object.entries(a).filter(([k])=>!['html','calculationHtml'].includes(k))),
   Object.fromEntries(Object.entries(original).filter(([k])=>!['html','calculationHtml'].includes(k))));
 assert.equal(a.html,a.articleHtml+a.calculationHtml);
 assert.ok(!a.calculationHtml.includes('US$1178,754m'));
 assert.ok(!a.calculationHtml.includes('US$3221,915m'));
 assert.ok(a.calculationHtml.includes('US$1636,799m'));
 assert.ok(a.calculationHtml.includes('US$3052,439m'));
 assert.equal((a.calculationHtml.match(/id="jmr-n2-fcfe-bank-native-20261031"/g)||[]).length,1);
 assert.ok(a.calculationHtml.includes('Ke inicial frente a crecimiento terminal'));
 for(let r=0;r<5;r++)for(let c=0;c<5;c++){
  const value=src.matriz[r][c];
  assert.ok(near(value,v.sensibilidadDCF.valorPorAccion[r][c]));
  assert.ok(a.calculationHtml.includes('US$'+fmt(value)),
    'El anexo debe contener el valor original en '+r+','+c);
 }
 assert.ok(near(src.matriz[2][2],v.valorPrincipal));
 assert.equal(v.metodos.find(m=>m.nombre==='DCF FCFE bancario').peso,1);
 for(const name of ['P/E','P/FCFE','P/BV'])
  assert.equal(v.metodos.find(m=>m.nombre===name).peso,null,'Múltiplos aún pendientes');
 assert.equal(v.descuentoMultiples.multiplesHoy,null);
});
