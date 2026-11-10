from datos import *
from fmt import *
from n1 import rev,cogs,sga,da,rd,ebit,prov,nonop,ebt,tax,ni,dsh,cfo,capex,bb,sbc,gm,em,b,c,o,vb,vc,vo,px,mos_price,cap,mexp,gl
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
    return [name,f(st['pv_cf'],0),f(st['tv'],0),f(st['pv_tv'],0),f(st['sum_pv'],0),p(st['pv_tv']/st['sum_pv'],0),f(-st['debt'],0),f(st['cash'],0),f(st['equity'],0),f(st['shares'],3),usd(st['value'],4)]
def n2():
    h=['<h2>Nivel 2 · Valoración reproducible</h2>']
    h.append(H3('1. Identificación, fuentes y unidades'))
    h.append(table(['Concepto','Valor'],[
      ['Empresa / ticker','MercadoLibre, Inc. · MELI · NASDAQ · USD · millones salvo por acción'],
      ['Revisión','MELI-REBOOT-3T26-R1 · perfil Floyd R1–R6 · contrato jmr-reboot-3libros-v1'],
      ['Corte contable / precio','30-sep-2026 (10-Q 3T-2026, acc. 0001099590-26-000029) · precio 1.510,00 (cierre 6-nov-2026, Alpha Vantage)'],
      ['Libro Históricos','15Z4mnTqLAm05V0svSMbKS1jZB9VEMKRwCO6z4GwvyPI'],
      ['Libro DCF Base / Conservadora / Optimista','174iyMLVgEsIw8sAWHNF3_SAvcbOoZbb1dB94gUF5yLc / 1RYE2kFcPstfBAH2eTRkyiMwvw64XuOcgnofD9Jq8jPM / 1fdZBeu5c4Agd54piuip2jnLL8HxM2yUbGOkGUKjgjd4'],
      ['Libro Múltiplos','19jUYjQ-KXnLUjvQBXzTJhIRHJgxN79BdOfoqdB7REJk'],
      ['Documento de análisis','__DOC__'],
      ['Fuentes','SEC XBRL <em>companyfacts</em> CIK 0001099590 (primaria); texto del 10-Q 3T-2026 y del 10-K FY2025; Alpha Vantage (precios); FRED DGS10 (tasa libre); Damodaran nov-2026 (prima) y tablas de industria del motor (enero 2026)'],
      ['Motor','fcffsimpleginzu original de Damodaran; entradas en Input sheet, Cost of capital worksheet, R&amp;D converter y Country equity risk premiums B1. Integridad de las fórmulas y los comentarios NO re-verificada en estas copias']]))
    h.append(H3('2. Estados históricos y LTM'))
    h.append(P('LTM = FY2025 + 9M-2026 − 9M-2025 (flujos) y saldos al 30-sep-2026. Fuente SEC XBRL cargada en el libro de Históricos. «Otros operativos» = ingresos − costo de ingresos − ventas y administración − I+D − EBIT: es, sobre todo, la provisión para cuentas incobrables del crédito. La D&A está incluida en los costos y se muestra desde el flujo de caja. «Intereses y otros» = diferencia entre EBIT y utilidad antes de impuestos (incluye gastos financieros y diferencia en cambio). Ingresos = «ingresos netos y financieros». Los pasivos de fondeo del crédito, los fondos de clientes y el efectivo restringido están en «otros» del balance (ver sección 4).'))
    h.append(table(['Estado de resultados']+YR,[row('Ingresos',rev),row('Costo de ingresos y gastos financieros',cogs),row('Ventas y marketing + G&A',sga),row('Investigación y desarrollo (desarrollo de producto y tecnología)',rd),row('Otros operativos (provisión para incobrables)',prov),
      row('EBIT (resultado operativo)',ebit),row('Intereses y otros resultados no operativos (neto)',nonop),row('Utilidad antes de impuestos',ebt),row('Impuestos',tax),row('Utilidad neta',ni),row('Acciones diluidas promedio',dsh,1)]))
    h.append(table(['Balance']+YR,[row('Efectivo',BSR[3]),row('Inversiones CP',BSR[4]),row('Total activos',BSR[16]),row('Préstamos y obligaciones financieras corrientes (total)',[None]*9+[4623.0,6909.0]),row('Préstamos y obligaciones financieras no corrientes (total)',[None]*9+[4570.0,6281.0]),row('Deuda corporativa (notas y arrendamientos financieros)',[None]*9+[1773.0,2369.0]),row('Patrimonio total',BSR[35])]))
    h.append(table(['Flujo de caja']+YR,[row('Flujo operativo',cfo),row('Capex',capex),row('Compensación LTRP (efectivo)',sbc),row('Otros ajustes (incluye provisión y cambios de cartera y fondos de clientes)',CFR[6]),row('Recompras',bb)]))
    h.append(H3('3. Ratios y economía del negocio'))
    h.append(table(['Ratio']+YR,[prow('Crecimiento de ingresos',[None]+[rev[i]/rev[i-1]-1 for i in range(1,10)]+[gl]),prow('Margen bruto',gm),prow('Margen EBIT',em),prow('Margen neto',[a/b_ for a,b_ in zip(ni,rev)]),
      prow('Tasa de impuestos efectiva',[a/b_ for a,b_ in zip(tax,ebt)]),prow('I+D / ingresos',[a/b_ for a,b_ in zip(rd,rev)]),prow('Provisión / ingresos',[a/b_ for a,b_ in zip(prov,rev)]),prow('Capex / ingresos',[a/b_ for a,b_ in zip(capex,rev)])]))
    h.append(P('Datos del 10-Q 3T-2026: ingresos del trimestre 10.750 M (+45 %) y de nueve meses 29.764 M (+48 %); costo de ingresos y gastos financieros 58,3 % de los ingresos (54,9 %); resultado operativo de nueve meses 1.970 M (2.312 M; margen 6,6 % frente a 11,5 %) y del trimestre 676 M (6,3 % frente a 9,8 %); provisión para incobrables 3.862 M (2.108 M). Ingresos de nueve meses por línea: comercio 16.771 M (servicios 12.670 M; productos 4.101 M); fintech 12.993 M (servicios y rendimientos 6.232 M; crédito 6.710 M; productos 51 M). Por país: Brasil 16.305 M, México 6.742 M, Argentina 5.355 M, otros 1.362 M. Indicadores del trimestre: usuarios activos de fintech 93 M (+29 %), compradores únicos 94 M (+22 %), mercancía bruta 22.818 M (+38 %), volumen de pagos 108.801 M (+53 %), NIMAL 20,1 % (21,0 %). Flujo operativo de nueve meses 8.687 M y flujo libre ajustado 443 M (718 M); caja disponible según MELI 8.126 M (6.710 M al inicio del año).'))
    h.append(H3('4. Puente contable a económico'))
    h.append(table(['Concepto','Valor','Nota'],[
      ['EBIT LTM (contable)',f(ebit[10],1),'Reportado; incluye el costo de fondeo del crédito y la provisión para incobrables'],
      ['EBIT ajustado por I+D capitalizada',f(3604.67,1),'I+D LTM 2.757; FY2025 2.269; FY2024 1.934; FY2023 1.831; vida 3 años; margen ajustado 9,36 %'],
      ['Capital invertido (año base)',f(b['ic'][0],1),'Incluye I+D capitalizada; el fondeo del crédito es pasivo operativo'],
      ['Deuda',f(b['debt'],0),'Notas 2031 (537), 2033 (742), 2036 (974) y arrendamientos financieros (116). <strong>No incluye</strong> préstamos bancarios, bills y certificados, deuda colateralizada ni notas comerciales (≈10.800), que financian la cartera y cuyo costo ya está en el EBIT (decisión que cambia lo acordado en R1)'],
      ['Caja',f(b['cash'],0),'«Efectivo, inversiones y activos digitales disponibles» según MELI al 30-sep-2026'],
      ['No incluidos en el puente','—','Efectivo restringido 14.559 y fondos por pagar a clientes 17.400; montos por pagar de tarjetas 5.464; cartera de crédito (parte del activo operativo)'],
      ['Arrendamientos operativos','—','2.964 de pasivo: no se restan (el EBIT ya deduce el alquiler; decisión del usuario del 10-nov-2026)'],
      ['Activos no operativos · minoritarios','0 · 0','Sin dato separable; sin participaciones no controladoras'],
      ['Acciones (millones)',f(b['shares'],3),'Portada del 10-Q; sin opciones ni RSU en acciones (el plan LTRP se paga en efectivo)'],
      ['Tasa efectiva / marginal','26,46 % / 32 %','680 / 2.570 LTM; marginal ponderada por país']]))
    h.append(H3('5. Supuestos efectivos por historia'))
    h.append(table(['Entrada del motor','Celda','Conservadora','Base','Optimista'],[
      ['Crecimiento año 1','Input B26','22 %','30 %','36 %'],['Margen EBIT año 1 (ajustado)','B27','9,36 %','9,36 %','9,36 %'],['CAGR años 2–5','B28','11 %','19 %','23 %'],
      ['Margen objetivo (ajustado)','B29','9,0 %','13,5 %','16,5 %'],['Año de convergencia del margen','B30','5','5','5'],['Ventas/capital años 1–5 · 6–10','B31 · B32','2,5 · 2,3','3,2 · 3,0','3,8 · 3,4'],
      ['ROIC terminal','B48 · B49','Costo de capital','14,0 %','16,4 %'],['Fracaso','B51','No','No','No'],['Tasa libre','B34','4,86 %','4,86 %','4,86 %'],['Crecimiento terminal','B68','4,0 %','4,0 %','4,0 %'],
      ['Opciones','B37','No','No','No'],['I+D capitalizada','B16','Sí · 3 años','igual','igual'],['Deuda · caja','B15 · B18','2.369 · 8.126','igual','igual']]))
    h.append(H3('6. Costo de capital descompuesto'))
    h.append(table(['Componente','Valor','Fuente / criterio'],[
      ['Tasa libre','4,86 %','FRED DGS10, 6-nov-2026'],['Beta desapalancada · apalancada','0,910 · '+f(BETA,3),'Multinegocio global por ingresos de 9M-2026: Retail (General) 0,937 (16.771) e Information Services 0,874 (12.993); mapeo de industrias es juicio propio'],
      ['Prima de riesgo',p(ERP,3),'Por país (ingresos 9M-2026): Brasil 16.305 (6,63 %), México 6.742 (5,85 %), Argentina 5.355 (13,10 %), Chile 500, Colombia 450, Uruguay 250, Perú 162 (reparto supuesto); madura 3,387 %'],['Costo del patrimonio (Ke)',p(KE,4),'4,86 % + '+f(BETA,3)+' × '+p(ERP,3)],
      ['Costo de la deuda','6,90 % antes de impuestos (entrada directa)','Estimación: tasa libre + ≈2 puntos; vencimiento medio 6 años'],['Pesos de mercado','97 % / 3 %','Capitalización 76.552; deuda corporativa 2.369'],
      ['Costo de capital inicial (años 1–5)',p(WACC0,2),'Común a las tres historias'],['Costo de capital terminal (año 10)',p(WACC_T,2),'Baja linealmente en los años 6–10']]))
    h.append(H3('7. Proyección explícita anual completa'))
    h.append(P('Millones de USD. Motor original recalculado localmente (LibreOffice), igual a Google Sheets en las tres historias (diferencia < 1e-4 por acción).'))
    h.append(proj(c,'Conservadora (25 %)')+proj(b,'Base (50 %)')+proj(o,'Optimista (25 %)'))
    h.append(H3('8. Valor terminal y puente hasta la acción'))
    h.append(table(['Historia','VP flujos años 1–10','Valor terminal','VP valor terminal','Activos operativos','VP terminal / total','− Deuda','+ Caja','Patrimonio','Acciones','Valor por acción'],
      [bridge(c,'Conservadora'),bridge(b,'Base'),bridge(o,'Optimista')]))
    h.append(P(f'Base: flujo terminal {f(b["tv_cf"])} M a costo de capital {p(b["tv_wacc"],2)} y g = 4,0 % → VT {f(b["tv"])} M. Reinversión terminal = g / ROIC = {p(0.04/0.14,1)} del NOPAT en la Base, {p(0.04/0.164,1)} en la Optimista y {p(0.04/WACC_T,1)} en la Conservadora (ROIC = costo de capital). Probabilidad de fracaso: 0 en las tres. Minoritarios, activos no operativos y opciones: 0.'))
    h.append(H3('9. Escenarios y ciclos'))
    h.append(table(['Historia','Probabilidad','Valor DCF','Frente al precio','Aporte al esperado'],[
      ['Conservadora','25 %',usd(vc),p(vc/px-1),usd(.25*vc)],['Base','50 %',usd(vb),p(vb/px-1),usd(.5*vb)],['Optimista','25 %',usd(vo),p(vo/px-1),usd(.25*vo)],
      ['<strong>Valor esperado</strong>','100 %','<strong>'+usd(EXPECTED)+'</strong>',p(EXPECTED/px-1),usd(EXPECTED)]]))
    h.append(P(f'Tipo de historia «crecimiento»: 50 / 25 / 25. Orden Conservadora ≤ Base ≤ Optimista: cumple. Costo de capital común: cumple. <strong>MOS de 35 % solo sobre el DCF Base:</strong> 0,65 × {usd(vb,4)} = {usd(mos_price)}; con la Conservadora daría {usd(vc*.65)} (informativo). Ciclo: crecimiento de ingresos FY2020 73,1 %, FY2021 77,9 %, FY2022 52,5 %, FY2023 40,1 %, FY2024 37,5 %, FY2025 39,1 %, LTM {p(gl)}; margen EBIT FY2022 9,9 %, FY2023 14,6 %, FY2024 12,7 %, FY2025 11,1 %, LTM {p(em[10])}.'))
    h.append(H3('10. Cinco múltiplos prioritarios'))
    h.append(P('Libro Múltiplos (sistema Atlas; sin P/S ni P/BV), con los supuestos del DCF: crecimiento 30/22/36 % (año 1) y 19/11/23 % (años 2–5), margen objetivo 13,5/9,0/16,5 % (base ajustada; 11,56/7,06/14,56 % en base contable), impuesto 26,46 %. Fondeo del crédito y arrendamientos reclasificados a otros pasivos: deuda = 2.369. Múltiplo de salida: Conservadora = actual −15 %; Base = actual; Optimista = actual +15 % (EV/EBITDA, P/E, P/FCFE y P/OCF). EV/FCFF no tiene múltiplo actual (FCFF LTM no calcula): 30/35/40x es juicio mío sin ancla histórica. Pesos: EV/EBITDA 12 % y P/E 7 % son los únicos apreciables; EV/FCFF 3 %, P/FCFE 1,5 % y P/OCF 1,5 % reciben peso mínimo porque su flujo incluye fondos de clientes (ajuste de flujo residual de 23,3 % de las ventas, mediana histórica).'))
    rows=[]
    for m in MET:
        e=MULT_EXIT[m]; hm=HIST_MULT[m]
        rows.append([m,p(PESO[m],1),f(hm['y10'],2),f(hm['y5'],2),f(hm['y3'],2),f(hm['ttm'],2) if hm['ttm'] else 'N/D',f(e[0],2),f(e[1],2),f(e[2],2)])
    h.append(table(['Método','Peso total','Mediana 10 a','Mediana 5 a','Mediana 3 a','Actual (LTM)','Salida Cons.','Salida Base','Salida Opt.'],rows))
    for k,name in (('cons','Conservadora'),('base','Base'),('opt','Optimista')):
        rr=[[m]+[f(x,2) for x in OBJ[k][m]]+[f(x,2) for x in VPM[k][m]]+[f(CONS[k][m],2)] for m in MET]
        rr.append(['<strong>Consolidado</strong>','','','','','','','<strong>'+f(MULT[k],2)+'</strong>'])
        h.append(H4(f'Descuento a valor presente · {name}')+table(['Método','Precio FY+1','FY+2','FY+3','VP 1 año','VP 2 años','VP 3 años','Consolidado hoy'],rr))
    h.append(P(f'Sin dividendos. Pesos de los años 1/2/3: 20 % / 30 % / 50 % sobre valores presentes. Ke {p(KE,2)} en los tres escenarios. Ponderación «Crecimiento»: DCF 75 % y múltiplos 25 % (12/3/7/1,5/1,5 %). Combinado secundario: {usd(COMB["cons"])} / {usd(COMB["base"])} / {usd(COMB["opt"])}. El P/E y el EV/EBITDA FY+3 de la Base (3.183 y 2.855) reflejan el crecimiento de utilidad y EBITDA de la Base; los métodos de flujo (EV/FCFF 1.349, P/FCFE 1.640, P/OCF 1.860) son de contraste.'))
    h.append(H3('11. Sensibilidades DCF y de múltiplos + DCF inverso'))
    GL=[0.15,0.17,0.19,0.21,0.23];ML=[0.105,0.12,0.135,0.15,0.165];DW=[-0.01,-0.005,0,0.005,0.01];TG=[0.03,0.035,0.04,0.045,0.048]
    A=[[f(SENS[f'a_{i}_{j}'],2) for j in range(5)] for i in range(5)];B=[[f(SENS[f'b_{i}_{j}'],2) for j in range(5)] for i in range(5)]
    h.append(H4('Matriz A · CAGR años 2–5 × margen objetivo ajustado (precio por acción; centro = DCF Base)'))
    h.append(table(['CAGR \\ margen']+[p(m,1) for m in ML],[[p(g,0)]+A[i] for i,g in enumerate(GL)]))
    h.append(H4('Matriz B · costo de capital inicial × crecimiento terminal (precio por acción; centro = DCF Base)'))
    h.append(table(['Costo de capital inicial \\ g']+[p(t,1) for t in TG],[[p(WACC0+d,2)]+B[i] for i,d in enumerate(DW)]))
    av=[SENS[k] for k in SENS if k.startswith('a_')];bv=[SENS[k] for k in SENS if k.startswith('b_')]
    h.append(P(f'Rango A: {usd(min(av))} a {usd(max(av))}; rango B: {usd(min(bv))} a {usd(max(bv))}. Centro de ambas = {usd(vb,4)} (conciliado). <strong>El precio de {usd(px)} queda por debajo de todas las celdas de A y de B.</strong>'))
    h.append(H4('DCF inverso (una variable a la vez)'))
    h.append(table(['Variable que se resuelve','Valor necesario','Base','Resultado'],[
      ['Crecimiento anual años 1–5',p(SENS['crecimiento'],2),'30 % / 19 %',usd(px)],['Margen objetivo ajustado',p(SENS['margen'],2),'13,5 %',usd(px)],
      ['Crecimiento con margen fijo de 13,5 %',p(SENS['crec_con_margen16'],2),'30 % / 19 %',usd(px)],['Costo de capital inicial',p(SENS['wacc'],2),p(WACC0,2),usd(px)]]))
    h.append(H4('Matrices 5×5 por múltiplo (solo Base) · valor presente por acción'))
    h.append(P('Origen: hoja de cada método del libro Múltiplos (precio FY+3 = múltiplo elegido × fundamental FY+3). Cada celda se descontó con el factor de 3 años del Ke Base (' + f(DF3,4) + '); MELI no paga dividendos, así que el ajuste al centro es solo de redondeo y el centro coincide con el VP3 Base de la hoja de Descuento. Derivación declarada; la hoja conserva el precio FY+3 sin descontar.'))
    for m in MET:
        mt=MATRICES_M[m]; V=matriz_vp(m)
        h.append(H4(f'{m} · centro VP3 = {usd(VPM["base"][m][2])}'))
        h.append(table([f'{m} \\ {mt["unidad"]}']+[f(x,0) for x in mt['col']],[[f(mt['fila'][i],2)+'x']+[f(x,2) for x in V[i]] for i in range(5)]))
    h.append(H3('12. Trazabilidad, reconciliaciones y límites'))
    h.append(table(['Control','Estado'],[
      ['Réplica local del motor vs Google Sheets (tres historias)','APROBADO: 908,3336 / 2.536,9518 / 4.120,9397'],
      ['Integridad de fórmulas y comentarios del motor en estas copias','NO re-verificada (pendiente R6)'],
      ['Costo de capital común (11,67 % inicial; 8,25 % estable)','APROBADO'],
      ['Probabilidades = 100 %; Cons ≤ Base ≤ Opt; costo de capital estable > g','APROBADO'],
      ['MOS 35 % solo sobre DCF Base','APROBADO'],
      ['Libro Múltiplos: compuerta «LISTA PARA CALCULAR»; Resumen de valoraciones CONCILIADO (6 controles)','APROBADO'],
      ['Ke del libro Múltiplos = Ke de la Base (11,88 %)','APROBADO'],
      ['Huellas del traspaso D↔M','Hash SHA-256 de los valores transferidos (no del libro completo)'],
      ['Fondeo del crédito como pasivo operativo (deuda 2.369)','SUPUESTO declarado; cambia lo acordado en R1; riesgo material para R6'],
      ['Verificación documental contra 10-K/10-Q','PENDIENTE (filas de verificación «PENDIENTE»; estados «MODELADO · SIN CERTIFICAR»)'],
      ['Ceros por dato no separable (deuda corporativa FY2016–FY2024, cuentas por pagar, ingresos diferidos < 2023)','DECLARADOS; no afectan el LTM'],
      ['EV/FCFF sin ancla histórica; P/FCFE y P/OCF con flujo distorsionado','SUPUESTOS; peso mínimo (3 %, 1,5 %, 1,5 %)'],
      ['Beta bottom-up, costo de la deuda y reparto de otros países','ESTIMADOS'],
      ['Auditoría económica independiente','NO_EJECUTADA (R6)'],
      ['<code>AISLAMIENTO=OK</code>','Los datos vienen de la SEC y de precios de mercado; ninguna revisión anterior de MELI (A-1.2, Floyd F1–F5) se usó como insumo']]))
    return ''.join(h)
