#!/usr/bin/env node
'use strict';
// Evalúa preparación por fases. No escribe, calcula valoraciones ni publica.
const fs=require('node:fs'),assert=require('node:assert/strict');
const {URL}=require('node:url');
const phases=['R1','R2','R3_R4','R5'];
const common={
 R1:['clasificacion','perimetro','metodo'],
 R2:['estados','utilidad_comun','patrimonio_comun','acciones_derechos','fechas_unidades'],
 R3_R4:['tres_historias','fuentes_supuestos','reinversion','riesgo_terminal','contrastes_aplicables','sensibilidades','inverso','firmas_vigentes','integridad_motor'],
 R5:['analisis_14_12','conciliacion_hoja_json','asuntos_visibles','adaptador_sectorial','catalogo_por_revision','qa_app']
};
const profiles={
 banco:{metodo:'FCFE_CAPITAL',tasa:'Ke',sources:['estados','precio','mercado','regulador','capital'],checks:{
  R2:['cartera_provisiones','fondeo_depositos','puente_prudencial_comun'],
  R3_R4:['capital_rwa','restricciones_distribucion','sin_restar_fondeo','exceso_retorno']}},
 aseguradora:{metodo:'EQUITY_DISTRIBUIBLE',tasa:'Ke',sources:['estados','precio','mercado','regulador','capital','reservas','inversiones'],checks:{
  R2:['ramos_y_contabilidad','reservas_reaseguro','activos_pasivos_alm','puente_solvencia_comun'],
  R3_R4:['capital_riesgo_asegurador','restricciones_distribucion','sin_sumar_float_csm','exceso_retorno']}},
 holding:{metodo:'SOTP',tasa:'POR_PARTE',sources:['estados','precio','mercado','participaciones','matriz','partes'],checks:{
  R2:['propiedad_economica','deuda_caja_matriz','clases_y_terceros','propiedad_cruzada'],
  R3_R4:['partes_con_metodo_propio','puente_ev_equity','sin_doble_conteo','costos_impuestos','nav_mercado_separado','descuento_justificado']}}
};
const text=x=>typeof x==='string'&&x.trim().length>0;
const https=x=>{try{return new URL(x).protocol==='https:';}catch{return false;}};
const date=x=>typeof x==='string'&&/^\d{4}-\d{2}-\d{2}$/.test(x)&&!Number.isNaN(Date.parse(x))&&new Date(x).toISOString().slice(0,10)===x;
function template(profile){
 assert.ok(profiles[profile],'Perfil sectorial desconocido');
 const p=profiles[profile],checks=Object.fromEntries(phases.flatMap(phase=>[...common[phase],...(p.checks[phase]||[])].map(key=>[key,{estado:'PENDIENTE',evidencia:null}])));
 return {versionProceso:'sectorial-damodaran-v1',perfilEmpresa:profile,ticker:'',revisionId:'',
  identidad:{subtipo:'',moneda:'',escala:'',claseAccion:'',corteContable:'',fechaValoracion:'',fechaPrecio:'',libroSectorial:'',documentoAnalisis:'',metodoPrincipal:p.metodo,tasaDescuento:p.tasa},
  fuentes:Object.fromEntries(p.sources.map(key=>[key,{url:'',fechaPublicacion:'',corte:'',detalle:''}])),
  controles:checks,snapshot:null,estado:'CANDIDATO',auditoriaEconomica:'NO_REALIZADA'};
}
function preflightSectorial(v){
 assert.equal(v.versionProceso,'sectorial-damodaran-v1','Versión de proceso desconocida');
 const p=profiles[v.perfilEmpresa];assert.ok(p,'Perfil sectorial desconocido');
 const id=v.identidad||{},pending=Object.fromEntries(phases.map(x=>[x,[]]));
 const add=(phase,key)=>pending[phase].push(key);
 for(const field of ['ticker','revisionId'])if(!text(v[field]))add('R1',field);
 for(const field of ['subtipo','moneda','escala','claseAccion'])if(!text(id[field]))add('R1','identidad.'+field);
 for(const field of ['corteContable','fechaValoracion','fechaPrecio'])if(!date(id[field]))add('R1','identidad.'+field);
 if(date(id.corteContable)&&date(id.fechaValoracion)&&id.corteContable>id.fechaValoracion)add('R1','corte posterior a valoración');
 if(date(id.fechaPrecio)&&date(id.fechaValoracion)&&id.fechaPrecio>id.fechaValoracion)add('R1','precio posterior a valoración');
 if(!/^https:\/\/docs\.google\.com\/spreadsheets\/d\/[\w-]+\/edit(?:[?#].*)?$/.test(id.libroSectorial||''))add('R1','libro sectorial válido');
 if(!/^https:\/\/docs\.google\.com\/document\/d\/[\w-]+\/edit(?:[?#].*)?$/.test(id.documentoAnalisis||''))add('R1','documento de análisis válido');
 if(id.libroSectorial?.split('/d/')[1]?.split('/')[0]===id.documentoAnalisis?.split('/d/')[1]?.split('/')[0])add('R1','dos artefactos distintos');
 if(id.metodoPrincipal!==p.metodo||id.tasaDescuento!==p.tasa)add('R1','método/tasa incompatibles con perfil');
 for(const key of p.sources){
  const s=v.fuentes?.[key]||{};
  if(!https(s.url)||!date(s.fechaPublicacion)||!date(s.corte)||!text(s.detalle))add('R2','fuente.'+key);
  else if(date(id.fechaValoracion)&&(s.fechaPublicacion>id.fechaValoracion||s.corte>id.fechaValoracion))add('R2','lookahead.'+key);
  if(key==='precio'&&date(s.corte)&&date(id.fechaPrecio)&&s.corte!==id.fechaPrecio)add('R2','precio con fecha distinta');
 }
 for(const phase of phases)for(const key of [...common[phase],...(p.checks[phase]||[])]){
  const c=v.controles?.[key],e=c?.evidencia;
  if(c?.estado!=='APROBADO'||e?.revisionId!==v.revisionId||!https(e?.url)||!text(e?.detalle))add(phase,'control.'+key);
 }
 const snap=v.snapshot;
 if(!snap||snap.revisionId!==v.revisionId||snap.sourceSheetId!==id.libroSectorial?.split('/d/')[1]?.split('/')[0]||!/^[a-f0-9]{64}$/.test(snap.sha256||''))add('R3_R4','snapshot de esta revisión/hoja y SHA256');
 if(snap){
  const hs=snap.historias||[];
  if(hs.length!==3||new Set(hs.map(h=>h.nombre)).size!==3||!['Conservadora','Base','Optimista'].every(n=>hs.some(h=>h.nombre===n))||!hs.every(h=>Number.isFinite(h.valor)&&Number.isFinite(h.probabilidad)&&h.probabilidad>=0&&h.probabilidad<=1)||Math.abs(hs.reduce((s,h)=>s+(h.probabilidad||0),0)-1)>1e-8)add('R3_R4','tres historias y probabilidades conciliadas');
  const base=hs.find(h=>h.nombre==='Base')?.valor;
  if(!Number.isFinite(base)||!Number.isFinite(snap.valorPrincipal)||Math.abs(snap.valorPrincipal-base)>1e-6||!Number.isFinite(snap.precioMOS)||Math.abs(snap.precioMOS-base*.65)>.005000001)add('R3_R4','principal Base y MOS 35%');
  if(snap.metodo!==p.metodo||snap.tasaDescuento!==p.tasa)add('R3_R4','snapshot con motor/tasa incorrectos');
 }
 const pass={};let previous=true;
 for(const phase of phases){pass[phase]=previous&&pending[phase].length===0;previous=pass[phase];}
 const estado=pass.R5?'CANDIDATO_R5_COMPLETO':pass.R3_R4?'R3_R4_LISTOS':pass.R2?'R2_LISTO':pass.R1?'R1_LISTO':'INCOMPLETO_R1';
 return {perfilEmpresa:v.perfilEmpresa,revisionId:v.revisionId||null,estado,fases:pass,pendientes:pending,
  publicacionAutorizada:false,alcance:'Control de preparación y trazabilidad declarada; no verifica URLs remotas, saldos, SHA contra la hoja, QA ni R6. No publica.'};
}
module.exports={preflightSectorial,template,profiles};
if(require.main===module){
 const [arg,profile]=process.argv.slice(2);
 if(arg==='--plantilla')console.log(JSON.stringify(template(profile),null,2));
 else{if(!arg)throw Error('Uso: node scripts/preflight_sectorial.cjs expediente.json | --plantilla banco|aseguradora|holding');
 const result=preflightSectorial(JSON.parse(fs.readFileSync(arg,'utf8')));console.log(JSON.stringify(result,null,2));if(result.estado!=='CANDIDATO_R5_COMPLETO')process.exitCode=1;}
}
