"""R5 · cifras de CMG-REBOOT-3T26-R1: Históricos (XBRL), motor original recalculado (motor/*.xlsx) y lecturas del libro M (2026-11-10)."""
import json,openpyxl,os
HERE=os.path.dirname(os.path.abspath(__file__)); BASE=os.path.dirname(HERE)
D=json.load(open(HERE+'/dataset_cmg.json'))
SENS=json.load(open(BASE+'/R3_evidencia/sens_res.json'))
FY=list(range(2016,2026))
def s(sheet,r): return D[f'{sheet}|{r}']
IS,BS,CF='Income Statement','Balance Sheet','Cash Flow Statement'
def story(tag):
    wb=openpyxl.load_workbook(f'{HERE}/motor/{tag}.xlsx',data_only=True);vo=wb['Valuation output'];cols='BCDEFGHIJKLM'
    def row(r): return [vo[f'{c}{r}'].value for c in cols]
    return dict(growth=row(2),rev=row(3),margin=row(4),ebit=row(5),tax=row(6),nopat=row(7),reinv=row(8),fcff=row(9),wacc=row(12),df=row(13),pv=row(14),s2c=row(38),ic=row(39),roic=row(40),
      tv_cf=vo['B16'].value,tv_wacc=vo['B17'].value,tv=vo['B18'].value,pv_tv=vo['B19'].value,pv_cf=vo['B20'].value,sum_pv=vo['B21'].value,op_assets=vo['B24'].value,
      debt=vo['B25'].value,cash=vo['B27'].value,nonop=vo['B28'].value,equity_pre=vo['B29'].value,options=vo['B30'].value,equity=vo['B31'].value,shares=vo['B32'].value,value=vo['B33'].value)
ST={'base':story('base'),'cons':story('cons'),'opt':story('opt')}
PREC=34.43; MOS=0.35
PROB={'cons':0.25,'base':0.5,'opt':0.25}
VAL={k:ST[k]['value'] for k in ST}
EXPECTED=sum(PROB[k]*VAL[k] for k in ST)
MET=['EV/EBITDA','EV/FCFF','P/E','P/FCFE','P/OCF']
PESO={'EV/EBITDA':.08,'EV/FCFF':.05,'P/E':.12,'P/FCFE':.07,'P/OCF':.03}
OBJ={'cons':{'EV/EBITDA':[30.41,31.70,33.01],'EV/FCFF':[32.05,32.76,33.38],'P/E':[31.49,32.62,33.73],'P/FCFE':[26.45,27.30,28.12],'P/OCF':[25.78,27.03,28.32]},
 'base':{'EV/EBITDA':[37.82,41.63,45.83],'EV/FCFF':[38.52,43.36,47.67],'P/E':[39.59,43.63,48.08],'P/FCFE':[32.01,35.94,39.60],'P/OCF':[32.08,35.38,39.02]},
 'opt':{'EV/EBITDA':[44.86,51.35,58.77],'EV/FCFF':[45.26,52.52,60.74],'P/E':[47.28,54.40,62.57],'P/FCFE':[37.68,43.59,50.27],'P/OCF':[38.07,43.56,49.82]}}
VPM={'cons':{'EV/EBITDA':[28.24,27.34,26.44],'EV/FCFF':[29.76,28.25,26.73],'P/E':[29.24,28.13,27.02],'P/FCFE':[24.57,23.55,22.52],'P/OCF':[23.94,23.31,22.68]},
 'base':{'EV/EBITDA':[35.12,35.90,36.71],'EV/FCFF':[35.77,37.39,38.18],'P/E':[36.76,37.62,38.50],'P/FCFE':[29.72,31.00,31.71],'P/OCF':[29.79,30.51,31.25]},
 'opt':{'EV/EBITDA':[41.66,44.29,47.07],'EV/FCFF':[42.03,45.30,48.65],'P/E':[43.91,46.92,50.11],'P/FCFE':[34.99,37.59,40.26],'P/OCF':[35.36,37.56,39.90]}}
_C={'EV/EBITDA':[27.0700570467,36.1472318538,45.154082043],'EV/FCFF':[27.7945689808,37.4610056133,46.318103172],'P/E':[27.7955145606,37.8911526236,47.9117971139],'P/FCFE':[23.2376322625,31.1013776361,38.4051187993],'P/OCF':[23.1233125946,30.7377056675,38.2898538323]}
CONS={k:{m:_C[m][i] for m in MET} for i,k in enumerate(('cons','base','opt'))}
MULT={'cons':26.3175097036,'base':35.4599849953,'opt':44.3277180189}
COMB={k:0.65*VAL[k]+0.35*MULT[k] for k in ST}
MULT_EXIT={'EV/EBITDA':(16.59,19.52,22.45),'EV/FCFF':(36.23,42.62,49.01),'P/E':(26.88,31.62,36.36),'P/FCFE':(24.51,28.84,33.17),'P/OCF':(15.77,18.55,21.33)}
HIST_MULT={'EV/EBITDA':dict(y10=33.38,y5=32.72,y3=32.72,ttm=19.52),'EV/FCFF':dict(y10=55.77,y5=62.21,y3=62.21,ttm=None),'P/E':dict(y10=59.83,y5=51.04,y3=51.04,ttm=31.62),
 'P/FCFE':dict(y10=52.68,y5=51.29,y3=51.29,ttm=28.84),'P/OCF':dict(y10=31.39,y5=35.16,y3=35.16,ttm=18.55)}
def _g(c,st): return [c+st*(i-2) for i in range(5)]
MATRICES_M={
 'EV/EBITDA':dict(fila=[17.57,18.54,19.52,20.50,21.47],col=[2660,2808,2956,3104,3252],val=[[37.27,39.30,41.33,43.35,45.38],[39.30,41.44,43.58,45.72,47.86],[41.33,43.58,45.83,48.08,50.33],[43.35,45.72,48.08,50.45,52.81],[45.38,47.86,50.33,52.81,55.29]],unidad='EBITDA FY+3 (M USD)'),
 'EV/FCFF':dict(fila=[38.36,40.49,42.62,44.75,46.88],col=[1268,1339,1409,1480,1550],val=[[38.76,40.87,42.98,45.09,47.20],[40.87,43.10,45.32,47.55,49.78],[42.98,45.32,47.67,50.01,52.36],[45.09,47.55,50.01,52.47,54.94],[47.20,49.78,52.36,54.94,57.51]],unidad='FCFF FY+3 (M USD)'),
 'P/E':dict(fila=[28.46,30.04,31.62,33.20,34.78],col=[1753,1850,1948,2045,2142],val=[[38.94,41.10,43.27,45.43,47.59],[41.10,43.39,45.67,47.96,50.24],[43.27,45.67,48.08,50.48,52.88],[45.43,47.96,50.48,53.00,55.53],[47.59,50.24,52.88,55.53,58.17]],unidad='Utilidad neta FY+3 (M USD)'),
 'P/FCFE':dict(fila=[25.96,27.40,28.84,30.28,31.72],col=[1583,1671,1759,1847,1935],val=[[32.07,33.86,35.64,37.42,39.20],[33.86,35.74,37.62,39.50,41.38],[35.64,37.62,39.60,41.58,43.56],[37.42,39.50,41.58,43.66,45.74],[39.20,41.38,43.56,45.74,47.91]],unidad='FCFE FY+3 (M USD)'),
 'P/OCF':dict(fila=[16.70,17.62,18.55,19.48,20.41],col=[2425,2560,2694,2829,2964],val=[[31.61,33.36,35.12,36.87,38.63],[33.36,35.22,37.07,38.92,40.78],[35.12,37.07,39.02,40.97,42.92],[36.87,38.92,40.97,43.02,45.07],[38.63,40.78,42.92,45.07,47.21]],unidad='OCF FY+3 (M USD)')}
KE=0.0768154743198044; WACC0=KE; WACC_T=0.08247
DF3=(1+KE)**-3
def matriz_vp(m):
    """VP por acción: celda×DF3 + (VP3 − centro×DF3). CMG no paga dividendos: el ajuste es solo redondeo."""
    mt=MATRICES_M[m]; c=mt['val'][2][2]; vp3=VPM['base'][m][2]; k=vp3-c*DF3
    return [[x*DF3+k for x in r] for r in mt['val']]
