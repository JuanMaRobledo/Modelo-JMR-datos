import fs from 'node:fs';
import assert from 'node:assert/strict';
const d=JSON.parse(fs.readFileSync(new URL('./CIERRE_REVISION.json',import.meta.url),'utf8'));
const run=function run(spec,growth){const rev=[spec.revenue0],years=[];let nol=spec.nol,pv=0,discount=1;
for(let t=1;t<=11;t++){const g=t<=5?growth[t-1]:t<=10?growth[4]+(spec.gT-growth[4])*(t-5)/5:spec.gT;rev.push(rev.at(-1)*(1+g));}
for(let t=1;t<=10;t++){const margin=t===1?spec.margin1:spec.marginT-(spec.marginT-spec.margin1)*Math.max(spec.convergence-t,0)/spec.convergence;const tax=t<=5?spec.tax0:spec.tax0+(spec.taxT-spec.tax0)*(t-5)/5;const ebit=rev[t]*margin;const nopat=ebit>0?ebit-Math.max(ebit-nol,0)*tax:ebit;nol=Math.max(nol-ebit,0);const sc=t<=5?spec.sc1:spec.sc2;const reinv=Math.max((spec.lag0 ? rev[t]-rev[t-1] : rev[t+1]-rev[t])/sc,0);const wacc=t<=5?spec.wacc:spec.wacc+((spec.discountWaccT??spec.waccT)-spec.wacc)*(t-5)/5;discount/=1+wacc;pv+=(nopat-reinv)*discount;years.push({t,revenue:rev[t],margin,tax,nopat,reinv,fcff:nopat-reinv,wacc,discount});}
const terminalNopat=rev[11]*spec.marginT*(1-spec.taxT);const terminalReinv=terminalNopat*spec.gT/spec.roicT;const pvt=(terminalNopat-terminalReinv)/(spec.waccT-spec.gT)*discount;return {price:(pv+pvt+spec.cash+spec.nonoperating-spec.debt)/spec.shares,mos:(pv+pvt+spec.cash+spec.nonoperating-spec.debt)/spec.shares*.65,pv,pvt,years,rev};};

const near=(a,b,label)=>assert.ok(Math.abs(a-b)<1e-8,label+': '+a+' vs '+b);
near(run(d.base_parameters,d.growth).price,d.native_base,'Conditional native Base');
near(d.native_base*.65,d.native_mos,'Conditional MOS');
for(let i=0;i<5;i++)for(let j=0;j<5;j++){
 const s=d.base_parameters,g=d.growth,dg=(j-2)*.005,dw=(i-2)*.005;
 near(run({...s,waccT:s.waccT+dw,discountWaccT:s.waccT,gT:s.gT+dg},g).price,d.matrices[0][i][j],'Terminal-only WACC matrix');
 near(run({...s,roicT:s.roicT+(i-2)*.005,gT:s.gT+dg},g).price,d.matrices[1][i][j],'ROIC matrix');
 near(run({...s,marginT:s.marginT+(j-2)*.02},g.map(x=>x+(i-2)*.02)).price,d.matrices[2][i][j],'Growth/margin matrix');
}
const facts=Object.fromEntries(d.cash_flow_primary_facts.map(x=>[x[0],x.slice(1)]));
for(let i=0;i<3;i++){
 const sum=keys=>keys.reduce((t,k)=>t+facts[k][i],0);
 near(sum(['NI','DeferredTax','SBC','DA','Accretion','Impairment','DeferredRevenue','Receivables','DeferredCost','Prepaid','Payables','Accrued','Noncurrent']),facts.CFO[i],'Primary CFO components '+i);
 near(sum(['InvestmentPurchases','InvestmentMaturities','Software','PPE','Acquisitions']),facts.CFI[i],'Primary investing components '+i);
 near(sum(['OptionExercise','Earnout','Buybacks','Withholding']),facts.CFF[i],'Primary financing components '+i);
 near(sum(['CFO','CFI','CFF']),facts.CashChange[i],'Primary cash movement '+i);
}
const ltm=k=>facts[k][0]+facts[k][2]-facts[k][1];
near(ltm('CFO'),435.753,'LTM CFO');near(ltm('CFO')+ltm('PPE')+ltm('Software'),395.488,'LTM FCF includes software');
const inc=Object.fromEntries(d.income_primary_facts.map(x=>[x[0],x.slice(1)]));
for(let i=0;i<3;i++){
 near(inc.Revenue[i]-inc.CostRevenue[i]-inc['R&D'][i]-inc.SalesMarketing[i]-inc['G&A'][i],inc.EBIT[i],'Primary EBIT '+i);
 near(inc.EBIT[i]+inc.Interest[i]+inc.OtherNet[i],inc.EBT[i],'Primary EBT '+i);
 near(inc.EBT[i]-inc.Tax[i],inc.NI[i],'Primary NI '+i);
}
const gate=JSON.parse(fs.readFileSync(new URL('./CONTROL_FINAL_NATIVO.json',import.meta.url),'utf8'));
const sheet=gate.sheets.find(s=>s.properties.title==='Input sheet');
assert.equal(sheet.data[0].rowData[3].values[0].effectiveValue.stringValue,'REVISAR');
const vo=gate.sheets.find(s=>s.properties.title==='Valuation output');
assert.ok(!vo.data[0].rowData?.[0]?.values?.[0]?.effectiveValue,'Blocked output must remain blank');
assert.equal(d.publication_ready,false);
console.log(JSON.stringify({conditional_DCF:'PASS',native_matrix_cells:75,primary_CFO_CFI_CFF_cash_components:'PASS',primary_income_identities:'PASS',LTM_FCF:395.488,conditional_base:d.native_base,conditional_mos:d.native_mos,native_promotion_gate:'REVISAR',publication_ready:false},null,2));
