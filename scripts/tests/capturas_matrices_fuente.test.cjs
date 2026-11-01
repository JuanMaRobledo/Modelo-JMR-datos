'use strict';
const test=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const root=path.join(__dirname,'../..');
const NAMES=['EV/EBITDA','EV/FCFF','P/E','P/FCFE','P/OCF','P/V','P/BV'];
const EXPECT_OK={SHAK:5,UBER:0,MELI:5,CELH:7,ADBE:7,BSX:7,CMG:7,NFLX:7,GOOGL:3,
  MSFT:7,NKE:7,PYPL:7,EPAM:7,ZTS:7,ONON:7,NVO:6,INTU:0,AFYA:7,DUOL:7};
const EXPECT_PRIORITY={SHAK:3,UBER:0,MELI:3,CELH:5,ADBE:5,BSX:5,CMG:5,NFLX:5,
  GOOGL:2,MSFT:5,NKE:5,PYPL:5,EPAM:5,ZTS:5,ONON:5,NVO:5,INTU:0,AFYA:5,DUOL:5};
const near=(a,b)=>typeof a==='number'&&Number.isFinite(a)&&typeof b==='number'&&Number.isFinite(b)&&
  Math.abs(a-b)<=Math.max(1e-6,Math.abs(b)*1e-8);
const catalog=JSON.parse(fs.readFileSync(path.join(root,'catalogo.json'),'utf8'));
const dir=path.join(root,'candidatos/hoja-multiples');
const files=fs.readdirSync(dir).filter(x=>x.endsWith('-captura-rango.json'));
const byTicker=new Map();

test('ninguna captura de solo rango contamina el catálogo de valoraciones',()=>{
  const active=Object.entries(catalog.controlModeloA.empresas)
    .filter(([,v])=>v.metodo==='A-1.2');
  assert.equal(active.length,18+['META','NVDA','XP','INTU'].filter(t=>active.some(([name])=>name===t)).length,'NU es CANDIDATO; INTU volvió con INTU-20261101-A12-R1');
  assert.equal(files.length,19,'NU se rige por contrato FCFE bancario separado');
  for(const f of files){
    const p='candidatos/hoja-multiples/'+f;
    assert.ok(!catalog.valoraciones.includes(p));
    assert.ok(!catalog.analisis.includes(p));
    assert.ok(!catalog.auditorias.includes(p));
  }
});
for(const file of files){
  const candidate=JSON.parse(fs.readFileSync(path.join(dir,file),'utf8'));
  test(candidate.ticker+': fotografía parcial nativa no publicada, centro conciliado',()=>{
    const ticker=candidate.ticker;
    assert.ok(Object.hasOwn(EXPECT_OK,ticker),'Empresa de captura desconocida');
    assert.notEqual(ticker,'NU','NU requiere contrato de múltiplos bancarios');
    assert.equal(byTicker.has(ticker),false,'Captura duplicada');
    byTicker.set(ticker,true);
    // La captura parcial de INTU pertenece a INTU-20261029-R1 (candidato conservado), no a la revisión activa nueva.
    const declared=ticker==='INTU'?{rutaValoracion:'candidatos/valoraciones/INTU-20261029-R1/VALORACION_A12_EN_REVISION.json'}:catalog.controlModeloA.empresas[ticker];
    const valuation=JSON.parse(fs.readFileSync(path.join(root,declared.rutaValoracion),'utf8'));
    assert.equal(candidate.tipo,'CAPTURA_ACOTADA_NO_PUBLICADA');
    assert.equal(candidate.contrato,'sensibilidad-nativa-base-parcial-v1');
    assert.equal(candidate.hashFotografiaCompleta,null,'el rango no es snapshot completo');
    assert.equal(candidate.sourceSheetId,valuation.sheet_id);
    assert.equal(candidate.revisionId,valuation.revisionId);
    assert.equal(candidate.ticker,valuation.ticker);
    assert.equal(valuation.estado,'EN_REVISION');
    assert.equal(candidate.historia,'Base');
    assert.equal(candidate.ancla,'JMR');
    assert.equal(candidate.metodos.length,7);
    assert.deepEqual(candidate.metodos.map(m=>m.metodo),NAMES);
    assert.equal(candidate.metodos.filter(m=>m.estadoHoja==='OK').length,EXPECT_OK[ticker]);
    assert.equal(candidate.metodos.filter(m=>m.estadoHoja==='OK'&&m.prioritario).length,EXPECT_PRIORITY[ticker]);
    for(const m of candidate.metodos){
      const calc=valuation.descuentoMultiples?.metodos?.find(x=>x.nombre===m.metodo);
      const vp3=calc?.base?.vp?.[2];
      if(valuation.sensibilidadMultiples?.contrato==='review-relative-v1'){
        // La captura antigua sigue intacta; la importación nueva se concilia con su fuente contemporánea.
        require('../validar_relativos_revision.cjs').validateReviewRelatives(valuation);
      }else if(typeof vp3==='number')assert.ok(near(m.vp3Original,vp3),
        ticker+'/'+m.metodo+': VP3 difiere de registro existente');
      assert.equal(m.origen.startsWith("'Sensibilidad por múltiplo'!A"),true);
      if(m.estadoHoja==='OK'){
        assert.ok(Array.isArray(m.matriz)&&m.matriz.length===5&&
          m.matriz.every(row=>Array.isArray(row)&&row.length===5&&row.every(Number.isFinite)));
        assert.equal(m.ejeHorizontalFY3.length,5);
        assert.equal(m.ejeVerticalMultiplo.length,5);
        assert.ok(m.ejeHorizontalFY3.every(Number.isFinite));
        assert.ok(m.ejeVerticalMultiplo.every(Number.isFinite));
        assert.ok(near(m.matriz[2][2],m.centro)&&near(m.centro,m.vp3Original));
      }else{
        assert.equal(m.estadoHoja,'N/D');
        assert.equal(m.matriz,null,'N/D no se sustituye con cero');
        assert.equal(m.centro,null);
      }
    }
  });
}
