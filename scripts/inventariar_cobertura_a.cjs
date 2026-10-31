'use strict';
/**
 * Inventario reproducible SOLO LECTURA de expedientes en catálogo.
 * No calcula valores intrínsecos ni acredita la procedencia de las fórmulas
 * de Google Sheets. El CI financiero sigue siendo un gate independiente.
 */
const fs=require('node:fs');
const path=require('node:path');
const CORE=['EV/EBITDA','EV/FCFF','P/E','P/FCFE','P/OCF'];
const isFiniteNumber=x=>typeof x==='number' && Number.isFinite(x);
const near=(a,b)=>isFiniteNumber(a)&&isFiniteNumber(b)&&Math.abs(a-b)<=Math.max(1e-5,Math.abs(b)*1e-8);
const read=(root,p)=>JSON.parse(fs.readFileSync(path.join(root,p),'utf8'));
const normalize=x=>x==='P/S'?'P/V':x;
function matrix5x5(m){
  const g=m?.values||m?.valores;
  return Array.isArray(g)&&g.length===5&&g.every(r=>Array.isArray(r)&&r.length===5&&r.every(isFiniteNumber));
}
function chapterCount(a){
  const h=a.articleHtml||'';
  const nums=[...h.matchAll(/<h2\b[^>]*>\s*(\d{1,2})\./gi)].map(m=>Number(m[1]));
  return nums.length&&nums.every((n,i)=>n===i+1)?nums.length:0;
}
function inspect(root=path.resolve(__dirname,'..')){
  const cat=read(root,'catalogo.json');
  const reported=[];
  const financialPaths=new Set(cat.valoraciones||[]);
  const analysisPaths=cat.analisis||[];
  for(const [ticker,declared] of Object.entries(cat.controlModeloA?.empresas||{})){
    const pathOfficial=declared.rutaValoracion;
    const issues=[];
    if(!financialPaths.has(pathOfficial)){
      reported.push({ticker,revisionId:null,metodo:declared.metodo,estado:'CATALOGO_INCONSISTENTE',issues:['Ruta financiera no está en catálogo activo']});
      continue;
    }
    let v;
    try{v=read(root,pathOfficial)}catch(e){
      reported.push({ticker,revisionId:null,metodo:declared.metodo,estado:'ARCHIVO_ILEGIBLE',issues:[e.message]});continue;
    }
    if(v.ticker!==ticker)issues.push('Ticker financiero distinto');
    const aPath=analysisPaths.find(p=>p.startsWith('analisis/'+ticker+'-'));
    let a=null;
    if(aPath){try{a=read(root,aPath)}catch(e){issues.push('Análisis ilegible: '+e.message)}}
    else issues.push('Sin análisis en catálogo activo');
    if(a && (a.ticker!==ticker || a.revisionId!==v.revisionId))issues.push('Análisis y valoración de revisiones diferentes');
    let enlace='SIN_ANALISIS';
    if(a){
      const l=a.linkedValuation;
      if(l && typeof l==='object'){
        const pathOK=l.sourcePath===pathOfficial && l.revisionId===v.revisionId;
        if(!pathOK)issues.push('Vínculo con ruta o revisión incorrecta');
        if(l.valorPrincipal!==undefined && !near(l.valorPrincipal,v.valorPrincipal))
          issues.push('Valor principal divergente en vínculo');
        enlace=pathOK?'REFERENCIA_ESTRUCTURADA':'REFERENCIA_INCONSISTENTE';
      } else if(typeof l==='string'){
        enlace=l===pathOfficial||l===v.revisionId?'REFERENCIA_CORTA':'REFERENCIA_INCONSISTENTE';
        if(enlace==='REFERENCIA_INCONSISTENTE')issues.push('Referencia corta no coincide');
      } else {enlace='NO_EXPLICITO';issues.push('Falta vinculación explícita del análisis')}
      if(a.remotePath && a.remotePath!==aPath)issues.push('remotePath diferente de ruta catalogada');
      if(!a.remotePath)issues.push('remotePath no declarado');
    }
    const legacy=declared.metodo!=='A-1.2';
    const dm=v.descuentoMultiples?.metodos;
    const methods=Array.isArray(dm)?dm:[];
    const evaluated=CORE.filter(m=>methods.some(x=>normalize(x.nombre)===m)).length;
    const sens=v.sensibilidadMultiples;
    const controls=Array.isArray(sens?.controles)?sens.controles:[];
    const matrices=Array.isArray(sens?.matrices)?sens.matrices:[];
    const matricesEstructurales=matrices.filter(matrix5x5).length;
    const checked=controls.filter(x=>x.escenario==='base'&&x.estado==='OK'&&near(x.centro,x.vp3Original)).length;
    const noDisponible=controls.filter(x=>x.escenario==='base'&&x.estado==='N/D').length;
    if(!legacy && !matricesEstructurales)issues.push('No se exportaron matrices 5x5 de múltiplos Base verificables');
    if(!legacy && evaluated<CORE.length)issues.push('Faltan métodos prioritarios en descuentoMultiples (o sus exclusiones)');
    if(!legacy && chapterCount(a||{})!==14)issues.push('Nivel 1 no acredita 14 capítulos');
    const item={
      ticker,revisionId:v.revisionId,metodo:declared.metodo,estado:declared.estado,
      clasificacionCatalogo:declared.multiplos,
      enlace,nivel1Capitulos:chapterCount(a||{}),nivel2Presente:!!a?.calculationHtml,
      precioBase:v.valorPrincipal,
      metodosPrioritariosEnDescuento:evaluated,
      controlesBase:controls.filter(x=>x.escenario==='base').length,
      centrosBaseConciliados:checked,
      controlesND:noDisponible,
      matricesExportadas:matrices.length,
      matrices5x5Estructurales:matricesEstructurales,
      hojasOriginales:!!(v.hojaGoogle||v.sheet_id),
      estadoInventario:legacy?'LEGADO_FUERA_MODELO_A':matricesEstructurales?'PENDIENTE_COTEJO_HOJA':'PENDIENTE_EXPORTACION_Y_CONCILIACION',
      issues
    };
    reported.push(item);
  }
  const current=reported.filter(x=>x.metodo==='A-1.2');
  return {
    titulo:'Inventario técnico. NO acredita auditoría ni origen Google Sheets',
    catalogoTotal:(cat.valoraciones||[]).length,
    metodoA:current.length,
    legados:reported.length-current.length,
    metodoAConMatrices5x5:current.filter(x=>x.matrices5x5Estructurales>0).length,
    metodoAConControlesBase:current.filter(x=>x.controlesBase>0).length,
    metodoAConCincoMetodosEnDescuento:current.filter(x=>x.metodosPrioritariosEnDescuento===5).length,
    metodoASinVinculo:current.filter(x=>x.enlace==='NO_EXPLICITO').map(x=>x.ticker),
    empresas:reported
  };
}
module.exports={inspect,matrix5x5,chapterCount};
if(require.main===module){
  const result=inspect(process.argv[2]?path.resolve(process.argv[2]):undefined);
  console.log(JSON.stringify(result,null,2));
}
