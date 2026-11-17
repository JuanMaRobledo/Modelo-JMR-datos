#!/usr/bin/env node
/**
 * Corrección documental del snapshot «Datos generales», sin alterar los DCF.
 * FUENTE: informes SEC / Investor Relations 10-K especificados por ticker.
 * Campos FY consolidados en financialPresentation.periods[].values.
 * NO modifica history, escenarios, accionistas, libro ni valoraciones.
 */
import fs from 'node:fs';
import {gzipSync,gunzipSync} from 'node:zlib';
import {createHash} from 'node:crypto';
import assert from 'node:assert/strict';
const d='jmr-v2',p=d+'/biblioteca.json',m=JSON.parse(fs.readFileSync(p,'utf8'));
assert.equal(m.schemaVersion,'jmr-biblioteca-gzip-1');
assert.equal(m.app,'jmr-v2');
const old=gunzipSync(fs.readFileSync(d+'/'+m.archive));
assert.equal(createHash('sha256').update(old).digest('hex'),m.sha256);
const b=JSON.parse(old);
assert.equal(b.schemaVersion,'jmr-biblioteca-1');
const files=b.files, snap={};
for(const [k,v] of Object.entries(files))if(k.startsWith('empresas/'))snap[k]={
 history:JSON.stringify(v.history),financials:JSON.stringify(v.financials),
 assumptions:JSON.stringify(v.assumptions),libro:JSON.stringify(v.libro),
 revision:JSON.stringify(v.revision),analysis:JSON.stringify(v.analysis)
};
const SEC={
CMG:'https://www.sec.gov/Archives/edgar/data/1058090/000105809026000009/cmg-20251231.htm',
DUOL:'https://www.sec.gov/Archives/edgar/data/1562088/000162828026012494/duol-20251231.htm',
EPAM:'https://www.sec.gov/Archives/edgar/data/1352010/000135201026000015/epam-20251231.htm',
LULU:'https://www.sec.gov/Archives/edgar/data/1397187/000139718726000020/lulu-20260201.htm',
MELI:'https://www.sec.gov/Archives/edgar/data/1099590/000109959026000006/meli-20251231.htm',
MSFT:'https://www.microsoft.com/investor/reports/ar26/index.html',
NKE:'https://www.sec.gov/Archives/edgar/data/320187/000032018726000088/nke-20260531.htm',
NVDA:'https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm',
UBER:'https://www.sec.gov/Archives/edgar/data/1543151/000154315126000015/uber-20251231.htm',
AAPL:'https://www.sec.gov/Archives/edgar/data/320193/000032019326000026/aapl-20260926.htm'
};
const patch={
 CMG:{year:2025,values:{
  sharesOutstanding:1304.360,shortTermInvestments:698.591,dividendsPaid:0
 },notes:{
  sharesOutstanding:'Estado de patrimonio FY2025: 1.304.360 miles de acciones emitidas al 31-dic-2025; verificar que no hay acciones en tesorería adicionales. División por 1000 para millones; NO acciones promedio diluidas.',
  shortTermInvestments:'Balance FY2025: Investments corriente = 698.591 miles USD = 698,591 millones; NO igual a inversiones no corrientes 197,123 millones.',
  dividendsPaid:'Política dividendos 10-K FY2025: no ha declarado ni pagado dividendos sobre acciones comunes. Cero CONFIRMADO.'
 }},
 DUOL:{year:2025,values:{
  sharesOutstanding:46.628,dividendsPaid:0
 },notes:{
  sharesOutstanding:'Balance 31-dic-2025: Clase A 40.368 miles + Clase B 6.260 miles = 46,628 millones de acciones, ambas clases. No usar promedio ponderado diluido.',
  dividendsPaid:'10-K 2025: nunca ha declarado ni pagado dividendos en efectivo. Cero CONFIRMADO.'
 }},
 EPAM:{year:2025,values:{
  revenue:5457.056,cogs:3883.535,sga:928.707,daExpense:124.811,
  operatingProfit:520.003,ebit:520.003,
  pretaxIncome:505.624,taxExpense:127.946,
  consolidatedNetIncome:377.678,netIncome:377.678,netIncomeCommon:377.678,
  sharesOutstanding:54.274,sharesDilutedWA:56.233,epsDiluted:6.72,
  cash:1296.077,shortTermInvestments:6.1,assets:4902.136,
  liabilities:1224.328,equity:3677.808,minority:0.582,
  currentAssets:2533.888,longTermDebt:25.034,totalDebt:25.034,
  currentLeases:37.173,leases:81.497,
  operatingCF:654.934,capex:42.243,da:124.811,
  dividendsPaid:0,interestExpense:null
 },notes:{
  revenue:'10-K SEC FY2025 final: ingresos 5.457.056 miles; NO confundir con LTM Sep-2026 5.648.806 miles.',
  operatingProfit:'10-K SEC FY2025: EBIT GAAP 520.003 miles; NO LTM Sep-2026 594.172 miles.',
  cash:'10-K SEC FY2025: cash and cash equivalents 1.296.077 miles; NO cifra LTM 2026 965.173 miles.',
  shortTermInvestments:'10-K SEC FY2025 MD&A: short-term investments 6,1 millones, incluidas en otras líneas; exactitud publicada a un decimal.',
  sharesOutstanding:'10-K SEC FY2025 balance: 54.274 miles shares issued and outstanding al 31-dic-2025.',
  interestExpense:'FY2025 no se acreditó gasto por intereses separado suficiente; no copiar estimado o valor LTM 2026.',
  dividendsPaid:'10-K SEC 2025: nunca declaró ni pagó dividendos en efectivo. Cero CONFIRMADO.',
  capex:'10-K FY2025 cash flows: purchases of property and equipment 42.243 miles.',
  operatingCF:'10-K FY2025 cash flows: CFO 654.934 miles.',
  taxExpense:'10-K FY2025: utilidad antes de impuestos 505.624 − utilidad neta consolidada 377.678 = 127.946 miles; derivación controlada.'
 }},
 LULU:{year:2025,values:{
  sharesOutstanding:116.496,totalCash:1807.202,dividendsPaid:0
 },notes:{
  sharesOutstanding:'10-K FY terminado 1-feb-2026, estado patrimonio: common stock 111.380 miles + 5.116 miles exchangeable económicamente equivalentes a una acción = 116,496 millones. No duplicar special voting stock (no derecho económico adicional).',
  totalCash:'Balance SEC 1-feb-2026: cash and cash equivalents 1.807.202 miles; sin renglón separado de short-term investments. Se publica total cash reportado, sin inventar shortTermInvestments=0.',
  dividendsPaid:'10-K 2025 cash flows no incluye dividendos de comunes; política no anticipa dividendos. Cero confirmado en FY.'
 }},
 MELI:{year:2025,values:{dividendsPaid:0},notes:{
  dividendsPaid:'10-K FY2025: consejo suspendió pagos de dividendos sobre acciones comunes desde el 1T2018. Cero CONFIRMADO FY2025.'
 }},
 MSFT:{year:2026,values:{dividendsPaid:26445},notes:{
  dividendsPaid:'10-K FY2026, cash flow financing: common stock cash dividends PAID = 26.445 millones. NO usar 27.035 millones declarados porque incluye dividendo pagadero en septiembre.'
 }},
 NKE:{year:2026,values:{sharesOutstanding:1483,dividendsPaid:2407},notes:{
  sharesOutstanding:'10-K FY2026 balance/equity al 31-may-2026: Clase A 281 millones + Clase B 1.202 millones = 1.483 millones (redondeado por el emisor). NO usar 1.483.498.703 del 8-jul-2026 para cierre FY.',
  dividendsPaid:'10-K FY2026 cash flows financiación: Dividends — common and preferred 2.407 millones PAGADOS. Incluye componente preferente; payout común es proxy y debe marcarse.'
 }},
 NVDA:{year:2026,values:{sharesOutstanding:24304},notes:{
  sharesOutstanding:'10-K FY2026 balance al 25-ene-2026: 24.304 millones de acciones comunes emitidas y en circulación; misma base split-adjusted que precio de referencia.'
 }},
 UBER:{year:2025,values:{dividendsPaid:0},notes:{
  dividendsPaid:'10-K FY2025: nunca declaró ni pagó dividendos sobre su capital común. Cero CONFIRMADO.'
 }}
};
let updated=[];
for(const [ticker,obj] of Object.entries(patch)){
 const mod=files['empresas/'+ticker+'.json'];assert.ok(mod,'Sin expediente '+ticker);
 assert.ok(Array.isArray(mod.history));
 const existing=(mod.financialPresentation?.periods||[]).find(x=>x.year===obj.year&&!/^LTM/i.test(x.periodo||''));
 assert.ok(existing,'No hay FY '+ticker+' '+obj.year);
 existing.values??={};existing.sources??={};
 for(const [field,val] of Object.entries(obj.values)){
  if(field==='revenue'&&ticker==='EPAM')assert.ok(existing.values.revenue===undefined || existing.values.revenue===null || existing.values.revenue>5000);
  existing.values[field]=val;
  existing.sources[field]={documento:'10-K FY '+obj.year,fuente:SEC[ticker],url:SEC[ticker],periodo:'FY '+obj.year,moneda:'USD',unidades:field==='sharesOutstanding'||field==='sharesDilutedWA'?'millones de acciones':field==='epsDiluted'?'USD por acción':'USD millones',valorReportado:val,nota:obj.notes?.[field]||'Partida conciliada con informe anual; valor expresado en millones.',verificacion:'Fuente primaria, dato documental o derivación indicada'};
 }
 mod.financialPresentation.completadoDatosGenerales??=[];
 mod.financialPresentation.completadoDatosGenerales.push({fecha:'2026-11-16',periodo:'FY '+obj.year,campos:Object.keys(obj.values),documento:SEC[ticker],modificaDCF:false,version:'datos-generales-snapshot-1'});
 updated.push({ticker,year:obj.year,fields:Object.keys(obj.values)});
}
{
 const m=files['empresas/AAPL.json'];
 assert.ok(m);
 m.datosGenerales??={};
 m.datosGenerales.inversionesNoOperativasAdicionales={
  valor:80213,
  fuente:'Apple FY2026 10-K Nota 4: inversiones negociables no corrientes 80.213 millones de USD; conciliación FY2026 cash 36.305 + inversiones corrientes 20.417 + inversiones no corrientes 80.213 = 136.935, mismo puente de caja del DCF R6.',
  url:SEC.AAPL,fecha:'2026-09-26',esNoOperativo:true
 };
 updated.push({ticker:'AAPL',year:2026,fields:['datosGenerales.inversionesNoOperativasAdicionales']});
}
for(const [k,v] of Object.entries(files)){
 if(k.startsWith('empresas/')){
  const a=snap[k];assert.equal(JSON.stringify(v.history),a.history,'History DCF fue alterado '+k);
  assert.equal(JSON.stringify(v.financials),a.financials,'Financials DCF fue alterado '+k);
  assert.equal(JSON.stringify(v.assumptions),a.assumptions,'Escenarios DCF alterados '+k);
  assert.equal(JSON.stringify(v.libro),a.libro,'Libro DCF alterado '+k);
  assert.equal(JSON.stringify(v.revision),a.revision,'Revision DCF alterada '+k);
  assert.equal(JSON.stringify(v.analysis),a.analysis,'Análisis cualitativo alterado '+k);
 }
}
assert.equal(b.files['catalogo.json'].empresas.length,11);
console.log('CAMBIOS_DOCUMENTADOS',JSON.stringify(updated));
console.log('NO ALTERADOS',Object.keys(snap).length,'history, financials, assumptions, libro, revision, analysis');
if(process.argv.includes('--aplicar')){
 const txt=JSON.stringify(b,null,1)+'\n';
 const sha=createHash('sha256').update(txt).digest('hex'),archive='biblioteca-'+sha+'.json.gz';
 fs.writeFileSync(d+'/'+archive,gzipSync(txt));
 fs.writeFileSync(p,JSON.stringify({schemaVersion:'jmr-biblioteca-gzip-1',app:'jmr-v2',archive,sha256:sha},null,1)+'\n');
 console.log('CANDIDATO',sha,archive);
}
