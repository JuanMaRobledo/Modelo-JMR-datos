"""r4 Argos: Odinsa y Pactia al 30-jun-2026, caja libre de Cementos, minoritarios a valor justo (libro × P/B), WACC de motores secundarios. Lee argos_readback.json."""
import json, re, sys
from pathlib import Path
F = Path(__file__).parent.parent.parent / "expedientes" / "PFGRUPOARG.CL-pfgrupoarg-20261009-clean-master.json"
rb = json.load(open(sys.argv[1])); d = json.load(open(F)); vs = d["valuationSummary"]; vo = vs["valuationOutput"]
NOW = "2026-10-11T00:30:00.000Z"
c11 = rb["'CO 11 SOTP economico'!A4:G16"]; econ = c11[12][6]; hq = -c11[10][6]
odinsa, pactia = c11[2][6], c11[5][6]
s11 = [r[0] for r in rb["'CO 11 SOTP economico'!G25:G29"]]
c12 = [r[0] for r in rb["'CO 12 Comparables sector'!B18:B40"]]; mult = c12[16]; cem_eq, cel_eq = c12[4], c12[9]
fy = [r[0] for r in rb["'CO 12 Comparables sector'!B44:B54"]]
sc = rb["'CO 03 Escenarios'!G12:J15"]; vals = sc[1]; probs = sc[2]; expv = sc[3][0]
base = rb["'CO 05 Multiples'!D11:F16"][5][0]
DCF = {"Base": 6880.522297, "Conservadora": 2238.6085, "Optimista": 12707.7178, "Disrupción": 0.0}; DCFEXP = 6541.4568
def c0(x): return f"{x:,.0f}".replace(",", ".")
def c4(x): return f"{x:,.4f}".replace(",", "X").replace(".", ",").replace("X", ".")
def pc(x, n=2): return f"{100*x:,.{n}f}".replace(",", "X").replace(".", ",").replace("X", ".") + " %"
vs.update({"base": base, "expected": expv, "navReference": econ, "primaryValueCOP": base, "combinedWeightedToday": base,
  "multiplesWeightedToday": mult, "sectorSotpMultiplesCOP": mult, "multiplesWeightedYear3": fy[5], "combinedWeightedYear3": fy[6], "combinedWeightedYear3PV": fy[7],
  "dcfPrimaryIntrinsicPerShareCOP": DCF["Base"], "dcfPrimaryExpectedCOP": DCFEXP,
  "sotpScenarios": [{"name": n, "probability": probs[i], "value": vals[i]} for i, n in enumerate(["Conservadora", "Base", "Optimista", "Disrupción"])],
  "conclusion": f"Valor base condicionado COP {c0(base)} = 60% SOTP económico {c0(econ)} + 40% múltiplos sectoriales {c0(mult)} (r4: Odinsa y Pactia al 30-jun-2026, caja libre de Cementos, minoritarios a valor justo). Contable 14.733 y DCF FCFF {c0(DCF['Base'])} opcionales. Potencial aritmético PF {pc(base/16500-1)}."})
vs["multiplesMethods"][0].update({"today": mult, "year3": fy[5], "anchors": [c12[22], mult, None],
  "status": "Cementos 5,7067× EBITDA FY26 − (−caja libre 2T26 4,914 billones) − minoritarios × P/B 1,536; Celsia 6,475× − deuda 2T26 4,85 − minoritarios × P/B 1,586. Odinsa y Pactia al 30-jun-2026 compartidos con el SOTP económico."})
for m in vs["independentSectorMethods"]:
    if m["company"] == "Cementos Argos": m.update({"netDebtCOPm": -4914000, "minorityInterestFairValueCOPm": 641600 * 1.5359, "groupEquityCOPm": cem_eq, "status": "Caja libre 7.793.000 (caja+inv. CP − restringida 5.000 − dividendo pendiente 262.000) − deuda 2.879.000; minoritarios a valor justo = libro × P/B 1,536"})
    if m["company"] == "Celsia": m.update({"minorityInterestFairValueCOPm": 1761600 * 1.5856, "groupEquityCOPm": cel_eq, "status": "Deuda neta oficial 2T26; minoritarios a valor justo = libro × P/B 1,586"})
for p in vs["privateHoldingNAV"]:
    if p["company"] == "Odinsa": p.update({"totalEquityNavCOPm": odinsa / 0.9499, "groupAttributableCOPm": odinsa, "asOf": "2026-06-30", "navRangeCOPm": [2400000, 3000000],
        "status": "Libro 2T26 (FCP Odinsa a valor razonable por expertos independientes, 1.274.152) + Quiport a precio de transacción USD 81,5 MM (+109.632) + gestor DCF 76.400; NAV gerencia dic-2025 2,4–3,0 billones solo como sensibilidad",
        "source": "https://files.grupoargos.com/uploads-grupo-argos/2026/08/Circular-Externa-012-2T2026.pdf"})
    if p["company"].startswith("Pactia"): p.update({"groupAttributableCOPm": pactia, "asOf": "2026-06-30", "status": "62.213.152 unidades × COP 17.128,50 (valor de unidad 30-jun-2026, emisor)", "source": "https://files.grupoargos.com/uploads-grupo-argos/2026/08/004.01.-Reporte-Resultados-Trimestrales-2Q2026.pdf"})
vs["newModelStress"] = {"cementNetCashAvailable70PctRelativeCOP": c12[22], "celsiaLTM2Q2026RelativeCOP": c12[20], "odinsaNavLowCOP": s11[0], "odinsaNavHighCOP": s11[1]}
vo.update({"dcfBaseCOP": DCF["Base"], "dcfConservativeCOP": DCF["Conservadora"], "dcfOptimisticCOP": DCF["Optimista"], "dcfDisruptionCOP": 0, "dcfExpectedCOP": DCFEXP,
  "priceToDCF": 16500 / DCF["Base"], "multiplesWeightedBaseCOP": mult, "marketSotpPrimaryCOP": econ, "synchronizedAt": NOW, "dcf60Multiples40COP": 0.6 * DCF["Base"] + 0.4 * mult,
  "year3ExDividendWeightedCOP": fy[6], "year3ExDividendDiscountedCOP": fy[7], "threeYearAssumedDividendsPV": fy[8]})
vo.setdefault("sotpCheck", {}).update({"hybridNAVBaseCOP": econ, "dcfBaseCOP": DCF["Base"]})
for s in vs["dcfFcffIntrinsicScenarios"]:
    k = "Disrupción" if s["name"].startswith("Disrup") else s["name"]
    s["intrinsicPerPreferredShareCOP"] = DCF[k]; s["upsideVsPF"] = DCF[k] / 16500 - 1
for m in vs.get("methodSelectionDefault", {}).get("methods", []):
    if m["id"] == "dcf": m["valueCOP"] = DCF["Base"]
    if m["id"] == "market_sotp": m["valueCOP"] = econ
d["scenarios"] = [dict(s, value=vals[{"Conservadora": 0, "Base": 1, "Optimista": 2, "Disrupción": 3}[s["name"]]]) for s in d["scenarios"]]
a = d["audit"]; a["checks"].update({"minoritiesFairValueCertified": False, "minoritiesFairValueMarketPB": True, "odinsaNAVOct2026Reconciled": False, "odinsaValue2Q26DatedSources": True,
  "pactiaNAVJun2026IssuerUnitValue": True, "cementCashAvailableCertified": False, "cementFreeCashFromNotes2Q26": True, "secondaryEnginesWaccDamodaran": True, "sameWaccAcrossStories": True})
a["warnings"] = [w for w in a["warnings"] if not w.startswith(("NAV Odinsa 2,4", "Pactia Colliers", "r3: DCF FCFF"))] + [
  "r4: Odinsa al 30-jun-2026 (libro con FCP a valor razonable + Quiport a precio de transacción 2023 + gestor DCF) = COP 1,967 billones atribuibles (antes 2,565 con NAV gerencia dic-2025, ahora sensibilidad).",
  "r4: Pactia al valor de unidad del 30-jun-2026 (COP 17.128,50 × 62.213.152 unidades) = COP 1,066 billones.",
  "r4: caja libre de Cementos 7,793 billones (restringida solo COP 5 mil MM; se resta el dividendo pendiente de 262 mil MM); minoritarios a valor justo = libro × P/B de mercado (Damodaran).",
  "r4: motores secundarios con WACC Damodaran del corte Colombia y la misma tasa en las cuatro historias: Growth 13,22%, concesiones 13,40%, Pactia fondo 15,36%, gestores 16,56%, NDU 14,10%, HQ 17,97%. DCF FCFF Base 6.881 (peso 0)."]
d["updatedAt"] = NOW; d["publication"]["revisedAt"] = NOW; d["publication"]["scope"] = "PFGRUPOARG_R4_20261010__SOTP60_SECTOR40_DATED_2Q26_NOT_CERTIFIED"
d["sources"] += [{"role": "EEFF consolidados Grupo Argos 2T26 (Circular 012)", "url": "https://files.grupoargos.com/uploads-grupo-argos/2026/08/Circular-Externa-012-2T2026.pdf", "retrievedAt": NOW},
  {"role": "Reporte de resultados Grupo Argos 2T26", "url": "https://files.grupoargos.com/uploads-grupo-argos/2026/08/004.01.-Reporte-Resultados-Trimestrales-2Q2026.pdf", "retrievedAt": NOW},
  {"role": "Odinsa · venta de 50% de Quiport a Macquarie (USD 81,5 MM)", "url": "https://odinsa.com/wp-content/uploads/IR-Autorizacion-SFC_Segregacion-Activos_Junio02-2023_English.pdf", "retrievedAt": NOW},
  {"role": "Damodaran · betas globales ene-2026", "url": "https://pages.stern.nyu.edu/~adamodar/pc/datasets/betaGlobal.xls", "retrievedAt": NOW}]
SEC = {
 3: f"No se suman EBITDA o FCFF de todas las subsidiarias para luego aplicar un WACC único. Se obtiene el patrimonio económico atribuible de cada unidad y se suman solo los derechos de la matriz. SOTP económico (cotizadas a bolsa, privadas con datos fechados al 30-jun-2026) COP **{c0(econ)}**/acción; no es un DCF certificado.",
 4: f"Bolsa BVC 11.500 × 671.439.556 títulos Grupo = **COP 7,7216 billones** en el SOTP económico. Método sector: pares Buzzi 5,15×, Dangote 6,87× y Huaxin 5,10× EV/EBITDA FY2026, promedio 5,707×, sobre EBITDA FY26 de consenso COP 1.317.719 millones. Caja libre al 30-jun-2026 COP 7.793.000 millones (caja e inversiones CP 8.060.000 − restringida 5.000 − dividendo 2026 aún por pagar 262.000) menos deuda 2.879.000 = caja neta 4.914.000; minoritarios a valor justo = libro 641.600 × P/B 1,536 de CEMARGOS. Equity estimado del Grupo **COP {c4(cem_eq/1e6)} billones**. Toda la caja es legalmente libre (notas 6 y de garantías); su riesgo es económico: la reinversión anunciada en EE.UU. (crecimiento orgánico < US$500 MM) y la recompra de COP 450 mil MM en curso. Las historias Conservadora y Disrupción del DCF castigan esa caja 15% y 30%.",
 5: f"Bolsa BVC 4.810 × 557.205.138 acciones = **COP 2,6802 billones**. Método sector: Enel Chile 6,52× y Engie Energía Chile 6,43× (promedio 6,475×) sobre EBITDA FY26 de COP 1.749.114 millones, menos deuda neta oficial 2T26 COP 4.850.000 millones y minoritarios a valor justo (libro 1.761.600 × P/B 1,586). Equity del Grupo **COP {c4(cel_eq/1e6)} billones**. Caja restringida de Celsia y Celsia Colombia: COP 84.649 millones.",
 6: f"Odinsa al 30-jun-2026 con datos fechados: patrimonio en libros al 100% COP 1.884.840 millones (incluye el 50% del FCP Odinsa Infraestructura a valor razonable, COP 1.274.152 millones, valorado por expertos independientes), más el mayor valor de Quiport 23,25% a precio de la venta idéntica a Macquarie (USD 81,5 MM → COP 262.767 millones frente a 153.135 en libros) y el gestor por DCF (COP 76.400 millones). Valor al 100% COP {c0(odinsa/0.9499)} millones; atribuible 94,99% **COP {c4(odinsa/1e6)} billones**. El NAV de la gerencia de dic-2025 (2,4–3,0 billones) queda como sensibilidad: SOTP económico {c0(s11[0])}–{c0(s11[1])}. Grupo Argos usa como referencia propia COP 2,057 billones (precio de OPA COP 10.500, 99,9%).",
 7: f"Pactia al valor de unidad del 30-jun-2026 publicado por el emisor: COP 17.128,50 × 62.213.152 unidades = **COP {c4(pactia/1e6)} billones** (antes 1,03 de Colliers sep-2025). El valor contable homologado es COP 16.990,09 por unidad (1,057 billones). Venta de centros comerciales a Mallplaza con cierre al 30-sep: no se suma caja y activo dos veces.",
 8: f"Sator COP 159.627m, Summa 4.644m, otras asociadas 3.032m y residual patrimonial 154.583m al libro; terrenos y desarrollo urbano ya están en el residual. Se resta una vez la readquisición de septiembre (COP 39.222m) y el VP de gastos de matriz COP {c0(hq)}m (Ke holding 17,97 %, g 4,5 %, recurrencia 90 %).",
 9: f"Las filiales cotizadas se valoran por EV/EBITDA de pares con puente EV → patrimonio que resta deuda o suma caja libre al 2T26 y resta minoritarios a valor justo; Odinsa y Pactia comparten la valoración del SOTP económico. Resultado **COP {c0(mult)} por acción**. Las dos rutas no son independientes en privadas y gastos de matriz.",
 10: f"| Método | Valor COP por acción | Peso inicial |\n|---|---:|---:|\n| SOTP económico (bolsa + privadas 2T26) | {c0(econ)} | 60 % |\n| SOTP EV/EBITDA de pares por filial | {c0(mult)} | 40 % |\n| Libro NIIF proforma | 14.733 | Opcional 0 % |\n| DCF FCFF por partes (r4) | {c0(DCF['Base'])} | Opcional 0 % |\n| P/B y dividend yield PF 2025 | 12.667 | Histórico, fuera de Base |\n| **VALOR BASE** | **{c0(base)}** | **100 %** |\n\nLos pesos se rebalancean en la hoja y en el visor.",
 11: f"| Historia | Probabilidad | COP/acción |\n|---|---:|---:|\n| Conservadora | 25 % | {c0(vals[0])} |\n| **Base** | **50 %** | **{c0(vals[1])}** |\n| Optimista | 20 % | {c0(vals[2])} |\n| Disrupción · deterioro fundamental | 5 % | {c0(vals[3])} |\n| Esperado | 100 % | {c0(expv)} |\n\nDCF FCFF por partes (misma tasa en las cuatro historias): {c0(DCF['Base'])} / {c0(DCF['Conservadora'])} / {c0(DCF['Optimista'])} / 0; esperado {c0(DCFEXP)}.",
 12: f"Supuestos ilustrativos: SOTP +3,5% anual y relativo +5% anual, Ke holding 17,97 %. Objetivo exdividendo FY+3 **COP {c0(fy[6])}**; descontado **COP {c0(fy[7])}**; dividendo hipotético COP 750/año con VP COP {c0(fy[8])}; paquete VP **COP {c0(fy[9])}**.",
 13: f"Caja libre de Cementos al 70%: múltiplos {c0(mult)} → **{c0(c12[22])}**. Celsia con EBITDA UDM (deuda/3,22): **{c0(c12[20])}**. Odinsa con NAV de gerencia 2,4–3,0 billones: SOTP económico **{c0(s11[0])}–{c0(s11[1])}**. WACC de motores secundarios por Damodaran: Growth 13,22%, concesiones 13,40%, Pactia fondo 15,36%, gestores 16,56%, NDU 14,10%.",
 14: f"**Base condicional COP {c0(base)}**; frente a la PF (16.500) potencial aritmético **{pc(base/16500-1)}**; frente a la ordinaria (21.000) **{pc(base/21000-1)}**. Cerrado en r4 con fuentes fechadas: Odinsa y Pactia al 30-jun-2026, caja libre de Cementos por notas, minoritarios a valor justo por P/B, WACC de motores secundarios. Sigue sin certificar: valor justo propio de cada minoritario (se usa el P/B de la matriz cotizada), Quiport con precio de 2023, y flujos por concesión. [Libro de cálculo](https://docs.google.com/spreadsheets/d/1cZbcnriKIfvQX2oPgOKZUKZudSd8EcOwlh9NvjUADDo/edit).",
}
c = d["reports"]["valuation"]["content"]
for n, txt in SEC.items():
    pat = re.compile(rf'(<a id="jmr-valuation-{n}"></a>\n## {n}\. [^\n]*\n)(.*?)(?=\n<a id="jmr-valuation-{n+1}"></a>|\Z)', re.S)
    assert pat.search(c), n
    c = pat.sub(lambda m: m.group(1) + txt + "\n", c, count=1)
note = f"\n> **r4 · 10-oct-2026.** Base 19.363 → **{c0(base)}**; esperado 18.913 → {c0(expv)}. Odinsa y Pactia con datos del 30-jun-2026, caja libre de Cementos por notas, minoritarios a valor justo (libro × P/B) y WACC Damodaran en los motores secundarios.\n"
if "**r4 · 10-oct-2026.**" not in c:
    i = c.find("> **r3 · 10-oct-2026."); j = c.find("\n", i); c = c[:j + 1] + note + c[j + 1:]
d["reports"]["valuation"]["content"] = c
r = d["reports"]["research"]["content"]
r = r.replace("Nuevo Base SOTP+sector **COP 19.363** (r2)", f"Base SOTP+sector **COP {c0(base)}** (r4)")
r = re.sub(r"SOTP mixto [\d\.]+ y sector peer [\d\.]+; ponderación 60/40 \*\*[\d\.]+\*\* por acción", f"SOTP económico {c0(econ)} y sector {c0(mult)}; ponderación 60/40 **{c0(base)}** por acción", r)
r = re.sub(r"Historias: Conservadora [\d\.]+ \(25%\), Base [\d\.]+ \(50%\), Optimista [\d\.]+ \(20%\), Disrupción [\d\.]+ \(5%\)\. Valor esperado [\d\.]+\. PF 16\.500 margen aritmético [\d,]+ % y ordinaria 21\.000 margen -?[\d,]+ %\.",
           f"Historias: Conservadora {c0(vals[0])} (25%), Base {c0(vals[1])} (50%), Optimista {c0(vals[2])} (20%), Disrupción {c0(vals[3])} (5%). Valor esperado {c0(expv)}. PF 16.500 margen aritmético {pc(base/16500-1)} y ordinaria 21.000 margen {pc(base/21000-1)}.", r)
r = re.sub(r"FY\+3 ex-div COP [\d\.]+, presente [\d\.]+", f"FY+3 ex-div COP {c0(fy[6])}, presente {c0(fy[7])}", r)
r = r.replace("6.808", c0(DCF["Base"]))
if "**r4 · 10-oct-2026.**" not in r:
    i = r.find("> **r3 · 10-oct-2026."); j = r.find("\n", i); r = r[:j + 1] + note + r[j + 1:]
d["reports"]["research"]["content"] = r
json.dump(d, open(F, "w"), ensure_ascii=False, indent=1)
print("ok base", round(base), "exp", round(expv), "econ", round(econ), "mult", round(mult), "odinsa", round(odinsa), "pactia", round(pactia))
