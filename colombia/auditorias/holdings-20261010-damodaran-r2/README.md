# Revisión Damodaran r2 · Grupo SURA y Grupo Argos · 10-oct-2026

Revisión de las valoraciones de GRUPOSURA.CL / PFGRUPSURA.CL y PFGRUPOARG.CL con criterio Damodaran y un mismo corte de tasas para Colombia (el de PFDAVVNDA publicado).

## Corte común
- Rf COP = TES jul-2036 13,217% (IRC, 25-sep-2026) − spread Colombia Baa3 1,75% (Damodaran ctrypremJuly26) = **11,467%**.
- ERP madura 4,20% (archivo de países jul-2026); implícita oct-2026 3,70% solo como sensibilidad.
- CRP por país del mismo archivo; betas sectoriales Damodaran ene-2026 que convergen a 1 entre los años 6 y 10.

## Grupo SURA (hoja 1Nb9_T6n8xbJikr68TN5MA5bIIiwm0aKrsF7m4MmOHyM)
| | r1 | r2 |
|---|---|---|
| Ke Cibest / AM / Suramericana | 17,51 / 16,81 / 16,75% (proxies) | 17,58→18,84 / 16,60→17,65 / 16,99→18,42% (CAPM) |
| ROE terminal Base | 17 / 14 / 13,5% (< Ke) | Ke estable +1 / 0 / 0 pp |
| Utilidad UDM Cibest; participación | 7.722.604 proxy; 24,88% | 7.934.717; 24,9365% (calculadora del emisor) |
| P/E sector | 9,27 / 9,45 / 11,07 (proxies) | 11,01 / 12,89 / 10,83 (pares LatAm + Damodaran EM) |
| Precio ordinaria | 67.760 | 67.480 |
| Intrínseco RE Base / esperado | 43.286 / 39.428 | **50.783 / 46.309** |
| Base publicada | RE 43.286 | **60/40 = 94.904** (SOTP económico 81.414; múltiplos 115.139); esperado 87.736 |

Nueva pestaña `CO · Ke y SOTP 60-40`; Ke variable por año en los 12 submodelos (filas 32-33), RE = DDM en las 12 ramas.

## Grupo Argos PF (hoja 1cZbcnriKIfvQX2oPgOKZUKZudSd8EcOwlh9NvjUADDo)
| | r1 | r2 |
|---|---|---|
| Ke holding (gastos HQ y FY+3) | 16% y 14,5% sin sustento | 17,97% (Rf 11,467% + 0,90 × 4,20% + 2,72%) |
| g gastos HQ | 2% | 4,5% nominal; VP = C(1+g)/(Ke−g) como SURA |
| Caja neta Cementos (múltiplos) | 6.016.768 (consenso FY26) | 5.181.000 (2T26) |
| Deuda neta Celsia (múltiplos) | 5.649.737 (FY26 proyectada) | 4.850.000 (2T26 oficial) |
| Minoritarios | no se restaban | Cementos 641.600; Celsia 1.761.600 (libro) |
| Precios GRUPOARGOS / CEMARGOS | 21.220 / 11.400 | 21.000 / 11.500 |
| Base / esperado | 20.174 / 19.716 | **19.363 / 18.913** |

## Archivos
- `sura_modelo.py`: réplica independiente del motor SURA; coincide con la hoja al peso. `sura_sensibilidades.py`: sensibilidades univariantes.
- `argos_modelo.py`: réplica del Base 60/40 de Argos; coincide con la hoja.
- `build_sura.py`, `build_argos.py`: generan los expedientes desde `*_readback.json` (valores leídos de las hojas).
- `escritura_hoja_sura.py`: escrituras hechas en la hoja de SURA (requiere un módulo `gs` con credenciales de la cuenta de servicio, no incluido). Las escrituras de Argos se listan en la tabla anterior.
- `respaldo_formulas_hojas_pre_r2.json.gz`: fórmulas de las pestañas tocadas antes del cambio.
- `pares_yahoo_20261009.json`: múltiplos de pares (Yahoo Finance, 9-oct-2026).

## Pendientes no certificados
Capital regulatorio (CET1/RWA) y solvencia de seguros; pesos de exposición por país (estimados); minoritarios a valor justo; NAV privados de Argos 2025; caja libre de Cementos; DCF FCFF de Argos sigue en la tasa del corte anterior (peso 0).
