'use strict';
const test=require('node:test'),assert=require('node:assert/strict');
const {template,preflightSectorial}=require('../preflight_sectorial.cjs');
const {preflight}=require('../preflight_floyd.cjs');
function complete(kind){
 const v=template(kind);v.ticker='PRUEBA';v.revisionId='PRUEBA-SECTORIAL-R1';
 Object.assign(v.identidad,{subtipo:'Prueba sintética',moneda:'USD',escala:'millones',claseAccion:'común',
 corteContable:'2026-06-30',fechaValoracion:'2026-11-12',fechaPrecio:'2026-11-10',
 libroSectorial:'https://docs.google.com/spreadsheets/d/TEST_BOOK/edit',documentoAnalisis:'https://docs.google.com/document/d/TEST_DOC/edit'});
 for(const [key,s]of Object.entries(v.fuentes))Object.assign(s,{url:'https://example.com/prueba',fechaPublicacion:'2026-11-10',corte:key==='precio'?'2026-11-10':'2026-06-30',detalle:'Caso sintético de prueba, no datos reales'});
 for(const c of Object.values(v.controles))Object.assign(c,{estado:'APROBADO',evidencia:{revisionId:v.revisionId,url:'https://example.com/prueba',detalle:'Caso sintético de prueba'}});
 v.snapshot={revisionId:v.revisionId,sourceSheetId:'TEST_BOOK',sha256:'a'.repeat(64),metodo:v.identidad.metodoPrincipal,tasaDescuento:v.identidad.tasaDescuento,
 historias:[{nombre:'Conservadora',valor:60,probabilidad:.25},{nombre:'Base',valor:100,probabilidad:.5},{nombre:'Optimista',valor:140,probabilidad:.25}],valorPrincipal:100,precioMOS:65};return v;
}
for(const kind of ['banco','aseguradora','holding']){
 test(kind+': plantilla vacía no aprueba; caso trazado queda candidato sin autopublicar',()=>{
  assert.equal(preflightSectorial(template(kind)).estado,'INCOMPLETO_R1');
  const r=preflightSectorial(complete(kind));assert.equal(r.estado,'CANDIDATO_R5_COMPLETO');assert.equal(r.publicacionAutorizada,false);
 });
 test(kind+': no puede usar el preflight industrial ni una tasa incompatible',()=>{
  assert.throws(()=>preflight({perfilEmpresa:kind}),/preflight_sectorial/);
  const v=complete(kind);v.identidad.tasaDescuento='WACC';assert.equal(preflightSectorial(v).fases.R1,false);
 });
}
test('capital regulatorio sin fuente y reservas sin conciliación bloquean las fases dependientes',()=>{
 const b=complete('banco');b.fuentes.capital.url='';let r=preflightSectorial(b);assert.equal(r.fases.R1,true);assert.equal(r.fases.R2,false);assert.equal(r.fases.R5,false);
 const i=complete('aseguradora');i.controles.reservas_reaseguro.estado='PENDIENTE';assert.equal(preflightSectorial(i).fases.R2,false);
});
test('holding sin propiedad cruzada resuelta o adaptador verificado no alcanza R5 completo',()=>{
 const h=complete('holding');h.controles.propiedad_cruzada.estado='PENDIENTE';assert.equal(preflightSectorial(h).fases.R2,false);
 const v=complete('holding');v.controles.adaptador_sectorial.estado='PENDIENTE';assert.equal(preflightSectorial(v).estado,'R3_R4_LISTOS');
});
test('datos posteriores, evidencia de otra revisión y snapshot de otra hoja se rechazan',()=>{
 for(const mutate of [v=>v.fuentes.estados.fechaPublicacion='2026-11-13',v=>v.controles.estados.evidencia.revisionId='OTRA']){
  const v=complete('banco');mutate(v);assert.equal(preflightSectorial(v).fases.R2,false);
 }
 const v=complete('holding');v.snapshot.sourceSheetId='OTRA';assert.equal(preflightSectorial(v).fases.R3_R4,false);
});
test('probabilidades y MOS no pueden cambiar la base económica de la revisión',()=>{
 for(const mutate of [v=>v.snapshot.precioMOS=70,v=>v.snapshot.historias[0].probabilidad=.5,v=>v.snapshot.valorPrincipal=110]){
  const v=complete('aseguradora');mutate(v);assert.equal(preflightSectorial(v).fases.R3_R4,false);
 }
});
