#!/usr/bin/env node
'use strict';
// Gate Floyd para cada empresa VIGENTE: identidad, N1+N2 y referencias de los dos libros.
// La calidad económica se audita por F5 independiente; no se certifica aquí.
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const root=path.resolve(__dirname,'..'),c=JSON.parse(fs.readFileSync(path.join(root,'catalogo.json'),'utf8'));
const val=new Map();
for(const p of c.valoraciones||[]){
  const v=JSON.parse(fs.readFileSync(path.join(root,p),'utf8'));
  if(v.perfil_valoracion!=='Floyd')continue;
  assert.ok(!val.has(v.ticker),v.ticker+': más de una valoración activa');
  val.set(v.ticker,{v,p});
}
assert.ok(val.size>0,'El catálogo no tiene empresas Floyd activas');
const seen=new Set();
for(const p of c.analisis||[]){
  const a=JSON.parse(fs.readFileSync(path.join(root,p),'utf8')),o=val.get(a.ticker);
  if(!o)continue;
  const {v}=o;
  assert.ok(!seen.has(a.ticker),'Más de un análisis activo: '+a.ticker);
  seen.add(a.ticker);
  assert.equal(a.revisionId,v.revisionId,a.ticker+': revisión de análisis distinta');
  assert.equal(a.linkedValuation?.sourcePath,o.p,a.ticker+': fuente del análisis desactualizada');
  assert.equal(a.linkedValuation?.valorPrincipal,v.valorPrincipal);
  assert.equal(a.status,'EN_REVISION',a.ticker+': no declarar sin auditoría F5');
  assert.equal(v.estado,'EN_REVISION',a.ticker+': estado económico inconsistente');
  assert.equal(a.documentos?.nivel1,v.libros?.analisis);
  assert.equal(a.documentos?.nivel2,v.libros?.analisis);
  assert.ok((a.articleHtml||'').length>10000,a.ticker+': falta Nivel 1');
  assert.ok((a.calculationHtml||'').length>5000,a.ticker+': falta Nivel 2');
  assert.equal(a.controlCobertura?.nivel1,true);
  assert.equal(a.controlCobertura?.nivel2,true);
  assert.equal(a.controlCobertura?.auditoriaEconomicaIndependiente,false);
  assert.equal(a.controlCobertura?.centrosDCFValidados,3);
  const matricesAplicables=(v.sensibilidadMultiples?.matrices||[]).filter(m=>m.estado==='OK').length;
  assert.ok(matricesAplicables>=4,a.ticker+': se requieren al menos cuatro anclas válidas');
  assert.equal(a.controlCobertura?.centrosMultiplesValidados,matricesAplicables);
  const count=s=>String(s||'').replace(/<[^>]*>/g,' ').trim().split(/\s+/).filter(Boolean).length;
  const n=count(a.articleHtml);
  if(n<7500)console.warn('PENDIENTE_EDITORIAL: '+a.ticker+': Nivel 1 '+n+' palabras; no declarar investigación extensa definitiva.');
  console.log('FLOYD '+a.ticker+' '+v.revisionId+' · Nivel1 '+n+' palabras · Nivel2 presente · F5 pendiente');
}
assert.equal(seen.size,val.size,'Empresa Floyd sin análisis activo');
console.log('PASS estructural Floyd: '+val.size+' empresas emparejadas. No sustituye F5 ni QA visual.');
