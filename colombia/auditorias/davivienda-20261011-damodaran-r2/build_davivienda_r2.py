"""r2 Davivienda: publica en los expedientes los valores de las hojas revisadas.

Lee las celdas sin formato de las hojas (no recalcula nada aquí) y escribe:
- PFDAVVNDA: precio 9-oct, Conservador moderado, puente de cesión DAVIbank y lectura de minoría.
- PFDAVIGRP: Ke armonizado (Rf COP 11,467%, ERP 4,20%) y resultados R4.
- valuationSummary.valuationOutput + dcfFcffIntrinsicScenarios para que el visor deje de mostrar N/D.
Uso: python3 build_davivienda_r2.py  (requiere GOOGLE_SERVICE_ACCOUNT_JSON_CONTENT)
"""
import json, pathlib, datetime
from gs import S

ROOT = pathlib.Path(__file__).resolve().parents[2] / "expedientes"
BANK_ID = "16smCZh7JIB3om_UabhiFymPElK6zyq_6Z8iY-P4Kgrs"
GROUP_ID = "1ogP8LfxEBxslOeC6Avgk2BAClJ_0cfzpgJ06icvVSys"
BANK_URL = f"https://docs.google.com/spreadsheets/d/{BANK_ID}/edit"
GROUP_URL = f"https://docs.google.com/spreadsheets/d/{GROUP_ID}/edit"
NOW = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z")
PRICE_DATE = "2026-10-09"


def get(sid, *ranges):
    r = S.spreadsheets().values().batchGet(spreadsheetId=sid, ranges=list(ranges),
                                           valueRenderOption="UNFORMATTED_VALUE").execute()
    return [vr.get("values", []) for vr in r["valueRanges"]]


def cop(x):
    return f"COP {x:,.0f}".replace(",", ".")


def pct(x, d=1):
    return f"{x*100:.{d}f}%".replace(".", ",")


NEW_SOURCES = [
    {"role": "cesion-davibank-info-relevante", "url": "https://cdn.aglty.io/scotiabank-colombia/davibank/Info_Relevante_0610_DAVIbank.pdf"},
    {"role": "guia-sinergias-y-desliste-2T26", "url": "https://www.accivalores.com/wp-content/uploads/Libro-de-resultados-Davivienda-Group-2T26-13.08.2026.pdf"},
    {"role": "presentacion-corporativa-1T26", "url": "https://ir.davivienda.com/wp-content/uploads/2026/05/Presentacion-Corporativa-Banco-Davivienda-1T26.pdf"},
    {"role": "rf-damodaran-ctryprem-jul26", "url": "https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/ctryprem.html"},
]


def add_sources(d, extra):
    have = {s.get("url") for s in d["sources"]}
    for s in extra:
        if s["url"] not in have:
            d["sources"].append({**s, "retrievedAt": NOW})


# ------------------------------------------------------------------ Banco
def bank():
    f = ROOT / "PFDAVVNDA.CL-pfdavvnda-20261009-jmr-r1.json"
    d = json.loads(f.read_text())
    res, ces, mb = get(BANK_ID, "Resumen!B14:E17", "'Cesión Davibank'!A31:E65", "'Múltiplos Banco'!A11:H14")
    reported = res[0]                      # Base, Cons, Opt, Disr (perímetro reportado)
    price = res[3][0]
    c = {row[0]: row[1:] for row in ces if row}
    rows = {r[0]: r for r in ces if r and r[0] in ("Base", "Conservadora", "Optimista", "Disrupción")}
    with_c = [rows[n][3] for n in ("Base", "Conservadora", "Optimista", "Disrupción")]
    npv = [rows[n][2] for n in ("Base", "Conservadora", "Optimista", "Disrupción")]
    probs = [rows[n][4] for n in ("Base", "Conservadora", "Optimista", "Disrupción")]
    expected = sum(p * v for p, v in zip(probs, with_c))
    exp_reported = sum(p * max(0, v) for p, v in zip(probs, reported))
    m = {r[0]: r[1:] for r in mb if r}
    pb = [m[n][5] for n in ("Base", "Conservador", "Optimista")]
    pe = [m[n][6] for n in ("Base", "Conservador", "Optimista")]
    mult = [0.65 * a + 0.35 * b for a, b in zip(pb, pe)]
    comb = [0.8 * dcf + 0.2 * mu for dcf, mu in zip(with_c[:3], mult)]
    shares = 487670413
    overpay = -0.1 * 2587000 * 1e6 / shares
    s = d["valuationSummary"]
    names = ["Base", "Conservador", "Optimista", "Disrupción"]
    s.update({
        "priceDate": PRICE_DATE,
        "scope": "reported-perimeter-plus-davibank-cession-bridge",
        "scopeLabel": "Perímetro reportado + cesión DAVIbank a valor justo con sinergias (r2)",
        "base": with_c[0], "expected": expected, "marketPrice": price,
        "mosBase": 1 - price / with_c[0], "mosExpected": 1 - price / expected,
        "potentialBase": with_c[0] / price - 1,
        "mos20Base": 0.8 * with_c[0], "mos20Expected": 0.8 * expected,
        "reportedPerimeter": {"base": reported[0], "conservador": reported[1], "optimista": reported[2],
                              "disrupcion": reported[3], "expectedFloor0": exp_reported},
        "pbToday": [*pb, None], "peToday": [*pe, None],
        "standaloneMultiplesToday": [*mult, 0],
        "weightedDcfMultiplesToday": [*comb, 0],
        "combinedWeightedToday": comb[0],
        "combinedWeightedTodayReportedPerimeter": 0.8 * reported[0] + 0.2 * mult[0],
        "dcfPrimaryIntrinsicPerShareCOP": with_c[0], "dcfPrimaryExpectedCOP": expected,
        "dcfFcffIntrinsicScenarios": [
            {"name": n, "weight": p, "intrinsicPerPreferredShareCOP": v, "reportedPerimeterCOP": r,
             "cessionNpvCOPm": x}
            for n, p, v, r, x in zip(names, probs, with_c, reported, npv)],
        "postTransfer": {
            "status": "BRIDGE_COMPLETE_FAIR_VALUE_EXCHANGE_PLUS_SYNERGIES",
            "resolution": "SFC Res. 1505 de 2-oct-2026",
            "consideration": "Hasta 30% de las acciones de HDI; términos de tercero independiente",
            "fairValueBusinessCOPm": c["Valor justo del negocio recibido (proxy: patrimonio DAVIbank Colombia; se cancela con la contraprestación)"][0],
            "groupSynergiesPreTaxCOPm": 1050000, "bankShare": 0.7, "realizationBase": 0.5, "taxRate": 0.35,
            "pvSynergiesBaseCOPm": c["VP de sinergias Base (perpetuidad desde 2028)"][0],
            "integrationCostsAfterTaxPVCOPm": c["Costos de integración del Banco después de impuestos (COP 600–700 mil MM, 70%)"][0],
            "npvBaseCOPm": npv[0], "npvPerShareBaseCOP": npv[0] * 1e6 / shares,
            "overpay10PctPerShareCOP": overpay,
            "value": with_c[0],
            "source": "https://cdn.aglty.io/scotiabank-colombia/davibank/Info_Relevante_0610_DAVIbank.pdf"},
        "controlledMinority": {
            "groupStake": 0.989, "bookPerShareCOP": 16879747e6 / shares, "exchange2025PriceToBook": 1.39,
            "exchange2025ReferenceCOP": 1.39 * 16879747e6 / shares, "priceToBook": price / (16879747e6 / shares),
            "delisting": "CEO 2T26: sin decisión de desliste, no descartado. En una OPA de desliste el precio lo fija un avaluador independiente. No se pondera.",
            "source": "https://www.accivalores.com/wp-content/uploads/Libro-de-resultados-Davivienda-Group-2T26-13.08.2026.pdf"},
        "conclusion": (f"Base r2 {cop(with_c[0])} por acción (perímetro reportado {cop(reported[0])} + cesión DAVIbank "
                       f"{cop(npv[0]*1e6/shares)}), esperado {cop(expected)}, frente a {cop(price)} el 9-oct: "
                       f"Base/precio {pct(with_c[0]/price-1)}. Múltiplos {cop(mult[0])}; combinado 80/20 {cop(comb[0])}. "
                       "La diferencia con el precio la explican la opción de OPA/desliste del controlante (98,9%) y una "
                       "rentabilidad terminal mayor que la del modelo; ninguna está en el Base."),
        "combinedStatus": "Base: FCFE con cesión 80% + múltiplos 20%; año 3 en perímetro reportado (sin cesión)",
        "certification": "R2_DAMODARAN_REVIEW__NOT_ACCOUNTING_AUDIT",
        "sheetUrl": BANK_URL,
        "valuationOutput": {
            "primarySheet": "Cesión Davibank", "sheetUrl": BANK_URL, "synchronizedAt": NOW,
            "status": "RE/FCFE r2 · perímetro reportado + cesión DAVIbank (VPN de sinergias); precio 9-oct-2026",
            "dcfBaseCOP": with_c[0], "dcfConservativeCOP": with_c[1], "dcfOptimisticCOP": with_c[2],
            "dcfDisruptionCOP": with_c[3], "dcfExpectedCOP": expected, "priceCOP": price,
            "dcfYear3ExDividend": None, "weights": {"dcf": 0.8, "multiples": 0.2, "pb": 0.65, "pe": 0.35}},
    })
    for m_ in s["multiplesMethods"]:
        if m_["name"] == "P/B":
            m_.update(today=pb[0], anchors=[pb[1], pb[0], pb[2]])
        if m_["name"] == "P/E":
            m_.update(today=pe[0], anchors=[pe[1], pe[0], pe[2]])
    s["multiplesWeightedToday"] = mult[0]
    for sc, v, r, x in zip(d["scenarios"], with_c, reported, npv):
        sc.update(value=v, reportedPerimeterValue=r, netModelValue=r, cessionNpvCOPm=x)
    s["scenarios"] = d["scenarios"]
    d["quote"].update(price=price, sessionDate=PRICE_DATE, source="Yahoo Finance PFDAVVNDA.CL — cierre BVC 2026-10-09",
                      url="https://finance.yahoo.com/quote/PFDAVVNDA.CL/history/", retrievedAt=NOW,
                      reverifiedAt=NOW, reverificationStatus="close-2026-10-09")
    d["assumptions"].update(terminalRoe=0.111, conservativeTerminalRoe=0.062,
                            erpNote="4,20% = base madura Damodaran jul-2026; implícita oct-2026 3,70% como sensibilidad")
    a = d["audit"]
    a["revisionDate"] = "2026-10-11"
    a["revisionStatus"] = "damodaran-r2-cession-bridge"
    a["postTransferValuationReady"] = True
    a["warnings"] = [w for w in a.get("warnings", []) if "cesión" not in w.lower() and "davibank" not in w.lower()] + [
        "Cesión DAVIbank valorada como intercambio a valor justo (VPN 0) + sinergias con 50% de realización; la contraprestación final la fija un tercero independiente.",
        f"Parte relacionada: un sobreprecio de 10% restaría ≈{cop(-overpay)} por acción.",
        "Minoría controlada (Group 98,9%): opción de OPA/desliste no ponderada; dividendos los decide el controlante.",
    ]
    add_sources(d, NEW_SOURCES + [{"role": "precio-cierre-2026-10-09", "url": "https://finance.yahoo.com/quote/PFDAVVNDA.CL/history/"}])
    note = f"""## Revisión r2 · 11-oct-2026

| Concepto | Base | Conservador | Optimista | Disrupción |
| --- | --- | --- | --- | --- |
| Perímetro reportado (COP/acción) | {cop(reported[0])} | {cop(reported[1])} | {cop(reported[2])} | {cop(reported[3])} |
| VPN cesión DAVIbank (COP/acción) | {cop(npv[0]*1e6/shares)} | {cop(npv[1]*1e6/shares)} | {cop(npv[2]*1e6/shares)} | {cop(npv[3]*1e6/shares)} |
| **Valor con cesión (piso 0)** | **{cop(with_c[0])}** | {cop(with_c[1])} | {cop(with_c[2])} | {cop(with_c[3])} |
| Probabilidad | {pct(probs[0],0)} | {pct(probs[1],0)} | {pct(probs[2],0)} | {pct(probs[3],0)} |

Esperado **{cop(expected)}**; precio 9-oct-2026 **{cop(price)}** (Yahoo Finance); Base/precio {pct(with_c[0]/price-1)}. Múltiplos 65% P/B + 35% P/E {cop(mult[0])}; combinado 80/20 {cop(comb[0])}.

1. **Cesión DAVIbank.** La SFC la autorizó el 2-oct-2026 (Res. 1505): DAVIbank cede su operación bancaria colombiana al Banco a cambio de hasta 30% de las acciones de HDI, con términos de un tercero independiente. Con Damodaran, un intercambio a valor justo tiene VPN cero; solo cuentan sinergias y costos. Sinergias del Group 0,9–1,2 billones/año desde 2028 (guía 2T26), 70% atribuibles al Banco, 50% de realización en Base (25%/75%/0% en las otras historias), 35% de impuestos y Ke terminal 18,92% ⇒ VP 1,29 billones; costos de integración después de impuestos 0,27 billones; VPN Base 1,02 billones.
2. **Parte relacionada.** Comprador y vendedor tienen el mismo controlante. Un sobreprecio de 10% en la contraprestación restaría ≈{cop(-overpay)} por acción; se muestra como sensibilidad, no en el Base.
3. **Minoría controlada y desliste.** Davivienda Group posee ≈98,9%. En 2T26 el CEO dijo que no hay decisión de desliste pero no lo descarta. El canje de 2025 se hizo a 1,39× libro (≈{cop(1.39*16879747e6/shares)} con el libro de junio); PFDAVVNDA cotiza a {f'{price/(16879747e6/shares):.2f}'.replace('.', ',')}× libro. El precio incorpora esa opción; el modelo no la pondera porque no hay oferta ni fecha.
4. **Conservadora moderada.** Crecimiento de gastos 4% (antes 4,5%): ROE terminal 6,2% en vez de 4,9%, aún muy por debajo del ROE histórico del Banco; valor {cop(reported[1])} (antes COP 2.234).
5. **Tasas.** Ke 17,66% → 18,92% (Rf COP 11,467% = TES 13,217% − spread soberano 1,75%; ERP 4,20% base madura Damodaran jul-2026; la implícita de oct-2026, 3,70%, queda como sensibilidad). Mismo corte que SURA, Argos y Davivienda Group.

*Las secciones siguientes son el informe r1 del perímetro reportado (17.387 Base); donde difieran, manda esta nota r2.*

"""
    for k in ("valuation", "research"):
        c_ = d["reports"][k]["content"]
        head, sep, body = c_.partition("\n---\n")
        head = head.replace("revision: damodaran-r3", "revision: damodaran-r3 · r2-cesion-11oct").replace(
            "post_cesion_status: contraprestacion_y_perimetro_efectivo_no_publicados",
            "post_cesion_status: puente_valor_justo_mas_sinergias")
        body = body.lstrip("\n")
        if k == "valuation":
            if body.startswith("## Revisión r2 · 11-oct-2026"):   # re-ejecución: quitar la nota anterior
                body = body.split("manda esta nota r2.*\n\n", 1)[1]
            d["reports"][k]["content"] = head + sep + "\n" + note + body
        else:
            if body.startswith("> r2 (11-oct-2026)"):
                body = body.split("\n\n", 1)[1]
            d["reports"][k]["content"] = (head + sep + "\n> r2 (11-oct-2026): valor publicado " + cop(with_c[0])
                                          + " con la cesión DAVIbank; ver Revisión r2 en la valoración.\n\n" + body)
        d["reports"][k]["importedAt"] = NOW
    d["publication"].update(revisedAt=NOW, revisionNote="r2 Damodaran: cesión DAVIbank a valor justo + sinergias, Conservadora moderada, precio 9-oct, campos del visor.")
    d["updatedAt"] = NOW
    f.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
    return dict(base=with_c[0], expected=expected, price=price, mult=mult[0], comb=comb[0], reported=reported)


# ------------------------------------------------------------------ Group
def group():
    f = ROOT / "PFDAVIGRP.CL-pfdavigrp-20261009-jmr-r3.json"
    d = json.loads(f.read_text())
    va, disc, ent = get(GROUP_ID, "'Valoración actual'!A8:P12", "'Group flujos'!J7", "'Entradas cierre'!B12:B26")
    disc = disc[0][0]
    rows = {r[0]: r for r in va}
    order = ["Base", "Conservador", "Optimista", "Disruptivo"]
    rf, erp, crp, ke0, ke1, price = ent[0][0], ent[1][0], ent[2][0], ent[7][0], ent[8][0], ent[14][0]
    pv = lambda fy3, r: fy3 / disc + r[13]
    s = d["valuationSummary"]
    R = [rows[n] for n in order]
    E = rows["Esperado"]
    pbt = [pv(r[7], r) for r in R]
    pet = [pv(r[8], r) for r in R]
    s.update({
        "base": R[0][2], "expected": E[2], "marketPrice": price, "priceDate": PRICE_DATE,
        "scopeLabel": "FCFE financiero R4 · Ke armonizado (Rf COP 11,467%, ERP 4,20%)",
        "conclusion": (f"Valor intrínseco Base R4 {cop(R[0][2])} frente a cierre {cop(price)} (9-oct): {pct(R[0][2]/price-1)}. "
                       f"Esperado {cop(E[2])}. R3 ({cop(28213)}) usaba un Ke terminal de 14,36% por conversión USD→COP; "
                       f"con el mismo corte que el Banco, Ke {pct(ke0,2)}→{pct(ke1,2)}. El precio implica ROE terminal mayor o costo de capital menor."),
        "sheetUrl": GROUP_URL,
        "multiplesWeights": {"pb": 0.65, "pe": 0.35}, "combinedWeights": {"fcfe": 0.8, "multiples": 0.2},
        "multiplesWeightedToday": R[0][9], "multiplesWeightedYear3": R[0][11],
        "multiplesWeightedYear3PV": R[0][11] / disc,
        "combinedWeightedToday": R[0][10], "combinedWeightedYear3": R[0][12],
        "combinedWeightedYear3PV": R[0][12] / disc,
        "dcfPrimaryIntrinsicPerShareCOP": R[0][2], "dcfPrimaryExpectedCOP": E[2],
        "dcfFcffIntrinsicScenarios": [{"name": n, "weight": r[1], "intrinsicPerPreferredShareCOP": r[2],
                                       "economicCOP": r[3], "residualFy3COP": r[4], "pvDistributions13COP": r[13]}
                                      for n, r in zip(order, R)],
        "valuationOutput": {
            "primarySheet": "Valoración actual", "sheetUrl": GROUP_URL, "synchronizedAt": NOW,
            "status": "FCFE financiero R4 · Ke armonizado con Banco/SURA/Argos",
            "dcfBaseCOP": R[0][2], "dcfConservativeCOP": R[1][2], "dcfOptimisticCOP": R[2][2],
            "dcfDisruptionCOP": R[3][2], "dcfExpectedCOP": E[2], "priceCOP": price,
            "dcfYear3ExDividend": None, "weights": {"dcf": 0.8, "multiples": 0.2, "pb": 0.65, "pe": 0.35}},
    })
    for m_ in s["multiplesMethods"]:
        if m_["name"].startswith("P/B"):
            m_.update(today=pbt[0], year3=R[0][7], year3PV=R[0][7] / disc, anchors=[pbt[1], pbt[0], pbt[2]])
        if m_["name"].startswith("P/E"):
            m_.update(today=pet[0], year3=R[0][8], year3PV=R[0][8] / disc, anchors=[pet[1], pet[0], pet[2]])
    for sc, r in zip(d["scenarios"], R):
        sc.update(value=r[2], year3=r[4])
    d["assumptions"].update(riskfreeRate=rf, equityRiskPremium=erp, countryRiskExposure=crp,
                            costOfEquity=ke0, terminalCostOfEquity=ke1)
    m = d["model"]
    m["ke_initial"], m["ke_terminal"] = ke0, ke1
    for res, r in zip(m["results"], R):
        res.update(dcf=r[2], economic=r[3], residual3=r[4], pvdistributions3=r[13], pb=r[5], pe=r[6],
                   pb3=r[7], pe3=r[8], multiple3=r[11], multiplepresent=r[9], combined=r[10], combined3=r[12])
    m["sensitivity_note"] = "Tabla Ke×ROE heredada de R3 (valores con Ke anterior); ver hoja «Sensibilidad cierre»."
    d["audit"]["warnings"] = d["audit"]["warnings"] + [
        "R4: Ke terminal 18,88% (antes 14,36%); el ROE terminal 14% (guía 14–16% 2028-29) ya incluye sinergias de la cesión DAVIbank, intragrupo."]
    add_sources(d, NEW_SOURCES)
    note = f"""## Revisión R4 · 11-oct-2026 · Ke armonizado

| Historia | Prob. | DCF COP/acción | Residual FY+3 | Múltiplos hoy | Combinado 80/20 |
| --- | --- | --- | --- | --- | --- |
""" + "".join(f"| {n} | {pct(r[1],0)} | {cop(r[2])} | {cop(r[4])} | {cop(r[9])} | {cop(r[10])} |\n" for n, r in zip(order, R)) + f"""| **Esperado** | 100% | **{cop(E[2])}** | {cop(E[4])} | {cop(E[9])} | {cop(E[10])} |

Precio 9-oct-2026 {cop(price)}; Base/precio {pct(R[0][2]/price-1)}.

- **Costo de capital.** R3 usaba Rf USD 5,07% + ERP 4,42% y convertía a COP con inflaciones supuestas: Ke inicial 17,68% pero terminal 14,36%, inconsistente con el Banco (18,92%). R4 usa el mismo corte que Banco Davivienda, SURA y Argos: Rf COP 11,467% (TES 13,217% − spread soberano 1,75%), ERP 4,20% (Damodaran jul-2026), CRP por cartera {pct(crp,2)}, beta 0,70 → 1,0: Ke {pct(ke0,2)} → {pct(ke1,2)}.
- **Efecto.** Base {cop(28213)} → {cop(R[0][2])}; esperado {cop(25238)} → {cop(E[2])}. Con ROE terminal 14% y Ke 18,9%, el Group no cubre su costo de capital a perpetuidad; al precio de {cop(price)} el mercado descuenta ROE más alto o Ke más bajo.
- **Cesión DAVIbank.** Es intragrupo (DAVIbank pertenece al Group), así que no crea valor por sí sola; las sinergias están dentro del ROE terminal 14% (guía 14–16%).
- La tabla Ke×ROE del modelo conserva los valores R3 como referencia.

*Las secciones siguientes son el informe R3; donde difieran, manda esta nota R4.*

"""
    c_ = d["reports"]["valuation"]["content"]
    if "## Revisión R4 · 11-oct-2026" in c_:
        c_ = c_.split("## Revisión R4 · 11-oct-2026")[0] + c_.split("manda esta nota R4.*\n\n", 1)[-1]
    first, _, rest = c_.partition("\n\n")
    d["reports"]["valuation"]["content"] = first + "\n\n" + note + rest
    r_ = d["reports"]["research"]["content"]
    if not r_.startswith("> R4"):
        d["reports"]["research"]["content"] = f"> R4 (11-oct-2026): Base {cop(R[0][2])} con Ke armonizado; ver Revisión R4 en la valoración.\n\n" + r_
    for k in ("valuation", "research"):
        d["reports"][k]["importedAt"] = NOW
    d["publication"].update(revisedAt=NOW, revisionNote="R4: Ke con el mismo corte que Banco/SURA/Argos; campos del visor.")
    d["updatedAt"] = NOW
    f.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
    return dict(base=R[0][2], expected=E[2], price=price, mult=R[0][9], comb=R[0][10], ke=(ke0, ke1))


if __name__ == "__main__":
    print("Banco", bank())
    print("Group", group())
