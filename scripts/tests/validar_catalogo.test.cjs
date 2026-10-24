'use strict';
const test=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),os=require('node:os'),path=require('node:path');
const {validate}=require('../validar_catalogo.cjs');const root=path.join(__dirname,'../..');
function fixture(t,mutate){const tmp=fs.mkdtempSync(path.join(os.tmpdir(),'jmr-catalog-'));t.after(()=>fs.rmSync(tmp,{recursive:true,force:true}));for(const p of ['catalogo.json','valoraciones','analisis','auditorias','scripts'])fs.cpSync(path.join(root,p),path.join(tmp,p),{recursive:true});mutate(tmp);return tmp;}
test('META, NKE y NFLX publicadas conservan vínculos, 18 secciones y auditoría narrativa vigente',()=>assert.deepEqual(validate(),{valoraciones:3,analisis:3,auditorias:3}));
test('rechaza análisis enlazado a otra valoración',t=>{const tmp=fixture(t,dir=>{const c=require(path.join(dir,'catalogo.json'));const p=path.join(dir,c.analisis[0]);const a=JSON.parse(fs.readFileSync(p));a.linkedValuation.sourcePath='valoraciones/OTRA.json';fs.writeFileSync(p,JSON.stringify(a));});assert.throws(()=>validate(tmp),/Análisis sin valoración/);});
test('rechaza MOS que no deriva del DCF principal',t=>{const tmp=fixture(t,dir=>{const c=require(path.join(dir,'catalogo.json'));const p=path.join(dir,c.valoraciones[0]);const v=JSON.parse(fs.readFileSync(p));v.precioMOS=0;fs.writeFileSync(p,JSON.stringify(v));});assert.throws(()=>validate(tmp),/MOS diferente/);});

test('archivo histórico preservado y excluido del catálogo público', () => {
  assert.ok(fs.existsSync(path.join(root,'auditorias/archivo/NFLX-auditoria-2026-10-22.md')));
  assert.ok(!require(path.join(root,'catalogo.json')).auditorias.some(p => p.includes('/archivo/')));
  assert.deepEqual(validate(), {valoraciones:3, analisis:3, auditorias:3});
});
test('rechaza revisión financiera editorial discordante', t => {
  const tmp=fixture(t,dir=>{
    const c=require(path.join(dir,'catalogo.json'));
    const p=path.join(dir,c.analisis.find(x=>x.includes('/NFLX-')));
    const a=JSON.parse(fs.readFileSync(p));
    a.revisionId='NFLX-OTRA-REVISION';
    fs.writeFileSync(p,JSON.stringify(a));
  });
  assert.throws(()=>validate(tmp),/Revisión financiera distinta/);
});
