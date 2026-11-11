#!/usr/bin/env python3
"""Valida las entregas FASE_<N>_ENTREGA.md de revisiones Floyd R1–R6 contra los campos exigidos por
docs/CONTRATO_REBOOT_JMR.md («Entregas y continuidad»). Por defecto informa (exit 0); con --estricto falla si falta algo.
Uso: python3 scripts/validar_entregas_floyd.py [--estricto] [revision ...]"""
import re, sys, json, pathlib
RAIZ = pathlib.Path(__file__).resolve().parents[1] / "candidatos" / "valoraciones"
REQ = {  # campo → patrón (insensible a mayúsculas)
    "ticker/revisión": r"[A-Z]{1,6}-(REBOOT|FLOYD)-[A-Z0-9]+-R\d",
    "fecha": r"20\d\d-\d\d-\d\d",
    "agente/modelo": r"agente|modelo",
    "id de archivos": r"[0-9A-Za-z_-]{33,}",   # libro único: 1 libro + Doc A; heredadas: 6 archivos
    "PASOS n/n": r"PASOS[^\n]{0,40}\d+\s*/\s*\d+",
    "AISLAMIENTO": r"AISLAMIENTO\s*=\s*(OK|NO_EJECUTADO|PARCIAL)",
    "controles APROBADO/PARCIAL/NO_EJECUTADO": r"APROBADO|PARCIAL|NO_EJECUTADO",
    "siguiente paso": r"siguiente paso|pr[oó]ximo paso|siguiente",
}
def revisar(d):
    out = []
    for f in sorted(d.glob("FASE_*_ENTREGA.md")):
        t = f.read_text(encoding="utf-8")
        falta = [k for k, p in REQ.items() if not re.search(p, t, re.I)]
        out.append({"archivo": f"{d.name}/{f.name}", "faltan": falta})
    return out
if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    dirs = [RAIZ / a for a in args] if args else sorted(p for p in RAIZ.iterdir() if p.is_dir() and "-REBOOT-" in p.name)
    res = [r for d in dirs for r in revisar(d)]
    print(json.dumps(res, ensure_ascii=False, indent=1))
    tot = sum(len(r["faltan"]) for r in res)
    print(f"# {len(res)} entregas, {tot} campos ausentes", file=sys.stderr)
    sys.exit(1 if tot and "--estricto" in sys.argv else 0)
