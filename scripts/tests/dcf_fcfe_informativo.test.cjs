'use strict';
const test=require('node:test'),assert=require('node:assert/strict');
const {validateDcfFcfe}=require('../validar_catalogo.cjs');
const rec=()=>({ticker:'X',revisionId:'X-R1',valorPrincipal:100,dcfFCFE:{estado:'INFORMATIVO',alimentaValorPrincipal:false,sinMOS:true,
 ponderadoNoEntraEnValorPrincipal:true,revisionId:'X-R1',
 historias:{conservador:{probabilidad:.25,dcfFCFF:80,dcfFCFE:81,diferencia:.0125,ponderadoFcffFcfe:80.5},
  base:{probabilidad:.5,dcfFCFF:100,dcfFCFE:99,diferencia:-.01,ponderadoFcffFcfe:99.5},
  optimista:{probabilidad:.25,dcfFCFF:120,dcfFCFE:121,diferencia:.0083,ponderadoFcffFcfe:120.5}},
 promedio:{dcfFCFF:100,dcfFCFE:100,diferencia:0,ponderadoFcffFcfe:100},
 controles:{promedioFcffHoja:100,concilia:true,dcfFcffBaseHoja:100},baseDetalle:{puente:{valorPorAccionFcfe:99}}}});
test('un dcfFCFE informativo y conciliado se acepta; sin él no se exige nada',()=>{
 validateDcfFcfe(rec());validateDcfFcfe({ticker:'Y'});
});
test('rechaza FCFE como valor principal, con MOS, de otra revisión o que no concilia con el DCF Base',()=>{
 const m=f=>{const r=rec();f(r);return r};
 for(const f of [r=>{r.dcfFCFE.alimentaValorPrincipal=true},r=>{r.dcfFCFE.sinMOS=false},r=>{r.dcfFCFE.revisionId='otra'},
   r=>{r.valorPrincipal=105},r=>{r.dcfFCFE.promedio.dcfFCFE=90},r=>{r.dcfFCFE.estado='PRINCIPAL'}])
   assert.throws(()=>validateDcfFcfe(m(f)));
});
