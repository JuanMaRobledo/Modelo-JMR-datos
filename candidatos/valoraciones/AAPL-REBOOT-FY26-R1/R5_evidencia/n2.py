from datos import *
from fmt import *
from n1 import rev,cogs,ebit,ni,rd,sga,cfo,capex,bb,dv,fcf,gm,em,b,c,o,vb,vc,vo,px,mos_price,netcash
YR=[f'FY{y}' for y in FY]
def row(label,vals,d=0): return [label]+[f(x,d) for x in vals]
def prow(label,vals,d=1): return [label]+[p(x,d) for x in vals]
def proj(st,name):
    yrs=['Año base']+[f'Año {i}' for i in range(1,11)]+['Terminal']
    L=[('Crecimiento de ingresos',[None]+st['growth'][1:],'p'),('Ingresos',st['rev'],'n'),('Margen EBIT (ajustado I+D)',st['margin'],'p'),
       ('EBIT',st['ebit'],'n'),('Tasa de impuestos',st['tax'],'p'),('EBIT(1−t)',st['nopat'],'n'),('Reinversión',st['reinv'],'n'),('FCFF',st['fcff'],'n'),
       ('Costo de capital',st['wacc'],'p2'),('Factor de descuento acumulado',st['df'],'d'),('VP(FCFF)',st['pv'],'n'),
       ('Ventas/capital',st['s2c'],'d1'),('Capital invertido',st['ic'],'n'),('ROIC',st['roic'],'p')]
    rows=[]
    for lab,v,k in L:
        out=[lab]
        for x in v:
            if x is None: out.append('—')
            elif k=='p': out.append(p(x,1))
            elif k=='p2': out.append(p(x,2))
            elif k=='d': out.append(f(x,4))
            elif k=='d1': out.append(f(x,1))
            else: out.append(f(x,0))
        rows.append(out)
    return H3_(f'Historia {name}')+table(yrs[:len(rows[0])],rows)
def H3_(t): return f'<h4>{t}</h4>'
def bridge(st,name,prob):
    return [name,f(st['sum_pv']-st['pv_tv'],0),f(st['tv'],0),f(st['pv_tv'],0),f(st['sum_pv'],0),p(st['pv_tv']/st['sum_pv'],0),
            f(st['op_assets'],0),f(-st['debt'],0),f(st['cash'],0),f(st['equity'],0),f(st['shares'],1),usd(st['value'],4)]
def n2():
    h=['<h2>Nivel 2 · Valoración reproducible</h2>']
    h.append(H3('1. Identificación, fuentes y unidades'))
    h.append(table(['Concepto','Valor'],[
      ['Empresa / ticker','Apple Inc. · AAPL · Nasdaq · USD · millones salvo por acción'],
      ['Revisión','AAPL-REBOOT-FY26-R1 · perfil Reboot · contrato jmr-reboot-3libros-v1'],
      ['Corte contable / precio','Ejercicio fiscal 2026 (cierre 26-sep-2026) · precio 342,37 (cierre 6-nov-2026, FMP y Alpha Vantage)'],
      ['Libro Históricos','1b1G1RciCJYH-J-RLXZhQX90RBlEZ-GY4qi13vSOdxEs'],
      ['Libro DCF Base / Conservadora / Optimista','1FDKimjBtpWeJO1wjK2-iFbQBhc7fziRWspCqkl41am8 / 1z7399gpLt0t0IMTgvXav4u6tEEsCIevd-GSE1U7KMcM / 18_DpC1IBerZBKzBpWWkSi-9h4EzXH_fIlesGqmeKffM'],
      ['Libro Múltiplos','1SJn1NC6zGAWvMPOS6yK-0TxheNlZ0oabBPX8yaqpXmg'],
      ['Documento de análisis','1CxPNSRM5GcV0UvMgxiaByM5xOQ55b1peHqMOT_c8n60'],
      ['Fuentes','SEC XBRL <em>companyfacts</em> del 10-K FY2026 (primaria); FMP y Alpha Vantage (contraste); FRED DGS10 (tasa libre); Damodaran nov-2026 (prima, primas por país, industrias, calificaciones)'],
      ['Motor','fcffsimpleginzu original de Damodaran (17 hojas; 1.230 fórmulas y 76 comentarios sin cambios; 5 celdas de entrada con valor en vez de fórmula: Input sheet B27, B28, B29, B32, B62)']]))
    h.append(H3('2. Estados históricos y LTM'))
    h.append(P('LTM = FY2026 (el ejercicio cierra en septiembre y el corte contable es el 10-K). Cifras del libro de Históricos, XBRL del 10-K. FY2017 con acciones ×4 por el split 4:1.'))
    h.append(table(['Estado de resultados']+YR,[
      row('Ingresos',rev),row('Costo de ventas',cogs),row('Utilidad bruta',[a-b_ for a,b_ in zip(rev,cogs)]),row('SG&A',sga),row('I+D',rd),
      row('EBIT reportado',ebit),row('Impuestos',s(IS,20)),row('Utilidad neta',ni),row('Acciones diluidas promedio',s(IS,26),0)]))
    h.append(table(['Balance']+YR,[
      row('Efectivo + inversiones CP + LP',[a+(b_ or 0)+(c_ or 0) for a,b_,c_ in zip(s(BS,3),s(BS,4),s(BS,14))]),row('Activos totales',s(BS,16)),
      row('Deuda LP + CP (sin arrendamientos)',[a+b_ for a,b_ in zip(s(BS,20),s(BS,25))]),row('Patrimonio',s(BS,34))]))
    h.append(table(['Flujo de caja']+YR,[
      row('Flujo operativo',cfo),row('Capex',capex),row('Flujo libre (CFO−capex)',fcf),row('Recompras',bb),row('Dividendos',dv),row('Compensación en acciones',s(CF,5))]))
    h.append(H3('3. Ratios y economía del negocio'))
    h.append(table(['Ratio']+YR,[
      prow('Margen bruto',gm),prow('Margen EBIT reportado',em),prow('Margen neto',[a/b_ for a,b_ in zip(ni,rev)]),
      prow('Tasa de impuestos efectiva',[a/b_ for a,b_ in zip(s(IS,20),s(IS,19))]),prow('I+D / ingresos',[a/b_ for a,b_ in zip(rd,rev)]),
      prow('Capex / ingresos',[a/b_ for a,b_ in zip(capex,rev)]),prow('Flujo libre / ingresos',[a/b_ for a,b_ in zip(fcf,rev)]),
      prow('Retorno al accionista / flujo libre',[(a+b_)/c_ for a,b_,c_ in zip(bb,dv,fcf)],0)]))
    h.append(P(f'Salud financiera FY2026: caja e inversiones {f(136935)} M; deuda total con arrendamientos {f(94479)} M; caja neta {f(netcash)} M; liquidez corriente {f(173857/s(BS,24)[-1],2)}x (activo corriente {f(173857)} / pasivo corriente {f(s(BS,24)[-1])}); EBIT / intereses estimados {f(158063/3000,0)}x. Eficiencia: ingresos / activos {f(rev[-1]/s(BS,16)[-1],2)}x. Dividendo por acción y recompras: ver libro Históricos, hoja Dividendos.'))
    h.append(H3('4. Puente contable a económico'))
    h.append(table(['Concepto','Valor','Nota'],[
      ['EBIT reportado FY2026',f(158063),'10-K'],['Ajuste por I+D capitalizada (5 años)','+'+f(16965),'Activo de investigación 109.443 M; I+D FY2017–26'],
      ['EBIT ajustado',f(175028),'Margen ajustado 36,55 % (reportado 33,0 %)'],
      ['Capital invertido (año base, con I+D)',f(179080),'Patrimonio 112.093 + deuda 94.479 − caja 136.935 + activo de investigación 109.443'],
      ['Deuda total',f(94479),'80.111 financiera + 14.368 arrendamientos ASC 842 (ya en balance; <em>Operating lease commitments</em> = No)'],
      ['Caja e inversiones',f(136935),'Efectivo 36.305 + inversiones CP 20.417 + inversiones LP 80.213'],
      ['Acciones (millones)',f(14590.6,1),'14.532,2 de la portada del 10-K + 58,4 de dilución por RSU; sin opciones (<em>Option value</em> = No)'],
      ['Tasa efectiva / marginal','17,0 % / 25 %','27.062 / 159.237; la efectiva converge a la marginal en el año 10'],
      ['Gasto por intereses (ESTIMADO)','3.000','No divulgado; ver limitaciones']]))
    h.append(H3('5. Supuestos efectivos por historia'))
    h.append(table(['Entrada del motor','Celda','Conservadora','Base','Optimista'],[
      ['Crecimiento año 1','Input B26','2,5 %','6,0 %','9,0 %'],['Margen EBIT año 1','B27','35,5 %','36,6 %','37,0 %'],['CAGR años 2–5','B28','2,0 %','5,5 %','8,0 %'],
      ['Margen objetivo','B29','31,0 %','37,0 %','40,0 %'],['Año de convergencia del margen','B30','5','5','5'],['Ventas/capital años 1–5 · 6–10','B31 · B32','2,4 · 2,4','3,0 · 3,0','3,5 · 3,5'],
      ['ROIC terminal','B48 · B49','Costo de capital','44,76 %','44,76 %'],['Fracaso · probabilidad · valor en fracaso','B51–B54','Sí · 5 % · 60 %','No','No'],
      ['Tasa libre','B34','4,86 %','4,86 %','4,86 %'],['Crecimiento terminal','B68','4,0 %','4,0 %','4,0 %'],['Impuesto efectivo / marginal','B23 · B24','17,0 % / 25 %','17,0 % / 25 %','17,0 % / 25 %']]))
    h.append(H3('6. Costo de capital descompuesto'))
    h.append(table(['Componente','Valor','Fuente / criterio'],[
      ['Tasa libre','4,86 %','FRED DGS10, 6-nov-2026'],['Beta desapalancada (multinegocio EE. UU.)','1,283','Computers/Peripherals 319.956; Electronics General 35.577; Software System & Application 123.301'],
      ['Beta apalancada','1,2988','D/E de mercado'],['Prima de riesgo (regiones)','4,2301 %','Norteamérica 198.083 (3,603 %); Europa Occidental 127.604 (4,424 %); Asia 153.147 (4,879 %)'],
      ['Prima madura (fase estable)','3,387 %','Damodaran, nov-2026 (decisión del usuario)'],['Costo del patrimonio (Ke)','10,3542 %','4,86 % + 1,2988 × 4,2301 %'],
      ['Costo de la deuda antes de impuestos','5,41 %','Calificación «Aa2/AA»; vencimiento medio 7 años'],['Pesos de mercado','98,4 % / 1,6 %','Capitalización 4.995.384 M; deuda a mercado 82.439 M'],
      ['Costo de capital inicial (años 1–5)',p(WACC0,2),'Común a las tres historias'],['Costo de capital terminal (año 10)',p(WACC_T,2),'Beta 1: 4,86 % + 3,387 %; baja linealmente en los años 6–10']]))
    h.append(H3('7. Proyección explícita anual completa'))
    h.append(P('Valores en millones de USD, calculados con el motor original (recálculo local con LibreOffice, idéntico al libro de Google Sheets a seis decimales). El año base usa EBIT ajustado por I+D.'))
    h.append(proj(c,'Conservadora (25 %)')+proj(b,'Base (50 %)')+proj(o,'Optimista (25 %)'))
    h.append(H3('8. Valor terminal y puente hasta la acción'))
    h.append(table(['Historia','VP flujos años 1–10','Valor terminal','VP valor terminal','Suma de VP','VP terminal / total','Activos operativos','− Deuda','+ Caja','Patrimonio','Acciones','Valor por acción'],
      [bridge(c,'Conservadora',.25),bridge(b,'Base',.5),bridge(o,'Optimista',.25)]))
    h.append(P(f'Conservadora: la suma de VP ({f(c["sum_pv"])} M) incluye el escenario de fracaso: probabilidad 5 % con recuperación de 60 % del valor ({f(c["proceeds"])} M) y 95 % de continuidad. Flujo terminal Base {f(b["tv_cf"])} M a costo de capital {p(b["tv_wacc"],2)} y g = 4,0 %: VT = {f(b["tv"])} M; el VP del valor terminal es el {p(b["pv_tv"]/b["sum_pv"],0)} del valor operativo. ROIC terminal Base 44,76 %: reinversión terminal = g / ROIC = {p(0.04/0.4476,1)} del NOPAT.'))
    h.append(H3('9. Escenarios y ciclos'))
    h.append(table(['Historia','Probabilidad','Valor DCF','Frente al precio','Aporte al esperado'],[
      ['Conservadora','25 %',usd(vc),p(vc/px-1),usd(.25*vc)],['Base','50 %',usd(vb),p(vb/px-1),usd(.5*vb)],['Optimista','25 %',usd(vo),p(vo/px-1),usd(.25*vo)],
      ['<strong>Valor esperado</strong>','100 %','<strong>'+usd(EXPECTED)+'</strong>',p(EXPECTED/px-1),usd(EXPECTED)]]))
    h.append(P(f'Probabilidades: tipo de historia «crecimiento maduro»; previa JMR 45 / 22,5 / 22,5 y 10 de disrupción → sin la cuarta historia, 50 / 25 / 25. Orden Conservadora ≤ Base ≤ Optimista: cumple. Costo de capital común a las tres historias: cumple. Fracaso solo en la Conservadora: cumple. <strong>MOS de 35 % solo sobre el DCF Base:</strong> 0,65 × {usd(vb,4)} = {usd(mos_price)}; en la Conservadora el mismo cálculo da {usd(vc*.65)} (informativo). Ciclo: FY2023 −2,8 %, FY2024 +2,0 %, FY2025 +6,4 %, FY2026 +15,1 %; la Base no extrapola el pico.'))
    h.append(H3('10. Cinco múltiplos prioritarios'))
    h.append(P('Libro Múltiplos (sistema Atlas original; sin P/S ni P/BV). Los supuestos operativos son los del DCF (verificados) con base contable sin I+D capitalizada: márgenes objetivo 33,46 % / 27,46 % / 36,46 % (el ajuste de I+D de 3,54 puntos se resta). Múltiplo de salida: Conservadora = mediana de 10 años; Optimista = mediana de 5 años; Base = punto medio; todos ≤ múltiplo actual.'))
    rows=[]
    for m in MET:
        e=MULT_EXIT[m]; hm=HIST_MULT[m]
        rows.append([m,p(PESO[m],0),f(hm['y10'],2),f(hm['y5'],2),f(hm['y3'],2),f(hm['ttm'],2) if hm['ttm'] else 'N/D',f(e[0],2),f(e[1],2),f(e[2],2)])
    h.append(table(['Método','Peso total','Mediana 10 a','Mediana 5 a','Mediana 3 a','Actual (TTM)','Salida Cons.','Salida Base','Salida Opt.'],rows))
    for k,name in (('cons','Conservadora'),('base','Base'),('opt','Optimista')):
        rr=[[m]+[f(x,2) for x in OBJ[k][m]]+[f(x,2) for x in VPM[k][m]]+[f(CONS[k][m],2)] for m in MET]
        rr.append(['<strong>Consolidado</strong>','','','','','','<strong>'+f(MULT[k],2)+'</strong>'])
        h.append(H3_(f'Descuento a valor presente · {name}')+table(['Método','Precio+div FY+1','FY+2','FY+3','VP 1 año','VP 2 años','VP 3 años','Consolidado hoy'],rr))
    h.append(P(f'Pesos de los años 1/2/3 en cada método: 20 % / 30 % / 50 % (sobre valores presentes). Ke: 10,3542 % en los tres escenarios (mismo que el DCF). Ponderación «Madura»: DCF 65 % y múltiplos 35 %; los pesos totales por método (8/8/9/7/3 %) suman 35 %. Valor combinado (secundario): {usd(COMB["cons"])} / {usd(COMB["base"])} / {usd(COMB["opt"])}. Chequeo VP3 < FY+3: OK en los tres escenarios.'))
    h.append(H3('11. Sensibilidades DCF y de múltiplos + DCF inverso'))
    GL=[0.035,0.045,0.055,0.065,0.075]; ML=[0.33,0.35,0.37,0.39,0.41]; DW=[-0.01,-0.005,0,0.005,0.01]; TG=[0.03,0.035,0.04,0.045,0.048]
    A=[[f(SENS[f'a_{i}_{j}'],2) for j in range(5)] for i in range(5)]
    B=[[f(SENS[f'b_{i}_{j}'],2) for j in range(5)] for i in range(5)]
    h.append(H3_('Matriz A · CAGR años 2–5 × margen objetivo (precio por acción; centro = DCF Base)'))
    h.append(table(['CAGR \\ margen']+[p(m,0) for m in ML],[[p(g,1)]+A[i] for i,g in enumerate(GL)]))
    h.append(H3_('Matriz B · costo de capital inicial × crecimiento terminal (precio por acción; centro = DCF Base)'))
    h.append(table(['WACC inicial \\ g']+[p(t,1) for t in TG],[[p(WACC0+d,2)]+B[i] for i,d in enumerate(DW)]))
    h.append(P(f'Rango A: {usd(min(SENS[k] for k in SENS if k.startswith("a_")))} a {usd(max(SENS[k] for k in SENS if k.startswith("a_")))}; rango B: {usd(min(SENS[k] for k in SENS if k.startswith("b_")))} a {usd(max(SENS[k] for k in SENS if k.startswith("b_")))}. Centro de ambas = {usd(vb,4)} (conciliado). En ninguna celda se alcanza el precio de {usd(px)}.'))
    h.append(H3_('DCF inverso (una variable a la vez)'))
    h.append(table(['Variable que se resuelve','Valor necesario','Base','Resultado'],[
      ['Crecimiento anual años 1–5',p(REV['crecimiento'],2),'5,5–6,0 %',usd(px)],['Margen objetivo',p(REV['margen'],2),'37,0 %',usd(px)],
      ['Crecimiento con margen fijo de 40 %',p(REV['crec_con_margen40'],2),'5,5–6,0 %',usd(px)],
      ['Costo de capital inicial (mínimo probado 5,0 %)','No alcanza',p(WACC0,2),usd(282.29)+' con 5,0 %']]))
    h.append(P('Se resolvió por bisección sobre el motor original recalculado. Para llegar al precio hay que creer repetir cinco años el crecimiento de FY2026 o un margen que Apple nunca ha tenido.'))
    h.append(H3_('Matrices 5×5 por múltiplo (solo Base) · valor presente por acción'))
    h.append(P('Origen: hoja de cada método del libro Múltiplos (precio FY+3 por múltiplo elegido × fundamental FY+3). Para cumplir el estándar «celda = valor presente por acción, centro conciliado al VP3 del método», cada celda se descontó con el factor de 3 años del Ke Base (' + f(DF3,4) + ') y se sumó el valor presente de los dividendos del método (constante por método); el centro coincide exactamente con el VP3 Base de la hoja de Descuento. Derivación declarada; la hoja del libro conserva el precio FY+3 sin descontar.'))
    for m in MET:
        mt=MATRICES_M[m]; V=matriz_vp(m)
        h.append(H3_(f'{m} · centro VP3 = {usd(VPM["base"][m][2])}'))
        h.append(table([f'{m} \\ {mt["unidad"]}']+[f(x,0) for x in mt['col']],[[f(mt['fila'][i],2)+'x']+[f(x,2) for x in V[i]] for i in range(5)]))
    h.append(H3('12. Trazabilidad, reconciliaciones y límites'))
    h.append(table(['Control','Estado'],[
      ['Motor original sin cambios (1.230 fórmulas; 76 comentarios)','APROBADO (5 entradas con valor en vez de fórmula)'],
      ['Reproducción independiente del motor (LibreOffice sobre el xlsx original) vs Google Sheets','APROBADO (a 6 decimales): 106,916018 / 209,576147 / 260,445606'],
      ['Costo de capital común (Ke 10,3542 %; WACC 10,2520 % / 8,247 %)','APROBADO'],
      ['Probabilidades = 100 %; Cons ≤ Base ≤ Opt; fracaso solo en Conservadora; WACC > g','APROBADO'],
      ['MOS 35 % solo sobre DCF Base','APROBADO'],
      ['Libro Múltiplos: compuerta «LISTA PARA CALCULAR», 0 errores en 16 hojas; Resumen de valoraciones conciliado (6 controles)','APROBADO'],
      ['Huellas SHA-256 entre libros (H→D, H→M, D→M, M→D)','APROBADO (por script; sin IMPORTRANGE)'],
      ['Verificación documental FY2017–FY2023','PENDIENTE'],
      ['Gasto por intereses (estimado)','ESTIMADO, declarado; no altera el DCF'],
      ['ROIC marginal 70,5 % alto','PARCIAL: explicado por activos ligeros y recompras; sin contraste externo'],
      ['<em>Estado de fuentes primarias</em> del libro M','PENDIENTE; «Puente EEFF!B63 REVISAR SIGNO I+D» sin efecto (M no capitaliza I+D)'],
      ['Sensibilidades 5×5 de múltiplos','Derivadas del libro (ver §11); la hoja conserva el precio FY+3'],
      ['Auditoría económica independiente','NO_EJECUTADA (R6)'],
      ['<code>AISLAMIENTO=OK</code>','Nada de <code>archivo-v1/</code> ni del libro Floyd previo de AAPL']]))
    return ''.join(h)
