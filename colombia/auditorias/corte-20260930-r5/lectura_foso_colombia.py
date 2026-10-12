"""Lectura «Damodaran por defecto» y foso de las valoraciones de Colombia (r5, corte 30-sep-2026), como en EE.UU.

Regla de la cartera (reference/moat_2026-09-30.json de JMR-valuation): sin ventaja defendible → el retorno terminal
(ROIC en industriales, ROE en financieras) converge al costo de capital. Aquí se registra, por expediente, la
clasificación, el retorno terminal del modelo frente al Ke/WACC terminal y el valor si el retorno terminal = costo de
capital («sin foso»). En Colombia varias historias suponen ROE terminal POR DEBAJO del Ke (destrucción de valor
perpetua), más conservador que la regla; la lectura lo hace visible sin cambiar el Base.
Valores leídos de las hojas el 12-oct-2026 (pruebas en celdas restauradas):
  - PFDAVIGRP: 'Entradas cierre'!E42 (ROE terminal Base 14%) = Ke terminal → 'Valoración actual'!C8 = 27.892.
  - SURA: pestaña 'Damodaran · ROE terminal Ke' (las tres participadas con ROE terminal = Ke) = 51.516.
  - PFDAVVNDA: aproximación con el motor terminal ('Terminal regulatorio' y 'Convergencia terminal'): con ROE = Ke el
    valor terminal residual es cero → se suma −VP(TV RE) = (libro FY10 − FCFE11/(Ke − g)) / (1 + Ke)^10 por acción.
  - PFGRUPOARG: el DCF ya usa ROIC terminal = WACC; «sin foso» = Base.
Uso: python3 lectura_foso_colombia.py
"""
import json
from pathlib import Path

P = Path(__file__).resolve().parent
EXP = P.parents[1] / "expedientes"
res = json.loads((P / "resultados_r5.json").read_text())

# Banco: aproximación desde el motor terminal (COP millones)
ke, g, fcfe11, book10, shares = 0.18207848126845605, 0.04, 2781083.628125147, 35326725.61831179, 487670413
tv_re = fcfe11 / (ke - g) - book10
banco_sinfoso = res["PFDAVVNDA.CL"]["base"] - tv_re / (1 + ke) ** 10 * 1e6 / shares

REG = {
    "PFDAVVNDA.CL": {"ventaja": "sin ventaja defendible", "retornoTerminal": {"tipo": "ROE", "modelo": 0.123, "costoCapital": ke},
                     "dcfSinFoso": banco_sinfoso, "metodoSinFoso": "aproximación: valor terminal residual = 0 (ROE terminal = Ke)",
                     "preguntas": "(1) ROE ~12% < Ke 18,2%: falla; (2) escala y franquicia local, sin rentas por encima del costo; (3) no aplica",
                     "nota": "El modelo supone ROE terminal 12,3% < Ke 18,2% (destrucción de valor perpetua), más conservador que la regla de la cartera."},
    "PFDAVIGRP.CL": {"ventaja": "sin ventaja defendible", "retornoTerminal": {"tipo": "ROE", "modelo": 0.14, "costoCapital": 0.1816796694435953},
                     "dcfSinFoso": 27892.27900815021, "metodoSinFoso": "hoja: 'Entradas cierre'!E42 = Ke terminal (celda restaurada)",
                     "preguntas": "(1) ROE 12-15% < Ke 18,2%: falla; (2) sin ventaja identificable que dé rentas; (3) no aplica",
                     "nota": "ROE terminal Base 14% (guía 14-16% 2028-29) < Ke terminal 18,2%."},
    "PFGRUPSURA.CL": {"ventaja": "mixta: Cibest con ventaja de escala; SURA AM y Suramericana sin ventaja defendible",
                      "retornoTerminal": {"tipo": "ROE", "modelo": {"Cibest": 0.17, "SURA AM": 0.14, "Suramericana": 0.135},
                                          "costoCapital": {"Cibest": 0.1693, "SURA AM": 0.1629, "Suramericana": 0.1618}},
                      "dcfSinFoso": 51515.96019711213, "metodoSinFoso": "hoja: 'Damodaran · ROE terminal Ke' (las tres a Ke)",
                      "preguntas": "Cibest: (1) ROE 20,8% > Ke 16,9%, (2) escala y costo de fondeo, (3) sin erosión visible → durable. SURA AM y Suramericana: (1) ROE 12-14% < Ke → falla",
                      "nota": "SURA AM y Suramericana con ROE terminal por debajo del Ke; la regla de la cartera los llevaría al Ke."},
    "PFGRUPOARG.CL": {"ventaja": "sin ventaja defendible", "retornoTerminal": {"tipo": "ROIC", "modelo": "= WACC", "costoCapital": {"Cementos Argos": 0.1617, "Celsia": 0.1283}},
                      "dcfSinFoso": res["PFGRUPOARG.CL"]["base"], "metodoSinFoso": "el DCF ya usa ROIC terminal = WACC",
                      "preguntas": "(1) ROIC Cementos ~7% y Celsia ~8% < WACC en COP: falla; (2) cemento y generación/distribución sin ventaja demostrada",
                      "nota": "Sin foso en el Base: el valor ya es el de la regla."},
}
REG["GRUPOSURA.CL"] = REG["PFGRUPSURA.CL"]
(P / "foso_colombia.json").write_text(json.dumps({"fecha": "2026-10-12", "regla": "Igual que reference/moat_2026-09-30.json de la cartera de EE.UU.: sin ventaja defendible → retorno terminal = costo de capital.", "empresas": REG}, ensure_ascii=False, indent=1))

FILES = {"PFDAVVNDA.CL": ("PFDAVVNDA.CL-pfdavvnda-20261009-jmr-r1.json", 2, True), "PFDAVIGRP.CL": ("PFDAVIGRP.CL-pfdavigrp-20261009-jmr-r3.json", 2, True),
         "PFGRUPSURA.CL": ("PFGRUPSURA.CL-pfgrupsura-20261010-damodaran-jmr.json", 1, False), "GRUPOSURA.CL": ("GRUPOSURA.CL-gruposura-20261010-damodaran-jmr.json", 1, False),
         "PFGRUPOARG.CL": ("PFGRUPOARG.CL-pfgrupoarg-20261009-clean-master.json", 1, False)}
for tk, (fn, ind, nl) in FILES.items():
    f = EXP / fn
    d = json.loads(f.read_text())
    r = REG[tk]
    d["lecturaDamodaran"] = {"fecha": "2026-10-12", "fuente": "colombia/auditorias/corte-20260930-r5/foso_colombia.json",
                             "foso": r["ventaja"], "retornoTerminal": r["retornoTerminal"], "dcfBase": res[tk]["base"],
                             "dcfSinFoso": r["dcfSinFoso"], "metodoSinFoso": r["metodoSinFoso"], "preguntas": r["preguntas"],
                             "nota": "Contraste, no una historia: «sin foso» = retorno terminal igual al costo de capital (regla de la cartera). " + r["nota"]}
    f.write_text(json.dumps(d, ensure_ascii=False, indent=ind) + ("\n" if nl else ""))
    print(tk, r["ventaja"], round(res[tk]["base"]), "→ sin foso", round(r["dcfSinFoso"]))
