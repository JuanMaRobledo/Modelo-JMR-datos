"""R5 · cifras de MSFT-REBOOT-3T26-R1: Históricos (SEC XBRL, hist_payload.json), motor original recalculado (R3_evidencia/motor) y lecturas del libro M (2026-11-10)."""
import json,openpyxl,os
HERE=os.path.dirname(os.path.abspath(__file__)); BASE=os.path.dirname(HERE)
P=json.load(open(HERE+'/hist_payload.json'))
SENS=json.load(open(BASE+'/R3_evidencia/sens_res.json'))
YR=[f'FY{y}' for y in range(2017,2027)]+['LTM']
def blk(k,r0): return {r0+i:(r if r else [None]*11) for i,r in enumerate(P[k])}
ISR,BSR,CFR=blk('IS',3),blk('BS',3),blk('CF',3)
def story(tag):
    wb=openpyxl.load_workbook(f'{BASE}/R3_evidencia/motor/{tag}.xlsx',data_only=True);vo=wb['Valuation output'];cols='BCDEFGHIJKLM'
    def row(r): return [vo[f'{c}{r}'].value for c in cols]
    return dict(growth=row(2),rev=row(3),margin=row(4),ebit=row(5),tax=row(6),nopat=row(7),reinv=row(8),fcff=row(9),wacc=row(12),df=row(13),pv=row(14),s2c=row(38),ic=row(39),roic=row(40),
      tv_cf=vo['B16'].value,tv_wacc=vo['B17'].value,tv=vo['B18'].value,pv_tv=vo['B19'].value,pv_cf=vo['B20'].value,sum_pv=vo['B21'].value,op_assets=vo['B24'].value,
      debt=vo['B25'].value,minor=vo['B26'].value,cash=vo['B27'].value,nonop=vo['B28'].value,equity_pre=vo['B29'].value,options=vo['B30'].value,equity=vo['B31'].value,shares=vo['B32'].value,value=vo['B33'].value)
ST={'base':story('base'),'cons':story('cons'),'opt':story('opt')}
PREC=530.61; MOS=0.35
PROB={'cons':0.25,'base':0.5,'opt':0.25}
VAL={k:ST[k]['value'] for k in ST}
EXPECTED=sum(PROB[k]*VAL[k] for k in ST)
MET=['EV/EBITDA','EV/FCFF','P/E','P/FCFE','P/OCF']
PESO={'EV/EBITDA':.08,'EV/FCFF':.08,'P/E':.10,'P/FCFE':.04,'P/OCF':.05}
OBJ={'cons':{'EV/EBITDA':[460.80,483.65,506.97],'EV/FCFF':[317.92,514.23,524.98],'P/E':[427.29,445.91,464.56],'P/FCFE':[289.68,473.29,483.44],'P/OCF':[399.61,424.73,446.49]},
 'base':{'EV/EBITDA':[577.64,659.36,751.94],'EV/FCFF':[460.56,627.80,710.94],'P/E':[537.97,613.43,698.79],'P/FCFE':[420.86,576.19,652.76],'P/OCF':[496.77,571.04,651.97]},
 'opt':{'EV/EBITDA':[687.72,813.39,961.15],'EV/FCFF':[654.23,866.16,1026.44],'P/E':[641.80,759.91,898.86],'P/FCFE':[599.79,796.04,943.65],'P/OCF':[588.77,700.61,828.32]}}
VPM={'cons':{'EV/EBITDA':[416.47,395.45,375.33],'EV/FCFF':[287.34,420.43,388.63],'P/E':[386.19,364.62,344.03],'P/FCFE':[261.81,386.98,357.97],'P/OCF':[361.17,347.31,330.69]},
 'base':{'EV/EBITDA':[522.07,539.00,556.30],'EV/FCFF':[416.26,513.22,526.03],'P/E':[486.22,501.48,517.06],'P/FCFE':[380.37,471.06,483.08],'P/OCF':[448.98,466.85,482.50]},
 'opt':{'EV/EBITDA':[621.56,664.84,710.82],'EV/FCFF':[591.29,707.94,759.02],'P/E':[580.06,621.15,664.84],'P/FCFE':[542.09,650.66,697.90],'P/OCF':[532.13,572.71,612.75]}}
_C={'EV/EBITDA':[389.5949238622,544.2659156963,679.1730077567],'EV/FCFF':[377.9100821861,500.2344858377,710.1511922747],'P/E':[358.6360949198,506.2198414577,634.7744484207],
    'P/FCFE':[347.4388712629,458.9316442837,652.5681418425],'P/OCF':[341.7706277066,471.101143092,584.6159327128]}
CONS={k:{m:_C[m][i] for m in MET} for i,k in enumerate(('cons','base','opt'))}
MULT={'cons':366.4288463191,'base':503.1266834127,'opt':657.0197232969}
COMB={k:0.65*VAL[k]+0.35*MULT[k] for k in ST}
MULT_EXIT={'EV/EBITDA':(16.46,19.36,22.26),'EV/FCFF':(40.55,47.70,54.86),'P/E':(23.49,27.63,31.77),'P/FCFE':(37.91,44.60,51.29),'P/OCF':(17.10,20.12,23.14)}
HIST_MULT={'EV/EBITDA':dict(y10=20.88,y5=23.59,y3=23.59,ttm=19.36),'EV/FCFF':dict(y10=41.64,y5=47.70,y3=56.61,ttm=None),'P/E':dict(y10=34.00,y5=34.97,y3=36.31,ttm=27.63),
 'P/FCFE':dict(y10=38.83,y5=44.60,y3=47.87,ttm=75.64),'P/OCF':dict(y10=23.45,y5=27.15,y3=27.15,ttm=20.12)}
def _m(fila,col,rows): return dict(fila=fila,col=col,val=rows)
MATRICES_M={
 'EV/EBITDA':dict(fila=[17.42,18.39,19.36,20.33,21.30],col=[254500,268639,282778,296917,311056],val=[[596.34,629.50,662.67,695.83,728.99],[629.50,664.51,699.51,734.52,769.52],[662.67,699.51,736.36,773.20,810.05],[695.83,734.52,773.20,811.89,850.58],[728.99,769.52,810.05,850.58,891.11]],unidad='EBITDA FY+3 (M USD)'),
 'EV/FCFF':dict(fila=[42.93,45.32,47.70,50.09,52.47],col=[97547,102966,108386,113805,119224],val=[[563.13,594.45,625.77,657.08,688.40],[594.45,627.51,660.56,693.62,726.67],[625.77,660.56,695.36,730.15,764.95],[657.08,693.62,730.15,766.69,803.23],[688.40,726.67,764.95,803.23,841.50]],unidad='FCFF FY+3 (M USD)'),
 'P/E':dict(fila=[24.87,26.25,27.63,29.01,30.39],col=[165329,174514,183699,192884,202069],val=[[553.40,584.14,614.89,645.63,676.38],[584.14,616.59,649.05,681.50,713.95],[614.89,649.05,683.21,717.37,751.53],[645.63,681.50,717.37,753.24,789.10],[676.38,713.95,751.53,789.10,826.68]],unidad='Utilidad neta FY+3 (M USD)'),
 'P/FCFE':dict(fila=[40.14,42.37,44.60,46.83,49.06],col=[95522,100828,106135,111442,116749],val=[[516.11,544.79,573.46,602.13,630.80],[544.79,575.05,605.32,635.58,665.85],[573.46,605.32,637.18,669.03,700.89],[602.13,635.58,669.03,702.49,735.94],[630.80,665.85,700.89,735.94,770.98]],unidad='FCFE FY+3 (M USD)'),
 'P/OCF':dict(fila=[18.11,19.11,20.12,21.13,22.13],col=[211481,223230,234979,246728,258477],val=[[515.47,544.11,572.75,601.39,630.02],[544.11,574.34,604.57,634.80,665.03],[572.75,604.57,636.39,668.21,700.03],[601.39,634.80,668.21,701.62,735.03],[630.02,665.03,700.03,735.03,770.03]],unidad='OCF FY+3 (M USD)')}
KE=0.10643641356; WACC0=0.104942900273807; WACC_T=0.08247; ERP=0.0452387871345746; BETA=1.27846958822995
DF3=(1+KE)**-3
def matriz_vp(m):
    """VP por acción: celda×DF3 + (VP3 − centro×DF3). El ajuste k es el valor presente de los dividendos de los tres años (MSFT paga dividendo)."""
    mt=MATRICES_M[m]; c=mt['val'][2][2]; vp3=VPM['base'][m][2]; k=vp3-c*DF3
    return [[x*DF3+k for x in r] for r in mt['val']]
