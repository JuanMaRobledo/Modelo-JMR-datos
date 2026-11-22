import fs from 'node:fs'; import {cargarMotor} from '/home/user/Modelo-JMR-V2/scripts/v2-motor.mjs';
const eng=cargarMotor(); const m=JSON.parse(fs.readFileSync('/tmp/claude-0/-home-user/02bdd347-b8be-5ac5-b2fc-27257db31770/scratchpad/nu3/origen/empresas/ONON.json'));
const C=JSON.parse(fs.readFileSync('calc.json')).ONON; const out={};
for(const [lab,A] of [['old',m.assumptions],['new',C.assumptions]]){const b=A.base;
 const v=o=>{const B={...b,...o};return eng.calculateAll({...m,assumptions:{conservador:B,base:B,optimista:B}}).scenarios.base.perShare;};
 const wis=[b.waccInitial,0.06,0.07,0.08,0.09,0.10], gs=[0.005,0.01,0.02,0.03];
 const G1=wis.map(wi=>gs.map(g=>v({waccInitial:wi,waccTerminal:Math.max(wi-0.0082,g+0.012),gTerminal:g})));
 const mts=[0.12,0.14,0.16,0.18,0.20], g25=[0.05,0.09,0.13,0.17,0.21];
 const G2=mts.map(mt=>g25.map(g=>v({marginTarget:mt,growth2to5:g,margin1:Math.min(b.margin1,mt)})));
 const rs=[0.10,0.15,0.20,0.25,0.30], scs=[0.667,0.833,1,1.167,1.333].map(f=>C.assumptions.base.salesToCapital1to5*f);
 const G3=rs.map(r=>scs.map(s=>v({roicTerminal:r,salesToCapital1to5:s,salesToCapital6to10:s})));
 const pm=[0.10,0.12,0.14,0.16,0.18], pg=[0.03,0.05,0.07,0.09,0.11,0.13];
 const PI=pm.map(mt=>pg.map(g=>v({waccInitial:0.08,waccTerminal:0.065,gTerminal:0.02,marginTarget:mt,growth2to5:g,margin1:Math.min(b.margin1,mt)})));
 const pr={g5:v({growth2to5:0.05}),m12:v({marginTarget:0.12,margin1:0.12}),roicW:v({roicTerminal:b.waccTerminal}),usd:v({waccInitial:0.08,waccTerminal:0.065,gTerminal:0.02}),g0:v({gTerminal:0}),
  c1:v({growth2to5:0.05,marginTarget:0.12,margin1:0.12}),c2:v({growth2to5:0.05,marginTarget:0.12,margin1:0.12,waccInitial:0.08,waccTerminal:0.065,gTerminal:0.02})};
 out[lab]={G1,G2,G3,PI,pr,axes:{wis,gs,mts,g25,rs,scs,pm,pg}};
 console.log(lab,'G1',JSON.stringify(G1.map(r=>r.map(x=>+x.toFixed(1)))));console.log(lab,'G2 row0',JSON.stringify(G2[0].map(x=>+x.toFixed(1))),'G3',JSON.stringify(G3.map(r=>r.map(x=>+x.toFixed(1)))));
 console.log(lab,'PI',JSON.stringify(PI.map(r=>r.map(x=>+x.toFixed(1)))));console.log(lab,JSON.stringify(Object.fromEntries(Object.entries(pr).map(([k,x])=>[k,+x.toFixed(2)]))));}
fs.writeFileSync('onon_g.json',JSON.stringify(out));
