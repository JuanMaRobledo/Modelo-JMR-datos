#!/usr/bin/env node
// Corrección puntual y auditada: AAPL FY2018 acciones al cierre en millones,
// base de acciones compatible con las cotizaciones históricas ajustadas por splits.
import fs from 'node:fs';
import path from 'node:path';
import {gunzipSync,gzipSync} from 'node:zlib';
import {createHash} from 'node:crypto';
const dir=path.resolve('jmr-v2'),mp=path.join(dir,'biblioteca.json');
const m=JSON.parse(fs.readFileSync(mp,'utf8'));
if(m.schemaVersion!=='jmr-biblioteca-gzip-1'||m.archive!==`biblioteca-${m.sha256}.json.gz`)throw Error('Manifest inesperado');
const original=gunzipSync(fs.readFileSync(path.join(dir,m.archive)));
if(createHash('sha256').update(original).digest('hex')!==m.sha256)throw Error('SHA original inválido');
const biblioteca=JSON.parse(original),a=biblioteca.files['empresas/AAPL.json'];
const periods=a?.financialPresentation?.periods||[];
const fy=y=>periods.find(p=>p.year===y&&!/^LTM/i.test(p.periodo||''));
const s2017=fy(2017)?.values?.sharesOutstanding??a.history?.find(h=>h.year===2017)?.sharesOutstanding;
const s2019=fy(2019)?.values?.sharesOutstanding??a.history?.find(h=>h.year===2019)?.sharesOutstanding;
if(Math.abs(s2017-20504.804)>1||Math.abs(s2019-17772.945)>1)throw Error('La base split-adjusted de AAPL cambió; revisar fuente');
const p=fy(2018);if(!p)throw Error('No hay FY2018');
if(typeof p.values?.sharesOutstanding==='number'){console.log('YA_EXISTE_ACCIONES_FY2018',p.values.sharesOutstanding);process.exit(0);}
const reportado=4754.986; // millones antes de split. 10-K FY2019 SEC, columna comparativa FY2018.
const reexpresado=reportado*4; // Split 4:1 de AAPL efectivo en agosto 2020.
p.values??={};p.sources??={};
p.values.sharesOutstanding=reexpresado;
p.sources.sharesOutstanding={
 fuente:'Apple Inc 2019 Form 10-K (comparativa FY2018)',concepto:'Common stock issued and outstanding',
 fechaCierre:'2018-09-29',millonesOriginales:reportado,factorSplitPosterior:4,
 millonesBaseLibro:reexpresado,
 url:'https://www.sec.gov/Archives/edgar/data/320193/000032019319000119/R4.htm'
};
console.log('ACCIONES_FY2018_VERIFICADAS',reportado,'M origen *4 =',reexpresado,'M base libro',
            'precio',p.values.stockPrice,'capitalización estimada',reexpresado*p.values.stockPrice);
if(process.argv.includes('--aplicar')){
 const content=JSON.stringify(biblioteca,null,1)+'\n',sha=createHash('sha256').update(content).digest('hex'),archive=`biblioteca-${sha}.json.gz`;
 fs.writeFileSync(path.join(dir,archive),gzipSync(content));
 fs.writeFileSync(mp,JSON.stringify({schemaVersion:'jmr-biblioteca-gzip-1',app:'jmr-v2',archive,sha256:sha},null,1)+'\n');
 console.log('CANDIDATO_SHA',sha);
}
