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
test('PAGS: candidato historico no sustituye la revision publicada EN_REVISION',()=>{
 assert.equal(c.ticker,'PAGS');assert.equal(c.metodo_valoracion,'A');assert.equal(c.version_metodo,'A-1.2');
 assert.equal(c.estado,'CANDIDATO_REVISADO');assert.equal(c.estadoPublicacion,'CANDIDATO_NO_PUBLICADO');assert.equal(c.publicationAuthorized,false);
 assert.equal(c.auditoriaEconomica,'NO_REALIZADA');
 const active=(cat.valoraciones||[]).filter(v=>v.startsWith('valoraciones/PAGS-'));
 assert.deepEqual(active,['valoraciones/PAGS-20261030-A12-R1.json']);
 const analyses=(cat.analisis||[]).filter(v=>v.startsWith('analisis/PAGS-'));
 assert.deepEqual(analyses,['analisis/PAGS-research-PAGS-20261030-A12-R1.json']);
 assert.ok(!(cat.valoraciones||[]).some(v=>v.startsWith('candidatos/valoraciones/PAGS-')));
 assert.ok(!(cat.analisis||[]).some(v=>v.endsWith('PAGS-20261030-A12-R1-CANDIDATO.json')));
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
 assert.equal(a.status,'CANDIDATO_REVISADO');assert.equal(a.estadoPublicacion,'CANDIDATO_NO_PUBLICADO');
 assert.ok(a.calculationHtml.includes('12. SALVEDADES'));
});

test('PAGS: 75 sensibilidad celdas recalculadas y ejes completos',()=>{
 const s=c.supuestos,b=c.escenarios.Base;
 const value=(ke,fx,roeShift=0,gShift=0,terminalRoe=null)=>{
   let book=s.patrimonioInicialBRLm,pv=0;
   for(const y of b.periodos){
     pv+=book*(y.roe+roeShift-y.crecimientoCapital-gShift)/(1+ke)**y.t;
     book*=1+y.crecimientoCapital+gShift;
   }
   return (pv+book*((terminalRoe??(b.periodos.at(-1).roe+roeShift))-s.gTerminalBRL)/(ke-s.gTerminalBRL)/(1+ke)**10)/fx/s.accionesDiluidasMillones;
 };
 for(const [name,obj] of Object.entries(c.sensibilidadDCF)){
   const m=obj.matriz;
   assert.equal(m[0].length,6,name+' encabezados');
   assert.ok(m[0].slice(1).every(Number.isFinite),name+' ejes numéricos');
   assert.equal(new Set(m[0].slice(1)).size,5,name+' eje X distinto');
   assert.equal(new Set(m.slice(1).map(r=>r[0])).size,5,name+' eje Y distinto');
   for(let i=1;i<=5;i++)for(let j=1;j<=5;j++){
     const x=m[0][j],y=m[i][0];
     const expected=name==='keVsRoeTerminal'?value(y,s.fxBRLUSD,0,0,x):
       name==='fxVsKe'?value(x,y):value(s.keBRL,s.fxBRLUSD,y,x);
     close(m[i][j],expected,name+' '+i+','+j);
     if(name==='keVsRoeTerminal'){
       if(j>1)assert.ok(m[i][j]>m[i][j-1],'valor aumenta con ROE terminal');
       if(i>1)assert.ok(m[i][j]<m[i-1][j],'valor disminuye con Ke');
     }
   }
   close(m[3][3],c.valorPrincipal,name+' centro real');
 }
});

test('PAGS: no promover con dependencias materiales sin cerrar',()=>{
 assert.equal(c.publicationReady,false);assert.equal(a.publicationReady,false);
 assert.equal(c.cierrePromocion.estado,'BLOQUEADA');
 assert.equal(c.cierrePromocion.capital.recursosLiberables,null);
 assert.equal(c.cierrePromocion.acciones.accionesEconomicasOctubre,null);
 const x=c.cierrePromocion;close(x.capital.capitalElegibleBRLm/x.capital.rwaBRLm,x.capital.ratio,'PR/RWA');
 assert.equal(x.acciones.emitidas-x.acciones.autocartera,x.acciones.circulacionJunio);
 assert.ok(Math.abs(x.diagnosticoTasas.impactoPct)>2);
 assert.ok(x.diagnosticoTasas.mosSoloCambioRf<c.precioMercadoUSD);
});

test('PAGS: evidencia calendario de pago, recompra autorizada y holgura NO distribuible',()=>{
 const e=JSON.parse(fs.readFileSync(path.join(root,'candidatos/valoraciones/PAGS-20261030-A12-R1/evidencia/PUENTE_20261030_DIVIDENDO_CAPITAL.json'),'utf8'));
 const b=JSON.parse(fs.readFileSync(path.join(root,'candidatos/valoraciones/PAGS-20261030-A12-R1/evidencia/BCB_CAPITAL_202606.json'),'utf8'));
 const get=(code)=>b.data.value.find(x=>x.Conta===code).Saldo/1e6;
 assert.equal(e.marketCutoff,'2026-10-30');assert.equal(e.ticker,c.ticker);
 close(e.capital.rwaBRLm,get('79665'),'RWA BCB');
 close(e.capital.regulatoryCapitalBRLm,get('79649'),'PR BCB');
 close(e.capital.additionalCoreCapitalBRLm,get('92999'),'ACP BCB');
 close(e.capital.irrbbBRLm,get('98576'),'IRRBB BCB');
 close(e.capital.capitalRatio,e.capital.regulatoryCapitalBRLm/e.capital.rwaBRLm,'ratio capital');
 close(e.capital.additionalCoreCapitalToRwa,e.capital.additionalCoreCapitalBRLm/e.capital.rwaBRLm,'buffer BCB');
 close(e.capital.min10_5IllustrativeExcessBRLm,e.capital.regulatoryCapitalBRLm-.105*e.capital.rwaBRLm,'simulación 10.5');
 close(e.capital.eightPlusReportedAcpIllustrativeExcessBRLm,e.capital.regulatoryCapitalBRLm-(.08+e.capital.additionalCoreCapitalToRwa)*e.capital.rwaBRLm,'simulación 8+ACP');
 assert.equal(e.capital.availableForEquityDistributionBRLm,null);
 assert.equal(e.dividend.paymentDate,'2026-09-30');
 assert.equal(e.dividend.usdPerShare,.28);
 assert.equal(e.repurchase.authorizationDate,'2026-09-01');
 assert.equal(e.repurchase.sharesRepurchasedSinceAuthorization,null);
 assert.equal(e.repurchase.asOfCutoffShares,null);
 assert.equal(e.controls.doesNotCertifyFCFE,true);
 assert.equal(e.controls.publicationReady,false);
});
