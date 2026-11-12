'use strict';
const test=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const root=path.join(__dirname,'../..');
const NAMES=['EV/EBITDA','EV/FCFF','P/E','P/FCFE','P/OCF','P/V','P/BV'];
const EXPECT_OK={SHAK:5,UBER:0,MELI:5,CELH:7,ADBE:7,BSX:7,CMG:6,NFLX:7,GOOGL:3,
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
  const previous=18+['META','NVDA','XP','INTU','DPZ','NU'].filter(t=>active.some(([name])=>name===t)).length;
  const amzn=active.find(([ticker])=>ticker==='AMZN');
  const pags=active.find(([ticker])=>ticker==='PAGS');
  // AAPL R1 se admite únicamente si el alta es la revisión oficial A-1.2,
  // no una captura de rango ni un registro alternativo sin contrato.
  const aapl=active.find(([ticker])=>ticker==='AAPL');
  const lulu=active.find(([ticker])=>ticker==='LULU');
  const ko=active.find(([ticker])=>ticker==='KO');
  const floyd=Object.entries(catalog.controlModeloA.empresas)
    .filter(([,v])=>v.metodo==='Floyd' && v.rutaValoracion && JSON.parse(fs.readFileSync(path.join(root,v.rutaValoracion),'utf8')).contratoLibros==='floyd-h1-h2-separados-v1'); // Floyd F1–F5, no Floyd R1–R6
  const FLOYD_RUTAS={UBER:'valoraciones/UBER-FLOYD-3T26.json',CMG:'valoraciones/CMG-FLOYD-20261108-R1.json'};
  assert.ok(floyd.length<=Object.keys(FLOYD_RUTAS).length,'Floyd se integra de forma explícita, no como captura parcial');
  // Sólo las selecciones A-1.2 archivadas que no fueron reemplazadas por Floyd R1–R6.
  // La identidad se valida contra el registro del archivo, no contra un contador obsoleto.
  const expectedLegacy=Object.entries(catalog.archivoFloyd.controlModeloA)
    .filter(([ticker,v])=>v.metodo==='A-1.2' && catalog.controlModeloA.empresas[ticker]?.metodo==='A-1.2').length;
  assert.equal(active.length,expectedLegacy,
    'No permitir altas desconocidas sin catálogo reconciliado');
  for(const [ticker,entry] of floyd){
    assert.ok(FLOYD_RUTAS[ticker],'El expediente Floyd debe estar identificado: '+ticker);
    assert.equal(entry.rutaValoracion,FLOYD_RUTAS[ticker]);
    assert.ok(catalog.valoraciones.includes(entry.rutaValoracion));
    const val=JSON.parse(fs.readFileSync(path.join(root,entry.rutaValoracion),'utf8'));
    assert.equal(val.perfil_valoracion,'Floyd');
    assert.equal(val.sensibilidadMultiples.matrices.length,5);
    assert.equal(val.sensibilidadDCF.matrices.length,3);
    assert.ok(val.sensibilidadMultiples.matrices.every(m=>m.estado==='OK'&&near(m.matriz[2][2],m.centro)));
  }
  if(pags)assert.equal(pags[1].rutaValoracion,'valoraciones/PAGS-20261030-A12-R1.json','PAGS exige revision A-1.2 vigente unica');
  if(amzn)assert.equal(amzn[1].rutaValoracion,'valoraciones/AMZN-20261102-A12-R5.json','AMZN exige revisión R5 activa única');
  if(aapl){
    const rel='valoraciones/AAPL-20261103-A12-R1.json';
    assert.equal(aapl[1].rutaValoracion,rel,'AAPL exige revisión A-1.2 R1 única');
    assert.ok(catalog.valoraciones.includes(rel),'AAPL sin valoración oficial en catálogo');
    assert.ok(catalog.analisis.includes('analisis/AAPL-research-AAPL-20261103-A12-R1.json'),
      'AAPL sin análisis oficial vinculado');
    const ficha=JSON.parse(fs.readFileSync(path.join(root,rel),'utf8'));
    assert.equal(ficha.revisionId,'AAPL-20261103-A12-R1');
    assert.equal(ficha.sensibilidadMultiples?.sourceSheetId,ficha.sheet_id);
    assert.equal(ficha.sensibilidadMultiples?.matrices?.filter(m=>m.prioritario&&m.estado==='OK').length,5,
      'AAPL debe tener cinco matrices Base completas, no capturas parciales');
  }
  if(lulu){
    // Alta expresamente autorizada por el usuario; no habilita capturas parciales.
    const rel='valoraciones/LULU-20261103-A12-R1.json',ana='analisis/LULU-research-LULU-20261103-A12-R1.json';
    assert.equal(lulu[1].rutaValoracion,rel,'LULU solo admite la revisión A-1.2 R1 publicada');
    assert.ok(catalog.valoraciones.includes(rel)&&catalog.analisis.includes(ana),
      'LULU necesita valoración y análisis oficiales enlazados');
    const ficha=JSON.parse(fs.readFileSync(path.join(root,rel),'utf8'));
    const nivel1=JSON.parse(fs.readFileSync(path.join(root,ana),'utf8'));
    assert.equal(ficha.revisionId,'LULU-20261103-A12-R1');
    assert.equal(ficha.sheet_id,'1XY_iXmarfM0ESnzu3RMV5E4TkgrJAy9-XzJ2PxndHz4');
    assert.equal(ficha.sensibilidadMultiples?.sourceSheetId,ficha.sheet_id);
    assert.equal(ficha.sensibilidadMultiples?.contrato,'base-native-five-priority-v1');
    assert.equal(ficha.sensibilidadMultiples?.matrices?.filter(m=>m.prioritario&&m.estado==='OK').length,5,
      'LULU debe tener cinco matrices Base5x5, no capturas de rango');
    assert.equal(nivel1.revisionId,ficha.revisionId,'LULU vinculó análisis de revisión distinta');
  }
  if(ko){
    // KO es alta oficial R1 con N1+N2 y captura numérica integral,
    // no una de las 19 capturas parciales históricas.
    const rel='valoraciones/KO-20261103-A12-R1.json',ana='analisis/KO-research-KO-20261103-A12-R1.json';
    assert.equal(ko[1].rutaValoracion,rel,'KO exige revision A-1.2 R1 unica');
    assert.ok(catalog.valoraciones.includes(rel)&&catalog.analisis.includes(ana),
      'KO requiere valoración y análisis oficiales enlazados');
    const ficha=JSON.parse(fs.readFileSync(path.join(root,rel),'utf8'));
    const nivel1=JSON.parse(fs.readFileSync(path.join(root,ana),'utf8'));
    assert.equal(ficha.revisionId,'KO-20261103-A12-R1');
    assert.equal(nivel1.revisionId,ficha.revisionId,'KO análisis/valoración mezclados');
    assert.equal(ficha.sensibilidadMultiples.sourceSheetId,ficha.sheet_id);
    assert.equal(ficha.sensibilidadMultiples.contrato,'base-native-five-priority-v1');
    assert.equal(ficha.sensibilidadMultiples.matrices.filter(m=>m.prioritario&&m.estado==='OK').length,5);
    assert.equal(nivel1.controlCobertura.secciones,14);
    assert.equal(nivel1.controlCobertura.nivel2Apartados,12);
    const capture=JSON.parse(fs.readFileSync(path.join(root,
      'candidatos/valoraciones/KO-20261103-A12-R1/CAPTURA_NATIVA_KO.json'),'utf8'));
    const digest=require('node:crypto').createHash('sha256').update(capture.canonicalPayload,'utf8').digest('hex');
    assert.equal(capture.sha256,digest,'KO captura fuente no coincide con SHA256 real');
    assert.equal(ficha.sensibilidadMultiples.resultadosSha256,digest);
  }
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
    // Las capturas parciales históricas siguen ligadas a su revisión de origen,
    // nunca a la revisión activa posterior ni se reescriben para forzar conciliación.
    const historicalSources={
      INTU:'candidatos/valoraciones/INTU-20261029-R1/VALORACION_A12_EN_REVISION.json',
      UBER:'valoraciones/UBER-20261030-A1.json',
      CMG:'valoraciones/CMG-20261028-A3.json',
      DUOL:'valoraciones/DUOL-20261029-A1.json',
      MELI:catalog.archivoFloyd.controlModeloA.MELI.rutaValoracion,
      MSFT:catalog.archivoFloyd.controlModeloA.MSFT.rutaValoracion,
    };
    const declared=historicalSources[ticker]
      ?{rutaValoracion:historicalSources[ticker]}
      :catalog.controlModeloA.empresas[ticker];
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
