from datos import *
from fmt import *
from n1 import rev,cogs,sga,da,rd,ebit,oth,intinc,intexp,nonop,ebt,tax,ni,nic,dsh,cfo,capex,sbc,bb,fcf,gm,em,b,c,o,vb,vc,vo,px,mos_price,cap,leases,mexp,gl
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
    return [name,f(st['pv_cf'],0),f(st['tv'],0),f(st['pv_tv'],0),f(st['sum_pv'],0),p(st['pv_tv']/st['sum_pv'],0),f(-st['debt'],0),f(-st['minor'],0),f(st['cash'],0),f(st['nonop'],0),f(-st['options'],0),f(st['equity'],0),f(st['shares'],1),usd(st['value'],4)]
def bsx(r):  # el balance de FY2017 no está completo en las fuentes
    return [None]+r[1:]
def n2():
    h=['<h2>Nivel 2 · Valoración reproducible</h2>']
    h.append(H3('1. Identificación, fuentes y unidades'))
    h.append(table(['Concepto','Valor'],[
      ['Empresa / ticker','Uber Technologies, Inc. · UBER · NYSE · USD · millones salvo por acción'],
      ['Revisión','UBER-REBOOT-3T26-R1 · perfil Floyd R1–R6 (antes Reboot) · contrato jmr-reboot-3libros-v1 (reconfiguración de UBER-FLOYD-3T26)'],
      ['Corte contable / precio','30-sep-2026 (10-Q 3T-2026) · precio 68,59 (cierre 6-nov-2026, Alpha Vantage)'],
      ['Libro Históricos','176tcVAz_RzHluf4kyjEEsMjDcDosldPdB5FBifO9YQA'],
      ['Libro DCF Base / Conservadora / Optimista','14QlydMFli2pxdG4agUYOAXL8QIE99P-3UDE7vwK8CaM / 1TUDP8WvRpjtm5AbCpGkKkfyAlItRuufIAAEkFp95aHA / 1f7Fzs7TBezRNa4E0lwHoh8fcPXTGn0d09HTatCaDLRU'],
      ['Libro Múltiplos','19fe8FcQ32d3yf169i-XA7F-c4IGhWTCNl_QO4WgCwA4'],
      ['Documento de análisis','__DOC__'],
      ['Fuentes','SEC XBRL <em>companyfacts</em> CIK 0001543151 (primaria); texto del 10-Q 3T-2026 y del 10-K FY2025; Alpha Vantage (precios); FRED DGS10 (tasa libre); Damodaran nov-2026 (prima) y tablas de industria del motor (enero 2026)'],
      ['Motor','fcffsimpleginzu original de Damodaran; entradas en Input sheet, Cost of capital worksheet, R&amp;D converter y Country equity risk premiums B1; cálculo iterativo habilitado para la hoja de opciones. Integridad de las fórmulas y los comentarios NO re-verificada en estas copias']]))
    h.append(H3('2. Estados históricos y LTM'))
    h.append(P('LTM = FY2025 + 9M-2026 − 9M-2025 (flujos) y saldos al 30-sep-2026. Fuente SEC XBRL cargada en el libro de Históricos. «Otros operativos» = ingresos − costo de ingresos − ventas y administración − D&A − I+D − EBIT (operaciones y soporte, litigios y otros, derivado). Los arrendamientos se reclasificaron a otros pasivos (la deuda financiera no los incluye). El balance de FY2017 no está completo en las fuentes (N/D).'))
    h.append(table(['Estado de resultados']+YR,[row('Ingresos',rev),row('Costo de ingresos',cogs),row('Ventas y marketing + G&A',sga),row('Depreciación y amortización',da),row('Investigación y desarrollo',rd),row('Otros operativos (derivado)',oth),
      row('EBIT (resultado operativo)',ebit),row('Ingresos por intereses',intinc),row('Gasto por intereses',intexp),row('Otros no operativos (principalmente revaluación de inversiones)',nonop),row('Utilidad antes de impuestos',ebt),row('Impuestos (− = beneficio)',tax),row('Utilidad neta consolidada',ni),row('Acciones diluidas promedio',dsh,1)]))
    h.append(table(['Balance']+YR,[row('Efectivo',bsx(BSR[3])),row('Inversiones CP',bsx([N(x) for x in BSR[4]])),row('Total activos',bsx(BSR[16])),row('Deuda de largo plazo (sin arrendamientos)',bsx(BSR[25])),row('Otros pasivos no corrientes (incluye arrendamientos y reservas)',bsx(BSR[27])),row('Patrimonio total (con no controladoras)',bsx(BSR[35]))]))
    h.append(table(['Flujo de caja']+YR,[row('Flujo operativo',cfo),row('Capex',capex),row('Flujo libre (CFO−capex)',fcf),row('Recompras',bb),row('Compensación en acciones',sbc),row('Otros ajustes',CFR[6][0:10])]))
    h.append(H3('3. Ratios y economía del negocio'))
    h.append(table(['Ratio']+YR,[prow('Crecimiento de ingresos',[None]+[rev[i]/rev[i-1]-1 for i in range(1,9)]+[gl]),prow('Margen bruto',gm),prow('Margen EBIT',em),prow('Margen neto',[a/b_ for a,b_ in zip(ni,rev)]),
      prow('Tasa de impuestos efectiva',[a/b_ for a,b_ in zip(tax,ebt)]),prow('I+D / ingresos',[a/b_ for a,b_ in zip(rd,rev)]),prow('Compensación en acciones / ingresos',[a/b_ for a,b_ in zip(sbc,rev)]),prow('Capex / ingresos',[a/b_ for a,b_ in zip(capex,rev)]),
      prow('Flujo libre / ingresos',[a/b_ for a,b_ in zip(fcf,rev)]),prow('Recompras / flujo libre',[a/b_ if a else None for a,b_ in zip(bb,fcf)],0)]))
    h.append(P('Datos del 10-Q 3T-2026: consumidores activos 215 M (+14 %), viajes 4.061 M (+16 %), reservas brutas 59.819 M (+20 %), ingresos 14.766 M (+10 %), resultado operativo 1.447 M (+30 %), utilidad neta atribuible 512 M (6.626 M un año antes). Nueve meses: flujo operativo 7.852 M (7.216 M), flujo libre 7.613 M (6.955 M), recompras 4.279 M (4.611 M). Segmentos del trimestre: Mobility ingresos −2 % (−162 M; cambio de modelo en el Reino Unido −1.100 M) y resultado operativo +498 M; Delivery ingresos +23 % y resultado +246 M; Freight ingresos +34 % y pérdida −7 M. Pasivos: deuda de largo plazo 15.664 M (10.521 M al cierre de FY2025), arrendamientos operativos 1.897 + 176 M, reservas de seguros 4.220 + 9.489 M, redimibles no controladoras 388 M.'))
    h.append(H3('4. Puente contable a económico'))
    h.append(table(['Concepto','Valor','Nota'],[
      ['EBIT LTM (contable)',f(ebit[9],1),'Reportado'],
      ['EBIT ajustado por I+D capitalizada',f(7961,0),'I+D LTM 4.152; FY2025 3.402; FY2024 3.109; FY2023 3.164; vida 3 años; margen ajustado 14,08 %'],
      ['Arrendamientos',f(leases),'No se restan como deuda: el EBIT ya deduce el alquiler (decisión del usuario, 10-nov-2026)'],
      ['Capital invertido (año base)',f(b['ic'][0],1),'Incluye I+D capitalizada'],
      ['Deuda',f(b['debt'],0),'Deuda de largo plazo neta (incluye notas convertibles y canjeables); sin arrendamientos'],
      ['Caja e inversiones CP',f(b['cash'],0),'Efectivo 9.558 + inversiones CP 510; excluye caja e inversiones restringidas (11.372), que respaldan las reservas de seguros (13.709)'],
      ['Activos no operativos',f(b['nonop'],0),'Inversiones 7.975 (Didi 2.061; Grab 1.667; Aurora 870; otras) + método de participación 3.498 (Delivery Hero 3.372), a valor en libros'],
      ['Minoritarios',f(b['minor'],0),'No redimibles 916 + redimibles 388 (valor en libros)'],
      ['Acciones (millones)',f(b['shares'],3),'2.041,898 (portada del 10-Q) + 65,539 RSU no devengadas (todas; conservador)'],
      ['Opciones','5,549 M · ejercicio 52,23 · 4,27 años','10-Q Nota 7; volatilidad 40 % (supuesto); valor '+f(b['options'],1)+' M restado del patrimonio'],
      ['Tasa efectiva / marginal','25,17 % / 25 %','1.238 / 4.919 LTM; FY2024–25 con beneficio por liberación de provisión, no representativo']]))
    h.append(H3('5. Supuestos efectivos por historia'))
    h.append(table(['Entrada del motor','Celda','Conservadora','Base','Optimista'],[
      ['Crecimiento año 1','Input B26','7,0 %','11,0 %','13,0 %'],['Margen EBIT año 1 (ajustado)','B27','14,08 %','14,08 %','14,08 %'],['CAGR años 2–5','B28','9,75 %','14,0 %','16,25 %'],
      ['Margen objetivo (ajustado)','B29','13,0 %','18,0 %','22,0 %'],['Año de convergencia del margen','B30','5','5','5'],['Ventas/capital años 1–5 · 6–10','B31 · B32','2,0 · 1,8','2,8 · 2,5','3,4 · 3,0'],
      ['ROIC terminal','B48 · B49','Costo de capital','13,23 %','18,21 %'],['Fracaso','B51','No','No','No'],['Tasa libre','B34','4,86 %','4,86 %','4,86 %'],['Crecimiento terminal','B68','4,0 %','4,0 %','4,0 %'],
      ['Opciones','B37–B41','Sí · 5,549 · 52,23 · 4,27 · 40 %','igual','igual'],['I+D capitalizada','B16','Sí · 3 años','igual','igual']]))
    h.append(P('Cambios frente a la revisión Floyd F1–F5 (Base 100,19): costo de capital inicial 10,00 % (beta 1,20, ERP 4,69 %) frente a 9,37 % (ERP 4,08 %), ROIC terminal por la regla del contrato (13,23 % Base, 18,21 % Optimista, costo de capital en la Conservadora, frente a 14 / 17 / 9 %), crecimiento como año 1 + CAGR 2–5, año 1 Base de 11 % por el efecto del Reino Unido, y activos no operativos 11.473 frente a 12.567.'))
    h.append(H3('6. Costo de capital descompuesto'))
    h.append(table(['Componente','Valor','Fuente / criterio'],[
      ['Tasa libre','4,86 %','FRED DGS10, 6-nov-2026'],['Beta apalancada','1,20','Entrada directa por decisión del usuario; la beta ascendente por industrias daba 0,822 (Base 108,62)'],
      ['Prima de riesgo',p(ERP,3),'Ingresos LTM por región: Norteamérica 29.543 (3,60 %), EMEA 15.905 (5,87 %), Asia 6.987 (4,88 %), Latinoamérica 4.091 (7,62 %); madura 3,387 % (Damodaran nov-2026)'],['Costo del patrimonio (Ke)',p(KE,4),'4,86 % + 1,20 × '+p(ERP,3)],
      ['Costo de la deuda','6,10 % antes de impuestos (entrada directa)','Estimación: tasa libre + ≈1,25 puntos de diferencial; vencimiento medio 7,5 años; no verifiqué la calificación'],['Pesos de mercado','91,75 % / 8,25 %','Capitalización 144.549; deuda a mercado 12.998'],
      ['Costo de capital inicial (años 1–5)',p(WACC0,2),'Común a las tres historias'],['Costo de capital terminal (año 10)',p(WACC_T,2),'Sube/baja linealmente en los años 6–10']]))
    h.append(H3('7. Proyección explícita anual completa'))
    h.append(P('Millones de USD. Motor original recalculado localmente (LibreOffice), igual a Google Sheets en las tres historias (diferencia < 1e-4 por acción).'))
    h.append(proj(c,'Conservadora (25 %)')+proj(b,'Base (50 %)')+proj(o,'Optimista (25 %)'))
    h.append(H3('8. Valor terminal y puente hasta la acción'))
    h.append(table(['Historia','VP flujos años 1–10','Valor terminal','VP valor terminal','Activos operativos','VP terminal / total','− Deuda','− Minoritarios','+ Caja','+ No operativos','− Opciones','Patrimonio','Acciones','Valor por acción'],
      [bridge(c,'Conservadora'),bridge(b,'Base'),bridge(o,'Optimista')]))
    h.append(P(f'Base: flujo terminal {f(b["tv_cf"])} M a costo de capital {p(b["tv_wacc"],2)} y g = 4,0 % → VT {f(b["tv"])} M. Reinversión terminal = g / ROIC = {p(0.04/0.1323,1)} del NOPAT en la Base, {p(0.04/0.1821,1)} en la Optimista y {p(0.04/WACC_T,1)} en la Conservadora (ROIC = costo de capital). Probabilidad de fracaso: 0 en las tres.'))
    h.append(H3('9. Escenarios y ciclos'))
    h.append(table(['Historia','Probabilidad','Valor DCF','Frente al precio','Aporte al esperado'],[
      ['Conservadora','25 %',usd(vc),p(vc/px-1),usd(.25*vc)],['Base','50 %',usd(vb),p(vb/px-1),usd(.5*vb)],['Optimista','25 %',usd(vo),p(vo/px-1),usd(.25*vo)],
      ['<strong>Valor esperado</strong>','100 %','<strong>'+usd(EXPECTED)+'</strong>',p(EXPECTED/px-1),usd(EXPECTED)]]))
    h.append(P(f'Tipo de historia «crecimiento»: 50 / 25 / 25. Orden Conservadora ≤ Base ≤ Optimista: cumple. Costo de capital común: cumple. <strong>MOS de 35 % solo sobre el DCF Base:</strong> 0,65 × {usd(vb,4)} = {usd(mos_price)}; con la Conservadora daría {usd(vc*.65)} (informativo). Ciclo: crecimiento de ingresos FY2021 56,7 %, FY2022 82,6 %, FY2023 17,0 %, FY2024 18,0 %, FY2025 18,3 %, LTM {p(gl)}; margen EBIT FY2022 −5,7 %, FY2023 3,0 %, FY2024 6,4 %, FY2025 10,7 %, LTM {p(em[9])}.'))
    h.append(H3('10. Cinco múltiplos prioritarios'))
    h.append(P('Libro Múltiplos (sistema Atlas; sin P/S ni P/BV), con los supuestos del DCF: crecimiento 11/7/13 % (año 1) y 14/9,75/16,25 % (años 2–5), margen objetivo 18/13/22 % (base ajustada; 16,36/11,36/20,36 % en base contable), impuesto 25,17 %. Arrendamientos reclasificados a otros pasivos. Múltiplo de salida: Conservadora = actual −15 % (P/E: mediana de 5 años); Base = actual (P/E: punto medio, porque el TTM está distorsionado por partidas no operativas); Optimista = actual +15 % (P/E: TTM). El EV/FCFF actual es el de FY2025 porque el LTM no calcula.'))
    rows=[]
    for m in MET:
        e=MULT_EXIT[m]; hm=HIST_MULT[m]
        rows.append([m,p(PESO[m],0),f(hm['y10'],2),f(hm['y5'],2),f(hm['y3'],2),f(hm['ttm'],2) if hm['ttm'] else 'N/D (31,50 en FY2025)',f(e[0],2),f(e[1],2),f(e[2],2)])
    h.append(table(['Método','Peso total','Mediana 10 a','Mediana 5 a','Mediana 3 a','Actual (LTM)','Salida Cons.','Salida Base','Salida Opt.'],rows))
    for k,name in (('cons','Conservadora'),('base','Base'),('opt','Optimista')):
        rr=[[m]+[f(x,2) for x in OBJ[k][m]]+[f(x,2) for x in VPM[k][m]]+[f(CONS[k][m],2)] for m in MET]
        rr.append(['<strong>Consolidado</strong>','','','','','','','<strong>'+f(MULT[k],2)+'</strong>'])
        h.append(H4(f'Descuento a valor presente · {name}')+table(['Método','Precio FY+1','FY+2','FY+3','VP 1 año','VP 2 años','VP 3 años','Consolidado hoy'],rr))
    h.append(P(f'Sin dividendos. Pesos de los años 1/2/3: 20 % / 30 % / 50 % sobre valores presentes. Ke {p(KE,2)} en los tres escenarios. Ponderación «Crecimiento»: DCF 75 % y múltiplos 25 % (10/6/5/2/2 %). Combinado secundario: {usd(COMB["cons"])} / {usd(COMB["base"])} / {usd(COMB["opt"])}. El libro de Múltiplos no resta el valor de las opciones (≈ 0,09 por acción). EV/FCFF Base de FY+2 (53,40) y FY+3 (69,42) refleja que el FCFF proyectado crece de forma muy desigual; P/E Base (107) y Optimista (179) están elevados por la utilidad neta proyectada y pesan solo 5 %.'))
    h.append(H3('11. Sensibilidades DCF y de múltiplos + DCF inverso'))
    GL=[0.10,0.12,0.14,0.16,0.18];ML=[0.14,0.16,0.18,0.20,0.22];DW=[-0.01,-0.005,0,0.005,0.01];TG=[0.03,0.035,0.04,0.045,0.048]
    A=[[f(SENS[f'a_{i}_{j}'],2) for j in range(5)] for i in range(5)];B=[[f(SENS[f'b_{i}_{j}'],2) for j in range(5)] for i in range(5)]
    h.append(H4('Matriz A · CAGR años 2–5 × margen objetivo ajustado (precio por acción; centro = DCF Base)'))
    h.append(table(['CAGR \\ margen']+[p(m,0) for m in ML],[[p(g,0)]+A[i] for i,g in enumerate(GL)]))
    h.append(H4('Matriz B · costo de capital inicial × crecimiento terminal (precio por acción; centro = DCF Base)'))
    h.append(table(['Costo de capital inicial \\ g']+[p(t,1) for t in TG],[[p(WACC0+d,2)]+B[i] for i,d in enumerate(DW)]))
    av=[SENS[k] for k in SENS if k.startswith('a_')];bv=[SENS[k] for k in SENS if k.startswith('b_')]
    h.append(P(f'Rango A: {usd(min(av))} a {usd(max(av))}; rango B: {usd(min(bv))} a {usd(max(bv))}. Centro de ambas = {usd(vb,4)} (conciliado). El precio de {usd(px)} queda por debajo de casi todas las celdas de A (solo la esquina de menor crecimiento y menor margen lo supera) y por debajo de todas las de B.'))
    h.append(H4('DCF inverso (una variable a la vez)'))
    h.append(table(['Variable que se resuelve','Valor necesario','Base','Resultado'],[
      ['Crecimiento anual años 1–5',p(SENS['crecimiento'],2),'11,0 % / 14,0 %',usd(px)],['Margen objetivo ajustado',p(SENS['margen'],2),'18,0 %',usd(px)],
      ['Crecimiento con margen fijo de 16 %',p(SENS['crec_con_margen16'],2),'11,0 % / 14,0 %',usd(px)],['Costo de capital inicial',p(SENS['wacc'],2),p(WACC0,2),usd(px)]]))
    h.append(H4('Matrices 5×5 por múltiplo (solo Base) · valor presente por acción'))
    h.append(P('Origen: hoja de cada método del libro Múltiplos (precio FY+3 = múltiplo elegido × fundamental FY+3). Cada celda se descontó con el factor de 3 años del Ke Base (' + f(DF3,4) + '); Uber no paga dividendos, así que el ajuste al centro es solo de redondeo y el centro coincide con el VP3 Base de la hoja de Descuento. Derivación declarada; la hoja conserva el precio FY+3 sin descontar.'))
    for m in MET:
        mt=MATRICES_M[m]; V=matriz_vp(m)
        h.append(H4(f'{m} · centro VP3 = {usd(VPM["base"][m][2])}'))
        h.append(table([f'{m} \\ {mt["unidad"]}']+[f(x,0) for x in mt['col']],[[f(mt['fila'][i],2)+'x']+[f(x,2) for x in V[i]] for i in range(5)]))
    h.append(H3('12. Trazabilidad, reconciliaciones y límites'))
    h.append(table(['Control','Estado'],[
      ['Réplica local del motor vs Google Sheets (tres historias)','APROBADO: 45,2912 / 98,7383 / 149,6689'],
      ['Integridad de fórmulas y comentarios del motor en estas copias','NO re-verificada (pendiente R6)'],
      ['Costo de capital común (10,00 % inicial; 8,25 % estable)','APROBADO'],
      ['Probabilidades = 100 %; Cons ≤ Base ≤ Opt; costo de capital estable > g','APROBADO'],
      ['MOS 35 % solo sobre DCF Base','APROBADO'],
      ['Libro Múltiplos: compuerta «LISTA PARA CALCULAR»; Resumen de valoraciones CONCILIADO (6 controles)','APROBADO'],
      ['Ke del libro Múltiplos = Ke de la Base (10,49 %)','APROBADO tras corregir un error propio (se había cargado el costo de capital 10,00 % como Ke); los múltiplos se recalcularon'],
      ['Huellas del traspaso D↔M','Hash SHA-256 de los valores transferidos (no del libro completo)'],
      ['Verificación documental contra 10-K/10-Q','PENDIENTE (filas de verificación «PENDIENTE»; estados «MODELADO · SIN CERTIFICAR»)'],
      ['«Otros ajustes» del flujo de caja LTM (6.540 M) y caja restringida','PENDIENTE; no afecta el DCF; afecta el CFO proyectado de P/OCF y P/FCFE'],
      ['Volatilidad de las opciones (40 %), costo de la deuda (6,10 %) y beta (1,20)','SUPUESTOS declarados; beta por decisión del usuario'],
      ['EV/FCFF LTM','N/D en el libro; se usó el de FY2025 (31,50x) como actual'],
      ['Auditoría económica independiente','NO_EJECUTADA (R6)'],
      ['<code>AISLAMIENTO=OK</code>','La revisión Floyd F1–F5 se usó solo como punto de partida de las historias y como contraste; los datos contables vienen de la SEC']]))
    return ''.join(h)
