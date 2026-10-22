'use strict';
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
function validate(root=path.join(__dirname,'..')){
 const c=JSON.parse(fs.readFileSync(path.join(root,'catalogo.json'),'utf8'));
 const inventory=dir=>fs.readdirSync(path.join(root,dir),{withFileTypes:true}).flatMap(e=>e.isDirectory()?inventory(dir+'/'+e.name):e.name==='.gitkeep'?[]:[dir+'/'+e.name]).sort();
 for(const group of ['valoraciones','analisis','auditorias'])assert.deepEqual(inventory(group),c[group].slice().sort(),'Inventario: '+group);
 const vals=c.valoraciones.map(p=>({path:p,record:JSON.parse(fs.readFileSync(path.join(root,p)))}));
 for(const p of c.analisis){const a=JSON.parse(fs.readFileSync(path.join(root,p))),v=vals.find(x=>x.path===a.linkedValuation?.sourcePath);assert.ok(v,'Análisis sin valoración');assert.equal(a.ticker,v.record.ticker);assert.equal(a.date,v.record.fecha);assert.equal(a.remotePath,p);assert.deepEqual(a.linkedValuation.descuentoMultiples,v.record.descuentoMultiples);assert.equal((a.articleHtml.match(/<h2>/g)||[]).length,18);}
 for(const {record:v} of vals){require('./auditar_integridad.cjs').validateRecord(v);assert.ok(c.auditorias.includes('auditorias/narrativas/'+v.ticker+'.md'));assert.ok(v.salvedades.length);}
 return {valoraciones:vals.length,analisis:c.analisis.length,auditorias:c.auditorias.length};
}
module.exports={validate};if(require.main===module)console.log(JSON.stringify(validate(),null,2));
