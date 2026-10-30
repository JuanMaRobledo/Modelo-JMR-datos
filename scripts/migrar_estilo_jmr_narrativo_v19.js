"use strict";
/* Migración editorial sin recálculo financiero. Ejecutar con Function(source)() => migrate(record).
  Preserva íntegros párrafos/tablas y todos los campos ajenos a presentación.
  No confundir estructura reorganizada con investigación económica completada.
*/
const TITLES=[
"Tesis de inversión y conclusión","La empresa y su modelo económico",
"Industria, competencia y ventaja competitiva","Motores del crecimiento futuro",
"Historia financiera y calidad de resultados","Reinversión, eficiencia del capital y ROIC",
"Dirección, gobierno y asignación de capital","Nuestro proceso de valoración",
"Supuestos económicos y su justificación","Valor intrínseco, escenarios y precio",
"Riesgos, tesis contraria y factores de ruptura","Catalizadores y plan de seguimiento",
"Fuentes, limitaciones y estado del estudio"];
function norm(x){return String(x||"").replace(/<[^>]*>/g," ").replace(/&amp;/gi,"&")
.replace(/&[^;]+;/g," ").normalize("NFD").replace(/[\u0300-\u036f]/g,"").toLowerCase().replace(/[^a-z0-9]+/g," ").trim();}
function heading(s,level){const re=new RegExp("<h"+level+"\\b[^>]*>([\\s\\S]*?)<\\/h"+level+">","i"),m=s.match(re);return m?m[1].replace(/<[^>]*>/g," ").trim():"";}
function breakSections(s){
 const re=/<\/?section\b[^>]*>/gi,stack=[],parts=[];let m;
 while((m=re.exec(s))){
  if(/^<\/section/i.test(m[0])){
   if(!stack.length)throw Error("Closing </section> without opener");
   const t=stack.pop();parts.push({...t,end:re.lastIndex,raw:s.slice(t.start,re.lastIndex)});
  } else stack.push({start:m.index,opener:m[0],parent:stack[stack.length-1]||null,depth:stack.length+1});
 }
 if(stack.length)throw Error("Open section elements at EOF");
 return parts.sort((a,b)=>a.start-b.start);
}
function category(text,fallback){
 const t=norm(text).replace(/^\d+\s+/,"");if(!t)return fallback||13;
 // The reasoned economic story is more important than the old chapter number.
 if(/^(fuentes|bibliografia|documentos y fuentes)|^referencias|^control editorial|control de calidad|documentos y fuentes/.test(t))return 13;
 if(/cierre|dictamen|conclusion|decision|resumen ejecutivo|tesis central|tesis economica|tesis de inversion|evaluacion final|resumen de inversion|valor intrinseco principal/.test(t))return 1;
 if(/bulls|bears|tesis contraria|prueba contraria|riesgos|ruptura|disrupcion de|amenazas|regulatorio/.test(t))return 11;
 if(/catalizadores|vigilar|indicadores|seguimiento|eventos recientes|noticias|que invalidaria|vigilancia|hit[oó]s/.test(t))return 12;
 if(/problema|pendientes|limitaciones|salvedades|control de cobertura|fuente y limite|verificaciones realizadas/.test(t))return 13;
 if(/filosofias|warren buffett|charlie munger|peter lynch|howard marks|greenblatt/.test(t))return 1;
 if(/calidad del negocio|calidad financiera|historia financiera/.test(t))return 5;
 if(/rentabilidad del capital|retorno sobre capital|eficiencia de capital/.test(t))return 6;
 if(/gestion|management|gobierno|incentivo|asignacion de capital|recompras|dilucion|sbc|equipo directivo|administracion/.test(t))return 7;
 if(/(costo|coste) de capital|wacc|cost of capital|costo de equity|ke\b|beta|tasa de descuento|valor terminal|crecimiento terminal|tasas y riesgo de descuento/.test(t))return 9;
 if(/metodo a|metodo b|modelo jmr|normalizacion de estados|procedencia de datos|calibracion|metodologia|nuestro proceso|definicion contable|perimetro|corte contable|criterio de valoracion|aclaracion de metodo|fuente y corte/.test(t))return 8;
 if(/(reinv|sales.to.capital|ventas.capital|roic|retorno del capital|capital invertido|capital fisico|capital de trabajo|capex|capitalizacion de i.d|arrendamientos|leases|leasing|intangibles|costos de contenido|compromisos de contenido|manufactura|inventarios y capital|adquisiciones y capital)/.test(t))return 6;
 if(/supuesto|hipotesis|crecimiento proyectado|trayectoria base|margen objetivo|margen terminal|base y escenario|proyeccion de ingresos|convergencia|sostenibilidad del margen|drivers de valor/.test(t))return 9;
 if(/valoracion|valuacion|valor intrinseco|dcf|fcff|fcfe|sotp|mos|precio|escenarios|historias|perpetuidad|sensibilidad|multiplo|az stocks|descuento de flujos|market value|valor esperado|retorno potencial/.test(t))return 10;
 if(/historia|resultados|ultimo trimestre|ltm|historico|margenes|margenes|flujo|cash.flow|cash flow|margenes gaap|balance|liquidez|deuda|rentabilidad corporativa|calidad de resultados|gaap|guia fy|ingresos reportados|inventarios/.test(t))return 5;
 if(/crecimiento: explicacion|motores de crecimiento|crecimiento base y verificacion/.test(t))return 4;
 if(/cliente|producto|segmento|geografia|mercado pago|business model|modelo de negocio|unidad economica|modelo comercial|modelo economico|monetizacion|cartera de clientes|modelo y propuesta|que hace/.test(t))return 2;
 if(/competencia|competidor|moat|ventaja|rival|industria|dinamica de mercado|cuota de mercado|pricing power|portafolio competitivo/.test(t))return 3;
 if(/crecimiento|expansion|penetracion|guia|demanda|drivers|motor|oportunidades|backlog|contratos|lanzamientos|nuevos productos|expansion regional|trafico|ticket/.test(t))return 4;
 return fallback||13;
}
function canonicalFallback(ch){
 return {1:1,2:2,3:2,4:3,5:5,6:3,7:3,8:7,9:12,10:11,11:11,12:9,13:1,14:12,15:12,16:13,17:13,18:13}[ch]||13;
}
function unwrapV18(s){
 const parts=breakSections(s),wrappers=parts.filter(p=>/id=["']jmr-capitulo-\d+["']/.test(p.opener));
 if(!wrappers.length)return null;
 const units=[];let discarded=0;
 for(const p of wrappers){
  const oldN=Number((p.opener.match(/jmr-capitulo-(\d+)/)||[])[1]);
  const nested=parts.filter(t=>t.parent && t.parent.start===p.start);
  if(!nested.length){discarded++;continue;}
  for(const t of nested){const title=heading(t.raw,3)||heading(t.raw,2),cat=category(title,canonicalFallback(oldN));
   units.push({title,cat,html:t.raw,section:p.opener,oldChapter:oldN});
  }
 }
 const first=wrappers[0],last=wrappers[wrappers.length-1];
 const allBoundaries=wrappers.map(x=>[x.start,x.end]);
 const before=s.slice(0,first.start),after=s.slice(last.end);
 const outside=[];
 // Preserve only text outside canonical wrappers; wrapper headings and generated "pending" placeholders are retired.
 for(let i=0;i<wrappers.length-1;i++) if(wrappers[i].end<wrappers[i+1].start) outside.push(s.slice(wrappers[i].end,wrappers[i+1].start));
 return {before,after,units,exterior:outside.join(""),discarded};
}
function unwrapLegacy(s){
 const parts=breakSections(s),sections=parts.filter(p=>!p.parent && heading(p.raw,2));
 if(!sections.length)return null;
 const units=sections.map(p=>{
  const title=heading(p.raw,2),body=p.raw.replace(/<h2(\b[^>]*)>/i,"<h3$1>").replace(/<\/h2>/i,"</h3>");
  return {title,html:body,cat:category(title)};
 });
 const first=sections[0],last=sections[sections.length-1];
 let exterior="";
 for(let i=0;i<sections.length-1;i++)exterior+=s.slice(sections[i].end,sections[i+1].start);
 return {before:s.slice(0,first.start),after:s.slice(last.end),units,exterior};
}
function unwrapFlat(s){
 const heads=[...s.matchAll(/<h2\b[^>]*>[\s\S]*?<\/h2>/gi)];
 if(heads.length<4)throw Error("Not enough H2 blocks to migrate flat report");
 const names18=["Resumen ejecutivo","Modelo de negocio","Segmentos y geografía","Industria y crecimiento","Calidad del negocio",
 "Ventaja competitiva","Competencia","Gestión y asignación de capital","Catalizadores","Riesgos",
 "Bulls say / Bears say","Valor con criterio Damodaran","Filosofías de inversión",
 "Noticias y eventos recientes","Qué vigilar","Preguntas abiertas","Fuentes","Control de calidad final"];
 const units=[];
 for(let i=0;i<heads.length;i++){
  const chunk=s.slice(heads[i].index,i+1<heads.length?heads[i+1].index:s.length);
  const title=heading(chunk,2),rawTitle=norm(title).replace(/^\d+\s+/,"");
  const oldIndex=names18.findIndex(n=>norm(n)===rawTitle)+1;
  const fallback=oldIndex?canonicalFallback(oldIndex):category(title);
  const subt=[...chunk.matchAll(/<h3\b[^>]*>[\s\S]*?<\/h3>/gi)];
  let leadEnd=subt.length?subt[0].index:chunk.length;
  let lead=chunk.slice(0,leadEnd).replace(/<h2(\b[^>]*)>/i,"<h3$1>").replace(/<\/h2>/i,"</h3>");
  if(lead.trim())units.push({title,html:'<section class="jmr-preserved-flat">'+lead+'</section>',cat:fallback});
  for(let j=0;j<subt.length;j++){
   const part=chunk.slice(subt[j].index,j+1<subt.length?subt[j+1].index:chunk.length);
   const subTitle=heading(part,3);
   units.push({title:subTitle,html:'<section class="jmr-preserved-flat">'+part+'</section>',
     cat:category(subTitle,fallback)});
  }
 }
 return {before:s.slice(0,heads[0].index),after:"",units,exterior:""};
}
function migrate(input){
 const rec=JSON.parse(JSON.stringify(input)),s=rec.articleHtml||rec.html||"";
 if(!s||s.length<900)throw Error("Empty or insufficient report");
 if(rec.jmrNarrative?.version==="JMR-NARRATIVO-V19")return {record:rec,report:{ticker:rec.ticker,status:"YA_MIGRADO"}};
 const parts=unwrapV18(s)||unwrapLegacy(s)||unwrapFlat(s);
 if(parts.units.length<4)throw Error("Too few source sections: "+parts.units.length);
 const bins=TITLES.map(()=>[]),seenNames=[];
 parts.units.forEach(x=>{
  const cat=x.cat;bins[cat-1].push(x);
  seenNames.push({title:x.title,chapter:cat});
 });
 const missing=[];
 let chapters=TITLES.map((title,i)=>{
  if(!bins[i].length)missing.push(i+1);
  const sec='<section class="jmr-v19-chapter" id="jmr-narrative-'+(i+1)+'"><h2>'+(i+1)+'. '+title+'</h2>';
  let html=bins[i].map(x=>x.html).join("\n");
  if(!html)html='<p class="jmr-editorial-gap" data-editorial-gap="true"><strong>Pendiente de investigación:</strong> todavía falta evidencia específica del emisor para desarrollar este capítulo; no se utiliza texto genérico como sustituto.</p>';
  return sec+html+'</section>';
 }).join("\n");
 let next=parts.before+chapters+parts.exterior+parts.after;
 // Integrity: preserve any source paragraph placed directly inside a legacy chapter wrapper,
 // outside its nested subsections (e.g. an SEC source bibliography).
 const originalP=[...s.matchAll(/<p\b[^>]*>[\s\S]*?<\/p>/gi)].map(x=>x[0])
 .filter(x=>!x.includes("data-editorial-gap")&&!x.includes("Pendiente de ampliación editorial"));
 const outsideP=originalP.filter(x=>!next.includes(x));
 if(outsideP.length){
   chapters=chapters.replace(/<\/section>\s*$/, '<div class="jmr-preserved-sources">'+outsideP.join("\\n")+'</div></section>');
   next=parts.before+chapters+parts.exterior+parts.after;
 }
 const lostP=originalP.filter(x=>!next.includes(x));
 if(lostP.length)throw Error("Lost "+lostP.length+" source paragraphs");
 if((next.match(/<h2\b/gi)||[]).length!==13)throw Error("Bad main chapter count");
 if(parts.units.some(x=>!next.includes(x.html)))throw Error("Lost source subsection");
 rec.articleHtml=next;
 if(rec.html===s)rec.html=next;
 else if(String(rec.html||"").startsWith(s))rec.html=next+String(rec.html).slice(s.length);
 if(!rec.calculationHtml){
   rec.calculationHtml='<section><h2>Soporte cuantitativo pendiente de importación</h2><p>Este expediente no incluye un anexo autónomo reproducible dentro del registro. Los estados, supuestos y cálculos deberán consultarse en la hoja oficial asociada cuando esté disponible; la ausencia del anexo no equivale a datos cero ni a una auditoría aprobada.</p></section>';
 }
 rec.jmrNarrative={
  version:"JMR-NARRATIVO-V19",schema:"jmr-fundamental-narrative-13",
  migratedAt:"2026-10-30",sourceRevision:input.revisionId||input.valoracionRevisionId||input.revision_id||"",
  structuralOnly:true,sectionsNeedingResearch:missing,originalSections:parts.units.length,
  originalLength:s.length,newLength:next.length,preservedSourceParagraphs:originalP.length,
  financialInputsChanged:false,needsEditorialReview:true
 };
 return {record:rec,report:{ticker:rec.ticker,status:"MIGRADO_ESTRUCTURAL",missing,
  sourceSections:parts.units.length,preservedParagraphs:originalP.length,
  oldLength:s.length,newLength:next.length,chapterCounts:bins.map(x=>x.length),mapping:seenNames}};
}
return migrate;