import json,openpyxl,sys
b=json.load(open('/tmp/claude-0/-home-user/02bdd347-b8be-5ac5-b2fc-27257db31770/scratchpad/bib_pub.json'));e=b['files']['empresas/NU.json']
p=sys.argv[1]; wb=openpyxl.load_workbook(p)
es=wb['JMR Estados']; fu=wb['JMR Fuentes']; sc=wb['JMR Escenarios']
cols={es.cell(3,c).value:c for c in range(3,13)}
for h in e['history']:
  y=2026 if str(h.get('periodo','')).startswith('LTM') else h['year']; es.cell(6,cols[y]).value=h['revenue']
es.cell(18,cols[2026]).value=41600.0; es.cell(19,cols[2026]).value=47487.0
es['M18']='Cartera bruta 30-sep-2026: USD 41,6 B (Form 6-K 3T26, presentación).'; es['M19']='Depósitos de clientes USD 47.487 M (Form 6-K 3T26, balance p. 6).'
es['M6']='Ingresos IFRS totales (86,1 % intereses y ganancias financieras en 9M26). LTM = FY25 + 9M26 − 9M25.'
es['M3']='2017–2019: N/D (Nu cotiza desde dic-2021; estados SEC desde FY2019, sin cotejo); columna 2026 = LTM 30-sep-2026.'
D6K='Form 6-K 3T26 Estados Financieros IFRS (acc. 0001292814-26-005272)'
filas={4:('Form 20-F FY2025 + '+D6K,'LTM 30-sep-2026','p. 5 (Income Statement): FY25 2.871,672 + 9M26 − 9M25'),
       5:(D6K,'30-sep-2026','p. 6 (Balance Sheet): patrimonio atribuible a los accionistas de Nu'),
       6:(D6K,'LTM 30-sep-2026','Estado de flujos de efectivo: dividendos pagados = 0 (recompras USD 500,4 M aparte)'),
       7:(D6K,'3T26','Nota 9 p. 23: acciones diluidas promedio 4.881,109 M')}
for r,(d,per,pag) in filas.items():
  fu.cell(r,2).value=d; fu.cell(r,3).value=per; fu.cell(r,4).value=pag
J={7:'ROE de alto crecimiento: LTM 27,3 % sobre patrimonio final (30,5 % sobre promedio) con tasa efectiva de 15,2 %. Base 26 % supone normalización parcial del impuesto hacia 34 % y costo de riesgo estable; Conservador 20 % (impuesto pleno + mora 90+ alta); Optimista 30 % (ROE actual sostenido).',
   8:'Retención: dividendos 0 y recompras de USD 500 M (13 % de la utilidad LTM). El crecimiento del patrimonio (ROE × retención ≈ 21 % en Base) debe acompañar el de los activos ponderados por riesgo (+28,3 % YTD) para sostener CET1 ≥ 7 % más colchón de gestión.',
   9:'ROE estable: Base 18 % (ventaja de costo digital frente a la banca tradicional; los líderes bancarios brasileños sostienen ROE superiores al costo de capital); Conservador = Ke (sin ventaja); Optimista 22 %.',
   17:'Beta 0,76 = promedio de betas apalancadas globales de Damodaran (ene-2026): Bank (Money Center) 0,697 y Financial Svcs. (Non-bank & Insurance) 0,823; banco digital y financiera de consumo sin garantías.',
   19:'ERP 7,62 % = prima madura 3,387 % + prima país regional 4,233 % (Brasil 90 % de ingresos), Damodaran ene-2026.',
   21:'Crecimiento estable 4 % nominal en USD, inferior a la tasa libre 5,15 %.'}
for r,t in J.items(): sc.cell(r,7).value=t
wb.save(p)
