'use strict';
const test=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const root=path.join(__dirname,'../..');
const read=p=>JSON.parse(fs.readFileSync(path.join(root,p),'utf8'));
const x=read('candidatos/valoraciones/XP-20261031-A12-R1/workspace.json');
const original=read(x.trabajo.valoracionAnterior),catalog=read('catalogo.json');
test('XP usa estructura A-1.2 sin cambiar valoración vigente',()=>{
assert.equal(x.schema,'jmr-valuation-workspace-v1');
assert.equal(x.versionMetodo,'A-1.2');
assert.equal(x.metodoPrincipal,'FCFE_FINANCIERO');
assert.equal(x.estado,'PREPARACION_SIN_VALORACION');
assert.equal(x.publicationStatus,'NO_PUBLICAR');
assert.equal(x.valorPrincipal,null);
assert.equal(x.precioMOS,null);
assert.equal(original.revisionId,'XP-JMR-20261026-R2');
assert.ok(catalog.valoraciones.includes(x.trabajo.valoracionAnterior));
assert.ok(!catalog.valoraciones.some(p=>p.includes(x.revisionCandidata)));
assert.notEqual(x.trabajo.hojaBorrador,x.trabajo.hojaAnterior);
});
test('XP comparte contrato único, escenarios y magnitudes coherentes',()=>{
const e=x.estandarPresentacion;
assert.equal(e.version,'jmr-a12-ficha-unica-v1');
assert.equal(e.mos,.35);assert.equal(e.nivel1.capitulos,18);assert.equal(e.nivel2.apartados,12);
assert.deepEqual(e.escenarios,['Base','Conservador','Optimista','Disrupción']);
assert.equal(e.disrupcionFueraDelPromedio,true);
assert.equal(e.release.estadoBorrador,'NO_PUBLICAR');
assert.equal(e.release.auditoriaEconomica,'después de revisión visual del usuario');
assert.equal(e.metodoPrincipal.financiero,'FCFE DCF regulatorio');
});
test('XP no mezcla monedas, contratos FCFE ni capital gerencial',()=>{
assert.equal(x.moneda,'BRL');assert.match(x.unidades,/BRL millones/);
assert.match(x.unidades,/USD por acción/);
assert.equal(x.datosHistoricosR2.valorAnterior_USDaccion,original.valorPrincipal);
assert.ok(x.conciliaciones.some(r=>r.id==='CAPITAL_REG'&&r.estado==='PENDIENTE'));
assert.ok(x.trabajo.formulasFuenteIntactas);
});
