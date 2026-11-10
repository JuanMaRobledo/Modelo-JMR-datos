from datos import *
from fmt import *
from n1 import rev,cogs,sga,da,rd,ebit,nonop,ebt,tax,ni,dsh,cfo,capex,bb,dv,sbc,gm,em,b,c,o,vb,vc,vo,px,mos_price,cap,mexp,gl
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
def bridge2(st,name):
    return [name,f(st['pv_cf'],0),f(st['tv'],0),f(st['pv_tv'],0),f(st['sum_pv'],0),p(st['pv_tv']/st['sum_pv'],0),f(-st['debt'],0),f(st['cash'],0),f(st['nonop'],0),f(st['equity'],0),f(st['shares'],3),usd(st['value'],4)]
def n2():
    h=['<h2>Nivel 2 · Valoración reproducible</h2>']
    h.append(H3('1. Identificación, fuentes y unidades'))
    h.append(table(['Concepto','Valor'],[
      ['Empresa / ticker','Microsoft Corporation · MSFT · NASDAQ · USD · millones salvo por acción'],
      ['Revisión','MSFT-REBOOT-3T26-R1 · perfil Floyd R1–R6 · contrato jmr-reboot-3libros-v1'],
      ['Corte contable / precio','30-sep-2026 (10-Q 1T-FY2027) · precio 530,61 (cierre 6-nov-2026, Alpha Vantage) · año fiscal al 30 de junio'],
      ['Libro Históricos','1t5ZM7SQF-An3WMJXfdYb0Q_XGHeJuiBY_rervY7eK8E'],
      ['Libro DCF Base / Conservadora / Optimista','19f9zo6xbYTnrjoAZwVf5ViHzVCEnkde9no2cryOBQjA / 1TF-_XL14nxdAgNkHzJN3w5plZzOPj54rN2jnFfB33ho / 13yJEdR4nTxVwE7b2bspxRGi8Pyk9Q_guwTmQdK36EMg'],
      ['Libro Múltiplos','1m_mbps0ZIVzsDUNyz76UzPGhei5YLuWwnSffk10496o'],
      ['Documento de análisis','__DOC__'],
      ['Fuentes','SEC XBRL <em>companyfacts</em> CIK 0000789019 (primaria); texto del 10-Q 1T-FY2027 y del 10-K FY2026; Alpha Vantage (precios); FRED DGS10 (tasa libre); Damodaran nov-2026 (prima) y tablas de industria del motor (enero 2026)'],
      ['Motor','fcffsimpleginzu original de Damodaran; entradas en Input sheet, Cost of capital worksheet, R&amp;D converter y Country equity risk premiums B1. Integridad de las fórmulas y los comentarios NO re-verificada en estas copias']]))
    h.append(H3('2. Estados históricos y LTM'))
    h.append(P('LTM = FY2026 + 3M-FY2027 − 3M-FY2026 (flujos) y saldos al 30-sep-2026. Fuente SEC XBRL cargada en el libro de Históricos. El año fiscal termina el 30 de junio. «Otros no operativos» incluye ganancias y pérdidas de las inversiones en OpenAI y otras participaciones. La D&A de los años anuales es depreciación + amortización de las notas (redondeadas a 100 M); la del LTM es la línea «depreciación, amortización y otros» del 10-Q (42.597). Los arrendamientos financieros (70.973 al 30-sep-2026) no tienen línea propia en el balance: están en otros pasivos y se leen de la nota de arrendamientos.'))
    h.append(table(['Estado de resultados']+YR,[row('Ingresos',rev),row('Costo de ingresos',cogs),row('Ventas y marketing + G&A',sga),row('Investigación y desarrollo',rd),
      row('EBIT (resultado operativo)',ebit),row('Otros ingresos (gastos) no operativos, neto',nonop),row('Utilidad antes de impuestos',ebt),row('Impuestos',tax),row('Utilidad neta',ni),row('Acciones diluidas promedio',dsh,1)]))
    h.append(table(['Balance']+YR,[row('Efectivo',BSR[3]),row('Inversiones CP',BSR[4]),row('Inversiones de capital y otras (no operativas)',BSR[14]),row('Total activos',BSR[16]),row('Deuda corriente (bonos)',BSR[20]),row('Deuda de largo plazo (bonos)',BSR[22]),row('Patrimonio total',BSR[34])]))
    h.append(table(['Flujo de caja']+YR,[row('Flujo operativo',cfo),row('Capex (efectivo)',capex),row('Depreciación y amortización',da),row('Compensación en acciones',sbc),row('Recompras',bb),row('Dividendos',dv)]))
    h.append(H3('3. Ratios y economía del negocio'))
    h.append(table(['Ratio']+YR,[prow('Crecimiento de ingresos',[None]+[rev[i]/rev[i-1]-1 for i in range(1,10)]+[None]),prow('Margen bruto',gm),prow('Margen EBIT',em),prow('Margen neto',[a/b_ for a,b_ in zip(ni,rev)]),
      prow('Tasa de impuestos efectiva',[a/b_ for a,b_ in zip(tax,ebt)]),prow('I+D / ingresos',[a/b_ for a,b_ in zip(rd,rev)]),prow('Capex / ingresos',[a/b_ for a,b_ in zip(capex,rev)]),prow('Flujo operativo / ingresos',[a/b_ for a,b_ in zip(cfo,rev)])]))
    h.append(P('Datos del 10-Q 1T-FY2027: ingresos del trimestre 92.279 M (+19 %); Azure +48 %; Microsoft Cloud 63.900 M (+30 %); RPO 683.000 M (comercial 677.000 M, +73 %; duración media 2,3 años); resultado operativo 45.915 M (margen 49,8 %); flujo operativo 58.000 M (45.057 M un año antes); gasto de capital del trimestre de ≈ 20.000 M adicionales frente al año anterior; plantilla −2 %. Segmentos: «Agents and Infra» 76.795 M (+25 %, margen operativo 52,8 %) y «Devices and Consumer» 15.484 M (−3 %, margen 34,6 %; ventas de Windows y dispositivos −22 %). Ingresos de FY2026 por región: Estados Unidos 170.794 M y resto del mundo 161.045 M.'))
    h.append(H3('4. Puente contable a económico'))
    h.append(table(['Concepto','Valor','Nota'],[
      ['EBIT LTM (contable)',f(ebit[10],1),'Reportado; no incluye el interés de los arrendamientos financieros'],
      ['EBIT ajustado por I+D capitalizada',f(167134,1),'I+D LTM 36.463; FY2026 35.562; FY2025 32.488; FY2024 29.510; vida 3 años; margen ajustado 48,24 %'],
      ['Capital invertido (año base)',f(b['ic'][0],1),'Incluye I+D capitalizada'],
      ['Deuda',f(b['debt'],0),'Bonos 35.481 (incluye 4.391 corriente) + arrendamientos financieros 70.973. <strong>Decisión mía:</strong> los arrendamientos financieros se restan como deuda (financian centros de datos; su interés no está en el EBIT). Efecto ≈ −9,5 por acción. Los arrendamientos operativos (27.477) no se restan (decisión del usuario del 10-nov-2026)'],
      ['Caja',f(b['cash'],0),'Efectivo 20.281 + inversiones de corto plazo 44.228'],
      ['Activos no operativos',f(b['nonop'],0),'«Inversiones de capital y otras» a valor en libros; incluye la participación en OpenAI (método de participación). No se valora a mercado'],
      ['Minoritarios · opciones','0 · 0','Sin dato; sin opciones'],
      ['Acciones (millones)',f(b['shares'],3),'7.426,195 de la portada del 10-Q (22-oct-2026) + 78 de acciones restringidas no devengadas (todas; conservador)'],
      ['Capex fuera del flujo de caja','24.608','Activos recibidos por arrendamientos financieros en FY2026: no están en el capex en efectivo'],
      ['Tasa efectiva / marginal','19,68 % / 23 %','34.955 / 177.586 LTM; marginal = federal 21 % + estatal neto (estimación mía)']]))
    h.append(H3('5. Supuestos efectivos por historia'))
    h.append(table(['Entrada del motor','Celda','Conservadora','Base','Optimista'],[
      ['Crecimiento año 1','Input B26','13 %','18 %','21 %'],['Margen EBIT año 1 (ajustado)','B27','48,24 %','48,24 %','48,24 %'],['CAGR años 2–5','B28','7 %','14 %','17 %'],
      ['Margen objetivo (ajustado)','B29','40 %','46 %','49 %'],['Año de convergencia del margen','B30','5','5','5'],['Ventas/capital años 1–5 · 6–10','B31 · B32','0,55 · 0,90','0,80 · 1,20','1,10 · 1,50'],
      ['ROIC terminal','B48 · B49','Costo de capital','18 %','26 %'],['Fracaso','B51','No','No','No'],['Tasa libre','B34','4,86 %','4,86 %','4,86 %'],['Crecimiento terminal','B68','4,0 %','4,0 %','4,0 %'],
      ['Opciones','B37','No','No','No'],['I+D capitalizada','B16','Sí · 3 años','igual','igual'],['Deuda · caja','B15 · B18','106.454 · 64.509','igual','igual']]))
    h.append(H3('6. Costo de capital descompuesto'))
    h.append(table(['Componente','Valor','Fuente / criterio'],[
      ['Tasa libre','4,86 %','FRED DGS10, 6-nov-2026'],['Beta desapalancada · apalancada','1,256 · '+f(BETA,3),'Multinegocio EE. UU. por ingresos del 1T-FY27: Software (System &amp; Application) 1,248 (76.795) y Computers/Peripherals 1,325 (15.484); el mapeo de industrias es juicio propio. Beta observada ≈ 1,0'],
      ['Prima de riesgo',p(ERP,3),'Por regiones (ingresos FY2026): Norteamérica 170.794 y resto del mundo 161.045; madura 3,387 %'],['Costo del patrimonio (Ke)',p(KE,4),'4,86 % + '+f(BETA,3)+' × '+p(ERP,3)],
      ['Costo de la deuda','5,20 % antes de impuestos (entrada directa)','Estimación: tasa libre + 0,34 puntos; calificación AAA no verificada'],['Pesos de mercado','97,4 % / 2,6 %','Capitalización '+f(cap*1000)+'; deuda 106.454'],
      ['Costo de capital inicial (años 1–5)',p(WACC0,2),'Común a las tres historias'],['Costo de capital terminal (año 10)',p(WACC_T,2),'Baja linealmente en los años 6–10']]))
    h.append(H3('7. Proyección explícita anual completa'))
    h.append(P('Millones de USD. Motor original recalculado localmente (LibreOffice), igual a Google Sheets en las tres historias (diferencia < 1e-4 por acción).'))
    h.append(proj(c,'Conservadora (25 %)')+proj(b,'Base (50 %)')+proj(o,'Optimista (25 %)'))
    h.append(H3('8. Valor terminal y puente hasta la acción'))
    h.append(table(['Historia','VP flujos años 1–10','Valor terminal','VP valor terminal','Activos operativos','VP terminal / total','− Deuda','+ Caja','+ No operativos','Patrimonio','Acciones','Valor por acción'],
      [bridge2(c,'Conservadora'),bridge2(b,'Base'),bridge2(o,'Optimista')]))
    h.append(P(f'Base: flujo terminal {f(b["tv_cf"])} M a costo de capital {p(b["tv_wacc"],2)} y g = 4,0 % → VT {f(b["tv"])} M. Reinversión terminal = g / ROIC = {p(0.04/0.18,1)} del NOPAT en la Base, {p(0.04/0.26,1)} en la Optimista y {p(0.04/WACC_T,1)} en la Conservadora (ROIC = costo de capital). Probabilidad de fracaso: 0 en las tres. Minoritarios y opciones: 0.'))
    h.append(H3('9. Escenarios y ciclos'))
    h.append(table(['Historia','Probabilidad','Valor DCF','Frente al precio','Aporte al esperado'],[
      ['Conservadora','25 %',usd(vc),p(vc/px-1),usd(.25*vc)],['Base','50 %',usd(vb),p(vb/px-1),usd(.5*vb)],['Optimista','25 %',usd(vo),p(vo/px-1),usd(.25*vo)],
      ['<strong>Valor esperado</strong>','100 %','<strong>'+usd(EXPECTED)+'</strong>',p(EXPECTED/px-1),usd(EXPECTED)]]))
    h.append(P(f'Tipo de historia «madura»: 50 / 25 / 25. Orden Conservadora ≤ Base ≤ Optimista: cumple. Costo de capital común: cumple. <strong>MOS de 35 % solo sobre el DCF Base:</strong> 0,65 × {usd(vb,4)} = {usd(mos_price)}; con la Conservadora daría {usd(vc*.65)} (informativo). Ciclo: crecimiento de ingresos FY2021 17,5 %, FY2022 18,0 %, FY2023 6,9 %, FY2024 15,7 %, FY2025 14,9 %, FY2026 17,8 %; margen EBIT FY2022 {p(em[5])}, FY2023 {p(em[6])}, FY2024 {p(em[7])}, FY2025 {p(em[8])}, FY2026 {p(em[9])}, LTM {p(em[10])}.'))
    h.append(H3('10. Cinco múltiplos prioritarios'))
    h.append(P('Libro Múltiplos (sistema Atlas; sin P/S ni P/BV), con los supuestos del DCF: crecimiento 18/13/21 % (año 1) y 14/7/17 % (años 2–5), margen objetivo 46/40/49 % (base ajustada; en base contable se resta la diferencia entre margen ajustado y reportado), impuesto 19,68 %. Arrendamientos financieros reclasificados a deuda de largo plazo: deuda = 106.454. Múltiplo de salida: Conservadora = actual −15 %; Base = actual; Optimista = actual +15 % para EV/EBITDA, P/E y P/OCF. <strong>EV/FCFF y P/FCFE usan la mediana de 5 años (47,70x y 44,60x)</strong> como Base porque el flujo libre del LTM está deprimido por el capex de IA (EV/FCFF actual N/D; P/FCFE actual 75,64x). Pesos: EV/EBITDA 8 %, EV/FCFF 8 %, P/E 10 %, P/FCFE 4 % y P/OCF 5 % (35 % del total; tipo «Madura»: DCF 65 %).'))
    rows=[]
    for m in MET:
        e=MULT_EXIT[m]; hm=HIST_MULT[m]
        rows.append([m,p(PESO[m],1),f(hm['y10'],2),f(hm['y5'],2),f(hm['y3'],2),f(hm['ttm'],2) if hm['ttm'] else 'N/D',f(e[0],2),f(e[1],2),f(e[2],2)])
    h.append(table(['Método','Peso total','Mediana 10 a','Mediana 5 a','Mediana 3 a','Actual (LTM)','Salida Cons.','Salida Base','Salida Opt.'],rows))
    for k,name in (('cons','Conservadora'),('base','Base'),('opt','Optimista')):
        rr=[[m]+[f(x,2) for x in OBJ[k][m]]+[f(x,2) for x in VPM[k][m]]+[f(CONS[k][m],2)] for m in MET]
        rr.append(['<strong>Consolidado</strong>','','','','','','','<strong>'+f(MULT[k],2)+'</strong>'])
        h.append(H4(f'Descuento a valor presente · {name}')+table(['Método','Precio FY+1','FY+2','FY+3','VP 1 año','VP 2 años','VP 3 años','Consolidado hoy'],rr))
    h.append(P(f'Pesos de los años 1/2/3: 20 % / 30 % / 50 % sobre valores presentes; incluyen los dividendos de cada año. Ke {p(KE,2)} en los tres escenarios. Ponderación «Madura»: DCF 65 % y múltiplos 35 % (8/8/10/4/5 %). Combinado secundario: {usd(COMB["cons"])} / {usd(COMB["base"])} / {usd(COMB["opt"])}. Múltiplos esperados (25/50/25): {usd(mexp)}.'))
    h.append(H3('11. Sensibilidades DCF y de múltiplos + DCF inverso'))
    GL=[0.10,0.12,0.14,0.16,0.18];ML=[0.40,0.43,0.46,0.49,0.52];DW=[-0.01,-0.005,0,0.005,0.01];TG=[0.03,0.035,0.04,0.045,0.048]
    A=[[f(SENS[f'a_{i}_{j}'],2) for j in range(5)] for i in range(5)];B=[[f(SENS[f'b_{i}_{j}'],2) for j in range(5)] for i in range(5)]
    h.append(H4('Matriz A · CAGR años 2–5 × margen objetivo ajustado (precio por acción; centro = DCF Base)'))
    h.append(table(['CAGR \\ margen']+[p(m,1) for m in ML],[[p(g,0)]+A[i] for i,g in enumerate(GL)]))
    h.append(H4('Matriz B · costo de capital inicial × crecimiento terminal (precio por acción; centro = DCF Base)'))
    h.append(table(['Costo de capital inicial \\ g']+[p(t,1) for t in TG],[[p(WACC0+d,2)]+B[i] for i,d in enumerate(DW)]))
    av=[SENS[k] for k in SENS if k.startswith('a_')];bv=[SENS[k] for k in SENS if k.startswith('b_')]
    h.append(P(f'Rango A: {usd(min(av))} a {usd(max(av))}; rango B: {usd(min(bv))} a {usd(max(bv))}. Centro de ambas = {usd(vb,4)} (conciliado). El precio de {usd(px)} queda dentro de ambos rangos (en la matriz B, solo con costo de capital menor o crecimiento terminal mayor que los de la Base).'))
    h.append(H4('DCF inverso (una variable a la vez)'))
    h.append(table(['Variable que se resuelve','Valor necesario','Base','Resultado'],[
      ['Crecimiento anual años 1–5',p(SENS['crecimiento'],2),'18 % / 14 %',usd(px)],['Margen objetivo ajustado',p(SENS['margen'],2),'46 %',usd(px)],
      ['Costo de capital inicial',p(SENS['wacc'],2),p(WACC0,2),usd(px)]]))
    h.append(H4('Matrices 5×5 por múltiplo (solo Base) · valor presente por acción'))
    h.append(P('Origen: hoja de cada método del libro Múltiplos (precio FY+3 = múltiplo elegido × fundamental FY+3). Cada celda se descontó con el factor de 3 años del Ke Base (' + f(DF3,4) + ') y se le suma el valor presente de los dividendos de los tres años (constante para toda la matriz), de modo que el centro coincide con el VP3 Base de la hoja de Descuento de múltiplos. Derivación declarada; la hoja conserva el precio FY+3 sin descontar.'))
    for m in MET:
        mt=MATRICES_M[m]; V=matriz_vp(m)
        h.append(H4(f'{m} · centro VP3 = {usd(VPM["base"][m][2])}'))
        h.append(table([f'{m} \\ {mt["unidad"]}']+[f(x,0) for x in mt['col']],[[f(mt['fila'][i],2)+'x']+[f(x,2) for x in V[i]] for i in range(5)]))
    h.append(H3('12. Trazabilidad, reconciliaciones y límites'))
    h.append(table(['Control','Estado'],[
      ['Réplica local del motor vs Google Sheets (tres historias)','APROBADO: 232,3824 / 496,2078 / 676,0823'],
      ['Integridad de fórmulas y comentarios del motor en estas copias','NO re-verificada (pendiente R6)'],
      ['Costo de capital común (10,49 % inicial; 8,25 % estable)','APROBADO'],
      ['Probabilidades = 100 %; Cons ≤ Base ≤ Opt; costo de capital estable > g','APROBADO'],
      ['MOS 35 % solo sobre DCF Base','APROBADO'],
      ['Libro Múltiplos: compuerta «LISTA PARA CALCULAR»; Resumen de valoraciones CONCILIADO (6 controles)','APROBADO'],
      ['Ke del libro Múltiplos = Ke de la Base (10,64 %)','APROBADO'],
      ['Huellas del traspaso D↔M','Hash SHA-256 de los valores transferidos (no del libro completo)'],
      ['Arrendamientos financieros (70.973) como deuda; operativos no','SUPUESTO declarado; efecto ≈ −9,5 por acción'],
      ['Inversiones no operativas (37.808) a valor en libros; OpenAI sin valoración de mercado','SUPUESTO declarado'],
      ['Verificación documental contra 10-K/10-Q','PENDIENTE (estados «MODELADO · SIN CERTIFICAR»)'],
      ['Ceros declarados por dato no separable en el libro de Múltiplos; reparto corriente/no corriente de arrendamientos financieros','DECLARADOS; no afectan el LTM'],
      ['EV/FCFF y P/FCFE con medianas de 5 años','SUPUESTO; juicio con respaldo histórico'],
      ['Beta bottom-up (1,28 vs ≈ 1,0 observada), costo de la deuda y tasa marginal','ESTIMADOS; con beta 1,00 la Base sería 533,88'],
      ['Auditoría económica independiente','NO_EJECUTADA (R6)'],
      ['<code>AISLAMIENTO=OK</code>','Los datos vienen de la SEC y de precios de mercado; ninguna revisión anterior de MSFT (A-1.2, Floyd F1–F5) se usó como insumo']]))
    return ''.join(h)
