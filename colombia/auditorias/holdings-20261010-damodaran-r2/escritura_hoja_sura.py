from gs import S
SID='1Nb9_T6n8xbJikr68TN5MA5bIIiwm0aKrsF7m4MmOHyM'
T='CO · Ke y SOTP 60-40'
data=[]
def put(rng,rows): data.append({'range':rng,'values':rows})
# 0) new tab
meta=S.spreadsheets().get(spreadsheetId=SID,fields='sheets.properties(title,sheetId)').execute()
if T not in [s['properties']['title'] for s in meta['sheets']]:
    S.spreadsheets().batchUpdate(spreadsheetId=SID,body={'requests':[{'addSheet':{'properties':{'title':T,'index':1,'gridProperties':{'rowCount':140,'columnCount':8,'frozenRowCount':1}}}}]}).execute()
q=f"'{T}'"
# 1) Datos
put("Datos!C5",[["Utilidad UDM 2T26 · calculadora de valoración del emisor (ago-2026)"]])
put("Datos!C6:D6",[[7934717,0.249365]])
put("Datos!F6:F8",[["Patrimonio controlador 38.123.672 COPm = calculadora emisor; UDM 7.934.717 y 235.565.920 acciones (24,9365%) de la calculadora del emisor ago-2026; antes 7.722.604 proxy y 24,88%"],["Libro 10.449.483 (tangible 4.538.077) y UDM 1.272.336 = calculadora emisor ago-2026; % económico 93,32% (emisor redondea 93,3%)"],["Libro 6.537.339 (tangible 5.516.362) y UDM 904.341 = calculadora emisor ago-2026; % económico 81,13% (emisor 81,1%)"]])
put("Datos!B26:C27",[[67480,"GRUPOSURA cierre BVC 9-oct-2026: 67.480 en Yahoo Finance y StockAnalysis (coinciden); Investing 67.760 descartado"],["2026-10-09 cierre BVC, COP; PFGRUPSURA 58.600 en 'CO · Clase y mercado'","Precio ordinaria en Datos para margen ordinaria"]])
# 2) Ke + SOTP tab
rows=[
 ["JMR · Grupo SURA · Costo del patrimonio Damodaran y SOTP canónico 60/40 · corte 9/10-oct-2026"],
 ["Mismo corte Colombia que PFDAVVNDA publicado: Rf COP = TES − spread soberano; ERP madura y CRP del archivo de países Damodaran jul-2026. Beta bottom-up del sector; beta → 1 entre años 6 y 10 (Damodaran: Goldman Sachs 2009 1,5→1,2; 'set the beta in stable growth to one')."],
 ["Mismo Ke en las cuatro historias: el riesgo operativo va en los flujos (ROE, crecimiento), no en la tasa. Pesos por país = ESTIMACIÓN del analista (cartera/utilidad/primas aproximadas); sensibilidad 100% Colombia en Sensibilidad."],
 [],
 ["Insumo","Valor","Fuente / convención"],
 ["TES COP ~10 años (jul-2036)",0.13217,"IRC/MHCP informe diario 25-sep-2026; mismo dato que PFDAVVNDA"],
 ["Spread default Colombia (Baa3)",0.01749881223830583,"Damodaran ctrypremJuly26.xlsx, Colombia"],
 ["Rf COP depurada","=B6-B7","TES menos spread soberano (Damodaran: riskfree local = bono de gobierno − default spread)"],
 ["ERP madura",0.042,"Damodaran ctrypremJuly26: total EE.UU. 4,42% − CRP EE.UU. 0,22%"],
 ["ERP implícita oct-2026 (sensibilidad)",0.037,"Damodaran ERPOct26.xlsx (sobre UST 5,29%); no usada en Base"],
 ["Beta estable (años 6-10 → terminal)",1,"Damodaran, Investment Valuation cap. 12; Valuing Financial Service Firms (Goldman Sachs)"],
 [],
 ["País","CRP Damodaran jul-2026","Cibest (cartera aprox.)","SURA AM (utilidad aprox.)","Suramericana (primas aprox.)"],
 ["Colombia",0.0272018253,0.72,0.20,0.62],
 ["Panamá",0.0272018253,0.13,0,0.04],
 ["El Salvador",0.0804417616,0.08,0,0.03],
 ["Guatemala",0.0309777,0.07,0,0],
 ["Chile",0.0104734301,0,0.35,0.10],
 ["México",0.0272018253,0,0.25,0.08],
 ["Perú",0.0197831457,0,0.15,0],
 ["Uruguay",0.0197831457,0,0.05,0.03],
 ["Brasil",0.0309777,0,0,0.06],
 ["Rep. Dominicana",0.0372356,0,0,0.04],
 ["Peso total","","=SUM(C14:C23)","=SUM(D14:D23)","=SUM(E14:E23)"],
 ["CRP ponderado","","=SUMPRODUCT($B$14:$B$23;C14:C23)/C24","=SUMPRODUCT($B$14:$B$23;D14:D23)/D24","=SUMPRODUCT($B$14:$B$23;E14:E23)/E24"],
 ["Beta inicial (Damodaran global ene-2026)","","0,7","0,75","0,66"],
 ["Ke inicial años 1-5","","=$B$8+C26*$B$9+C25","=$B$8+D26*$B$9+D25","=$B$8+E26*$B$9+E25"],
 ["Ke estable (β=1) año 10 y terminal","","=$B$8+$B$11*$B$9+C25","=$B$8+$B$11*$B$9+D25","=$B$8+$B$11*$B$9+E25"],
 ["Fuente beta","","Bank (Money Center) global 0,697 (EM 0,586)","Investments & Asset Mgmt global 0,748 (EM 0,669)","Insurance General 0,51 / Life 0,80 global; promedio"],
 ["Ke holding (ponderado por valor RE Base de las participadas)","=SUMPRODUCT(C27:E27;Resumen!B6:B8)/SUM(Resumen!B6:B8)","Descuenta gastos corporativos (Resumen!B11) y precios FY+3"],
 [],
 ["ROE terminal = Ke estable + spread (regla Damodaran del Modelo JMR)","","Cibest","SURA AM","Suramericana"],
 ["Base","","0,01","0","0"],
 ["Conservador","","-0,02","-0,03","-0,03"],
 ["Optimista","","0,03","0,02","0,02"],
 ["Disrupción","","ROE absoluto 8%","ROE absoluto 7%","ROE absoluto 6%"],
 ["Criterio","Sin ventaja: ROE terminal = Ke. Ventaja durable (Cibest: líder con fondeo barato): +1pp. Antes los tres ROE terminales Base quedaban 0,5–4pp debajo del Ke (destrucción de valor perpetua), contrario a la regla del modelo; la Disrupción conserva deterioro absoluto."],
 [],[],
 ["SOTP CANÓNICO DE HOLDINGS · 60% SOTP ECONÓMICO + 40% SOTP DE MÚLTIPLOS POR PARTICIPADA (prompt Colombia 10-oct-2026)"],
 ["Insumo","Valor","Fuente"],
 ["Precio CIBEST ordinaria 9-oct-2026",88000,"BVC cierre (Yahoo Finance CIBEST.CL); P/B 2,18×, P/E UDM 11,0×"],
 ["Acciones Cibest de Grupo SURA",235565920,"Calculadora de valoración del emisor ago-2026 (24,9365% de 944,66 millones)"],
 ["Participación Cibest a mercado COPm","=B42*B43/1000000","Acciones ordinarias: se usa el precio de la ordinaria"],
 ["Peso SOTP económico",0.6,"Parámetro del Modelo JMR, no regla Damodaran; editable"],
 ["Peso SOTP múltiplos",0.4,"Parámetro del Modelo JMR; editable"],
 [],
 ["P/E sector (UDM)","","Cibest","SURA AM","Suramericana"],
 ["Mediana pares LatAm 9-oct-2026","","=MEDIAN(C99:C106)","=MEDIAN(C107:C108)","=MEDIAN(C109:C112)"],
 ["Damodaran mercados emergentes ene-2026 (Mkt cap / NI firmas con utilidad)","","9,0707","16,5569","10,1018"],
 ["P/E aplicado = promedio de las dos anclas","","=AVERAGE(C49:C50)","=AVERAGE(D49:D50)","=AVERAGE(E49:E50)"],
 ["Utilidad UDM 100% COPm","","=Datos!C6","=Datos!C7","=Datos!C8"],
 ["Participación económica","","=Datos!D6","=Datos!D7","=Datos!D8"],
 ["Valor por múltiplos atribuible Base COPm","","=C51*C52*C53","=D51*D52*D53","=E51*E52*E53"],
 [],
 ["Historia (COPm salvo indicación)","Base","Conservador","Optimista","Disrupción"],
 ["Escala Cibest (RE historia / RE Base)","=Resumen!B6/Resumen!$B$6","=Resumen!C6/Resumen!$B$6","=Resumen!D6/Resumen!$B$6","=Resumen!E6/Resumen!$B$6"],
 ["Escala SURA AM","=Resumen!B7/Resumen!$B$7","=Resumen!C7/Resumen!$B$7","=Resumen!D7/Resumen!$B$7","=Resumen!E7/Resumen!$B$7"],
 ["Escala Suramericana","=Resumen!B8/Resumen!$B$8","=Resumen!C8/Resumen!$B$8","=Resumen!D8/Resumen!$B$8","=Resumen!E8/Resumen!$B$8"],
 ["Cibest a bolsa × escala","=$B$44*B57","=$B$44*C57","=$B$44*D57","=$B$44*E57"],
 ["SURA AM · RE intrínseco","=Resumen!B7","=Resumen!C7","=Resumen!D7","=Resumen!E7"],
 ["Suramericana · RE intrínseco","=Resumen!B8","=Resumen!C8","=Resumen!D8","=Resumen!E8"],
 ["Otros activos netos","=Datos!$B$20","=Datos!$B$20","=Datos!$B$20","=Datos!$B$20"],
 ["Puente matriz (deuda neta y otros)","=-Datos!$B$29","=-Datos!$B$29","=-Datos!$B$29","=-Datos!$B$29"],
 ["VP gastos corporativos","=-Resumen!B11","=-Resumen!C11","=-Resumen!D11","=-Resumen!E11"],
 ["SOTP económico COPm","=SUM(B60:B65)","=SUM(C60:C65)","=SUM(D60:D65)","=SUM(E60:E65)"],
 ["SOTP económico COP/acción","=B66*1000000/Datos!$B$30","=C66*1000000/Datos!$B$30","=D66*1000000/Datos!$B$30","=E66*1000000/Datos!$B$30"],
 ["Cibest por múltiplos × escala","=$C$54*B57","=$C$54*C57","=$C$54*D57","=$C$54*E57"],
 ["SURA AM por múltiplos × escala","=$D$54*B58","=$D$54*C58","=$D$54*D58","=$D$54*E58"],
 ["Suramericana por múltiplos × escala","=$E$54*B59","=$E$54*C59","=$E$54*D59","=$E$54*E59"],
 ["SOTP múltiplos COPm","=SUM(B68:B70)+SUM(B63:B65)","=SUM(C68:C70)+SUM(C63:C65)","=SUM(D68:D70)+SUM(D63:D65)","=SUM(E68:E70)+SUM(E63:E65)"],
 ["SOTP múltiplos COP/acción","=B71*1000000/Datos!$B$30","=C71*1000000/Datos!$B$30","=D71*1000000/Datos!$B$30","=E71*1000000/Datos!$B$30"],
 ["VALOR BASE JMR 60/40 COP/acción","=($B$45*B67+$B$46*B72)/($B$45+$B$46)","=($B$45*C67+$B$46*C72)/($B$45+$B$46)","=($B$45*D67+$B$46*D72)/($B$45+$B$46)","=($B$45*E67+$B$46*E72)/($B$45+$B$46)"],
 ["Valor intrínseco Damodaran RE (todas las participadas)","=Resumen!B14","=Resumen!C14","=Resumen!D14","=Resumen!E14"],
 ["Probabilidad","=Resumen!B15","=Resumen!C15","=Resumen!D15","=Resumen!E15"],
 ["Esperado 60/40","=SUMPRODUCT(B73:E73;B75:E75)"],
 ["Esperado SOTP económico","=SUMPRODUCT(B67:E67;B75:E75)"],
 ["Esperado SOTP múltiplos","=SUMPRODUCT(B72:E72;B75:E75)"],
 ["Esperado intrínseco RE","=SUMPRODUCT(B74:E74;B75:E75)"],
 [],
 ["Precio GRUPOSURA 9-oct","=Datos!B26"],
 ["Precio PFGRUPSURA 9-oct","='CO · Clase y mercado'!B6"],
 ["Base 60/40 / precio ordinaria − 1","=B73/B81-1"],
 ["Base 60/40 / precio preferencial − 1","=B73/B82-1"],
 ["Intrínseco RE / precio ordinaria − 1","=B74/B81-1"],
 ["Intrínseco RE / precio preferencial − 1","=B74/B82-1"],
 [],
 ["HORIZONTE FY+3 · P3 = (V0 − VP dividendos) × (1+Ke)^3; P3/(1+Ke)^3 + VP div = V0"],
 ["Ke holding","=B30"],
 ["VP dividendos Base 2.000/2.200/2.400 (hipótesis)","=Datos!B25/(1+B89)+'CO · Ponderaciones'!C19/(1+B89)^2+'CO · Ponderaciones'!D19/(1+B89)^3"],
 ["Método","Hoy COP","FY+3 exdiv COP","VP FY+3 exdiv","Control VP FY+3 + VP div − hoy"],
 ["SOTP económico","=B67","=(B92-$B$90)*(1+$B$89)^3","=C92/(1+$B$89)^3","=D92+$B$90-B92"],
 ["SOTP múltiplos","=B72","=(B93-$B$90)*(1+$B$89)^3","=C93/(1+$B$89)^3","=D93+$B$90-B93"],
 ["Base 60/40","=B73","=(B94-$B$90)*(1+$B$89)^3","=C94/(1+$B$89)^3","=D94+$B$90-B94"],
 ["Intrínseco RE","=B74","=(B95-$B$90)*(1+$B$89)^3","=C95/(1+$B$89)^3","=D95+$B$90-B95"],
 [],
 ["PARES (Yahoo Finance, 9-oct-2026, P/E UDM; se excluye la propia participada)","Ticker","P/E UDM","Sector"],
 ["Credicorp","BAP",14.358,"Banca Perú"],
 ["Banco Santander Chile","BSAC",12.440,"Banca Chile"],
 ["Banco de Chile","BCH",14.900,"Banca Chile"],
 ["Itaú Unibanco","ITUB",13.026,"Banca Brasil"],
 ["Banorte","GFNORTEO.MX",8.827,"Banca México"],
 ["Grupo Aval","AVAL",12.868,"Banca Colombia"],
 ["Davivienda PF","PFDAVVNDA.CL",8.584,"Banca Colombia"],
 ["Bradesco","BBD",13.871,"Banca Brasil"],
 ["AFP Habitat","HABITAT.SN",8.569,"Pensiones Chile"],
 ["Vinci Partners","VINP",9.863,"Gestión de activos Brasil"],
 ["BB Seguridade","BBSE3.SA",8.630,"Seguros Brasil"],
 ["Porto Seguro","PSSA3.SA",9.359,"Seguros Brasil"],
 ["Caixa Seguridade","CXSE3.SA",13.821,"Seguros Brasil"],
 ["Quálitas","Q.MX",13.746,"Seguros México"],
 [],
 ["Referencias Damodaran usadas","Valuing Financial Service Firms (2009): patrimonio, rendimientos en exceso, ROE estable = Ke (Goldman Sachs) · Good banks/bad banks (Citi, may-2023): P/BV según ROE − Ke · Cash and cross holdings (2010) y a22.htm: valorar cada participación y sumar la cuota económica; descuento de holding por costos y por desconfianza en la asignación de capital · Datasets ene-2026: betaGlobal, betaemerg, peemerg, pbvemerg"],
]
put(f"{q}!A1:E{len(rows)}",rows)
# 3) Supuestos
put("Supuestos!C6:C9",[[f"={q}!$B$30"]]*4)
put("Supuestos!H14",[["Ke estable (β=1)"]])
put("Supuestos!G14",[["Ke inicial"]])
gcol={1:'C',2:'D',3:'E'}
G=[];H=[];D=[]
for i,(scen,sp_row) in enumerate([('Base',33)]*3+[('Conservador',34)]*3+[('Optimista',35)]*3+[('Disrupcion',None)]*3):
    p=i%3+1; c=gcol[p]
    G.append([f"={q}!${c}$27"]); H.append([f"={q}!${c}$28"])
    if sp_row: D.append([f"={q}!${c}$28+{q}!{c}{sp_row}"])
put("Supuestos!G15:G26",G); put("Supuestos!H15:H26",H); put("Supuestos!D15:D23",D)
put("Supuestos!A27",[["Ke por participada = Rf COP depurada + beta sector × ERP madura + CRP ponderado por país (pestaña 'CO · Ke y SOTP 60-40'); converge a beta 1 entre años 6 y 10. Ke holding (C6:C9) = promedio ponderado por valor."]])
put("Supuestos!A29",[["ROE terminal Base/Conservador/Optimista = Ke estable + spread de la historia (D15:D23); Disrupción conserva ROE absoluto deteriorado (D24:D26)."]])
# 4) scenario sheets
names=['Base','Conservador','Optimista','Disrupcion']
cols='BCDEFGHIJK'
for si,n in enumerate(names):
    for p in (1,2,3):
        sh=f"{n}_{p}"; r=15+si*3+(p-1)
        put(f"{sh}!A32:B33",[["Ke estable (β=1)",f"=Supuestos!H{r}"],["Ke año t (β converge a 1 años 6-10)",""]])
        put(f"{sh}!B33:K33",[[f"=IF({c}10<=5;$B$5;$B$5+($B$32-$B$5)*({c}10-5)/5)" for c in cols]])
        put(f"{sh}!B18:K18",[[f"={c}14-{c}33*{c}11" for c in cols]])
        put(f"{sh}!B19:K19",[["=1+B33"]+[f"={cols[j-1]}19*(1+{cols[j]}33)" for j in range(1,10)]])
        put(f"{sh}!B23:B24",[[f"=K17*(Supuestos!D{r}-$B$32)/($B$32-Supuestos!F{r})"],[f"=K17*(Supuestos!D{r}-Supuestos!F{r})/($B$32-Supuestos!F{r})"]])
        put(f"{sh}!B29",[[f'=IF($B$32>Supuestos!F{r};"OK";"ERROR")']])
# 5) Multiples proxy rows -> new sector P/E
put("Multiples!B23:C25",[[f"={q}!C51",1],[f"={q}!D51",1],[f"={q}!E51",1]])
put("Multiples!E23:E25",[["P/E = promedio mediana pares LatAm 9-oct-2026 y Damodaran EM ene-2026; ver 'CO · Ke y SOTP 60-40'"]]*3)
put("Multiples!A21",[["CONTRASTE RELATIVO · P/E sectorial por participada (pares LatAm 9-oct-2026 + Damodaran EM ene-2026)"]])
put("Multiples!C26",[["Utilidad UDM del emisor (calculadora ago-2026) × P/E sector; = SOTP múltiplos Base de 'CO · Ke y SOTP 60-40'"]])
# 6) Sensibilidad row 6 -> stable Ke
put("Sensibilidad!B6",[["=IF(Datos!B30=0;0;((Base_1!K17*Datos!D6/(Base_1!B32-Supuestos!F15)/Base_1!K19)+(Base_2!K17*Datos!D7/(Base_2!B32-Supuestos!F16)/Base_2!K19)+(Base_3!K17*Datos!D8/(Base_3!B32-Supuestos!F17)/Base_3!K19))*1/100*1000000/Datos!B30)"]])
# 7) Clase y mercado / control texts
put("'CO · Clase y mercado'!C5",[["BVC cierre 9-oct (Yahoo Finance y StockAnalysis coinciden: 67.480)"]])
put("'CO · Clase y mercado'!F4",[["Intrínseco RE Base COP"]])
put("'CO · Clase y mercado'!G4:G6",[["Base JMR 60/40 COP"],[f"={q}!B73"],[f"={q}!B73"]])
put("Control!B13:C13",[["PARCIAL","P/E sector por participada: mediana de pares LatAm + Damodaran EM; sin serie histórica"]])
put("Resumen!A2",[["GRUPOSURA y PFGRUPSURA · revisión Damodaran 10-oct-2026 (r2); estados 2T26; esta hoja = SOTP INTRÍNSECO por rendimientos excedentes. Base publicado 60/40 en 'CO · Ke y SOTP 60-40'."]])
res=S.spreadsheets().values().batchUpdate(spreadsheetId=SID,body={'valueInputOption':'USER_ENTERED','data':data}).execute()
print(res['totalUpdatedCells'])
