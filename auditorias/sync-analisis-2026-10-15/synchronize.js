
function synchronize(records, valuations, now) {
 const esc=x=>String(x??"N/D").replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
 const num=x=>typeof x==="number"&&Number.isFinite(x);
 const fmt=x=>num(x)?x.toLocaleString("es-CO",{minimumFractionDigits:2,maximumFractionDigits:2}):"N/D";
 const pct=x=>num(x)?fmt(x*100)+"%":"N/D";
 const table=(heads,rows)=>"<table><thead><tr>"+heads.map(x=>"<th>"+esc(x)+"</th>").join("")+"</tr></thead><tbody>"+rows.map(r=>"<tr>"+r.map(x=>"<td>"+esc(x)+"</td>").join("")+"</tr>").join("")+"</tbody></table>";
 const strip=h=>(h||"").replace(/<section\b[^>]*(?:data-jmr-valuation-sync|data-jmr-market-level1-20261015|data-jmr-market-research-20261015|data-jmr-unified-comparison)[^>]*>[\s\S]*?<\/section>/g,"");
 const insert=(h,b)=>{h=strip(h);return /<\/h1>/i.test(h)?h.replace(/<\/h1>/i,"</h1>"+b):b+h};
 const out=[], report=[];
 for(const item of records) {
  const d=JSON.parse(item.content), old=JSON.stringify(d), lv=d.linkedValuation||{}, source=lv.sourcePath, v=valuations[source];
  if(!v){report.push({ticker:d.ticker,status:"PENDIENTE",reason:"Sin valoración vinculada verificable",path:item.path});continue;}
  if(v.ticker!==d.ticker)throw Error("Ticker mismatch "+d.ticker);
  const ve=v.valorEsperado||{}, dm=v.descuentoMultiples||{}, holding=v.valoracionHolding;
  const base=holding?.nav?.base??ve.valorCentral??ve.dcfBase??dm.dcfHoy?.base;
  const currency=v.currency||d.currency||(/GRUPO|SURA|DAVV/.test(d.ticker)?"COP":"USD");
  const money=x=>currency+" "+fmt(x);
  const stories=ve.historias||[], central=stories.find(x=>x.central)||stories.find(x=>x.id===ve.historiaCentralId)||stories[0];
  const price=v.precioAnalisis??v.precio, mos=v.mos, basis=v.baseMOS;
  const basisValue=basis==="dcfBase"?base:basis==="valorEsperado"?ve.valor:basis==="navReferencial"?holding?.nav?.base:null;
  const threshold=num(basisValue)&&num(mos)?basisValue*(1-mos):null;
  const savedThreshold=v.precioMOSHoy?.base??v.precioMOS??holding?.umbralMOS;
  const pending=[...(d.workReview?.pending||[])];
  if(num(threshold)&&num(savedThreshold)&&Math.abs(threshold-savedThreshold)>Math.max(.02,Math.abs(threshold)*1e-6))pending.push("El umbral MOS guardado difiere del cálculo según baseMOS; requiere conciliar el registro.");
  const inverse=v.crecimientoImplicito, inv=inverse?.dcfInverso;
  const inverseConsistent=!(num(inverse?.dcfHoy)&&num(base)&&Math.abs(inverse.dcfHoy-base)>Math.max(.02,Math.abs(base)*.001));
  if(inverse&&!inverseConsistent)pending.push("El DCF inverso guardado se calculó con una valoración anterior; no se interpreta como vigente.");
  const cm=v.cotizacionMultiples, im=v.multiplosImplicitosDCF, methods=im?.metodos||[];
  const label=holding?"NAV SOTP referencial":/FCFE|financier|banco/i.test(v.tipo||"")?"DCF de la metodología financiera del registro":"DCF Base";
  let body="<section data-jmr-valuation-sync=\"2026-10-15\" id=\"valoracion-vigente-"+esc(d.ticker.toLowerCase())+"\"><h2>Valoración vigente y lectura de inversión</h2>";
  body+="<p>Actualización del análisis: 15 de octubre de 2026. Fuente: registro vinculado guardado "+esc(v.savedAt||v.fecha||"sin fecha de guardado")+". "+esc(label)+": <strong>"+money(base)+" por acción</strong>. ";
  if(num(price)&&num(base)&&price>0)body+="Frente al precio fijo del análisis ("+money(price)+"), la diferencia valor/precio es "+pct(base/price-1)+". ";
  if(num(ve.valor))body+="El promedio por probabilidades es "+money(ve.valor)+"; complementa la historia central. ";
  body+="</p>";
  if(num(threshold))body+="<p>El registro aplica un MOS de "+pct(mos)+" sobre "+esc(basis==="dcfBase"?"el DCF Base":basis==="valorEsperado"?"el valor esperado":basis==="navReferencial"?"el NAV SOTP referencial":basis)+": umbral "+money(threshold)+". El valor intrínseco y el umbral de compra se presentan por separado.</p>";
  if(central) {
   let c=[];
   if(num(central.crecimiento))c.push("crecimiento "+pct(central.crecimiento)+(central.crecimientoAnios?.length?" compuesto en años 1–5":" según la historia guardada"));
   if(num(central.margen))c.push("margen operativo objetivo "+pct(central.margen));
   if(central.salesToCapital!=null)c.push("ventas/capital inicial "+esc(num(central.salesToCapital)?fmt(central.salesToCapital):central.salesToCapital));
   if(central.salesToCapital2!=null)c.push("ventas/capital posterior "+esc(num(central.salesToCapital2)?fmt(central.salesToCapital2):central.salesToCapital2));
   if(num(central.terminalGrowth))c.push("crecimiento terminal "+pct(central.terminalGrowth));
   if(central.roicTerminal!=null)c.push("ROIC terminal "+(num(central.roicTerminal)?pct(central.roicTerminal):esc(central.roicTerminal)));
   if(c.length)body+="<p>Supuestos de la historia Base: "+c.join("; ")+". Son hipótesis del modelo. La justificación empresarial y sus riesgos se desarrollan en el artículo.</p>";
  }
  if(num(dm.costoPatrimonio))body+="<p>El costo del patrimonio usado para descontar los múltiplos es "+pct(dm.costoPatrimonio)+". Este dato corresponde a Ke; el WACC del FCFF se consulta en el desglose del modelo.</p>";
  if(inv&&num(inv.gImplicito)&&inverseConsistent) body+="<p>DCF inverso del registro ("+esc(inverse.fecha||"fecha no consignada")+"): el precio de referencia "+money(inverse.precio)+" requiere "+pct(inv.gImplicito)+" de crecimiento frente a "+pct(inv.gDcf)+" del caso modelado"+(num(inv.dif)?" (diferencia "+fmt(inv.dif*100)+" puntos porcentuales)":"")+". "+esc(inv.lectura||"Se mantienen las demás hipótesis del cálculo guardado.")+"</p>";
  else body+="<p>El registro no aporta un DCF inverso vigente con solución numérica verificable para esta valoración. Se conserva como pendiente; no se sustituye por una estimación inventada.</p>";
  if(cm&&num(cm.precioMercado)){
   body+="<p>Referencia de mercado para los múltiplos: "+money(cm.precioMercado)+"; corte "+esc(cm.fechaCorte||"no documentado")+". "+esc(cm.fuente||"Fuente no consignada")+". "+(cm.esPrecioActualVerificado===false?"Es una referencia guardada; no se presenta como precio actual verificado. ":"")+"La comparación utiliza métricas FY+3 de cada escenario. Los múltiplos de mercado equivalentes a FY+3 no son múltiplos LTM. ";
   if(num(base)&&base>0)body+="Frente al DCF Base, la referencia de mercado está "+pct(cm.precioMercado/base-1)+" por encima o por debajo, según el signo. ";
   body+="</p>";
  }
  if(methods.length)body+="<p>Los múltiplos implícitos son el resultado de expresar el DCF de cada escenario en relación con sus propias métricas proyectadas. Ayudan a juzgar la exigencia de la valoración; no justifican por sí solos los supuestos ni recalibran el DCF. Las anclas seleccionadas conservan la justificación histórica, de comparables o de fundamentales documentada en el expediente.</p>";
  const uniquePending=[...new Set(pending)];
  if(uniquePending.length)body+="<p><strong>Estado pendiente de auditoría:</strong> "+uniquePending.map(esc).join(" · ")+".</p>";
  body+="<p><a href=\"#calculo-vigente-"+esc(d.ticker.toLowerCase())+"\">Ver escenarios, operaciones y múltiplos vigentes</a>. <a href=\""+esc(v.hojaGoogle||"#")+"\">Consultar la hoja vinculada</a>.</p></section>";
  let calc="<section data-jmr-valuation-sync=\"2026-10-15\" id=\"calculo-vigente-"+esc(d.ticker.toLowerCase())+"\"><h2>Cálculos de la valoración vigente</h2>";
  calc+=table(["Operación","Resultado"],[[label,money(base)],["Precio fijo del análisis",money(price)],["Valor/precio − 1",num(base)&&num(price)&&price>0?pct(base/price-1):"N/D"],["Base del MOS",basis||"No consignada"],["MOS",pct(mos)],["Base MOS × (1 − MOS)",money(threshold)],["Umbral guardado",money(savedThreshold)]]);
  if(stories.length)calc+=table(["Escenario","Probabilidad","Valor por acción","Crecimiento","Margen","Ventas/capital","g terminal","ROIC terminal"],stories.map(x=>[x.nombre||x.id,pct(x.probabilidad),money(x.valor),pct(x.crecimiento),pct(x.margen),num(x.salesToCapital)?fmt(x.salesToCapital):x.salesToCapital??"N/D",pct(x.terminalGrowth),num(x.roicTerminal)?pct(x.roicTerminal):x.roicTerminal??"N/D"]));
  if(central?.crecimientoAnios?.length)calc+=table(["Año","Crecimiento Base"],central.crecimientoAnios.map((x,i)=>[i+1,pct(x)]));
  if(holding?.nav)calc+=table(["Escenario SOTP","NAV por acción"],Object.entries(holding.nav).map(([k,x])=>[k,money(x)]));
  if(methods.length){
   const lookup=Object.fromEntries((cm?.metodos||[]).map(x=>[x.nombre,x]));
   calc+=table(["Método","DCF Conservador FY+3","Mercado equivalente FY+3","Diferencia","DCF Base FY+3","Mercado equivalente FY+3","Diferencia","DCF Optimista FY+3","Mercado equivalente FY+3","Diferencia"],methods.map(m=>{let row=[m.nombre];for(const sc of ["conservador","base","optimista"]){const val=m[sc], mk=lookup[m.nombre]?.mercado_FY3_equivalente?.[sc]; row.push(fmt(val),fmt(mk),num(val)&&num(mk)&&val!==0?pct(mk/val-1):"N/D");}return row;}));
   calc+="<p>Múltiplos expresados en veces. Diferencia = mercado equivalente FY+3 / múltiplo DCF FY+3 − 1. Precio y corte de mercado: "+money(cm?.precioMercado)+"; "+esc(cm?.fechaCorte||"N/D")+".</p>";
  }
  if(inv&&num(inv.gImplicito)&&inverseConsistent)calc+=table(["DCF inverso","Valor"],[["Precio utilizado",money(inverse.precio)],["Crecimiento implícito",pct(inv.gImplicito)],["Crecimiento del modelo",pct(inv.gDcf)],["Diferencia en puntos porcentuales",num(inv.dif)?fmt(inv.dif*100):"N/D"]]);
  calc+="</section>";
  const fields=["precio","precioAnalisis","fecha","fechaValoracion","zonas","objetivoPonderado","valorPresentePonderado","descuentoMultiples","cagr","metodos","precioMOS","precioMOSMax","precioMOSHoy","valorEsperado","mos","hojaGoogle","precioMOSValorEsperado","baseMOS","escenariosDCF","crecimientoImplicito","multiplosImplicitosDCF","cotizacionMultiples","valoracionHolding","currency","precioReferenciaConsultadoAt","precioReferenciaFuente"];
  for(const k of fields){if(Object.prototype.hasOwnProperty.call(v,k))lv[k]=JSON.parse(JSON.stringify(v[k]));else delete lv[k];}
  // Stored sheet snapshots and audits are also copied when a link already exposes them.
  for(const k of ["hojas","auditoria"])if(k in lv && k in v)lv[k]=JSON.parse(JSON.stringify(v[k]));
  lv.sourcePath=source;d.linkedValuation=lv;
  for(const k of ["valorEsperado","escenariosDCF","crecimientoImplicito","valoracionHolding"]) {if(k in v)d[k]=JSON.parse(JSON.stringify(v[k]));else if(k in d)delete d[k];}
  d.html=insert(d.html,body);d.articleHtml=insert(d.articleHtml||d.html,body);
  d.calculationHtml=calc+strip(d.calculationHtml);
  d.valuationHtml=calc+strip(d.valuationHtml||"");
  if(d.workReview) {
   d.workReview.savedBase=base;
   if(num(d.workReview.sheetBase)&&num(base)&&Math.abs(d.workReview.sheetBase-base)>Math.max(.02,Math.abs(base)*.001))d.workReview.recordMatchesSheet=false;
   d.workReview.valuationSyncAt=now;
  }
  d.updatedAt=now;
  d.valuationSync={version:"jmr-analysis-valuation-sync-v1",updatedAt:now,sourcePath:source,sourceSavedAt:v.savedAt||null,base,baseMOS:basis,threshold,valuationInputsChanged:false,scope:"Sincronización del registro publicado; no certifica una nueva lectura de Sheets",pending:uniquePending};
  out.push({path:item.path,content:JSON.stringify(d,null,2)+"\n"});
  report.push({ticker:d.ticker,status:uniquePending.length?"ACTUALIZADO_CON_PENDIENTES":"ACTUALIZADO",sourcePath:source,base,pending:uniquePending,path:item.path});
 }
 return {files:out,report};
}

if(typeof module!=='undefined') module.exports={synchronize};
