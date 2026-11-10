import json,re,subprocess,os
from datos import *
from n1 import n1,vb,vc,vo,px,mos_price
from n2 import n2
ROOT='/home/user/Modelo-JMR-datos'
REV_ID='CMG-REBOOT-3T26-R1'
IDS=dict(h='1fWez5DOCZv7RBUCCzKgrEUZa4imFmRCyVzFxuxirizI',b='1asO4BR42MypptINAooJ3hP6joY5fFUYDB5IM2NSDo7U',c='1i5Sc_uoJX6cnvq9wDjr4jP0XtMIE5c1vtlDDEBfz_qU',o='1hSctlkSB4-mUMZPxwtnGpKLWaH8Bn_Ymzhdowh6mpzQ',m='1jdUkjDwPG79FmSGLbZfQd-xTXMVBC8xJ9wG2imACeK0')
DOC='1jlt6v-PWeZOckqaLJWs6nClg2GyayuhQFOt-A4rCwlY'
sh=lambda i:f'https://docs.google.com/spreadsheets/d/{i}/edit'
LIB={'historicos':sh(IDS['h']),'dcf':{'base':sh(IDS['b']),'conservadora':sh(IDS['c']),'optimista':sh(IDS['o'])},'multiplos':sh(IDS['m']),'analisis':f'https://docs.google.com/document/d/{DOC}/edit'}
b=ST['base']
P_={'base':dict(g1=.095,cagr=.088,m=.16,s1=2.7,s2=2.9,roic=.1836),'cons':dict(g1=.064,cagr=.064,m=.13,s1=2.2,s2=2.4,roic=WACC_T),'opt':dict(g1=.11,cagr=.109,m=.18,s1=2.9,s2=3.2,roic=.1836)}
def hist(id_,nombre,k,prob):
    st=ST[k];q=P_[k]
    return dict(id=id_,nombre=nombre,historia=nombre,probabilidad=prob,crecimiento=(st['rev'][5]/st['rev'][0])**(1/5)-1,margen=q['m'],salesToCapital=q['s1'],salesToCapital2=q['s2'],roicTerminal=q['roic'],
      valor=st['value'],terminalGrowth=0.04,estado='LISTO',incluidaEnPromedio=True,pesoEnPromedio=prob,s2c=q['s1'],s2c610=q['s2'],crecimientoAnio1=q['g1'],cagr25=q['cagr'],probabilidadFracaso=0)
H=[hist('A','Base','base',.5),hist('B','Conservadora','cons',.25),hist('C','Optimista','opt',.25)]
GL=[0.068,0.078,0.088,0.098,0.108];ML=[0.14,0.15,0.16,0.17,0.18];DW=[-0.01,-0.005,0,0.005,0.01];TG=[0.03,0.035,0.04,0.045,0.048]
MA=[[SENS[f'a_{i}_{j}'] for j in range(5)] for i in range(5)];MB=[[SENS[f'b_{i}_{j}'] for j in range(5)] for i in range(5)]
SHEETS={'EV/EBITDA':'EVEBITDA','EV/FCFF':'EVFCFF','P/E':'PE','P/FCFE':'PFCFE','P/OCF':'POCF'}
mm=[]
for m in MET:
    mt=MATRICES_M[m];V=matriz_vp(m)
    mm.append(dict(metodo=m,escenario='base',estado='OK',peso=PESO[m],ancla='JMR',origen=f"'{SHEETS[m]}'!A46:F51",matriz=V,fundamentalFY3=mt['col'],multiploElegido=mt['fila'],centro=V[2][2],vp3Original=VPM['base'][m][2],
      precioFY3SinDescontar=mt['val'],unidadFundamental=mt['unidad'],derivacion='celda = precio FY+3 × factor de descuento 3 años (Ke Base); sin dividendos; centro = VP3 Base de Descuento de múltiplos'))
def mdet(m):
    d={n:dict(objetivo=OBJ[k][m],vp=VPM[k][m],consolidado=CONS[k][m]) for k,n in (('cons','conservador'),('base','base'),('opt','optimista'))}
    return dict(nombre=m,peso=PESO[m],estado='OK',**d)
metodos=[dict(nombre='DCF Damodaran',peso=.65,conservador=vc,base=vb,optimista=vo)]+[dict(nombre=m,peso=PESO[m],conservador=CONS['cons'][m],base=CONS['base'][m],optimista=CONS['opt'][m]) for m in MET]
SALV=['Auditoría económica independiente (R6) no realizada: el estado EN_REVISION no certifica el criterio económico.',
 'Verificación documental de la serie histórica contra los 10-K/10-Q pendiente (insumo: SEC XBRL); precios de cierre fiscal de una sola fuente.',
 'Arrendamientos (5.599 M) no se restan como deuda por decisión del usuario: el EBIT ya deduce el alquiler; en el libro de Múltiplos están reclasificados a otros pasivos.',
 '«Otros ajustes» del flujo de caja LTM (804 M) sin desglosar; no afecta el DCF, sí el CFO proyectado de P/OCF.',
 'Integridad de fórmulas y comentarios del motor fcffsimpleginzu no re-verificada en las copias de CMG.',
 'Volatilidad de las opciones (35 %) y beta de industria 0,783 (tabla de enero 2026) son supuestos; el valor es sensible al costo de capital.',
 'Participación de mercado N/D; gobierno corporativo no analizado.',
 'Matrices 5×5 de múltiplos derivadas de las hojas de método (precio FY+3 descontado con el Ke Base); el libro de Múltiplos no descuenta el valor de las opciones.']
rec=dict(ticker='CMG',revisionId=REV_ID,revision_id=REV_ID,sheet_id=IDS['b'],estado='EN_REVISION',publicationStatus='EN_REVISION',perfil_valoracion='Reboot',metodo_valoracion='A',version_metodo='Reboot',
 fecha_corte='2026-11-06',fechaCorteContable='2026-09-30',valorPrincipal=vb,precioMOS=vb*(1-MOS),baseMOS='dcfBase',hojaGoogle=LIB['dcf']['base'],nombreActivo='Chipotle Mexican Grill, Inc.',market='NYSE',moneda='USD',
 precio=PREC,precioReferenciaFecha='2026-11-06',mos=MOS,metodoPrincipal='DCF FCFF Base 10 años',
 escenariosDCF=dict(version='Reboot',revisionId=REV_ID,fecha='2026-11-06',central='A',principal='DCF Base',historias=H),
 valorEsperado=dict(valor=EXPECTED,dcfBase=vb,historiaCentralId='A',disrupcionEnPromedio=False,historias=H,escenariosUnificados=dict(conservador=vc,base=vb,optimista=vo),escenariosPromedio=3,rango=dict(minimo=vc,maximo=vo)),
 sensibilidadDCF=dict(centro=vb,centroConciliado=True,matrices=[
   dict(nombre='CAGR años 2–5 × margen operativo objetivo',ejeFilas=GL,ejeColumnas=ML,valores=MA,centro=MA[2][2],centroConciliado=True,origen="'Sensibilidades DCF'!A5:F10"),
   dict(nombre='Costo de capital inicial × crecimiento terminal',ejeFilas=[WACC0+d for d in DW],ejeColumnas=TG,valores=MB,centro=MB[2][2],centroConciliado=True,origen="'Sensibilidades DCF'!A13:F18")]),
 sensibilidadMultiples=dict(contrato='reboot-atlas-cinco-v1',revisionId=REV_ID,sourceSheetId=IDS['m'],estadoPublicacion='INTEGRADO_EN_REVISION',controlesTecnicosAprobados=True,certificado=False,matrices=mm,
   resultadosSha256='0'*64,resultadosHashMetodo='SHA256 UTF8 JSON.stringify(sensibilidadMultiples.matrices)'),
 metodos=metodos,
 descuentoMultiples=dict(version=3,costoPatrimonio=KE,criterio='Ponderado FY+1–FY+3 (20/30/50 %)',horizontes=[1,2,3],pesoDcf=.65,pesoMultiplos=.35,dcfHoy=dict(conservador=vc,base=vb,optimista=vo),
   multiplesHoy=dict(conservador=MULT['cons'],base=MULT['base'],optimista=MULT['opt']),ponderadoHoy=dict(conservador=COMB['cons'],base=COMB['base'],optimista=COMB['opt']),metodos=[mdet(m) for m in MET],tipoEmpresa='Madura'),
 dcfInverso=dict(precio=PREC,replicaBase=vb,
   crecimientoBaseFijo=dict(cagr5=SENS['crecimiento'],margenObjetivo=.16,valor=PREC,descripcion='Crecimiento anual años 1–5 que iguala el precio con el margen de la Base'),
   margenBaseFijo=dict(cagr5=.088,margenObjetivo=SENS['margen'],valor=PREC,descripcion='Margen objetivo que iguala el precio con el crecimiento de la Base'),
   crecimientoMargen18=dict(cagr5=SENS['crec_con_margen18'],margenObjetivo=.18,valor=PREC),
   waccInicial=dict(alcanzable=True,valor=SENS['wacc'],valorResultado=PREC),constantes=dict(g=.04,w=WACC0,wTerminal=WACC_T,roic=.1836)),
 puente=dict(operativo=b['op_assets'],deuda=0,minoritarios=0,caja=902.564,noOperativos=100.365,opciones=b['options'],accionesMillones=1270.149),
 tasas=dict(wacc=WACC0,waccTerminal=WACC_T,ke=KE,fuenteWacc='Cost of capital worksheet (DCF Base): Rf 4,86 % (FRED DGS10, 6-nov-2026), beta 0,783 (Restaurant/Dining), ERP 3,603 % (Norteamérica), ERP madura 3,387 % (Damodaran nov-2026)'),
 fecha='2026-11-06',fechaPublicacion='2026-11-10',auditPendingUserVisualReview=True,auditoriaEconomica='NO_REALIZADA',salvedades=SALV,
 controlPublicacion=dict(dcfBaseConcilia=True,probabilidadesSuman1=True,centrosDcfVerificados=3,centrosMultiplesVerificados=5,perfil='Reboot',revisionId=REV_ID,fechaComprobacion='2026-11-10',
   replicaIndependiente='Base 32,28368; Conservadora 17,68578; Optimista 40,46753 (LibreOffice sobre fcffsimpleginzu original; diferencia < 1e-4 con la hoja)',
   integridadMotor='NO re-verificada en las copias de CMG',visorEndToEnd='QA_BROWSER_VISUAL_SIN_REALIZAR',auditoriaEconomicaRealizada=False,ciMotor='por ejecutar en PR',revisionAnterior='CMG-FLOYD-20261108-R1'),
 libros=LIB,contratoLibros='jmr-reboot-3libros-v1')
N1=n1();N2=n2().replace('__DOC__',DOC)
rp=f'{ROOT}/valoraciones/{REV_ID}.json'
json.dump(rec,open(rp,'w'),ensure_ascii=False,indent=1)
sha=subprocess.check_output(['node','-e',"const c=require('crypto'),f=require('fs');const r=JSON.parse(f.readFileSync(process.argv[1],'utf8'));console.log(c.createHash('sha256').update(JSON.stringify(r.sensibilidadMultiples.matrices),'utf8').digest('hex'))",rp]).decode().strip()
rec['sensibilidadMultiples']['resultadosSha256']=sha;json.dump(rec,open(rp,'w'),ensure_ascii=False,indent=1)
words=lambda s:len(re.sub('<[^>]+>',' ',s).split())
ana=dict(id=f'CMG-research-{REV_ID}',title='CMG | Chipotle Mexican Grill — Análisis JMR Reboot 3T-2026',ticker='CMG',company='Chipotle Mexican Grill, Inc.',revisionId=REV_ID,valuationRevisionId=REV_ID,version_metodo='Reboot',
 perfil_valoracion='Reboot',estado='EN_REVISION',publicationStatus='EN_REVISION',sheet_id=IDS['b'],price=PREC,financialCutoff='2026-09-30',valorPrincipal=vb,precioMOS=vb*(1-MOS),articleHtml=N1,calculationHtml=N2,
 documentos=dict(nivel1=LIB['analisis'],nivel2=LIB['analisis']),linkedValuation=dict(revisionId=REV_ID,valorPrincipal=vb,sourcePath=f'valoraciones/{REV_ID}.json',estado='EN_REVISION'),salvedades=SALV,status='EN_REVISION',
 date='2026-11-10',remotePath=f'analisis/CMG-research-{REV_ID}.json',
 controlCobertura=dict(secciones=14,escenariosDCF=3,centrosDCFValidados=3,centrosMultiplesValidados=5,nivel1=True,nivel2=True,auditoriaEconomicaIndependiente=False,palabrasNivel1=words(N1),nivel2Apartados=12),html=N1+N2)
json.dump(ana,open(f'{ROOT}/analisis/CMG-research-{REV_ID}.json','w'),ensure_ascii=False,indent=1)
print('ok',sha,words(N1),words(N2))
