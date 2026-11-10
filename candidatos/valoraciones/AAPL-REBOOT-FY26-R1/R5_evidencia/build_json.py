import json,re,subprocess,os
from datos import *
from n1 import n1,vb,vc,vo,px,mos_price
from n2 import n2
ROOT='/home/user/Modelo-JMR-datos'
REV_ID='AAPL-REBOOT-FY26-R1'
IDS=dict(h='1b1G1RciCJYH-J-RLXZhQX90RBlEZ-GY4qi13vSOdxEs',b='1FDKimjBtpWeJO1wjK2-iFbQBhc7fziRWspCqkl41am8',c='1z7399gpLt0t0IMTgvXav4u6tEEsCIevd-GSE1U7KMcM',o='18_DpC1IBerZBKzBpWWkSi-9h4EzXH_fIlesGqmeKffM',m='1SJn1NC6zGAWvMPOS6yK-0TxheNlZ0oabBPX8yaqpXmg')
DOC='1CxPNSRM5GcV0UvMgxiaByM5xOQ55b1peHqMOT_c8n60'
sh=lambda i:f'https://docs.google.com/spreadsheets/d/{i}/edit'
LIB={'historicos':sh(IDS['h']),'dcf':{'base':sh(IDS['b']),'conservadora':sh(IDS['c']),'optimista':sh(IDS['o'])},'multiplos':sh(IDS['m']),'analisis':f'https://docs.google.com/document/d/{DOC}/edit'}
b,c,o=ST['base'],ST['cons'],ST['opt']
def cagr5(st): return (st['rev'][6]/st['rev'][1])**(1/5)-1 if False else (st['rev'][5]/st['rev'][0])**(1/5)-1
def hist(id_,nombre,k,prob,roic,s2c):
    st=ST[k]
    return dict(id=id_,nombre=nombre,historia=nombre,probabilidad=prob,crecimiento=cagr5(st),margen={'base':.37,'cons':.31,'opt':.40}[k],
      salesToCapital=s2c,salesToCapital2=s2c,roicTerminal=roic,valor=st['value'],terminalGrowth=0.04,estado='LISTO',incluidaEnPromedio=True,pesoEnPromedio=prob,s2c=s2c,s2c610=s2c,
      crecimientoAnio1={'base':.06,'cons':.025,'opt':.09}[k],cagr25={'base':.055,'cons':.02,'opt':.08}[k],probabilidadFracaso=0.05 if k=='cons' else 0)
H=[hist('A','Base','base',.5,.4476,3.0),hist('B','Conservadora','cons',.25,WACC_T,2.4),hist('C','Optimista','opt',.25,.4476,3.5)]
GL=[0.035,0.045,0.055,0.065,0.075];ML=[0.33,0.35,0.37,0.39,0.41];DW=[-0.01,-0.005,0,0.005,0.01];TG=[0.03,0.035,0.04,0.045,0.048]
MA=[[SENS[f'a_{i}_{j}'] for j in range(5)] for i in range(5)]
MB=[[SENS[f'b_{i}_{j}'] for j in range(5)] for i in range(5)]
SHEETS={'EV/EBITDA':'EVEBITDA','EV/FCFF':'EVFCFF','P/E':'PE','P/FCFE':'PFCFE','P/OCF':'POCF'}
mm=[]
for m in MET:
    mt=MATRICES_M[m];V=matriz_vp(m)
    mm.append(dict(metodo=m,escenario='base',estado='OK',peso=PESO[m],ancla='JMR',origen=f"'{SHEETS[m]}'!A46:F51",matriz=V,fundamentalFY3=mt['col'],multiploElegido=mt['fila'],
      centro=V[2][2],vp3Original=VPM['base'][m][2],precioFY3SinDescontar=mt['val'],unidadFundamental=mt['unidad'],
      derivacion='celda = precio FY+3 × factor de descuento 3 años (Ke Base) + VP de dividendos del método; centro = VP3 Base de Descuento de múltiplos'))
def mdet(m):
    d={}
    for k,n in (('cons','conservador'),('base','base'),('opt','optimista')):
        d[n]=dict(objetivo=OBJ[k][m],vp=VPM[k][m],consolidado=CONS[k][m])
    return dict(nombre=m,peso=PESO[m],estado='OK',**d)
metodos=[dict(nombre='DCF Damodaran',peso=.65,conservador=vc,base=vb,optimista=vo)]+[dict(nombre=m,peso=PESO[m],conservador=CONS['cons'][m],base=CONS['base'][m],optimista=CONS['opt'][m]) for m in MET]
rec=dict(ticker='AAPL',revisionId=REV_ID,revision_id=REV_ID,sheet_id=IDS['b'],estado='EN_REVISION',publicationStatus='EN_REVISION',perfil_valoracion='Reboot',
 metodo_valoracion='A',version_metodo='Reboot',fecha_corte='2026-11-06',fechaCorteContable='2026-09-26',valorPrincipal=vb,precioMOS=vb*(1-MOS),baseMOS='dcfBase',hojaGoogle=LIB['dcf']['base'],
 nombreActivo='Apple Inc.',market='NASDAQ',moneda='USD',precio=PREC,precioReferenciaFecha='2026-11-06',mos=MOS,metodoPrincipal='DCF FCFF Base 10 años',
 escenariosDCF=dict(version='Reboot',revisionId=REV_ID,fecha='2026-11-06',central='A',principal='DCF Base',historias=H),
 valorEsperado=dict(valor=EXPECTED,dcfBase=vb,historiaCentralId='A',disrupcionEnPromedio=False,historias=H,
   escenariosUnificados=dict(conservador=vc,base=vb,optimista=vo),escenariosPromedio=3,rango=dict(minimo=vc,maximo=vo)),
 sensibilidadDCF=dict(centro=vb,centroConciliado=True,matrices=[
   dict(nombre='CAGR años 2–5 × margen operativo objetivo',ejeFilas=GL,ejeColumnas=ML,valores=MA,centro=MA[2][2],centroConciliado=True,origen="'Sensibilidades DCF'!A5:F10"),
   dict(nombre='WACC inicial × crecimiento terminal',ejeFilas=[WACC0+d for d in DW],ejeColumnas=TG,valores=MB,centro=MB[2][2],centroConciliado=True,origen="'Sensibilidades DCF'!A13:F18")]),
 sensibilidadMultiples=dict(contrato='reboot-atlas-cinco-v1',revisionId=REV_ID,sourceSheetId=IDS['m'],estadoPublicacion='INTEGRADO_EN_REVISION',controlesTecnicosAprobados=True,certificado=False,matrices=mm,
   resultadosSha256='0'*64,resultadosHashMetodo='SHA256 UTF8 JSON.stringify(sensibilidadMultiples.matrices)'),
 metodos=metodos,
 descuentoMultiples=dict(version=3,costoPatrimonio=KE,criterio='Ponderado FY+1–FY+3 (20/30/50 %)',horizontes=[1,2,3],pesoDcf=.65,pesoMultiplos=.35,
   dcfHoy=dict(conservador=vc,base=vb,optimista=vo),multiplesHoy=dict(conservador=MULT['cons'],base=MULT['base'],optimista=MULT['opt']),
   ponderadoHoy=dict(conservador=COMB['cons'],base=COMB['base'],optimista=COMB['opt']),metodos=[mdet(m) for m in MET],tipoEmpresa='Madura'),
 dcfInverso=dict(precio=PREC,replicaBase=vb,
   crecimientoBaseFijo=dict(cagr5=REV['crecimiento'],margenObjetivo=.37,valor=PREC,descripcion='CAGR años 1–5 que iguala el precio con el margen de la Base'),
   margenBaseFijo=dict(cagr5=.055,margenObjetivo=REV['margen'],valor=PREC,descripcion='Margen objetivo que iguala el precio con el crecimiento de la Base'),
   crecimientoMargen40=dict(cagr5=REV['crec_con_margen40'],margenObjetivo=.40,valor=PREC),
   waccInicial=dict(alcanzable=False,minimoProbado=SENS['wacc_inverso'],valorEnMinimo=282.29),
   constantes=dict(g=.04,w=WACC0,wTerminal=WACC_T,roic=.4476)),
 puente=dict(operativo=b['op_assets'],deuda=94479,minoritarios=0,caja=136935,noOperativos=0,opciones=0,accionesMillones=14590.6),
 tasas=dict(wacc=WACC0,waccTerminal=WACC_T,ke=KE,fuenteWacc='Cost of capital worksheet (DCF Base): Rf 4,86 % (FRED DGS10, 6-nov-2026), beta 1,2988, ERP regiones 4,2301 %, ERP madura 3,387 % (Damodaran nov-2026)'),
 fecha='2026-11-06',fechaPublicacion='2026-11-09',auditPendingUserVisualReview=True,auditoriaEconomica='NO_REALIZADA',
 salvedades=['Auditoría económica independiente (R6) no realizada: el estado EN_REVISION no certifica el criterio económico.',
  'Gasto por intereses ESTIMADO (3.000 FY2026; 3.500 FY2025; 3.700 FY2024): Apple ya no lo divulga; afecta el costo de la deuda y la compuerta de M, no el DCF.',
  'Verificación documental de FY2017–FY2023 pendiente (FY2024–LTM verificados contra el 10-K).',
  'Participación de mercado N/D: no hay TAM homogéneo y confiable; el crecimiento se ata a los ingresos reportados y a la mezcla de Servicios.',
  'Pagos de Google por búsqueda (del orden de 20.000 M anuales) no verificados con fuente primaria en esta revisión.',
  'Gobierno corporativo y compensación de la dirección no analizados.',
  'Matrices 5×5 de múltiplos derivadas de las hojas de método (precio FY+3 descontado con el Ke Base); la hoja conserva el precio FY+3 sin descontar.'],
 controlPublicacion=dict(dcfBaseConcilia=True,probabilidadesSuman1=True,centrosDcfVerificados=3,centrosMultiplesVerificados=5,perfil='Reboot',revisionId=REV_ID,fechaComprobacion='2026-11-09',
   replicaIndependiente='Base 209,57615; Conservadora 106,91602; Optimista 260,44561 (LibreOffice sobre fcffsimpleginzu original; diferencia < 1e-6 con la hoja)',
   integridadMotor='1.230 fórmulas y 76 comentarios sin cambios; 5 celdas de entrada con valor en vez de fórmula',
   visorEndToEnd='QA_BROWSER_VISUAL_SIN_REALIZAR',auditoriaEconomicaRealizada=False,ciMotor='por ejecutar en PR',ciApp='pruebas locales: 191/194 con 3 fallos previos ajenos al cambio'),
 libros=LIB,contratoLibros='jmr-reboot-3libros-v1')
N1=n1();N2=n2()
rec_path=f'{ROOT}/valoraciones/{REV_ID}.json'
json.dump(rec,open(rec_path,'w'),ensure_ascii=False,indent=1)
sha=subprocess.check_output(['node','-e',"const c=require('crypto'),f=require('fs');const r=JSON.parse(f.readFileSync(process.argv[1],'utf8'));console.log(c.createHash('sha256').update(JSON.stringify(r.sensibilidadMultiples.matrices),'utf8').digest('hex'))",rec_path]).decode().strip()
rec['sensibilidadMultiples']['resultadosSha256']=sha
json.dump(rec,open(rec_path,'w'),ensure_ascii=False,indent=1)
words=lambda s:len(re.sub('<[^>]+>',' ',s).split())
ana=dict(id=f'AAPL-research-{REV_ID}',title='AAPL | Apple Inc. — Análisis JMR Reboot FY2026',ticker='AAPL',company='Apple Inc.',revisionId=REV_ID,valuationRevisionId=REV_ID,version_metodo='Reboot',
 perfil_valoracion='Reboot',estado='EN_REVISION',publicationStatus='EN_REVISION',sheet_id=IDS['b'],price=PREC,financialCutoff='2026-09-26',valorPrincipal=vb,precioMOS=vb*(1-MOS),
 articleHtml=N1,calculationHtml=N2,documentos=dict(nivel1=LIB['analisis'],nivel2=LIB['analisis']),
 linkedValuation=dict(revisionId=REV_ID,valorPrincipal=vb,sourcePath=f'valoraciones/{REV_ID}.json',estado='EN_REVISION'),salvedades=rec['salvedades'],status='EN_REVISION',date='2026-11-09',
 remotePath=f'analisis/AAPL-research-{REV_ID}.json',
 controlCobertura=dict(secciones=14,escenariosDCF=3,centrosDCFValidados=3,centrosMultiplesValidados=5,nivel1=True,nivel2=True,auditoriaEconomicaIndependiente=False,palabrasNivel1=words(N1),nivel2Apartados=12),
 html=N1+N2)
json.dump(ana,open(f'{ROOT}/analisis/AAPL-research-{REV_ID}.json','w'),ensure_ascii=False,indent=1)
open(f'{os.path.dirname(os.path.abspath(__file__))}/N1.html','w').write(N1);open(f'{os.path.dirname(os.path.abspath(__file__))}/N2.html','w').write(N2)
print('ok',sha,words(N1),words(N2))
