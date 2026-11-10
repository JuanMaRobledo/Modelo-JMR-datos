'use strict';
const test=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
const root=path.resolve(__dirname,'../..');
const read=p=>JSON.parse(fs.readFileSync(path.join(root,p)));
test('UBER: captura nativa, ficha y análisis concilian presente, MOS, pesos y cinco VP3',()=>{
 const v=read('valoraciones/UBER-20261030-A1.json'),a=read('analisis/UBER-research-UBER-20261030-A1.json');
 const e=v.conciliacionHoja,raw=fs.readFileSync(path.join(root,e.sourcePath));
 assert.equal(crypto.createHash('sha256').update(raw).digest('hex'),e.sha256);
 const cap=JSON.parse(raw).capture;
 const cell=(title,row,col)=>{const sh=cap.sheets.find(s=>s.properties.title===title);for(const d of sh.data||[]){const r=d.rowData?.[row-1-(d.startRow||0)];const c=r?.values?.[col-1-(d.startColumn||0)];if(c?.effectiveValue)return c.effectiveValue.numberValue??c.effectiveValue.stringValue;}throw Error(`${title}!${row},${col} ausente`);};
 const near=(x,y)=>assert.ok(Math.abs(x-y)<1e-8,`${x} != ${y}`);
 near(cell('Resumen de Valoración',22,2),v.valorPrincipal);
 near(cell('Resumen de Valoración',19,2),v.precioMOS);
 near(cell('Valuation output',35,2),v.valorPrincipal);
 near(cell('Resumen de Valoración',6,2),1);
 for(let r=7;r<=11;r++)near(cell('Resumen de Valoración',r,2),0);
 for(const [i,m] of v.sensibilidadMultiples.matrices.entries()){
  near(cell('Sensibilidad por múltiplo',81+10*i,4),m.centro);
  near(cell('Descuento de múltiplos',20+i,10),m.centro);
  assert.equal(m.peso,0);assert.equal(m.anclaCertificada,false);
 }
 assert.equal(a.revisionId,v.revisionId);assert.equal(a.sheet_id,v.sheet_id);
 assert.deepEqual(a.linkedValuation.descuentoMultiples,v.descuentoMultiples);
 assert.equal(v.estado,'EN_REVISION');assert.equal(v.auditoriaEconomica,'NO_REALIZADA');
 assert.equal(v.sensibilidadMultiples.certificado,false);
 assert.ok(!/Cinco múltiplos aún N\/D|Gate global en repo datos continúa bloqueado/.test(a.html));
});
