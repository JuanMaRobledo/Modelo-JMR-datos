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
const combined={
  ...active,
  valoraciones:[...archive.valoraciones,...active.valoraciones],
  analisis:[...archive.analisis,...active.analisis],
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
