const fs=require('fs'), vm=require('vm'), path=require('path');
process.chdir(__dirname);
const ctx={};vm.createContext(ctx);vm.runInContext(fs.readFileSync('jmr_engine.cjs','utf8'),ctx);
const out={};
for(const snap of JSON.parse(fs.readFileSync('snapshot-inputs.json'))){
 const tk=snap.ticker;if(!tk)continue;
 const c=(s,a)=>{const match=a.match(/([A-Z]+)(\d+)/);let col=0;for(const l of match[1])col=col*26+l.charCodeAt(0)-64;const start=Number((snap.ranges[s]?.range||'A1').match(/\d+/)[0]);return snap.ranges[s]?.values?.[Number(match[2])-start]?.[col-1];};
 const n=(s,a)=>typeof c(s,a)==='number'?c(s,a):null;
 const yes=(s,a)=>/^(yes|sí|si)$/i.test(c(s,a)||'');
 const r=(a)=>n('Valuation output',a), u=(a)=>n('Input sheet',a), history=snap.ranges['Escenarios e historias']?.values?.slice(1)||[];
 const inp={revenue0:r('B5'),ebit0:r('B7'),taxEffective:r('C8'),taxMarginal:r('M8'),shares0:r('B34'),cash:r('B29'),debt:r('B27'),nonOperatingAssets:r('B30')||0,minorityInterests:r('B28')||0,optionsValue:r('B32')||0,preferredStock:u('B76')||0,nol0:r('B12')||0,probFailure:r('B24')||0,recoveryPct:u('B55')||0,failureBookCapital:c('Input sheet','B54')==='B'?(u('B15')||0)+(u('B16')||0):null,wacc:r('C14'),terminalWacc:r('M14'),riskFreeRate:u('B35'),terminalGrowth:r('M4'),roicTerminal:r('M42')||r('M14'),convergenceYear:u('B31'),salesToCapital:r('C40'),salesToCapital2:yes('Input sheet','B120')?u('B33'):r('H40'),smoothTerminalCapital:yes('Input sheet','B120')||yes('Input sheet','B78'),investedCapital0:r('B41'),nopatBase:r('B9'),reinvestLag:yes('Input sheet','B57')?u('B58'):1,sinLiberacion:c('Input sheet','B98')==='Sin liberación',crecimientoAnios:['C','D','E','F','G'].map(col=>r(col+'4'))};
 const baseRecord=history[0]?.[7]; const p=u('B23');
 const result={ticker:tk,sheetId:snap.metadata.spreadsheetId,history,baseSheet:baseRecord,priceSheet:p,input:inp,origin:snap.ranges['Origen de los Supuestos']?.values||[],costCapital:snap.ranges['Cost of capital worksheet']?.values||[],snapshotReadAt:new Date().toISOString()};out[tk]=result;
 if(snap.ranges['SOTP holding auditado']){result.method='SOTP';result.holding=snap.ranges['SOTP holding auditado'].values;continue;}
 if(snap.ranges['DCF FCFE financiero']){
  result.method='FCFE';result.financial=snap.ranges['DCF FCFE financiero'].values;
  const f=result.financial,baseRows=snap.financialBase.values.slice(1,11);
  const bv0=f[11][1],kt=f[3][1],gt=f[4][1],ke=f[5][1],shares=f[6][1],roe=f[4][3];
  const gp=baseRows.map(r=>r[1]);
  const run=(changes={})=>{
   const rterm=changes.terminalRoe??kt,gterm=changes.terminalGrowth??gt,kterm=changes.terminalKe??kt,rtarget=changes.roeTarget??roe,delta=changes.delta??0;
   let bv=bv0,disc=1,pv=0;const rows=[];
   for(let i=0;i<10;i++){
    const growth=gp[i]+(i<5?delta:delta*(9-i)/5)+(gterm-gt)*(i<5?0:(i-4)/5);
    const ry=i<5?rtarget:rtarget+(rterm-rtarget)*(i-4)/5,ki=i<5?ke:ke+(kterm-ke)*(i-4)/5;
    const ni=bv*ry,re=bv*Math.max(0,growth);bv+=re;const flow=ni-re;disc/=1+ki;pv+=flow*disc;rows.push([i+1,growth,ry,ni,re,flow,ki,disc]);
   }
   const terminal=bv*rterm*(1-gterm/rterm)/(kterm-gterm);return {valuePerShare:(pv+terminal*disc)/shares,rows,terminal,bookEquity:bv,equityValue:pv+terminal*disc};
  };
  result.baseEngine=run().valuePerShare;result.detailFinancial=run();result.errorBase=Math.abs(result.baseEngine-baseRecord);
  result.financialInputs={bookEquity0:bv0,keInitial:ke,keTerminal:kt,gTerminal:gt,roeTarget:roe,roeTerminal:kt,shares0:shares,growthPath:gp};
  if(result.errorBase>Math.max(.001,Math.abs(baseRecord)*1e-7)){result.error='FCFE_NO_RECONCILIADO';continue;}
  result.matrices=[];const grid=(name,xs,ys,fn)=>{const cells=ys.map(y=>xs.map(x=>fn(x,y)));result.matrices.push({name,xs,ys,cells,center:cells[2][2],baseError:Math.abs(cells[2][2]-baseRecord)});};
  const gs=[gt-.01,gt-.005,gt,gt+.005,gt+.01];
  grid('Ke terminal × crecimiento perpetuo',gs,[kt-.02,kt-.01,kt,kt+.01,kt+.02],(g,k)=>k>g?run({terminalGrowth:g,terminalKe:k}).valuePerShare:null);
  grid('ROE terminal × crecimiento perpetuo',gs,[kt*.6,kt*.8,kt,kt*1.2,kt*1.4],(g,r)=>run({terminalGrowth:g,terminalRoe:r}).valuePerShare);
  grid('Cambio de crecimiento patrimonial años 1–5 × ROE explícito',[-.04,-.02,0,.02,.04],[roe-.04,roe-.02,roe,roe+.02,roe+.04],(delta,r)=>run({delta,roeTarget:r}).valuePerShare);
  const roots=[],target=p,fun=x=>run({delta:x}).valuePerShare-target;let prior=-.5,fp=fun(prior);
  for(let i=1;i<=350;i++){const x=-.5+i*.01,fx=fun(x);if(Number.isFinite(fx)&&fx*fp<=0){let lo=prior,hi=x,fl=fp;for(let n=0;n<70;n++){const m=(lo+hi)/2,fm=fun(m);if(fl*fm<=0)hi=m;else{lo=m;fl=fm;}}roots.push((lo+hi)/2);}prior=x;fp=fx;}
  const cagr=a=>Math.pow(a.reduce((p,g)=>p*(1+g),1),.2)-1;
  if(roots.length){const delta=roots.sort((a,b)=>Math.abs(a)-Math.abs(b))[0];result.inverse={delta,cagrBase:cagr(gp.slice(0,5)),cagrImplied:cagr(gp.slice(0,5).map(g=>g+delta)),reconstructed:run({delta}).valuePerShare,target,error:Math.abs(fun(delta)),roots:roots.length,fixed:'ROE explícito y terminal, Ke inicial y terminal, g terminal, patrimonio inicial y acciones; años 6–10 convergen desde el año 5 ajustado.'};}
  else result.inverse={error:'SIN_RAIZ_EN_RANGO',target,range:[-.5,3]};
  continue;
 }
 if(['NU','PAGS'].includes(tk)){result.method='FINANCIERA_PENDIENTE';continue;}
 result.method='FCFF';
 const required=['revenue0','ebit0','taxEffective','taxMarginal','shares0','cash','debt','wacc','terminalWacc','terminalGrowth','salesToCapital'];
 if(required.some(k=>!Number.isFinite(inp[k]))){result.error='INPUT_INCOMPLETO';continue;}
 const columns=['C','D','E','F','G','H','I','J','K','L'];
 const actualGrowth=columns.map(col=>r(col+'4')), actualMargins=columns.map(col=>r(col+'6'));
 const actualIntensity=columns.map(col=>1/r(col+'40'));
 const g=inp.crecimientoAnios[1], margin=r('L6'), marginY1=r('C6');
 result.marginTarget=margin;result.marginInitial=r('B6');result.marginYear1=marginY1;
 // Preserve bespoke year-by-year paths. Perturb their endpoints without replacing them
 // with a different generic DCF; all transformations below are disclosed in the report.
 let engineSource=fs.readFileSync('jmr_engine.cjs','utf8');
 engineSource=engineSource.replace('var capitalIntensity = function(n){','var capitalIntensity = function(n){ if(inp.capitalIntensityPath) return inp.capitalIntensityPath[n-1];');
 const local={};vm.createContext(local);vm.runInContext(engineSource,local);
 const run=(changes={})=>{
  const delta=(changes.crecimientoAnios?.[0]??actualGrowth[0])-actualGrowth[0],dg=(changes.terminalGrowth??inp.terminalGrowth)-inp.terminalGrowth;
  const pathGrowth=actualGrowth.map((g,i)=>g+(i<5?delta:delta*(9-i)/5)+dg*(i<5?0:(i-4)/5));
  const dm=(changes.marginTarget??margin)-margin;
  const pathMargins=actualMargins.map((m,i)=>m+dm*Math.min(1,i/Math.max(1,inp.convergenceYear-1)));
  local.marginPath=()=>[null,...pathMargins];
  const roic=changes.roicTerminal??inp.roicTerminal;
  const intensity=actualIntensity.map((ci,i)=>{
   if(i<5||!inp.smoothTerminalCapital)return ci;
   const tax=inp.taxEffective+(inp.taxMarginal-inp.taxEffective)*(i-4)/5;
   return ci+(i-4)/5*(1-tax)*(pathMargins[i]/roic-actualMargins[i]/inp.roicTerminal);
  });
  if(tk==='MU'){
   const spec=snap.muReinvestment.values;
   const rd=[3116,3114,3430,3798,5650], rev=[inp.revenue0];for(const gg of pathGrowth)rev.push(rev.at(-1)*(1+gg));rev.push(rev.at(-1)*(1+(changes.terminalGrowth??inp.terminalGrowth)));
   let prevWC=spec[8][1];const custom=[];
   for(let i=0;i<10;i++){
    const revenue=rev[i+1],da=i<5?spec[4][i+2]:revenue*.09,capex=i<5?spec[5][i+2]:revenue*.15;
    const rdi=revenue*(i<5?.028+.002*i:i===5?.038:.04),amort=rd.slice(-5).reduce((a,b)=>a+b,0)/5;rd.push(rdi);
    const wc=revenue*.23;const re=Math.max(0,wc-prevWC)+Math.max(0,capex-da)+Math.max(0,rdi-amort);prevWC=wc;
    const alpha=i<5?0:(i-4)/5,tt=i<9?inp.taxEffective+(inp.taxMarginal-inp.taxEffective)*Math.max(0,(i-3)/5):inp.taxMarginal;
    // Fade uses next year's economic NOPAT and its tax rate (MU Sheet H14:L14).
    const nextIndex=i+1,nextTax=nextIndex<5?inp.taxEffective:inp.taxEffective+(inp.taxMarginal-inp.taxEffective)*Math.min(1,(nextIndex-4)/5);
    const nextMargin=nextIndex<10?pathMargins[nextIndex]:pathMargins[9];
    custom.push((1-alpha)*re+alpha*rev[i+2]*nextMargin*(1-nextTax)*(changes.terminalGrowth??inp.terminalGrowth)/roic);
   }
   local.runDCFDetalle=vm.runInContext('runDCFDetalle',local);
   const muSource=engineSource.replace('var lag0 = inp.reinvestLag === 0;', 'var lag0 = inp.reinvestLag === 0;').replace('// Plantilla del 12-oct-2026', 'if(inp.customReinvestment) reinvest=[null,...inp.customReinvestment];\n  // Plantilla del 12-oct-2026');
   vm.runInContext(muSource,local);local.marginPath=()=>[null,...pathMargins];
   return local.runDCFDetalle({...inp,...changes,customReinvestment:custom,capitalIntensityPath:intensity,crecimientoAnios:pathGrowth},g,changes.marginTarget??margin,pathGrowth[0],marginY1);
  }
  return local.runDCFDetalle({...inp,...changes,capitalIntensityPath:intensity,crecimientoAnios:pathGrowth},g,changes.marginTarget??margin,pathGrowth[0],marginY1);
 };
 const base=run();result.baseEngine=base.valuePerShare;result.errorBase=Math.abs(base.valuePerShare-baseRecord);result.detail=base;
 if(result.errorBase>Math.max(.001,Math.abs(baseRecord)*1e-7)){result.error='BASE_NO_RECONCILIADA';continue;}
 result.matrices=[];
 const grid=(name,xs,ys,fn)=>{const cells=ys.map(y=>xs.map(x=>fn(x,y)));result.matrices.push({name,xs,ys,cells,center:cells[2][2],baseError:Math.abs(cells[2][2]-baseRecord)});};
 const w=inp.terminalWacc,gt=inp.terminalGrowth,rt=inp.roicTerminal;
 const gs=[gt-.01,gt-.005,gt,gt+.005,gt+.01];
 grid('WACC terminal × crecimiento perpetuo',gs,[w-.02,w-.01,w,w+.01,w+.02],(growth,wacc)=>wacc>growth?run({terminalGrowth:growth,terminalWacc:wacc}).valuePerShare:null);
 grid('ROIC marginal terminal × crecimiento perpetuo',gs,[rt*.6,rt*.8,rt,rt*1.2,rt*1.4],(growth,roic)=>run({terminalGrowth:growth,roicTerminal:roic}).valuePerShare);
 grid('Cambio de crecimiento años 1–5 × margen EBIT objetivo',[-.04,-.02,0,.02,.04],[margin-.04,margin-.02,margin,margin+.02,margin+.04],(delta,m)=>run({crecimientoAnios:inp.crecimientoAnios.map(a=>a+delta),marginTarget:m,growthY1:inp.crecimientoAnios[0]+delta}).valuePerShare);
 // Root of a common additive shock to the actual five growth rates; no calibration.
 const objective=delta=>run({crecimientoAnios:inp.crecimientoAnios.map(a=>a+delta),growthY1:inp.crecimientoAnios[0]+delta}).valuePerShare-p;
 const roots=[];let prior=-.5,fp=objective(prior);
 for(let i=1;i<=350;i++){const next=-.5+i*.01,fn=objective(next);if(Number.isFinite(fp)&&Number.isFinite(fn)&&fp*fn<=0){let lo=prior,hi=next,fl=fp;for(let k=0;k<70;k++){const mid=(lo+hi)/2,fm=objective(mid);if(fl*fm<=0)hi=mid;else{lo=mid;fl=fm;}}roots.push((lo+hi)/2);}prior=next;fp=fn;}
 if(roots.length){const delta=roots.sort((a,b)=>Math.abs(a)-Math.abs(b))[0],cur=inp.crecimientoAnios;const cagr=a=>Math.pow(a.reduce((p,g)=>p*(1+g),1),.2)-1;result.inverse={delta,cagrBase:cagr(cur),cagrImplied:cagr(cur.map(g=>g+delta)),reconstructed:p+objective(delta),target:p,error:Math.abs(objective(delta)),roots:roots.length,fixed:'Margen EBIT, impuestos, WACC inicial y terminal, ROIC, Sales to Capital, g terminal, deuda, caja y acciones. Años 6–10 convergen desde el año 5 ajustado al g terminal fijo.'};}
 else result.inverse={error:'SIN_RAIZ_EN_RANGO',range:[-.5,3]};
}
fs.writeFileSync('numerical.json',JSON.stringify(out,null,2));
console.log(JSON.stringify(Object.values(out).map(r=>({ticker:r.ticker,method:r.method,sheet:r.baseSheet,engine:r.baseEngine,error:r.error,diff:r.errorBase,matrices:r.matrices?.length,inverseError:r.inverse?.error})),null,2));
