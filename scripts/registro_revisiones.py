#!/usr/bin/env python3
"""Registro de revisiones y de los cinco drivers del DCF Base.

Genera, a partir de `catalogo.json`, `valoraciones/` y `candidatos/valoraciones/`:

- `registro/revisiones.json` y `registro/REVISIONES.md`: por emisor, la revisión
  VIGENTE (la que figura en el catálogo) y las SUSTITUIDAS (candidatas o
  valoraciones anteriores del mismo emisor). Las sustituidas se conservan como
  evidencia; no son insumo de revisiones nuevas (REGLAS_VIGENTES §10).
- `registro/drivers.json` y `registro/DRIVERS.md`: por revisión, los drivers de
  la historia Base (crecimiento años 1-5, margen terminal, Sales-to-Capital,
  WACC/Ke, g terminal y ROIC/ROE terminal) y su variación frente a la revisión
  anterior del mismo emisor.

Reglas: solo lee campos estructurados de los JSON; nunca extrae cifras de texto
libre ni rellena huecos. Un driver ausente queda como null (N/D en el .md) y
cada valor registra el campo de origen. No modifica valoraciones ni catálogo.

Uso:
  python3 scripts/registro_revisiones.py          # regenera registro/
  python3 scripts/registro_revisiones.py --check  # falla si registro/ está
                                                  # desactualizado o si un emisor
                                                  # no tiene exactamente 1 vigente
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "registro"

# driver -> lista de (ruta, etiqueta). Se toma el primer campo presente y no nulo.
# Rutas que empiezan por "base." se leen en la historia Base; "raiz." en el JSON.
DRIVERS = {
    "crecimiento_1_5": [
        ("base.crecimientoCAGR1a5", "CAGR ventas 1-5"),
        ("base.crecimiento", "crecimiento (esquema anterior)"),
        ("base.crecimientoNIprimeros5", "crecimiento utilidad 1-5 (financiera)"),
    ],
    "margen_terminal": [
        ("base.margenTerminal", "margen EBIT terminal"),
        ("base.margen", "margen EBIT objetivo (esquema anterior)"),
    ],
    "sales_to_capital_1_5": [
        ("base.ventasACapital1a5", "S/C 1-5"),
        ("base.s2c", "S/C 1-5 (esquema anterior)"),
    ],
    "sales_to_capital_6_10": [
        ("base.ventasACapital6a10", "S/C 6-10"),
        ("base.s2c610", "S/C 6-10 (esquema anterior)"),
    ],
    "costo_capital": [
        ("raiz.tasas.wacc", "WACC inicial"),
        ("base.wacc", "WACC (historia Base)"),
        ("base.Ke", "Ke (financiera)"),
    ],
    "g_terminal": [
        ("base.gTerminal", "g terminal"),
        ("base.terminalGrowth", "g terminal (esquema anterior)"),
    ],
    "rentabilidad_terminal": [
        ("base.roicTerminal", "ROIC terminal"),
        ("base.ROEterminal", "ROE terminal (financiera)"),
    ],
}
ETIQUETAS = {
    "crecimiento_1_5": "Crec. 1-5",
    "margen_terminal": "Margen term.",
    "sales_to_capital_1_5": "S/C 1-5",
    "sales_to_capital_6_10": "S/C 6-10",
    "costo_capital": "WACC/Ke",
    "g_terminal": "g term.",
    "rentabilidad_terminal": "ROIC/ROE term.",
}
PORCENTAJES = {"crecimiento_1_5", "margen_terminal", "costo_capital", "g_terminal", "rentabilidad_terminal"}
FECHA_RE = re.compile(r"-(\d{8})-")


def leer(p: Path):
    return json.loads(p.read_text(encoding="utf-8"))


def historia_base(d: dict):
    ve = d.get("valorEsperado")
    hs = ve.get("historias") if isinstance(ve, dict) else None
    if not isinstance(hs, list):
        hs = d.get("historias") if isinstance(d.get("historias"), list) else []
    for h in hs:
        if isinstance(h, dict) and (h.get("id") == "A" or str(h.get("nombre", "")).lower().startswith("base")):
            return h
    return None


def obtener(d: dict, base: dict | None, ruta: str):
    origen, *partes = ruta.split(".")
    o = base if origen == "base" else d
    for p in partes:
        if not isinstance(o, dict):
            return None
        o = o.get(p)
    return o if isinstance(o, (int, float)) and not isinstance(o, bool) else None


def drivers_de(d: dict) -> tuple[dict, dict]:
    base = historia_base(d)
    valores, origen = {}, {}
    for k, rutas in DRIVERS.items():
        valores[k], origen[k] = None, None
        for ruta, etiqueta in rutas:
            v = obtener(d, base, ruta)
            if v is not None:
                valores[k], origen[k] = v, f"{ruta} ({etiqueta})"
                break
    return valores, origen


def revision_id(d: dict, p: Path) -> str:
    return d.get("revisionId") or d.get("revision_id") or (p.parent.name if p.name.startswith("VALORACION") else p.stem)


def fecha(rev: str) -> str:
    m = FECHA_RE.search(rev + "-")
    return m.group(1) if m else ""


def orden(d: dict, rev: str) -> tuple[str, str]:
    """(fecha de revisión, fecha de análisis) en AAAA-MM-DD; los JSON no traen hora."""
    fr = d.get("fechaRevision") or d.get("fecha") or d.get("fecha_corte") or ""
    if not fr and fecha(rev):
        f = fecha(rev)
        fr = f"{f[:4]}-{f[4:6]}-{f[6:]}"
    return (str(fr), str(d.get("fecha") or fr))


def recolectar():
    cat = leer(ROOT / "catalogo.json")
    vigentes = {}
    for rel in cat["valoraciones"]:
        d = leer(ROOT / rel)
        vigentes[d["ticker"]] = revision_id(d, ROOT / rel)

    revisiones = {}  # revision_id -> registro
    fuentes = sorted((ROOT / "valoraciones").glob("*.json")) + sorted(
        (ROOT / "candidatos" / "valoraciones").glob("*/VALORACION_*.json"))
    for p in fuentes:
        try:
            d = leer(p)
        except (json.JSONDecodeError, UnicodeDecodeError):
            continue
        t = d.get("ticker")
        if not t:
            continue
        rev = revision_id(d, p)
        rel = p.relative_to(ROOT).as_posix()
        if rev in revisiones:  # misma revisión en valoraciones/ y candidatos/
            revisiones[rev]["rutas"].append(rel)
            continue
        valores, origen = drivers_de(d)
        revisiones[rev] = {
            "ticker": t, "revisionId": rev, "fecha": orden(d, rev)[0], "_orden": orden(d, rev), "rutas": [rel],
            "metodo": d.get("version_metodo") or d.get("metodo_valoracion"),
            "metodoPrincipal": d.get("metodoPrincipal"),
            "valorPrincipal": d.get("valorPrincipal"),
            "drivers": valores, "origen": origen,
        }
    for r in revisiones.values():
        r["estado"] = "VIGENTE" if vigentes.get(r["ticker"]) == r["revisionId"] else "SUSTITUIDA"
        r["rutas"].sort()
    return vigentes, revisiones


def construir():
    vigentes, revisiones = recolectar()
    por_ticker: dict[str, list] = {}
    for r in revisiones.values():
        por_ticker.setdefault(r["ticker"], []).append(r)
    for lst in por_ticker.values():
        # La vigente es la más reciente de su día; entre sustituidas con las mismas
        # fechas no hay forma de saber cuál fue antes, así que no se compara.
        lst.sort(key=lambda r: (r["_orden"][0], r["estado"] == "VIGENTE", r["_orden"][1], r["revisionId"]))
        for i, r in enumerate(lst):
            previo = lst[i - 1] if i else None
            # Ambiguo si el previo empata en fechas con la propia revisión (dos
            # sustituidas del mismo día) o con otra sustituida anterior.
            empate = [x for x in lst[:i] if previo and x["_orden"] == previo["_orden"]]
            r["ordenAmbiguo"] = bool(previo and (
                (r["estado"] != "VIGENTE" and r["_orden"] == previo["_orden"]) or len(empate) > 1))
            if r["ordenAmbiguo"]:
                previo = None
            r["anterior"] = previo["revisionId"] if previo else None
            r["variacion"] = {
                k: (r["drivers"][k] - previo["drivers"][k])
                if previo and r["drivers"][k] is not None and previo["drivers"][k] is not None else None
                for k in DRIVERS
            }

    reg_rev = {
        "descripcion": "Revisión VIGENTE (catálogo) y SUSTITUIDAS por emisor. Las sustituidas se conservan como evidencia y no son insumo de revisiones nuevas (REGLAS_VIGENTES §10). Generado por scripts/registro_revisiones.py; no editar a mano.",
        "emisores": {
            t: {"vigente": vigentes.get(t),
                "sustituidas": [r["revisionId"] for r in lst if r["estado"] == "SUSTITUIDA"],
                "rutas": {r["revisionId"]: r["rutas"] for r in lst}}
            for t, lst in sorted(por_ticker.items())
        },
    }
    reg_drv = {
        "descripcion": "Drivers de la historia Base por revisión, leídos solo de campos estructurados (null = N/D, sin rellenar). 'origen' indica el campo de cada valor; 'variacion' es la diferencia frente a la revisión anterior del mismo emisor. Generado por scripts/registro_revisiones.py; no editar a mano.",
        "revisiones": [
            {k: r[k] for k in ("ticker", "revisionId", "estado", "fecha", "anterior", "ordenAmbiguo", "metodo", "metodoPrincipal",
                               "valorPrincipal", "drivers", "variacion", "origen")}
            for t in sorted(por_ticker) for r in por_ticker[t]
        ],
    }
    return reg_rev, reg_drv, por_ticker


def fmt(k, v):
    if v is None:
        return "N/D"
    return f"{v * 100:.1f} %" if k in PORCENTAJES else f"{v:.2f}"


def fmt_var(k, v):
    if v is None:
        return ""
    return f" ({v * 100:+.1f} pp)" if k in PORCENTAJES else f" ({v:+.2f})"


def markdown(reg_rev, por_ticker):
    rev_md = ["# Registro de revisiones por emisor", "",
              "Generado por `scripts/registro_revisiones.py` desde `catalogo.json`. **No editar a mano.**", "",
              "- **VIGENTE**: la revisión que figura en el catálogo. Es la única base para trabajar.",
              "- **SUSTITUIDA**: revisión anterior del mismo emisor. Se conserva como evidencia (no se borra ni se mueve: pruebas y fichas la referencian), pero **no es insumo** de revisiones nuevas (REGLAS_VIGENTES §10).", "",
              "| Emisor | Vigente | Sustituidas |", "|---|---|---|"]
    for t, e in reg_rev["emisores"].items():
        rev_md.append(f"| {t} | {e['vigente'] or '— (fuera del catálogo)'} | {', '.join(e['sustituidas']) or '—'} |")

    drv_md = ["# Registro de drivers del DCF Base", "",
              "Generado por `scripts/registro_revisiones.py`. **No editar a mano.** Valores de la historia Base leídos solo de campos estructurados de cada JSON; **N/D** = el campo no existe en ese esquema (no se rellena ni se extrae de texto). Entre paréntesis, la variación frente a la revisión anterior del mismo emisor (orden por fecha de revisión; la vigente es la última). **⚠ orden ambiguo**: varias revisiones sustituidas comparten fecha y no se puede saber cuál fue antes, así que no se calcula variación. En financieras (FCFE) el costo de capital es Ke y la rentabilidad terminal es ROE. El campo exacto de cada cifra está en `drivers.json` → `origen`.", ""]
    for t in sorted(por_ticker):
        drv_md += [f"## {t}", "",
                   "| Revisión | Estado | Valor Base | " + " | ".join(ETIQUETAS.values()) + " |",
                   "|---|---|---|" + "---|" * len(ETIQUETAS)]
        for r in por_ticker[t]:
            vb = r["valorPrincipal"]
            celdas = [fmt(k, r["drivers"][k]) + fmt_var(k, r["variacion"][k]) for k in DRIVERS]
            est = r["estado"] + (" ⚠ orden ambiguo" if r["ordenAmbiguo"] else "")
            drv_md.append(f"| {r['revisionId']} | {est} | {vb:.2f} | " if isinstance(vb, (int, float)) else
                          f"| {r['revisionId']} | {est} | N/D | ")
            drv_md[-1] += " | ".join(celdas) + " |"
        drv_md.append("")
    return "\n".join(rev_md) + "\n", "\n".join(drv_md)


def salidas():
    reg_rev, reg_drv, por_ticker = construir()
    rev_md, drv_md = markdown(reg_rev, por_ticker)
    dump = lambda o: json.dumps(o, ensure_ascii=False, indent=2) + "\n"
    return {
        "revisiones.json": dump(reg_rev), "REVISIONES.md": rev_md,
        "drivers.json": dump(reg_drv), "DRIVERS.md": drv_md,
    }, reg_rev


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true", help="verifica sin escribir")
    a = ap.parse_args()
    archivos, reg_rev = salidas()
    errores = []
    for t, e in reg_rev["emisores"].items():
        if e["vigente"] and e["vigente"] not in e["rutas"]:
            errores.append(f"{t}: la vigente {e['vigente']} del catálogo no se encontró en valoraciones/ ni candidatos/")
    if a.check:
        for nombre, contenido in archivos.items():
            p = OUT / nombre
            if not p.exists() or p.read_text(encoding="utf-8") != contenido:
                if p.exists() and nombre in ("DRIVERS.md", "drivers.json"):
                    import difflib
                    actual = p.read_text(encoding="utf-8")
                    print(f"DIFERENCIA EXACTA {nombre}:", file=sys.stderr)
                    print("".join(difflib.unified_diff(actual.splitlines(keepends=True), contenido.splitlines(keepends=True), fromfile="en-repositorio", tofile="generado")), file=sys.stderr)
                errores.append(f"registro/{nombre} desactualizado: ejecutar python3 scripts/registro_revisiones.py")
    else:
        OUT.mkdir(exist_ok=True)
        for nombre, contenido in archivos.items():
            (OUT / nombre).write_text(contenido, encoding="utf-8")
    for e in errores:
        print("ERROR:", e, file=sys.stderr)
    if not errores:
        n = len(reg_rev["emisores"])
        s = sum(len(e["sustituidas"]) for e in reg_rev["emisores"].values())
        print(f"OK: {n} emisores, {s} revisiones sustituidas" + (" (registro al día)" if a.check else " · registro/ regenerado"))
    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main())
