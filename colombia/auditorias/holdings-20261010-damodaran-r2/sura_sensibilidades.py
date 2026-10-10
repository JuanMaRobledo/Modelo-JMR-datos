"""Sensibilidades univariantes del modelo SURA (réplica independiente). No se suman entre sí."""
import json, importlib
import sura_modelo as M

def base():
    r = M.compute(); b = r["stories"]["Base"]
    return b["intrinsicRE"], b["blend"]

def run(label, mutate, **kw):
    importlib.reload(M); mutate(M)
    re_, bl = (lambda r: (r["stories"]["Base"]["intrinsicRE"], r["stories"]["Base"]["blend"]))(M.compute(**kw))
    importlib.reload(M); return label, re_, bl

ref = base()
cases = [
 run("Rf COP +1pp (todas las Ke)", lambda m: setattr(m, "RF", m.RF + .01)),
 run("Rf COP −1pp (todas las Ke)", lambda m: setattr(m, "RF", m.RF - .01)),
 run("ERP madura implícita oct-2026 3,70%", lambda m: setattr(m, "ERP", .037)),
 run("CRP 100% Colombia en las tres", lambda m: m.EXPO.update({k: {"Colombia": 1} for k in m.EXPO})),
 run("ROE terminal +1pp (Base, tres participadas)", lambda m: m.STORIES["Base"].update({n: (v[0], v[1] + .01, v[2], v[3]) for n, v in m.STORIES["Base"].items() if n in m.BOOK})),
 run("ROE terminal −1pp (Base, tres participadas)", lambda m: m.STORIES["Base"].update({n: (v[0], v[1] - .01, v[2], v[3]) for n, v in m.STORIES["Base"].items() if n in m.BOOK})),
 run("ROE terminal = Ke estable en las tres (sin spread)", lambda m: m.STORIES["Base"].update({n: (v[0], 0.0, v[2], v[3]) for n, v in m.STORIES["Base"].items() if n in m.BOOK})),
 run("Gastos corporativos +20%", lambda m: setattr(m, "HQ", m.HQ * 1.2)),
 run("Precio Cibest −10%", lambda m: setattr(m, "CIBEST_PRICE", m.CIBEST_PRICE * .9)),
 run("P/E sector solo pares LatAm (sin Damodaran EM)", lambda m: None, peers_only=True),
]
out = {"base": {"intrinsicRE": ref[0], "blend6040": ref[1]}, "cases": [{"driver": l, "intrinsicRE": a, "deltaRE": a - ref[0], "blend6040": b, "deltaBlend": b - ref[1]} for l, a, b in cases]}
if __name__ == "__main__":
    print(json.dumps(out, indent=1, ensure_ascii=False))
