'use strict';
const test=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),os=require('node:os'),path=require('node:path');
const {validate}=require('../validar_catalogo.cjs');const root=path.join(__dirname,'../..');
function fixture(t,mutate){const tmp=fs.mkdtempSync(path.join(os.tmpdir(),'jmr-catalog-'));t.after(()=>fs.rmSync(tmp,{recursive:true,force:true}));for(const p of ['catalogo.json','valoraciones','analisis','auditorias','scripts'])fs.cpSync(path.join(root,p),path.join(tmp,p),{recursive:true});mutate(tmp);return tmp;}
test('Netflix publicada conserva vínculos, 18 secciones y auditoría',()=>assert.deepEqual(validate(),{valoraciones:1,analisis:1,auditorias:1}));
test('rechaza análisis enlazado a otra valoración',t=>{const tmp=fixture(t,dir=>{const c=require(path.join(dir,'catalogo.json'));const p=path.join(dir,c.analisis[0]);const a=JSON.parse(fs.readFileSync(p));a.linkedValuation.sourcePath='valoraciones/OTRA.json';fs.writeFileSync(p,JSON.stringify(a));});assert.throws(()=>validate(tmp),/Análisis sin valoración/);});
test('rechaza MOS que no deriva del DCF principal',t=>{const tmp=fixture(t,dir=>{const c=require(path.join(dir,'catalogo.json'));const p=path.join(dir,c.valoraciones[0]);const v=JSON.parse(fs.readFileSync(p));v.precioMOS=0;fs.writeFileSync(p,JSON.stringify(v));});assert.throws(()=>validate(tmp),/MOS diferente/);});
