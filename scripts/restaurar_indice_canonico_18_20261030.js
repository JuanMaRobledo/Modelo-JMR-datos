// Migración editorial no destructiva: devuelve {record,report}. No cambia valoración.
"use strict";
const canonical=["Resumen ejecutivo","Modelo de negocio","Segmentos y geografía",
"Industria y crecimiento","Calidad del negocio","Ventaja competitiva","Competencia",
"Gestión y asignación de capital","Catalizadores","Riesgos","Bulls say / Bears say",
"Valor con criterio Damodaran","Filosofías de inversión","Noticias y eventos recientes",
"Qué vigilar","Preguntas abiertas","Fuentes","Control de calidad final"];
const normalize=s=>String(s||"").replace(/<[^>]*>/g," ").replace(/&amp;/gi,"&")
.replace(/&[^;]+;/g," ").normalize("NFD").replace(/[\u0300-\u036f]/g,"")
.toLowerCase().replace(/[^a-z0-9]+/g," ").trim();
function sections(html){
 const re=/<\/?section\b[^>]*>/gi,stack=[],outer=[];let m,start=0;
 while((m=re.exec(html))){
  if(/^<\/section/i.test(m[0])){
   if(!stack.length)throw Error("Closing section unmatched");
   stack.pop();
   if(!stack.length)outer.push({start,end:re.lastIndex});
  }else{if(!stack.length)start=m.index;stack.push(m.index);}
 }
 if(stack.length||outer.length<2)throw Error("Unbalanced or absent section blocks: "+outer.length);
 return outer.map((a,i)=>({html:html.slice(a.start,i+1<outer.length?outer[i+1].start:a.end),start:a.start,end:a.end}));
}
function classify(title){
 const t=normalize(title).replace(/^\d+\s+/,"");
 if(/tarjeta/.test(t))return 1;
 if(/fuentes|documentos y fuentes|bibliografia/.test(t))return 17;
 if(/^(control|dictamen|conclusion|decision|verificaciones|estado de publicacion)|^18 conclusion|revision visual|proceso de revision|revision pendiente|conclusion y/.test(t))return 18;
 if(/preguntas|limites del modelo|pendientes|reservas|incertidumbres|lo que no significan|rango y expectativa/.test(t))return 16;
 if(/riesgos|regulacion|morosidad|provisiones|erosion de precio/.test(t))return 10;
 if(/vigilar|vigilancia|seguimiento|indicadores/.test(t))return 15;
 if(/noticias|eventos recientes|acontecimientos recientes/.test(t))return 14;
 if(/filosofias/.test(t))return 13;
 if(/bulls|bears|tesis contraria|prueba contraria/.test(t))return 11;
 if(/catalizadores|lanzamientos|guia oficial|guia fy/.test(t))return 9;
 if(/wacc|costo de capital|coste de capital|costo de equity|descuento|perpetu|roic|reinv|sales.to.capital|capital marginal|multiplo|escenario|sensibilidad|valoracion|dcf|fcff|fcfe|margen de seguridad|az stocks|precio implicito|costo del capital|crecimiento base|crecimiento explicito|trayectoria de ingresos|impuesto/.test(t))return 12;
 if(/gestion|administracion|gobierno|asignacion de capital|recompras|dilucion|sbc|incentivos|clases de acciones/.test(t))return 8;
 if(/competencia|competidores|rivales/.test(t))return 7;
 if(/ventaja|moat|persistencia competitiva/.test(t))return 6;
 if(/geografia|pais|segmentos|cartera comercial|clientes y sectores/.test(t))return 3;
 if(/industria|mercado|tam|cuota|sector|entorno y crecimiento/.test(t))return 4;
 if(/modelo de negocio|modelo comercial|modelo economico|modelo y propuesta|negocio y unidad|negocio y ventajas|negocios y|unidad economica|suscripcion|publicidad|portafolio y|actividad y expansion|modelo y geografia/.test(t))return 2;
 if(/histori|resultado|normaliza|margenes|margen|costos|coste|cash.flow|caja|cfo|flujos|liquidez|balance|financ|credito|deuda|capital trabajo|inventari|capex|r.d|investigacion|i d|gaap|ingresos|ltm|guia|roe|rentabilidad|trimestre|flujo operativo|activos no operativos/.test(t))return 5;
 if(/tesis|resumen|precio|potencial|valor intrinseco|dictamen de inversion/.test(t))return 1;
 if(/crecim|driver|expansion|demanda|trafico|ticket/.test(t))return 4;
 return 16;
}
function firstHeading(html){const m=html.match(/<h2\b[^>]*>([\s\S]*?)<\/h2>/i);return m?m[1].replace(/<[^>]*>/g," ").trim():"";}
function isCanonical(html){
 const found=[...html.matchAll(/<h2\b[^>]*>([\s\S]*?)<\/h2>/gi)].map(m=>normalize(m[1]).replace(/^\d+\s+/,""));
 const indices=canonical.map(x=>found.indexOf(normalize(x)));
 return indices.every((x,i)=>x>=0&&(!i||x>indices[i-1]));
}
function migration(record){
 const j=JSON.parse(JSON.stringify(record));let original=j.articleHtml||j.html||"";
 if(!original)throw Error("Empty article");
 if(isCanonical(original))return {record:j,report:{ticker:j.ticker,status:"YA_CANONICO",missing:[],oldChars:original.length,newChars:original.length}};
 const blocks=sections(original),bins=canonical.map(()=>[]),oldHeadings=[],orphans=[];
 for(const item of blocks){
  const h=firstHeading(item.html);
  if(!h){orphans.push(item.html);continue;}
  const category=classify(h);
  let section=item.html.replace(/<h2(\b[^>]*)>/i,"<h3$1>").replace(/<\/h2>/i,"</h3>");
  bins[category-1].push(section);
  oldHeadings.push({old:h,chapter:category,html:section});
 }
 if(oldHeadings.length<4)throw Error("Cannot safely classify source");
 const missing=[];
 const chapterHtml=canonical.map((name,i)=>{
  let content=bins[i].join("\n");
  if(!content){
   missing.push(i+1);
   content='<p class="jmr-editorial-gap" data-editorial-gap="true"><strong>Pendiente de ampliación editorial:</strong> no hay un desarrollo autónomo con evidencia suficiente sobre '+name.toLowerCase()+'. Se debe completar con investigación específica del emisor sin trasladar cifras de otra revisión ni inventar conclusiones.</p>';
  }
  return '<section id="jmr-capitulo-'+(i+1)+'" class="jmr-capitulo-canonico"><h2>'+(i+1)+'. '+name+'</h2>'+content+'</section>';
 }).join("\n");
 const prefix=original.slice(0,blocks[0].start),suffix=original.slice(blocks[blocks.length-1].end);
 const next=prefix+orphans.join("")+chapterHtml+suffix;
 for(const item of oldHeadings){if(!next.includes(item.html))throw Error("Lost original section "+item.old);}
 if(!isCanonical(next))throw Error("Bad chapter hierarchy");
 j.articleHtml=next;
 if(j.html===original)j.html=next;
 else if(String(j.html||"").startsWith(original))j.html=next+String(j.html).slice(original.length);
 if(!j.calculationHtml){
  j.calculationHtml='<section><h2>Procedencia y respaldo de la valoración</h2><p>El informe original no contiene un anexo técnico autónomo importado. Consultar la hoja oficial enlazada en este expediente, si está disponible. No se reconstruyen fórmulas ni escenarios en esta migración editorial.</p></section>';
 }
 j.editorialMigration={
  version:"JMR-18-CAPITULOS-20261030",reference:"META",
  status:missing.length?"REORGANIZADO_PENDIENTE_AMPLIACION":"REORGANIZADO_PENDIENTE_REVISION",
  missingCanonicalSections:missing,sourceRevision:j.revisionId||j.valuationRevisionId||"",
  originalSections:oldHeadings.length,preservedOriginalText:true,financialAssumptionsChanged:false,
  structuralMigrationOnly:true
 };
 return {record:j,report:{ticker:j.ticker,status:j.editorialMigration.status,missing,
  oldChars:original.length,newChars:next.length,originalSections:oldHeadings.length,
  mapping:oldHeadings.map(x=>x.chapter+":"+x.old)}};
}
return migration;