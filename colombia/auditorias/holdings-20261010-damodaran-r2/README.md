# Revisión Damodaran r2–r4 · Grupo SURA y Grupo Argos · 10-oct-2026

Revisión de las valoraciones de GRUPOSURA.CL / PFGRUPSURA.CL y PFGRUPOARG.CL con criterio Damodaran y un mismo corte de tasas para Colombia (el de PFDAVVNDA publicado).

## Corte común
- Rf COP = TES jul-2036 13,217% (IRC, 25-sep-2026) − spread Colombia Baa3 1,75% (Damodaran ctrypremJuly26) = **11,467%**.
- ERP madura 4,20% (archivo de países jul-2026); implícita oct-2026 3,70% solo como sensibilidad.
- CRP por país del mismo archivo; betas sectoriales Damodaran ene-2026 que convergen a 1 entre los años 6 y 10.

## Grupo SURA (hoja 1Nb9_T6n8xbJikr68TN5MA5bIIiwm0aKrsF7m4MmOHyM)
| | r1 | r2 |
|---|---|---|
| Ke Cibest / AM / Suramericana | 17,51 / 16,81 / 16,75% (proxies) | 17,58→18,84 / 16,60→17,65 / 16,99→18,42% (CAPM) |
| Valor terminal | ROE 17 / 14 / 13,5% (< Ke) sobre todo el libro | r3: libro existente conserva su ROE contable; inversión nueva rinde Ke estable (+1pp Cibest): NI11 × (1 − g/ROE nuevo)/(Ke − g). (r2 aplicaba ROE = Ke a todo el libro y sobrevaloraba SURA AM, con 5,9 billones de plusvalía.) |
| Exposición país | Estimada | r3 verificada 2T26: Cibest por cartera (Colombia 87,2%, El Salvador 6,5%, Guatemala 6,4%; Banistmo vendido el 30-jun-2026), SURA AM por AUM, Suramericana por primas |
| Capital Cibest | No conciliado | Solvencia básica 12,55% / total 14,19% (6-K 2T26); payout implícito 69,5% compatible con solvencia constante |
| Solvencia Suramericana | No conciliada | r4: Colombia Vida 1,57× y Generales 1,55× (jun-2026); México RCS 6,88× (dic-2025); Panamá capital fuerte (AM Best); Chile y Brasil sin cifra pública |
| Utilidad UDM Cibest; participación | 7.722.604 proxy; 24,88% | 7.934.717; 24,9365% (calculadora del emisor) |
| P/E sector | 9,27 / 9,45 / 11,07 (proxies) | 11,01 / 12,89 / 10,83 (pares LatAm + Damodaran EM) |
| Precio ordinaria | 67.760 | 67.480 |
| Intrínseco RE Base / esperado | 43.286 / 39.428 | r2 50.783 / 46.309 → **r3 42.115 / 38.390** |
| Base publicada | RE 43.286 | r2 94.904 → **r3 60/40 = 91.033** (SOTP económico 74.958; múltiplos 115.146); esperado 84.497 |

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
| Base / esperado | 20.174 / 19.716 | r2/r3 19.363 / 18.913 → **r4 18.004 / 17.585** |
| Odinsa (atribuible) | NAV gerencia dic-2025 2,565 billones | r4: 1,967 billones = libro 2T26 (FCP a valor razonable) + Quiport a precio de transacción (USD 81,5 MM) + gestor DCF; NAV gerencia como sensibilidad |
| Pactia (atribuible) | Colliers sep-2025 1,030 billones | r4: 1,066 billones = valor de unidad 30-jun-2026 × 62.213.152 unidades |
| Caja de Cementos | 5,181 billones neta (todo) | r4: caja libre 7,793 (restringida 5 mil MM; resta dividendo pendiente 262 mil MM) − deuda 2,879 = 4,914 neta |
| Minoritarios | a libro | r4: a valor justo = libro × P/B de mercado (Cementos 1,536; Celsia 1,586) |
| WACC motores secundarios | analista, distinto por historia (hasta 20%) | r4: Damodaran, misma tasa en las 4 historias: Growth 13,22%, concesiones 13,40%, Pactia fondo 15,36%, gestores 16,56%, NDU 14,10%, HQ 17,97% |
| DCF FCFF opcional (peso 0) | 8.294 (Rf sintética 8,86%) | r3 6.808 → r4 6.881 (todos los motores con WACC Damodaran; caja libre y minoritarios a valor justo) |

## Archivos
- `sura_modelo.py`: réplica independiente del motor SURA; coincide con la hoja al peso. `sura_sensibilidades.py`: sensibilidades univariantes.
- `argos_modelo.py`: réplica del Base 60/40 de Argos; coincide con la hoja.
- `build_sura.py`, `build_argos.py`: generan los expedientes desde `*_readback.json` (valores leídos de las hojas).
- `build_argos_r4.py`: Odinsa, Pactia, caja libre, minoritarios y motores secundarios (r4).
- `build_argos_r3.py`: lleva el DCF FCFF recalculado al expediente.
- `escritura_hoja_sura.py`: escrituras hechas en la hoja de SURA (requiere un módulo `gs` con credenciales de la cuenta de servicio, no incluido). Las escrituras de Argos se listan en la tabla anterior.
- `respaldo_formulas_hojas_pre_r2.json.gz`: fórmulas de las pestañas tocadas antes del cambio.
- `pares_yahoo_20261009.json`: múltiplos de pares (Yahoo Finance, 9-oct-2026).

## Pendientes no certificados
Solvencia de Suramericana en Chile, Brasil, Uruguay y Rep. Dominicana (sin cifra pública); valor justo propio de cada minoritario (se aproxima con el P/B de la matriz cotizada); Quiport con precio de transacción de 2023; flujos por concesión de Odinsa; WACC de Sator (sin cambio); serie histórica homogénea de múltiplos postescisión.
