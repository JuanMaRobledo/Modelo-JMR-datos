import fs from 'node:fs'; import {cargarMotor} from '/home/user/Modelo-JMR-V2/scripts/v2-motor.mjs';
const eng=cargarMotor(); const [t,ov,k,lo0,hi0,P]=process.argv.slice(2);
const m=JSON.parse(fs.readFileSync('/tmp/claude-0/-home-user/02bdd347-b8be-5ac5-b2fc-27257db31770/scratchpad/nu3/origen/empresas/'+t+'.json'));
const C=JSON.parse(fs.readFileSync('calc.json'))[t];
for(const [lab,A] of [['old',m.assumptions],['new',C.assumptions]]){const v=x=>{const B={...A.base,...JSON.parse(ov),[k]:x};return eng.calculateAll({...m,assumptions:{conservador:B,base:B,optimista:B}}).scenarios.base.perShare;};
 let lo=+lo0,hi=+hi0; for(let i=0;i<100;i++){const mid=(lo+hi)/2;(v(mid)>+P)?hi=mid:lo=mid;} console.log(lab,((lo+hi)/2*100).toFixed(2));}
