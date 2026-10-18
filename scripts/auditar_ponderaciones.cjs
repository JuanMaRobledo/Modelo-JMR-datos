"use strict";
// Auditoría estructural sin redes ni credenciales. Ejecutar: node scripts/auditar_ponderaciones.cjs
const fs=require("node:fs"),path=require("node:path"),assert=require("node:assert/strict");
const base=path.join(__dirname,"..","valoraciones");
const files=fs.readdirSync(base).filter(f=>f.endsWith(".json"));
assert.equal(files.length,38,"Cobertura incompleta de valoraciones");
const eps=1e-7,near=(a,b)=>typeof a==="number"&&typeof b==="number"&&Math.abs(a-b)<eps;
let nd=0,ok=0, normal=0;
const needsSpecial=new Set(["GRUPOARGOS","PFGRUPOARG","MP"]);
for(const file of files){
 const j=JSON.parse(fs.readFileSync(path.join(base,file),"utf8"));
 assert.ok(j.ticker&&file.startsWith(j.ticker+"-"),"Ticker/archivo: "+file);
 const m=j.metodos||[],s=j.seleccionMultiples?.metodos||[];
 const sx=j.sensibilidadMultiples;
 assert.ok(sx&&sx.methods===7&&sx.scenarios?.length===3&&sx.disrupcionFuera,
   j.ticker+": faltan 7 métodos y tres escenarios ordinarios separados del estrés");
 assert.equal(sx.controlesOK+sx.noDisponibles,21,j.ticker+": suma de matrices");
 ok+=sx.controlesOK;nd+=sx.noDisponibles;
 const total=m.reduce((a,x)=>a+(Number(x.peso)||0),0);
 if(!needsSpecial.has(j.ticker)){assert.ok(near(total,1),j.ticker+": pesos no suman 100%"); normal++;}
 if(!["GRUPOARGOS","PFGRUPOARG"].includes(j.ticker)){
  for(const x of s){const actual=m.find(z=>z.nombre===x.nombre);
   const w=actual?actual.peso:0;
   assert.ok(near(Number(x.pesoVigente)||0,Number(w)||0),
     j.ticker+": selector publicado diferente de método "+x.nombre);
   assert.ok(!(x.pesoVigente>0&&x.control!=="OK"),j.ticker+": método N/D con peso positivo "+x.nombre);
  }
 }
 if(j.descuentoMultiples&&typeof j.descuentoMultiples.pesoDcf==="number"&&j.ticker!=="MP"&&!["GRUPOARGOS","PFGRUPOARG"].includes(j.ticker)){
  const dcf=m.find(x=>/DCF/i.test(x.nombre));
  assert.ok(dcf&&near(j.descuentoMultiples.pesoDcf,dcf.peso),j.ticker+": peso DCF en dos registros no concilia");
 }
}
assert.equal(ok,723,"Cantidad histórica de centros OK inesperada");
assert.equal(nd,75,"Cantidad histórica de centros N/D inesperada");
const n=JSON.parse(fs.readFileSync(path.join(base,"NFLX-1792004267547.json"),"utf8"));
assert.ok(near(n.descuentoMultiples.pesoDcf,.6)&&near(n.descuentoMultiples.pesoMultiplos,.4));
assert.ok(near(n.escenariosDCF.base,71.68383443894892));
assert.ok(near(n.descuentoMultiples.multiplesHoy.base,87.6045115538154));
assert.ok(near(n.valorPresentePonderado.base,78.0521052848955));
assert.ok(near(n.objetivoPonderado.base,108.32704875135202));
assert.equal(n.baseMOS,"dcfBase");
assert.ok(near(n.precioMOS,n.escenariosDCF.base*(1-n.mos)),"NFLX MOS debe basarse en DCF Base");
console.log(JSON.stringify({estado:"OK",empresas:files.length,matricesOK:ok,matricesND:nd,registrosNormales:normal,excepciones:[...needsSpecial]},null,2));
