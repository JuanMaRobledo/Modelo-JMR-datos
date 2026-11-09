# AAPL-FLOYD-FY26-R1 · continuación F3/F4 (9-nov-2026) · ESTADO: CANDIDATO_REVISADO (NO EN_REVISION)

Agente: Claude (Claude Code, modelo configurado claude-sonnet-5-5; esfuerzo no identificable). Acceso real: Google Sheets (lectura/escritura), Drive (lectura/copia), FMP (precios). **Sin escritura en Google Docs.**
Libros: H1 `1MHlhgbWgRGysN11_LnyBS94aueV4KijXnqKvLhN5U98` · H2 `1gtAc2TclEjszznAC8tfDGiOviq3bagTA7AzOh2r1h0c` · H3 doc `1SfPYnHbSKUh7_0ziFsPTYOI5gIg-pRJDLIb8P2gU-xs`. No se crearon libros nuevos. Fórmulas del motor no modificadas (la comparación contra la Maestra NO se ejecutó: NO_EJECUTADO).

## Hecho en H2 (APROBADO salvo nota)
1. `Trailing Valuation!B3:L3`: precios de cierre fiscal ajustados por splits (FMP historical-price-eod-full, 9-nov-2026): 2017-09-29 38,53 · 2018-09-28 56,44 · 2019-09-27 54,71 · 2020-09-25 112,28 · 2021-09-24 146,92 · 2022-09-23 150,43 · 2023-09-29 171,21 · 2024-09-27 227,79 · 2025-09-26 255,46 · 2026-09-25 341,07 (LTM = FY2026). Fechas en `Entradas históricas auxiliares!A6:L7`.
2. `Entradas históricas auxiliares!B4:L5` (NCI y preferentes) = 0 (Apple no los reporta; **verificación contra 10-K por año NO_EJECUTADA**, solo conocimiento del emisor). TEV calcula FY2021-FY2026; FY2017-FY2020 N/D (arrendamientos no desglosados en balance).
3. Salida de los cinco múltiplos: `J19 = MIN(B19:E19)` (mínimo positivo de 4 cierres), `J8 = 0,9×J19`, `J30 = 1,1×J19` en EVEBITDA, EVFCFF, PE, PFCFE, POCF. Base 21,66x / 27,29x / 27,45x / 29,76x / 24,13x. Cinco matrices 5×5 Base con centro = VP3 (OK). P/V y P/BV: N/D (no son de los cinco).
4. `Resumen de Valoración!G3 = Madura`, `G4 = 35 %`. Valor hoy múltiplos consolidados (secundario) Base 242,70; ponderado 217,55. DCF Base sin cambio: 179,81 (Cons 115,72 · Opt 236,72 · esperado 178,21 · MOS35 = 116,87).
5. `Compuertas económicas!B31:D31`: justificación del escalón ROIC año 10→terminal con sensibilidad reproducible (Base: 15 %→179,81; 25 %→192,45; 74,74 %→205,08). Sigue AVISO, no auditoría.

## DCF inverso (réplica externa del motor, error 0,0002 USD/acción frente a H2; script no versionado)
Precio 342,37, resto en Base: crecimiento años 1-5 ≈ 24,6 % (Base 7,0 %); margen objetivo año 10 ≈ 76,3 % (Base 36 %); WACC paralelo −2,49 pp (inicial 7,53 %, terminal 6,07 %); con margen 40 %: crecimiento ≈ 21,9 %. Sales-to-Capital no explica el precio (100x → 188,10). **No está escrito aún en H2/Tesis.**

## Hallazgo I+D (resuelto como LIMITACIÓN DOCUMENTADA, no como corrección)
`R& D converter!B12` = `'Income Statement'!K10` (FY2026) como «año −1» mientras LTM (L) = FY2026: FY2026 entra dos veces y FY2024 no entra (activo 87.791,7 vs 79.255; ajuste EBIT +8.537 vs +13.820). Con autorización del usuario se re-cableó B12:B21 (J10…B10): `Huella motor` pasó a **10 diferencias / 1883**, `Escenarios e historias!H5:H12` quedaron en blanco (gate) y el semáforo marcó INTEGRIDAD FALLA. Se **revirtió exactamente** (0 diferencias, valores 179,8060617 / 115,715746 / 236,7237544 restaurados; verificado). Impacto estimado por réplica externa de la corrección: Cons 116,82 (+0,95 %) · Base 181,05 (+0,69 %) · Opt 238,09 (+0,58 %) → inmaterial y acotado; corregir requiere mantenimiento de plantilla con respaldo y regresión. Vida de I+D (F7) 2/3/5 años, DCF Cons/Base/Opt: 115,10/179,12/235,97 · 115,72/179,81/236,72 · 116,48/180,67/237,67 (F7 restaurado a 3). Notas escritas en `Control de integridad!A9:A13`.

## Pendiente (bloquea EN_REVISION)
- Escribir el DCF inverso en `Tesis de Inversión y Supuestos` (hoja aún sin llenar; solo está en `Control de integridad!A9:A13`).
- Cotejo FY2017-FY2023 de H1 contra 10-K (NO_EJECUTADO).
- Hoja `Tesis de Inversión y Supuestos` sigue con la plantilla sin llenar ([TICKER]).
- Reescribir H3 (Nivel 1 14 caps + Nivel 2 12 apart.) con cifras finales: **sin herramienta de escritura en Docs en esta sesión**.
- `Huella motor`/diff contra Maestra, `validar_catalogo`, `validar_profundidad_floyd`, JSON de valoración/análisis, catálogo: NO_EJECUTADO.
- F5 independiente: NO_EJECUTADA.
Siguiente paso exacto: decidir la corrección del puente I+D (año −1 = FY2025) y, con escritura en Docs, rehacer H3.
