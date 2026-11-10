"""R5 · cifras de MELI-REBOOT-3T26-R1: Históricos (SEC XBRL, hist_payload.json), motor original recalculado (R3_evidencia/motor) y lecturas del libro M (2026-11-10)."""
import json,openpyxl,os
HERE=os.path.dirname(os.path.abspath(__file__)); BASE=os.path.dirname(HERE)
P=json.load(open(HERE+'/hist_payload.json'))
SENS=json.load(open(BASE+'/R3_evidencia/sens_res.json'))
YR=[f'FY{y}' for y in range(2016,2026)]+['LTM']
def blk(k,r0): return {r0+i:(r if r else [None]*11) for i,r in enumerate(P[k])}
ISR,BSR,CFR=blk('IS',3),blk('BS',3),blk('CF',3)
def N(x): return 0 if x is None else x
def story(tag):
    wb=openpyxl.load_workbook(f'{BASE}/R3_evidencia/motor/{tag}.xlsx',data_only=True);vo=wb['Valuation output'];cols='BCDEFGHIJKLM'
    def row(r): return [vo[f'{c}{r}'].value for c in cols]
    return dict(growth=row(2),rev=row(3),margin=row(4),ebit=row(5),tax=row(6),nopat=row(7),reinv=row(8),fcff=row(9),wacc=row(12),df=row(13),pv=row(14),s2c=row(38),ic=row(39),roic=row(40),
      tv_cf=vo['B16'].value,tv_wacc=vo['B17'].value,tv=vo['B18'].value,pv_tv=vo['B19'].value,pv_cf=vo['B20'].value,sum_pv=vo['B21'].value,op_assets=vo['B24'].value,
      debt=vo['B25'].value,minor=vo['B26'].value,cash=vo['B27'].value,nonop=vo['B28'].value,equity_pre=vo['B29'].value,options=vo['B30'].value,equity=vo['B31'].value,shares=vo['B32'].value,value=vo['B33'].value)
ST={'base':story('base'),'cons':story('cons'),'opt':story('opt')}
PREC=1510.0; MOS=0.35
PROB={'cons':0.25,'base':0.5,'opt':0.25}
VAL={k:ST[k]['value'] for k in ST}
EXPECTED=sum(PROB[k]*VAL[k] for k in ST)
MET=['EV/EBITDA','EV/FCFF','P/E','P/FCFE','P/OCF']
PESO={'EV/EBITDA':.12,'EV/FCFF':.03,'P/E':.07,'P/FCFE':.015,'P/OCF':.015}
OBJ={'cons':{'EV/EBITDA':[1524.42,1590.13,1652.36],'EV/FCFF':[170.98,798.77,725.24],'P/E':[1611.06,1653.58,1685.03],'P/FCFE':[841.14,1015.01,1113.28],'P/OCF':[1009.65,1139.10,1247.05]},
 'base':{'EV/EBITDA':[2007.02,2392.39,2855.35],'EV/FCFF':[361.03,1124.09,1349.28],'P/E':[2196.22,2644.25,3183.43],'P/FCFE':[1074.87,1371.59,1640.10],'P/OCF':[1266.91,1555.38,1860.24]},
 'opt':{'EV/EBITDA':[2491.56,3190.66,4085.72],'EV/FCFF':[625.86,1730.64,2354.93],'P/E':[2784.37,3638.57,4739.98],'P/FCFE':[1319.24,1748.24,2183.98],'P/OCF':[1525.06,1963.70,2456.86]}}
VPM={'cons':{'EV/EBITDA':[1362.59,1270.44,1180.02],'EV/FCFF':[152.82,638.18,517.92],'P/E':[1440.03,1321.13,1203.34],'P/FCFE':[751.84,810.94,795.03],'P/OCF':[902.47,910.09,890.56]},
 'base':{'EV/EBITDA':[1793.96,1911.41,2039.11],'EV/FCFF':[322.70,898.10,963.57],'P/E':[1963.07,2112.63,2273.41],'P/FCFE':[960.77,1095.84,1171.26],'P/OCF':[1132.42,1242.68,1328.47]},
 'opt':{'EV/EBITDA':[2227.06,2549.18,2917.76],'EV/FCFF':[559.42,1382.70,1681.74],'P/E':[2488.79,2907.05,3385.00],'P/FCFE':[1179.19,1396.76,1559.66],'P/OCF':[1363.16,1568.90,1754.54]}}
_C={'EV/EBITDA':[1243.6581694449,1951.7691063103,2669.0497716528],'EV/FCFF':[480.9798943775,815.7562598322,1367.5681422152],'P/E':[1286.0164809666,2163.1087758262,3062.3738422425],
    'P/FCFE':[791.1674476329,1106.5354317913,1434.6987511712],'P/OCF':[898.8028442335,1263.5217281611,1620.5720323696]}
CONS={k:{m:_C[m][i] for m in MET} for i,k in enumerate(('cons','base','opt'))}
MULT={'cons':1116.1563408415,'base':1782.6138090373,'opt':2486.0329902995}
COMB={k:0.75*VAL[k]+0.25*MULT[k] for k in ST}
MULT_EXIT={'EV/EBITDA':(15.43,18.15,20.87),'EV/FCFF':(30.0,35.0,40.0),'P/E':(34.43,40.50,46.58),'P/FCFE':(3.71,4.37,5.03),'P/OCF':(4.68,5.51,6.34)}
HIST_MULT={'EV/EBITDA':dict(y10=None,y5=None,y3=None,ttm=18.15),'EV/FCFF':dict(y10=None,y5=None,y3=None,ttm=None),'P/E':dict(y10=80.72,y5=80.72,y3=51.14,ttm=40.50),
 'P/FCFE':dict(y10=38.22,y5=11.92,y3=9.51,ttm=4.37),'P/OCF':dict(y10=43.94,y5=14.47,y3=10.89,ttm=5.51)}
MATRICES_M={
 'EV/EBITDA':dict(fila=[16.34,17.24,18.15,19.06,19.97],col=[6865,7246,7627,8009,8390],val=[[2331.76,2455.77,2579.78,2703.78,2827.79],[2455.77,2586.67,2717.56,2848.46,2979.35],[2579.78,2717.56,2855.35,2993.13,3130.92],[2703.78,2848.46,2993.13,3137.81,3282.48],[2827.79,2979.35,3130.92,3282.48,3434.04]],unidad='EBITDA FY+3 (M USD)'),
 'EV/FCFF':dict(fila=[31.50,33.25,35.00,36.75,38.50],col=[1614,1704,1794,1883,1973],val=[[1111.85,1168.08,1224.32,1280.55,1336.78],[1168.08,1227.44,1286.80,1346.16,1405.51],[1224.32,1286.80,1349.28,1411.76,1474.24],[1280.55,1346.16,1411.76,1477.37,1542.97],[1336.78,1405.51,1474.24,1542.97,1611.70]],unidad='FCFF FY+3 (M USD)'),
 'P/E':dict(fila=[36.45,38.48,40.50,42.53,44.55],col=[3554,3751,3949,4146,4344],val=[[2578.58,2721.84,2865.09,3008.34,3151.60],[2721.84,2873.05,3024.26,3175.47,3326.69],[2865.09,3024.26,3183.43,3342.60,3501.78],[3008.34,3175.47,3342.60,3509.73,3676.87],[3151.60,3326.69,3501.78,3676.87,3851.95]],unidad='Utilidad neta FY+3 (M USD)'),
 'P/FCFE':dict(fila=[3.93,4.15,4.37,4.59,4.81],col=[16969,17911,18854,19797,20740],val=[[1328.48,1402.29,1476.09,1549.90,1623.70],[1402.29,1480.19,1558.10,1636.00,1713.91],[1476.09,1558.10,1640.10,1722.11,1804.11],[1549.90,1636.00,1722.11,1808.21,1894.32],[1623.70,1713.91,1804.11,1894.32,1984.53]],unidad='FCFE FY+3 (M USD)'),
 'P/OCF':dict(fila=[4.96,5.23,5.51,5.79,6.06],col=[15264,16112,16960,17808,18656],val=[[1506.80,1590.51,1674.22,1757.93,1841.64],[1590.51,1678.87,1767.23,1855.59,1943.95],[1674.22,1767.23,1860.24,1953.26,2046.27],[1757.93,1855.59,1953.26,2050.92,2148.58],[1841.64,1943.95,2046.27,2148.58,2250.89]],unidad='OCF FY+3 (M USD)')}
KE=0.11876602146; WACC0=0.116666277042492; WACC_T=0.08247; ERP=0.0755632905523451; BETA=0.928572868494608
DF3=(1+KE)**-3
def matriz_vp(m):
    """VP por acción: celda×DF3 + (VP3 − centro×DF3). MELI no paga dividendos: el ajuste es solo redondeo."""
    mt=MATRICES_M[m]; c=mt['val'][2][2]; vp3=VPM['base'][m][2]; k=vp3-c*DF3
    return [[x*DF3+k for x in r] for r in mt['val']]
