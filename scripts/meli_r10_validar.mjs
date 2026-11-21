// Recalcula el MELI R10 con el motor oficial del repositorio V2 y crea matrices verificables.
import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
const stage=path.resolve(process.argv[2]||'/tmp/meli-r10');
const repoEngine=path.resolve(process.argv[3]||'engine');
const {cargarMotor}=await import(pathToFileURL(path.join(repoEngine,'scripts/v2-motor.mjs')));
const {crearMotor}=await import(pathToFileURL(path.join(repoEngine,'docs/v2/motores/despacho.mjs')));
const motor=crearMotor(cargarMotor());
const modelPath=path.join(stage,'origen/empresas/MELI.json');
const model=JSON.parse(fs.readFileSync(modelPath,'utf8'));
const expected=JSON.parse(fs.readFileSync(path.join(stage,'expected.json'),'utf8')).prices;
const r=motor.calculateAll(model);
const scenarios=r.scenarios||{};
const prices={};
for(const name of ['conservador','base','optimista']){
  const p=scenarios[name]?.perShare;
  if(!(Number.isFinite(p)&&p>0))throw Error('Valor no finito '+name+': '+p);
  const relative=Math.abs(p-expected[name])/expected[name];
  if(relative>0.005)throw Error('Libro/motor '+name+' no concilian: '+p+' vs '+expected[name]+' Δ='+relative);
  prices[name]=p;
}
const b=scenarios.base;
if(Math.abs(b.mosPrice-expected.base*0.65)>0.01)throw Error('MOS 35% incorrecto: '+b.mosPrice);
if(model.revision?.id!=='MELI-V2-LTM20260930-R10')throw Error('Revisión incorrecta');
if(model.libro?.sha256!=='b798cd448f34d773a7dd781461e886c12d85976b16863dabaec98c9bd4cb1aa1')throw Error('Huella del libro no coincide');
const wacc=model.assumptions.base.waccInitial,g=model.assumptions.base.gTerminal;
function sensitivity(yValues,xValues,assign){
 const values=[];
 for(const y of yValues){let row=[];for(const x of xValues){
   const copy=structuredClone(model);
   assign(copy.assumptions.base,y,x);
   const v=motor.calculateAll(copy).scenarios?.base?.perShare;
   if(!Number.isFinite(v)||v<=0)throw Error('Sensibilidad inválida '+y+' / '+x+': '+v);
   row.push(v);
 }values.push(row)}
 return values;
}
const waccAxis=[wacc-.01,wacc-.005,wacc,wacc+.005,wacc+.01];
const gAxis=[g-.01,g-.005,g,g+.005,g+.01];
const grids={
  wacc_g:{
    rowAxis:waccAxis,columnAxis:gAxis,
    values:sensitivity(waccAxis,gAxis,(a,y,x)=>{a.waccInitial=y;a.waccTerminal=y;a.gTerminal=x;})
  },
  margen1_crecimiento1:{
    rowAxis:[.10,.11,.12,.13,.14],
    columnAxis:[.26,.28,.30,.32,.34],
    values:sensitivity([.10,.11,.12,.13,.14],[.26,.28,.30,.32,.34],(a,y,x)=>{a.margin1=y;a.growth1=x;})
  },
  crecimientoto5_margenobjetivo:{
    rowAxis:[.16,.18,.20,.22,.24],
    columnAxis:[.13,.14,.15,.16,.17],
    values:sensitivity([.16,.18,.20,.22,.24],[.13,.14,.15,.16,.17],(a,y,x)=>{a.growth2to5=y;a.marginTarget=x;})
  },
  roicterminal_ventascapital:{
    rowAxis:[.14,.16,.18,.20,.22],
    columnAxis:[2.5,3,3.5,4,4.5],
    values:sensitivity([.14,.16,.18,.20,.22],[2.5,3,3.5,4,4.5],(a,y,x)=>{a.roicTerminal=y;a.salesToCapital1to5=x;a.salesToCapital6to10=x;})
  }
};
for(const [name,grid] of Object.entries(grids)){
  const center=grid.values[2][2];
  if(Math.abs(center-expected.base)/expected.base>0.005)throw Error('Centro matriz '+name+' no coincide: '+center);
}
const info={scenarios:prices,mos:b.mosPrice,engineBookTolerance:0.005,grids,engineShape:Object.keys(r),terminalShare:74935.89660043699/114272.31669649723};
fs.writeFileSync(path.join(stage,'engine-results.json'),JSON.stringify(info,null,2));
console.log('PARITY_OK',JSON.stringify({revision:model.revision.id,scenarios:prices,mos:b.mosPrice,centerSensitivity:grids.wacc_g.values[2][2],sensitivityCount:Object.keys(grids).length}));
