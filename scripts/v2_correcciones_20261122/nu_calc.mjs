import fs from 'node:fs';
import * as fin from '/home/user/Modelo-JMR-V2/docs/v2/motores/financieras.mjs';
const e=JSON.parse(fs.readFileSync(process.argv[2])); const f=e.financials, A=e.assumptions;
const run=a=>fin.evaluarExcesoRetorno({bookEquity:f.bookEquity,shares:f.shares,...a});
const out={esc:{}};
for(const n of ['conservador','base','optimista']){const r=run(A[n]);
 const pvTV=r.terminalValue/r.years.at(-1).cumulative, pvExc=r.pvExcess-pvTV;
 out.esc[n]={v:r.perShare,ke:r.costOfEquity,payoutStable:r.payoutStable,bv0:f.bookEquity/f.shares,pvExc:pvExc/f.shares,pvTV:pvTV/f.shares,
  years:r.years.map(y=>({t:y.year,bv:y.beginningBook,roe:y.roe,ni:y.netIncome,exc:y.excess,payout:y.payout}))};}
const B=A.base, vb=out.esc.base.v;
const d=o=>run({...B,...o}).perShare;
out.sensKeG={erps:[],gs:[0.03,0.035,0.04,0.045,0.05],rows:[]};
for(const dk of [-0.01,-0.005,0,0.005,0.01]){const erp=B.erp+dk/B.beta; out.sensKeG.rows.push({ke:B.riskFree+B.beta*erp,cells:out.sensKeG.gs.map(g=>d({erp,stableGrowth:g}))});}
out.sensRoe={hg:[0.20,0.23,0.26,0.29,0.32],st:[0.1094,0.14,0.18,0.22,0.26],rows:[]};
for(const h of out.sensRoe.hg) out.sensRoe.rows.push(out.sensRoe.st.map(s=>d({roeHighGrowth:h,roeStable:s})));
out.estres=[['S1 · Normalización fiscal plena y mora alta (ROE alto crecimiento 20 %)',{roeHighGrowth:0.20}],
 ['S2 · Shock de riesgo país Brasil (Ke +200 pb)',{erp:B.erp+0.02/B.beta}],
 ['S3 · Mayor exigencia de capital (CET1 objetivo +200 pb: ROE alto crecimiento 26 % × 12,1/14,1 = 22,3 %)',{roeHighGrowth:0.26*12.1/14.1}],
 ['S4 · Combinado adverso (ROE 20 %, Ke +150 pb, ROE estable 14 %)',{roeHighGrowth:0.20,erp:B.erp+0.015/B.beta,roeStable:0.14}]].map(([l,o])=>[l,d(o)]);
let lo=0.05,hi=0.5;for(let i=0;i<60;i++){const m=(lo+hi)/2;(d({roeHighGrowth:m})>f.sharePrice)?hi=m:lo=m;} out.roeImplicito=lo;
lo=0.05;hi=0.4;for(let i=0;i<60;i++){const m=(lo+hi)/2;(d({roeStable:m})>f.sharePrice)?hi=m:lo=m;} out.roeEstableImplicito=lo;
const bvps=f.bookEquity/f.shares, eps=f.netIncome/f.shares;
out.mult={pbvPrecio:f.sharePrice/bvps,pbvBase:vb/bvps,pePrecio:f.sharePrice/eps,peBase:vb/eps,bvps,eps};
out.sensBeta={b0806:d({beta:0.806}),b0697:d({beta:0.697}),b0823:d({beta:0.823})};
out.ret={r70:d({retentionHighGrowth:0.7}),r90:d({retentionHighGrowth:0.9})};
fs.writeFileSync(process.argv[3],JSON.stringify(out,null,1));
console.log(Object.fromEntries(Object.entries(out.esc).map(([k,v])=>[k,[v.v.toFixed(2),v.bv0.toFixed(2),v.pvExc.toFixed(2),v.pvTV.toFixed(2),v.ke.toFixed(4),v.payoutStable.toFixed(3)]])));
console.log('estres',out.estres.map(x=>x[1].toFixed(2)),'roeImp',out.roeImplicito.toFixed(4),'roeStImp',out.roeEstableImplicito.toFixed(4),out.mult,out.sensBeta,out.ret);
console.log(out.sensKeG.rows.map(r=>[r.ke.toFixed(4),...r.cells.map(c=>c.toFixed(2))]));console.log(out.sensRoe.rows.map(r=>r.map(c=>c.toFixed(2))));
