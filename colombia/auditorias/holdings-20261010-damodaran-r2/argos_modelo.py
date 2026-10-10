"""Réplica independiente del Base 60/40 de Grupo Argos PF (hoja 1cZbcnri...), corte 10-oct-2026. COP millones."""
import json, sys
RF = 0.13217 - 0.01749881223830583; ERP = 0.042; BETA_H = 0.90; CRP_CO = 0.0272018253
KE_H = RF + BETA_H * ERP + CRP_CO; G_HQ = 0.045
SHARES = 395820682 + 285940511 - 1368769 - 560390          # 30-jun menos recompra sept
BUYBACK = 1368769 * 21900 / 1e6 + 560390 * 16500 / 1e6
HQ = (106138.849 - 58884.275) * 2 * 0.9
HQ_PV = HQ * (1 + G_HQ) / (KE_H - G_HQ)
CEM_SH, CEM_PX = 671439556, 11500
CEL_SH, CEL_PX = 566360307 - 9155169, 4810
ODINSA = 2700000 * 0.9499; PACTIA = 1030000
OTHERS = 159626.653 + 4643.741 + 3031.948 + 154583.179      # Sator, Summa, otras asociadas, residual matriz
econ_eq = CEM_SH * CEM_PX / 1e6 + CEL_SH * CEL_PX / 1e6 + ODINSA + PACTIA + OTHERS - BUYBACK - HQ_PV
econ = econ_eq * 1e6 / SHARES
# Múltiplos: EV/EBITDA FY26 de pares × EBITDA FY26 consenso − deuda neta 2T26 − minoritarios libro
cem_eq = max(0, (5.15 + 6.87 + 5.10) / 3 * 1317719 - (-5181000) - 641600) * 0.5528
cel_eq = max(0, (6.52 + 6.43) / 2 * 1749114 - 4850000 - 1761600) * (CEL_SH / 1011329371)
mult_eq = cem_eq + cel_eq + ODINSA + PACTIA + (159626.653 + 4643.741 + 3031.948 + 154583.179) - BUYBACK - HQ_PV
mult = mult_eq * 1e6 / SHARES
base = 0.6 * econ + 0.4 * mult
r = {"keHolding": KE_H, "hqPV": HQ_PV, "sotpEconomic": econ, "sotpMultiples": mult, "base6040": base,
     "cementosEquityMult": cem_eq, "celsiaEquityMult": cel_eq}
print(json.dumps(r, indent=1))
