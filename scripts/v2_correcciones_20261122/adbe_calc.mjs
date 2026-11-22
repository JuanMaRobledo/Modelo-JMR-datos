import fs from 'node:fs'; import {cargarMotor} from '/home/user/Modelo-JMR-V2/scripts/v2-motor.mjs';
const eng=cargarMotor(); const m=JSON.parse(fs.readFileSync(process.argv[2])); const P=+process.argv[4];
const WI=0.10242696089998787, WT=0.08537;
for(const s of ['conservador','base','optimista']){m.assumptions[s].waccInitial=WI;m.assumptions[s].waccTerminal=WT;}
const B=m.assumptions.base; const v=o=>eng.calculateAll({...m,assumptions:{conservador:{...B,...o},base:{...B,...o},optimista:{...B,...o}}}).scenarios.base.perShare;
const r=eng.calculateAll(m).scenarios; const out={esc:Object.fromEntries(Object.entries(r).map(([k,x])=>[k,x.perShare])), tv:r.base.pvTerminal/r.base.evBeforeRisk, det:Object.fromEntries(Object.entries(r).map(([k,x])=>[k,{sumPV:x.sumPV,pvTerminal:x.pvTerminal,ev:x.evBeforeRisk,equity:x.equity}]))};
out.f08={rows:[WT-0.02,WT-0.01,WT,WT+0.01,WT+0.02],cols:[0.03,0.035,0.04,0.045,0.05]}; out.f08.m=out.f08.rows.map(w=>out.f08.cols.map(g=>v({waccTerminal:w,gTerminal:g})));
out.f09={rows:[0,0.05,0.10,0.15,0.20],cols:[0.28,0.33,0.38,0.43,0.48]}; out.f09.m=out.f09.rows.map(g=>out.f09.cols.map(mt=>v({growth2to5:g,marginTarget:mt})));
out.f10={rows:[0.095,0.13,0.17,0.21,0.26],cols:[0.03,0.035,0.04,0.045,0.05]}; out.f10.m=out.f10.rows.map(x=>out.f10.cols.map(g=>v({roicTerminal:x,gTerminal:g})));
const solve=(f,lo,hi)=>{for(let i=0;i<80;i++){const mid=(lo+hi)/2;(f(mid)>P)?hi=mid:lo=mid;}return (lo+hi)/2;};
out.gImp=solve(x=>v({growth2to5:x}),-0.3,0.5); out.mImp=solve(x=>v({marginTarget:x}),0.05,0.6);
let lo=0.05,hi=0.4; for(let i=0;i<80;i++){const mid=(lo+hi)/2;(v({waccTerminal:mid})>P)?lo=mid:hi=mid;} out.wImp=(lo+hi)/2;
out.gCons=v({growth2to5:0.03}); out.mCons=v({marginTarget:0.28}); out.wt1=v({waccTerminal:WT+0.01}); out.wt75=v({waccTerminal:0.075}); out.wt115=v({waccTerminal:0.115}); out.g0=v({growth2to5:0});
fs.writeFileSync(process.argv[3],JSON.stringify(out,null,1)); console.log(JSON.stringify({esc:out.esc,tv:out.tv,gImp:out.gImp,mImp:out.mImp,wImp:out.wImp,gCons:out.gCons,mCons:out.mCons,wt1:out.wt1,wt75:out.wt75,wt115:out.wt115,g0:out.g0}));
