#!/usr/bin/env node
'use strict';
// Gate estructural del perfil Floyd R1–R6 (alias histórico Reboot) (contrato jmr-reboot-3libros-v1): seis archivos, tres DCF, M y análisis.
// La calidad económica la audita R6 independiente; este validador NO la certifica.
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto'),assert=require('node:assert/strict');
const near=(a,b,t=1e-6)=>Number.isFinite(a)&&Number.isFinite(b)&&Math.abs(a-b)<=Math.max(t,Math.abs(b)*1e-8);
const sheetId=u=>/^https:\/\/docs\.google\.com\/spreadsheets\/d\/([A-Za-z0-9_-]+)\/edit(?:[?#].*)?$/.exec(String(u||''))?.[1];
const docId=u=>/^https:\/\/docs\.google\.com\/document\/d\/([A-Za-z0-9_-]+)\/edit(?:[?#].*)?$/.exec(String(u||''))?.[1];
const METHODS=['EV/EBITDA','EV/FCFF','P/E','P/FCFE','P/OCF'];
const grid=x=>Array.isArray(x)&&x.length===5&&x.every(r=>Array.isArray(r)&&r.length===5&&r.every(Number.isFinite));
function validateRebootRecord(v){
  const t=v.ticker+': ';
  assert.ok(['Floyd','Reboot'].includes(v.perfil_valoracion),t+'perfil Floyd R1–R6 o alias Reboot');
  assert.equal(v.version_metodo,v.perfil_valoracion,t+'versión de método incoherente con perfil');
  assert.ok(['jmr-reboot-3libros-v1','floyd-libro-unico-v1'].includes(v.contratoLibros),t+'contrato Floyd desconocido');
  const unico=v.contratoLibros==='floyd-libro-unico-v1';
  const L=v.libros||{};
  let multiplesId;
  if(unico){
    const id=sheetId(L.unico);
    assert.ok(id,t+'libro único debe ser una URL Sheets válida');
    assert.ok(docId(L.analisis),t+'documento de análisis ausente');
    assert.notEqual(id,docId(L.analisis),t+'libro y análisis deben ser distintos');
    assert.equal(L.unico,v.hojaGoogle,t+'hojaGoogle debe ser el libro único');
    assert.equal(id,v.sheet_id,t+'sheet_id debe ser el libro único');
    assert.ok(!L.dcf&&!L.historicos&&!L.multiplos,t+'no mezclar arquitectura única y heredada');
    multiplesId=id;
  }else{
    const ids=[sheetId(L.historicos),sheetId(L.dcf?.base),sheetId(L.dcf?.conservadora),sheetId(L.dcf?.optimista),sheetId(L.multiplos)];
    assert.ok(ids.every(Boolean),t+'los cinco libros Sheets deben ser URLs válidas');
    assert.equal(new Set(ids).size,5,t+'los cinco libros Sheets deben ser distintos');
    assert.ok(docId(L.analisis),t+'documento de análisis ausente');
    assert.equal(L.dcf.base,v.hojaGoogle,t+'hojaGoogle debe ser el DCF Base');
    assert.equal(ids[1],v.sheet_id,t+'sheet_id debe ser el DCF Base');
    multiplesId=ids[4];
  }
  const st=v.valorEsperado?.historias||[];
  assert.deepEqual(st.map(h=>h.id).sort(),['A','B','C'],t+'tres historias A/B/C');
  assert.ok(st.every(h=>Number.isFinite(h.valor)&&h.probabilidad>=0&&h.probabilidad<=1));
  const prob=st.reduce((s,h)=>s+h.probabilidad,0),exp=st.reduce((s,h)=>s+h.probabilidad*h.valor,0);
  const A=st.find(h=>h.id==='A').valor,B=st.find(h=>h.id==='B').valor,C=st.find(h=>h.id==='C').valor;
  assert.ok(near(prob,1),t+'probabilidades no suman 1');assert.ok(near(exp,v.valorEsperado.valor),t+'valor esperado no concilia');
  assert.ok(near(A,v.valorPrincipal)&&near(A,v.valorEsperado.dcfBase),t+'DCF Base no concilia');
  assert.ok(B<=A&&A<=C,t+'orden Conservadora ≤ Base ≤ Optimista');
  assert.equal(v.valorEsperado.disrupcionEnPromedio,false);assert.equal(v.valorEsperado.escenariosPromedio,3);
  assert.ok(near(v.precioMOS,A*(1-v.mos))&&v.baseMOS==='dcfBase',t+'MOS no corresponde al DCF Base');
  assert.deepEqual(v.escenariosDCF.historias.map(h=>h.valor),st.map(h=>h.valor));
  const sd=v.sensibilidadDCF||{};assert.ok(sd.matrices?.length>=2,t+'faltan matrices DCF');
  for(const m of sd.matrices){assert.ok(grid(m.valores),t+'matriz DCF no 5×5');assert.equal(m.centroConciliado,true);assert.ok(near(m.valores[2][2],A)&&near(m.centro,A),t+'centro de matriz DCF ≠ Base');}
  const s=v.sensibilidadMultiples||{};
  assert.equal(s.revisionId,v.revisionId);assert.equal(multiplesId,s.sourceSheetId);assert.equal(s.certificado,false,t+'no autocertificar');
  assert.deepEqual((s.matrices||[]).map(m=>m.metodo),METHODS,t+'cinco matrices en orden');
  assert.equal(s.resultadosSha256,crypto.createHash('sha256').update(JSON.stringify(s.matrices),'utf8').digest('hex'),t+'SHA-256 de matrices no coincide');
  const dm=v.descuentoMultiples||{};
  for(const m of s.matrices){
    const d=(dm.metodos||[]).find(x=>x.nombre===m.metodo);
    assert.equal(m.escenario,'base');
    if(m.estado==='N/D'||m.estado==='N/A'){
      // Sin ancla válida = no se inventa el centro, ni se finge que el valor es cero.
      assert.equal(m.peso,0,t+m.metodo+': N/D debe tener peso cero');
      assert.equal(d?.peso,0,t+m.metodo+': peso de descuento N/D debe ser cero');
      assert.equal(m.matriz,null,t+m.metodo+': N/D no puede tener cuadrícula ficticia');
      assert.equal(m.centro,null,t+m.metodo+': N/D no puede tener centro');
      assert.equal(m.vp3Original,null,t+m.metodo+': N/D no puede declarar VP3');
      assert.ok(typeof m.motivo==='string'&&m.motivo.length>=25,t+m.metodo+': falta motivo material documentado');
      continue;
    }
    assert.equal(m.estado,'OK',t+m.metodo+': estado de matriz desconocido');
    assert.ok(grid(m.matriz)&&m.fundamentalFY3?.length===5&&m.multiploElegido?.length===5,t+m.metodo+': falta cuadrícula/fundamental');
    assert.ok(near(m.matriz[2][2],m.centro,1e-4)&&near(m.centro,m.vp3Original,1e-4)&&near(m.centro,d?.base?.vp?.[2],1e-4),t+m.metodo+': centro ≠ VP3');
  }
  assert.ok(near(dm.pesoDcf+dm.pesoMultiplos,1),t+'pesos DCF+múltiplos');
  assert.ok(near(dm.metodos.reduce((x,m)=>x+m.peso,0),dm.pesoMultiplos,1e-9),t+'pesos de método ≠ peso de múltiplos');
  for(const [k,n] of [['conservador',B],['base',A],['optimista',C]]){
    assert.ok(near(dm.dcfHoy[k],n),t+'dcfHoy '+k);
    assert.ok(Math.abs(dm.pesoDcf*dm.dcfHoy[k]+dm.pesoMultiplos*dm.multiplesHoy[k]-dm.ponderadoHoy[k])<0.02,t+'combinado '+k);
  }
  assert.equal(v.estado,'EN_REVISION');assert.equal(v.auditPendingUserVisualReview,true);assert.equal(v.auditoriaEconomica,'NO_REALIZADA');
  assert.ok(v.salvedades?.length>=3);
  return true;
}
function validateRebootAnalysis(a,v){
  const t=a.ticker+': ',count=s=>String(s||'').replace(/<[^>]*>/g,' ').trim().split(/\s+/).filter(Boolean).length;
  assert.equal(a.perfil_valoracion,v.perfil_valoracion);assert.equal(a.revisionId,v.revisionId);assert.equal(a.status,'EN_REVISION',t+'no declarar sin auditoría R6');
  assert.equal(a.documentos?.nivel1,v.libros.analisis);assert.equal(a.documentos?.nivel2,v.libros.analisis);
  const h3=s=>[...String(s).matchAll(/<h3[^>]*>([\s\S]*?)<\/h3>/gi)].map(m=>m[1].replace(/<[^>]+>/g,'').trim());
  const nums=s=>h3(s).map(x=>/^(\d+)\.\s+/.exec(x)).filter(Boolean).map(m=>+m[1]);
  assert.deepEqual(nums(a.articleHtml),Array.from({length:14},(_,i)=>i+1),t+'Nivel 1 exige 14 capítulos numerados');
  assert.ok(h3(a.articleHtml).some(x=>/ciclos?/i.test(x)&&/macro|mercado/i.test(x)),t+'falta capítulo de ciclos');
  assert.deepEqual(nums(a.calculationHtml).slice(0,12),Array.from({length:12},(_,i)=>i+1),t+'Nivel 2 exige 12 apartados numerados');
  assert.equal(a.html,String(a.articleHtml)+String(a.calculationHtml),t+'html ≠ Nivel 1 + Nivel 2');
  assert.ok(count(a.articleHtml)>=3000,t+'Nivel 1 demasiado corto');assert.ok(count(a.calculationHtml)>=2500,t+'Nivel 2 demasiado corto');
  assert.equal(a.controlCobertura?.secciones,14);assert.equal(a.controlCobertura?.nivel2Apartados,12);assert.equal(a.controlCobertura?.auditoriaEconomicaIndependiente,false);
  assert.equal(a.linkedValuation?.valorPrincipal,v.valorPrincipal);
  // Las cifras clave de la valoración deben aparecer en el texto del análisis.
  const txt=a.articleHtml.replace(/<[^>]+>/g,' ');
  const es=x=>x.toFixed(2).replace('.',',');
  assert.ok(txt.includes(es(v.valorPrincipal)),t+'el Nivel 1 no cita el DCF Base de la valoración');
  assert.ok(txt.includes(es(v.valorEsperado.valor)),t+'el Nivel 1 no cita el valor esperado');
  assert.ok(txt.includes(es(v.precioMOS)),t+'el Nivel 1 no cita el precio con MOS');
  return count(a.articleHtml);
}
module.exports={validateRebootRecord,validateRebootAnalysis};
if(require.main===module){
  const root=path.resolve(__dirname,'..'),c=JSON.parse(fs.readFileSync(path.join(root,'catalogo.json'),'utf8'));
  const vals=new Map();let n=0;
  for(const p of c.valoraciones){const v=JSON.parse(fs.readFileSync(path.join(root,p),'utf8'));if(['jmr-reboot-3libros-v1','floyd-libro-unico-v1'].includes(v.contratoLibros)){validateRebootRecord(v);vals.set(v.ticker,{v,p});}}
  for(const p of c.analisis){const a=JSON.parse(fs.readFileSync(path.join(root,p),'utf8'));const o=vals.get(a.ticker);if(!o)continue;
    assert.equal(a.linkedValuation?.sourcePath,o.p);const w=validateRebootAnalysis(a,o.v);n++;console.log('FLOYD R1–R6 '+a.ticker+' '+o.v.revisionId+' · Nivel1 '+w+' palabras · R6 pendiente');}
  assert.equal(n,vals.size,'Empresa Reboot sin análisis activo');
  console.log('PASS estructural Floyd R1–R6: '+vals.size+' empresas. No sustituye R6 ni QA visual.');
}
