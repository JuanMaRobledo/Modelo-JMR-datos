"""Actualiza el expediente PFGRUPOARG.CL (r2) con los valores leídos de la hoja tras la revisión Damodaran. Uso: python3 build_argos.py argos_readback.json"""
import json, sys
from pathlib import Path
P = Path(__file__).parent; F = P.parent.parent / "expedientes" / "PFGRUPOARG.CL-pfgrupoarg-20261009-clean-master.json"
rb = json.load(open(sys.argv[1])); d = json.load(open(F))
NOW = "2026-10-10T23:00:00.000Z"
c11 = rb["'CO 11 SOTP economico'!A4:G16"]; econ = c11[12][6]; hq = -c11[10][6]
sens11 = rb["'CO 11 SOTP economico'!G25:G29"]
c12 = [r[0] for r in rb["'CO 12 Comparables sector'!B18:B40"]]
fy = [r[0] for r in rb["'CO 12 Comparables sector'!B44:B54"]]
sc = rb["'CO 03 Escenarios'!G12:J15"]; vals = sc[1]; probs = sc[2]; expv = sc[3][0]
mult = c12[16]; base = rb["'CO 05 Multiples'!D11:F16"][5][0]; ke_h = rb["'CO 11 SOTP economico'!B36:B43"][6][0]
cem_eq, cel_eq = c12[4], c12[9]
def c0(x): return f"{x:,.0f}".replace(",", ".")
def c4(x): return f"{x:,.4f}".replace(",", "X").replace(".", ",").replace("X", ".")
def pc(x, n=2): return f"{100*x:,.{n}f}".replace(",", "X").replace(".", ",").replace("X", ".") + " %"
old = {"base": 20174, "exp": 19716}
vs = d["valuationSummary"]
vs.update({"base": base, "expected": expv, "marketPrice": 16500, "priceDate": "2026-10-09", "navReference": econ,
  "multiplesWeightedToday": mult, "multiplesWeightedYear3": fy[5], "combinedWeightedToday": base, "combinedWeightedYear3": fy[6], "combinedWeightedYear3PV": fy[7],
  "sectorSotpMultiplesCOP": mult, "primaryValueCOP": base,
  "conclusion": f"Valor base condicionado COP {c0(base)} con SOTP económico {c0(econ)} y sector {c0(mult)} (r2: caja neta Cementos y deuda Celsia al 2T26, minoritarios restados, Ke holding {pc(ke_h)} del corte Colombia, precios 9-oct verificados). Contable 14.733 y FCFF previo 8.294 opcionales. Upside aritmético PF {pc(base/16500-1)}.",
  "sotpScenarios": [{"name": n, "probability": probs[i], "value": vals[i]} for i, n in [(0, "Conservadora"), (1, "Base"), (2, "Optimista"), (3, "Disrupción")]]})
vs["multiplesMethods"][0].update({"today": mult, "year3": fy[5], "year3PV": fy[5] / (1 + ke_h) ** 3, "anchors": [c12[22], mult, None],
  "status": "Cementos peers FY26 5,7067× sobre EBITDA FY26, menos caja neta 2T26 (5,181 billones) y minoritarios a libro (0,642); Celsia 6,475× menos deuda neta 2T26 (4,85) y minoritarios a libro (1,762). Privadas NAV gerente 2025 compartidas."})
for m in vs["independentSectorMethods"]:
    if m["company"] == "Cementos Argos": m.update({"netDebtCOPm": -5181000, "minorityInterestBookCOPm": 641600, "groupEquityCOPm": cem_eq, "netDebtDate": "2026-06-30", "status": "Caja+inversiones CP 8.060.000 − deuda 2.879.000 al 2T26; antes −6.016.768 pronóstico FY26. Minoritarios a libro, no a valor justo."})
    if m["company"] == "Celsia": m.update({"netDebtCOPm": 4850000, "minorityInterestBookCOPm": 1761600, "groupEquityCOPm": cel_eq, "netDebtDate": "2026-06-30", "status": "Deuda neta oficial 2T26; minoritarios a libro restados; JV no verificadas."})
hs = vs["holdingSotp"]; hs["assumptions"].update({"holdingKe": ke_h, "hqTerminalGrowthBase": 0.045, "hqPVCOPm": hq, "rfCOP": 0.11467118776169417, "erpMature": 0.042, "betaHolding": 0.9, "crpColombia": 0.0272018253})
for comp in hs["components"]:
    if comp["name"] == "Cementos Argos": comp["base"] = 7721.554894
    if comp["name"] == "PV corporate overhead": comp.update({"base": -hq / 1000, "method": "annual 2*(106.138849-58.884275)*90% *(1+g)/(Ke 17,97%-g 4,5%)"})
vo = vs["valuationOutput"]; vo.update({"multiplesWeightedBaseCOP": mult, "synchronizedAt": NOW, "year3ExDividendWeightedCOP": fy[6], "year3ExDividendDiscountedCOP": fy[7], "threeYearAssumedDividendsPV": fy[8]})
vo.setdefault("sotpCheck", {})["hybridNAVBaseCOP"] = econ
vo["marketSotpPrimaryCOP"] = econ
d["scenarios"] = [dict(s, value=vals[{"Base": 1, "Conservadora": 0, "Optimista": 2, "Disrupción": 3}[s["name"]]]) for s in d["scenarios"]]
d["assumptions"].update({"riskfreeRate": 0.11467118776169417, "equityRiskPremium": 0.042, "costOfEquity": ke_h, "countryRiskExposure": "CRP Colombia 2,72% (Damodaran jul-2026); Cementos con Centroamérica/Caribe como sensibilidad",
  "damodaranMatureERP": 0.042, "damodaranColombiaCRP": 0.0272018253, "costOfCapitalReferenceDate": "2026-09-25 (TES) / 2026-07 (Damodaran países)", "tesCop10y": 0.13217, "sovereignDefaultSpread": 0.01749881223830583})
d["quote"].update({"quotedAt": "2026-10-09T20:00:00.000Z", "sessionDate": "2026-10-09", "source": "BVC cierre 9-oct-2026 (Yahoo Finance y StockAnalysis)"})
a = d["audit"]; a["checks"].update({"r2CostOfCapitalHarmonizedColombia": True, "r2CementosNetCash2Q26": True, "r2MinorityInterestsDeducted": True, "r2PricesVerifiedTwoSources": True, "r2IndependentPythonReplicaMatchesSheet": True, "minoritiesFairValueCertified": False, "fcffEnginesOnHarmonizedRate": False})
a["warnings"] = [w for w in a["warnings"] if "Ke16%" not in w and "6.017T" not in w] + [
  "r2 10-oct: Ke holding 17,97% (Rf COP 11,47% = TES 13,217% − spread 1,75%; ERP 4,20%; beta 0,90; CRP 2,72%) reemplaza 16% y 14,5% sin sustento; g de gastos HQ 4,5% nominal en vez de 2%.",
  "r2 10-oct: múltiplos sectoriales restan caja/deuda neta al 2T26 y minoritarios a libro (Cementos 0,64; Celsia 1,76 billones). Antes se usaba caja neta FY26 de consenso (6,02 billones) y no se restaban minoritarios.",
  "El DCF FCFF opcional (8.294) sigue con la Rf sintética 8,86% del corte anterior; con el corte Colombia sería menor. Peso 0 en el Base."]
a["lastMathAudit"] = "2026-10-10 r2"
d["updatedAt"] = NOW; d["publication"].update({"revisedAt": NOW, "scope": "PFGRUPOARG_R2_20261010__SOTP60_SECTOR40_DAMODARAN_RATE_NCI_NOT_CERTIFIED"})
d["sources"] += [{"role": "Damodaran · primas país jul-2026", "url": "https://pages.stern.nyu.edu/~adamodar/pc/datasets/ctrypremJuly26.xlsx", "retrievedAt": NOW},
                 {"role": "Damodaran · Cash and cross holdings", "url": "https://aswathdamodaran.blogspot.com/2010/05/cash-and-cross-holdings.html", "retrievedAt": NOW},
                 {"role": "Precios BVC 9-oct (StockAnalysis)", "url": "https://stockanalysis.com/quote/bvc/GRUPOARGOS/history/", "retrievedAt": NOW}]
R = [("ordinaria COP 21.220, preferencial COP 16.500 al cierre marcado 09/10/2026", "ordinaria COP 21.000, preferencial COP 16.500 al cierre del 09/10/2026 (StockAnalysis y Yahoo coinciden)"),
 ("COP **20.011**/acción", f"COP **{c0(econ)}**/acción"),
 ("Bolsa BVC 11.400 × 671.439.556 títulos Grupo = **COP 7,6544 billones**", "Bolsa BVC 11.500 × 671.439.556 títulos Grupo = **COP 7,7216 billones**"),
 ("deuda neta 2026 negativa COP 6.016.768 millones; equity estimado Grupo **COP 7,4830 billones**. Caja excedente y minoritarios de sociedades no certificados: NO tratar el -6,017T completo como caja libre sin estrés.",
  f"caja neta al 30-jun-2026 COP 5.181.000 millones (caja e inversiones CP 8.060.000 − deuda 2.879.000) y minoritarios a libro COP 641.600 millones; equity estimado Grupo **COP {c4(cem_eq/1e6)} billones**. Antes se usaba la caja neta FY26 de consenso (6,017 billones) y no se restaban minoritarios; caja realmente libre sin certificar."),
 ("deuda neta FY26 estimada COP 5.649.737 millones. Equity grupo aprox **COP 3,1271 billones** sin certificar NCI/vehículos JV.",
  f"deuda neta oficial 2T26 COP 4.850.000 millones y minoritarios a libro COP 1.761.600 millones. Equity grupo aprox **COP {c4(cel_eq/1e6)} billones**; minoritarios a valor justo y JV sin certificar."),
 ("VP de gastos HQ hipotéticos COP 607.559m, Ke16%, g2%, recurrencia90%", f"VP de gastos HQ hipotéticos COP {c0(hq/1)}m con Ke holding {pc(ke_h)} (corte Colombia Damodaran), g 4,5% nominal, recurrencia 90%"),
 ("Resultado **COP 20.417 por acción**", f"Resultado **COP {c0(mult)} por acción**"),
 ("| SOTP mixto mercado + gerencial | 20.011 |", f"| SOTP mixto mercado + gerencial | {c0(econ)} |"),
 ("| SOTP EV/EBITDA de peers por filial | 20.417 |", f"| SOTP EV/EBITDA de peers por filial | {c0(mult)} |"),
 ("| **VALOR BASE** | **20.174** |", f"| **VALOR BASE** | **{c0(base)}** |"),
 ("| Conservadora | 25 % | 16.584 |", f"| Conservadora | 25 % | {c0(vals[0])} |"),
 ("| **Base** | **50 %** | **20.174** |", f"| **Base** | **50 %** | **{c0(vals[1])}** |"),
 ("| Optimista | 20 % | 24.820 |", f"| Optimista | 20 % | {c0(vals[2])} |"),
 ("| Disrupción · deterioro fundamental | 5 % | 10.380 |", f"| Disrupción · deterioro fundamental | 5 % | {c0(vals[3])} |"),
 ("| Esperado | 100 % | 19.716 |", f"| Esperado | 100 % | {c0(expv)} |"),
 ("Ke nominal para VP 14,5%. Objetivo ex-dividendo FY+3 **COP 22.766**; descontado al presente **COP 15.166**. Dividendo hipotético COP 750/año por 3 años con VP COP 1.727; paquete VP total **COP 16.893**.",
  f"Ke holding para VP {pc(ke_h)}. Objetivo ex-dividendo FY+3 **COP {c0(fy[6])}**; descontado al presente **COP {c0(fy[7])}**. Dividendo hipotético COP 750/año por 3 años con VP COP {c0(fy[8])}; paquete VP total **COP {c0(fy[9])}**."),
 ("relativo sectorial baja de COP 20.417 a COP **18.949**", f"relativo sectorial baja de COP {c0(mult)} a COP **{c0(c12[22])}**"),
 ("relativo cae aprox COP **19.790**, pero esta prueba MEZCLA fechas", f"relativo cae aprox COP **{c0(c12[20])}** (usa deuda 2T26 y minoritarios)"),
 ("mueve SOTP mixto a **19.592–20.431**", f"mueve SOTP mixto a **{c0(sens11[0][0])}–{c0(sens11[1][0])}**"),
 ("**Base condicional COP 20.174**; frente PF mercado 16.500, potencial aritmético **22,26 %**; frente ordinaria 21.220, **-4,93 %**.",
  f"**Base condicional COP {c0(base)}**; frente PF mercado 16.500, potencial aritmético **{pc(base/16500-1)}**; frente ordinaria 21.000, **{pc(base/21000-1)}**."),
 ("Nuevo Base SOTP+sector **COP 20.174**", f"Nuevo Base SOTP+sector **COP {c0(base)}** (r2)"),
 ("SOTP mixto 20.011 y sector peer 20.417; ponderación 60/40 **20.174** por acción", f"SOTP mixto {c0(econ)} y sector peer {c0(mult)}; ponderación 60/40 **{c0(base)}** por acción"),
 ("Historias: Conservadora 16.584 (25%), Base 20.174 (50%), Optimista 24.820 (20%), Disrupción 10.380 (5%). Valor esperado 19.716. PF 16.500 margen aritmético 22,26 % y ordinaria 21.220 margen -4,93 %.",
  f"Historias: Conservadora {c0(vals[0])} (25%), Base {c0(vals[1])} (50%), Optimista {c0(vals[2])} (20%), Disrupción {c0(vals[3])} (5%). Valor esperado {c0(expv)}. PF 16.500 margen aritmético {pc(base/16500-1)} y ordinaria 21.000 margen {pc(base/21000-1)}."),
 ("FY+3 ex-div COP22.766, presente 15.166", f"FY+3 ex-div COP {c0(fy[6])}, presente {c0(fy[7])}")]
note = (f"\n> **Revisión Damodaran r2 · 10-oct-2026.** Base {c0(old['base'])} → **{c0(base)}**; esperado {c0(old['exp'])} → {c0(expv)}. Cambios: (1) costo del patrimonio de la holding con el mismo corte Colombia que Grupo SURA y Davivienda (Rf COP 11,47% = TES 13,217% − spread 1,75%; ERP 4,20%; beta 0,90; CRP 2,72% → Ke {pc(ke_h)}), en vez de 16% y 14,5% sin sustento; (2) SOTP de múltiplos con caja neta de Cementos y deuda neta de Celsia al 2T26 y resta de minoritarios a libro, como pide Damodaran al pasar de EV a patrimonio; (3) precios del 9-oct verificados en dos fuentes (ordinaria 21.000, CEMARGOS 11.500); (4) gastos de matriz con g 4,5% nominal y la misma convención de VP que SURA. El DCF FCFF opcional sigue con la tasa del corte anterior.\n")
for k in ("valuation", "research"):
    c = d["reports"][k]["content"]
    for a_, b_ in R:
        if a_ in c: c = c.replace(a_, b_)
    i = c.find("**Revisión 10 de octubre de 2026."); j = c.find("\n", i)
    c = c[:j + 1] + note + c[j + 1:]
    d["reports"][k]["content"] = c
missing = [a_[:50] for a_, _ in R if a_ in json.dumps(d["reports"], ensure_ascii=False)]
json.dump(d, open(F, "w"), ensure_ascii=False, indent=1)
print("base", round(base), "exp", round(expv), "econ", round(econ), "mult", round(mult), "pendientes", missing)
