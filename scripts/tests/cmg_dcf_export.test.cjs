const test=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path');
const root=path.resolve(__dirname,'../..');
const read=p=>JSON.parse(fs.readFileSync(path.join(root,p),'utf8'));
test('CMG: 75 celdas DCF y ejes exactos de la hoja, centros conciliados y MOS intacto',()=>{
 const rec=read('valoraciones/CMG-20261028-A3.json');
 const capture=read('evidencia/CMG-20261103-sensibilidad-dcf.json');
 assert.equal(rec.revisionId,capture.revisionId);assert.equal(rec.sheet_id,capture.sourceSheetId);
 assert.equal(rec.valorPrincipal,25.246494601933065);assert.equal(rec.precioMOS,16.410221491256493);
 assert.equal(rec.estado,'EN_REVISION');
 const g=capture.source.values;
 assert.equal(rec.sensibilidadDCF.matrices.length,3);
 for(const [i,head,start] of [[0,4,5],[1,15,16],[2,26,27]]){
  const m=rec.sensibilidadDCF.matrices[i];
  assert.equal(m.sourceSheetId,rec.sheet_id);
  assert.deepEqual(m.columns,g[head].slice(1,6));
  assert.deepEqual(m.rows,g.slice(start,start+5).map(r=>r[0]));
  assert.deepEqual(m.values,g.slice(start,start+5).map(r=>r.slice(1,6)));
  assert.equal(m.centroConciliado,true);
  assert.ok(Math.abs(m.values[2][2]-rec.valorPrincipal)<1e-8);
 }
});
