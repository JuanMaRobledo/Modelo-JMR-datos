// Sondas sobre el Base (antiguo y nuevo): v(overrides), grids, implícitos.
import fs from 'node:fs'; import {cargarMotor} from '/home/user/Modelo-JMR-V2/scripts/v2-motor.mjs';
const eng=cargarMotor(); const [t,cfgPath,outPath]=process.argv.slice(2); const cfg=JSON.parse(fs.readFileSync(cfgPath));
const m=JSON.parse(fs.readFileSync('/tmp/claude-0/-home-user/02bdd347-b8be-5ac5-b2fc-27257db31770/scratchpad/nu3/origen/empresas/'+t+'.json'));
const C=JSON.parse(fs.readFileSync('calc.json'))[t];
const mk=A=>o=>{const B={...A.base,...o};return eng.calculateAll({...m,assumptions:{conservador:B,base:B,optimista:B}}).scenarios.base;};
const res={};
for(const [lab,A] of [['old',m.assumptions],['new',C.assumptions]]){
  const v=o=>mk(A)(o).perShare; const r={};
  const full=eng.calculateAll({...m,assumptions:A}).scenarios;
  r.esc=Object.fromEntries(Object.entries(full).map(([k,x])=>[k,x.perShare]));
  r.tv=Object.fromEntries(Object.entries(full).map(([k,x])=>[k,x.pvTerminal/x.evBeforeRisk]));
  r.det=Object.fromEntries(Object.entries(full).map(([k,x])=>[k,{sumPV:x.sumPV,pvTerminal:x.pvTerminal,ev:x.evBeforeRisk,equity:x.equity}]));
  r.probes=Object.fromEntries(Object.entries(cfg.probes||{}).map(([k,o])=>[k,v(o)]));
  r.grids=Object.fromEntries(Object.entries(cfg.grids||{}).map(([k,g])=>[k,{...g,m:g.rows.map(x=>g.cols.map(y=>v({[g.rk]:x,[g.ck]:y,...(g.extra||{}),...(g.tie?{salesToCapital6to10:y}:{}),...(g.m1cap?{margin1:Math.min(A.base.margin1,g.rk==='marginTarget'?x:y)}:{})})))}]));
  const P=cfg.price; const solve=(k,lo,hi,inc=true)=>{for(let i=0;i<100;i++){const mid=(lo+hi)/2; const val=v({[k]:mid}); ((val>P)===inc)?hi=mid:lo=mid;}return (lo+hi)/2;};
  if(P){r.imp2=Object.fromEntries((cfg.solve||[]).map(([k,lo,hi,inc])=>[k,solve(k,lo,hi,inc)]));r.imp={growth2to5:solve('growth2to5',-0.5,0.8),marginTarget:solve('marginTarget',0.0,0.9),waccTerminal:solve('waccTerminal',0.03,0.5,false)};}
  res[lab]=r;
}
fs.writeFileSync(outPath,JSON.stringify(res,null,1));
const f=x=>typeof x==='number'?x.toFixed(4):x;
console.log('esc',JSON.stringify(res.old.esc),'→',JSON.stringify(res.new.esc));
console.log('tv',JSON.stringify(res.old.tv),'→',JSON.stringify(res.new.tv));
for(const k in res.old.probes) console.log('probe',k,f(res.old.probes[k]),'→',f(res.new.probes[k]));
if(res.old.imp2) console.log('imp2',JSON.stringify(res.old.imp2),'→',JSON.stringify(res.new.imp2));
if(res.old.imp) console.log('imp',JSON.stringify(res.old.imp),'→',JSON.stringify(res.new.imp));
for(const k in res.old.grids) console.log('grid',k,JSON.stringify(res.old.grids[k].m.map(r=>r.map(x=>Math.round(x)))),'\n   →',JSON.stringify(res.new.grids[k].m.map(r=>r.map(x=>Math.round(x)))));
