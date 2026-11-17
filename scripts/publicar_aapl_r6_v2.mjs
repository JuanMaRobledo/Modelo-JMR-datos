#!/usr/bin/env node
// Publica exclusivamente AAPL R6 en biblioteca JMR V2, desde valores del libro Google Sheets comprobados.
// Nunca altera Floyd ni otras empresas. Revisión visible, no certificada ni aprobada.
import fs from 'node:fs';
import {gunzipSync,gzipSync} from 'node:zlib';
import {createHash} from 'node:crypto';
import assert from 'node:assert/strict';
const dir='jmr-v2',p=dir+'/biblioteca.json';
const man=JSON.parse(fs.readFileSync(p,'utf8'));
assert.equal(man.schemaVersion,'jmr-biblioteca-gzip-1');
assert.equal(man.app,'jmr-v2');
assert.equal(man.archive,`biblioteca-${man.sha256}.json.gz`);
const old=gunzipSync(fs.readFileSync(dir+'/'+man.archive));
assert.equal(createHash('sha256').update(old).digest('hex'),man.sha256);
const b=JSON.parse(old.toString('utf8'));
assert.equal(b.schemaVersion,'jmr-biblioteca-1');
const m=b.files['empresas/AAPL.json'],an=b.files['analisis/AAPL.json'],cat=b.files['catalogo.json'];
assert.ok(m&&an&&cat);
assert.equal(m.ticker,'AAPL');
assert.equal(m.revision?.id,'AAPL-V2-FY2026-R5','Revisión inesperada: no sobreescribir otra publicación');
assert.equal(m.financials.sharePrice,356.27,'Precio R5 cambió, revisar');
assert.equal(an.revision,'AAPL-V2-FY2026-R5');
const antes=new Map(Object.entries(b.files).filter(([key])=>!['empresas/AAPL.json','analisis/AAPL.json','catalogo.json'].includes(key)).map(([k,v])=>[k,JSON.stringify(v)]));
const R5=m.revision.id,R6='AAPL-V2-FY2026-R6';
const sheet='https://docs.google.com/spreadsheets/d/13K2SzF8cmD5mbR3Ke4J_6zkSy3pHLAlDX9scoJy1XlI/edit';
const excel='https://docs.google.com/spreadsheets/d/1D2Ia1EBgoo2hZ1T3KcVDDU5ZR1_dJGMm/edit';
const revision='https://docs.google.com/document/d/1mNjdVeLfOZQHRLhM2kXqkgnCKt6mHKTnHZFTDKo0Bhc/edit';
const prices={conservador:105.43074076749818,base:196.91400562592787,optimista:244.28125842167222};
const pct=(prices.base/352.78-1);
assert.ok(Math.abs(prices.base*0.65-127.99410365685313)<1e-8);
assert.equal(m.libro?.valores?.base>196&&m.libro?.valores?.base<197,true);
const sha='dcfbf2a5ecc9e039abda6c2618e029af8f0db19f2b094e148e40f65a80b45d80';
const prev={...m.libro.valores};
m.revision.historial??={};m.revision.historial[R5]=prev;
m.revision.id=R6;m.revision.anterior=R5;
m.revision.notaPresentacion='R6 publicada SOLO para revisión: precio 16-nov-2026; I+D amortizada a cinco años; EV de mercado resta caja/inversiones no corrientes como el DCF; EV/FCFF N/D. Auditoría económica del ROIC terminal, WACC, leases, RSU y costo de deuda pendientes.';
m.asOf='2026-11-16';m.priceAsOf='2026-11-16';
m.financials.sharePrice=352.78;
for(const name of ['conservador','base','optimista'])m.assumptions[name].waccInitial=0.10536404551190949;
m.libro.id=R6;m.libro.sha256=sha;m.libro.valores={...prices};
m.libro.url=sheet;m.libro.contratoVersion='1.4.2';
m.libro.costoCapital={...m.libro.costoCapital,formulas:true,waccInicial:0.10536404551190949,waccTerminal:0.08537};
m.libro.googleSheets={...m.libro.googleSheets,id:'13K2SzF8cmD5mbR3Ke4J_6zkSy3pHLAlDX9scoJy1XlI',url:sheet,mimeType:'application/vnd.google-apps.spreadsheet',carpeta:'1LGRFlLytjh4S6W8cbqkTaAF9D_4s4VR_',fecha:'2026-11-16',conversionVerificada:true,paridadConExcel:'Tres escenarios y centros de cuatro rejillas coinciden al valor Base en Google Sheets R6; control de diferencias simultáneo−guardado: cero.'};
m.libro.excel={id:'AAPL-V2-FY2026-R6_VALORACION.xlsx',url:excel,sha256:sha};
m.libro.formatoPrincipal='google_sheets';
m.libro.revisionR6={fecha:'2026-11-16',estado:'CANDIDATO_PUBLICADO_PARA_REVISION',contrato:'1.4.2',fuentePrimaria:'https://www.sec.gov/Archives/edgar/data/320193/000032019326000026/aapl-20260926.htm',informeEconomico:revision,precioMercado:352.78,efectivoMasInversiones:136935,deudaConLeasesReconocidos:94479,FCFFMultiplo:'N/D hasta conciliar',capitalizacionIDAnos:5,centrosSensibilidadConcilian:true,aprobacionPersonal:false,pendientes:['ROIC terminal 44,76%','WACC específico de empresa','Tratamiento leases en EBIT y EV','Dilución de RSU/SBC y número de acciones','Datos de gasto de intereses FY estimados','FCFF histórico para múltiplo EV/FCFF']};
m.libro.escenariosPresentacion??={};m.libro.escenariosPresentacion.valores={
 conservador:{...m.libro.escenariosPresentacion.valores?.conservador,valor:prices.conservador},
 base:{...m.libro.escenariosPresentacion.valores?.base,valor:prices.base},
 optimista:{...m.libro.escenariosPresentacion.valores?.optimista,valor:prices.optimista}
};
// Mantener EN_PROCESO hasta el cierre de la auditoría, pero visible en el visor de pendientes.
m.estado='EN_PROCESO';m.auditoriaUsuario=null;
const avisos=[
'R6 PARA REVISIÓN: valores provisionales, no certificados; ROIC terminal del 44,76% y WACC estable requieren auditoría económica independiente.',
'R6: capitalización de I+D a cinco años (activo 109.443,2 M USD; EBIT ajustado 175.028 M); la variación de vida útil no obligó a cambiar automáticamente los supuestos de margen futuro.',
'R6: EV de mercado usa 136.935 M USD en caja e inversiones negociables, corrientes y no corrientes; la pestaña Datos generales evita doble conteo; EV/FCFF N/D.',
'R6: 14.590,6 M acciones DCF versus 14.532,259 M FY en circulación; no intercambiar sin conciliar; SBC, arrendamientos y gasto de intereses estimado requieren revisión.',
'R6: el valor Base proviene del libro V2 y no implica aprobación personal. Revisión económica: '+revision
];
m.warnings=Array.isArray(m.warnings)?[...m.warnings.filter(x=>typeof x==='string'&&!x.startsWith('R6:')), ...avisos]:avisos;
m.documentLinks??=[];if(Array.isArray(m.documentLinks)){m.documentLinks=m.documentLinks.filter(x=>!String(x).includes('AAPL-V2-FY2026-R6'));m.documentLinks.push(sheet,excel,revision)}
m.historialAmpliaciones??=[];if(Array.isArray(m.historialAmpliaciones))m.historialAmpliaciones.push({revision:R6,fecha:'2026-11-16',tipo:'revisión económica preliminar',detalles:'Precio 352,78; I+D 5 años; EV coherente con caja total; controles sensibles de ROIC/WACC abiertos; sin aprobación.',libro:sheet,informe:revision});
if(m.analysis&&typeof m.analysis==='object'){
 const msg='Publicación provisional R6 (16-nov-2026): US$105,43 / US$196,91 / US$244,28; precio US$352,78; MOS35% US$127,99. El WACC y el ROIC terminal de 44,76%, el tratamiento de arrendamientos y la dilución siguen pendientes de auditoría. Informe: '+revision;
 m.analysis.risks=(m.analysis.risks||'')+'\n'+msg;
 m.analysis.conclusion=(m.analysis.conclusion||'')+'\n'+msg;
}
const actualiza=s=>typeof s!=='string'?s:s
 .replaceAll('AAPL-V2-FY2026-R5',R6)
 .replaceAll('US$356,27','US$352,78').replaceAll('US$342,37','US$352,78')
 .replaceAll('US$196,90','US$196,91').replaceAll('US$244,27','US$244,28')
 .replaceAll('US$260,45','US$244,28')
 .replaceAll('https://docs.google.com/spreadsheets/d/1TZksWBh9S-ZLhrz4eKuXXEUoYC6oIx2RxcNvynQ3C9Q/edit?usp=drivesdk#gid=2000000000',sheet)
 .replaceAll('https://docs.google.com/spreadsheets/d/1TZksWBh9S-ZLhrz4eKuXXEUoYC6oIx2RxcNvynQ3C9Q/edit',sheet)
 .replaceAll('Apple no publica el margen por línea de producto','Apple sí publica el margen bruto agregado de Productos y Servicios, pero no su EBIT segmentado')
 .replaceAll('Apple no publica el margen por línea de producto, de modo que','Apple publica el margen bruto de Productos (39,3 %) y Servicios (76,2 %), pero no el EBIT por categoría, de modo que');
an.revision=R6;an.status='BORRADOR_EDITORIAL_NO_AUDITADO';an.source={type:'Libro JMR V2 R6 publicado solo para revisión. 10-K y notas; números provisionales, sin auditoría independiente ni aprobación del usuario.',url:sheet,revisionEconomica:revision};
for(const [k,v] of Object.entries(an.blocks||{}))if(typeof v==='string')an.blocks[k]=actualiza(v);
const addendum='<p><strong>AAPL R6 · PUBLICADA PARA REVISIÓN (no auditada).</strong> Corte 16-nov-2026; referencia de mercado US$352,78. DCF: Conservador US$105,43, Base US$196,91, Optimista US$244,28; MOS35% US$127,99. Caja/inversiones usadas en EV: US$136.935 millones; EV/FCFF no disponible sin FCFF desapalancado conciliado. La capitalización de I+D usa cinco años. Riesgo principal: ROIC terminal 44,76% en Base/Optimista, sensible a la perpetuidad; WACC, leases, SBC y número de acciones aún por auditar. <a href="'+revision+'">Informe económico R6</a> · <a href="'+sheet+'">Libro R6</a>. Esta publicación NO implica aprobación económica.</p>';
an.blocks.tesis=addendum+(an.blocks.tesis||'');
an.blocks.valoracion=addendum+(an.blocks.valoracion||'');
an.conciliacionEditorial={...(an.conciliacionEditorial||{}),revision:R6,fuenteLibro:sheet,verificacion:'Tres escenarios y cuatro centros de sensibilidad conciliados en Google Sheets R6; pendiente auditoría de los supuestos económicos; no se extrapolan precios.',estado:'PARA_REVISION'};
const c=cat.empresas.find(x=>x.ticker==='AAPL');assert.ok(c);
c.asOf='2026-11-16';c.precio=352.78;c.valorBase=prices.base;c.precioMOS=prices.base*0.65;c.estado='EN_PROCESO';c.estadoDeclarado='EN_PROCESO';c.visibilidadApp='PUBLICADA_PARA_REVISION';c.visorAuditoria='pendientes';c.aprobacionUsuario=null;
assert.equal(cat.empresas.length,11,'La colección completa debe conservarse');
assert.ok(cat.empresas.every(x=>x.ticker!=='AAPL'||Math.abs(x.valorBase-prices.base)<1e-8));
assert.ok(Object.entries(b.files).filter(([key])=>antes.has(key)).every(([k,v])=>JSON.stringify(v)===antes.get(k)),'Otra empresa fue modificada');
assert.equal(m.libro.valores.base,prices.base);assert.equal(m.libro.sha256,sha);
console.log('AAPL_R6_APROBACION_PERSONAL',m.auditoriaUsuario);
console.log('AAPL_R6',R6,'precio',c.precio,'valores',JSON.stringify(prices),'brecha',pct,'visibilidad',c.visibilidadApp,'visor',c.visorAuditoria,'hojas',sheet);
console.log('OTRAS_EMPRESAS_INTACTAS',antes.size,'ARCHIVOS',Object.keys(b.files).length);
if(process.argv.includes('--aplicar')){
 const texto=JSON.stringify(b,null,1)+'\n',sha256=createHash('sha256').update(texto).digest('hex'),archive=`biblioteca-${sha256}.json.gz`;
 fs.writeFileSync(dir+'/'+archive,gzipSync(texto));
 fs.writeFileSync(p,JSON.stringify({schemaVersion:'jmr-biblioteca-gzip-1',app:'jmr-v2',archive,sha256},null,1)+'\n');
 console.log('CANDIDATO_PUBLICACION_R6',archive,'SHA256',sha256);
}
