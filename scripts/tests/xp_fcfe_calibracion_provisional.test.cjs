'use strict';
const test=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs'),path=require('node:path');
const read=p=>JSON.parse(fs.readFileSync(path.resolve(__dirname,'../..',p),'utf8'));
const x=read('candidatos/valoraciones/XP-20261031-A12-R1/CALIBRACION_FCFE_PROVISIONAL.json');
const ws=read('candidatos/valoraciones/XP-20261031-A12-R1/workspace.json'),catalog=read('catalogo.json');
const near=(a,b,tolerance=1e-6)=>assert.ok(Math.abs(a-b)<tolerance,String(a)+' != '+String(b));
test('XP A-1.2 no publica nuevo FCFE ni toca la revisión anterior',()=>{
 assert.equal(x.publicationStatus,'NO_PUBLICAR');
 assert.equal(ws.publicationStatus,'NO_PUBLICAR');
 assert.equal(ws.valorPrincipal,null);
 assert.equal(x.originalRevision,'XP-20261026-R2');
 assert.ok(catalog.valoraciones.includes(ws.trabajo.valoracionAnterior));
 assert.ok(!catalog.valoraciones.some(p=>p.includes(x.revision)));
 assert.equal(x.accountingCut,'2026-06-30');
 assert.equal(x.priceDate,'2026-10-30');
});
test('XP coherencia de monedas, fecha, Ke y dilución',()=>{
 const a=x.inputs;
 assert.equal(x.units.fcfe,'BRL millones');
 assert.equal(x.units.perShare,'USD por acción');
 near(a.fxPTAX,5.4209);
 near(a.marketPrice,14.29);
 near(a.rfUSD,.0494);near(a.erpMature,.037);near(a.crpBrasilJuly,.031);
 near(a.keUSD,a.rfUSD+a.beta*a.erpMature+a.crpBrasilJuly+a.repricingShockAnalyst);
 near(a.keBRL,(1+a.keUSD)*(1+a.inflationBRL)/(1+a.inflationUSD)-1);
 near(a.effectiveShares,a.dilutionBasicShares+a.rsuPsu*a.vestingFraction);
 assert.equal(x.checks.hasCET1RequirementBuffer,false);
});
test('XP proyección de cuatro escenarios 10 años y EV/acción usa FCFE BRL',()=>{
 assert.equal(x.scenarios.length,4);near(x.scenarios.reduce((p,s)=>p+s.probability,0),1);
 for(const s of x.scenarios){
  assert.equal(s.fcfe.length,10); assert.equal(s.presentValueFCFE.length,10);
  near(s.equityValueBRLm,s.explicitValue+s.terminalPresentValue);
  near(s.explicitValue,s.presentValueFCFE.reduce((p,y)=>p+y,0));
  near(s.perShareBRL,s.equityValueBRLm/x.inputs.effectiveShares);
  near(s.perShareUSD,s.perShareBRL/x.inputs.fxPTAX);
  near(s.mos35USD,s.perShareUSD*.65);
  near(s.terminalWeight,s.terminalPresentValue/s.equityValueBRLm);
  for(let i=0;i<10;i++){
   near(s.fcfe[i],s.netIncomeAttributable[i]-s.equityReinvestment[i]);
   near(s.presentValueFCFE[i],s.fcfe[i]/s.discountAccumulated[i]);
  }
 }
 const three=x.scenarios.filter(z=>z.name!=='Disrupción');
 near(three.reduce((a,s)=>a+s.probability,0),.9);
 near(x.weightedThreeWithoutDisruption,three.reduce((a,s)=>a+s.probability*s.perShareUSD,0)/.9);
});
test('XP seis sensibilidades 5x5 con centros exactos: DCF y cuatro múltiplos',()=>{
 assert.equal(x.dcfSensitivities.length,3);
 for(const m of x.dcfSensitivities){
  assert.equal(m.values.length,5);assert.equal(m.columns.length,5);
  for(const v of m.values){assert.equal(v.length,5);assert.ok(v.every(Number.isFinite));}
  near(m.values[2][2],x.scenarios[0].perShareUSD);
 }
 assert.equal(x.multipleSensitivities.length,4);
 for(const m of x.multipleSensitivities){
  assert.equal(m.grid.length,5);assert.equal(m.rows.length,5);assert.equal(m.columns.length,5);
  for(const row of m.grid){assert.equal(row.length,5);assert.ok(row.every(Number.isFinite));}
  near(m.grid[2][2],m.center);
 }
 assert.equal(x.multipleSensitivities.find(m=>m.method==='P/FCFE').weight,0);
 assert.equal(x.checks.hasIndependentPFCFEAnchor,false);
});
