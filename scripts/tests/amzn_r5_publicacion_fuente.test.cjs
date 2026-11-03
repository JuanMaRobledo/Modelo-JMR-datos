'use strict';
const test=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
const root=path.resolve(__dirname,'../..'),rev='AMZN-20261102-A12-R5';
const sourcePath='evidencia/captura-hoja-20261103/'+rev+'_captura_numerica.json';
const valPath='valoraciones/'+rev+'.json',analysisPath='analisis/AMZN-research-20261102-A12-R5.json';
const near=(a,b)=>typeof a==='number'&&typeof b==='number'&&Math.abs(a-b)<=Math.max(1e-7,Math.abs(b)*1e-10);
test('AMZN R5: fuente completa SHA-256, DCF, MOS, cinco métodos y revisión única',()=>{
 const raw=fs.readFileSync(path.join(root,sourcePath));
 const h=crypto.createHash('sha256').update(raw).digest('hex');
 const s=JSON.parse(raw),v=JSON.parse(fs.readFileSync(path.join(root,valPath),'utf8'));
 const a=JSON.parse(fs.readFileSync(path.join(root,analysisPath),'utf8'));
 const cat=JSON.parse(fs.readFileSync(path.join(root,'catalogo.json'),'utf8'));
 assert.equal(v.ticker,'AMZN');assert.equal(v.revisionId,rev);
 assert.equal(v.sheet_id,s.sheetId);assert.equal(a.revisionId,rev);
 assert.equal(v.sensibilidadMultiples.resultadosSha256,h);
 assert.equal(v.reporteFuentes.capturaSha256,h);
 assert.equal(v.sensibilidadDCF.capturaSha256,h);
 assert.equal(cat.valoraciones.filter(p=>p===valPath).length,1);
 assert.equal(cat.analisis.filter(p=>p===analysisPath).length,1);
 assert.equal(cat.controlModeloA.empresas.AMZN.rutaValoracion,valPath);
 assert.equal(v.estado,'EN_REVISION');assert.equal(a.estado,'EN_REVISION');
 assert.ok(near(v.valorPrincipal,149.19148575564947));
 assert.ok(near(v.precioMOS,v.valorPrincipal*.65));
 assert.ok(near(s.verifiedNumbers.dcfBase,v.valorPrincipal));
 assert.equal(s.nativeMultipleMatrices.length,7);
 assert.deepEqual(s.nativeMultipleMatrices.map(m=>m.estado),['OK','N/A','OK','OK','OK','N/D','N/D']);
 for(const [i,m] of s.nativeMultipleMatrices.entries()){
  const target=v.sensibilidadMultiples.matrices[i];
  assert.deepEqual(target,m);
  if(m.estado==='OK'){
   assert.equal(m.matriz.length,5);
   assert.ok(m.matriz.every(r=>r.length===5));
   assert.ok(near(m.matriz[2][2],m.centro));
   assert.ok(near(v.descuentoMultiples.metodos[i].base.vp[2],m.vp3Original));
  }
 }
 const na=s.nativeMultipleMatrices[1];
 assert.equal(na.matriz,null);assert.equal(na.vp3Original,null);
 assert.ok(na.fundamentalFY3[2]<0);
 assert.ok(near(na.fundamentalFY3[2],v.nivel2ProyeccionBase[2].fcff));
 assert.equal(v.descuentoMultiples.metodos[1].peso,0);
 const sum=v.metodos.reduce((z,m)=>z+m.peso,0);
 assert.ok(near(sum,1));
 assert.ok(near(v.descuentoMultiples.pesoDcf,.6));
 assert.ok(near(v.descuentoMultiples.pesoMultiplos,.4));
 for(const scenario of ['conservador','base','optimista']){
  assert.ok(near(v.descuentoMultiples.multiplesHoy[scenario],s.relativeDiscountsByScenario[scenario].rel));
  assert.ok(near(v.descuentoMultiples.ponderadoHoy[scenario],s.relativeDiscountsByScenario[scenario].ponderado));
 }
 assert.equal(v.sensibilidadDCF.matrices.length,3);
 for(const m of v.sensibilidadDCF.matrices){assert.equal(m.valores.length,5);assert.ok(m.valores.every(r=>r.length===5));assert.ok(near(m.valores[2][2],v.valorPrincipal));assert.equal(m.centroConciliado,true);}
 assert.equal(a.html,a.articleHtml+a.calculationHtml);
 assert.equal((a.articleHtml.match(/<h2 id="jmr-n1-chapter-\d+">/g)||[]).length,14);
});
test('AMZN R5: fuente no sustituida por cadena hash sin contenido',()=>{
 const raw=fs.readFileSync(path.join(root,sourcePath));
 const v=JSON.parse(fs.readFileSync(path.join(root,valPath),'utf8'));
 assert.notEqual(crypto.createHash('sha256').update(Buffer.from('{}')).digest('hex'),v.sensibilidadMultiples.resultadosSha256);
 assert.ok(raw.length>14000,'La fuente numerica no es una captura parcial vacia');
});
