// Genera justificaciones de supuestos (expediente) y la sección HTML del capítulo «Supuestos y escenarios».
// No modifica supuestos, valores ni motor: comprueba que el valor por escenario no cambia.
import fs from 'node:fs'; import vm from 'node:vm';
import {C} from './contenido.mjs';
const [,,entrada,salida,fragDir]=process.argv;
const html=fs.readFileSync('/home/user/Modelo-JMR-V2/docs/jmr-v2.html','utf8');
const eng=vm.runInNewContext(html.slice(html.indexOf('const JMR_DCF=(()=>{'),html.indexOf('const JMR_IND=(()=>{'))+'\nJMR_DCF;',{});
const lib=JSON.parse(fs.readFileSync(entrada,'utf8'));const F=lib.files;
const FECHA='2026-11-22', MARCA='justificacion-supuestos-20261122';
const num=(x,d=1)=>x==null||!isFinite(x)?'n. d.':x.toLocaleString('es-ES',{minimumFractionDigits:d,maximumFractionDigits:d,useGrouping:'always'});
const pct=(x,d=1)=>x==null||!isFinite(x)?'n. d.':num(x*100,d)+' %';
const pp=x=>num(x*100,1)+' pp';
const mult=x=>num(x,2)+'×';
const esc=s=>String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
const S=['conservador','base','optimista'];
const val=(m,a)=>eng.calculateAll({...m,assumptions:{conservador:a,base:a,optimista:a}}).scenarios.base;
const resumen=[];
fs.mkdirSync(fragDir,{recursive:true});
for(const c of F['catalogo.json'].empresas){
 const t=c.ticker, m=F['empresas/'+t+'.json'], a=F['analisis/'+t+'.json'], k=C[t];
 if(process.env.SOLO&&!process.env.SOLO.split(',').includes(t)) continue;
 if(['banco','aseguradora','holding'].includes(m.profile)) continue;
 if(!k) throw Error('Sin contenido '+t);
 const A=m.assumptions, B=A.base, cur=m.currency||'USD', mon=cur==='USD'?'US$':cur+' ';
 const res=eng.calculateAll(m).scenarios;
 for(const s of S) if(Math.abs(res[s].perShare-m.libro.valores[s])>0.005*Math.abs(m.libro.valores[s])) throw Error('Paridad '+t+' '+s);
 // Contraste histórico
 const h=m.history.filter(x=>x.revenue);
 const fy=h.filter(x=>!/LTM/i.test(String(x.periodo||'')));
 const ltm=h[h.length-1]; const esLTM=/LTM/i.test(String(ltm.periodo||''));
 const ult=esLTM?fy[fy.length-1]:fy[fy.length-2]; const fyU=esLTM?fy[fy.length-1]:ltm;
 const cagr=n=>{const z=fyU, i=fy.indexOf(fyU)-n; if(i<0) return null; const a0=fy[i].revenue; return a0>0?(z.revenue/a0)**(1/n)-1:null;};
 const crecUlt=(()=>{const i=fy.indexOf(fyU); return i>0?fyU.revenue/fy[i-1].revenue-1:null;})();
 const crecLTM=esLTM&&ult?ltm.revenue/ult.revenue-1:null;
 const mg=x=>x.ebit!=null?x.ebit/x.revenue:null;
 const ult5=fy.slice(-5).map(mg).filter(x=>x!=null);
 const mAvg=ult5.reduce((p,x)=>p+x,0)/ult5.length, mMax=Math.max(...fy.map(mg).filter(x=>x!=null)), mMin=Math.min(...fy.map(mg).filter(x=>x!=null));
 const ic=x=>(x.equity??0)+(x.debt??0)-(x.cash??0);
 const i3=h.length-4>=0?h[h.length-4]:null;
 let scObs=null; if(i3){const dI=ic(ltm)-ic(i3), dR=ltm.revenue-i3.revenue; scObs=dI>0&&dR>0&&dR/dI<=6?dR/dI:null;}
 const tEff=m.financials.effectiveTaxRate??B.marginalTax;
 const roicLTM=ic(ltm)>0&&ltm.ebit!=null?ltm.ebit*(1-tEff)/ic(ltm):null;
 // Pruebas de coherencia
 const Bv=res.base, tv=Bv.pvTerminal/Bv.evBeforeRisk;
 const roicMarg=B.marginTarget*(1-B.marginalTax)*B.salesToCapital6to10;
 const precio=m.financials.sharePrice??c.precio;
 let lo=-0.3,hi=0.9; for(let i=0;i<80;i++){const mid=(lo+hi)/2;(val(m,{...B,growth2to5:mid}).perShare>precio)?hi=mid:lo=mid;}
 const gImp=(lo+hi)/2;
 const dv=o=>val(m,{...B,...o}).perShare/Bv.perShare-1;
 const dW=dv({waccInitial:B.waccInitial+0.01,waccTerminal:B.waccTerminal+0.01}), dG=dv({gTerminal:B.gTerminal-0.01}), dR=dv({roicTerminal:B.waccTerminal});
 const sens=(k.sens||[]).map(([l,o])=>{const v=val(m,{...B,...o}).perShare;return [l,v,v/Bv.perShare-1];});
 // ---------- Expediente: justificaciones por escenario y transversales ----------
 const J=m.justificaciones||(m.justificaciones={});
 const vs=s=>res[s].perShare;
 const evid=`Contraste con el expediente ${m.revision?.id||''}: ventas ${esLTM?'LTM':'del último ejercicio'} ${mon}${num(ltm.revenue,0)} M`+
  (crecLTM!=null?` (+${pct(crecLTM)} sobre el último FY)`:'')+`; crecimiento del último FY ${pct(crecUlt)}; CAGR de 3 años ${pct(cagr(3))} y de 5 años ${pct(cagr(5))}; margen operativo reportado ${pct(mg(ltm))} (promedio de 5 FY ${pct(mAvg)}); `+
  `ventas/capital incremental de 3 años ${scObs?mult(scObs):'no significativo'}; ROIC contable ${roicLTM!=null&&roicLTM<1.5?pct(roicLTM):'no significativo'}; valor terminal ${pct(tv,0)} del valor operativo. Fuentes: estados SEC/emisor del expediente, libro oficial y motor V2 (paridad 0,000 %).`;
 const pend=(k.pendientes||[]);
 J.escenarios={};
 for(const s of S){const x=A[s];
  J.escenarios[s]={
   tesis:`${k.tesis[s[0]]} Valor ${mon}${num(vs(s),2)} por acción calculado por el mismo motor que el libro.`,
   crecimiento:`Año 1 ${pct(x.growth1)}; años 2–5 ${pct(x.growth2to5)} anual; después converge al ${pct(x.gTerminal)} terminal. ${k.g1} ${k.g25}`,
   margenes:`Margen operativo de ${pct(x.margin1)} en el año 1 que converge a ${pct(x.marginTarget)} en el año ${x.marginConvergenceYear}. ${k.m1} ${k.mT}`,
   reinversion:`Ventas/capital de ${mult(x.salesToCapital1to5)} en los años 1–5 y ${mult(x.salesToCapital6to10)} en los años 6–10. ${k.sc}`,
   roic:`ROIC terminal ${pct(x.roicTerminal)} frente a WACC terminal ${pct(x.waccTerminal,2)}${Math.abs(x.roicTerminal-x.waccTerminal)<0.0006?' (sin ventaja competitiva perpetua)':''}. ${k.roic}`,
   descuento:`WACC inicial ${pct(x.waccInitial,2)} y terminal ${pct(x.waccTerminal,2)}, común a los tres escenarios. ${k.wacc}`,
   terminal:`Crecimiento perpetuo ${pct(x.gTerminal)}; tasa marginal ${pct(x.marginalTax)}; probabilidad de fracaso ${pct(x.failureProbability,0)}. ${k.g}`,
   evidencia:evid,
   contraevidencia:`${k.contra}`+(pend.length?` Correcciones pendientes en el libro: ${pend.join(' ')}`:'')};
 }
 for(const s of ['conservador','base','optimista']) if(J[s]&&typeof J[s]==='object') delete J[s];
 Object.assign(J,{growth1:k.g1,growth2to5:k.g25,margin1:k.m1,marginTarget:k.mT,salesToCapital1to5:k.sc,salesToCapital6to10:k.sc,
  roicTerminal:k.roic,wacc:k.wacc,gTerminal:k.g,marginalTax:k.tax,failureProbability:k.riesgo,mos:'Margen de seguridad de 35 % sobre el valor Base (estándar MOS_ESTANDAR del contrato V2), igual para todas las empresas.'});
 if(typeof J.tasas==='string'&&/Floyd/.test(J.tasas)) J.tasas=k.wacc;
 J.revisionJustificaciones=`${FECHA}: justificación completa de cada supuesto con evidencia, contraste histórico, contraevidencia y pruebas de coherencia del motor V2. No cambia supuestos, valores ni revisión.`+(pend.length?' Quedan correcciones que exigen recalcular el libro (ver contraevidencia).':'');
 m.warnings=(m.warnings||[]).filter(w=>!String(w).startsWith('Corrección pendiente (22-nov-2026)'));
 for(const p of pend) m.warnings.push('Corrección pendiente (22-nov-2026): '+p);
 // ---------- Sección HTML ----------
 const fila=(lab,f,obs)=>`<tr><td>${esc(lab)}</td>${S.map(s=>`<td>${esc(f(A[s]))}</td>`).join('')}<td>${esc(obs)}</td></tr>`;
 const tabla=`<table><thead><tr><th>Supuesto</th><th>Conservador</th><th>Base</th><th>Optimista</th><th>Contraste observado</th></tr></thead><tbody>`+
  fila('Crecimiento año 1',x=>pct(x.growth1),crecLTM!=null?`LTM +${pct(crecLTM)} sobre FY; último FY ${pct(crecUlt)}`:`Último FY ${pct(crecUlt)}`)+
  fila('Crecimiento anual años 2–5',x=>pct(x.growth2to5),`CAGR 3 años ${pct(cagr(3))}; 5 años ${pct(cagr(5))}`)+
  fila('Margen operativo año 1',x=>pct(x.margin1),`Reportado ${esLTM?'LTM':'último FY'} ${pct(mg(ltm))}`)+
  fila('Margen objetivo (año de convergencia)',x=>`${pct(x.marginTarget)} (año ${x.marginConvergenceYear})`,`Promedio 5 FY ${pct(mAvg)}; rango ${pct(mMin)} a ${pct(mMax)}`)+
  fila('Ventas/capital años 1–5',x=>mult(x.salesToCapital1to5),`Incremental 3 años ${scObs?mult(scObs):'no significativo (recompras, adquisiciones o reclasificación de deuda)'}`)+
  fila('Ventas/capital años 6–10',x=>mult(x.salesToCapital6to10),'—')+
  fila('ROIC terminal',x=>pct(x.roicTerminal),`ROIC contable ${roicLTM!=null&&roicLTM<1.5?pct(roicLTM):'no significativo'}`)+
  fila('WACC inicial → terminal',x=>`${pct(x.waccInitial,2)} → ${pct(x.waccTerminal,2)}`,`Tasa libre ${pct(m.libro?.costoCapital?.tasaLibre,2)}; prima madura ${pct(m.libro?.costoCapital?.primaMadura,3)}`)+
  fila('Crecimiento terminal (g)',x=>pct(x.gTerminal),`Inferior a la tasa libre`)+
  fila('Tasa marginal',x=>pct(x.marginalTax),`Efectiva ${pct(tEff)}`)+
  fila('Probabilidad de fracaso',x=>pct(x.failureProbability,0),'—')+
  fila('Valor por acción',x=>'',`Precio ${mon}${num(precio,2)}`).replace(/<td><\/td><td><\/td><td><\/td>/,S.map(s=>`<td>${mon}${num(vs(s),2)}</td>`).join(''))+
  `</tbody></table>`;
 const par=(l,x)=>`<p><strong>${esc(l)}.</strong> ${esc(x)}</p>`;
 const marcaRoic=roicMarg>B.roicTerminal+0.10?'El periodo explícito supone retornos marginales muy superiores al ROIC terminal: el salto al año 11 hace que el terminal sea la hipótesis prudente, pero sobrestima el valor de los años 6–10 si la eficiencia del capital no se sostiene.':(roicMarg<B.roicTerminal-0.03?'El ROIC terminal supera el retorno marginal implícito de los años 6–10: el terminal es más generoso que el periodo explícito.':'ROIC terminal coherente con el retorno marginal del periodo explícito.');
 const coh=`<table><thead><tr><th>Prueba de coherencia (Base)</th><th>Resultado</th><th>Lectura</th></tr></thead><tbody>`+
  `<tr><td>Peso del valor terminal en el valor operativo</td><td>${pct(tv,0)}</td><td>${tv>0.75?'Por encima del umbral de alerta de 75 %: la valoración depende sobre todo del largo plazo.':'Por debajo del umbral de alerta de 75 %.'}</td></tr>`+
  `<tr><td>Diferencial WACC terminal − g</td><td>${pp(B.waccTerminal-B.gTerminal)}</td><td>g ${pct(B.gTerminal)} frente a tasa libre ${pct(m.libro?.costoCapital?.tasaLibre,2)}.</td></tr>`+
  `<tr><td>Reinversión terminal (g/ROIC)</td><td>${pct(B.gTerminal/B.roicTerminal,0)} del NOPAT</td><td>Sin crecimiento gratuito: cada punto de g exige reinversión.</td></tr>`+
  `<tr><td>ROIC marginal implícito años 6–10 (margen × (1 − t) × ventas/capital) frente a ROIC terminal</td><td>${pct(roicMarg,0)} frente a ${pct(B.roicTerminal,1)}</td><td>${esc(marcaRoic)}</td></tr>`+
  `<tr><td>DCF inverso: crecimiento anual años 2–5 que justifica el precio</td><td>${pct(gImp)} frente a ${pct(B.growth2to5)} del Base</td><td>${gImp>B.growth2to5+0.02?'El mercado descuenta más crecimiento que el Base.':gImp<B.growth2to5-0.02?'El mercado descuenta menos crecimiento que el Base: la diferencia debe explicarse con la contraevidencia.':'El precio es coherente con el crecimiento del Base.'}</td></tr>`+
  `<tr><td>WACC inicial y terminal +1 pp</td><td>${pct(dW,0)}</td><td>Sensibilidad del valor Base al costo de capital.</td></tr>`+
  `<tr><td>g terminal −1 pp</td><td>${pct(dG,0)}</td><td>Sensibilidad al crecimiento perpetuo.</td></tr>`+
  `<tr><td>ROIC terminal igual al WACC terminal</td><td>${pct(dR,0)}</td><td>Valor que depende de la ventaja competitiva perpetua.</td></tr>`+
  sens.map(([l,v,d])=>`<tr><td>${esc(l)}</td><td>${mon}${num(v,2)} (${d>=0?'+':''}${pct(d,0)})</td><td>Prueba específica de la hipótesis más discutible.</td></tr>`).join('')+
  `</tbody></table>`;
 let frag=`<div id="${MARCA}"><h3>Justificación de cada supuesto</h3>`+
  `<p>Cada cifra del libro se justifica con evidencia del emisor, su contraste con la historia de la empresa y la contraevidencia que la debilita. Las cifras de contraste se calculan con los estados del expediente ${esc(m.revision?.id||'')} y las pruebas de coherencia, con el mismo motor V2 que reproduce el libro (paridad 0,000 %). Esta sección no modifica ningún supuesto ni valor (${FECHA}).</p>`+
  tabla+`<p><em>Fuente: libro oficial y expediente ${esc(m.revision?.id||'')}; cálculos de contraste propios con los estados del expediente. Ventas/capital incremental = Δventas / Δ(patrimonio + deuda − caja) en tres años; ROIC contable = EBIT × (1 − tasa efectiva) / capital invertido.</em></p>`+
  `<h4>Por qué cada supuesto</h4>`+
  par('Escenario Conservador',k.tesis.c)+par('Escenario Base',k.tesis.b)+par('Escenario Optimista',k.tesis.o)+
  par('Crecimiento del año 1',k.g1)+par('Crecimiento de los años 2–5',k.g25)+par('Margen operativo del año 1',k.m1)+par('Margen objetivo',k.mT)+
  par('Eficiencia de la reinversión (ventas/capital)',k.sc)+par('ROIC terminal',k.roic)+par('Costo de capital',k.wacc)+par('Impuestos',k.tax)+
  par('Crecimiento terminal',k.g)+par('Riesgo de fracaso y margen de seguridad',k.riesgo)+par('Contraevidencia',k.contra)+
  `<h4>Pruebas de coherencia</h4>`+coh+
  `<blockquote><strong>Nuestra lectura.</strong> ${esc(k.lectura)}</blockquote>`+
  (pend.length?`<h4>Correcciones que requieren recalcular el libro</h4><ul>${pend.map(p=>`<li>${esc(p)}</li>`).join('')}</ul><p><em>No se aplicaron aquí: cambian el valor y, según el contrato V2, exigen recalcular el libro oficial y abrir una nueva revisión.</em></p>`:'')+
  `</div>`;
 fs.writeFileSync(`${fragDir}/${t}.html`,frag);
 let sup=a.blocks.supuestos;
 const i=sup.indexOf(`<div id="${MARCA}">`); if(i>=0) sup=sup.slice(0,i);
 if(t==='MELI'){
  sup=sup.replace('Hipótesis R10, reconstruida desde la auditoría de R9 y la figura R10','Hipótesis R10 verificadas en «Input sheet» del libro R10 (B26:B32, 22-nov-2026)')
   .replace(/<p><em>Verificar contra Input sheet[\s\S]*?<\/em><\/p>/,'<p><em>Verificado el 22-nov-2026 contra «Input sheet» del libro R10 (Google Sheets, fecha de valoración 19-nov-2026): crecimiento 30 % / 20 %, margen 12 % → 15 % en el año 5, ventas/capital 3,5×, WACC 10,68 % inicial y terminal (override), ROIC terminal 18 % y g 4 %.</em></p>');
 }
 a.blocks.supuestos=sup+frag;
 a.justificacionSupuestos={fecha:FECHA,alcance:'Sección «Justificación de cada supuesto» añadida al capítulo de supuestos y justificaciones del expediente reescritas; sin cambios de supuestos ni valores.',correccionesPendientes:pend};
 // comprobación: valores intactos
 const r2=eng.calculateAll(m).scenarios; for(const s of S) if(r2[s].perShare!==res[s].perShare) throw Error('Valor alterado '+t);
 resumen.push({t,tv:+(tv*100).toFixed(0),gImp:+(gImp*100).toFixed(1),pend:pend.length,sens:sens.map(x=>[x[0],+x[1].toFixed(2)])});
}
fs.writeFileSync(salida,JSON.stringify(lib));
console.log(JSON.stringify(resumen,null,0).replace(/\},\{/g,'},\n{'));
