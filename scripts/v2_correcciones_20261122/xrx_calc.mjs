import fs from 'node:fs'; import {cargarMotor} from '/home/user/Modelo-JMR-V2/scripts/v2-motor.mjs';
const eng=cargarMotor(); const m=JSON.parse(fs.readFileSync(process.argv[2]));
m.financials.debt=4228+497.8;
const fp={conservador:[0.5038,0.25],base:[0.5038,0.5],optimista:[0.2374,0.5]};
for(const [s,[p,r]] of Object.entries(fp)){m.assumptions[s].failureProbability=p;m.assumptions[s].recoveryRate=r;}
const B=m.assumptions.base; const v=o=>eng.calculateAll({...m,assumptions:{conservador:{...B,...o},base:{...B,...o},optimista:{...B,...o}}}).scenarios.base.perShare;
const out={base:v({})};
out.mWT={wt:[0.0654,0.0754,0.0854,0.0954,0.1054],g:[0,0.005,0.01,0.015,0.02]}; out.mWT.rows=out.mWT.wt.map(w=>out.mWT.g.map(g=>v({waccTerminal:w,gTerminal:g})));
out.mMP={mt:[0.038,0.048,0.058,0.068,0.078],p:[0,0.12,0.2374,0.3706,0.5038]}; out.mMP.rows=out.mMP.mt.map(t=>out.mMP.p.map(p=>v({marginTarget:t,failureProbability:p})));
const solve=(f,lo,hi,target)=>{for(let i=0;i<80;i++){const mid=(lo+hi)/2;(f(mid)>target)?hi=mid:lo=mid;}return (lo+hi)/2;};
out.mtPrecio=solve(x=>v({marginTarget:x}),0.03,0.2,0.85); out.mtCero=solve(x=>v({marginTarget:x}),0.03,0.2,0);
out.pPrecio=1-solve(x=>v({failureProbability:1-x}),0,1,0.85); // prob that gives price
out.sinFracaso=v({failureProbability:0}); out.sinPension=eng.calculateAll({...m,financials:{...m.financials,debt:4228},assumptions:{conservador:B,base:B,optimista:B}}).scenarios.base.perShare;
out.m100=v({marginTarget:B.marginTarget+0.01})-out.base;
out.estres=[['Recorte de 15 % en la realización de la cartera XFS',null,{nonoperatingAssets:1209*0.85}],['Probabilidad de fracaso con recuperación de 25 %',{recoveryRate:0.25}],['Declive operativo acelerado (−5,0 % / −4,5 %, margen 4,0 %)',{growth1:-0.05,growth2to5:-0.045,margin1:0.04,marginTarget:0.04}],['Muro 2028–2029 (WACC +200 pb)',{waccInitial:B.waccInitial+0.02,waccTerminal:B.waccTerminal+0.02}]].map(([l,o,f])=>[l,f?eng.calculateAll({...m,financials:{...m.financials,...f},assumptions:{conservador:B,base:B,optimista:B}}).scenarios.base.perShare:v(o)]);
fs.writeFileSync(process.argv[3],JSON.stringify(out,null,1)); console.log(JSON.stringify({base:out.base,mtPrecio:out.mtPrecio,mtCero:out.mtCero,pPrecio:out.pPrecio,sinFracaso:out.sinFracaso,sinPension:out.sinPension,m100:out.m100,estres:out.estres}));
console.log(out.mWT.rows.map(r=>r.map(x=>x.toFixed(2)).join(' '))); console.log(out.mMP.rows.map(r=>r.map(x=>x.toFixed(2)).join(' ')));
