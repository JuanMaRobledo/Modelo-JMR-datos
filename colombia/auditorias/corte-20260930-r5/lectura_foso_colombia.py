"""(r6) Lectura «Damodaran por defecto» y foso de las valoraciones de Colombia (r5, corte 30-sep-2026), como en EE.UU.

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

# r6 (12-oct-2026): ROE terminal = Ke aplicado en las hojas del Banco, Group y SURA (respaldo_roe_ke.json): el Base ya es «sin foso».
# «antes» = valor con el ROE terminal del modelo anterior (r5), medido en la misma hoja antes del cambio.
REG = {
    "PFDAVVNDA.CL": {"ventaja": "sin ventaja defendible", "retornoTerminal": {"tipo": "ROE", "modelo": "= Ke", "costoCapital": 0.18207848126845605},
                     "antes": 20663, "metodoSinFoso": "Terminal regulatorio: TV RE = 0 y TV DDM = libro FY10 (J6:K9)",
                     "preguntas": "(1) ROE ~12% < Ke 18,2%: falla; (2) escala y franquicia local, sin rentas por encima del costo; (3) no aplica",
                     "nota": "ROE terminal = Ke desde r6; antes el modelo suponía 12,3% < Ke 18,2%."},
    "PFDAVIGRP.CL": {"ventaja": "sin ventaja defendible", "retornoTerminal": {"tipo": "ROE", "modelo": "= Ke", "costoCapital": 0.1816796694435953},
                     "antes": 23160, "metodoSinFoso": "hoja: 'Entradas cierre'!E42:E45 = Ke terminal",
                     "preguntas": "(1) ROE 12-15% < Ke 18,2%: falla; (2) sin ventaja identificable que dé rentas; (3) no aplica",
                     "nota": "ROE terminal = Ke desde r6; antes 14% (Base), 11%, 16% y 10%."},
    "PFGRUPSURA.CL": {"ventaja": "mixta: Cibest con ventaja de escala; SURA AM y Suramericana sin ventaja defendible",
                      "retornoTerminal": {"tipo": "ROE", "modelo": "= Ke estable en las tres y en las cuatro historias", "costoCapital": {"Cibest": 0.1804, "SURA AM": 0.1722, "Suramericana": 0.1744}},
                      "antes": 45136, "metodoSinFoso": "hoja: Supuestos!D15:D26 = Ke estable; inversión nueva = Ke (Cibest ya no +1pp)",
                      "preguntas": "Cibest: (1) ROE 20,8% > Ke 16,9%, (2) escala y costo de fondeo, (3) sin erosión visible → durable por regla, pero r6 aplica ROE = Ke por instrucción del analista. SURA AM y Suramericana: (1) ROE 12-14% < Ke → falla",
                      "nota": "ROE terminal = Ke en las tres participadas (r6); antes 17/14/13,5% (Base) y +1pp de Cibest."},
    "PFGRUPOARG.CL": {"ventaja": "sin ventaja defendible", "retornoTerminal": {"tipo": "ROIC", "modelo": "= WACC", "costoCapital": {"Cementos Argos": 0.1617, "Celsia": 0.1283}},
                      "antes": 10346, "metodoSinFoso": "el DCF ya usa ROIC terminal = WACC",
                      "preguntas": "(1) ROIC Cementos ~7% y Celsia ~8% < WACC en COP: falla; (2) cemento y generación/distribución sin ventaja demostrada",
                      "nota": "Sin foso en el Base: el valor ya es el de la regla."},
}
for k in REG:
    REG[k]["dcfSinFoso"] = res[k]["base"]
REG["GRUPOSURA.CL"] = REG["PFGRUPSURA.CL"]
(P / "foso_colombia.json").write_text(json.dumps({"fecha": "2026-10-12", "regla": "Igual que reference/moat_2026-09-30.json de la cartera de EE.UU.: sin ventaja defendible → retorno terminal = costo de capital. Aplicado al Base en r6.", "empresas": REG}, ensure_ascii=False, indent=1))

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
                             "valorAntesR6": r["antes"], "nota": "r6: el Base ya aplica «sin foso» (retorno terminal = costo de capital, regla de la cartera). " + r["nota"]}
    f.write_text(json.dumps(d, ensure_ascii=False, indent=ind) + ("\n" if nl else ""))
    print(tk, r["ventaja"], round(res[tk]["base"]), "→ sin foso", round(r["dcfSinFoso"]))
