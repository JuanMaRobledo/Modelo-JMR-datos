#!/usr/bin/env node
// Completa exclusivamente precios FY verificables de V2. NO altera DCF, históricos
// económicos, acciones, supuestos ni los libros Google Sheets. --aplicar genera
// manifiesto y gzip atómicos para revisarlos en un PR, no publica en main.
import fs from 'node:fs';
import path from 'node:path';
import {gzipSync,gunzipSync} from 'node:zlib';
import {createHash} from 'node:crypto';

const raiz=path.resolve('jmr-v2');
const manPath=path.join(raiz,'biblioteca.json');
const man=JSON.parse(fs.readFileSync(manPath,'utf8'));
if(man.schemaVersion!=='jmr-biblioteca-gzip-1'||man.app!=='jmr-v2'||man.archive!==`biblioteca-${man.sha256}.json.gz`)throw Error('Formato o manifest no soportado');
const before=gunzipSync(fs.readFileSync(path.join(raiz,man.archive)));
if(createHash('sha256').update(before).digest('hex')!==man.sha256)throw Error('SHA no coincide');
const data=JSON.parse(before);
if(data.schemaVersion!=='jmr-biblioteca-1'||data.app!=='jmr-v2')throw Error('Datos incompatibles');
const cierres={
  // AAPL: cierres reportados en sus formularios 10-K. Las acciones históricas
  // del libro AAPL están reexpresadas a la base posterior al split 4:1 de 2020:
  // 2017 5.126,201 M reportadas -> 20.504,804 M en el libro; 2019 4.443,236 M
  // reportadas -> 17.772,944 M. Por eso usamos cierre Yahoo ajustado SOLO por splits,
  // no precio original sin ajustar, evitando multiplicar artificialmente el market cap.
  AAPL:{2017:'2017-09-30',2018:'2018-09-29',2019:'2019-09-28',2020:'2020-09-26',2021:'2021-09-25',2022:'2022-09-24',2023:'2023-09-30',2024:'2024-09-28',2025:'2025-09-27',2026:'2026-09-26'},
  // Cierres de año calendario o junio conforme a los 10-K; no inferir del
  // texto LTM, ni rellenar empresas sin fechas documentadas.
  MSFT:{2018:'2018-06-30',2019:'2019-06-30',2020:'2020-06-30',2021:'2021-06-30',2022:'2022-06-30',2023:'2023-06-30',2024:'2024-06-30',2025:'2025-06-30',2026:'2026-06-30'},
  UBER:{2019:'2019-12-31',2020:'2020-12-31',2021:'2021-12-31',2022:'2022-12-31',2023:'2023-12-31',2024:'2024-12-31',2025:'2025-12-31'},
  MELI:{2017:'2017-12-31',2018:'2018-12-31',2019:'2019-12-31',2020:'2020-12-31',2021:'2021-12-31',2022:'2022-12-31',2023:'2023-12-31',2024:'2024-12-31',2025:'2025-12-31'}
};
const asNum=v=>typeof v==='number'&&Number.isFinite(v)?v:null;
let changed=0;
for(const [ticker,dates] of Object.entries(cierres)){
  const model=data.files[`empresas/${ticker}.json`];if(!model)throw Error('Falta '+ticker);
  const periods=model.financialPresentation?.periods||[];
  const pendiente=Object.keys(dates).filter(year=>periods.some(p=>p.year===Number(year)&&!/^LTM/i.test(p.periodo||'')&&asNum(p.values?.stockPrice)===null));
  if(!pendiente.length)continue;
  const start=Math.min(...Object.values(dates).map(d=>Date.parse(d)/1000));
  const end=Math.floor(Date.now()/1000)+86400;
  const url=`https://query1.finance.yahoo.com/v8/finance/chart/${ticker}?period1=${Math.floor(start)-864000}&period2=${end}&interval=1d&events=splits`;
  const r=await fetch(url,{headers:{'User-Agent':'Mozilla/5.0 (JMR V2 research)'},signal:AbortSignal.timeout(25000)});
  if(!r.ok)throw Error('Yahoo '+ticker+' HTTP '+r.status);
  const j=await r.json(),q=j.chart?.result?.[0];
  if(!q||j.chart?.error)throw Error('Yahoo sin resultados '+ticker);
  const times=q.timestamp||[],closes=q.indicators?.quote?.[0]?.close||[];
  const quote=times.map((x,i)=>({date:new Date(x*1000).toISOString().slice(0,10),px:asNum(closes[i])})).filter(x=>x.px!==null);
  for(const year of pendiente){
    const cierre=dates[year];
    const x=quote.filter(x=>x.date<=cierre && (Date.parse(cierre)-Date.parse(x.date))/86400000<=5).at(-1);
    if(!x){console.log('SIN_PRECIO',ticker,year,cierre);continue}
    const p=periods.find(p=>p.year===Number(year)&&!/^LTM/i.test(p.periodo||''));
    const val=Math.round(x.px*1e6)/1e6;
    // AAPL precisa una base de acciones compatible con la serie de Yahoo
    // (ajustada por splits posteriores, no por dividendos).
    if(ticker==='AAPL' && Number(year)<=2019){
      const obs=(p.values?.sharesOutstanding??model.history?.find(h=>h.year===Number(year))?.sharesOutstanding);
      if(year==='2017'&&asNum(obs)!==null&&Math.abs(obs-20504.804)>2)throw Error('Base acciones AAPL 2017 cambió: reconciliar split');
      if(year==='2019'&&asNum(obs)!==null&&Math.abs(obs-17772.945)>2)throw Error('Base acciones AAPL 2019 cambió: reconciliar split');
    }
    p.values??={};p.sources??={};
    p.values.stockPrice=val;
    p.sources.stockPrice={proveedor:'Yahoo Finance chart',fechaCierre:cierre,fechaCotizacion:x.date,metodo:'último cierre <= cierre fiscal (5 días)',baseSplits:ticker==='AAPL'?'precio ajustado por splits a la base de acciones reexpresadas del libro':'precio de cierre sin ajuste por dividendos; sin splits posteriores en período',url:`https://finance.yahoo.com/quote/${ticker}/history/`};
    changed++;
    console.log('PRECIO_VERIFICADO',ticker,year,cierre,x.date,val);
  }
}
if(!changed)throw Error('No hubo precios nuevos: revisar si la biblioteca ya estaba actualizada');
console.log('RESUMEN_PRECIO_V2',changed,'celdas nuevas; DCF, acciones e históricos económicos inalterados');
if(process.argv.includes('--aplicar')){
  const serialized=JSON.stringify(data,null,1)+'\n',sha=createHash('sha256').update(serialized).digest('hex');
  const archive=`biblioteca-${sha}.json.gz`;
  fs.writeFileSync(path.join(raiz,archive),gzipSync(serialized));
  fs.writeFileSync(manPath,JSON.stringify({schemaVersion:'jmr-biblioteca-gzip-1',app:'jmr-v2',archive,sha256:sha},null,1)+'\n');
  console.log('CANDIDATO_V2',archive,sha);
}
