'use strict';
const test=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs'),path=require('node:path');
const root=path.resolve(__dirname,'../..');
const read=p=>JSON.parse(fs.readFileSync(path.join(root,p),'utf8'));
const same=(a,b)=>typeof a==='number'&&typeof b==='number'&&Math.abs(a-b)<=Math.max(1e-7,Math.abs(b)*1e-8);
test('SHAK: 125 fórmulas fuente preservadas como evidencia y no como publicación',()=>{
 const id='SHAK-20261029-A12-R2';
 const v=read('valoraciones/'+id+'.json');
 const c=read('candidatos/hoja-multiples/'+id+'-captura-rango.json');
 const proof=read('evidencia/capturas-acotadas-20261031/'+id+'-formulas.json');
 assert.equal(proof.tipo,'EVIDENCIA_ACOTADA_FORMULAS_NO_PUBLICADA');
 assert.equal(proof.revisionId,v.revisionId);
 assert.equal(proof.sourceSheetId,v.sheet_id);
 assert.equal(c.revisionId,v.revisionId);
 assert.equal(proof.shaFotografiaCompleta,null);
 assert.equal(proof.fotoCompleta46Hojas,false);
 assert.equal(proof.estado,'SOLO_EVIDENCIA_NO_INTEGRAR');
 assert.equal(v.sensibilidadMultiples?.matrices?.length||0,0,
   'No convertir la evidencia acotada en matriz oficial');
 assert.equal(proof.metodos.length,7);
 let ok=0,nd=0, formulas=0;
 for(let i=0;i<7;i++){
   const m=proof.metodos[i],s=c.metodos[i];
   assert.equal(m.method,s.metodo);
   assert.equal(m.sourceStatus,s.estadoHoja);
   assert.equal(m.origin,s.origen);
   if(m.sourceStatus==='OK'){
     ok++;
     assert.equal(m.grid.length,5);
     assert.equal(m.gridFormulas.length,5);
     for(let r=0;r<5;r++)for(let col=0;col<5;col++){
       assert.ok(same(m.grid[r][col],s.matriz[r][col]),m.method+' matrix');
       assert.match(m.gridFormulas[r][col],/^=/);
       formulas++;
     }
     assert.ok(same(m.grid[2][2],s.centro));
     assert.ok(same(m.sourceVP3,s.vp3Original));
   }else{
     nd++;
     assert.equal(m.sourceStatus,'N/D');
     assert.equal(s.matriz,null);
     assert.equal(m.grid,null);
   }
 }
 assert.equal(ok,5);assert.equal(nd,2);assert.equal(formulas,125);
 assert.equal(v.estado,'EN_REVISION');
});
