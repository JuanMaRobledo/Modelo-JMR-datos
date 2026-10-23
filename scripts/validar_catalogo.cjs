'use strict';
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
function validate(root=path.join(__dirname,'..')){
 const c=JSON.parse(fs.readFileSync(path.join(root,'catalogo.json'),'utf8'));
 // El catálogo enumera registros PUBLICADOS. Auditorías archivadas se conservan
 // fuera del catálogo para trazabilidad y nunca contaminan la auditoría vigente.
 const inventory=dir=>fs.readdirSync(path.join(root,dir),{withFileTypes:true})
   .flatMap(e=>e.isDirectory()?inventory(dir+'/'+e.name):e.name==='.gitkeep'?[]:[dir+'/'+e.name]).sort();
 for(const group of ['valoraciones','analisis'])assert.deepEqual(inventory(group),c[group].slice().sort(),'Inventario: '+group);
 assert.deepEqual(inventory('auditorias/narrativas'),c.auditorias.slice().sort(),'Inventario: auditorias vigentes');
 assert.ok(c.auditorias.every(p=>p.startsWith('auditorias/narrativas/')),'Un archivo histórico no puede ser versión vigente');
 const vals=c.valoraciones.map(p=>({path:p,record:JSON.parse(fs.readFileSync(path.join(root,p)))}));
 for(const p of c.analisis){const a=JSON.parse(fs.readFileSync(path.join(root,p))),v=vals.find(x=>x.path===a.linkedValuation?.sourcePath);assert.ok(v,'Análisis sin valoración');assert.equal(a.ticker,v.record.ticker);// La revisión editorial puede ser posterior a la valoración, sin cambiar el DCF.
 const dateOK=/^\\d{4}-\\d{2}-\\d{2}$/.test(a.date||'') &&
   /^\\d{4}-\\d{2}-\\d{2}$/.test(v.record.fecha||'') &&
   a.date>=v.record.fecha;
 assert.ok(dateOK,'La fecha editorial no puede preceder la valoración');
 if(a.revisionId&&v.record.revisionId)assert.equal(a.revisionId,v.record.revisionId,'Revisión financiera distinta');
 if(a.linkedValuation.revisionId&&v.record.revisionId)assert.equal(a.linkedValuation.revisionId,v.record.revisionId,'Enlace a revisión distinta');assert.equal(a.remotePath,p);assert.deepEqual(a.linkedValuation.descuentoMultiples,v.record.descuentoMultiples);assert.equal((a.articleHtml.match(/<h2>/g)||[]).length,18);}
 for(const {record:v} of vals){require('./auditar_integridad.cjs').validateRecord(v);assert.ok(c.auditorias.includes('auditorias/narrativas/'+v.ticker+'.md'));assert.ok(v.salvedades.length);}
 return {valoraciones:vals.length,analisis:c.analisis.length,auditorias:c.auditorias.length};
}
module.exports={validate};if(require.main===module)console.log(JSON.stringify(validate(),null,2));
