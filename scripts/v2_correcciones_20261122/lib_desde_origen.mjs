import fs from 'node:fs'; import path from 'node:path';
import {construirCatalogo} from '/home/user/Modelo-JMR-V2/scripts/v2-catalogo.mjs';
const [,,origen,salida]=process.argv; const {catalogo,errores}=construirCatalogo(origen); if(errores.length) throw Error(errores.join('\n'));
const files={'catalogo.json':catalogo};
for(const e of catalogo.empresas){files[e.archivo]=JSON.parse(fs.readFileSync(path.join(origen,e.archivo)));const a=path.join(origen,'analisis',e.ticker+'.json'); if(fs.existsSync(a)) files['analisis/'+e.ticker+'.json']=JSON.parse(fs.readFileSync(a));}
fs.writeFileSync(salida,JSON.stringify({schemaVersion:'jmr-biblioteca-1',app:'jmr-v2',files}));console.log(catalogo.empresas.length,'empresas');
