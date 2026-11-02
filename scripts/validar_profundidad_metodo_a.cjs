#!/usr/bin/env node
'use strict';
/* Editorial integrity and coverage check, separate from economic audit. */
const fs=require('node:fs'), path=require('node:path');
const root=path.resolve(__dirname,'..');
const cat=JSON.parse(fs.readFileSync(path.join(root,'catalogo.json'),'utf8'));
const historicalDepth='MELI CELH ADBE BSX CMG NFLX GOOGL MSFT NKE PYPL EPAM ZTS ONON NU NVO INTU'.split(' ');
// Reescrituras completas con el índice vigente de 14 capítulos (1-nov-2026). El análisis anterior se conserva íntegro y
// sus 18 bloques históricos se siguen exigiendo en el archivo conservado; la revisión nueva debe cumplir el mínimo por
// capítulo medido sobre su propio HTML.
const REESCRITAS={INTU:{revision:'INTU-20261101-A12-R1',anterior:'candidatos/valoraciones/INTU-20261029-R1/ANALISIS_A12_EN_REVISION.json'},
 NU:{revision:'NU-20261102-A12-R1',anterior:'candidatos/valoraciones/NU-20261029-R1/ANALISIS_A12_EN_REVISION.json'}};
const selected=Object.entries(cat.controlModeloA?.empresas||{})
 .filter(([,entry])=>entry.metodo==='A-1.2').map(([ticker])=>ticker);
if(!selected.length)throw new Error('No A-1.2 entries in active catalog');
const errors=[],results=[],warnings=[];
const words=h=>String(h||'').replace(/<script\b[\s\S]*?<\/script>/gi,' ')
 .replace(/<style\b[\s\S]*?<\/style>/gi,' ').replace(/<[^>]+>/g,' ')
 .replace(/&(?:[a-z]+|#\d+);/gi,' ').replace(/\s+/g,' ').trim().split(/\s+/).filter(Boolean).length;
for(const t of selected){
 const matching=(cat.analisis||[]).filter(p=>path.basename(p).startsWith(t+'-'));
 const vals=(cat.valoraciones||[]).filter(p=>path.basename(p).startsWith(t+'-'));
 if(matching.length!==1||vals.length!==1){errors.push(t+': expected one analysis and one valuation in active catalog');continue}
 const p=matching[0],vp=vals[0];
 let a,v;try{a=JSON.parse(fs.readFileSync(path.join(root,p),'utf8'));v=JSON.parse(fs.readFileSync(path.join(root,vp),'utf8'))}
 catch(e){errors.push(t+': parse or read: '+e.message);continue}
 const status=a.status??a.estado;
 if(a.status&&a.estado&&a.status!==a.estado)errors.push(t+': conflicting status/estado');
 const h=a.articleHtml||'',n=words(h),heads=[...h.matchAll(/<h2[^>]*>\s*(\d+)\./gi)].map(m=>Number(m[1]));
 const expected14=Array.from({length:14},(_,i)=>i+1);
 const legacy13=Array.from({length:13},(_,i)=>i+1);
 const is14=JSON.stringify(heads)===JSON.stringify(expected14);
 const isLegacy13=JSON.stringify(heads)===JSON.stringify(legacy13);
 const is18Provisional=JSON.stringify(heads)===JSON.stringify(Array.from({length:18},(_,i)=>i+1)) && status==='EN_REVISION' && a.version_metodo==='A-1.2' && /ciclo empresarial/i.test(h) && /ciclo macro/i.test(h);
 if(a.ticker!==t||v.ticker!==t||a.revisionId!==v.revisionId)errors.push(t+': analysis/valuation revision or ticker mismatch');
 if(status!=='EN_REVISION')errors.push(t+': report changed status');
 if(!Number.isFinite(v.valorPrincipal)||v.valorPrincipal<=0)errors.push(t+': active Base value missing');
 if(n<7500)errors.push(t+': only '+n+' words, min=7500');
 if(!is14&&!isLegacy13&&!is18Provisional)errors.push(t+': índice inválido; vigente=14, legado EN_REVISION=13, encontrado='+heads.join(','));
 if(is18Provisional){
   warnings.push(t+': 18 capitulos narrativos en revision; el minimo de 7500 palabras no cambia');
 } else if(isLegacy13){
   if(status!=='EN_REVISION')errors.push(t+': 13 capítulos heredados solo admisibles como EN_REVISION');
   else warnings.push(t+': PENDIENTE_EDITORIAL, separar ciclos para obtener 14 capítulos; no certifica investigación');
 }else if(is14&&!/<h2[^>]*>\s*5\.\s*(?:Ciclos de la empresa, del mercado y de la macroeconomía|Ciclos empresariales, macroeconómicos y de mercado)\s*<\/h2>/i.test(h))
   errors.push(t+': capítulo 5 de ciclos no identificado');
 if(h.includes('data-jmr-depth='))errors.push(t+': redundant generic appendix still present');
 if(/data-editorial-gap=["']true["']/i.test(h))warnings.push(t+': contiene apartados pendientes de investigación; no acredita completitud');
 if(a.html!==h+(a.calculationHtml||''))errors.push(t+': level 1/level 2 HTML no longer reconcile');
 if(a.ampliacionEconomica?.auditoriaEconomicaEjecutada===true)errors.push(t+': editorial expansion must not certify financial audit');
 const reescrita=REESCRITAS[t]&&REESCRITAS[t].revision===a.revisionId;
 if(reescrita){
   const old=JSON.parse(fs.readFileSync(path.join(root,REESCRITAS[t].anterior),'utf8')).articleHtml||'';
   if((old.match(/data-jmr-longform=/g)||[]).length!==18||(old.match(/data-jmr-deep-20261029=/g)||[]).length!==18)
     errors.push(t+': bloques históricos de profundidad económica (18) perdidos en el análisis conservado');
   const per=[...h.matchAll(/<section id="jmr-n1-chapter-\d+">([\s\S]*?)<\/section>/g)].map(m=>words(m[1]));
   if(per.length!==14||Math.min(...per)<330)errors.push(t+': some chapter is too thin');
 }else if(historicalDepth.includes(t)&&t!=='GOOGL'){
   if((h.match(/data-jmr-longform=/g)||[]).length!==18||(h.match(/data-jmr-deep-20261029=/g)||[]).length!==18)
     errors.push(t+': bloques históricos de profundidad económica (18) perdidos');
   if((a.controlProfundidadModeloA?.minimumPerChapter||0)<330)
     errors.push(t+': some chapter is too thin');
 }else if(t==='GOOGL'&&(h.match(/<section id="jmr-goog-r3-\d+"/g)||[]).length!==18)
   errors.push(t+': long Google report damaged');
 results.push({ticker:t,words:n,headings:heads.length,financialRevision:a.revisionId,base:v.valorPrincipal,legacy:isLegacy13});
}
console.log('Método A · profundidad editorial e integridad: '+results.length+'/'+selected.length);
results.forEach(r=>console.log(r.ticker.padEnd(6)+String(r.words).padStart(6)+' palabras | '+r.headings+' capítulos | Base '+r.base));
warnings.forEach(w=>console.warn('AVISO: '+w));
if(errors.length){
 console.error('FALLAS:\n'+errors.map(e=>' - '+e).join('\n'));
 process.exitCode=1;
}else{
 console.log('PASS ESTRUCTURAL: '+results.length+' estudios vinculados; '+results.filter(x=>x.legacy).length+' con formato legado EN_REVISION, '+results.filter(x=>!x.legacy).length+' con índice actual de 14.');
 console.log('Las fichas legadas NO se califican como 14 capítulos ni editorialmente completas.');
 console.log('No sustituye validación de fuentes primarias ni auditoría económica.');
}

