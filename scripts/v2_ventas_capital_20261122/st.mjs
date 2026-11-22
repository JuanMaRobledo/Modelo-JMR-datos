import fs from 'node:fs'; import {cargarMotor} from '/home/user/Modelo-JMR-V2/scripts/v2-motor.mjs';
const eng=cargarMotor(); const [t,json]=process.argv.slice(2); const tests=JSON.parse(json);
const m=JSON.parse(fs.readFileSync('/tmp/claude-0/-home-user/02bdd347-b8be-5ac5-b2fc-27257db31770/scratchpad/nu3/origen/empresas/'+t+'.json'));
const C=JSON.parse(fs.readFileSync('calc.json'))[t];
const run=(A,o)=>{const B={...A.base,...o};return eng.calculateAll({...m,assumptions:{conservador:B,base:B,optimista:B}}).scenarios.base;};
for(const [name,o] of Object.entries(tests)){const a=run(m.assumptions,o), b=run(C.assumptions,o); console.log(name.padEnd(28),'old',a.perShare.toFixed(2),'new',b.perShare.toFixed(2), 'rev5', (a.revenues?.[5]??a.years?.[4]?.revenue??''));}
