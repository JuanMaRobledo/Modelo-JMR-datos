'use strict';
const test=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const root=path.join(__dirname,'../..');
const NAMES=['EV/EBITDA','EV/FCFF','P/E','P/FCFE','P/OCF','P/V','P/BV'];
const expected={SHAK:{revision:'SHAK-20261029-A12-R2',ok:5,nd:2},AFYA:{revision:'AFYA-20261029-R1',ok:7,nd:0}};
const near=(a,b)=>typeof a==='number'&&Number.isFinite(a)&&typeof b==='number'&&Number.isFinite(b)&&Math.abs(a-b)<=Math.max(1e-6,Math.abs(b)*1e-8);
for(const [ticker,expect] of Object.entries(expected)){
  test(ticker+': captura parcial conserva celdas nativas sin convertirse en publicación',()=>{
    const file=path.join(root,'candidatos/hoja-multiples',expect.revision+'-captura-rango.json');
    const candidate=JSON.parse(fs.readFileSync(file,'utf8'));
    const valuation=JSON.parse(fs.readFileSync(path.join(root,'valoraciones',expect.revision+'.json'),'utf8'));
    assert.equal(candidate.tipo,'CAPTURA_ACOTADA_NO_PUBLICADA');
    assert.equal(candidate.contrato,'sensibilidad-nativa-base-parcial-v1');
    assert.equal(candidate.hashFotografiaCompleta,null,'rango no acredita foto de 46 pestañas');
    assert.equal(candidate.sourceSheetId,valuation.sheet_id);
    assert.equal(candidate.revisionId,valuation.revisionId);
    assert.equal(candidate.ticker,valuation.ticker);
    assert.equal(valuation.estado,'EN_REVISION');
    assert.equal(candidate.historia,'Base');
    assert.equal(candidate.ancla,'JMR');
    assert.equal(candidate.metodos.length,7);
    assert.deepEqual(candidate.metodos.map(m=>m.metodo),NAMES);
    assert.equal(candidate.metodos.filter(m=>m.estadoHoja==='OK').length,expect.ok);
    assert.equal(candidate.metodos.filter(m=>m.estadoHoja==='N/D').length,expect.nd);
    for(const m of candidate.metodos){
      const calc=valuation.descuentoMultiples?.metodos?.find(x=>x.nombre===m.metodo);
      const vp3=calc?.base?.vp?.[2];
      if(typeof vp3==='number')assert.ok(near(m.vp3Original,vp3),m.metodo+': VP3 diferente');
      if(m.estadoHoja==='OK'){
        assert.ok(Array.isArray(m.matriz)&&m.matriz.length===5&&
          m.matriz.every(row=>Array.isArray(row)&&row.length===5&&row.every(Number.isFinite)));
        assert.equal(m.ejeHorizontalFY3.length,5);
        assert.equal(m.ejeVerticalMultiplo.length,5);
        assert.ok(near(m.matriz[2][2],m.centro)&&near(m.centro,m.vp3Original));
      }else{
        assert.equal(m.estadoHoja,'N/D');
        assert.equal(m.matriz,null,'N/D no debe convertirse en cero');
        assert.equal(m.centro,null);
      }
    }
  });
}
