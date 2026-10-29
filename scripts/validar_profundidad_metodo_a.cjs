#!/usr/bin/env node
'use strict';
/* Editorial integrity and coverage check, separate from economic audit. */
const fs=require('node:fs'), path=require('node:path');
const root=path.resolve(__dirname,'..');
const cat=JSON.parse(fs.readFileSync(path.join(root,'catalogo.json'),'utf8'));
const selected='MELI CELH ADBE BSX CMG NFLX GOOGL MSFT NKE PYPL EPAM ZTS ONON NU NVO INTU'.split(' ');
const errors=[],results=[];
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
 const h=a.articleHtml||'',n=words(h),heads=[...h.matchAll(/<h2[^>]*>\s*(\d+)\./gi)].map(m=>Number(m[1]));
 const matches=Array.from({length:18},(_,i)=>i+1);
 if(a.ticker!==t||v.ticker!==t||a.revisionId!==v.revisionId)errors.push(t+': analysis/valuation revision or ticker mismatch');
 if(a.status!=='EN_REVISION')errors.push(t+': report changed status');
 if(!Number.isFinite(v.valorPrincipal)||v.valorPrincipal<=0)errors.push(t+': active Base value missing');
 if(n<7500)errors.push(t+': only '+n+' words, min=7500');
 if(JSON.stringify(heads)!==JSON.stringify(matches))errors.push(t+': 18 consecutive chapter headings missing, got '+heads.join(','));
 if(h.includes('data-jmr-depth='))errors.push(t+': redundant generic appendix still present');
 if(a.html!==h+(a.calculationHtml||''))errors.push(t+': level 1/level 2 HTML no longer reconcile');
 if(a.ampliacionEconomica?.auditoriaEconomicaEjecutada===true)errors.push(t+': editorial expansion must not certify financial audit');
 if(t!=='GOOGL'){
   if((h.match(/data-jmr-longform=/g)||[]).length!==18||(h.match(/data-jmr-deep-20261029=/g)||[]).length!==18)
     errors.push(t+': 18 integrated economic chapters not present');
   if((a.controlProfundidadModeloA?.minimumPerChapter||0)<330)
     errors.push(t+': some chapter is too thin');
 }else if((h.match(/<section id="jmr-goog-r3-\d+"/g)||[]).length!==18)
   errors.push(t+': long Google report damaged');
 results.push({ticker:t,words:n,headings:heads.length,financialRevision:a.revisionId,base:v.valorPrincipal});
}
console.log('Método A · profundidad editorial e integridad: '+results.length+'/'+selected.length);
results.forEach(r=>console.log(r.ticker.padEnd(6)+String(r.words).padStart(6)+' palabras | '+r.headings+' capítulos | Base '+r.base));
if(errors.length){
 console.error('FALLAS:\n'+errors.map(e=>' - '+e).join('\n'));
 process.exitCode=1;
}else{
 console.log('PASS: 16 estudios vinculados, revisión, profundidad y cálculos técnicos preservados.');
 console.log('No sustituye validación de fuentes primarias ni auditoría económica.');
}
