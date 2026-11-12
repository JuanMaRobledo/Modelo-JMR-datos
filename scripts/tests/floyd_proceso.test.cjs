'use strict';
const test=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path');
const root=path.resolve(__dirname,'../..');
const {validateRebootRecord}=require('../validar_reboot.cjs');
const {preflight}=require('../preflight_floyd.cjs');
const load=p=>JSON.parse(fs.readFileSync(path.join(root,p),'utf8'));
const vp='valoraciones/ORCL-FLOYD-FY26Q1FY27-R1.json',ap='analisis/ORCL-research-ORCL-FLOYD-FY26Q1FY27-R1.json';
const fresh=()=>load(vp);
test('nuevo emisor: contrato real de dos URLs, sin convertirlo a IDs heredados',()=>{
 const v=fresh();v.ticker='NUEVA';v.revisionId='NUEVA-FLOYD-FY26-R1';
 v.sensibilidadMultiples.revisionId=v.revisionId;
 assert.equal(validateRebootRecord(v),true);
});
test('rechaza matriz corrupta, fuente ajena, enlace ajeno y arquitectura mixta',()=>{
 for(const mutate of [v=>v.sensibilidadMultiples.matrices[0].matriz[0][0]++,v=>v.sensibilidadMultiples.sourceSheetId='ajena',v=>v.hojaGoogle='https://docs.google.com/spreadsheets/d/ajeno/edit',v=>v.libros.dcf={base:v.libros.unico}]){
  const v=fresh();mutate(v);assert.throws(()=>validateRebootRecord(v));
 }
});
test('la app necesita clasificación exacta por revisión, no basta estar en valoraciones',()=>{
 const v=fresh(),a=load(ap),c=load('catalogo.json');
 assert.equal(preflight(v,a,c,vp).estado,'ESTRUCTURA_OK');
 delete c.controlModeloA.empresas.ORCL;
 assert.throws(()=>preflight(v,a,c,vp),/rutaValoracion/);
});
test('legado de seis archivos conserva validación estricta de URLs distintas',()=>{
 const v=fresh();v.contratoLibros='jmr-reboot-3libros-v1';
 const url=id=>'https://docs.google.com/spreadsheets/d/'+id+'/edit';
 v.libros={historicos:url('H'),dcf:{base:v.hojaGoogle,conservadora:url('C'),optimista:url('O')},multiplos:url('M'),analisis:v.libros.analisis};
 v.sensibilidadMultiples.sourceSheetId='M';
 assert.equal(validateRebootRecord(v),true);
 v.libros.multiplos=v.libros.historicos;
 assert.throws(()=>validateRebootRecord(v),/distintos/);
});
test('valores de seis fichas conservados al corregir solo procedencia',()=>{
 const c=load('catalogo.json');
 for(const p of c.valoraciones){const v=load(p);assert.equal(validateRebootRecord(v),true);}
});
