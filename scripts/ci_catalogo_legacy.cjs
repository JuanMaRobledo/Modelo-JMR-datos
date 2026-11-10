#!/usr/bin/env node
'use strict';
// Ejecuta controles históricos A-1.2 sobre una vista temporal del catálogo archivado.
// Las fichas Floyd vigentes permanecen guardadas y se restauran SIEMPRE al terminar.
// Nunca se reactivan expedientes en la app ni se escribe en main.
const fs=require('node:fs');
const path=require('node:path');
const {spawnSync}=require('node:child_process');
const root=path.resolve(__dirname,'..'),file=path.join(root,'catalogo.json');
const original=fs.readFileSync(file,'utf8');
const active=JSON.parse(original),archive=active.archivoFloyd;
if(!archive || !Array.isArray(archive.valoraciones)||!Array.isArray(archive.analisis))
  throw new Error('Falta archivoFloyd: no se puede reconstruir el catálogo histórico para auditoría');
// Reconstruir UNA pareja por empresa histórica, no todas las versiones archivadas.
// Las rutas físicas se mantienen dentro de archivo-v1; jamás tocar el catálogo publicado.
const resolveRel = rel => {
  const options = [rel, 'archivo-v1/'+rel];
  return options.find(x=>fs.existsSync(path.join(root,x))) || null;
};
const canonicalValuations=[],canonicalAnalysis=[];
for(const [ticker,selection] of Object.entries(archive.controlModeloA||{})){
  if(selection.metodo!=='A-1.2')continue;
  const valPath=resolveRel(selection.rutaValoracion);
  if(!valPath)throw new Error('Falta valoración A-1.2 archivada '+ticker+': '+selection.rutaValoracion);
  const v=JSON.parse(fs.readFileSync(path.join(root,valPath),'utf8'));
  const sameRevision=(archive.analisis||[]).filter(rel=>{
    const p=resolveRel(rel);
    if(!p)return false;
    try{const a=JSON.parse(fs.readFileSync(path.join(root,p),'utf8'));
      return a.ticker===ticker && a.revisionId===v.revisionId;
    }catch{return false}
  });
  if(sameRevision.length<1)throw new Error('Falta análisis archivado '+ticker+' / '+v.revisionId);
  // Análisis editable previo de mismo revisionId: escoger el de ruta más específica si existen duplicados.
  const analysis=resolveRel(sameRevision.sort((a,b)=>a.length-b.length)[0]);
  canonicalValuations.push(valPath);
  canonicalAnalysis.push(analysis);
}
const combined={
  ...active,
  valoraciones:[...new Set([...canonicalValuations,...active.valoraciones])],
  analisis:[...new Set([...canonicalAnalysis,...active.analisis])],
  auditorias:[...archive.auditorias],
  controlModeloA:{...active.controlModeloA,empresas:{...archive.controlModeloA,...active.controlModeloA.empresas}},
  seleccionesDefinitivas:{...archive.seleccionesDefinitivas,...active.seleccionesDefinitivas}
};
const args=process.argv.slice(2);
if(!args.length)throw new Error('Uso: node scripts/ci_catalogo_legacy.cjs COMANDO [ARG...]');
let code=1;
try{
  fs.writeFileSync(file,JSON.stringify(combined,null,2)+'\n');
  const p=spawnSync(args[0],args.slice(1),{stdio:'inherit',cwd:root,env:{...process.env,JMR_CI_ARCHIVO_LEGADO:'1'}});
  code=p.status??1;
  if(p.error)console.error(p.error);
}finally{
  fs.writeFileSync(file,original);
}
process.exitCode=code;
