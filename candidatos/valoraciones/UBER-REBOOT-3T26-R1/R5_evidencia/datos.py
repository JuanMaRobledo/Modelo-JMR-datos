"""R5 · cifras de UBER-REBOOT-3T26-R1: Históricos (SEC XBRL, hist_payload.json), motor original recalculado (R3_evidencia/motor) y lecturas del libro M (2026-11-10)."""
import json,openpyxl,os
HERE=os.path.dirname(os.path.abspath(__file__)); BASE=os.path.dirname(HERE)
P=json.load(open(HERE+'/hist_payload.json'))
SENS=json.load(open(BASE+'/R3_evidencia/sens_res.json'))
YR=[f'FY{y}' for y in range(2017,2026)]+['LTM']
def blk(k,r0): return {r0+i:(r[1:] if r else [None]*10) for i,r in enumerate(P[k])}
ISR,BSR,CFR=blk('IS',3),blk('BS',3),blk('CF',3)
def N(x): return 0 if x is None else x
def story(tag):
    wb=openpyxl.load_workbook(f'{BASE}/R3_evidencia/motor/{tag}.xlsx',data_only=True);vo=wb['Valuation output'];cols='BCDEFGHIJKLM'
    def row(r): return [vo[f'{c}{r}'].value for c in cols]
    return dict(growth=row(2),rev=row(3),margin=row(4),ebit=row(5),tax=row(6),nopat=row(7),reinv=row(8),fcff=row(9),wacc=row(12),df=row(13),pv=row(14),s2c=row(38),ic=row(39),roic=row(40),
      tv_cf=vo['B16'].value,tv_wacc=vo['B17'].value,tv=vo['B18'].value,pv_tv=vo['B19'].value,pv_cf=vo['B20'].value,sum_pv=vo['B21'].value,op_assets=vo['B24'].value,
      debt=vo['B25'].value,minor=vo['B26'].value,cash=vo['B27'].value,nonop=vo['B28'].value,equity_pre=vo['B29'].value,options=vo['B30'].value,equity=vo['B31'].value,shares=vo['B32'].value,value=vo['B33'].value)
ST={'base':story('base'),'cons':story('cons'),'opt':story('opt')}
PREC=68.59; MOS=0.35
PROB={'cons':0.25,'base':0.5,'opt':0.25}
VAL={k:ST[k]['value'] for k in ST}
EXPECTED=sum(PROB[k]*VAL[k] for k in ST)
MET=['EV/EBITDA','EV/FCFF','P/E','P/FCFE','P/OCF']
PESO={'EV/EBITDA':.10,'EV/FCFF':.06,'P/E':.05,'P/FCFE':.02,'P/OCF':.02}
# libro M · Descuento de múltiplos (lectura 2026-11-10, Ke 10,4875 %): precio+div FY+1..3, VP 1..3 años, consolidado hoy
OBJ={'cons':{'EV/EBITDA':[53.95,59.20,64.98],'EV/FCFF':[35.90,30.76,34.15],'P/E':[52.11,57.50,63.43],'P/FCFE':[23.48,23.18,25.65],'P/OCF':[47.71,53.72,59.05]},
 'base':{'EV/EBITDA':[70.46,86.00,104.45],'EV/FCFF':[47.43,53.40,69.42],'P/E':[100.88,125.15,154.07],'P/FCFE':[35.66,41.57,51.28],'P/OCF':[70.60,86.53,103.62]},
 'opt':{'EV/EBITDA':[86.90,113.26,145.74],'EV/FCFF':[62.69,80.31,111.61],'P/E':[155.06,206.42,269.94],'P/FCFE':[50.57,63.38,81.92],'P/OCF':[94.98,121.83,152.41]}}
VPM={'cons':{'EV/EBITDA':[48.83,48.49,48.17],'EV/FCFF':[32.49,25.20,25.32],'P/E':[47.17,47.10,47.03],'P/FCFE':[21.25,18.99,19.01],'P/OCF':[43.18,44.00,43.78]},
 'base':{'EV/EBITDA':[63.78,70.45,77.44],'EV/FCFF':[42.92,43.75,51.47],'P/E':[91.30,102.52,114.23],'P/FCFE':[32.27,34.05,38.02],'P/OCF':[63.90,70.88,76.83]},
 'opt':{'EV/EBITDA':[78.65,92.78,108.05],'EV/FCFF':[56.74,65.79,82.75],'P/E':[140.34,169.09,200.14],'P/FCFE':[45.77,51.92,60.74],'P/OCF':[85.96,99.80,113.00]}}
_C={'EV/EBITDA':[48.4014351438,72.607723098,97.5898952452],'EV/FCFF':[26.7179363699,47.4449269673,72.4577145047],'P/E':[47.0757948935,106.130270565,178.8644629516],
    'P/FCFE':[19.4544850954,35.6791709437,55.0992055893],'P/OCF':[43.7274107477,72.4576340153,103.6311244464]}
CONS={k:{m:_C[m][i] for m in MET} for i,k in enumerate(('cons','base','opt'))}
MULT={'cons':40.2425894325,'base':70.3068702211,'opt':104.8971285724}
COMB={k:0.75*VAL[k]+0.25*MULT[k] for k in ST}
MULT_EXIT={'EV/EBITDA':(15.96,18.78,21.60),'EV/FCFF':(26.78,31.50,36.23),'P/E':(16.73,28.58,40.42),'P/FCFE':(8.26,9.72,11.18),'P/OCF':(11.09,13.05,15.01)}
HIST_MULT={'EV/EBITDA':dict(y10=None,y5=36.85,y3=36.85,ttm=18.78),'EV/FCFF':dict(y10=None,y5=31.65,y3=31.65,ttm=None),'P/E':dict(y10=None,y5=16.73,y3=16.73,ttm=40.42),
 'P/FCFE':dict(y10=36.41,y5=36.41,y3=18.31,ttm=9.72),'P/OCF':dict(y10=None,y5=26.66,y3=17.66,ttm=13.05)}
MATRICES_M={
 'EV/EBITDA':dict(fila=[16.90,17.84,18.78,19.72,20.66],col=[10611,11200,11790,12379,12969],val=[[85.00,89.61,94.21,98.82,103.42],[89.61,94.47,99.33,104.19,109.05],[94.21,99.33,104.45,109.56,114.68],[98.82,104.19,109.56,114.94,120.31],[103.42,109.05,114.68,120.31,125.94]],unidad='EBITDA FY+3 (M USD)'),
 'EV/FCFF':dict(fila=[28.35,29.93,31.50,33.08,34.65],col=[4161,4392,4624,4855,5086],val=[[56.64,59.66,62.69,65.72,68.75],[59.66,62.86,66.06,69.26,72.45],[62.69,66.06,69.42,72.79,76.16],[65.72,69.26,72.79,76.32,79.86],[68.75,72.45,76.16,79.86,83.56]],unidad='FCFF FY+3 (M USD)'),
 'P/E':dict(fila=[25.72,27.15,28.58,30.01,31.44],col=[10498,11081,11664,12247,12831],val=[[124.80,131.73,138.66,145.60,152.53],[131.73,139.05,146.37,153.69,161.00],[138.66,146.37,154.07,161.77,169.48],[145.60,153.69,161.77,169.86,177.95],[152.53,161.00,169.48,177.95,186.43]],unidad='Utilidad neta FY+3 (M USD)'),
 'P/FCFE':dict(fila=[8.75,9.23,9.72,10.21,10.69],col=[10273,10843,11414,11985,12556],val=[[41.53,43.84,46.15,48.46,50.76],[43.84,46.28,48.71,51.15,53.58],[46.15,48.71,51.28,53.84,56.40],[48.46,51.15,53.84,56.53,59.22],[50.76,53.58,56.40,59.22,62.04]],unidad='FCFE FY+3 (M USD)'),
 'P/OCF':dict(fila=[11.75,12.40,13.05,13.70,14.36],col=[15463,16322,17181,18040,18899],val=[[83.93,88.60,93.26,97.92,102.59],[88.60,93.52,98.44,103.36,108.29],[93.26,98.44,103.62,108.80,113.98],[97.92,103.36,108.80,114.24,119.68],[102.59,108.29,113.98,119.68,125.38]],unidad='OCF FY+3 (M USD)')}
KE=0.1048752249; WACC0=0.0999972388628437; WACC_T=0.08247; ERP=0.0468960207480527
DF3=(1+KE)**-3
def matriz_vp(m):
    """VP por acción: celda×DF3 + (VP3 − centro×DF3). Uber no paga dividendos: el ajuste es solo redondeo."""
    mt=MATRICES_M[m]; c=mt['val'][2][2]; vp3=VPM['base'][m][2]; k=vp3-c*DF3
    return [[x*DF3+k for x in r] for r in mt['val']]
