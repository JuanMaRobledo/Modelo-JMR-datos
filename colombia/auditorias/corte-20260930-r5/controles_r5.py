"""Controles r5 de los expedientes de Colombia (como consistencia_app.py de la cartera de EE.UU.).

Por expediente: valor principal = intrínseco y coincide con la hoja; esperado = Σ probabilidad × historia; probabilidades
suman 100%; precio de compra = esperado × 65%; ponderado secundario = 40% DCF + 60% múltiplos; corte 30-sep-2026 y ERP
3,70%; nota r5 en los dos informes; lectura Damodaran presente. Lee la hoja para el DCF Base. Sale con 1 si algo falla.
Uso: python3 controles_r5.py
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, "/home/user/JMR-valuation")
from jmr_valuation.io.sheets_auth import get_gspread_client  # noqa: E402

P = Path(__file__).resolve().parent
EXP = P.parents[1] / "expedientes"
ref = json.loads((P / "argos_dcf_filiales.ref.json").read_text())
SHEET = {"PFDAVVNDA.CL": ("16smCZh7JIB3om_UabhiFymPElK6zyq_6Z8iY-P4Kgrs", "'Cesión Davibank'!D59"),
         "PFDAVIGRP.CL": ("1ogP8LfxEBxslOeC6Avgk2BAClJ_0cfzpgJ06icvVSys", "'Valoración actual'!C8"),
         "PFGRUPSURA.CL": ("1Nb9_T6n8xbJikr68TN5MA5bIIiwm0aKrsF7m4MmOHyM", "Resumen!B14"),
         "GRUPOSURA.CL": ("1Nb9_T6n8xbJikr68TN5MA5bIIiwm0aKrsF7m4MmOHyM", "Resumen!B14"),
         "PFGRUPOARG.CL": ("1cZbcnriKIfvQX2oPgOKZUKZudSd8EcOwlh9NvjUADDo", f"'CO 15 DCF Damodaran'!B{ref['per_share']}")}
FILES = ["PFDAVVNDA.CL-pfdavvnda-20261009-jmr-r1.json", "PFDAVIGRP.CL-pfdavigrp-20261009-jmr-r3.json",
         "PFGRUPSURA.CL-pfgrupsura-20261010-damodaran-jmr.json", "GRUPOSURA.CL-gruposura-20261010-damodaran-jmr.json",
         "PFGRUPOARG.CL-pfgrupoarg-20261009-clean-master.json"]
gc = get_gspread_client()
fallos = 0
for fn in FILES:
    d = json.loads((EXP / fn).read_text())
    t, s = d["ticker"], d["valuationSummary"]
    sid, cell = SHEET[t]
    hoja = gc.open_by_key(sid).values_get(cell, params={"valueRenderOption": "UNFORMATTED_VALUE"})["values"][0][0]
    sc = d["scenarios"]
    exp = sum(x["probability"] * x["value"] for x in sc)
    c = {
        "principal intrínseco": s.get("baseIsIntrinsic") is True and abs(s["primaryValueCOP"] - s["base"]) < 1e-6,
        "base = hoja": abs(s["base"] - hoja) < 0.01,
        "base = historia Base": abs(sc[0]["value"] - s["base"]) < 1e-6,
        "probs = 100": abs(sum(x["probability"] for x in sc) - 1) < 1e-9,
        "esperado = suma": abs(exp - s["expected"]) < 0.01,
        "MOS 35% sobre esperado": abs(s["precioMOS"] - 0.65 * s["expected"]) < 0.01 and s.get("mos") == 0.35,
        "ponderado 40/60": abs(s["combinedWeightedToday"] - (0.4 * s["base"] + 0.6 * s["multiplesWeightedToday"])) < 0.01,
        "corte 30-sep": s.get("priceDate") == "2026-09-30" and d["quote"].get("sessionDate") == "2026-09-30",
        "ERP 3,70%": abs(d["assumptions"]["equityRiskPremium"] - 0.037) < 1e-9,
        "VO = esperado": abs(s["valuationOutput"]["dcfExpectedCOP"] - s["expected"]) < 0.01,
        "nota r5 en informes": all(("## Revisión r5 · corte" in d["reports"][k]["content"]) or ("revision: r6" in d["reports"][k]["content"]) for k in ("valuation", "research")),
        "lectura Damodaran": isinstance(d.get("lecturaDamodaran", {}).get("dcfSinFoso"), (int, float)),
    }
    bad = [k for k, v in c.items() if not v]
    fallos += len(bad)
    print(f"{t:14s} {len(c)-len(bad)}/{len(c)}", bad or "")
print("FALLOS", fallos)
sys.exit(1 if fallos else 0)
