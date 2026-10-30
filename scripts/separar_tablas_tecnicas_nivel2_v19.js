"use strict";
/* Reparto documental sin cambios financieros; sólo tablas cuantitativas >=9 filas.
   Mantener interpretación y tablas breves del Nivel 1. El enlace ancla abre Nivel 2.
 */
function strip(s){return String(s).replace(/<[^>]*>/g," ").replace(/&[^;]+;/g," ").trim();}
function split(input){
 const rec=JSON.parse(JSON.stringify(input)),original=rec.articleHtml||rec.html||"";
 if(!original||!rec.jmrNarrative)throw Error("Only v19 migrated articles");
 if(rec.jmrNarrative.tablesInLevel2)return {record:rec,report:{ticker:rec.ticker,moved:0,skipped:true}};
 const ticker=String(rec.ticker||"T").replace(/[^a-zA-Z0-9]/g,""),tables=[];let index=0;
 const article=original.replace(/<table\b[^>]*>[\s\S]*?<\/table>/gi,function(table,offset){
  const rows=(table.match(/<tr\b/gi)||[]).length;
  if(rows<9)return table;
  const cells=[...table.matchAll(/<t[dh]\b[^>]*>([\s\S]*?)<\/t[dh]>/gi)].map(m=>strip(m[1]));
  const numbers=cells.filter(t=>/\d/.test(t)&&t.split(/\s+/).length<22).length;
  if(numbers<7 || numbers/cells.length<.3)return table;
  const id="jmr-tabla-nivel2-"+ticker+"-"+(++index);
  const before=original.slice(Math.max(0,offset-900),offset);
  const nearby=[...before.matchAll(/<h[234]\b[^>]*>([\s\S]*?)<\/h[234]>/gi)].pop();
  const heading=nearby?strip(nearby[1]).slice(0,145):"Detalle financiero";
  tables.push({id,heading,rows,table});
  return '<p class="jmr-table-in-level2">La tabla numérica detallada de <strong>'+heading.replace(/&/g,"&amp;").replace(/</g,"&lt;")+'</strong> se conserva en <a href="#'+id+'">Nivel 2 · ver datos y cálculos</a>. La interpretación económica permanece en este capítulo.</p>';
 });
 if(article===original){rec.jmrNarrative.tablesInLevel2=0;return {record:rec,report:{ticker:rec.ticker,moved:0}};}
 const extra='<section class="jmr-tables-appendix"><h2>Tablas cuantitativas conservadas desde el artículo</h2>'+
  tables.map(t=>'<section id="'+t.id+'"><h3>'+t.heading.replace(/&/g,"&amp;").replace(/</g,"&lt;")+' · '+t.rows+' filas</h3><div class="table-scroll">'+t.table+'</div></section>').join("\n")+'</section>';
 rec.articleHtml=article;
 if(rec.html===original)rec.html=article;
 else if(String(rec.html||"").startsWith(original))rec.html=article+rec.html.slice(original.length);
 rec.calculationHtml=String(rec.calculationHtml||"")+extra;
 rec.jmrNarrative.tablesInLevel2=tables.length;
 rec.jmrNarrative.tableAnchors=tables.map(x=>x.id);
 rec.jmrNarrative.newLength=article.length;
 // Every table must still exist byte-for-byte in one level.
 for(const t of tables)if(!rec.calculationHtml.includes(t.table))throw Error("Table lost "+t.id);
 return {record:rec,report:{ticker:rec.ticker,moved:tables.length,rows:tables.map(x=>x.rows),articleChars:article.length,calcChars:rec.calculationHtml.length}};
}
return split;