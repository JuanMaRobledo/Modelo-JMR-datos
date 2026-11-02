"""Fase 2 R3 AMZN: escribe SOLO celdas de entrada (correcciones de la auditoría fase 4 que la regla admite), con nota.
No toca fórmulas. Hoja R3 = copia de R2 en Análisis/AMZN."""
import sys
sys.path[:0]=['.','scripts']
from jmr_valuation.io.sheets_auth import get_gspread_client
R3='1yzSqSP3Qopz3lPBNKsyXCsNSgioxZkoWOrZ6eaTjBvA'
sh=get_gspread_client().open_by_key(R3)
CRP=(0.0078*43212+0.0091*30688+0.018*107467)/716924
ERP=0.0379; WT=0.0494+ERP; MID=round((WT+0.165)/2,4)
E={
 ('Country equity risk premiums','B2'):(ERP,"[DATO R3] Prima madura Damodaran 1-nov-2026, columna T12m (convención de corte JMR, igual que corte_vigente.json oct=3,70 %), ERPNov26.xlsx, T.Bond 4,94 % = Treasury 10A 30-oct-2026 (Input B35). Misma fecha que Rf (REGLAS §4). Sustituye el rebase 4,55 % de R2 (auditoría A-01). https://pages.stern.nyu.edu/~adamodar/pc/implprem/ERPNov26.xlsx"),
 ('Cost of capital worksheet','B27'):(ERP+CRP,f"[CÁLCULO R3] {ERP:.4f} + CRP ponderada por ingresos FY25 (0,0078×43212 UK + 0,0091×30688 Japón + 0,018×107467 resto)/716924 = {CRP:.6f}. CRP de la tabla Damodaran ene-2026 (sin cambio frente a R2). Auditoría A-01."),
 ('Cost of capital worksheet','G39'):('Software (System & Application)',"[JUICIO R3] AWS = infraestructura y plataforma de nube (IaaS/PaaS), más cercana a Software (System & Application) que a Computer Services (consultoría/servicios TI). Coherente con la referencia de foso (industria proxy Retail + Software). Beta de regresión 60m AMZN vs SPY = 1,49 (EE 0,21) como contraste: la bottom-up R2 0,86 quedaba fuera de su IC 95 %. Auditoría B-03."),
 ('Input sheet','B84'):(294595-54440,"[CÁLCULO R3] Valor económico neto de impuesto diferido: 294.595 − 54.440. DTL = 34.608 (AOCI de las notas de Anthropic, 10-Q T3-26) + (92.500 − base 12.100)×24,67 % preferentes (base = 8.000 − 5.900 notas convertidas + 5.000 Serie G + 5.000 Serie H). OpenAI a costo: sin DTL. Auditoría B-01. B83 (contable) sin cambio."),
 ('Input sheet','B40'):(0.01,"[JUICIO TÉCNICO R3] Ejercicio 0,01 USD (RSU, ejercicio económico cero). Con 0 exacto, la fórmula nativa calcula ln(S/0) → IFERROR → N(d1)=0,5 y valora cada RSU a la mitad. 0,01 es inmaterial frente a S y deja Black-Scholes en su límite correcto (≈ S ajustado). Excepción declarada; auditoría C-01. La corrección definitiva es de mantenimiento de la maestra."),
 ('Input sheet','B50'):(0.165,"[REGLA R3] ROIC terminal Base = referencia de foso JMR (reference/moat_2026-09-30.json: AMZN «ventaja durable», industria ponderada 22 %, topada en el ROIC actual → 16,5 %), REGLAS §4. R2 usaba 12,5 % sin citar la referencia (auditoría B-02)."),
 ('Escenarios e historias','N5'):(0.165,"[REGLA R3] Base: ventaja durable → referencia de foso 16,5 % (REGLAS §4)."),
 ('Escenarios e historias','N6'):(MID,f"[REGLA R3] Conservadora: ventaja que se desvanece → punto medio entre costo de capital terminal {WT:.4f} y 16,5 % = {MID:.4f} (REGLAS §4)."),
 ('Escenarios e historias','N7'):(round(WT,4),f"[REGLA R3] Disrupción: sin ventaja → ROIC terminal = costo de capital terminal (Rf 4,94 % + prima madura 3,79 % = {WT:.4f})."),
 ('Escenarios e historias','N8'):(0.20,"[JUICIO R3] Optimista: ventaja durable con mezcla AWS/publicidad mayor; 20 % < promedio de industria ponderado 22 % (referencia de foso) y ≈ ROIC año 10 del Optimista (20,3 %)."),
 ('Tesis de Inversión y Supuestos','A1'):("AMZN · AMZN-20261102-A12-R3 · FASE2 SUPUESTOS Y VALORACIÓN · CANDIDATO",None),
}
por_hoja={}
for (t,c),(v,nota) in E.items(): por_hoja.setdefault(t,[]).append((c,v,nota))
for t,items in por_hoja.items():
    ws=sh.worksheet(t)
    ws.batch_update([{'range':c,'values':[[v]]} for c,v,_ in items], value_input_option='RAW')
    notas={c:n for c,_,n in items if n}
    if notas: ws.update_notes(notas)
    print(t, [(c,v) for c,v,_ in items])
