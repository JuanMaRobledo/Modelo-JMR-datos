#!/usr/bin/env python3
"""Migración idempotente y limitada a precios de corte históricos ADBE/ONON.

No altera DCF, métodos, ponderaciones, supuestos, fechas, ni referencias al análisis.
Conserva el precio legado y su fuente en un campo separado.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CASES = {
    "ADBE": {
        "file": "valoraciones/ADBE-1789572982820.json",
        "revision": "ADBE-REC-20261027-R1",
        "precio_corte": 239.94,
        "precio_heredado": 251.67,
        "nota": "Referencia de análisis anterior del 15-oct-2026; no pertenece al corte 30-sep-2026.",
    },
    "ONON": {
        "file": "valoraciones/ONON-1790595640519.json",
        "revision": "ONON-REC-20261027-R1",
        "precio_corte": 29.61,
        "precio_heredado": 30.20,
        "nota": "Referencia guardada 6-oct-2026 sin fecha de cotización confirmada; no es el corte 30-sep-2026.",
    },
}


def migrate(case: dict, *, apply: bool) -> str:
    path = ROOT / case["file"]
    old_text = path.read_text(encoding="utf-8")
    data = json.loads(old_text)

    if data.get("revisionId") != case["revision"]:
        raise ValueError(f"{path}: revisión cambió; se detiene sin mutaciones")
    if data.get("fecha") != "2026-09-30" or data.get("precio") != case["precio_corte"]:
        raise ValueError(f"{path}: corte/insumo no coincide; se detiene")
    if data.get("precioAnalisis") == case["precio_corte"]:
        legacy = data.get("precioAnalisisHistorico")
        if isinstance(legacy, dict) and legacy.get("valor") == case["precio_heredado"]:
            return f"YA_CONCILIADO {case['file']}"
        raise ValueError(f"{path}: precio ya cambió sin rastro histórico esperado")
    if data.get("precioAnalisis") != case["precio_heredado"]:
        raise ValueError(f"{path}: precioAnalisis cambió; no reemplazar")

    old_source = data.get("precioReferenciaFuente")
    if not isinstance(old_source, str) or not old_source:
        raise ValueError(f"{path}: falta fuente anterior")

    # Sustituciones textuales acotadas, sin reserializar las ~500 KB de cada registro.
    m = re.search(r'(?m)^(?P<indent>\s*)"precioAnalisis":\s*(?P<value>[0-9]+(?:\.[0-9]+)?),\s*$', old_text)
    if not m or float(m.group("value")) != case["precio_heredado"]:
        raise ValueError(f"{path}: ubicación única de precioAnalisis no verificada")
    indent = m.group("indent")
    legacy = {"valor": case["precio_heredado"], "fuenteAnterior": old_source,
              "observacion": case["nota"], "fechaRegistro": "2026-10-27"}
    audit = {"fecha": "2026-10-27", "estado": "CONCILIADO_METADATOS",
             "revision": case["revision"], "precioCorte": case["precio_corte"],
             "fechaCorte": "2026-09-30", "cambioValorIntrinseco": False}
    new_price_block = (
        indent + '"precioAnalisis": ' + json.dumps(case["precio_corte"]) + ',\n'
        + indent + '"precioAnalisisHistorico": ' + json.dumps(legacy, ensure_ascii=False) + ',\n'
        + indent + '"conciliacionPrecioCorte": ' + json.dumps(audit, ensure_ascii=False) + ','
    )
    text = old_text[:m.start()] + new_price_block + old_text[m.end():]

    source_pattern = r'(?m)^(?P<indent>\s*)"precioReferenciaFuente":\s*"(?:\\.|[^"\\])*"'
    source_match = re.search(source_pattern, text)
    if not source_match:
        raise ValueError(f"{path}: ubicación fuente no verificada")
    new_source = "Precio del corte del 30-sep-2026, comprobado en Input sheet!D1 y Resumen de Valoración!C25; no cotización en vivo."
    text = text[:source_match.start()] + (source_match.group("indent") +
        '"precioReferenciaFuente": ' + json.dumps(new_source, ensure_ascii=False)) + text[source_match.end():]

    check = json.loads(text)
    for key in ("valorPrincipal", "metodos", "valorEsperado", "descuentoMultiples",
                "objetivoPonderado", "salvedades", "revisionId", "fecha", "mos"):
        if check.get(key) != data.get(key):
            raise ValueError(f"{path}: cambio económico inesperado en {key}")
    if check["precioAnalisis"] != check["precio"] or check["precioAnalisisHistorico"]["valor"] != case["precio_heredado"]:
        raise ValueError(f"{path}: migración no consistente")
    if apply:
        path.write_text(text, encoding="utf-8")
    return ("ACTUALIZADO " if apply else "REVISADO_EN_SECO ") + case["file"]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    opts = parser.parse_args()
    for case in CASES.values():
        print(migrate(case, apply=opts.apply))


if __name__ == "__main__":
    main()
