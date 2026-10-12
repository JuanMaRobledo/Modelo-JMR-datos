"""r5 Colombia (corte 30-sep-2026): lleva a los expedientes los valores de las hojas con el mismo criterio que la cartera
de EE.UU.: valor principal = DCF Base intrínseco (Damodaran); esperado = suma por probabilidades; precio de compra =
esperado × (1 − 35%); múltiplos y SOTP de mercado como lectura secundaria (ponderado 40% DCF + 60% múltiplos).

Lee celdas sin formato de las cuatro hojas (no recalcula aquí) y escribe:
  PFDAVVNDA, PFDAVIGRP, PFGRUPSURA y GRUPOSURA (r3 del 10-oct) y PFGRUPOARG.
El expediente PFGRUPSURA del 9-oct (clean-master) queda marcado como reemplazado, sin cambiar su fecha de revisión.
Idempotente: una nueva corrida reemplaza la nota r5 anterior. Uso: python3 build_r5.py
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, "/home/user/JMR-valuation")
from jmr_valuation.io.sheets_auth import get_gspread_client  # noqa: E402

P = Path(__file__).resolve().parent
EXP = P.parents[1] / "expedientes"
NOW = "2026-10-12T03:00:00.000Z"
DATE = "2026-09-30"
MOS = 0.35
W_DCF = 0.4
ID = {"BANCO": "16smCZh7JIB3om_UabhiFymPElK6zyq_6Z8iY-P4Kgrs", "GROUP": "1ogP8LfxEBxslOeC6Avgk2BAClJ_0cfzpgJ06icvVSys",
      "SURA": "1Nb9_T6n8xbJikr68TN5MA5bIIiwm0aKrsF7m4MmOHyM", "ARGOS": "1cZbcnriKIfvQX2oPgOKZUKZudSd8EcOwlh9NvjUADDo"}
URL = {k: f"https://docs.google.com/spreadsheets/d/{v}/edit" for k, v in ID.items()}
gc = get_gspread_client()


def get(key, *ranges):
    r = gc.open_by_key(ID[key]).values_batch_get(list(ranges), params={"valueRenderOption": "UNFORMATTED_VALUE"})
    return [v.get("values", []) for v in r["valueRanges"]]


def cop(x):
    return "N/D" if x is None else f"COP {x:,.0f}".replace(",", ".")


def pct(x, d=1):
    return f"{x*100:.{d}f}%".replace(".", ",")


NAMES = ["Base", "Conservadora", "Optimista", "Disrupción"]
SOURCES = [
    {"role": "erp-implicita-damodaran-oct-2026", "url": "https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/implpr.html"},
    {"role": "tes-2036-cierre-septiembre-2026", "url": "https://es-us.noticias.yahoo.com/colombia-arranca-octubre-tes-alza-151456108.html"},
    {"role": "precios-cierre-bvc-2026-09-30", "url": "https://finance.yahoo.com/quote/PFDAVVNDA.CL/history/"},
]


def common(d, *, key, base, expected, stories, probs, price, mult, ke, rf, erp, method, label, note_rows, extra=""):
    """Campos comunes con la semántica de la cartera de EE.UU."""
    s = d["valuationSummary"]
    comb = W_DCF * base + (1 - W_DCF) * mult if mult is not None else None
    s.update({
        "base": base, "expected": expected, "marketPrice": price, "priceDate": DATE,
        "primaryValueCOP": base, "primaryValueMethod": method, "primaryValueLabel": label, "baseIsIntrinsic": True,
        "dcfPrimaryIntrinsicPerShareCOP": base, "dcfPrimaryExpectedCOP": expected,
        "mos": MOS, "baseMOS": "valorEsperado", "precioMOS": expected * (1 - MOS),
        "potentialBase": base / price - 1, "priceToBase": price / base if base else None,
        "combinedWeights": {"fcfe": W_DCF, "multiples": 1 - W_DCF},
        "combinedWeightedToday": comb,
        "combinedStatus": "Secundario: 40% DCF intrínseco + 60% múltiplos (igual que la cartera de EE.UU.); no sustituye el DCF Base.",
        "sheetUrl": URL[key],
    })
    for k in ("mos20Base", "mos20Expected"):
        s.pop(k, None)
    s["mosBase"] = 1 - price / base if base else None
    s["mosExpected"] = 1 - price / expected if expected else None
    vo = s.setdefault("valuationOutput", {})
    vo.update({"sheetUrl": URL[key], "synchronizedAt": NOW, "dcfBaseCOP": stories[0], "dcfConservativeCOP": stories[1],
               "dcfOptimisticCOP": stories[2], "dcfDisruptionCOP": stories[3], "dcfExpectedCOP": expected, "priceCOP": price,
               "weights": {**(vo.get("weights") or {}), "dcf": W_DCF, "multiples": 1 - W_DCF},
               "status": f"r5 corte {DATE}: valor principal = {label}"})
    for sc, v, p in zip(d["scenarios"], stories, probs):
        sc.update(value=v, probability=p)
    d["quote"].update(price=price, sessionDate=DATE, quotedAt=f"{DATE}T20:00:00.000Z", kind="historical-session-close",
                      source=f"Yahoo Finance {d['ticker']} — cierre BVC {DATE} (corte común con la cartera de EE.UU.)",
                      url=f"https://finance.yahoo.com/quote/{d['ticker']}/history/", retrievedAt=NOW)
    a = d["assumptions"]
    a.update(riskfreeRate=rf, equityRiskPremium=erp, costOfEquity=ke,
             erpNote="ERP madura 3,70% = implícita de Damodaran oct-2026 (igual que la cartera de EE.UU.) + prima país; antes 4,20% base madura jul-2026",
             riskfreeNote="Rf COP = TES jul-2036 13,00% al cierre de sep-2026 − spread soberano Colombia 1,75% (Damodaran jul-2026)")
    au = d["audit"]
    au["revision"] = "r5-20260930-corte-comun"
    au["revisionDate"] = "2026-10-12"
    au.setdefault("checks", {}).update({"commonCutoffWithUSPortfolio": True, "primaryValueIsIntrinsic": True, "mosOnExpected35": True})
    au["warnings"] = [w for w in au.get("warnings", []) if not w.startswith("r5:")] + [
        f"r5: corte común con la cartera de EE.UU. ({DATE}): ERP 3,70% + CRP, Rf COP 11,25%, cierres BVC del 30-sep.",
        "r5: el valor principal es el intrínseco Damodaran; SOTP de mercado, 60/40 y múltiplos quedan como lectura secundaria.",
        "r5: TES del cierre de septiembre (13,00%) de fuente secundaria (prensa); el IRC publicó 13,217% el 25-sep y 13,12% el 2-oct."]
    have = {x.get("url") for x in d.get("sources", [])}
    d.setdefault("sources", []).extend({**x, "retrievedAt": NOW} for x in SOURCES if x["url"] not in have)
    d["publication"].update(revisedAt=NOW, revisionNote=f"r5 ({DATE}): corte común con EE.UU. y valor principal = intrínseco Damodaran; MOS 35% sobre el esperado.")
    d["updatedAt"] = NOW
    rows = "".join(f"| {n} | {pct(p,0)} | {cop(v)} |\n" for n, p, v in zip(NAMES, probs, stories))
    note = (f"## Revisión r5 · corte {DATE} · valor principal = intrínseco Damodaran\n\n"
            f"Igual que la cartera de EE.UU.: el **DCF Base intrínseco es el valor principal**, el esperado es su complemento y el precio "
            f"de compra aplica un margen de seguridad de 35% sobre el esperado. Los múltiplos y el SOTP de mercado son lectura secundaria.\n\n"
            f"| Historia | Probabilidad | Valor intrínseco COP/acción |\n| --- | --- | --- |\n{rows}"
            f"| **Esperado** | 100% | **{cop(expected)}** |\n\n"
            f"- **DCF Base (valor intrínseco principal): {cop(base)}**; precio {d['ticker']} al {DATE}: {cop(price)} (Base/precio {pct(base/price-1)}).\n"
            f"- **Precio de compra con MOS 35% sobre el esperado: {cop(expected*(1-MOS))}.**\n"
            + (f"- Múltiplos (secundario): {cop(mult)}; ponderado 40% DCF + 60% múltiplos: {cop(comb)}.\n" if mult is not None else "")
            + note_rows +
            f"- Tasas: Rf COP {pct(rf,2)} (TES 13,00% − spread 1,75%), ERP madura {pct(erp,2)} (implícita oct-2026) + prima país; Ke {pct(ke,2)}.\n"
            + extra +
            "\n*Las secciones siguientes son el informe anterior; donde sus cifras difieran, manda esta nota r5.*\n\n")
    for k in ("valuation", "research"):
        rep = d["reports"].get(k)
        if not rep:
            continue
        c = rep["content"]
        start = c.find("## Revisión r5 · corte")
        if start >= 0:
            end = c.find("manda esta nota r5.*\n\n", start)
            c = c[:start] + c[end + len("manda esta nota r5.*\n\n"):]
        if c.startswith("---\n"):
            fm_end = c.find("\n---\n", 4) + len("\n---\n")
            c = c[:fm_end] + "\n" + note + c[fm_end:].lstrip("\n")
        else:
            c = note + c
        rep["content"] = c
        rep["importedAt"] = NOW
    return comb


def banco():
    f = EXP / "PFDAVVNDA.CL-pfdavvnda-20261009-jmr-r1.json"
    d = json.loads(f.read_text())
    res, ces, mb, ke = get("BANCO", "Resumen!B14:E17", "'Cesión Davibank'!A58:E65", "'Múltiplos Banco'!A11:H14", "'Ke sustentado'!B5:B13")
    rows = {r[0]: r for r in ces if r}
    order = ["Base", "Conservadora", "Optimista", "Disrupción"]
    st = [rows[n][3] for n in order]
    probs = [rows[n][4] for n in order]
    exp = sum(p * v for p, v in zip(probs, st))
    price = res[3][0]
    m = {r[0]: r[1:] for r in mb if r}
    pb = [m[n][5] for n in ("Base", "Conservador", "Optimista")]
    pe = [m[n][6] for n in ("Base", "Conservador", "Optimista")]
    mult = [0.65 * a + 0.35 * b for a, b in zip(pb, pe)]
    rf, erp, ke0 = ke[2][0], ke[3][0], ke[7][0]
    s = d["valuationSummary"]
    s["reportedPerimeter"] = {"base": res[0][0], "conservador": res[0][1], "optimista": res[0][2], "disrupcion": res[0][3]}
    s["multiplesWeightedToday"] = mult[0]
    s["standaloneMultiplesToday"] = [*mult, 0]
    s["weightedDcfMultiplesToday"] = [W_DCF * a + (1 - W_DCF) * b for a, b in zip(st[:3], mult)] + [0]
    for x in s.get("multiplesMethods", []):
        if x["name"] == "P/B":
            x.update(today=pb[0], anchors=[pb[1], pb[0], pb[2]])
        if x["name"] == "P/E":
            x.update(today=pe[0], anchors=[pe[1], pe[0], pe[2]])
    for sc, v in zip(s.get("dcfFcffIntrinsicScenarios", []), st):
        sc["intrinsicPerPreferredShareCOP"] = v
    s["scopeLabel"] = "Perímetro reportado + cesión DAVIbank (valor justo + sinergias) · r5 corte 30-sep-2026"
    comb = common(d, key="BANCO", base=st[0], expected=exp, stories=st, probs=probs, price=price, mult=mult[0], ke=ke0, rf=rf, erp=erp,
                  method="RE_DDM_REGULATORY_PLUS_CESSION", label="DCF Base · RE/DDM con cesión DAVIbank (intrínseco Damodaran)",
                  note_rows=f"- Perímetro reportado sin cesión: {cop(res[0][0])} (Base).\n")
    s["scenarios"] = d["scenarios"]
    f.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
    return dict(base=st[0], exp=exp, price=price, mos=exp * (1 - MOS), mult=mult[0], comb=comb, ke=ke0)


def group():
    f = EXP / "PFDAVIGRP.CL-pfdavigrp-20261009-jmr-r3.json"
    d = json.loads(f.read_text())
    va, disc, ent = get("GROUP", "'Valoración actual'!A8:P12", "'Group flujos'!J7", "'Entradas cierre'!B12:B26")
    disc = disc[0][0]
    rows = {r[0]: r for r in va}
    order = ["Base", "Conservador", "Optimista", "Disruptivo"]
    R = [rows[n] for n in order]
    E = rows["Esperado"]
    rf, erp, crp, ke0, ke1, price = ent[0][0], ent[1][0], ent[2][0], ent[7][0], ent[8][0], ent[14][0]
    st = [r[2] for r in R]
    probs = [r[1] for r in R]
    s = d["valuationSummary"]
    s.update({"multiplesWeightedToday": R[0][9], "multiplesWeightedYear3": R[0][11], "multiplesWeightedYear3PV": R[0][11] / disc,
              "combinedWeightedYear3": R[0][12], "combinedWeightedYear3PV": R[0][12] / disc,
              "scopeLabel": "FCFE financiero (intrínseco Damodaran) · r5 corte 30-sep-2026"})
    pv = lambda fy3, r: fy3 / disc + r[13]  # noqa: E731
    for x in s.get("multiplesMethods", []):
        if x["name"].startswith("P/B"):
            x.update(today=pv(R[0][7], R[0]), year3=R[0][7], year3PV=R[0][7] / disc, anchors=[pv(R[1][7], R[1]), pv(R[0][7], R[0]), pv(R[2][7], R[2])])
        if x["name"].startswith("P/E"):
            x.update(today=pv(R[0][8], R[0]), year3=R[0][8], year3PV=R[0][8] / disc, anchors=[pv(R[1][8], R[1]), pv(R[0][8], R[0]), pv(R[2][8], R[2])])
    s["dcfFcffIntrinsicScenarios"] = [{"name": n, "weight": r[1], "intrinsicPerPreferredShareCOP": r[2], "economicCOP": r[3],
                                      "residualFy3COP": r[4], "pvDistributions13COP": r[13]} for n, r in zip(order, R)]
    m = d.get("model", {})
    m["ke_initial"], m["ke_terminal"] = ke0, ke1
    for res, r in zip(m.get("results", []), R):
        res.update(dcf=r[2], economic=r[3], residual3=r[4], pvdistributions3=r[13], multiplepresent=r[9], combined=r[10])
    d["assumptions"]["terminalCostOfEquity"] = ke1
    d["assumptions"]["countryRiskExposure"] = crp
    comb = common(d, key="GROUP", base=st[0], expected=E[2], stories=st, probs=probs, price=price, mult=R[0][9], ke=ke0, rf=rf, erp=erp,
                  method="FCFE_FINANCIAL_REGULATORY", label="DCF Base · FCFE financiero (intrínseco Damodaran)",
                  note_rows=f"- Ke inicial {pct(ke0,2)} y terminal {pct(ke1,2)} (beta 0,7 → 1).\n")
    f.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
    return dict(base=st[0], exp=E[2], price=price, mos=E[2] * (1 - MOS), mult=R[0][9], comb=comb, ke=ke0)


def sura():
    res, T, ke, pord, ppf = get("SURA", "Resumen!B14:E16", "'CO · Ke y SOTP 60-40'!B57:E79", "'CO · Ke y SOTP 60-40'!B6:B9",
                               "Datos!B26", "'CO · Clase y mercado'!B6")
    st, probs, exp = res[0], res[1], res[2][0]
    rows = {n: T[i] for i, n in enumerate(["sCib", "sAM", "sSur", "cibMkt", "amRE", "surRE", "other", "bridge", "hq", "econM", "econ",
                                           "cibMult", "amMult", "surMult", "multM", "mult", "blend", "re", "prob"])}
    rf, erp = ke[2][0], ke[3][0]
    kh = get("SURA", "'CO · Ke y SOTP 60-40'!B30")[0][0][0]
    out = {}
    for fname, price, cls in (("PFGRUPSURA.CL-pfgrupsura-20261010-damodaran-jmr.json", ppf[0][0], "preferencial"),
                              ("GRUPOSURA.CL-gruposura-20261010-damodaran-jmr.json", pord[0][0], "ordinaria")):
        f = EXP / fname
        d = json.loads(f.read_text())
        s = d["valuationSummary"]
        s.update({"sotpEconomicCOP": rows["econ"][0], "sectorSotpMultiplesCOP": rows["mult"][0], "multiplesWeightedToday": rows["mult"][0],
                  "intrinsicDamodaranCOP": st[0], "intrinsicDamodaranExpectedCOP": exp,
                  "scopeLabel": "Holding financiero · valor principal = intrínseco Damodaran RE/DDM de Cibest, SURA AM y Suramericana (r5 corte 30-sep-2026). SOTP de mercado y 60/40 como referencia secundaria."})
        vo = s.setdefault("valuationOutput", {})
        vo.update({"marketSotpPrimaryCOP": rows["econ"][0], "sectorSotpMultiplesCOP": rows["mult"][0], "base6040COP": rows["blend"][0],
                   "dcfLabel": "Valor intrínseco Damodaran RE/DDM · principal",
                   "methodWeightPolicy": "r5: principal = intrínseco RE; ponderado secundario 40% intrínseco + 60% múltiplos; SOTP de mercado y 60/40 opcionales"})
        s["holdingScenarioTable"] = [{"name": n, "probability": probs[i], "intrinsicRECOP": st[i], "base6040COP": rows["blend"][i],
                                      "sotpEconomicCOP": rows["econ"][i], "sotpMultiplesCOP": rows["mult"][i]} for i, n in enumerate(NAMES)]
        for sc, v in zip(s.get("dcfFcffIntrinsicScenarios", []), st):
            sc.update(intrinsicPerPreferredShareCOP=v, intrinsicPerShareCOP=v)
        comb = common(d, key="SURA", base=st[0], expected=exp, stories=st, probs=probs, price=price, mult=rows["mult"][0], ke=kh, rf=rf, erp=erp,
                      method="RESIDUAL_INCOME_DDM_PER_SUBSIDIARY", label="DCF Base · intrínseco RE/DDM (Damodaran)",
                      note_rows=(f"- Acción {cls}. Referencias secundarias: SOTP de mercado (Cibest a bolsa) {cop(rows['econ'][0])}; "
                                 f"60/40 anterior {cop(rows['blend'][0])}.\n"))
        f.write_text(json.dumps(d, ensure_ascii=False, indent=1))
        out[d["ticker"]] = dict(base=st[0], exp=exp, price=price, mos=exp * (1 - MOS), mult=rows["mult"][0], comb=comb, ke=kh)
    old = EXP / "PFGRUPSURA.CL-pfgrupsura-20261009-clean-master.json"
    d = json.loads(old.read_text())
    d["publication"]["supersededBy"] = "PFGRUPSURA.CL-pfgrupsura-20261010-damodaran-jmr.json"
    d["publication"]["supersededNote"] = "Reemplazado por la revisión Damodaran del 10-oct (r3) y su actualización r5 (corte 30-sep-2026)."
    old.write_text(json.dumps(d, ensure_ascii=False, indent=2))
    return out


def argos():
    ref = json.loads((P / "argos_dcf_filiales.ref.json").read_text())
    ps, ex = ref["per_share"], ref["expected"]
    q = "'CO 15 DCF Damodaran'"
    rows = get("ARGOS", f"{q}!B{ps}:E{ps}", f"{q}!B{ps+1}:E{ps+1}", f"{q}!B{ex}", f"{q}!B{ps-1}:E{ps-1}",
               "'CO 12 Comparables sector'!B34", "'CO 11 SOTP economico'!G16", "'CO 05 Multiples'!D16",
               "'CO 01 Fuentes y datos'!B10:B11", "'CO 11 SOTP economico'!B38:B42", f"{q}!B26", f"{q}!B45")
    st, probs, exp, eq = rows[0][0], rows[1][0], rows[2][0][0], rows[3][0]
    mult, mkt, pond = rows[4][0][0], rows[5][0][0], rows[6][0][0]
    ppf, pord = rows[7][0][0], rows[7][1][0]
    rf, erp, keh = rows[8][0][0], rows[8][1][0], rows[8][4][0]
    ev = {}
    for name, d_ in ref["subs"].items():
        ev[name] = [get("ARGOS", f"{q}!B{d_[n]-2}")[0][0][0] for n in NAMES]
    f = EXP / "PFGRUPOARG.CL-pfgrupoarg-20261009-clean-master.json"
    d = json.loads(f.read_text())
    s = d["valuationSummary"]
    s.update({"navReference": mkt, "multiplesWeightedToday": mult, "sectorSotpMultiplesCOP": mult,
              "scopeLabel": "Holding · valor principal = SOTP intrínseco Damodaran (Cementos Argos y Celsia por FCFF; Odinsa, Pactia y demás a valores fechados 2T26) · r5 corte 30-sep-2026"})
    s["dcfFcffIntrinsicScenarios"] = [{"name": n, "weight": probs[i], "intrinsicPerPreferredShareCOP": st[i], "intrinsicPerShareCOP": st[i],
                                      "equityHoldingCOPtrillions": eq[i] / 1e6, "enterpriseValueCementosCOPm": ev["Cementos Argos"][i],
                                      "enterpriseValueCelsiaCOPm": ev["Celsia"][i]} for i, n in enumerate(NAMES)]
    vo = s.setdefault("valuationOutput", {})
    vo.update({"primarySheet": "CO 15 DCF Damodaran", "marketSotpPrimaryCOP": mkt, "multiplesWeightedBaseCOP": mult,
               "dcf60Multiples40COP": None, "priceToDCF": ppf / st[0], "dcfWeight": W_DCF, "multiplesWeight": 1 - W_DCF,
               "method": "SOTP intrínseco: FCFF Damodaran de Cementos Argos y Celsia + valores fechados de privadas − HQ"})
    vo.setdefault("sotpCheck", {}).update({"hybridNAVBaseCOP": mkt, "dcfBaseCOP": st[0]})
    for m in s.get("methodSelectionDefault", {}).get("methods", []):
        if m.get("id") == "dcf":
            m["valueCOP"] = st[0]
        if m.get("id") == "market_sotp":
            m["valueCOP"] = mkt
    extra = (f"- Filiales (DCF FCFF, pestaña «CO 15 DCF Damodaran»): EV Base Cementos Argos {cop(ev['Cementos Argos'][0])} millones y Celsia "
             f"{cop(ev['Celsia'][0])} millones; WACC 16,2% y 12,8%; ROIC terminal = WACC (sin foso); crecimiento terminal = Rf COP; "
             "inflación COP consistente con el diferencial de tasas. Con esas tasas, Cementos (ROIC ~7%) y Celsia (~8%) rinden menos que su costo "
             "de capital en pesos, y el DCF queda por debajo de la bolsa.\n"
             f"- Referencias secundarias: SOTP de mercado {cop(mkt)}; múltiplos sectoriales {cop(mult)}; ponderado de la hoja {cop(pond)}. "
             f"Ordinaria GRUPOARGOS al {DATE}: {cop(pord)}.\n")
    comb = common(d, key="ARGOS", base=st[0], expected=exp, stories=st, probs=probs, price=ppf, mult=mult, ke=keh, rf=rf, erp=erp,
                  method="SOTP_INTRINSIC_FCFF_DAMODARAN", label="DCF Base · SOTP intrínseco (Damodaran)", note_rows="", extra=extra)
    f.write_text(json.dumps(d, ensure_ascii=False, indent=1))
    return dict(base=st[0], exp=exp, price=ppf, mos=exp * (1 - MOS), mult=mult, comb=comb, ke=keh)


if __name__ == "__main__":
    out = {"PFDAVVNDA.CL": banco(), "PFDAVIGRP.CL": group(), **sura(), "PFGRUPOARG.CL": argos()}
    (P / "resultados_r5.json").write_text(json.dumps(out, ensure_ascii=False, indent=1))
    for k, v in out.items():
        print(k, {a: round(b, 4) if isinstance(b, float) and b < 1 else (round(b) if isinstance(b, float) else b) for a, b in v.items()})
