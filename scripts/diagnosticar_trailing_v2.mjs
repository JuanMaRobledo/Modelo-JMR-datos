#!/usr/bin/env node
// Diagnóstico únicamente: no crea múltiplos ni inventa acciones al cierre.
import {readFileSync} from 'node:fs';
import {gunzipSync} from 'node:zlib';
const dir=new URL('../jmr-v2/', import.meta.url);
const man=JSON.parse(readFileSync(new URL('biblioteca.json',dir),'utf8'));
const d=man.schemaVersion==='jmr-biblioteca-gzip-1'?
 JSON.parse(gunzipSync(readFileSync(new URL(man.archive,dir))).toString('utf8')):man;
const num=x=>typeof x==='number'&&Number.isFinite(x);
const reps=[];
for(const c of d.files['catalogo.json'].empresas){
 const m=d.files[c.archivo];
 const p=m.financialPresentation?.periods||[];
 const h=m.history||[];
 const rows=[];
 for(const x of h){
  const e=p.find(k=>k.year===x.year&&(k.periodo||'')===(x.periodo||''))||
      p.find(k=>k.year===x.year&&!/^LTM/i.test(k.periodo||'')&&!/^LTM/i.test(x.periodo||''));
  const v=e?.values||{};
  const px=num(v.stockPrice)?v.stockPrice:(/^LTM/i.test(x.periodo||'')?m.financials?.sharePrice:x.sharePrice);
  const shares=num(v.sharesOutstanding)?v.sharesOutstanding:x.sharesOutstanding;
  const cash=num(v.cash)?v.cash:x.cash;
  const inv=v.shortTermInvestments;
  const debt=num(v.totalDebt)?v.totalDebt:x.debt;
  const minority=num(v.minority)?v.minority:x.minority;
  rows.push({periodo:x.periodo||x.year,precio:num(px),accionesCierre:num(shares),caja:num(cash),inversionesCorto:num(inv),deuda:num(debt),minoritarias:num(minority),cap:num(px)&&num(shares),ev:num(px)&&num(shares)&&num(cash)&&num(inv)&&num(debt)&&num(minority)});
 }
 const cnt=k=>rows.filter(x=>x[k]).length;
 reps.push({ticker:c.ticker,cik:m.cik||null,annualReportDocuments:(m.annualReportDocuments||[]).map(z=>({fy:z.fy,periodEnd:z.periodEnd})),periodos:m.financialPresentation?.periods?.map(z=>({year:z.year,periodo:z.periodo,fechaCierre:z.fechaCierre,periodEnd:z.periodEnd}))?.slice(0,12),total:rows.length,precio:cnt('precio'),accionesCierre:cnt('accionesCierre'),capitalizacion:cnt('cap'),evCompleto:cnt('ev'),
 faltantesMasReciente:rows.at(-1),sinDato:rows.filter(x=>!x.cap).map(x=>x.periodo)});
}
console.log('DIAGNOSTICO_TRAILING_V2='+JSON.stringify(reps));
