"""R5 · carga de cifras de AAPL-REBOOT-FY26-R1 desde las evidencias R2/R3 y las lecturas de los libros (R4)."""
import json,openpyxl,os
SP='/tmp/claude-0/-home-user/b8c0d315-1e6b-524a-8878-fb2b853781cf/scratchpad'
HERE=os.path.dirname(os.path.abspath(__file__)); BASE=os.path.dirname(HERE)
D=json.load(open(BASE+'/R2_evidencia/dataset_xbrl.json'))
PRC=json.load(open(BASE+'/R2_evidencia/precios_cierre_fiscal.json'))
SENS=json.load(open(BASE+'/R3_evidencia/sens2_res.json'))
REV=json.load(open(BASE+'/R3_evidencia/rev_res.json'))
FY=list(range(2017,2027))
def s(sheet,r): return D[f'{sheet}|{r}']
IS,BS,CF='Income Statement','Balance Sheet','Cash Flow Statement'
def story(tag):
    wb=openpyxl.load_workbook(f'{SP}/lo/{tag}/out/in.xlsx',data_only=True)
    vo=wb['Valuation output']
    cols='BCDEFGHIJKLM'
    def row(r): return [vo[f'{c}{r}'].value for c in cols]
    return dict(growth=row(2),rev=row(3),margin=row(4),ebit=row(5),tax=row(6),nopat=row(7),reinv=row(8),fcff=row(9),
      wacc=row(12),df=row(13),pv=row(14),s2c=row(38),ic=row(39),roic=row(40),
      tv_cf=vo['B16'].value,tv_wacc=vo['B17'].value,tv=vo['B18'].value,pv_tv=vo['B19'].value,pv_cf=vo['B20'].value,
      sum_pv=vo['B21'].value,p_fail=vo['B22'].value,proceeds=vo['B23'].value,op_assets=vo['B24'].value,
      debt=vo['B25'].value,cash=vo['B27'].value,equity=vo['B31'].value,shares=vo['B32'].value,value=vo['B33'].value,price=vo['B34'].value)
ST={'base':story('base'),'cons':story('cons'),'opt':story('opt')}
PREC=342.37; MOS=0.35
PROB={'cons':0.25,'base':0.5,'opt':0.25}
VAL={k:ST[k]['value'] for k in ST}
EXPECTED=sum(PROB[k]*VAL[k] for k in ST)
# Múltiplos (lectura de 'Descuento de múltiplos' del libro M, 2026-11-09)
MET=['EV/EBITDA','EV/FCFF','P/E','P/FCFE','P/OCF']
PESO={'EV/EBITDA':.08,'EV/FCFF':.08,'P/E':.09,'P/FCFE':.07,'P/OCF':.03}
OBJ={ # precio + dividendos FY+1..FY+3
 'cons':{'EV/EBITDA':[249.28,253.02,256.52],'EV/FCFF':[263.81,268.70,271.15],'P/E':[240.86,243.85,246.54],'P/FCFE':[201.11,204.88,206.73],'P/OCF':[235.11,240.49,244.08]},
 'base':{'EV/EBITDA':[297.30,323.18,351.19],'EV/FCFF':[276.11,302.12,328.53],'P/E':[293.53,319.01,346.59],'P/FCFE':[250.25,273.89,297.85],'P/OCF':[269.70,295.03,320.59]},
 'opt':{'EV/EBITDA':[342.73,387.51,437.79],'EV/FCFF':[286.17,327.95,371.89],'P/E':[344.02,389.29,440.17],'P/FCFE':[299.99,343.85,389.91],'P/OCF':[301.29,345.11,390.19]}}
VPM={
 'cons':{'EV/EBITDA':[225.89,207.88,191.17],'EV/FCFF':[239.05,220.75,202.06],'P/E':[218.26,200.34,183.75],'P/FCFE':[182.24,168.35,154.12],'P/OCF':[213.05,197.58,181.92]},
 'base':{'EV/EBITDA':[269.40,265.49,261.65],'EV/FCFF':[250.20,248.20,244.79],'P/E':[265.98,262.07,258.23],'P/FCFE':[226.77,225.02,221.96],'P/OCF':[244.40,242.38,238.88]},
 'opt':{'EV/EBITDA':[310.57,318.33,326.11],'EV/FCFF':[259.32,269.41,277.07],'P/E':[311.74,319.79,327.88],'P/FCFE':[271.84,282.47,290.48],'P/OCF':[273.02,283.51,290.69]}}
CONS={ # consolidado hoy por método
 'cons':{'EV/EBITDA':203.13,'EV/FCFF':215.07,'P/E':195.63,'P/FCFE':164.02,'P/OCF':192.85},
 'base':{'EV/EBITDA':264.35,'EV/FCFF':246.90,'P/E':260.93,'P/FCFE':223.84,'P/OCF':241.03},
 'opt':{'EV/EBITDA':320.67,'EV/FCFF':271.22,'P/E':322.22,'P/FCFE':284.35,'P/OCF':285.00}}
MULT={'cons':195.22,'base':249.38,'opt':299.45}
COMB={'cons':137.82,'base':223.51,'opt':274.10}
MULT_EXIT={'EV/EBITDA':(21.17,23.57,25.97),'EV/FCFF':(30.53,30.73,30.93),'P/E':(26.47,30.08,33.69),'P/FCFE':(23.99,28.74,33.49),'P/OCF':(23.41,26.27,29.12)}
KE=0.103542; WACC0=0.1025195876573334; WACC_T=0.08247
# Matrices 5×5 de cada método (hoja del libro M, Base): precio FY+3 sin descontar; filas = múltiplo elegido, columnas = fundamental FY+3
MATRICES_M={
 'EV/EBITDA':dict(fila=[21.21,22.39,23.57,24.75,25.93],col=[183491,193685,203879,214073,224267],
   val=[[280.42,296.15,311.88,327.61,343.34],[296.15,312.75,329.36,345.97,362.57],[311.88,329.36,346.84,364.32,381.80],[327.61,345.97,364.32,382.67,401.03],[343.34,362.57,381.80,401.03,420.25]],unidad='EBITDA FY+3 (M USD)'),
 'EV/FCFF':dict(fila=[27.66,29.19,30.73,32.27,33.80],col=[131617,138929,146241,153553,160865],
   val=[[262.07,276.78,291.49,306.20,320.91],[276.78,292.31,307.84,323.37,338.89],[291.49,307.84,324.18,340.53,356.88],[306.20,323.37,340.53,357.69,374.86],[320.91,338.89,356.88,374.86,392.84]],unidad='FCFF FY+3 (M USD)'),
 'P/E':dict(fila=[27.07,28.58,30.08,31.58,33.09],col=[140759,148579,156399,164219,172039],
   val=[[277.22,292.62,308.02,323.42,338.82],[292.62,308.87,325.13,341.39,357.64],[308.02,325.13,342.24,359.35,376.47],[323.42,341.39,359.35,377.32,395.29],[338.82,357.64,376.47,395.29,414.11]],unidad='Utilidad neta FY+3 (M USD)'),
 'P/FCFE':dict(fila=[25.87,27.30,28.74,30.18,31.61],col=[126341,133360,140379,147398,154417],
   val=[[237.74,250.94,264.15,277.36,290.57],[250.94,264.89,278.83,292.77,306.71],[264.15,278.83,293.50,308.18,322.85],[277.36,292.77,308.18,323.59,339.00],[290.57,306.71,322.85,339.00,355.14]],unidad='FCFE FY+3 (M USD)'),
 'P/OCF':dict(fila=[23.64,24.96,26.27,27.58,28.90],col=[148929,157203,165477,173751,182025],
   val=[[256.16,270.39,284.62,298.85,313.08],[270.39,285.41,300.43,315.45,330.47],[284.62,300.43,316.24,332.05,347.87],[298.85,315.45,332.05,348.66,365.26],[313.08,330.47,347.87,365.26,382.65]],unidad='OCF FY+3 (M USD)')}
HIST_MULT={'EV/EBITDA':dict(y10=21.17,y5=25.97,y3=26.47,ttm=29.23),'EV/FCFF':dict(y10=30.53,y5=30.93,y3=44.74,ttm=None),
 'P/E':dict(y10=26.47,y5=33.69,y3=36.74,ttm=37.64),'P/FCFE':dict(y10=23.99,y5=33.49,y3=41.80,ttm=42.25),'P/OCF':dict(y10=23.41,y5=29.12,y3=33.85,ttm=34.29)}
DF3=(1+0.103542)**-3
def matriz_vp(m):
    """VP por acción: celda×DF3 + (VP3 − centro×DF3); centro = VP3 Base del método (regla §8: centro conciliado al VP3)."""
    mt=MATRICES_M[m]; c=mt['val'][2][2]; vp3=VPM['base'][m][2]; k=vp3-c*DF3
    return [[x*DF3+k for x in r] for r in mt['val']]
