#!/usr/bin/env node
'use strict';
// Preflight de UNA revisión, sin IDs sintéticos, sin escribir ni publicar.
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const {validateRebootRecord,validateRebootAnalysis}=require('./validar_reboot.cjs');
function preflight(v,a,c,valuationPath){
  if(v.perfilEmpresa && v.perfilEmpresa!=='operativa')throw Error('Perfil '+v.perfilEmpresa+': usar preflight_sectorial.cjs y un motor compatible; no Ginsu industrial');
  validateRebootRecord(v);validateRebootAnalysis(a,v);
  assert.equal(v.contratoLibros,'floyd-libro-unico-v1','Las revisiones nuevas usan libro único');
  assert.equal(a.ticker,v.ticker,'Ticker del análisis distinto');
  assert.equal(a.linkedValuation?.revisionId,v.revisionId,'Vínculo a otra revisión');
  if(c){
    assert.ok(c.valoraciones.includes(valuationPath),'Valoración fuera del catálogo');
    const item=c.controlModeloA?.empresas?.[v.ticker];
    assert.equal(item?.rutaValoracion,valuationPath,'La app ocultaría la ficha: falta rutaValoracion exacta');
    assert.equal(item?.metodo,'Floyd','Método de clasificación incorrecto');
    assert.ok(['INCOMPLETA_EN_REVISION','COMPLETA'].includes(item?.estado),'Estado de clasificación desconocido');
  }
  return {estado:'ESTRUCTURA_OK',ticker:v.ticker,revisionId:v.revisionId,
    alcance:'JSON y vínculo editorial; exige además gates vivos de la hoja y QA de app. No certifica R6 ni publica.'};
}
module.exports={preflight};
if(require.main===module){
  const [vp,ap,cp]=process.argv.slice(2);
  if(!vp||!ap)throw Error('Uso: node scripts/preflight_floyd.cjs valoraciones/REV.json analisis/REV.json [catalogo.json]');
  const read=p=>JSON.parse(fs.readFileSync(p,'utf8'));
  console.log(JSON.stringify(preflight(read(vp),read(ap),cp?read(cp):null,path.relative(process.cwd(),path.resolve(vp)).split(path.sep).join('/')),null,2));
}
