"""Grupo Argos r5 (corte 30-sep-2026): DCF Damodaran de Cementos Argos y Celsia y SOTP intrínseco con fórmulas vivas.

Escribe la pestaña 'CO 15 DCF Damodaran' en la hoja 1cZbcnri… (no toca las demás). Cada filial: FCFF a 10 años en COP
nominales, cuatro historias (Base, Conservadora, Optimista, Disrupción), WACC con beta desapalancada del sector
(Damodaran global ene-2026), Rf COP del corte (CO 11!B38), ERP madura (CO 11!B39) y CRP de Colombia (CO 11!B41).
Consistencia de inflación (Damodaran): la inflación esperada en COP sale del diferencial de tasas libres de riesgo
(1 + Rf COP) / (1 + Rf USD) × (1 + inflación USD) − 1, y el crecimiento terminal es igual a la Rf COP, como la cartera de
EE.UU. (g = Rf). Sin foso: ROIC terminal = WACC (cemento y generación/distribución eléctrica sin ventaja demostrada).
Puente EV → patrimonio: menos deuda neta del 2T26; los minoritarios se llevan su proporción del mismo valor intrínseco
(proporción contable), no un valor de mercado; piso cero (responsabilidad limitada); × participación económica del Grupo.
SOTP intrínseco: Cementos y Celsia por DCF; Odinsa, Pactia, Sator, Summa y otros al valor fechado de 'CO 11' (sin flujos
propios) con los factores por historia de 'CO 03'; menos recompra y VP de gastos de la matriz; ÷ acciones proforma.
Uso: python3 argos_dcf_filiales.py  (cuenta de servicio de Google)
"""
import sys
from pathlib import Path

sys.path.insert(0, "/home/user/JMR-valuation")
from jmr_valuation.io.sheets_auth import get_gspread_client  # noqa: E402

SID = "1cZbcnriKIfvQX2oPgOKZUKZudSd8EcOwlh9NvjUADDo"
TAB = "CO 15 DCF Damodaran"
C11, C12, C01, C03 = "'CO 11 SOTP economico'", "'CO 12 Comparables sector'", "'CO 01 Fuentes y datos'", "'CO 03 Escenarios'"
Y = "DEFGHIJKLMN"  # años 1..10 en D..M; N = terminal
STORIES = ["Base", "Conservadora", "Optimista", "Disrupción"]

# Insumos (COP millones). Fuentes en la columna C de cada fila.
SUBS = {
    "Cementos Argos": {
        "rev": (5190000, "Ingresos UDM 2T26 ≈ FY2025 5,156 billones − 1S25 + 1S26 2,53 billones (Cementos Argos, resultados 2T26; Yahoo Finance)"),
        "m0": (0.154, "Margen EBIT UDM ≈ (EBITDA ajustado UDM ~1,25 billones − D&A ~0,45) / ingresos; EBITDA consenso FY26 1,318 billones (CO 12!B19)"),
        "bu": (0.9027205933766406, "Beta desapalancada Building Materials, Damodaran global ene-2026"),
        "de": (f"=2879000/({C01}!B12*{C01}!B14/{C12}!B21/1000000)", "Deuda bruta 2T26 2,879 billones / capitalización de mercado al corte (11.240 × acciones totales)"),
        "spread": (0.015, "Spread de deuda en COP: calificación nacional AAA; supuesto 1,5 pp sobre la Rf COP"),
        "nd": (f"={C12}!B20", "Deuda neta 2T26 (negativa = caja libre neta), CO 12!B20"),
        "nci": (f"={C12}!B56/(10530000+{C12}!B56)", "Proporción de minoritarios en el patrimonio contable (NCI 2T26 641.600 / (patrimonio controlador ~10,53 billones FY2025 + NCI)); se aplica al patrimonio intrínseco"),
        "stake": (f"={C12}!B21", "Participación económica del Grupo (CO 12!B21)"),
        "story": {"Base": (0.025, 0.17, 1.0), "Conservadora": (0.01, 0.14, 0.7), "Optimista": (0.04, 0.19, 1.4), "Disrupción": (0.0, 0.10, 0.5)},
        "story_note": "Crecimiento real años 1-5, margen EBIT objetivo (año 5) y ventas/capital marginal. Histórico: margen 14-16%, ventas/capital ~0,5 (capital invertido ~10,6 billones con exceso de capacidad); sector 10,4% y 1,74.",
    },
    "Celsia": {
        "rev": (5251000, "Ingresos UDM 2T26 = FY2025 5,395 billones − 1S25 2,764 + 1S26 2,62 billones (Celsia, resultados 2T26)"),
        "m0": (0.203, "Margen EBIT UDM ≈ (EBITDA UDM 1,506 billones = deuda neta 4,85 / 3,22× − D&A ~0,44) / ingresos"),
        "bu": (0.45529282820391, "Beta desapalancada Power, Damodaran global ene-2026"),
        "de": (f"={C12}!B25/({C01}!B13*1011329371/1000000)", "Deuda neta 2T26 4,85 billones / capitalización al corte (4.800 × 1.011.329.371 acciones)"),
        "spread": (0.02, "Spread de deuda en COP: AAA nacional con apalancamiento 3,2× EBITDA; supuesto 2,0 pp"),
        "nd": (f"={C12}!B25", "Deuda neta oficial 2T26 (CO 12!B25)"),
        "nci": (f"={C12}!B57/(3421000+{C12}!B57)", "Proporción de minoritarios en el patrimonio contable (NCI 2T26 1.761.600 / (patrimonio controlador ~3,42 billones FY2025 + NCI)); se aplica al patrimonio intrínseco"),
        "stake": (f"={C12}!B26", "Participación económica del Grupo (CO 12!B26)"),
        "story": {"Base": (0.025, 0.25, 0.55), "Conservadora": (0.01, 0.21, 0.45), "Optimista": (0.04, 0.29, 0.65), "Disrupción": (0.0, 0.16, 0.4)},
        "story_note": "Margen EBIT UDM ~20% (EBITDA 28-33% con gastos de eficiencia); la empresa apunta a un margen EBITDA > 40%. Ventas/capital histórico ~0,52; sector Power 0,57.",
    },
}


def build():
    rows = {}

    def put(r, vals):
        rows[r] = vals

    put(1, ["GRUPO ARGOS · DCF DAMODARAN DE CEMENTOS ARGOS Y CELSIA + SOTP INTRÍNSECO · corte 30-sep-2026 · COP millones"])
    put(2, ["Valor intrínseco principal del Modelo JMR (como la cartera de EE.UU.): FCFF en COP nominales con inflación consistente con la Rf COP; ROIC terminal = WACC (sin foso); g terminal = Rf COP; minoritarios en proporción al valor intrínseco; piso cero por responsabilidad limitada."])
    put(4, ["COMUNES", "Valor", "Fuente / convención"])
    put(5, ["Rf COP (TES − spread soberano)", f"={C11}!B38", "CO 11!B38: TES jul-2036 13,00% al cierre de sep-2026 − 1,75%"])
    put(6, ["ERP madura", f"={C11}!B39", "Damodaran implícita oct-2026 (igual que EE.UU.)"])
    put(7, ["CRP Colombia", f"={C11}!B41", "Damodaran jul-2026; Cementos y Celsia tienen parte en Centroamérica/Caribe (prima mayor): sensibilidad"])
    put(8, ["Rf USD (UST 10 años 30-sep-2026)", 0.0529, "Corte de la cartera de EE.UU."])
    put(9, ["Inflación esperada USD", 0.025, "Supuesto de largo plazo"])
    put(10, ["Inflación esperada COP implícita", "=(1+B5)/(1+B8)*(1+B9)-1", "Damodaran: diferencial de tasas libres de riesgo"])
    put(11, ["Tasa de impuestos", 0.33, "Colombia 35% con operaciones de menor tasa; supuesto"])
    put(12, ["Crecimiento terminal (= Rf COP)", "=B5", "Igual a la Rf, como EE.UU."])
    blocks_start = 14
    r = blocks_start
    sub_rows = {}
    for name, s in SUBS.items():
        put(r, [name.upper() + " · INSUMOS", "Valor", "Fuente"])
        lab = [("Ingresos UDM", "rev"), ("Margen EBIT UDM", "m0"), ("Beta desapalancada", "bu"), ("Deuda / patrimonio de mercado", "de"),
               ("Spread de deuda", "spread"), ("Deuda neta (− = caja neta)", "nd"), ("Proporción de minoritarios (sobre el patrimonio)", "nci"), ("Participación económica del Grupo", "stake")]
        idx = {}
        for i, (l, k) in enumerate(lab, 1):
            v, src = s[k]
            put(r + i, [l, v, src])
            idx[k] = r + i
        b = r + len(lab)
        put(b + 1, ["Beta apalancada", f"=B{idx['bu']}*(1+(1-$B$11)*B{idx['de']})", "Hamada"])
        put(b + 2, ["Costo del patrimonio (Ke)", f"=$B$5+B{b+1}*$B$6+$B$7", "Rf + β·ERP + CRP"])
        put(b + 3, ["Costo de la deuda después de impuestos", f"=($B$5+B{idx['spread']})*(1-$B$11)", ""])
        put(b + 4, ["WACC", f"=B{b+2}*(1/(1+B{idx['de']}))+B{b+3}*(B{idx['de']}/(1+B{idx['de']}))", "Constante en los 10 años y en el terminal"])
        put(b + 5, ["Historia", "Crecimiento real 1-5", "Margen EBIT objetivo", "Ventas/capital", "Probabilidad", "Nota"])
        for j, st in enumerate(STORIES):
            gr, m, sc = s["story"][st]
            put(b + 6 + j, [st, gr, m, sc, f"={C03}!{'HGIJ'[j]}14", s["story_note"] if j == 0 else ""])
        sub_rows[name] = {"idx": idx, "wacc": b + 4, "st0": b + 6}
        r = b + 11
    # bloques de DCF por filial e historia
    out = {}
    for name in SUBS:
        sr = sub_rows[name]
        out[name] = {}
        for j, st in enumerate(STORIES):
            sp = sr["st0"] + j
            put(r, [f"{name} · {st}", "", "Año 0"] + [f"Año {k}" for k in range(1, 11)] + ["Terminal"])
            R = {k: r + i for i, k in enumerate(["rev", "g", "m", "nopat", "reinv", "fcff", "df", "pv"], 1)}
            gn = f"((1+$B${sp})*(1+$B$10)-1)"
            rev = ["Ingresos", "", f"=$B${sr['idx']['rev']}"]
            g = ["Crecimiento nominal", "", ""]
            m = ["Margen EBIT", "", f"=$B${sr['idx']['m0']}"]
            for k in range(1, 11):
                col, prev = Y[k - 1], ("C" if k == 1 else Y[k - 2])
                g.append(f"={gn}" if k <= 5 else f"={gn}-({gn}-$B$12)*({k}-5)/5")
                rev.append(f"={prev}{R['rev']}*(1+{col}{R['g']})")
                m.append(f"=$C${sr['idx']['m0']}" if False else (f"=$C{R['m']}+($C${sp}-$C{R['m']})*{min(k,5)}/5"))
            g.append("=$B$12"); rev.append(f"=M{R['rev']}*(1+N{R['g']})"); m.append(f"=$C${sp}")
            nop = ["NOPAT", "", ""] + [f"={c}{R['rev']}*{c}{R['m']}*(1-$B$11)" for c in Y]
            rei = ["Reinversión", "", ""] + [f"=({c}{R['rev']}-{p}{R['rev']})/$D${sp}" for c, p in zip(Y[:10], "C" + Y[:9])] + \
                  [f"=N{R['nopat']}*$B$12/$B${sr['wacc']}"]
            fc = ["FCFF", "", ""] + [f"={c}{R['nopat']}-{c}{R['reinv']}" for c in Y]
            df = ["Factor de descuento", "", ""] + [f"=1/(1+$B${sr['wacc']})^{k}" for k in range(1, 11)] + [""]
            pv = ["VP FCFF", "", ""] + [f"={c}{R['fcff']}*{c}{R['df']}" for c in Y[:10]] + [""]
            for key, row in zip(["rev", "g", "m", "nopat", "reinv", "fcff", "df", "pv"], [rev, g, m, nop, rei, fc, df, pv]):
                put(R[key], row)
            e = R["pv"] + 1
            put(e, ["Valor terminal (ROIC terminal = WACC)", f"=N{R['fcff']}/($B${sr['wacc']}-$B$12)", "VP terminal", f"=B{e}*M{R['df']}"])
            put(e + 1, ["Valor de la operación (EV)", f"=SUM(D{R['pv']}:M{R['pv']})+D{e}", "EV / EBITDA UDM implícito",
                        f"=B{e+1}/($B${sr['idx']['rev']}*$B${sr['idx']['m0']}+{'450000' if name.startswith('Cem') else '440000'})"])
            put(e + 2, ["Patrimonio de los accionistas de la filial (piso 0)", f"=MAX(0;(B{e+1}-$B${sr['idx']['nd']})*(1-$B${sr['idx']['nci']}))", "ROIC del capital nuevo", f"=$C${sp}*(1-$B$11)*$D${sp}"])
            put(e + 3, ["Patrimonio atribuible al Grupo", f"=B{e+2}*$B${sr['idx']['stake']}", "WACC", f"=$B${sr['wacc']}"])
            out[name][st] = e + 3
            r = e + 5
    # SOTP intrínseco por historia
    put(r, ["SOTP INTRÍNSECO DAMODARAN · COP millones", "Base", "Conservadora", "Optimista", "Disrupción", "Fuente"])
    fac = {"Base": "D", "Conservadora": "C", "Optimista": "E", "Disrupción": "F"}
    lines = [("Cementos Argos · DCF", lambda st: f"=B{out['Cementos Argos'][st]}", "DCF de esta pestaña"),
             ("Celsia · DCF", lambda st: f"=B{out['Celsia'][st]}", "DCF de esta pestaña")]
    for i, (lbl, crow) in enumerate([("Odinsa (valor fechado 2T26)", 6), ("Sator", 7), ("Summa", 8), ("Pactia FCP + GP (valor de unidad 2T26)", 9),
                                     ("Otras asociadas", 10), ("Otros netos de matriz + NDU", 11)]):
        lines.append((lbl, (lambda st, crow=crow: f"={C11}!G{crow}*{C03}!{fac[st]}{crow}"), f"CO 11!G{crow} × factor de historia CO 03 fila {crow}"))
    lines.append(("Recompra y VP de gastos de matriz", lambda st: f"=({C11}!G13+{C11}!G14)*{C03}!{fac[st]}11", "CO 11!G13:G14 × factor CO 03 fila 11"))
    first = r + 1
    for i, (lbl, f, src) in enumerate(lines):
        put(r + 1 + i, [lbl] + [f(st) for st in STORIES] + [src])
    last = r + len(lines)
    put(last + 1, ["Patrimonio intrínseco del holding"] + [f"=SUM({c}{first}:{c}{last})" for c in "BCDE"] + [""])
    put(last + 2, ["VALOR INTRÍNSECO POR ACCIÓN (COP)"] + [f"={c}{last+1}*1000000/{C01}!B66" for c in "BCDE"] + ["Acciones económicas proforma tras la recompra de septiembre"])
    put(last + 3, ["Probabilidad"] + [f"={C03}!{c}14" for c in "HGIJ"] + ["CO 03 (Base 50%, Conservadora 25%, Optimista 20%, Disrupción 5%)"])
    put(last + 4, ["VALOR ESPERADO POR ACCIÓN (COP)", f"=SUMPRODUCT(B{last+2}:E{last+2};B{last+3}:E{last+3})", "", "", "", "Complemento del DCF Base"])
    put(last + 5, ["Precio de compra con MOS 35% sobre el esperado", f"=B{last+4}*(1-0,35)", "", "", "", "Igual que la cartera de EE.UU."])
    put(last + 6, ["Precio PFGRUPOARG al corte (30-sep-2026)", f"={C01}!B10", "Precio ordinaria", f"={C01}!B11", "", ""])
    put(last + 7, ["Control probabilidades", f"=SUM(B{last+3}:E{last+3})", "", "", "", "Debe ser 1"])
    return rows, {"per_share": last + 2, "expected": last + 4, "mos": last + 5, "subs": out}


def main():
    rows, ref = build()
    gc = get_gspread_client()
    sh = gc.open_by_key(SID)
    try:
        ws = sh.worksheet(TAB); ws.clear()
    except Exception:  # noqa: BLE001
        ws = sh.add_worksheet(TAB, rows=max(rows) + 10, cols=16)
    n = max(rows)
    grid = [rows.get(i, []) for i in range(1, n + 1)]
    width = max(len(x) for x in grid)
    grid = [x + [""] * (width - len(x)) for x in grid]
    ws.update(grid, "A1", value_input_option="USER_ENTERED")
    vals = ws.get(f"A{ref['per_share']}:E{ref['mos']}", value_render_option="UNFORMATTED_VALUE")
    for v in vals:
        print(v)
    for name, d in ref["subs"].items():
        print(name, [round(ws.acell(f"B{d[st]}", value_render_option='UNFORMATTED_VALUE').value) for st in STORIES])
    Path(__file__).with_suffix(".ref.json").write_text(__import__("json").dumps(ref))


if __name__ == "__main__":
    main()
