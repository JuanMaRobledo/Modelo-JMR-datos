import fs from 'node:fs'; import {cargarMotor} from '/home/user/Modelo-JMR-V2/scripts/v2-motor.mjs';
const eng=cargarMotor(); const O='/tmp/claude-0/-home-user/02bdd347-b8be-5ac5-b2fc-27257db31770/scratchpad/nu3/origen/empresas/';
const P={MSFT:{a:0.5937825468202881,f:[0.6875,1,1.375],wi:0.10737116925238065},NVDA:{a:1.640402347024309,f:[0.8148,1,1.2593]},
GOOGL:{a:0.900289332166322,f:[0.7,1,1.3]},AMZN:{a:1.046019588887825,f:[0.8,1,1.3]},ONON:{a:2.13915259636827,f:[0.6667,1,1.3333]},EPAM:{a:2.128396168830679,f:[0.8182,1,1.1818]}};
const S=['conservador','base','optimista']; const out={};
for(const [t,p] of Object.entries(P)){
  const m=JSON.parse(fs.readFileSync(O+t+'.json')); const old=eng.calculateAll(m).scenarios;
  // reproducir sensitivity5x5 antiguo
  const grid=(mm,s5)=>s5.rows.map(r=>s5.growths.map(g=>{const B={...mm.assumptions.base,waccTerminal:r.wacc,gTerminal:g};return eng.calculateAll({...mm,assumptions:{conservador:B,base:B,optimista:B}}).scenarios.base.perShare;}));
  let rep=null; if(m.sensitivity5x5){const g=grid(m,m.sensitivity5x5); rep=Math.max(...g.flat().map((x,i)=>Math.abs(x-m.sensitivity5x5.rows[Math.floor(i/5)].cells[i%5])));}
  S.forEach((s,i)=>{m.assumptions[s].salesToCapital1to5=p.a*p.f[i];m.assumptions[s].salesToCapital6to10=p.a*p.f[i]; if(p.wi) m.assumptions[s].waccInitial=p.wi;});
  const r=eng.calculateAll(m).scenarios;
  const o={sc:Object.fromEntries(S.map((s,i)=>[s,p.a*p.f[i]])),old:Object.fromEntries(S.map(s=>[s,old[s].perShare])),esc:Object.fromEntries(S.map(s=>[s,r[s].perShare])),
    det:Object.fromEntries(S.map(s=>[s,{sumPV:r[s].sumPV,pvTerminal:r[s].pvTerminal,ev:r[s].evBeforeRisk,equity:r[s].equity}])),
    detOld:Object.fromEntries(S.map(s=>[s,{sumPV:old[s].sumPV,pvTerminal:old[s].pvTerminal,ev:old[s].evBeforeRisk,equity:old[s].equity}])),
    price:m.financials.sharePrice, assumptions:m.assumptions, rep};
  if(m.sensitivity5x5){const g=grid(m,m.sensitivity5x5); o.s5={...m.sensitivity5x5,rows:m.sensitivity5x5.rows.map((r,i)=>({...r,cells:g[i]})),centerValue:r.base.perShare};}
  out[t]=o; console.log(t,'rep5x5',rep, S.map(s=>o.old[s].toFixed(2)+'→'+o.esc[s].toFixed(2)).join(' '), 'precio',o.price);
}
fs.writeFileSync('calc.json',JSON.stringify(out,null,1));
