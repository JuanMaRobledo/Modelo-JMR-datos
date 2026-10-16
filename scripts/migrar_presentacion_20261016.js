async function (items) {
  const repo="JuanMaRobledo/Modelo-JMR-datos", br="feature/unificar-38-valoraciones-20261016";
  const esc=s=>String(s??"").replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
  async function retry(fn){let last;for(let i=0;i<3;i++){try{return await fn()}catch(e){last=e;}}throw last;}
  function matrixCheck(rows,base){
    if(typeof base!=="number")return {status:"SIN_DCF_BASE"};
    let seen=0,match=0,bad=[];
    for(let i=0;i+6<rows.length;i++){
      const title=(rows[i]||[]).filter(Boolean).join(" ");
      if(!/×|sensibilidad|sensitivity/i.test(title)||((rows[i]||[]).filter(Boolean).length>2))continue;
      const head=rows[i+1]||[];
      if(head.slice(1,6).filter(v=>String(v||"").trim()).length<4)continue;
      const block=rows.slice(i+2,i+7);
      if(block.length!==5||!block.every(r=>r&&r.slice(1,6).every(v=>v!==""&&v!==undefined)))continue;
      const parsed=String(block[2]?.[3]??"").replace(/[$%\s]/g,"").replace(",",".");
      let center=Number(parsed);if(!Number.isFinite(center))continue;
      seen++;if(Math.abs(center-base)<=Math.max(.03,Math.abs(base)*.0005))match++;
      else bad.push({title,center,base});
      i+=6;
    }
    return {status:!seen?"SIN_MATRICES_5X5":bad.length?"CENTROS_DESACTUALIZADOS":"CONCILIADO",detected:seen,matched:match,discrepancies:bad};
  }
  function formatTable(name,rows){
    let n=Math.min(rows.length,145);while(n&&!rows[n-1]?.some(v=>String(v||"").trim()))n--;
    let w=Math.min(16,Math.max(0,...rows.slice(0,n).map(r=>r?.length||0)));
    return '<table class="jmr-sheet" data-sheet="'+esc(name)+'"><tbody>'+rows.slice(0,n).map((r,i)=>
      !r?.some(v=>String(v||"").trim())?"":'<tr data-row="'+(i+1)+'">'+Array.from({length:w},(_,j)=>'<td>'+esc(r[j]||"")+'</td>').join("")+"</tr>").join("")+"</tbody></table>";
  }
  const results=[];
  for(const entry of items){
    const [ticker,file,id]=entry;
    try{
      const f=await retry(()=>tools.mcp__GitHub__fetch_file({repository_full_name:repo,path:"valoraciones/"+file,ref:br}));
      const m=await retry(()=>tools.mcp__Google_Drive__get_spreadsheet_metadata({spreadsheet_id:id}));
      const d=JSON.parse(f.result.content),already=new Set(Object.values(d.hojas||{}).flatMap(o=>Object.keys(o||{})));
      const tabs=new Set(m.result.sheets.map(o=>o.properties.title));
      const required=["Input sheet","Cost of capital worksheet","Option value","Crecimiento implícito",
        "Anexo Work 15-oct-2026","Sensibilidad DCF","Sensibilidad","Análisis y sensibilidad",
        "Sensibilidad ventaja NFLX","Escenarios e historias","Valuation output","Resumen de Valoración",
        "Márgenes","Eficiencia de capital","Salud Financiera",
        "Income Statement","Balance Sheet","Cash Flow Statement",
        "DCF FCFE financiero","SOTP holding auditado","DCF por negocio"];
      const needed=required.filter(n=>tabs.has(n)&&!already.has(n));
      let sources=[];
      if(needed.length){
        const g=await retry(()=>tools.mcp__Google_Drive__get_spreadsheet_cells({spreadsheet_id:id,
          ranges:needed.map(n=>"'"+n.replaceAll("'","''")+"'!A1:P"+
            (n==="Input sheet"?115:n==="Cost of capital worksheet"?90:/sensib|anexo work/i.test(n)?70:n==="Escenarios e historias"?110:n==="Valuation output"?198:80)),
          cell_fields:"formattedValue"}));
        sources=g.result.sheets||[];
      }
      d.hojas ||= {};const added=[],matrixReviews={};
      const base=d.valorEsperado?.dcfBase ?? d.descuentoMultiples?.dcfHoy?.base ?? null;
      for(const sh of sources){
        const tab=sh.properties.title,rows=[];
        for(const area of sh.data||[])for(let i=0;i<(area.rowData||[]).length;i++){
          const ri=(area.startRow||0)+i;rows[ri] ||= [];
          const values=area.rowData[i].values||[];
          for(let j=0;j<values.length;j++)rows[ri][(area.startColumn||0)+j]=values[j]?.formattedValue||"";
        }
        if(rows.flat().filter(x=>String(x||"").trim()).length<4)continue;
        if(/sensib|anexo work/i.test(tab))matrixReviews[tab]=matrixCheck(rows,base);
        const html=formatTable(tab,rows);
        const group=["Income Statement","Balance Sheet","Cash Flow Statement"].includes(tab)?"financieros":
          ["Márgenes","Eficiencia de capital","Salud Financiera"].includes(tab)?"analisis":"valoracion";
        d.hojas[group] ||= {};
        d.hojas[group][tab]=html;
        added.push(tab);
      }
      const missing=required.filter(n=>!Object.values(d.hojas).some(o=>o&&Object.hasOwn(o,n))&&tabs.has(n));
      d.reportSchema="jmr-report-contract-v1-20261016";
      d.reportIntegrity={date:"2026-10-16",sourceSheet:id,presentationOnly:true,
        originalEconomicsPreserved:true,addedTables:added,originalTablesRetained:true,
        requiredAvailableButNotExported:missing,matrixReviews,
        note:"Sensibilidad en HTML es lectura de hoja fuente, no recalculada. Verificar vigencia DCF antes de interpretar."};
      const payload=JSON.stringify(d,null,2)+"\n";
      if(payload.length>900000){results.push({ticker,status:"EXCEDE_900KB",length:payload.length,wouldAdd:added});continue;}
      if(!added.length && already.size>0 && f.result.content.includes('"reportSchema"')) {
        results.push({ticker,status:"YA_COMPLETO",savedTabs:already.size});continue;
      }
      const u=await retry(()=>tools.mcp__GitHub__update_file({repository_full_name:repo,path:"valoraciones/"+file,ref:undefined,
        branch:br,sha:f.result.sha,content:payload,message:"refactor("+ticker+"): migrar tablas a reporte uniforme desde hoja original"}));
      results.push({ticker,status:"ACTUALIZADO",added,bytes:payload.length,
        matrixReviews,sha:u.result?.commit_sha,available:d.hojas&&Object.values(d.hojas).reduce((a,o)=>a+Object.keys(o).length,0)});
    }catch(e){results.push({ticker,status:"ERROR",error:String(e).slice(0,300)});}
  }
  return results;
}