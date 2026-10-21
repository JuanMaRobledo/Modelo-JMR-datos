"use strict";
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const root=path.join(__dirname,'..');
function inventory(dir){if(!fs.existsSync(dir))return [];return fs.readdirSync(dir,{withFileTypes:true}).flatMap(x=>x.isDirectory()?inventory(path.join(dir,x.name)):[path.relative(root,path.join(dir,x.name)).replaceAll('\\','/')]).filter(x=>!/\.gitkeep$/.test(x)).sort();}
function validate(){const c=JSON.parse(fs.readFileSync(path.join(root,'catalogo.json'),'utf8'));for(const group of ['valoraciones','analisis','auditorias'])assert.deepEqual(inventory(path.join(root,group)),c[group].slice().sort(),'Inventario inesperado: '+group);
const v=JSON.parse(fs.readFileSync(path.join(root,c.valoraciones[0]),'utf8')),a=JSON.parse(fs.readFileSync(path.join(root,c.analisis[0]),'utf8'));
assert.equal(v.ticker,'NFLX');assert.equal(a.ticker,'NFLX');assert.equal(v.fecha,'2026-10-15');assert.equal(a.date,'2026-10-15');
assert.equal(v.descuentoMultiples.dcfHoy.base,71.68383443894892);assert.deepEqual(a.linkedValuation.descuentoMultiples.dcfHoy,v.descuentoMultiples.dcfHoy);assert.equal(a.linkedValuation.sourcePath,c.valoraciones[0]);assert.equal(a.remotePath,c.analisis[0]);
assert.equal(v.baseMOS,'dcfBase');assert.ok(Math.abs(v.precioMOS-v.descuentoMultiples.dcfHoy.base*(1-v.mos))<1e-8);assert.equal((a.html.match(/<h2\b/g)||[]).length,18);assert.equal(c.auditorias.length,0);
return {valoraciones:c.valoraciones.length,analisis:c.analisis.length,auditorias:0,dcfBase:v.descuentoMultiples.dcfHoy.base,fecha:v.fecha};}
module.exports={validate};if(require.main===module)console.log(JSON.stringify(validate(),null,2));
