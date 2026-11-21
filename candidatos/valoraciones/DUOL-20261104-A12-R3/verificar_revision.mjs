import fs from 'node:fs';
import assert from 'node:assert/strict';
const d=JSON.parse(fs.readFileSync(new URL('./REVISION_SUPUESTOS.json',import.meta.url),'utf8'));
const run=function run(spec,growth){const rev=[spec.revenue0],years=[];let nol=spec.nol,pv=0,discount=1;
for(let t=1;t<=11;t++){const g=t<=5?growth[t-1]:t<=10?growth[4]+(spec.gT-growth[4])*(t-5)/5:spec.gT;rev.push(rev.at(-1)*(1+g));}
for(let t=1;t<=10;t++){const margin=t===1?spec.margin1:spec.marginT-(spec.marginT-spec.margin1)*Math.max(spec.convergence-t,0)/spec.convergence;const tax=t<=5?spec.tax0:spec.tax0+(spec.taxT-spec.tax0)*(t-5)/5;const ebit=rev[t]*margin;const nopat=ebit>0?ebit-Math.max(ebit-nol,0)*tax:ebit;nol=Math.max(nol-ebit,0);const sc=t<=5?spec.sc1:spec.sc2;const reinv=Math.max((spec.lag0 ? rev[t]-rev[t-1] : rev[t+1]-rev[t])/sc,0);const wacc=t<=5?spec.wacc:spec.wacc+(spec.waccT-spec.wacc)*(t-5)/5;discount/=1+wacc;pv+=(nopat-reinv)*discount;years.push({t,revenue:rev[t],margin,tax,nopat,reinv,fcff:nopat-reinv,wacc,discount});}
const terminalNopat=rev[11]*spec.marginT*(1-spec.taxT);const terminalReinv=terminalNopat*spec.gT/spec.roicT;const pvt=(terminalNopat-terminalReinv)/(spec.waccT-spec.gT)*discount;return {price:(pv+pvt+spec.cash+spec.nonoperating-spec.debt)/spec.shares,mos:(pv+pvt+spec.cash+spec.nonoperating-spec.debt)/spec.shares*.65,pv,pvt,years,rev};};
const near=(a,b,label)=>assert.ok(Math.abs(a-b)<1e-8,label+': '+a+' vs '+b);
near(run(d.base_parameters,d.original_growth).price,d.previous_base,'R2 reproduction');
near(run(d.base_parameters,d.base_growth).price,d.native_base,'R3 native reconciliation');
near(d.base_result.price*.65,d.base_result.mos,'MOS only on Base');
near(d.inverse.reconstructed,128,'Historical reverse DCF target');
near(run(d.base_parameters,d.base_growth.map(g=>g+d.inverse.delta)).price,128,'Reverse DCF full reconstruction');
assert.equal(d.formula_check.compared,194);assert.deepEqual(d.formula_check.changed,[]);
for(let i=0;i<5;i++)for(let j=0;j<5;j++){
 const dg=(j-2)*.005,dw=(i-2)*.005,s=d.base_parameters,g=d.base_growth;
 near(run({...s,wacc:s.wacc+dw,waccT:s.waccT+dw,gT:s.gT+dg},g).price,d.native_matrices[0].values[i][j],'WACC matrix');
 near(run({...s,roicT:s.roicT+(i-2)*.005,gT:s.gT+dg},g).price,d.native_matrices[1].values[i][j],'ROIC matrix');
 near(run({...s,marginT:s.marginT+(j-2)*.02},g.map(x=>x+(i-2)*.02)).price,d.native_matrices[2].values[i][j],'Growth margin matrix');
}
let sub=1021.214,ad=82.707,det=41.563,iap=36.81,total=d.base_parameters.revenue0;const noMonetization=[];
for(let i=0;i<5;i++){sub*=1+d.driver_forecast[i].mauGrowth;ad*=1+[0,.08,.10,.08,.06][i];det*=1+[0,.02,.03,.03,.03][i];iap*=1+[0,.10,.10,.08,.05][i];const next=sub+ad+det+iap;noMonetization.push(next/total-1);total=next;}
near(run(d.base_parameters,noMonetization).price,d.native_stress_no_monetization,'Native zero monetization stress');
near(Object.values(d.probabilities_after).reduce((a,b)=>a+b,0),1,'Probability total');
assert.deepEqual(d.probabilities_after,{base:.4,conservadora:.225,optimista:.225,disrupcion:.15});
assert.equal(d.multiple_centers.length,5);for(const m of d.multiple_centers)near(m.center,m.vp3,m.name+' matrix center');
assert.equal(d.candados.length,15);assert.ok(d.candados.every(c=>['LISTO','VALIDADO','CONCILIADO','NO APLICA'].includes(c.value)));
assert.equal(d.validation_scope.publication_ready,false);
console.log(JSON.stringify({arithmetic:'PASS',native_DCF_matrix_cells:75,multiple_centers:5,unchanged_base_formulas:194,native_stress:'PASS_AND_RESTORED',base:d.native_base,mos:d.base_result.mos,publication_ready:false,limitations:d.unresolved},null,2));

