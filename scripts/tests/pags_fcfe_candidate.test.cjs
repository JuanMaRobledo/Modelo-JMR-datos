'use strict';
const {test}=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const root=path.resolve(__dirname,'..','..');
const c=JSON.parse(fs.readFileSync(path.join(root,'candidatos/valoraciones/PAGS-20261030-A12-R1/PAGS-20261030-A12-R1.json'),'utf8'));
const a=JSON.parse(fs.readFileSync(path.join(root,'analisis/PAGS-20261030-A12-R1-CANDIDATO.json'),'utf8'));
const cat=JSON.parse(fs.readFileSync(path.join(root,'catalogo.json'),'utf8'));
const close=(x,y,label)=>assert.ok(Number.isFinite(x)&&Number.isFinite(y)&&Math.abs(x-y)<Math.max(1e-6,1e-9*Math.abs(y)),label+': '+x+' vs '+y);
test('PAGS: revision no publicada ni activada en catalogo',()=>{
 assert.equal(c.ticker,'PAGS');assert.equal(c.metodo_valoracion,'A');assert.equal(c.version_metodo,'A-1.2');
 assert.equal(c.estado,'CANDIDATO_NO_PUBLICADO');assert.equal(c.publicationAuthorized,false);
 assert.equal(c.auditoriaEconomica,'NO_REALIZADA');
 for(const v of cat.valoraciones||[]) assert.ok(!v.includes('PAGS-'));
 for(const v of cat.analisis||[]) assert.ok(!v.includes('PAGS-'));
});
test('PAGS: cuatro FCFE 10 años conciliados en BRL',()=>{
 for(const [name,s] of Object.entries(c.escenarios)){
   assert.equal(s.periodos.length,10,name);
   let book=c.supuestos.patrimonioInicialBRLm,pv=0;
   for(const [i,y] of s.periodos.entries()){
     close(y.capitalInicialBRLm,book,name+' book '+i);
     close(y.utilidadBRLm,book*y.roe,name+' NI '+i);
     close(y.capitalRetenidoBRLm,book*y.crecimientoCapital,name+' reinversion '+i);
     close(y.fcfeBRLm,y.utilidadBRLm-y.capitalRetenidoBRLm,name+' FCFE '+i);
     close(y.vpFCFEBRLm,y.fcfeBRLm/(1+c.supuestos.keBRL)**(i+1),name+' PV '+i);
     book+=y.capitalRetenidoBRLm;close(y.capitalFinalBRLm,book,name+' cierre '+i);
     pv+=y.vpFCFEBRLm;
   }
   const last=s.periodos.at(-1);
   const terminal=book*(last.roe-c.supuestos.gTerminalBRL)/(c.supuestos.keBRL-c.supuestos.gTerminalBRL)/(1+c.supuestos.keBRL)**10;
   close(terminal,s.vpTerminalBRLm,name+' terminal');
   close(pv,s.vpFCFEBRLm,name+' PV10');
   close(pv+terminal,s.equityBRLm,name+' equity');
   close(s.equityBRLm/c.supuestos.fxBRLUSD/c.supuestos.accionesDiluidasMillones,s.valorUSDAccion,name+' USD');
 }
});
test('PAGS: MOS, promedio y centros matrices',()=>{
 close(c.precioMOS,c.valorPrincipal*.65,'MOS 35');
 const sc=c.escenarios,average=(.5*sc.Base.valorUSDAccion+.25*sc.Conservadora.valorUSDAccion+.25*sc.Optimista.valorUSDAccion);
 close(c.valorEsperadoOrdinario,average,'promedio tres');
 close(c.sensibilidadDCF.keVsRoeTerminal.centro,c.valorPrincipal,'centro Ke ROE');
 close(c.sensibilidadDCF.fxVsKe.centro,c.valorPrincipal,'centro FX Ke');
 close(c.sensibilidadDCF.roeVsRetencion.centro,c.valorPrincipal,'centro ROE retencion');
 for(const v of [c.sensibilidadDCF.keVsRoeTerminal,c.sensibilidadDCF.fxVsKe,c.sensibilidadDCF.roeVsRetencion]){
   assert.equal(v.matriz.length,6);
   assert.ok(v.matriz.slice(1).every(x=>x.length===6&&x.every(Number.isFinite)));
 }
 assert.equal(c.multiplos.peso,0);
 assert.equal(c.multiplos.anclasIndependientesCertificadas,false);
});
test('PAGS: nivel editorial en rama, no certificacion economica',()=>{
 const h=a.articleHtml;
 const n=h.replace(/<[^>]+>/g,' ').replace(/\s+/g,' ').trim().split(/\s+/).length;
 assert.ok(n>=7500,'N1 por debajo de 7500 palabras: '+n);
 assert.deepEqual([...h.matchAll(/<h2>\s*(\d+)\./g)].map(x=>Number(x[1])),Array.from({length:14},(_,i)=>i+1));
 assert.match(h,/<h2>5\. Ciclos de la empresa, del mercado y de la macroeconomía<\/h2>/);
 assert.ok(a.controlProfundidadModeloA.minimoPorCapitulo>=330);
 assert.equal(a.status,'CANDIDATO_NO_PUBLICADO');
 assert.ok(a.calculationHtml.includes('12. SALVEDADES'));
});
