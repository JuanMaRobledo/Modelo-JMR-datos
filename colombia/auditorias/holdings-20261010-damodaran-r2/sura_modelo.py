"""Réplica independiente del motor RE/DDM de Grupo SURA (hoja 1Nb9_T6n...), corte 10-oct-2026.

Reproduce, sin leer la hoja, el SOTP intrínseco por rendimientos excedentes, el SOTP económico
(Cibest a bolsa) y el SOTP de múltiplos sectoriales, y la ponderación canónica 60/40 de holdings.
Todas las cifras en COP millones salvo precios y acciones. Uso: python3 sura_modelo.py [--json]
"""
import json, sys
from statistics import median

# --- Corte de tasas Colombia (mismo corte que PFDAVVNDA publicado) ---
TES = 0.13217                     # TES COP ~10 años, IRC 25-sep-2026
SPREAD_CO = 0.01749881223830583   # Damodaran ctrypremJuly26, Colombia Baa3
RF = TES - SPREAD_CO              # 11,467%
ERP = 0.042                       # base madura del archivo de países jul-2026
CRP = {"Colombia": 0.0272018253, "Panamá": 0.0272018253, "El Salvador": 0.0804417616,
       "Guatemala": 0.0309777, "Chile": 0.0104734301, "México": 0.0272018253,
       "Perú": 0.0197831457, "Uruguay": 0.0197831457, "Brasil": 0.0309777,
       "Rep. Dominicana": 0.0372356}
EXPO = {  # Pesos verificados 2T26 (r3): Cibest cartera 6-K 2T26 (Banistmo vendido 30-jun-2026); SURA AM AUM y Suramericana primas LTM, presentación corporativa Grupo SURA 2T26
    "Cibest": {"Colombia": 229573, "El Salvador": 16959, "Guatemala": 16736},
    "AM": {"México": 321, "Colombia": 267, "Chile": 202, "Perú": 52, "Uruguay": 18},
    "Suramericana": {"Colombia": .65, "Chile": .15, "México": .07, "Brasil": .05, "Panamá": .03, "Uruguay": .03, "Rep. Dominicana": .02},
}
BETA = {"Cibest": 0.70, "AM": 0.75, "Suramericana": 0.66}   # Damodaran global ene-2026: bancos 0,697; inversiones/gestión 0,748; seguros (gral 0,51 + vida 0,80)/2
BETA_STABLE = 1.0

def crp(name, expo=None):
    e = expo or EXPO[name]
    return sum(w * CRP[c] for c, w in e.items()) / sum(e.values())

def ke(name, beta=None, expo=None):
    return RF + (BETA[name] if beta is None else beta) * ERP + crp(name, expo)

# --- Datos 2T26 (calculadora de valoración del emisor, ago-2026, y EEFF separados) ---
BOOK = {"Cibest": 38123672, "AM": 10449483, "Suramericana": 6537339}
NI = {"Cibest": 7934717, "AM": 1272336, "Suramericana": 904340}
STAKE = {"Cibest": 0.249365, "AM": 0.9332, "Suramericana": 0.8113}
OTHER = 165883
BRIDGE = 5790704 + 1271839 + 179064 + 9197 - 120548 - 39926 - 1099070 + 500591   # = 6.491.851
HQ = 117000
SHARES = 165834026 + 161871882
CIBEST_SHARES_HELD = 235565920
CIBEST_PRICE = 88000

# Historias: (ROE año 5, ROE contable terminal, spread ROE inversión nueva sobre Ke estable o ("abs", x), g libro 1-5, g terminal)
STORIES = {
 "Base":        {"p": .50, "g_hq": .045, "Cibest": (.19, .17, .01, .06, .045), "AM": (.15, .14, .00, .07, .045), "Suramericana": (.145, .135, .00, .06, .045)},
 "Conservador": {"p": .25, "g_hq": .03,  "Cibest": (.16, .14, -.02, .035, .03), "AM": (.12, .10, -.03, .04, .03), "Suramericana": (.11, .10, -.03, .035, .03)},
 "Optimista":   {"p": .15, "g_hq": .045, "Cibest": (.22, .19, .03, .08, .05), "AM": (.18, .16, .02, .10, .05), "Suramericana": (.17, .15, .02, .08, .05)},
 "Disrupcion":  {"p": .10, "g_hq": .02,  "Cibest": (.09, .08, ("abs", .08), .01, .02), "AM": (.08, .07, ("abs", .07), .01, .02), "Suramericana": (.06, .06, ("abs", .06), .01, .02)},
}

def re_value(name, story, ke_ini=None, ke_st=None, roe_shift=0.0):
    roe5, roeT, spread, g15, gT = STORIES[story][name]
    k0 = ke(name) if ke_ini is None else ke_ini
    kS = ke(name, BETA_STABLE) if ke_st is None else ke_st
    roeT = roeT + roe_shift                                         # ROE contable terminal sobre el libro existente
    roeN = spread[1] if isinstance(spread, tuple) else kS + spread  # ROE de la inversión nueva en crecimiento estable
    b0 = BOOK[name]; roe0 = NI[name] / b0
    book = b0; pv = 0.0; fac = 1.0; ddm = 0.0; divs = []
    for t in range(1, 11):
        g = g15 if t <= 5 else g15 + (gT - g15) * (t - 5) / 5
        roe = roe0 + (roe5 - roe0) * t / 5 if t <= 5 else roe5 + (roeT - roe5) * (t - 5) / 5
        k = k0 if t <= 5 else k0 + (kS - k0) * (t - 5) / 5
        ni = book * roe; reinv = book * g; div = ni - reinv
        fac *= (1 + k)
        pv += (ni - k * book) / fac; ddm += div / fac; divs.append(div)
        book += reinv
    tv_ddm = book * roeT * (1 - gT / roeN) / (kS - gT)             # Damodaran: valor estable = NI11 × (1 − g/ROE nuevo)/(Ke − g)
    tv_re = tv_ddm - book
    v_re = b0 + pv + tv_re / fac; v_ddm = ddm + tv_ddm / fac
    assert abs(v_re - v_ddm) < 1e-3 * abs(v_re), (name, story, v_re, v_ddm)
    v3 = v_re * (1 + k0) ** 3 - divs[0] * (1 + k0) ** 2 - divs[1] * (1 + k0) - divs[2]
    return {"equity100": v_re, "attrib": v_re * STAKE[name], "ke_ini": k0, "ke_stable": kS, "roe_terminal": roeT, "roe_new": roeN, "year3": v3}

def holding_ke():
    w = {n: re_value(n, "Base")["attrib"] for n in BOOK}
    return sum(ke(n) * w[n] for n in w) / sum(w.values())

def hq_pv(story, k=None):
    k = holding_ke() if k is None else k
    g = STORIES[story]["g_hq"]
    return HQ * (1 + g) / (k - g)

# Múltiplos P/E UDM (Yahoo Finance, 9-oct-2026) y anclas sectoriales Damodaran mercados emergentes ene-2026
PEERS = {
 "Cibest": {"BAP": 14.358, "BSAC": 12.440, "BCH": 14.900, "ITUB": 13.026, "GFNORTEO.MX": 8.827, "AVAL": 12.868, "PFDAVVNDA.CL": 8.584, "BBD": 13.871},
 "AM": {"HABITAT.SN": 8.569, "VINP": 9.863},
 "Suramericana": {"BBSE3.SA": 8.630, "PSSA3.SA": 9.359, "CXSE3.SA": 13.821, "Q.MX": 13.746},
}
DAMODARAN_EM_PE = {"Cibest": 9.0707, "AM": 16.5569, "Suramericana": (10.1860 + 10.0176) / 2}   # Mkt cap / NI firmas con utilidad: Bank (Money Center); Investments & AM; Insurance (General, Life)

def sector_pe(n, peers_only=False):
    m = median(PEERS[n].values())
    return m if peers_only else (m + DAMODARAN_EM_PE[n]) / 2

def compute(w_econ=0.6, w_mult=0.4, peers_only=False):
    out = {"rf": RF, "erp": ERP, "holding_ke": holding_ke(), "stories": {}}
    base_attr = {n: re_value(n, "Base")["attrib"] for n in BOOK}
    for s in STORIES:
        parts = {n: re_value(n, s) for n in BOOK}
        hq = hq_pv(s)
        intr = (sum(p["attrib"] for p in parts.values()) + OTHER - BRIDGE - hq) * 1e6 / SHARES
        scale = {n: parts[n]["attrib"] / base_attr[n] for n in BOOK}
        cib_mkt = CIBEST_SHARES_HELD * CIBEST_PRICE / 1e6 * scale["Cibest"]
        econ = (cib_mkt + parts["AM"]["attrib"] + parts["Suramericana"]["attrib"] + OTHER - BRIDGE - hq) * 1e6 / SHARES
        mult_parts = {n: sector_pe(n, peers_only) * NI[n] * STAKE[n] * scale[n] for n in BOOK}
        mult = (sum(mult_parts.values()) + OTHER - BRIDGE - hq) * 1e6 / SHARES
        out["stories"][s] = {"p": STORIES[s]["p"], "intrinsicRE": intr, "sotpEconomic": econ, "sotpMultiples": mult,
                             "blend": w_econ * econ + w_mult * mult, "hqPV": hq, "cibestMarketAttrib": cib_mkt,
                             "parts": {n: {k: v for k, v in p.items()} for n, p in parts.items()}, "multParts": mult_parts}
    for k in ("intrinsicRE", "sotpEconomic", "sotpMultiples", "blend"):
        out["expected_" + k] = sum(v["p"] * v[k] for v in out["stories"].values())
    out["sectorPE"] = {n: sector_pe(n, peers_only) for n in BOOK}
    return out

if __name__ == "__main__":
    r = compute()
    if "--json" in sys.argv:
        print(json.dumps(r, indent=1, ensure_ascii=False)); sys.exit()
    print(f"Rf {RF:.4%}  ERP {ERP:.2%}  Ke holding {r['holding_ke']:.4%}")
    for n in BOOK:
        print(f"{n:13s} CRP {crp(n):.4%} Ke ini {ke(n):.4%} Ke estable {ke(n,1):.4%} ROE UDM {NI[n]/BOOK[n]:.2%} P/E sector {r['sectorPE'][n]:.2f} (pares {sector_pe(n,True):.2f})")
    for s, v in r["stories"].items():
        print(f"{s:12s} RE {v['intrinsicRE']:9,.0f}  econ {v['sotpEconomic']:9,.0f}  mult {v['sotpMultiples']:9,.0f}  60/40 {v['blend']:9,.0f}  HQ {v['hqPV']:,.0f}")
    print("esperado", {k: round(r['expected_'+k]) for k in ("intrinsicRE","sotpEconomic","sotpMultiples","blend")})
    print("Sensibilidad P/E solo pares:", round(compute(peers_only=True)["stories"]["Base"]["blend"]))
