import fs from 'node:fs'; import vm from 'node:vm';
const R='/home/user/Modelo-JMR-V2/';
const html=fs.readFileSync(R+'docs/jmr-v2.html','utf8');
const eng=vm.runInNewContext(html.slice(html.indexOf('const JMR_DCF=(()=>{'),html.indexOf('const JMR_IND=(()=>{'))+'\nJMR_DCF;',{});
const {evaluarExpediente}=await import(R+'docs/v2/expediente-v2.mjs');const {crearMotor}=await import(R+'docs/v2/motores/despacho.mjs');
const [n,o]=process.argv.slice(2).map(p=>JSON.parse(fs.readFileSync(p)).files);
let ok=true;
for(const c of n['catalogo.json'].empresas){const t=c.ticker,m=n['empresas/'+t+'.json'];
 const en=evaluarExpediente(m,crearMotor(eng)).resumen, eo=evaluarExpediente(o['empresas/'+t+'.json'],crearMotor(eng)).resumen;
 const v=eng.calculateAll(m).scenarios.base.perShare, vo=eng.calculateAll(o['empresas/'+t+'.json']).scenarios.base.perShare;
 const cortos=[];for(const s of ['conservador','base','optimista'])for(const k of ['tesis','crecimiento','margenes','reinversion','roic','descuento','terminal','contraevidencia','evidencia']){const x=m.justificaciones.escenarios[s][k];if(!(typeof x==='string'&&x.length>80))cortos.push(s+'.'+k);}
 const floyd=JSON.stringify(m.justificaciones).match(/heredados del libro Floyd|Ver capítulos 10 y 12/g);
 if(cortos.length||floyd||v!==vo||JSON.stringify(en)!==JSON.stringify(eo)) ok=false;
 console.log(t.padEnd(5),'valor',v.toFixed(2),v===vo?'=':'≠','controles',JSON.stringify(en),JSON.stringify(en)===JSON.stringify(eo)?'(sin cambio)':'(antes '+JSON.stringify(eo)+')','cortos',cortos.length,'Floyd',floyd?floyd.length:0);
}
console.log(ok?'TODO OK':'REVISAR');
