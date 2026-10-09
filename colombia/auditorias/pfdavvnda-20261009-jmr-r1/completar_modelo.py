import json, math, statistics
from pathlib import Path
P=Path(__file__).parent
inp=json.loads((P/'inputs_actuales.json').read_text())
req=[]; adds=[]
IDS={'Base_1':1425003473,'Conservador_1':321033654,'Optimista_1':265703549,'Disrupcion_1':621850745,'Motor Operativo':1951000109,'Terminal regulatorio':1951000110,'Supuestos':443728977,'Capital Regulatorio':1951000106,'Múltiplos Banco':1951000101,'Pares Históricos':1951000107,'Resumen':11420752,'Verificación documental':1951000108,'Convergencia terminal':1951000114,'Sensibilidad Damodaran':1951000115,'Ke Colombia':1951000105,'Auditoría Damodaran':1951000113}
K=1951000118; C=1951000119; H=1951000120
def cv(v):
 if v is None:return {}
 return {'userEnteredValue':{('numberValue' if isinstance(v,(int,float)) else 'formulaValue' if v.startswith('=') else 'stringValue'):v}}
def wr(s,r,c,rows):
 req.append({'updateCells':{'start':{'sheetId':s,'rowIndex':r-1,'columnIndex':c-1},'rows':[{'values':[cv(v) for v in row]} for row in rows],'fields':'userEnteredValue'}})
def put(s,cell,v):
 import re
 a,r=re.match(r'([A-Z]+)(\d+)',cell).groups();col=0
 for x in a:col=col*26+ord(x)-64
 wr(IDS.get(s,s),int(r),col,[[v]])
def add(s,title,rows,cols):
 adds.append({'addSheet':{'properties':{'sheetId':s,'title':title,'gridProperties':{'rowCount':rows,'columnCount':cols,'frozenRowCount':4,'hideGridlines':True}}}})
 req.extend([{'repeatCell':{'range':{'sheetId':s},'cell':{'userEnteredFormat':{'textFormat':{'fontFamily':'Arial','fontSize':10},'wrapStrategy':'WRAP','verticalAlignment':'TOP'}},'fields':'userEnteredFormat'}},{'repeatCell':{'range':{'sheetId':s,'endRowIndex':1},'cell':{'userEnteredFormat':{'backgroundColor':{'red':.08,'green':.15,'blue':.24},'textFormat':{'bold':True,'fontSize':14,'foregroundColor':{'red':1,'green':1,'blue':1}}}},'fields':'userEnteredFormat.backgroundColor,userEnteredFormat.textFormat'}},{'updateDimensionProperties':{'range':{'sheetId':s,'dimension':'COLUMNS','startIndex':0,'endIndex':cols},'properties':{'pixelSize':165},'fields':'pixelSize'}},{'updateDimensionProperties':{'range':{'sheetId':s,'dimension':'ROWS','startIndex':0,'endIndex':rows},'properties':{'pixelSize':48},'fields':'pixelSize'}}])
add(K,'Ke sustentado',60,12);add(C,'Capital completo',95,20);add(H,'Anclas verificadas',80,12)
countries=[('Colombia',122352593,.027201825339291618),('Costa Rica',20316411,.044512077827931727),('Honduras',6311058,.055712829438228272),('Panamá',11704463,.027201825339291618),('El Salvador',9717479,.080441761564857009),('Estados Unidos / Miami',4375785,.0021863536781947081)]
crp=sum(n*p for _,n,p in countries)/sum(n for _,n,p in countries)
rf=.13217-.017498812238305829;erp=.042
wr(K,1,1,[['JMR · Ke nominal COP · corte 09-oct-2026'],['TES 25-sep-2026; ERP 01-oct-2026; países julio2026; beta sector enero2026. Se usan las últimas series primarias recuperadas, no una falsa fecha única.'],['Ke = TES − spread soberano Colombia + beta × ERP maduro + CRP por exposición; lambda país =1; sin prima discrecional de liquidez.'],['Insumo','Valor','Fuente / convención'],['TES COP julio2036',.13217,'MHCP/IRC, 25-sep-2026: tabla SEN / MEC, aproximadamente10años'],['Spread Colombia rating',.017498812238305829,'Damodaran ctrypremJuly26.xlsx, Colombia, default spread'],['Rf COP depurado','=B5-B6','Aproximación TES menos spread por rating; sensibilidad en hoja.'],['ERP mercado maduro',erp,'Damodaran 01-oct-2026,4,20%. CRP de EEUU se incluye por separado en exposición Miami; no sumar4,42% más el mismo riesgo EEUU.'],['Beta bancaria inicial',.7,'Money Center Banks,604 firmas globales,enero2026; beta apalancada sectorial, depósitos no son deuda industrial.'],['Beta estable',1,'Convergencia analítica años6–10 hacia empresa madura; no regresión propia.'],['CRP ponderado','=SUMPRODUCT(C18:C23;D18:D23)','Cartera por geografía H126; pesos constantes como proxy de exposición, no confundir con ingresos por país.'],['Ke inicial','=B7+B9*B8+B11','Mismo Ke entre historias: riesgo operativo se expresa en los flujos.'],['Ke terminal','=B7+B10*B8+B11','Terminal nominal COP; Ke > g.'],['Beta Regional Banks',.51,'825 firmas,enero2026; contraste, no sustituye el segmento elegido.'],['Fuente países','https://pages.stern.nyu.edu/~adamodar/pc/datasets/ctrypremJuly26.xlsx'],['Fuente TES','https://www.irc.gov.co/documents/d/guest/informe-diario-25-de-septiembre-de-2026?download=true'],['País','Cartera COPm','Peso','CRP']])
for j,(name,n,p) in enumerate(countries,18):wr(K,j,1,[[name,n,f'=B{j}/SUM($B$18:$B$23)',p]])
wr(K,25,1,[['Ajuste de combinación de negocios',-68532,'Se excluye de la asignación geográfica y se normalizan los seis saldos positivos.'],['Fuente beta','https://pages.stern.nyu.edu/adamodar/New_Home_Page/datafile/BetasGlobal.html'],['Fuente ERP','https://pages.stern.nyu.edu/~adamodar/New_Home_Page/home.htm'],['Año','Beta','Ke','Factor acumulado']])
for y in range(1,11):
 r=28+y;wr(K,r,1,[[y,f'=IF(A{r}<=5;$B$9;$B$9+($B$10-$B$9)*(A{r}-5)/5)',f'=$B$7+B{r}*$B$8+$B$11',f'=1+C{r}' if y==1 else f'=D{r-1}*(1+C{r})']])
wr(C,1,1,[['JMR · Capital completo · COP millones'],['CET1 = libro controlador + libro minoritarios − ajustes regulatorios netos. Puente inicial conciliado, sin multiplicador fijo85%.'],['Ajustes netos crecen con RWA; minoritarios retienen proporcionalmente a su participación en utilidad H126. AT1 nominal constante; Tier2 cae linealmente a cero en9años: hipótesis prudente sin refinanciación neta.'],['Dato inicial','Valor','Fuente / hipótesis','Historia','CET1 meta','Tier1 meta','Total meta','Apalancamiento meta','Shock OCI total FY1'],['CET1',17605250,'Nota10.14 H126','Base',.12,.105,.14,.05,0],['RWA',145082745,'Nota10.14 H126','Conservador',.1225,.11,.15,.055,-700000],['Libro controlador',16879747,'Estado consolidado H126','Optimista',.1175,.10,.135,.05,0],['Libro minoritarios',2476921,'Estado consolidado H126','Disrupción',.125,.115,.16,.06,-1400000],['Ajustes netos','=B7+B8-B5','No equivale solo a goodwill: concilia el agregado regulatorio.'],['AT1',1731178,'Nota10.14 H126; sin financiación incremental futura.'],['Tier2',3996219,'Nota10.14 H126; salida gradual prudente2035, no calendario contractual de cada bono.'],['Exposición apalancamiento',244806078,'Nota10.14 H126'],['Fracción utilidad minoritaria','=16,622/945,329','No se aplica la fracción minoritaria del patrimonio a la utilidad.']])
headers=['Año','RWA cierre','Exposición cierre','Ajuste neto cierre','AT1','Tier2','CET1 apertura','CET1 requerido','OCI total','Retención controlador','CET1 cierre','CET1 / RWA','Tier1 / RWA','Total / RWA','Apalancamiento','Estado / financiación','Libro controlador cierre','Libro NCI cierre','Brecha contable','OCI controlador']
scenarios=[]
for si,name in enumerate(['Base','Conservador','Optimista','Disrupcion']):
 sheet=name+'_1';sid=IDS[sheet];pr=5+si;off=55*si;cap=16+15*si;old=14+15*si;tr=6+si;mp=5+si
 wr(C,cap-1,1,[headers])
 for y in range(1,11):
  r=cap+y-1;c=chr(65+y);prev=chr(64+y); kr=28+y; mr=20+off
  rwag=f"IF(A{r}<=5;'Capital Regulatorio'!$B${7+si};'Capital Regulatorio'!$B${7+si}+('Capital Regulatorio'!$C${7+si}-'Capital Regulatorio'!$B${7+si})*(A{r}-5)/5)"
  wr(C,r,1,[[y,f'=$B$6*(1+{rwag})' if y==1 else f'=B{r-1}*(1+{rwag})',f'=$B$12*(1+\'Motor Operativo\'!{c}{23+off})' if y==1 else f'=C{r-1}*(1+\'Motor Operativo\'!{c}{23+off})',f'=$B$9*B{r}/$B$6','=$B$10',f'=$B$11*MAX(0;1-A{r}/9)','=$B$5' if y==1 else f'=K{r-1}',f'=MAX($E${pr}*B{r};$F${pr}*B{r}-E{r};$G${pr}*B{r}-E{r}-F{r}+8;$H${pr}*C{r}-E{r})',f'=$I${pr}' if y==1 else 0,f'=MAX(0;(H{r}-G{r}-I{r}+D{r}-'+('$B$9' if y==1 else f'D{r-1}')+')*(1-$B$13))',f'=G{r}+J{r}/(1-$B$13)+I{r}-D{r}+'+('$B$9' if y==1 else f'D{r-1}'),f'=K{r}/B{r}',f'=(K{r}+E{r})/B{r}',f'=(K{r}+E{r}+F{r}-8)/B{r}',f'=(K{r}+E{r})/C{r}',f'=IF({sheet}!{c}16<0;"APORTE REQUERIDO";IF(MIN(L{r}-$E${pr};M{r}-$F${pr};N{r}-$G${pr};O{r}-$H${pr})<-0,00000001;"INCUMPLE";"OK"))',f'={sheet}!{c}17',f'=$B$8+J{r}*$B$13/(1-$B$13)+I{r}*$B$13' if y==1 else f'=R{r-1}+J{r}*$B$13/(1-$B$13)+I{r}*$B$13',f'=Q{r}+R{r}-D{r}-K{r}',f'=I{r}*(1-$B$13)']])
  put(sheet,c+'15',f"='Capital completo'!J{r}")
  put(sheet,c+'17',f"={c}11+{c}15+'Capital completo'!T{r}")
  put(sheet,c+'12',f'=({c}17-{c}11)/{c}11')
  put(sheet,c+'18',f"={c}14+'Capital completo'!T{r}-'Ke sustentado'!C{kr}*{c}11")
  put(sheet,c+'19',f"='Ke sustentado'!D{kr}")
  put('Motor Operativo',c+str(25+off),f'=(('+('195575,016' if y==1 else prev+str(21+off))+f'+{c}{21+off})/2)*{c}{24+off}')
  if y==1:put('Motor Operativo',c+str(21+off),f'=195575,016*(1+{c}{23+off})')
  otherg=f'IF({c}{20+off}<=5;$H${mp};$H${mp}+($C${mp}-$H${mp})*({c}{20+off}-5)/5)'
  costg=f'IF({c}{20+off}<=5;$I${mp};$I${mp}+($C${mp}-$I${mp})*({c}{20+off}-5)/5)'
  put('Motor Operativo',c+str(28+off),f'=1420,741*2*(1+{otherg})' if y==1 else f'={prev}{28+off}*(1+{otherg})')
  put('Motor Operativo',c+str(29+off),f'=(3960,895*2-$L${mp})*(1+{costg})' if y==1 else f'={prev}{29+off}*(1+{costg})')
  put('Motor Operativo',c+str(31+off),f'=IF({c}{20+off}<=5;$J${mp};$J${mp}+(0,35-$J${mp})*({c}{20+off}-5)/5)')
  put('Motor Operativo',c+str(32+off),f'={c}{30+off}-MAX(0;{c}{30+off})*{c}{31+off}')
  # Legacy capital rows continue to point to the corrected model, preserving all existing consumers.
  rr=old+y-1
  for col,f in [('C',f"='Capital completo'!B{r}/1000"),('D',f"='Capital completo'!G{r}/1000"),('E',f"='Capital completo'!H{r}/1000"),('F',f"='Capital completo'!J{r}/1000"),('G',f"='Capital completo'!J{r}/1000"),('H',f"='Capital completo'!K{r}/1000"),('I',f"='Capital completo'!L{r}"),('L',f"='Capital completo'!P{r}")]:put('Capital Regulatorio',col+str(rr),f)
 put('Supuestos','C'+str(6+si),"='Ke sustentado'!B12")
 put(sheet,'B30','=($B$25-SUM(B21:D21))*D19')
 put('Terminal regulatorio','B'+str(tr),"='Ke sustentado'!B13")
 put('Terminal regulatorio','E'+str(tr),f"='Capital completo'!G{pr}")
 put('Terminal regulatorio','H'+str(tr),f"=('Capital completo'!B{cap+9}*E{tr}+'Capital completo'!D{cap+9})*F{tr}*(1-'Capital completo'!$B$13)")
 for col in ['H','I']:
  rr=20+si;price='F' if col=='H' else 'G'
  put('Múltiplos Banco',col+str(rr),f'={price}{rr}/{sheet}!D19+SUM({sheet}!B21:D21)*1000000/Datos!B30')
 # Independent arithmetic projection mirrors the economically specified model, not cached formulas.
 p={x:inp['Motor Operativo'][x+str(mp)]['value']['numberValue'] for x in 'BCDEFGHIJKL'}
 rwg=[.07,.06,.09,.02][si];rwend=[.04,.03,.045,.015][si];targets=[(.12,.105,.14,.05),(.1225,.11,.15,.055),(.1175,.10,.135,.05),(.125,.115,.16,.06)][si]
 book=16879747;nci=2476921;rwa=145082745;exp=244806078;adj=1751418;cet=17605250;assets=195575.016;loans=174709.257;other=1420.741*2;cost=3960.895*2-225.22;factor=1;flows=[];arr=[]
 for y in range(1,11):
  fade=max(0,y-5)/5;growth=p['B']+(p['C']-p['B'])*fade;rwag=rwg+(rwend-rwg)*fade;nim=p['D']+(p['E']-p['D'])*y/10;risk=p['F']+(p['G']-p['F'])*y/10
  prevassets=assets;assets*=1+growth;loans*=1+growth;other*=1+p['H']+(p['C']-p['H'])*fade;cost*=1+p['I']+(p['C']-p['I'])*fade;tax=p['J']+(.35-p['J'])*fade
  pbt=(prevassets+assets)/2*nim-loans*risk+other-cost;ni=(pbt-max(0,pbt)*tax)*(1-p['K'])*1000
  prevadj=adj;rwa*=1+rwag;exp*=1+growth;adj=1751418*rwa/145082745;at1=1731178;t2=3996219*max(0,1-y/9)
  need=max(targets[0]*rwa,targets[1]*rwa-at1,targets[2]*rwa-at1-t2+8,targets[3]*exp-at1);oci=[0,-700000,0,-1400000][si] if y==1 else 0
  retain=max(0,(need-cet-oci+adj-prevadj)*(1-p['K']));fcfe=ni-retain;re=ni+oci*(1-p['K'])-(rf+erp*(.7+.3*fade)+crp)*book
  cet+=retain/(1-p['K'])+oci-adj+prevadj;nci+=retain*p['K']/(1-p['K'])+oci*p['K'];book+=retain+oci*(1-p['K']);factor*=1+rf+erp*(.7+.3*fade)+crp
  flows.append(fcfe/factor);arr.append(dict(year=y,ni=ni,retain=retain,fcfe=fcfe,book=book,cet=cet,rwa=rwa,adj=adj,exposure=exp,re=re,factor=factor,nci=nci))
 ni11=ni*(1+p['C']);ret11=(targets[2]*rwa+adj)*p['C']*(1-p['K']);fcfe11=ni11-ret11;kt=rf+erp+crp;tv=0 if ni11<=0 else max(0,fcfe11)/(kt-p['C']);equity=sum(flows)+tv/factor;value=equity*1e6/487670413
 scenarios.append(dict(name=name,value=value,equity=equity,ni11=ni11,ret11=ret11,fcfe11=fcfe11,tv=tv,terminalShare=(tv/factor/equity if equity else 0),years=arr,keInitial=rf+.7*erp+crp,keTerminal=kt,g=p['C'],valueFY3=(equity-sum(flows[:3]))*arr[2]['factor']*1e6/487670413))
wr(C,80,1,[['Mínimos regulatorios verificados','CET1 con buffers7%','Tier1 con buffers8,5%','Total con buffers11,5%','Apalancamiento3%'],['Las metas de historias son buffers del analista, no política anunciada por el banco. OCI0 Base/Optimista; shocks únicos −0,7/−1,4 billones Cons/Dis. No se espera OCI cero por certeza.'],['Pérdidas y aporte: FCFE negativo incluye recapitalización a cargo del accionista. No es dividendo negativo legal. Deterioro persistente termina en valor de continuidad cero, sin inventar liquidación.'],['AT1/Tier2: las condiciones contractuales son diversas; la salida lineal agregada es una hipótesis de suficiencia de capital y se somete a estrés, no una transcripción de vencimientos.'],['Fuente','https://ir.davivienda.com/wp-content/uploads/2026/08/Banco-Davivienda-EEFF-Consolidados-2T26-2.pdf']])
put('Capital Regulatorio','C4',"=1-'Capital completo'!B13")
put('Capital Regulatorio','C3','Participación controlador en utilidad; NO factor NIIF→CET1')
put('Capital Regulatorio','A2','Modelo vigente: Capital completo. Se reemplazó el factor85% por puente explícito, cuatro controles y trayectoria AT1/Tier2.')
put('Ke Colombia','A1','KE COLOMBIA · Modelo vigente en Ke sustentado')
put('Ke Colombia','A2','Insumos antiguos reemplazados: ver Ke sustentado para fuentes y fórmulas actualizadas.')
for r in range(6,10):put('Ke Colombia','F'+str(r),"='Ke sustentado'!B12")
put('Terminal regulatorio','A3','FCFE11 = NI10×(1+g) − (meta total×RWA10 + ajuste neto10)×g×fracción beneficio controlador. Tier2=0; AT1 constante, cuatro restricciones verificadas.')
put('Terminal regulatorio','A2','Ingresos, gasto, cartera y RWA convergen a g enFY10; NIM, deterioro y fiscalidad estabilizados. Perpetuidad coherente desdeFY11; libro y ROE convergen a estado estable.')
put('Motor Operativo','A2','Activos productivos proxy cierre H126195.575,016COPbn; NIM aplicado al promedio apertura/cierre. Deterioro agregado publicado, no pérdida puramente de cartera; costes de integración no eliminados; impuesto patrimonial anual mantenido.')
put('Resumen','A1','JMR · PFDAVVNDA · Valoración revisada Damodaran ·09-oct-2026')
put('Resumen','A3','FCFE potencial tras capital regulatorio; pago legal sujeto a reservas y aprobación. Preferencia COP161,30 solo sobre utilidad distribuible; no flujo garantizado ni adicional.')
for r in range(6,10):put('Terminal regulatorio','R'+str(r),'Meta total vinculante tras salida de Tier2; todas las masas operativas crecen al mismo g.')
# Rebuild the 100-year mathematical terminal test under the corrected capital bridge.
for n in range(1,101):
 r=n+5;put('Convergencia terminal','C'+str(r),f"='Terminal regulatorio'!$H$6*(1+'Terminal regulatorio'!$F$6)^{n-1}")
put('Convergencia terminal','A2','Prueba independiente: cien años con NI y retención sostenible creciendo g; mismo Ke terminal, sin factor85%.')
# Reconstruct historical market ratios from official preferred prices, shares and controlling equity.
wr(H,1,1,[['JMR · Tres anclas de múltiplos independientes'],['Historia propia 5FY verificables; no se presenta como10años. Precio preferencial/beneficio controlador por acción; no se llama capitalización de todas las clases.'],['P/B ancla:50% historia +25% comparable ajustado +25% justificado. P/E:70% historia +0% peer +30% justificado; PER peer UDM excluido por perímetro discontinuado.'],['FY','Precio PF COP','Acciones','Libro controlador COPm','NI controlador COPm','P/B','P/E','Fuente precio / financiero']])
prices=[31800,27560,19180,17560,24820];shares=[451670413]*3+[487670413]*2;books=[14114030,16089689,14565906,15938311,16264321];profits=[None,None,-395700,-115975,1522055]
for i in range(5):
 r=5+i;wr(H,r,1,[[2021+i,prices[i],shares[i],books[i],profits[i],f'=B{r}*C{r}/(D{r}*1000000)',('=31800/(2792-22*1000000000/451670413)' if i==0 else '=27560/(3578-23*1000000000/451670413)' if i==1 else None if i in [2,3] else f'=B{r}*C{r}/(E{r}*1000000)'),['IR4T22:EPS total menos NCI22COPbn; NCI redondeado, contraste','IR4T22:EPS total menos NCI23COPbn; NCI redondeado, contraste','IR4T24; EEFF2023','IR4T24; EEFF auditados2025 con comparativo2024','IR4T25 precio; EEFF auditados2025 NI y patrimonio'][i]]])
wr(H,11,1,[['Mediana histórica P/B','=MEDIAN(F5:F9)'],['Mediana histórica P/E positivo','=MEDIAN(G5:G9)'],['Banco Bogotá precio marcación COP',38320,'Referencia08-oct-2026 GrupoAval, no precio en vivo'],['Banco Bogotá acciones verificadas',355251068,'Nota15.3 /16.3 H126 emisor'],['Banco Bogotá libro controlador COPm',14797672,'EEFF consolidado H126 emisor, copia FinancialFilings'],['Banco Bogotá NI semestre COPm',702999,'EEFFH126; H1 incluía resultado discontinuado, proxy anual2×H126 solo contraste'],['P/B peer observado','=B13*B14/(B15*1000000)'],['ROE peer proxy apertura cierre medio','=2*B16/AVERAGE(B15;17231192)','No UDM pro forma, base semestre nuevo perímetro'],['ROE propio estable',"='Terminal regulatorio'!G6*'Terminal regulatorio'!F6/'Terminal regulatorio'!H6",'Límite de régimen consistente con capital, no ROE transitorioFY11'],['P/B peer ajustado ROE','=B17*B19/B18','Escala relativa ROE propio/ROEpeer; mismo g y Ke como proxy, riesgo residual difiere.'],['P/B justificado',"=(B19-'Terminal regulatorio'!F6)/('Ke sustentado'!B13-'Terminal regulatorio'!F6)",'Damodaran (ROE−g)/(Ke−g), régimen estable. No se deriva del valorDCF.'],['P/E justificado',"=(1-'Terminal regulatorio'!F6/B19)/('Ke sustentado'!B13-'Terminal regulatorio'!F6)",'Payout/ (Ke−g). Una observación matemática del mismo régimen; P/B y PER no evidencias independientes.'],['Ancla P/B','=0,5*B11+0,25*B20+0,25*B21'],['Ancla P/E','=0,7*B12+0,3*B22'],['Fuente peer','https://financialfilings.com/filings/banco-de-bogota-sa/interim-quarterly-report/2026/56572004/'],['Fuente IR4T22','https://ir.davivienda.com/wp-content/uploads/2023/02/Informe-de-Resultados-Financieros-Davivienda-4T22..pdf'],['Fuente IR4T24','https://ir.davivienda.com/wp-content/uploads/2025/02/Informe-de-Resultados-Davivienda-4T24.pdf'],['Fuente IR4T25','https://ir.davivienda.com/wp-content/uploads/2026/03/Informe-de-Resultados-Banco-Davivienda-4T25.pdf'],['Fuente estados2025','https://ir.davivienda.com/wp-content/uploads/2026/03/Estados_Financieros_Consolidados_2025_-Banco-Davivienda_-Final.pdf']])
for i in range(5):
 put('Pares Históricos','B'+str(i+4),f"='Anclas verificadas'!F{i+5}");put('Pares Históricos','C'+str(i+4),f"='Anclas verificadas'!G{i+5}" if i not in [2,3] else None)
 put('Verificación documental','B'+str(i+36),f"='Anclas verificadas'!B{i+5}*'Anclas verificadas'!C{i+5}/1000000")
 put('Verificación documental','G'+str(i+36),'Precio PF y acciones oficiales; ratio por acción controlador, no capitalización multiclase.')
put('Verificación documental','B48',355251068)
put('Pares Históricos','B21',"='Anclas verificadas'!B23");put('Pares Históricos','C21',"='Anclas verificadas'!B24")
put('Pares Históricos','D21','Ver Anclas verificadas: historia +peer corregido por ROE +justificado; PERpeer excluido por cambios de perímetro.')
put('Pares Históricos','B19',.5);put('Pares Históricos','C19',.7);put('Pares Históricos','B20',.25);put('Pares Históricos','C20',0)
put('Pares Históricos','A18','Pesos adicionales justificado: P/B25%; P/E30%; peer directo único, no mediana de muchos pares.')
put('Múltiplos Banco','A6','Precio congelado de referencia08-oct-2026; no cotización actual')
put('Múltiplos Banco','D6','Grupo Aval marcación,31.900Investing excluido por posible rutaGroup. Identidad Banco PFDAVVNDA.')
# Correct sensitivity table: all Ke vary by a parallel shift, g changes sustainable terminal flows.
for row,shift in zip(range(5,10),[-.02,-.01,0,.01,.02]):
 put('Sensibilidad Damodaran','A'+str(row),f"='Ke sustentado'!B13+"+str(shift).replace('.',','))
 for col in 'BCDE':
  denom=f"(1+'Ke sustentado'!$C$29+$A{row}-'Ke sustentado'!$B$13)"
  terms=[]
  for y in range(1,11):
   cc=chr(65+y);discount='*'.join(f"(1+'Ke sustentado'!$C${28+k}+$A{row}-'Ke sustentado'!$B$13)" for k in range(1,y+1));terms.append(f'Base_1!{cc}16/({discount})')
  ret=f"('Capital completo'!$B$25*'Capital completo'!$G$5+'Capital completo'!$D$25)*{col}$4*(1-'Capital completo'!$B$13)"
  put('Sensibilidad Damodaran',col+str(row),'=('+ '+'.join(terms)+f'+(Base_1!$K$14*(1+{col}$4)-{ret})/($A{row}-{col}$4)/('+discount+'))*1000000/Datos!B30')
put('Sensibilidad Damodaran','A2','Ke terminal ±1/2pp con desplazamiento paralelo de toda la curva; crecimiento terminal2/3/4/5%.')
put('Sensibilidad Damodaran','A12','Modelo anterior archivado; resultados siguientes sustituidos por sensibilidades reproducidas en informe.')
for r in range(13,29):wr(IDS['Sensibilidad Damodaran'],r,1,[[None]*8])
(P/'completar_adds.json').write_text(json.dumps(adds))
(P/'completar_requests.json').write_text(json.dumps(req))
(P/'resultados_finales.json').write_text(json.dumps({'rf':rf,'erp':erp,'crp':crp,'scenarios':scenarios,'expected':sum(w*max(0,s['value']) for w,s in zip([.5,.25,.15,.1],scenarios))},indent=2))
print(json.dumps({'requests':len(req),'newSheets':3,'rf':rf,'crp':crp,'values':[(s['name'],s['value'],s['valueFY3']) for s in scenarios]},indent=2))
