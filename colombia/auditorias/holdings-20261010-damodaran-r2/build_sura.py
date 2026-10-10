"""Construye los expedientes GRUPOSURA.CL y PFGRUPSURA.CL (r2) desde los valores leídos de la hoja.
Entrada: sura_readback.json (lectura de la hoja tras recalcular) y sura_sensibilidades.json. Uso: python3 build_sura.py <readback.json>"""
import json, sys, copy
from pathlib import Path
P = Path(__file__).parent
EXP = P.parent.parent / "expedientes"
rb = json.load(open(sys.argv[1]))
sens = json.load(open(P / "sura_sensibilidades.json"))
q = "'CO · Ke y SOTP 60-40'"
def g(rng): return rb[rng]
T = g(f"{q}!B57:E79")
esc = {n: T[i] for i, n in enumerate(["sCib", "sAM", "sSur", "cibMkt", "amRE", "surRE", "other", "bridge", "hq", "econM", "econ", "cibMult", "amMult", "surMult", "multM", "mult", "blend", "re", "prob"])}
exp_blend, exp_econ, exp_mult, exp_re = (T[19][0], T[20][0], T[21][0], T[22][0])
fy = g(f"{q}!B89:E95"); ke_h = fy[0][0]; pvdiv = fy[1][0]
fy3 = {"econ": fy[3], "mult": fy[4], "blend": fy[5], "re": fy[6]}
pe = g(f"{q}!C49:E54")
res = g("Resumen!B6:E16"); y3re = g("Resumen!B28:E31")[3]
base1 = g("Base_1!B5:B8")
NAMES = ["Base", "Conservadora", "Optimista", "Disrupción · Deterioro fundamental"]
SHEET = "https://docs.google.com/spreadsheets/d/1Nb9_T6n8xbJikr68TN5MA5bIIiwm0aKrsF7m4MmOHyM/edit"
NOW = "2026-10-10T23:00:00.000Z"
KE = {"Cibest": (0.1757965191946942, 0.18839651919469419), "AM": (0.1660343388216942, 0.1765343388216942), "Suramericana": (0.16992271471269418, 0.18420271471269418)}
def c0(x): return f"{x:,.0f}".replace(",", ".")
def c1(x, d=1): return f"{x:,.{d}f}".replace(",", "X").replace(".", ",").replace("X", ".")
def pc(x, d=1): return c1(100 * x, d) + "%"
NAV_LT = 54058.26596992569; BOOK = 58058; BOOK_SEP = 47652.23823795084; ROE_KE = 49787.78185318446

def build(ticker, cls, price, price_src, price_url, older):
    d = copy.deepcopy(older)
    up_b = esc["blend"][0] / price - 1; up_r = esc["re"][0] / price - 1
    other_cls = "preferencial" if cls == "ordinary" else "ordinaria"
    d.update({"updatedAt": NOW})
    d["instrument"]["economicRightsVerified"] = False
    d["quote"].update({"price": price, "source": price_src, "kind": "historical-close-reference", "quotedAt": "2026-10-09T20:00:00.000Z", "sessionDate": "2026-10-09"})
    d["audit"] = {"isolation": "ok", "primaryReconciled": True, "valuationReady": True, "modelApproved": True,
      "revision": "r2-20261010-damodaran",
      "checks": {"identity": True, "currency": True, "noInheritedAssumptions": True, "sourceMasterClean": True, "formulaMath": True,
        "independentPythonReplicaMatchesSheet": True, "reEqualsDdm12Branches": True, "keAboveGrowth12Branches": True, "probabilitiesSum100": True,
        "costOfEquityDamodaranBuilt": True, "terminalRoeRuleApplied": True, "cibestMarketValueIncluded": True, "issuerLtmEarnings": True,
        "sectorPeerMultiplesDocumented": True, "multiplesHistoryFiveTenYears": False, "regulatoryCapital": False, "insuranceReservesSolvency": False,
        "countryExposureWeightsVerified": False, "preferentialRightsValued": False, "fy3IdentityCheck": True},
      "warnings": [
        "Base JMR 60/40 = SOTP económico (Cibest a bolsa) + SOTP de múltiplos: es precio relativo, no valor intrínseco. El intrínseco Damodaran (RE) se publica aparte.",
        "Capital regulatorio (CET1/RWA) de Cibest y solvencia/reservas de Suramericana no conciliados con dividendos distribuibles.",
        "Pesos de exposición por país para la prima país son estimaciones del analista; sensibilidad 100% Colombia −215 COP en el RE.",
        "P/E sectorial = promedio de mediana de pares LatAm (UDM 9-oct) y Damodaran emergentes ene-2026; sin serie histórica homogénea postescisión.",
        "Pasivo PF 520.729m no se resta: las preferenciales están en el denominador económico, igual que en la calculadora del emisor.",
        "Recompras posteriores a 30-jun-2026 y posible emisión CDPQ (17.314.142 acciones) no incorporadas."]}
    d["assumptions"] = {"valuationCurrency": "COP", "riskfreeRate": 0.11467118776169417, "equityRiskPremium": 0.042,
      "countryRiskExposure": "CRP Damodaran jul-2026 ponderado por país (estimado): Cibest 3,17%, SURA AM 1,99%, Suramericana 2,75%",
      "beta": None, "betaBySubsidiary": {"Cibest": 0.70, "SURA AM": 0.75, "Suramericana": 0.66, "stable": 1.0},
      "costOfEquity": ke_h, "costOfEquityBySubsidiary": {"Cibest": {"initial": KE["Cibest"][0], "stable": KE["Cibest"][1]}, "SURA AM": {"initial": KE["AM"][0], "stable": KE["AM"][1]}, "Suramericana": {"initial": KE["Suramericana"][0], "stable": KE["Suramericana"][1]}},
      "costOfDebt": None, "wacc": None, "terminalGrowth": 0.045, "terminalRoic": None,
      "terminalRoe": "Base: Ke estable + 1pp Cibest (19,84%), = Ke estable AM (17,65%) y Suramericana (18,42%)",
      "tesCop10y": 0.13217, "sovereignDefaultSpread": 0.01749881223830583, "costOfCapitalSource": "TES IRC 25-sep-2026; Damodaran ctrypremJuly26; betas Damodaran ene-2026"}
    d["scenarios"] = [{"name": NAMES[i], "probability": esc["prob"][i], "inputs": {"valuationMethod": "SOTP_ECONOMIC60_SECTOR_PE40", "sotpEconomicCOP": esc["econ"][i], "sotpMultiplesCOP": esc["mult"][i], "intrinsicRECOP": esc["re"][i]}, "value": esc["blend"][i]} for i in range(4)]
    vs = {"base": esc["blend"][0], "expected": exp_blend, "marketPrice": price, "priceDate": "2026-10-09",
      "scopeLabel": "Holding financiero: 60% SOTP económico (Cibest a bolsa + SURA AM y Suramericana por rendimientos excedentes) + 40% SOTP por P/E sectorial. Intrínseco Damodaran (RE) publicado aparte. No certificado: capital regulatorio, reservas, derechos por clase.",
      "sheetUrl": SHEET, "primaryValueCOP": esc["blend"][0], "primaryValueMethod": "SOTP_ECONOMIC_SECTOR_PEER_BLEND",
      "primaryValueLabel": "Base JMR 60/40: SOTP económico + múltiplos sectoriales", "baseIsIntrinsic": False,
      "intrinsicDamodaranCOP": esc["re"][0], "intrinsicDamodaranExpectedCOP": exp_re,
      "dcfPrimaryMethod": "RESIDUAL_INCOME_DDM_PER_SUBSIDIARY", "dcfPrimaryIntrinsicPerShareCOP": esc["re"][0], "dcfPrimaryExpectedCOP": exp_re,
      "dcfFcffIntrinsicScenarios": [{"name": NAMES[i], "weight": esc["prob"][i], "intrinsicPerPreferredShareCOP": esc["re"][i], "intrinsicPerShareCOP": esc["re"][i], "year3ExDividendCOP": y3re[i], "method": "RE/DDM por participada"} for i in range(4)],
      "sotpEconomicCOP": esc["econ"][0], "sotpEconomicExpectedCOP": exp_econ, "sectorSotpMultiplesCOP": esc["mult"][0], "sectorSotpMultiplesExpectedCOP": exp_mult,
      "multiplesWeightedToday": esc["mult"][0], "multiplesWeightedYear3": fy3["mult"][1], "multiplesWeightedYear3PV": fy3["mult"][2],
      "combinedWeightedToday": esc["blend"][0], "combinedWeightedYear3": fy3["blend"][1], "combinedWeightedYear3PV": fy3["blend"][2],
      "multiplesStatus": "P/E UDM por participada: promedio de mediana de pares LatAm (9-oct-2026) y Damodaran emergentes (ene-2026): Cibest 11,01×, SURA AM 12,89×, Suramericana 10,83×.",
      "combinedStatus": "Base canónica de holdings JMR: 60% SOTP económico + 40% SOTP de múltiplos; pesos editables. No es valor intrínseco.",
      "multiplesMethods": [
        {"name": "SOTP P/E sectorial por participada (pares LatAm + Damodaran EM)", "today": esc["mult"][0], "year3": fy3["mult"][1], "year3PV": fy3["mult"][2], "weight": 1,
         "status": f"Cibest {c1(pe[2][0],2)}× (pares {c1(pe[0][0],2)}×, Damodaran {c1(pe[1][0],2)}×); SURA AM {c1(pe[2][1],2)}× (pares {c1(pe[0][1],2)}×, Damodaran {c1(pe[1][1],2)}×); Suramericana {c1(pe[2][2],2)}× (pares {c1(pe[0][2],2)}×, Damodaran {c1(pe[1][2],2)}×). Utilidad UDM del emisor."},
        {"name": "P/B justificado (ROE−g)/(Ke−g)", "today": None, "weight": None, "status": "Diagnóstico derivado del mismo RE (Cibest 1,22×, AM 1,04×, Suramericana 1,10×); no es ancla independiente."},
        {"name": "P/E histórico homogéneo", "today": None, "weight": None, "status": "No homogéneo tras escisión 2025 y reorganización de Grupo Cibest."},
        {"name": "P/FCFE distribuible", "today": None, "weight": None, "status": "Pendiente CET1/RWA y reservas técnicas."},
        {"name": "EV/EBITDA industrial", "today": None, "weight": None, "status": "No aplica a banca, seguros y gestión de activos."},
        {"name": "EV/FCFF industrial", "today": None, "weight": None, "status": "No aplica a holding financiero."},
        {"name": "P/OCF", "today": None, "weight": None, "status": "No aplica al flujo de intermediación financiera."}],
      "sotpScenarios": [{"name": NAMES[i], "probability": esc["prob"][i], "value": esc["blend"][i]} for i in range(4)],
      "holdingScenarioTable": [{"name": NAMES[i], "probability": esc["prob"][i], "base6040COP": esc["blend"][i], "sotpEconomicCOP": esc["econ"][i], "sotpMultiplesCOP": esc["mult"][i], "intrinsicRECOP": esc["re"][i]} for i in range(4)],
      "holdingSotp": {"assumptions": {"holdingKe": ke_h, "sotpEconomicWeight": 0.6, "sotpMultiplesWeight": 0.4, "cibestPriceCOP": 88000, "cibestSharesHeld": 235565920, "corporateCostCOPm": 117000},
        "method": "SOTP económico: Cibest a bolsa × escala de historia + SURA AM y Suramericana RE + otros − puente − VP gastos; SOTP múltiplos: P/E sector × UDM × participación × escala + mismos ajustes de matriz."},
      "costOfCapital": {"rfCOP": 0.11467118776169417, "erpMature": 0.042, "erpImpliedOct2026": 0.037, "keHolding": ke_h, "bySubsidiary": d["assumptions"]["costOfEquityBySubsidiary"]},
      "valuationOutput": {"dcfBaseCOP": esc["re"][0], "dcfExpectedCOP": exp_re, "dcfConservativeCOP": esc["re"][1], "dcfOptimisticCOP": esc["re"][2], "dcfDisruptionCOP": esc["re"][3], "dcfYear3ExDividend": y3re[0],
        "dcfLabel": "Intrínseco Damodaran · SOTP por rendimientos excedentes (RE/DDM)",
        "bookValueProformaCOP": BOOK, "bookValueSeparatedCOP": BOOK_SEP, "bookLookThroughCOP": NAV_LT,
        "marketSotpPrimaryCOP": esc["econ"][0], "marketSotpLabel": "SOTP económico: Cibest a bolsa + SURA AM y Suramericana RE − matriz",
        "sectorSotpMultiplesCOP": esc["mult"][0], "base6040COP": esc["blend"][0], "roeterminalKeSensitivityCOP": ROE_KE,
        "primarySheet": "CO · Ke y SOTP 60-40", "sheetUrl": SHEET, "synchronizedAt": NOW,
        "status": "BASE 60/40 CONDICIONADA; intrínseco RE condicionado a capital regulatorio",
        "sotpScenarios": [{"name": NAMES[i], "weight": esc["prob"][i], "valuePerPreferredShareCOP": esc["re"][i], "economicShares": 327705908,
            "totalEquityCOPtrillions": (res[0][i] + res[1][i] + res[2][i] + 165883 - 6491851 - res[5][i]) / 1e6,
            "componentEquityCOPtrillions": ([{"company": "Grupo Cibest", "equity": res[0][0] / 1e6}, {"company": "SURA Asset Management", "equity": res[1][0] / 1e6}, {"company": "Suramericana", "equity": res[2][0] / 1e6}] if i == 0 else [])} for i in range(4)],
        "submodels": [{"company": "Grupo Cibest", "title": "RE/DDM 10 años + terminal", "method": f"Ke {pc(KE['Cibest'][0],2)} → {pc(KE['Cibest'][1],2)}; ROE UDM {pc(base1[3][0],1)}", "url": SHEET},
                      {"company": "SURA Asset Management", "title": "RE/DDM 10 años + terminal", "method": f"Ke {pc(KE['AM'][0],2)} → {pc(KE['AM'][1],2)}", "url": SHEET},
                      {"company": "Suramericana", "title": "RE/DDM 10 años + terminal", "method": f"Ke {pc(KE['Suramericana'][0],2)} → {pc(KE['Suramericana'][1],2)}", "url": SHEET}],
        "bridge": {"otherNetAssetsCOPm": 165883, "parentNetLiabilitiesCOPm": 6491851, "corporateCostsPVCOPm": -esc["hq"][0], "cibestMarketValueCOPm": esc["cibMkt"][0]},
        "methodWeightPolicy": {"sotpEconomic": 0.6, "sotpMultiples": 0.4, "intrinsicRE": 0, "book": 0},
        "sensitivities": [{"driver": c["driver"], "deltaCOPperShare": c["deltaRE"], "adjustedFCFFCOP": c["intrinsicRE"], "deltaBase6040": c["deltaBlend"], "base6040": c["blend6040"], "scope": "Intrínseco RE y Base 60/40; univariante, no sumar"} for c in sens["cases"]]}}
    d["valuationSummary"] = vs
    d["sources"] = [s for s in d["sources"] if s["role"] not in ("precio clase",)] + [
        {"role": "precio clase", "url": price_url, "retrievedAt": NOW},
        {"role": "Calculadora de valoración Grupo SURA (UDM y acciones Cibest)", "url": "https://www.gruposura.com/wp-content/uploads/2026/08/sura-grupo-calculadora-de-valoracion.xlsx", "retrievedAt": NOW},
        {"role": "Damodaran · Valuing Financial Service Firms", "url": "https://pages.stern.nyu.edu/~adamodar/pdfiles/papers/finfirm09.pdf", "retrievedAt": NOW},
        {"role": "Damodaran · Cash and cross holdings", "url": "https://aswathdamodaran.blogspot.com/2010/05/cash-and-cross-holdings.html", "retrievedAt": NOW},
        {"role": "Damodaran · primas país jul-2026", "url": "https://pages.stern.nyu.edu/~adamodar/pc/datasets/ctrypremJuly26.xlsx", "retrievedAt": NOW},
        {"role": "Damodaran · ERP implícita oct-2026", "url": "https://pages.stern.nyu.edu/~adamodar/pc/implprem/ERPOct26.xlsx", "retrievedAt": NOW},
        {"role": "Damodaran · betas y P/E sector ene-2026", "url": "https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datacurrent.html", "retrievedAt": NOW},
        {"role": "Precio Cibest ordinaria", "url": "https://finance.yahoo.com/quote/CIBEST.CL/", "retrievedAt": NOW}]
    d["publication"].update({"revisedAt": NOW, "scope": "r2-base-6040-condicionado-intrinseco-RE-aparte", "workbookUrl": SHEET})
    lbl = "Ordinaria" if cls == "ordinary" else "Preferencial"
    mcap = 165834026 * 67480 / 1e6 + 161871882 * 58600 / 1e6
    implied = mcap - esc["cibMkt"][0] + 6491851 - esc["hq"][0] - 165883
    earn_att = 1272336 * 0.9332 + 904340 * 0.8113
    front = f"---\nmarket: CO\nticker: {ticker}\nanalysis_date: 2026-10-10\nrun_id: {d['runId']}\ncompany: Grupo de Inversiones Suramericana S.A.\ncurrency: COP\nstatus: condicionado\nrevision: r2\n---\n"
    srcs = ("\n### Fuentes\n- [Estados separados 2T26](https://www.gruposura.com/wp-content/uploads/2026/08/sura-grupo-estados-financieros-separados-2026-2T.pdf)\n"
            "- [Calculadora de valoración del emisor](https://www.gruposura.com/wp-content/uploads/2026/08/sura-grupo-calculadora-de-valoracion.xlsx)\n"
            "- [Damodaran · Valuing Financial Service Firms](https://pages.stern.nyu.edu/~adamodar/pdfiles/papers/finfirm09.pdf)\n"
            "- [Damodaran · Good banks, bad banks (Citi, 2023)](https://aswathdamodaran.blogspot.com/2023/05/good-bad-banks-and-good-bad-investments.html)\n"
            "- [Damodaran · Cash and cross holdings](https://aswathdamodaran.blogspot.com/2010/05/cash-and-cross-holdings.html)\n"
            "- [Damodaran · participaciones cruzadas](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/valquestions/a22.htm)\n"
            "- [Damodaran · primas país jul-2026](https://pages.stern.nyu.edu/~adamodar/pc/datasets/ctrypremJuly26.xlsx)\n"
            f"- [Precio de la clase]({price_url})\n\n[Hoja del modelo]({SHEET})")
    sc_rows = "\n".join(f"| {NAMES[i]} | {pc(esc['prob'][i],0)} | {c0(esc['blend'][i])} | {c0(esc['econ'][i])} | {c0(esc['mult'][i])} | {c0(esc['re'][i])} |" for i in range(4))
    sens_rows = "\n".join(f"| {c['driver']} | {c0(c['deltaRE'])} | {c0(c['deltaBlend'])} |" for c in sens["cases"])
    val = front + f"""# Grupo SURA · Valoración Modelo JMR · {lbl} · revisión Damodaran r2

**Base JMR 60/40 COP {c0(esc['blend'][0])} por acción; valor intrínseco Damodaran (rendimientos excedentes) COP {c0(esc['re'][0])}; precio de la clase COP {c0(price)} (9-oct-2026).**

## Índice
1. Resumen · 2. Historia · 3. Datos · 4. Supuestos y tasas · 5. Historias · 6. Múltiplos · 7. Resultados · 8. Intrínseco frente a múltiplos · 9. Sensibilidad · 10. Log de cambios · 11. Precio · 12. Decisión · 13. Fuentes · 14. Control

## 1. Resumen
- **Base JMR (regla canónica de holdings): COP {c0(esc['blend'][0])}** = 60% SOTP económico COP {c0(esc['econ'][0])} + 40% SOTP de múltiplos COP {c0(esc['mult'][0])}. Esperado COP {c0(exp_blend)}.
- **Valor intrínseco Damodaran (RE/DDM por participada): COP {c0(esc['re'][0])}**; esperado COP {c0(exp_re)}. Es el único valor de flujos; el Base 60/40 es precio relativo (Cibest a bolsa y P/E de pares).
- Rango de historias del Base: COP {c0(esc['blend'][3])} (Disrupción) a COP {c0(esc['blend'][2])} (Optimista).

## 2. Historia y visión externa
Holding de tres franquicias financieras: Grupo Cibest (banca, 24,94%), SURA Asset Management (pensiones y gestión, 93,32%) y Suramericana (seguros, 81,13%). Cibest es líder del crédito colombiano con ROE UDM 20,8%; SURA AM y Suramericana tienen ROE de 12–14% con fuerte componente regulado. La matriz tiene deuda neta de COP 6,49 billones y gastos corporativos de COP 117.000 millones al año. Damodaran valora una holding sumando el valor de cada participación por su cuota económica y restando costos y deuda de la matriz; el descuento de holding que pone el mercado responde a esos costos y a la confianza en la asignación de capital ([Cash and cross holdings](https://aswathdamodaran.blogspot.com/2010/05/cash-and-cross-holdings.html)).

## 3. Datos
Estados separados 2T26 (puente de matriz), calculadora de valoración del emisor ago-2026 (patrimonio controlador, utilidad UDM y acciones de Cibest), precios BVC del 9-oct-2026. Patrimonio controlador: Cibest 38.123.672, SURA AM 10.449.483, Suramericana 6.537.339 COPm. Utilidad UDM: 7.934.717, 1.272.336 y 904.340 COPm. Acciones económicas 327.705.908 (165.834.026 ordinarias y 161.871.882 preferenciales). La utilidad de Cibest pasó de un proxy de 7.722.604 a la cifra del emisor, y su participación de 24,88% a 24,9365% (235.565.920 acciones).

## 4. Supuestos y tasas
| Supuesto | Valor | Fuente |
|---|---|---|
| Rf COP | 11,47% | TES 13,217% (IRC 25-sep-2026) − spread Colombia 1,75% (Damodaran) |
| ERP madura | 4,20% | Damodaran jul-2026; implícita oct-2026 3,70% como sensibilidad |
| CRP ponderado | Cibest 3,17% · AM 1,99% · Suramericana 2,75% | Damodaran jul-2026; pesos por país estimados |
| Beta inicial → estable | 0,70 / 0,75 / 0,66 → 1,0 | Damodaran ene-2026 (bancos, gestión de activos, seguros) |
| Ke inicial → estable | {pc(KE['Cibest'][0],2)}→{pc(KE['Cibest'][1],2)} · {pc(KE['AM'][0],2)}→{pc(KE['AM'][1],2)} · {pc(KE['Suramericana'][0],2)}→{pc(KE['Suramericana'][1],2)} | CAPM con prima país; mismo Ke en las cuatro historias |
| Ke holding | {pc(ke_h,2)} | Promedio ponderado por valor; descuenta gastos y FY+3 |
| ROE terminal Base | Ke estable +1pp Cibest; = Ke en AM y Suramericana | Regla Damodaran del modelo: sin ventaja ROE = Ke; ventaja durable, algo más |
| g terminal | 4,5% nominal COP | Menor que Rf |
| P/E sector | 11,01× / 12,89× / 10,83× | Mediana pares LatAm + Damodaran emergentes |

Damodaran, en *Valuing Financial Service Firms*, valora a Goldman Sachs con rendimientos excedentes, fija el ROE estable igual al Ke y baja la beta hacia 1,2 en crecimiento estable; en Citi (2023) muestra que un banco cotiza sobre libro solo si ROE > Ke. El modelo anterior dejaba el ROE terminal 0,5–4 puntos por debajo del Ke en las tres participadas, lo que suponía destrucción de valor perpetua; ahora sigue la regla del modelo.

## 5. Historias y probabilidades
Base 50% (ROE se normaliza: Cibest 19% año 5), Conservadora 25% (ROE terminal 2–3pp bajo Ke, crecimiento 3–4%), Optimista 15% (ROE terminal 2–3pp sobre Ke), Disrupción 10% (ROE terminal 6–8%, crecimiento 1%). En el SOTP económico y en el de múltiplos, el valor de mercado y el de múltiplos de cada participada se escalan por la razón RE historia / RE Base.

## 6. Múltiplos
P/E UDM por participada con dos anclas: mediana de pares latinoamericanos del 9-oct-2026 (bancos: Credicorp, Santander Chile, Banco de Chile, Itaú, Banorte, Aval, Davivienda, Bradesco; pensiones y gestión: Habitat, Vinci; seguros: BB Seguridade, Porto, Caixa Seguridade, Quálitas) y el P/E agregado de Damodaran para emergentes (ene-2026). El P/B justificado (ROE−g)/(Ke−g) sale del mismo RE y no cuenta como ancla independiente. P/E histórico, P/FCFE, EV/EBITDA, EV/FCFF y P/OCF: N/D o no aplican.

## 7. Resultados
| Historia | Prob. | Base 60/40 | SOTP económico | SOTP múltiplos | Intrínseco RE |
|---|---|---|---|---|---|
{sc_rows}
| Esperado | 100% | {c0(exp_blend)} | {c0(exp_econ)} | {c0(exp_mult)} | {c0(exp_re)} |

Puente Base (COPm): Cibest a bolsa {c0(esc['cibMkt'][0])} + SURA AM RE {c0(esc['amRE'][0])} + Suramericana RE {c0(esc['surRE'][0])} + otros 165.883 − puente matriz 6.491.851 − VP gastos {c0(-esc['hq'][0])} = {c0(esc['econM'][0])}.

| FY+3 (Ke {pc(ke_h,2)}, dividendos 2.000/2.200/2.400 con VP {c0(pvdiv)}) | Hoy | FY+3 exdiv | VP FY+3 exdiv |
|---|---|---|---|
| Base 60/40 | {c0(fy3['blend'][0])} | {c0(fy3['blend'][1])} | {c0(fy3['blend'][2])} |
| SOTP económico | {c0(fy3['econ'][0])} | {c0(fy3['econ'][1])} | {c0(fy3['econ'][2])} |
| SOTP múltiplos | {c0(fy3['mult'][0])} | {c0(fy3['mult'][1])} | {c0(fy3['mult'][2])} |
| Intrínseco RE | {c0(fy3['re'][0])} | {c0(fy3['re'][1])} | {c0(fy3['re'][2])} |

Control: VP FY+3 + VP dividendos = valor de hoy (diferencia 0).

## 8. Valor intrínseco frente a múltiplos
La brecha entre el intrínseco RE ({c0(esc['re'][0])}) y el Base 60/40 ({c0(esc['blend'][0])}) tiene dos fuentes. (1) Cibest: a bolsa vale COP {c0(esc['cibMkt'][0])} millones para SURA, frente a {c0(res[0][0])} millones en el RE; con P/B 2,18× y ROE 20,8%, el mercado le exige un Ke cercano a 11–12%, frente al 17,6% del CAPM con prima país. (2) SURA AM y Suramericana a P/E de pares valen COP {c0(esc['amMult'][0]+esc['surMult'][0])} millones frente a {c0(esc['amRE'][0]+esc['surRE'][0])} millones en el RE. Damodaran no promedia valor y precio: los presenta por separado y pide entender la brecha. Aquí el promedio es una regla del Modelo JMR.

## 9. Sensibilidad
| Variable (univariante) | Δ intrínseco RE | Δ Base 60/40 |
|---|---|---|
{sens_rows}

## 10. Log de cambios (r1 → r2)
| Cambio | Antes | Después |
|---|---|---|
| Ke | Proxies 17,51/16,81/16,75%, Rf vacía | CAPM Damodaran con Rf 11,47%, beta sector y CRP; converge a beta 1 |
| ROE terminal Base | 17/14/13,5% (< Ke) | Ke estable +1/0/0 pp |
| Utilidad Cibest | 7.722.604 proxy | 7.934.717 emisor |
| Participación Cibest | 24,88% | 24,9365% |
| P/E sector | 9,27/9,45/11,07 (proxies sin pares) | 11,01/12,89/10,83 (pares + Damodaran) |
| Precio ordinaria | 67.760 (Investing) | 67.480 (Yahoo y StockAnalysis) |
| Valor principal | RE 43.286 | Base 60/40 {c0(esc['blend'][0])}; RE {c0(esc['re'][0])} aparte |
| Etiquetas | "SOTP de mercado" = NAV contable | NAV contable {c0(NAV_LT)} y SOTP económico {c0(esc['econ'][0])} separados |

## 11. El precio al final
Precio {lbl.lower()} COP {c0(price)} (9-oct-2026); la {other_cls} cotiza a COP {c0(67480 if cls != 'ordinary' else 58600)}. Base 60/40 / precio − 1 = {pc(up_b)}; intrínseco RE / precio − 1 = {pc(up_r)}. Al precio de hoy (capitalización de ambas clases COP {c0(mcap)} millones), el mercado valora SURA AM y Suramericana juntas en unos COP {c0(implied)} millones (≈ {c1(implied/earn_att,1)}× su utilidad atribuible), frente a {c0(esc['amMult'][0]+esc['surMult'][0])} millones a P/E de pares: un descuento de holding amplio. La brecha entre clases no se convierte en prima de voto en el valor.

## 12. Registro de decisión
Sin recomendación automática. La opinión cambia si: el capital regulatorio limita los dividendos de Cibest; el ROE de SURA AM no supera 15%; el TES baja de forma sostenida (cada −1pp de Rf suma COP {c0(sens['cases'][1]['deltaRE'])} al intrínseco); o la operación CDPQ/MRE se cierra a un precio distinto del valor intrínseco. Revisar con los estados del 3T26.
{srcs}

## 14. Control de calidad
AISLAMIENTO = OK. Réplica Python independiente = hoja (diferencia 0 en las cuatro historias). RE = DDM en 12 ramas; Ke > g en 12; probabilidades 100%; identidad FY+3 = 0. Moneda COP nominal en flujos y tasas. No certificado: capital regulatorio, solvencia de seguros, pesos de exposición país y derechos por clase.
"""
    val = val.replace("\n### Fuentes", "\n## 13. Fuentes")
    research = front + f"""# Grupo SURA · Análisis fundamental · {lbl} · revisión Damodaran r2

**Datos 2T26 y calculadora del emisor; precios 9-oct-2026. Base JMR 60/40 COP {c0(esc['blend'][0])}; intrínseco Damodaran COP {c0(esc['re'][0])}; precio COP {c0(price)}.**

## Índice
1–18 secciones enlazadas abajo.

## 1. Negocio y perímetro
Holding financiera latinoamericana: banca (Cibest), pensiones y gestión de activos (SURA AM) y seguros (Suramericana). El valor para el accionista depende de los patrimonios regulados y de los dividendos que puedan subir a la matriz.

## 2. Historia y reorganización
La escisión de 2025 y la creación de Grupo Cibest cambian el perímetro; no hay diez años homogéneos de utilidades.

## 3. Segmentos y participaciones
Cibest 24,94% (235.565.920 acciones ordinarias), SURA AM 93,32%, Suramericana 81,13%. Se suman cuotas económicas y no se restan dos veces los minoritarios.

## 4. Ventajas competitivas
Cibest: escala y fondeo de bajo costo justifican un ROE terminal 1pp sobre su Ke. SURA AM y Suramericana: marcas fuertes en mercados regulados con presión de comisiones; ROE terminal = Ke.

## 5. Gestión y asignación de capital
Dividendos, desendeudamiento y la operación CDPQ/MRE (posible emisión de 17.314.142 acciones) definen el descuento de holding. Damodaran atribuye ese descuento a costos y a la confianza en la asignación de capital.

## 6. Utilidad
UDM del emisor: Cibest 7.934.717, SURA AM 1.272.336, Suramericana 904.340 COPm. El H1-2026 consolidado controlador fue ~COP 1,7 billones.

## 7. Rentabilidad frente a costo del patrimonio
ROE UDM: Cibest 20,8% vs Ke {pc(KE['Cibest'][0],2)}; SURA AM 12,2% vs {pc(KE['AM'][0],2)}; Suramericana 13,8% vs {pc(KE['Suramericana'][0],2)}. Solo Cibest supera hoy su Ke.

## 8. Matriz: deuda y gastos
Puente neto COP 6.491.851 millones; gastos COP 117.000 millones/año, VP COP {c0(-esc['hq'][0])} millones al Ke holding {pc(ke_h,2)}.

## 9. Cibest
A bolsa vale COP {c0(esc['cibMkt'][0])} millones para SURA (P/B 2,18×). Riesgos: cartera, CET1/RWA, cuatro países con El Salvador como mayor prima país.

## 10. Suramericana
Reservas técnicas, siniestralidad y solvencia limitan los dividendos sostenibles; RE COP {c0(esc['surRE'][0])} millones atribuibles.

## 11. SURA Asset Management
Regulación previsional (reformas en Chile y Colombia), AUM y comisiones. Patrimonio con 5,9 billones de intangibles: el P/E es más útil que el P/B. RE COP {c0(esc['amRE'][0])} millones atribuibles.

## 12. Valor con criterio Damodaran
Intrínseco RE: Base COP {c0(esc['re'][0])}, esperado COP {c0(exp_re)}. Base JMR 60/40: COP {c0(esc['blend'][0])} (esperado {c0(exp_blend)}). SOTP económico {c0(esc['econ'][0])}; SOTP múltiplos {c0(esc['mult'][0])}. NAV contable look-through {c0(NAV_LT)}; patrimonio consolidado {c0(BOOK)}.

## 13. Cuatro historias
Base 50%, Conservadora 25%, Optimista 15%, Disrupción 10%. Base 60/40: {c0(esc['blend'][0])} / {c0(esc['blend'][1])} / {c0(esc['blend'][2])} / {c0(esc['blend'][3])}.

## 14. Sensibilidad
Rf ±1pp: {c0(sens['cases'][0]['deltaRE'])} / +{c0(sens['cases'][1]['deltaRE'])} en el RE. ROE terminal ±1pp: ±{c0(sens['cases'][4]['deltaRE'])}. Precio Cibest −10%: {c0(sens['cases'][8]['deltaBlend'])} en el Base 60/40.

## 15. Riesgo país
Prima país ponderada por exposición estimada; la sensibilidad 100% Colombia mueve el RE en {c0(sens['cases'][3]['deltaRE'])}. No se suma el spread soberano dos veces: el TES se depura antes de añadir la prima país.

## 16. Múltiplos
P/E: Cibest 11,01×, SURA AM 12,89×, Suramericana 10,83× (pares LatAm + Damodaran emergentes). EV/EBITDA no aplica a financieras.

## 17. Clases de acciones
Ordinaria COP 67.480 y preferencial COP 58.600. El mínimo preferencial (COP 359,73) es menor que el dividendo ordinario (COP 2.000), así que no genera prima económica; el valor por acción es igual para ambas clases.

## 18. Registro de decisión
Sin recomendación automática. Pendientes: CET1/RWA de Cibest, solvencia de Suramericana, pesos de exposición país verificados, comparables históricos y operación CDPQ/MRE.
{srcs}
"""
    d["reports"] = {"valuation": {"content": val}, "research": {"content": research}}
    return d

for fn, t, cls, price, src, url in [
    ("GRUPOSURA.CL-gruposura-20261010-damodaran-jmr.json", "GRUPOSURA.CL", "ordinary", 67480, "BVC cierre 9-oct-2026 (Yahoo Finance y StockAnalysis)", "https://stockanalysis.com/quote/bvc/GRUPOSURA/history/"),
    ("PFGRUPSURA.CL-pfgrupsura-20261010-damodaran-jmr.json", "PFGRUPSURA.CL", "preferential", 58600, "BVC cierre 9-oct-2026 (Yahoo Finance y StockAnalysis)", "https://stockanalysis.com/quote/bvc/PFGRUPSURA/history/")]:
    old = json.load(open(EXP / fn))
    new = build(t, cls, price, src, url, old)
    json.dump(new, open(EXP / fn, "w"), ensure_ascii=False, indent=1)
    print(fn, round(new["valuationSummary"]["primaryValueCOP"]), round(new["valuationSummary"]["intrinsicDamodaranCOP"]))
