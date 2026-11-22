import fs from 'node:fs'; import {cargarMotor} from '/home/user/Modelo-JMR-V2/scripts/v2-motor.mjs';
const eng=cargarMotor(); const C=JSON.parse(fs.readFileSync('calc.json')); const out={};
for(const t of ['GOOGL','AMZN','ONON','MSFT','NVDA','EPAM']){const m=JSON.parse(fs.readFileSync('/tmp/claude-0/-home-user/02bdd347-b8be-5ac5-b2fc-27257db31770/scratchpad/nu3/origen/empresas/'+t+'.json'));
 const o=eng.calculateAll(m).scenarios, nn=eng.calculateAll({...m,assumptions:C[t].assumptions}).scenarios;
 out[t]={old:Object.fromEntries(Object.entries(o).map(([k,x])=>[k,{years:x.years,reinvT:x.reinvestmentTerminal,fcffT:x.fcffTerminal,tv:x.terminalValue}])),new:Object.fromEntries(Object.entries(nn).map(([k,x])=>[k,{years:x.years,reinvT:x.reinvestmentTerminal,fcffT:x.fcffTerminal,tv:x.terminalValue}]))};}
fs.writeFileSync('years.json',JSON.stringify(out));
