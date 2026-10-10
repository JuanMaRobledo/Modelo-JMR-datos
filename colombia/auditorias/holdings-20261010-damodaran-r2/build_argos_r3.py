"""r3 Argos: DCF FCFF por partes recalculado con el WACC del corte Colombia común (hoja 1NAxSGF9...). Valores leídos de la hoja."""
import json
from pathlib import Path
F = Path(__file__).parent.parent.parent / "expedientes" / "PFGRUPOARG.CL-pfgrupoarg-20261009-clean-master.json"
d = json.load(open(F)); vs = d["valuationSummary"]; vo = vs["valuationOutput"]
NOW = "2026-10-10T23:30:00.000Z"
DCF = {"Base": 6808.331519361185, "Conservadora": 1114.1555951071691, "Optimista": 15607.060773304474, "Disrupción": 0.0}
EXPV = 6804.11681311828
CEM = {"Base": 3140390.1361405624, "Conservadora": 2430495.7986322315, "Optimista": 4083380.494581117, "Disrupcion": 1832221.3607659643}
CEL = {"Base": 5652946.036956072, "Conservadora": 4329343.193621953, "Optimista": 7173079.427239475, "Disrupcion": 3529849.3662820207}
WACC = {"Cementos": 0.15906022171819997, "Celsia": 0.126630451791}
mult = vs["sectorSotpMultiplesCOP"]
vs.update({"dcfPrimaryIntrinsicPerShareCOP": DCF["Base"], "dcfPrimaryExpectedCOP": EXPV})
vo.update({"dcfBaseCOP": DCF["Base"], "dcfConservativeCOP": DCF["Conservadora"], "dcfOptimisticCOP": DCF["Optimista"], "dcfDisruptionCOP": 0, "dcfExpectedCOP": EXPV,
           "priceToDCF": 16500 / DCF["Base"], "dcf60Multiples40COP": 0.6 * DCF["Base"] + 0.4 * mult, "synchronizedAt": NOW})
vo.setdefault("sotpCheck", {})["dcfBaseCOP"] = DCF["Base"]
for s in vs["dcfFcffIntrinsicScenarios"]:
    k = "Disrupcion" if s["name"].startswith("Disrup") else s["name"]
    s["intrinsicPerPreferredShareCOP"] = DCF["Disrupción" if k == "Disrupcion" else k]
    s["upsideVsPF"] = s["intrinsicPerPreferredShareCOP"] / 16500 - 1
    s["enterpriseValueCementosCOPm"] = CEM[k]; s["enterpriseValueCelsiaCOPm"] = CEL[k]
    if "breakdownCOPtrillions" in s and k == "Base":
        s["breakdownCOPtrillions"].update({"cementosConsolidatedEV": CEM["Base"] / 1e6, "celsiaCoreEV": CEL["Base"] / 1e6})
vs["dcfEnterpriseScenariosCOPm"]["Cementos"] = CEM; vs["dcfEnterpriseScenariosCOPm"]["Celsia"] = CEL
for c in vs["dcfComponents"]:
    if c["name"].startswith("Cementos"):
        c.update({"enterpriseValue": CEM["Base"], "scenarios": CEM, "status": "CEMENTOS: DCF FCFF operativo 10 años, WACC 15,906% (r3: Rf COP 11,467% = TES − spread; ERP 4,20%; CRP 2,72% × λ 0,7; Kd 12,8%; D/V 18%). EV NO equity."})
    if c["name"].startswith("Celsia"):
        c.update({"enterpriseValue": CEL["Base"], "scenarios": CEL, "status": "CELSIA: DCF FCFF parcial, WACC 12,663% (r3: β 0,71; λ 0,94; D/V 50%). No captura vehículos Growth completos; diagnóstico."})
ra = vs.get("dcfRateAudit", {})
ra.update({"rfCOP": 0.11467118776169417, "rfSyntheticCOP": None, "erpMature": 0.042, "crpColombia": 0.0272018253, "dateOfRecalculation": "2026-10-10",
           "sourceStatus": "r3: Rf COP = TES 13,217% (IRC 25-sep-2026) − spread 1,75% (Damodaran jul-2026), mismo corte que Grupo SURA y Davivienda; beta, lambda, D/V y Kd del analista sin cambios"})
for co in ra.get("company", []):
    co["previousBaseWacc"] = co.get("wacc"); co["wacc"] = WACC["Cementos" if co["business"].startswith("Cementos") else "Celsia"]
for m in vs.get("methodSelectionDefault", {}).get("methods", []):
    if m["id"] == "dcf": m["valueCOP"] = DCF["Base"]
vs["conclusion"] = vs["conclusion"].replace("FCFF previo 8.294 opcionales", "FCFF r3 6.808 (WACC corte Colombia) opcionales")
a = d["audit"]; a["checks"]["fcffEnginesOnHarmonizedRate"] = True
a["warnings"] = [w for w in a["warnings"] if not w.startswith("El DCF FCFF opcional (8.294)")] + [
  "r3: DCF FCFF por partes recalculado con el corte Colombia (WACC Cementos 15,91%, Celsia 12,66%): Base 6.808 (antes 8.294), esperado 6.804; peso 0 en el Base. Motores secundarios (Odinsa, Pactia, Growth) conservan sus WACC de analista."]
d["updatedAt"] = NOW; d["publication"]["revisedAt"] = NOW
note = "\n> **r3 · 10-oct-2026.** DCF FCFF por partes recalculado con el mismo corte: WACC Cementos 15,91% y Celsia 12,66% (antes 13,87% y 11,43% con Rf sintética 8,86%). DCF Base 6.808 (antes 8.294), esperado 6.804; sigue con peso 0. El Base 60/40 no cambia.\n"
for k in ("valuation", "research"):
    c = d["reports"][k]["content"]
    if "**r3 · 10-oct-2026.**" not in c:
        i = c.find("> **Revisión Damodaran r2"); j = c.find("\n\n", i)
        c = c[:j + 1] + note + c[j + 1:]
    c = c.replace("8.294", "6.808").replace("8294", "6808")
    c = c.replace("DCF Base 6.808 (antes 6.808)", "DCF Base 6.808 (antes 8.294)").replace("(antes 6.808), esperado 6.804", "(antes 8.294), esperado 6.804")
    d["reports"][k]["content"] = c
json.dump(d, open(F, "w"), ensure_ascii=False, indent=1)
print("ok", round(vs["dcfPrimaryIntrinsicPerShareCOP"]), round(vs["primaryValueCOP"]))
