'use strict';
const test=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),os=require('node:os'),path=require('node:path');
const {validate}=require('../validar_catalogo.cjs');const root=path.join(__dirname,'../..');
function fixture(t,mutate){const tmp=fs.mkdtempSync(path.join(os.tmpdir(),'jmr-catalog-'));t.after(()=>fs.rmSync(tmp,{recursive:true,force:true}));for(const p of ['catalogo.json','valoraciones','analisis','auditorias','scripts'])fs.cpSync(path.join(root,p),path.join(tmp,p),{recursive:true});mutate(tmp);return tmp;}
test('catálogo vigente conserva vínculos únicos y auditorías disponibles sin certificar pendientes',()=>{
 const c=require(path.join(root,'catalogo.json'));
 // Prueba estructural independiente: el gate financiero exhaustivo se ejecuta al final del CI.
 assert.ok(c.valoraciones.every(p=>fs.existsSync(path.join(root,p))),'Valoración inexistente');
 assert.ok(c.analisis.every(p=>fs.existsSync(path.join(root,p))),'Análisis inexistente');
 assert.ok(c.auditorias.every(p=>fs.existsSync(path.join(root,p))),'Auditoría inexistente');
 assert.equal(c.valoraciones.length,c.analisis.length);
 // La auditoría económica es posterior a EN_REVISION. No fabricar ocho
 // informes para igualar contadores; exigir estado pendiente explícito.
 const audited=new Set(c.auditorias.map(p=>path.basename(p,'.md')));
 assert.equal(audited.size,c.auditorias.length,'Auditoría duplicada');
 for(const p of c.valoraciones){
  const v=JSON.parse(fs.readFileSync(path.join(root,p)));
  if(!audited.has(v.ticker)){
   assert.equal(v.estado,'EN_REVISION',v.ticker+': sin auditoría no puede cerrarse');
   assert.equal(v.auditPendingUserVisualReview,true,v.ticker+': falta revisión visual pendiente');
   assert.match(v.auditoriaEconomica||'',/^(NO_REALIZADA|PENDIENTE_REVISION_VISUAL)/,
    v.ticker+': auditoría ausente no puede declararse realizada');
  }
 }
 const tickers=c.valoraciones.map(p=>JSON.parse(fs.readFileSync(path.join(root,p))).ticker);
 assert.equal(new Set(tickers).size,tickers.length,'Una revisión activa por ticker');
 for(const t of ['META','NFLX','NKE','NVDA'])assert.ok(tickers.includes(t),'Se perdió un estudio existente: '+t);
});
test('rechaza análisis enlazado a otra valoración',t=>{const tmp=fixture(t,dir=>{const c=require(path.join(dir,'catalogo.json'));const p=path.join(dir,c.analisis[0]);const a=JSON.parse(fs.readFileSync(p));a.linkedValuation.sourcePath='valoraciones/OTRA.json';fs.writeFileSync(p,JSON.stringify(a));});assert.throws(()=>validate(tmp),/valoración del catálogo ausente o ambigua/);});
test('rechaza MOS que no deriva del DCF principal',t=>{const tmp=fixture(t,dir=>{const c=require(path.join(dir,'catalogo.json'));const p=path.join(dir,c.valoraciones[0]);const v=JSON.parse(fs.readFileSync(p));v.precioMOS=0;fs.writeFileSync(p,JSON.stringify(v));});assert.throws(()=>validate(tmp),/DCF y MOS/);});

test('archivo histórico preservado y excluido del catálogo público', () => {
  assert.ok(fs.existsSync(path.join(root,'auditorias/archivo/NFLX-auditoria-2026-10-22.md')));
  assert.ok(!require(path.join(root,'catalogo.json')).auditorias.some(p => p.includes('/archivo/')));
  const c=require(path.join(root,'catalogo.json'));
  assert.ok(c.auditorias.every(p=>!p.includes('/archivo/')));
  assert.ok(c.valoraciones.every(p=>fs.existsSync(path.join(root,p))));
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

test('XP FCFE A-1.2 activo usa contraste historico R2 no certificado',()=>{
 const c=require(path.join(root,'catalogo.json'));
 const p=c.valoraciones.find(p=>p.startsWith('valoraciones/XP-'));
 const v=JSON.parse(fs.readFileSync(path.join(root,p)));
 const ap=c.analisis.find(p=>p.startsWith('analisis/XP-'));
 const a=JSON.parse(fs.readFileSync(path.join(root,ap)));
 assert.equal(v.revisionId,'XP-20261031-A12-R1');
 assert.equal(v.version_metodo,'A-1.2');
 assert.match(v.metodoPrincipal,/FCFE/);
 assert.equal(v.estado,'EN_REVISION');
 assert.equal(v.certificacionEconomica,'NO_CERTIFICADA');
 assert.equal(v.auditPendingUserVisualReview,true);
 assert.equal(v.sensibilidadMultiples.contrato,'review-relative-v1');
 assert.deepEqual(v.sensibilidadMultiples.matrices.map(m=>m.metodo),['P/E','P/FCFE','P/BV','P/S']);
 assert.ok(v.sensibilidadMultiples.matrices.every(m=>m.peso===0&&m.anclaCertificada===false));
 assert.ok(Math.abs(v.valorPrincipal-14.475590094736917)<1e-8);
 assert.ok(Math.abs(v.precioMOS-v.valorPrincipal*.65)<1e-8);
 assert.equal(a.linkedValuation.sourcePath,p);
 assert.ok(!c.auditorias.includes('auditorias/narrativas/XP.md'));
 assert.ok(fs.existsSync(path.join(root,'valoraciones/XP-20261026-R2.json')));
});
