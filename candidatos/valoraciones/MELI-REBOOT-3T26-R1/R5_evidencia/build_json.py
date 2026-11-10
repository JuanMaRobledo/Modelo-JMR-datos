import json,re,subprocess,os,sys
from datos import *
from n1 import n1,vb,vc,vo,px,mos_price
from n2 import n2
ROOT='/home/user/Modelo-JMR-datos'
REV_ID='MELI-REBOOT-3T26-R1'
IDS=dict(h='15Z4mnTqLAm05V0svSMbKS1jZB9VEMKRwCO6z4GwvyPI',b='174iyMLVgEsIw8sAWHNF3_SAvcbOoZbb1dB94gUF5yLc',c='1RYE2kFcPstfBAH2eTRkyiMwvw64XuOcgnofD9Jq8jPM',o='1fdZBeu5c4Agd54piuip2jnLL8HxM2yUbGOkGUKjgjd4',m='19jUYjQ-KXnLUjvQBXzTJhIRHJgxN79BdOfoqdB7REJk')
mode=sys.argv[1]; DOC=sys.argv[2] if len(sys.argv)>2 else 'PENDIENTE'
if mode=='html':
    html=n1()+n2().replace('__DOC__','Este documento (sexto archivo de la revisión)')
    open(sys.argv[2],'w').write('<!doctype html><html><head><meta charset="utf-8"><title>MELI-REBOOT-3T26-R1 · 04 ANÁLISIS</title></head><body>'+html+'</body></html>');print('html ok');sys.exit()
sh=lambda i:f'https://docs.google.com/spreadsheets/d/{i}/edit'
LIB={'historicos':sh(IDS['h']),'dcf':{'base':sh(IDS['b']),'conservadora':sh(IDS['c']),'optimista':sh(IDS['o'])},'multiplos':sh(IDS['m']),'analisis':f'https://docs.google.com/document/d/{DOC}/edit'}
P_={'base':dict(g1=.30,cagr=.19,m=.135,s1=3.2,s2=3.0,roic=.14),'cons':dict(g1=.22,cagr=.11,m=.09,s1=2.5,s2=2.3,roic=WACC_T),'opt':dict(g1=.36,cagr=.23,m=.165,s1=3.8,s2=3.4,roic=.164)}
def hist(id_,nombre,k,prob):
    st=ST[k];q=P_[k]
    return dict(id=id_,nombre=nombre,historia=nombre,probabilidad=prob,crecimiento=(st['rev'][5]/st['rev'][0])**(1/5)-1,margen=q['m'],salesToCapital=q['s1'],salesToCapital2=q['s2'],roicTerminal=q['roic'],
      valor=st['value'],terminalGrowth=0.04,estado='LISTO',incluidaEnPromedio=True,pesoEnPromedio=prob,s2c=q['s1'],s2c610=q['s2'],crecimientoAnio1=q['g1'],cagr25=q['cagr'],probabilidadFracaso=0)
H=[hist('A','Base','base',.5),hist('B','Conservadora','cons',.25),hist('C','Optimista','opt',.25)]
GL=[0.15,0.17,0.19,0.21,0.23];ML=[0.105,0.12,0.135,0.15,0.165];DW=[-0.01,-0.005,0,0.005,0.01];TG=[0.03,0.035,0.04,0.045,0.048]
MA=[[SENS[f'a_{i}_{j}'] for j in range(5)] for i in range(5)];MB=[[SENS[f'b_{i}_{j}'] for j in range(5)] for i in range(5)]
SHEETS={'EV/EBITDA':'EVEBITDA','EV/FCFF':'EVFCFF','P/E':'PE','P/FCFE':'PFCFE','P/OCF':'POCF'}
mm=[]
for m in MET:
    mt=MATRICES_M[m];V=matriz_vp(m)
    mm.append(dict(metodo=m,escenario='base',estado='OK',peso=PESO[m],ancla='JMR',origen=f"'{SHEETS[m]}'!A46:F51",matriz=V,fundamentalFY3=mt['col'],multiploElegido=mt['fila'],centro=V[2][2],vp3Original=VPM['base'][m][2],
      precioFY3SinDescontar=mt['val'][2][2],unidadFundamental=mt['unidad'],derivacion='celda = precio FY+3 × factor de descuento 3 años (Ke Base); sin dividendos; centro = VP3 Base de Descuento de múltiplos'))
def mdet(m):
    d={n:dict(objetivo=OBJ[k][m],vp=VPM[k][m],consolidado=CONS[k][m]) for k,n in (('cons','conservador'),('base','base'),('opt','optimista'))}
    return dict(nombre=m,peso=PESO[m],estado='OK',**d)
metodos=[dict(nombre='DCF Damodaran',peso=.75,conservador=vc,base=vb,optimista=vo)]+[dict(nombre=m,peso=PESO[m],conservador=CONS['cons'][m],base=CONS['base'][m],optimista=CONS['opt'][m]) for m in MET]
SALV=['Auditoría económica independiente (R6) no realizada: el estado EN_REVISION no certifica el criterio económico.',
 'Verificación documental de la serie histórica contra los 10-K/10-Q pendiente (insumo: SEC XBRL); filas de verificación del libro de Múltiplos en «PENDIENTE».',
 'El fondeo del crédito (≈10.800 M de préstamos, certificados y deuda colateralizada) se trata como pasivo operativo y no se resta como deuda, porque el EBIT ya descuenta su costo; solo se resta la deuda corporativa (2.369 M). Cambia lo acordado en R1. Si se restara todo (13.190 M) el valor bajaría unos 213 por acción pero con doble cuenta del costo de fondeo.',
 'Valor muy por encima del precio: el precio (1.510) queda por debajo de todas las celdas de las matrices; implica 9,6 % de crecimiento o 8,4 % de margen. Los supuestos de margen y de ventas/capital de la Base son favorables y no se prueban con el historial (margen contable en caída desde 2023, provisión creciente).',
 'Beta bottom-up 0,93 con mapeo de industrias propio (fintech → Information Services); con beta directa 1,30 el DCF Base sería 2.289,61. ERP por país con reparto supuesto de «otros países».',
 'EV/FCFF sin ancla histórica (30/35/40x son juicio) y P/FCFE, P/OCF con flujo operativo distorsionado por fondos de clientes y fondeo; sus pesos son mínimos (3 %, 1,5 %, 1,5 %).',
 'Caja de 8.126 M según la definición de MELI (efectivo, inversiones y activos digitales disponibles); el efectivo restringido (14.559) y los fondos de clientes (17.400) quedan fuera del puente. Arrendamientos (2.964 M) no se restan como deuda por decisión del usuario.',
 'Costo de la deuda (6,90 %) estimado; participación de mercado y calidad de la cartera N/D; gobierno corporativo no analizado. Ceros por dato no separable en el libro de Múltiplos (deuda corporativa FY2016–FY2024, cuentas por pagar, ingresos diferidos < 2023).',
 'Integridad de fórmulas y comentarios del motor fcffsimpleginzu no re-verificada en las copias de MELI. Matrices 5×5 de múltiplos derivadas de las hojas de método (precio FY+3 descontado con el Ke Base).']
rec=dict(ticker='MELI',revisionId=REV_ID,revision_id=REV_ID,sheet_id=IDS['b'],estado='EN_REVISION',publicationStatus='EN_REVISION',perfil_valoracion='Floyd',metodo_valoracion='A',version_metodo='Floyd',
 fecha_corte='2026-11-06',fechaCorteContable='2026-09-30',valorPrincipal=vb,precioMOS=vb*(1-MOS),baseMOS='dcfBase',hojaGoogle=LIB['dcf']['base'],nombreActivo='MercadoLibre, Inc.',market='NASDAQ',moneda='USD',
 precio=PREC,precioReferenciaFecha='2026-11-06',mos=MOS,metodoPrincipal='DCF FCFF Base 10 años',
 escenariosDCF=dict(version='Floyd',revisionId=REV_ID,fecha='2026-11-06',central='A',principal='DCF Base',historias=H),
 valorEsperado=dict(valor=EXPECTED,dcfBase=vb,historiaCentralId='A',disrupcionEnPromedio=False,historias=H,escenariosUnificados=dict(conservador=vc,base=vb,optimista=vo),escenariosPromedio=3,rango=dict(minimo=vc,maximo=vo)),
 sensibilidadDCF=dict(centro=vb,centroConciliado=True,matrices=[
   dict(nombre='CAGR años 2–5 × margen operativo objetivo ajustado',ejeFilas=GL,ejeColumnas=ML,valores=MA,centro=MA[2][2],centroConciliado=True,origen="'Sensibilidades DCF'!A5:F10"),
   dict(nombre='Costo de capital inicial × crecimiento terminal',ejeFilas=[WACC0+d for d in DW],ejeColumnas=TG,valores=MB,centro=MB[2][2],centroConciliado=True,origen="'Sensibilidades DCF'!A13:F18")]),
 sensibilidadMultiples=dict(contrato='reboot-atlas-cinco-v1',revisionId=REV_ID,sourceSheetId=IDS['m'],estadoPublicacion='INTEGRADO_EN_REVISION',controlesTecnicosAprobados=True,certificado=False,matrices=mm,
   resultadosSha256='0'*64,resultadosHashMetodo='SHA256 UTF8 JSON.stringify(sensibilidadMultiples.matrices)'),
 metodos=metodos,
 descuentoMultiples=dict(version=3,costoPatrimonio=KE,criterio='Ponderado FY+1–FY+3 (20/30/50 %)',horizontes=[1,2,3],pesoDcf=.75,pesoMultiplos=.25,dcfHoy=dict(conservador=vc,base=vb,optimista=vo),
   multiplesHoy=dict(conservador=MULT['cons'],base=MULT['base'],optimista=MULT['opt']),ponderadoHoy=dict(conservador=COMB['cons'],base=COMB['base'],optimista=COMB['opt']),metodos=[mdet(m) for m in MET],tipoEmpresa='Crecimiento'),
 dcfInverso=dict(precio=PREC,replicaBase=vb,
   crecimientoBaseFijo=dict(cagr5=SENS['crecimiento'],margenObjetivo=.135,valor=PREC,descripcion='Crecimiento anual años 1–5 que iguala el precio con el margen de la Base'),
   margenBaseFijo=dict(cagr5=.19,margenObjetivo=SENS['margen'],valor=PREC,descripcion='Margen objetivo ajustado que iguala el precio con el crecimiento de la Base'),
   crecimientoMargen135=dict(cagr5=SENS['crec_con_margen16'],margenObjetivo=.135,valor=PREC),
   waccInicial=dict(alcanzable=True,valor=SENS['wacc'],valorResultado=PREC),constantes=dict(g=.04,w=WACC0,wTerminal=WACC_T,roic=.14)),
 puente=dict(operativo=ST['base']['op_assets'],deuda=2369,minoritarios=0,caja=8126,noOperativos=0,opciones=0,accionesMillones=50.696802),
 tasas=dict(wacc=WACC0,waccTerminal=WACC_T,ke=KE,fuenteWacc='Cost of capital worksheet (DCF Base): Rf 4,86 % (FRED DGS10, 6-nov-2026), beta bottom-up 0,93 (Retail (General) e Information Services por ingresos), ERP por país 7,56 % (madura 3,387 %, Damodaran nov-2026), Kd 6,90 %'),
 fecha='2026-11-06',fechaPublicacion='2026-11-10',auditPendingUserVisualReview=True,auditoriaEconomica='NO_REALIZADA',salvedades=SALV,
 controlPublicacion=dict(dcfBaseConcilia=True,probabilidadesSuman1=True,centrosDcfVerificados=3,centrosMultiplesVerificados=5,perfil='Floyd',revisionId=REV_ID,fechaComprobacion='2026-11-10',
   replicaIndependiente='Base 2536,95; Conservadora 908,33; Optimista 4120,94 (LibreOffice sobre fcffsimpleginzu original; diferencia < 1e-4 con la hoja)',
   integridadMotor='NO re-verificada en las copias de MELI',visorEndToEnd='QA_BROWSER_VISUAL_SIN_REALIZAR',auditoriaEconomicaRealizada=False,ciMotor='por ejecutar en PR',revisionAnterior='ninguna (MELI no tenía revisión activa)'),
 libros=LIB,contratoLibros='jmr-reboot-3libros-v1')
N1=n1();N2=n2().replace('__DOC__',f'https://docs.google.com/document/d/{DOC}/edit')
rp=f'{ROOT}/valoraciones/{REV_ID}.json'
json.dump(rec,open(rp,'w'),ensure_ascii=False,indent=1)
sha=subprocess.check_output(['node','-e',"const c=require('crypto'),f=require('fs');const r=JSON.parse(f.readFileSync(process.argv[1],'utf8'));console.log(c.createHash('sha256').update(JSON.stringify(r.sensibilidadMultiples.matrices),'utf8').digest('hex'))",rp]).decode().strip()
rec['sensibilidadMultiples']['resultadosSha256']=sha;json.dump(rec,open(rp,'w'),ensure_ascii=False,indent=1)
words=lambda s:len(re.sub('<[^>]+>',' ',s).split())
ana=dict(id=f'MELI-research-{REV_ID}',title='MELI | MercadoLibre — Análisis JMR Floyd R1–R6 3T-2026',ticker='MELI',company='MercadoLibre, Inc.',revisionId=REV_ID,valuationRevisionId=REV_ID,version_metodo='Floyd',
 perfil_valoracion='Floyd',estado='EN_REVISION',publicationStatus='EN_REVISION',sheet_id=IDS['b'],price=PREC,financialCutoff='2026-09-30',valorPrincipal=vb,precioMOS=vb*(1-MOS),articleHtml=N1,calculationHtml=N2,
 documentos=dict(nivel1=LIB['analisis'],nivel2=LIB['analisis']),linkedValuation=dict(revisionId=REV_ID,valorPrincipal=vb,sourcePath=f'valoraciones/{REV_ID}.json',estado='EN_REVISION'),salvedades=SALV,status='EN_REVISION',
 date='2026-11-10',remotePath=f'analisis/MELI-research-{REV_ID}.json',
 controlCobertura=dict(secciones=14,escenariosDCF=3,centrosDCFValidados=3,centrosMultiplesValidados=5,nivel1=True,nivel2=True,auditoriaEconomicaIndependiente=False,palabrasNivel1=words(N1),nivel2Apartados=12),html=N1+N2)
json.dump(ana,open(f'{ROOT}/analisis/MELI-research-{REV_ID}.json','w'),ensure_ascii=False,indent=1)
print('ok',sha,words(N1),words(N2))
