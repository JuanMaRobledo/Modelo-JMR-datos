import json,re,subprocess,os,sys
from datos import *
from n1 import n1,vb,vc,vo,px,mos_price
from n2 import n2
ROOT='/home/user/Modelo-JMR-datos'
REV_ID='MSFT-REBOOT-3T26-R1'
IDS=dict(h='1t5ZM7SQF-An3WMJXfdYb0Q_XGHeJuiBY_rervY7eK8E',b='19f9zo6xbYTnrjoAZwVf5ViHzVCEnkde9no2cryOBQjA',c='1TF-_XL14nxdAgNkHzJN3w5plZzOPj54rN2jnFfB33ho',o='13yJEdR4nTxVwE7b2bspxRGi8Pyk9Q_guwTmQdK36EMg',m='1m_mbps0ZIVzsDUNyz76UzPGhei5YLuWwnSffk10496o')
mode=sys.argv[1]; DOC=sys.argv[2] if len(sys.argv)>2 else 'PENDIENTE'
if mode=='html':
    html=n1()+n2().replace('__DOC__','Este documento (sexto archivo de la revisión)')
    open(sys.argv[2],'w').write('<!doctype html><html><head><meta charset="utf-8"><title>MSFT-REBOOT-3T26-R1 · 04 ANÁLISIS</title></head><body>'+html+'</body></html>');print('html ok');sys.exit()
sh=lambda i:f'https://docs.google.com/spreadsheets/d/{i}/edit'
LIB={'historicos':sh(IDS['h']),'dcf':{'base':sh(IDS['b']),'conservadora':sh(IDS['c']),'optimista':sh(IDS['o'])},'multiplos':sh(IDS['m']),'analisis':f'https://docs.google.com/document/d/{DOC}/edit'}
P_={'base':dict(g1=.18,cagr=.14,m=.46,s1=.8,s2=1.2,roic=.18),'cons':dict(g1=.13,cagr=.07,m=.40,s1=.55,s2=.9,roic=WACC_T),'opt':dict(g1=.21,cagr=.17,m=.49,s1=1.1,s2=1.5,roic=.26)}
def hist(id_,nombre,k,prob):
    st=ST[k];q=P_[k]
    return dict(id=id_,nombre=nombre,historia=nombre,probabilidad=prob,crecimiento=(st['rev'][5]/st['rev'][0])**(1/5)-1,margen=q['m'],salesToCapital=q['s1'],salesToCapital2=q['s2'],roicTerminal=q['roic'],
      valor=st['value'],terminalGrowth=0.04,estado='LISTO',incluidaEnPromedio=True,pesoEnPromedio=prob,s2c=q['s1'],s2c610=q['s2'],crecimientoAnio1=q['g1'],cagr25=q['cagr'],probabilidadFracaso=0)
H=[hist('A','Base','base',.5),hist('B','Conservadora','cons',.25),hist('C','Optimista','opt',.25)]
GL=[0.10,0.12,0.14,0.16,0.18];ML=[0.40,0.43,0.46,0.49,0.52];DW=[-0.01,-0.005,0,0.005,0.01];TG=[0.03,0.035,0.04,0.045,0.048]
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
metodos=[dict(nombre='DCF Damodaran',peso=.65,conservador=vc,base=vb,optimista=vo)]+[dict(nombre=m,peso=PESO[m],conservador=CONS['cons'][m],base=CONS['base'][m],optimista=CONS['opt'][m]) for m in MET]
SALV=['Auditoría económica independiente (R6) no realizada: el estado EN_REVISION no certifica el criterio económico.',
 'Verificación documental de la serie histórica contra los 10-K/10-Q pendiente (insumo: SEC XBRL); filas de verificación del libro de Múltiplos en «PENDIENTE».',
 'Arrendamientos financieros (70.973 M) tratados como deuda porque financian centros de datos y su interés no está en el EBIT; efecto ≈ −9,5 por acción. Arrendamientos operativos (27.477 M) no se restan como deuda (decisión del usuario). El capex en efectivo excluye 24.608 M de activos recibidos por arrendamientos financieros en FY2026.',
 'Precio por encima del DCF Base (−6,9 %): sin margen de seguridad. El precio implica 16,0 % de crecimiento anual (años 1–5), 49,1 % de margen objetivo o 9,37 % de costo de capital inicial.',
 'Beta bottom-up 1,28 (mapeo de industrias propio; beta observada ≈ 1,0): con beta 1,00 el DCF Base sería 533,88. Tasa marginal 23 % y costo de la deuda 5,20 % son estimaciones; calificación crediticia no verificada.',
 'Inversiones no operativas (37.808 M, incluye la participación en OpenAI) a valor en libros; compromisos con OpenAI y concentración del RPO (683.000 M) no cuantificados.',
 'EV/FCFF (47,70x) y P/FCFE (44,60x) usan la mediana de 5 años como múltiplo de salida porque el flujo libre del LTM está deprimido por el capex de IA; el múltiplo actual es N/D o extremo.',
 'Acciones: 7.426,195 M (portada del 10-Q) + 78 M de acciones restringidas no devengadas (todas; conservador). Participación de mercado y gobierno corporativo N/D o no analizados. Ceros por dato no separable en el libro de Múltiplos y reparto corriente/no corriente de arrendamientos financieros no disponible.',
 'Integridad de fórmulas y comentarios del motor fcffsimpleginzu no re-verificada en las copias de MSFT. Matrices 5×5 de múltiplos derivadas de las hojas de método (precio FY+3 descontado con el Ke Base y ajustado por dividendos).']
rec=dict(ticker='MSFT',revisionId=REV_ID,revision_id=REV_ID,sheet_id=IDS['b'],estado='EN_REVISION',publicationStatus='EN_REVISION',perfil_valoracion='Floyd',metodo_valoracion='A',version_metodo='Floyd',
 fecha_corte='2026-11-06',fechaCorteContable='2026-09-30',valorPrincipal=vb,precioMOS=vb*(1-MOS),baseMOS='dcfBase',hojaGoogle=LIB['dcf']['base'],nombreActivo='Microsoft Corporation',market='NASDAQ',moneda='USD',
 precio=PREC,precioReferenciaFecha='2026-11-06',mos=MOS,metodoPrincipal='DCF FCFF Base 10 años',
 escenariosDCF=dict(version='Floyd',revisionId=REV_ID,fecha='2026-11-06',central='A',principal='DCF Base',historias=H),
 valorEsperado=dict(valor=EXPECTED,dcfBase=vb,historiaCentralId='A',disrupcionEnPromedio=False,historias=H,escenariosUnificados=dict(conservador=vc,base=vb,optimista=vo),escenariosPromedio=3,rango=dict(minimo=vc,maximo=vo)),
 sensibilidadDCF=dict(centro=vb,centroConciliado=True,matrices=[
   dict(nombre='CAGR años 2–5 × margen operativo objetivo ajustado',ejeFilas=GL,ejeColumnas=ML,valores=MA,centro=MA[2][2],centroConciliado=True,origen="'Sensibilidades DCF'!A5:F10"),
   dict(nombre='Costo de capital inicial × crecimiento terminal',ejeFilas=[WACC0+d for d in DW],ejeColumnas=TG,valores=MB,centro=MB[2][2],centroConciliado=True,origen="'Sensibilidades DCF'!A13:F18")]),
 sensibilidadMultiples=dict(contrato='reboot-atlas-cinco-v1',revisionId=REV_ID,sourceSheetId=IDS['m'],estadoPublicacion='INTEGRADO_EN_REVISION',controlesTecnicosAprobados=True,certificado=False,matrices=mm,
   resultadosSha256='0'*64,resultadosHashMetodo='SHA256 UTF8 JSON.stringify(sensibilidadMultiples.matrices)'),
 metodos=metodos,
 descuentoMultiples=dict(version=3,costoPatrimonio=KE,criterio='Ponderado FY+1–FY+3 (20/30/50 %)',horizontes=[1,2,3],pesoDcf=.65,pesoMultiplos=.35,dcfHoy=dict(conservador=vc,base=vb,optimista=vo),
   multiplesHoy=dict(conservador=MULT['cons'],base=MULT['base'],optimista=MULT['opt']),ponderadoHoy=dict(conservador=COMB['cons'],base=COMB['base'],optimista=COMB['opt']),metodos=[mdet(m) for m in MET],tipoEmpresa='Madura'),
 dcfInverso=dict(precio=PREC,replicaBase=vb,
   crecimientoBaseFijo=dict(cagr5=SENS['crecimiento'],margenObjetivo=.46,valor=PREC,descripcion='Crecimiento anual años 1–5 que iguala el precio con el margen de la Base'),
   margenBaseFijo=dict(cagr5=.14,margenObjetivo=SENS['margen'],valor=PREC,descripcion='Margen objetivo ajustado que iguala el precio con el crecimiento de la Base'),
   crecimientoMargen46=dict(cagr5=SENS['crec_con_margen16'],margenObjetivo=.46,valor=PREC),
   waccInicial=dict(alcanzable=True,valor=SENS['wacc'],valorResultado=PREC),constantes=dict(g=.04,w=WACC0,wTerminal=WACC_T,roic=.18)),
 puente=dict(operativo=ST['base']['op_assets'],deuda=106454,minoritarios=0,caja=64509,noOperativos=37808,opciones=0,accionesMillones=7504.195),
 tasas=dict(wacc=WACC0,waccTerminal=WACC_T,ke=KE,fuenteWacc='Cost of capital worksheet (DCF Base): Rf 4,86 % (FRED DGS10, 6-nov-2026), beta bottom-up 1,28 (Software (System & Application) y Computers/Peripherals por ingresos), ERP por regiones 4,52 % (madura 3,387 %, Damodaran nov-2026), Kd 5,20 %'),
 fecha='2026-11-06',fechaPublicacion='2026-11-10',auditPendingUserVisualReview=True,auditoriaEconomica='NO_REALIZADA',salvedades=SALV,
 controlPublicacion=dict(dcfBaseConcilia=True,probabilidadesSuman1=True,centrosDcfVerificados=3,centrosMultiplesVerificados=5,perfil='Floyd',revisionId=REV_ID,fechaComprobacion='2026-11-10',
   replicaIndependiente='Base 496,21; Conservadora 232,38; Optimista 676,08 (LibreOffice sobre fcffsimpleginzu original; diferencia < 1e-4 con la hoja)',
   integridadMotor='NO re-verificada en las copias de MSFT',visorEndToEnd='QA_BROWSER_VISUAL_SIN_REALIZAR',auditoriaEconomicaRealizada=False,ciMotor='por ejecutar en PR',revisionAnterior='ninguna (MSFT no tenía revisión Reboot activa)'),
 libros=LIB,contratoLibros='jmr-reboot-3libros-v1')
N1=n1();N2=n2().replace('__DOC__',f'https://docs.google.com/document/d/{DOC}/edit')
rp=f'{ROOT}/valoraciones/{REV_ID}.json'
json.dump(rec,open(rp,'w'),ensure_ascii=False,indent=1)
sha=subprocess.check_output(['node','-e',"const c=require('crypto'),f=require('fs');const r=JSON.parse(f.readFileSync(process.argv[1],'utf8'));console.log(c.createHash('sha256').update(JSON.stringify(r.sensibilidadMultiples.matrices),'utf8').digest('hex'))",rp]).decode().strip()
rec['sensibilidadMultiples']['resultadosSha256']=sha;json.dump(rec,open(rp,'w'),ensure_ascii=False,indent=1)
words=lambda s:len(re.sub('<[^>]+>',' ',s).split())
ana=dict(id=f'MSFT-research-{REV_ID}',title='MSFT | Microsoft — Análisis JMR Floyd R1–R6 3T-2026',ticker='MSFT',company='Microsoft Corporation',revisionId=REV_ID,valuationRevisionId=REV_ID,version_metodo='Floyd',
 perfil_valoracion='Floyd',estado='EN_REVISION',publicationStatus='EN_REVISION',sheet_id=IDS['b'],price=PREC,financialCutoff='2026-09-30',valorPrincipal=vb,precioMOS=vb*(1-MOS),articleHtml=N1,calculationHtml=N2,
 documentos=dict(nivel1=LIB['analisis'],nivel2=LIB['analisis']),linkedValuation=dict(revisionId=REV_ID,valorPrincipal=vb,sourcePath=f'valoraciones/{REV_ID}.json',estado='EN_REVISION'),salvedades=SALV,status='EN_REVISION',
 date='2026-11-10',remotePath=f'analisis/MSFT-research-{REV_ID}.json',
 controlCobertura=dict(secciones=14,escenariosDCF=3,centrosDCFValidados=3,centrosMultiplesValidados=5,nivel1=True,nivel2=True,auditoriaEconomicaIndependiente=False,palabrasNivel1=words(N1),nivel2Apartados=12),html=N1+N2)
json.dump(ana,open(f'{ROOT}/analisis/MSFT-research-{REV_ID}.json','w'),ensure_ascii=False,indent=1)
print('ok',sha,words(N1),words(N2))
