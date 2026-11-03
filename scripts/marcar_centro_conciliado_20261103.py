#!/usr/bin/env python3
"""Marca sensibilidadDCF.centroConciliado=true en valoraciones vigentes que no lo declaran,
solo si cada matriz es 5x5 numérica y su celda central reproduce el valorPrincipal (DCF Base).

Autorizado por el usuario el 3-nov-2026 para META, NVDA, INTU, DPZ y XP. Inserta dos líneas
de texto (bandera y verificación) sin reescribir el resto del JSON. Idempotente.
"""
import json, math, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REVS = ["META-20261101-A12-R1", "NVDA-20261101-A12-R1", "INTU-20261101-A12-R1", "DPZ-20261101-A1", "XP-20261031-A12-R1"]


def matrices(s):
    m = s.get("matrices")
    items = m.items() if isinstance(m, dict) else enumerate(m or [])
    for k, x in items:
        yield str(x.get("title") or x.get("nombre") or k), x.get("values") or x.get("valores")


def main():
    fallos = 0
    for rev in REVS:
        p = ROOT / "valoraciones" / f"{rev}.json"
        texto = p.read_text(encoding="utf-8")
        d = json.loads(texto)
        s, base = d["sensibilidadDCF"], d["valorPrincipal"]
        if s.get("centroConciliado") is True:
            print(f"{rev}: ya declarado, sin cambios"); continue
        tol = max(0.05, abs(base) * 1e-6)
        centros, ok = [], True
        for nombre, v in matrices(s):
            celdas = isinstance(v, list) and len(v) == 5 and all(
                isinstance(r, list) and len(r) == 5 and all(isinstance(x, (int, float)) and math.isfinite(x) for x in r) for r in v)
            if not celdas or abs(v[2][2] - base) >= tol:
                ok = False; print(f"{rev}: {nombre} NO concilia", file=sys.stderr)
            else:
                centros.append(v[2][2])
        if not ok or len(centros) < 1:
            fallos += 1; continue
        dif = max(abs(c - base) for c in centros)
        m = re.search(r'^( *)"sensibilidadDCF": \{\n( *)', texto, re.M)
        ind = m.group(2)
        nota = (f"3-nov-2026: centro de las {len(centros)} matrices = valorPrincipal {base:.6f} "
                f"(máx. |Δ| {dif:.2e}, tolerancia {tol:g}); scripts/marcar_centro_conciliado_20261103.py")
        texto = texto[:m.end()] + f'"centroConciliado": true,\n{ind}"centroConciliadoVerificacion": {json.dumps(nota, ensure_ascii=False)},\n{ind}' + texto[m.end():]
        json.loads(texto)  # el resultado sigue siendo JSON válido
        p.write_text(texto, encoding="utf-8")
        print(f"{rev}: marcado · {nota}")
    return 1 if fallos else 0


if __name__ == "__main__":
    sys.exit(main())
