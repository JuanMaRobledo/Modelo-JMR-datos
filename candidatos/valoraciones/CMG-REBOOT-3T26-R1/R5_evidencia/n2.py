from datos import *
from fmt import *
from n1 import rev,cost,ebit,ni,ga,da,cfo,capex,bb,fcf,rm,em,b,c,o,vb,vc,vo,px,mos_price,cash,leases,mexp
YR=[f'FY{y}' for y in FY]+['LTM']
def row(label,vals,d=0): return [label]+[f(x,d) for x in vals]
def prow(label,vals,d=1): return [label]+[p(x,d) for x in vals]
def H4(t): return f'<h4>{t}</h4>'
def proj(st,name):
    yrs=['Año base']+[f'Año {i}' for i in range(1,11)]+['Terminal']
    L=[('Crecimiento de ingresos',[None]+st['growth'][1:],'p'),('Ingresos',st['rev'],'n'),('Margen EBIT',st['margin'],'p'),('EBIT',st['ebit'],'n'),('Tasa de impuestos',st['tax'],'p'),
       ('EBIT(1−t)',st['nopat'],'n'),('Reinversión',st['reinv'],'n'),('FCFF',st['fcff'],'n'),('Costo de capital',st['wacc'],'p2'),('Factor de descuento acumulado',st['df'],'d'),
       ('VP(FCFF)',st['pv'],'n'),('Ventas/capital',st['s2c'],'d1'),('Capital invertido',st['ic'],'n'),('ROIC',st['roic'],'p')]
    rows=[]
    for lab,v,k in L:
        out=[lab]
        for x in v:
            out.append('—' if x is None else p(x,1) if k=='p' else p(x,2) if k=='p2' else f(x,4) if k=='d' else f(x,1) if k=='d1' else f(x,0))
        rows.append(out)
    return H4(f'Historia {name}')+table(['Concepto']+yrs,rows)
def bridge(st,name):
    return [name,f(st['pv_cf'],0),f(st['tv'],0),f(st['pv_tv'],0),f(st['sum_pv'],0),p(st['pv_tv']/st['sum_pv'],0),f(st['cash'],0),f(st['nonop'],0),f(-st['options'],0),f(st['equity'],0),f(st['shares'],1),usd(st['value'],4)]
def n2():
    h=['<h2>Nivel 2 · Valoración reproducible</h2>']
    h.append(H3('1. Identificación, fuentes y unidades'))
    h.append(table(['Concepto','Valor'],[
      ['Empresa / ticker','Chipotle Mexican Grill, Inc. · CMG · NYSE · USD · millones salvo por acción'],
      ['Revisión','CMG-REBOOT-3T26-R1 · perfil Reboot · contrato jmr-reboot-3libros-v1 (reconfiguración de CMG-FLOYD-20261108-R1)'],
      ['Corte contable / precio','30-sep-2026 (10-Q 3T-2026, acc. 0001058090-26-000104) · precio 34,43 (cierre 6-nov-2026, Alpha Vantage)'],
      ['Libro Históricos','1fWez5DOCZv7RBUCCzKgrEUZa4imFmRCyVzFxuxirizI'],
      ['Libro DCF Base / Conservadora / Optimista','1asO4BR42MypptINAooJ3hP6joY5fFUYDB5IM2NSDo7U / 1i5Sc_uoJX6cnvq9wDjr4jP0XtMIE5c1vtlDDEBfz_qU / 1hSctlkSB4-mUMZPxwtnGpKLWaH8Bn_Ymzhdowh6mpzQ'],
      ['Libro Múltiplos','1jdUkjDwPG79FmSGLbZfQd-xTXMVBC8xJ9wG2imACeK0'],
      ['Documento de análisis','__DOC__'],
      ['Fuentes','SEC XBRL <em>companyfacts</em> CIK 0001058090 (primaria); texto del 10-Q 3T-2026; Alpha Vantage (precios); FRED DGS10 (tasa libre); Damodaran nov-2026 (prima) y tablas de industria del motor (enero 2026)'],
      ['Motor','fcffsimpleginzu original de Damodaran; entradas en Input sheet, Cost of capital worksheet y Country equity risk premiums B1; cálculo iterativo habilitado para la hoja de opciones. Integridad de las 1.230 fórmulas y 76 comentarios NO re-verificada en estas copias']]))
    h.append(H3('2. Estados históricos y LTM'))
    h.append(P('LTM = FY2025 + 9M-2026 − 9M-2025 (flujos) y saldos al 30-sep-2026. Acciones ajustadas por el split 50:1 de junio de 2024. Impuestos de FY2018 corregidos a +91,9 (el XBRL traía el signo invertido).'))
    h.append(table(['Estado de resultados']+YR,[row('Ingresos',rev),row('Costos del restaurante (costo de ventas)',cost),row('Utilidad bruta (margen del restaurante)',[a-b_ for a,b_ in zip(rev,cost)]),row('Gastos generales',ga),row('Depreciación y amortización',da),
      row('Otros gastos operativos (pre-apertura, deterioro)',s(IS,11)),row('EBIT',ebit),row('Impuestos',s(IS,20)),row('Utilidad neta',ni),row('Acciones diluidas promedio',s(IS,26),0)]))
    h.append(table(['Balance']+YR,[row('Efectivo + inversiones CP',[a+b_ for a,b_ in zip(s(BS,3),s(BS,4))]),row('Inversiones LP',[x or 0 for x in s(BS,14)]),row('Activos totales',s(BS,16)),
      row('Deuda financiera',[0]*11),row('Pasivos por arrendamiento (no se tratan como deuda)',[a+b_ for a,b_ in zip(s(BS,21),s(BS,26))]),row('Patrimonio',s(BS,34))]))
    h.append(table(['Flujo de caja']+YR,[row('Flujo operativo',cfo),row('Capex',capex),row('Flujo libre (CFO−capex)',fcf),row('Recompras',bb),row('Compensación en acciones',s(CF,5)),row('Otros ajustes (derivado)',s(CF,6))]))
    h.append(H3('3. Ratios y economía del negocio'))
    h.append(table(['Ratio']+YR,[prow('Crecimiento de ingresos',[None]+[rev[i]/rev[i-1]-1 for i in range(1,10)]+[rev[10]/11787.4-1]),prow('Margen del restaurante',rm),prow('Margen EBIT',em),prow('Margen neto',[a/b_ for a,b_ in zip(ni,rev)]),
      prow('Tasa de impuestos efectiva',[a/b_ for a,b_ in zip(s(IS,20),s(IS,19))]),prow('Gastos generales / ingresos',[a/b_ for a,b_ in zip(ga,rev)]),prow('Capex / ingresos',[a/b_ for a,b_ in zip(capex,rev)]),
      prow('Flujo libre / ingresos',[a/b_ for a,b_ in zip(fcf,rev)]),prow('Recompras / flujo libre',[a/b_ for a,b_ in zip(bb,fcf)],0)]))
    h.append(P(f'Datos operativos del 10-Q 3T-2026: 4.267 restaurantes propios (3.916 un año antes) y 20 de socios; 233 aperturas en nueve meses; ventas comparables +2,1 % en el trimestre y +1,6 % en nueve meses; ventas promedio por restaurante 3,106 M (−0,8 %); ventas digitales 38,8 %. Costos como porcentaje de ingresos en nueve meses de 2026 (y 2025): comida 29,6 % (29,4 %), mano de obra 25,6 % (25,0 %), ocupación 5,4 % (5,2 %), otros costos operativos 15,5 % (14,5 %). Salud financiera: caja e inversiones CP {f(cash)} M, sin deuda financiera; liquidez corriente {f(s(BS,10)[10]/s(BS,24)[10],2)}x; arrendamientos {f(leases)} M.'))
    h.append(H3('4. Puente contable a económico'))
    h.append(table(['Concepto','Valor','Nota'],[
      ['EBIT LTM',f(ebit[10],1),'Reportado; sin I+D que capitalizar (R&D = No)'],
      ['Arrendamientos',f(leases),'No se convierten ni se restan como deuda: el EBIT ya deduce el alquiler (decisión del usuario, 10-nov-2026). <em>Operating lease commitments</em> = No; deuda = 0'],
      ['Capital invertido (año base)',f(b['ic'][0],1),'Patrimonio 2.455,1 + deuda 0 − caja 902,6'],
      ['Caja e inversiones CP',f(cash,1),'Efectivo 634,2 + inversiones CP 268,4'],
      ['Activos no operativos','100,4','Inversiones de largo plazo'],
      ['Acciones (millones)','1.270,149','1.264,975 (portada del 10-Q) + 4,138 RSU + 1,036 PSU esperadas'],
      ['Opciones (SOSARs)','12,268 M · ejercicio 39,51 · 4,2 años','10-Q Nota 7; volatilidad 35 % (supuesto); valor 126,7 M restado del patrimonio'],
      ['Tasa efectiva / marginal','24,74 % / 25 %','452,7 / 1.829,8 LTM']]))
    h.append(H3('5. Supuestos efectivos por historia'))
    h.append(table(['Entrada del motor','Celda','Conservadora','Base','Optimista'],[
      ['Crecimiento año 1','Input B26','6,4 %','9,5 %','11,0 %'],['Margen EBIT año 1','B27','14,12 %','14,12 %','14,12 %'],['CAGR años 2–5','B28','6,4 %','8,8 %','10,9 %'],
      ['Margen objetivo','B29','13,0 %','16,0 %','18,0 %'],['Año de convergencia del margen','B30','5','5','5'],['Ventas/capital años 1–5 · 6–10','B31 · B32','2,2 · 2,4','2,7 · 2,9','2,9 · 3,2'],
      ['ROIC terminal','B48 · B49','Costo de capital','18,36 %','18,36 %'],['Fracaso','B51','No','No','No'],['Tasa libre','B34','4,86 %','4,86 %','4,86 %'],['Crecimiento terminal','B68','4,0 %','4,0 %','4,0 %'],
      ['Opciones','B37–B41','Sí · 12,268 · 39,51 · 4,2 · 35 %','igual','igual']]))
    h.append(P('Cambios frente a la revisión Floyd (33,04 Base): ROIC terminal por la regla del contrato (18,36 % en vez de 22 %; costo de capital en vez de 15 % en la Conservadora; 18,36 % en vez de 28 % en la Optimista), crecimiento como año 1 + CAGR 2–5 en lugar de trayectoria anual, tasa libre 4,86 % (antes 4,94 %) y beta de industria 0,783 (antes 0,86).'))
    h.append(H3('6. Costo de capital descompuesto'))
    h.append(table(['Componente','Valor','Fuente / criterio'],[
      ['Tasa libre','4,86 %','FRED DGS10, 6-nov-2026'],['Beta desapalancada = apalancada','0,783','Restaurant/Dining (Single Business US); deuda 0'],
      ['Prima de riesgo','3,603 %','100 % de los ingresos en Norteamérica; madura 3,387 % (Damodaran nov-2026)'],['Costo del patrimonio (Ke)',p(KE,4),'4,86 % + 0,783 × 3,603 %'],
      ['Costo de la deuda','5,86 % (entrada directa)','Sin efecto: peso de la deuda 0 %'],['Pesos de mercado','100 % / 0 %','Capitalización ≈ 43.731 M'],
      ['Costo de capital inicial (años 1–5)',p(WACC0,2),'Común a las tres historias'],['Costo de capital terminal (año 10)',p(WACC_T,2),'Beta 1: 4,86 % + 3,387 %; sube linealmente en los años 6–10']]))
    h.append(H3('7. Proyección explícita anual completa'))
    h.append(P('Millones de USD. Motor original recalculado localmente (LibreOffice), igual a Google Sheets en las tres historias (diferencia < 1e-4 por acción).'))
    h.append(proj(c,'Conservadora (25 %)')+proj(b,'Base (50 %)')+proj(o,'Optimista (25 %)'))
    h.append(H3('8. Valor terminal y puente hasta la acción'))
    h.append(table(['Historia','VP flujos años 1–10','Valor terminal','VP valor terminal','Activos operativos','VP terminal / total','+ Caja','+ No operativos','− Opciones','Patrimonio','Acciones','Valor por acción'],
      [bridge(c,'Conservadora'),bridge(b,'Base'),bridge(o,'Optimista')]))
    h.append(P(f'Base: flujo terminal {f(b["tv_cf"])} M a costo de capital {p(b["tv_wacc"],2)} y g = 4,0 % → VT {f(b["tv"])} M. Reinversión terminal = g / ROIC = {p(0.04/0.1836,1)} del NOPAT en Base y Optimista; en la Conservadora, {p(0.04/WACC_T,1)} (ROIC = costo de capital). Deuda y minoritarios: 0.'))
    h.append(H3('9. Escenarios y ciclos'))
    h.append(table(['Historia','Probabilidad','Valor DCF','Frente al precio','Aporte al esperado'],[
      ['Conservadora','25 %',usd(vc),p(vc/px-1),usd(.25*vc)],['Base','50 %',usd(vb),p(vb/px-1),usd(.5*vb)],['Optimista','25 %',usd(vo),p(vo/px-1),usd(.25*vo)],
      ['<strong>Valor esperado</strong>','100 %','<strong>'+usd(EXPECTED)+'</strong>',p(EXPECTED/px-1),usd(EXPECTED)]]))
    h.append(P(f'Tipo de historia «crecimiento maduro»: 50 / 25 / 25. Orden Conservadora ≤ Base ≤ Optimista: cumple. Costo de capital común: cumple. <strong>MOS de 35 % solo sobre el DCF Base:</strong> 0,65 × {usd(vb,4)} = {usd(mos_price)}; con la Conservadora daría {usd(vc*.65)} (informativo). Ciclo: crecimiento de ingresos FY2021 26,1 %, FY2022 14,4 %, FY2023 14,3 %, FY2024 14,6 %, FY2025 5,4 %, LTM 7,9 %; margen EBIT FY2024 16,9 %, FY2025 16,2 %, LTM 14,1 %.'))
    h.append(H3('10. Cinco múltiplos prioritarios'))
    h.append(P('Libro Múltiplos (sistema Atlas; sin P/S ni P/BV), con los supuestos del DCF: crecimiento 9,5/6,4/11,0 % y 8,8/6,4/10,9 %, margen objetivo 16/13/18 %, impuesto 24,74 %. Arrendamientos reclasificados a otros pasivos: deuda financiera 0 y EV = capitalización − caja. Múltiplo de salida: Base = actual; Conservadora = actual −15 %; Optimista = actual +15 %. No se usan las medianas históricas porque superan el múltiplo actual (tope «Conservador ≤ actual»).'))
    rows=[]
    for m in MET:
        e=MULT_EXIT[m]; hm=HIST_MULT[m]
        rows.append([m,p(PESO[m],0),f(hm['y10'],2),f(hm['y5'],2),f(hm['y3'],2),f(hm['ttm'],2) if hm['ttm'] else 'N/D (42,62 en FY2025)',f(e[0],2),f(e[1],2),f(e[2],2)])
    h.append(table(['Método','Peso total','Mediana 10 a','Mediana 5 a','Mediana 3 a','Actual (LTM)','Salida Cons.','Salida Base','Salida Opt.'],rows))
    for k,name in (('cons','Conservadora'),('base','Base'),('opt','Optimista')):
        rr=[[m]+[f(x,2) for x in OBJ[k][m]]+[f(x,2) for x in VPM[k][m]]+[f(CONS[k][m],2)] for m in MET]
        rr.append(['<strong>Consolidado</strong>','','','','','','','<strong>'+f(MULT[k],2)+'</strong>'])
        h.append(H4(f'Descuento a valor presente · {name}')+table(['Método','Precio FY+1','FY+2','FY+3','VP 1 año','VP 2 años','VP 3 años','Consolidado hoy'],rr))
    h.append(P(f'Sin dividendos. Pesos de los años 1/2/3: 20 % / 30 % / 50 % sobre valores presentes. Ke {p(KE,2)} en los tres escenarios. Ponderación «Madura»: DCF 65 % y múltiplos 35 % (8/5/12/7/3 %). Combinado secundario: {usd(COMB["cons"])} / {usd(COMB["base"])} / {usd(COMB["opt"])}. El libro de Múltiplos no resta el valor de las opciones (≈ 0,10 por acción). Avisos del libro: P/OCF «REVISAR · AJUSTES >10 %» y EV/EBITDA «COMPROBAR D&A».'))
    h.append(H3('11. Sensibilidades DCF y de múltiplos + DCF inverso'))
    GL=[0.068,0.078,0.088,0.098,0.108];ML=[0.14,0.15,0.16,0.17,0.18];DW=[-0.01,-0.005,0,0.005,0.01];TG=[0.03,0.035,0.04,0.045,0.048]
    A=[[f(SENS[f'a_{i}_{j}'],2) for j in range(5)] for i in range(5)];B=[[f(SENS[f'b_{i}_{j}'],2) for j in range(5)] for i in range(5)]
    h.append(H4('Matriz A · CAGR años 2–5 × margen objetivo (precio por acción; centro = DCF Base)'))
    h.append(table(['CAGR \\ margen']+[p(m,0) for m in ML],[[p(g,1)]+A[i] for i,g in enumerate(GL)]))
    h.append(H4('Matriz B · costo de capital inicial × crecimiento terminal (precio por acción; centro = DCF Base)'))
    h.append(table(['Costo de capital inicial \\ g']+[p(t,1) for t in TG],[[p(WACC0+d,2)]+B[i] for i,d in enumerate(DW)]))
    av=[SENS[k] for k in SENS if k.startswith('a_')];bv=[SENS[k] for k in SENS if k.startswith('b_')]
    h.append(P(f'Rango A: {usd(min(av))} a {usd(max(av))}; rango B: {usd(min(bv))} a {usd(max(bv))}. Centro de ambas = {usd(vb,4)} (conciliado). El precio de {usd(px)} queda dentro de los dos rangos.'))
    h.append(H4('DCF inverso (una variable a la vez)'))
    h.append(table(['Variable que se resuelve','Valor necesario','Base','Resultado'],[
      ['Crecimiento anual años 1–5',p(SENS['crecimiento'],2),'9,5 % / 8,8 %',usd(px)],['Margen objetivo',p(SENS['margen'],2),'16,0 %',usd(px)],
      ['Crecimiento con margen fijo de 18 %',p(SENS['crec_con_margen18'],2),'9,5 % / 8,8 %',usd(px)],['Costo de capital inicial',p(SENS['wacc'],2),p(WACC0,2),usd(px)]]))
    h.append(H4('Matrices 5×5 por múltiplo (solo Base) · valor presente por acción'))
    h.append(P('Origen: hoja de cada método del libro Múltiplos (precio FY+3 = múltiplo elegido × fundamental FY+3). Cada celda se descontó con el factor de 3 años del Ke Base (' + f(DF3,4) + '); CMG no paga dividendos, así que el ajuste al centro es solo de redondeo y el centro coincide con el VP3 Base de la hoja de Descuento. Derivación declarada; la hoja conserva el precio FY+3 sin descontar.'))
    for m in MET:
        mt=MATRICES_M[m]; V=matriz_vp(m)
        h.append(H4(f'{m} · centro VP3 = {usd(VPM["base"][m][2])}'))
        h.append(table([f'{m} \\ {mt["unidad"]}']+[f(x,0) for x in mt['col']],[[f(mt['fila'][i],2)+'x']+[f(x,2) for x in V[i]] for i in range(5)]))
    h.append(H3('12. Trazabilidad, reconciliaciones y límites'))
    h.append(table(['Control','Estado'],[
      ['Réplica local del motor vs Google Sheets (tres historias)','APROBADO: 17,6858 / 32,2837 / 40,4675'],
      ['Integridad de fórmulas y comentarios del motor en estas copias','NO re-verificada (pendiente R6)'],
      ['Costo de capital común (7,68 % inicial; 8,25 % estable)','APROBADO'],
      ['Probabilidades = 100 %; Cons ≤ Base ≤ Opt; costo de capital estable > g','APROBADO'],
      ['MOS 35 % solo sobre DCF Base','APROBADO'],
      ['Libro Múltiplos: compuerta «LISTA PARA CALCULAR»; Resumen de valoraciones CONCILIADO (6 controles)','APROBADO'],
      ['Balance cuadra en los 11 períodos; CFO+CFI+CFF vs variación de caja ≤ 2','APROBADO'],
      ['Huellas del traspaso D↔M','Hash SHA-256 de los valores transferidos (no del libro completo)'],
      ['Verificación documental contra 10-K/10-Q','PENDIENTE'],
      ['«Otros ajustes» del flujo de caja LTM (804 M)','PENDIENTE; no afecta el DCF; afecta el CFO proyectado de P/OCF'],
      ['Volatilidad de las opciones (35 %) y beta de industria (0,783; tabla de enero 2026)','SUPUESTOS declarados'],
      ['EV/FCFF LTM','N/D en el libro; se usó el de FY2025 (42,62x) como actual'],
      ['Auditoría económica independiente','NO_EJECUTADA (R6)'],
      ['<code>AISLAMIENTO=OK</code>','La revisión Floyd se usó solo como punto de partida de las historias y como contraste; ningún dato contable proviene de ella']]))
    return ''.join(h)
