#!/usr/bin/env node
/* Calidad editorial mínima de estudios ACTIVOS; no valida el DCF ni hechos externos.
 * Uso: node scripts/auditar_profundidad.cjs
 */
'use strict';
const fs=require('node:fs');
const path=require('node:path');
const root=path.resolve(__dirname,'..'), catalog=JSON.parse(fs.readFileSync(path.join(root,'catalogo.json'),'utf8'));
const active=Array.isArray(catalog.analisis)?catalog.analisis:[];
let failed=0;
function countProse(html){
  return String(html||'').replace(/<table\b[\s\S]*?<\/table>/ig,' ')
    .replace(/<(?:script|style)\b[\s\S]*?<\/(?:script|style)>/ig,' ')
    .replace(/<[^>]+>/g,' ').replace(/&(?:nbsp|amp|lt|gt);/gi,' ')
    .replace(/\s+/g,' ').trim().split(/\s+/).filter(Boolean).length;
}
for(const rel of active){
 try{
  if(typeof rel!=='string'||!/^analisis\/[A-Za-z0-9._-]+\.json$/.test(rel))throw Error('ruta no válida');
  const d=JSON.parse(fs.readFileSync(path.join(root,rel),'utf8'));
  const html=String(d.articleHtml||d.html||''),words=countProse(html);
  const paras=(html.match(/<p\b/ig)||[]).length;
  const headings=(html.match(/<h2\b/ig)||[]).length;
  const ticker=path.basename(rel).split('-')[0];
  const rev=d.valoracionRevisionId||d.revisionId;
  let errors=[];
  if(d.ticker!==ticker)errors.push('ticker no coincide con nombre de archivo');
  if(!rev)errors.push('revisión ausente');
  if(words<1800)errors.push('menos de 1.800 palabras de PROSA (tablas excluidas)');
  if(headings<12)errors.push('menos de 12 encabezados de profundidad');
  if(paras<10)errors.push('menos de 10 párrafos de contenido');
  const expanded=(html.match(/data-jmr-depth=/g)||[]).length;
  if(expanded>1)errors.push('ampliación repetida');
  if(errors.length){failed++;console.error('FAIL',ticker,words+' palabras:',errors.join('; '));}
  else console.log('OK',ticker,words+' palabras',headings+' secciones',paras+' párrafos');
 }catch(e){failed++;console.error('FAIL',rel,String(e.message||e));}
}
console.log('\n',active.length+' análisis activos auditados; '+failed+' incumplimientos editoriales.');
if(failed)process.exitCode=1;
