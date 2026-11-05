import fs from 'node:fs/promises';
import {Workbook,SpreadsheetFile} from '@oai/artifact-tool';
const dir='/workspace/scratch/9514d8f35352/cmg_work';
const spec=JSON.parse(await fs.readFile(dir+'/workbook_spec.json','utf8'));
const wb=Workbook.create();
for(const name of Object.keys(spec.sheets))wb.worksheets.add(name);
function xy(a){const m=a.match(/([A-Z]+)(\d+)/);let c=0;for(const ch of m[1])c=c*26+ch.charCodeAt(0)-64;return [+m[2],c];}
for(const [name,cells] of Object.entries(spec.sheets)){
 const sh=wb.worksheets.getItem(name);let rows=0,cols=0;
 for(const a of Object.keys(cells)){const [r,c]=xy(a);rows=Math.max(rows,r);cols=Math.max(cols,c);}
 const vals=Array.from({length:rows},()=>Array(cols).fill(null));const formulas=[];
 for(const [a,v] of Object.entries(cells)){const [r,c]=xy(a);if(typeof v==='string'&&v.startsWith('='))formulas.push([r,c,v]);else vals[r-1][c-1]=v;}
 sh.getRangeByIndexes(0,0,rows,cols).values=vals;
 formulas.sort((a,b)=>a[0]-b[0]||a[1]-b[1]);
 for(let i=0;i<formulas.length;){const first=formulas[i];const run=[first[2]];let j=i+1;while(j<formulas.length&&formulas[j][0]===first[0]&&formulas[j][1]===first[1]+run.length){run.push(formulas[j][2]);j++;}sh.getRangeByIndexes(first[0]-1,first[1]-1,1,run.length).formulas=[run];i=j;}
 sh.showGridLines=false;
 if(name!=='Motor JMR'){
  const used=sh.getRangeByIndexes(0,2,rows,Math.max(1,cols-2));used.format.font={name:'Arial',size:10,color:'#202B35'};used.format.rowHeight=21;
  sh.getRange('A:B').format.columnWidth=2;
  sh.getRangeByIndexes(1,2,1,Math.max(1,cols-2)).format.font={name:'Arial',size:14,bold:true,color:'#253D32'};
  for(const r of spec.headers[name]||[]){const rg=sh.getRangeByIndexes(r-1,2,1,Math.max(1,cols-2));rg.format.fill='#334E43';rg.format.font={name:'Arial',size:10,color:'#FFFFFF',bold:true};rg.format.rowHeight=26;}
  for(let i=0;i<(spec.columns[name]||[]).length;i+=2)sh.getRange(spec.columns[name][i]+':'+spec.columns[name][i].split(':').at(-1)).format.columnWidth=spec.columns[name][i+1];
  // Format only numeric working area; distinct rates below.
  sh.getRangeByIndexes(4,3,Math.max(1,rows-4),Math.max(1,cols-3)).setNumberFormat('#,##0.00;(#,##0.00);"-"');
  if(['Base','Conservadora','Optimista','Disrupcion'].includes(name)){
   for(const rg of ['D5','D8:D10','D12:D13','D15','D25:O25','E20:N20','D27:O27','D24:O24','D32:O33','D37:O39','D54','D65:O66'])sh.getRange(rg).setNumberFormat('0.0%');
   for(const rg of ['E18:N19','D16:O16'])sh.getRange(rg).setNumberFormat('#,##0');
   sh.getRange('C51:D53').format.font.bold=true;sh.getRange('C51:D53').format.borders={preset:'doubleBottom',color:'#334E43',style:'thin'};
   sh.freezePanes.freezeRows(16);sh.freezePanes.freezeColumns(3);
  }
  if(name==='Sensibilidades'){for(const rg of ['D7:D11','E6:I6','D17:D21','E16:I16','D27:D31','E26:I26'])sh.getRange(rg).setNumberFormat('0.0%');}
  if(name==='Resumen'){sh.getRange('F6:F9').setNumberFormat('0.0%');sh.getRange('D14:D17').setNumberFormat('0.0%');sh.getRange('D16').setNumberFormat('$0.00');sh.getRange('C6:F6').format.fill='#EAF0EA';sh.getRange('D6:E6').format.font={name:'Arial',size:14,bold:true};sh.getRange('D19:L21').format.columnWidth=20;}
 }
 console.log('built',name,Object.keys(cells).length);
}
wb.recalculate();
console.log((await wb.inspect({kind:'table',range:'Resumen!C5:F17',include:'values,formulas',tableMaxRows:15,tableMaxCols:4,maxChars:4000})).ndjson);
console.log((await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#NUM!|#N/A',options:{useRegex:true,maxResults:15},summary:'Errores',maxChars:2000})).ndjson);
await fs.mkdir(dir+'/outputs',{recursive:true});
const out=await SpreadsheetFile.exportXlsx(wb);await out.save(dir+'/outputs/CMG_R4_AUXILIAR_JMR.xlsx');
for(const [name,range] of [['Resumen','C2:F17'],['Base','C16:J39'],['Datos y ajustes','C65:F78'],['Sensibilidades','C5:I13'],['Multiplos','C5:K10']]){
 const img=await wb.render({sheetName:name,range,scale:1.3,format:'png'});await fs.writeFile(dir+'/outputs/'+name.replaceAll(' ','_')+'.png',new Uint8Array(await img.arrayBuffer()));
}
await fs.writeFile(dir+'/artifact_verification.json',JSON.stringify({summary:wb.worksheets.getItem('Resumen').getRange('C5:F17').values,base:wb.worksheets.getItem('Base').getRange('C43:D70').values,sens:wb.worksheets.getItem('Sensibilidades').getRange('C5:I43').values,multiples:wb.worksheets.getItem('Multiplos').getRange('C5:K10').values}));
