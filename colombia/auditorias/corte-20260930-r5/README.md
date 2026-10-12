# Colombia r5 · corte 30-sep-2026 · como la cartera de EE.UU.

Revisión del 12-oct-2026: las valoraciones de Colombia quedan con el mismo criterio que la cartera de EE.UU.

## Resultado (COP por acción)

| Expediente | DCF Base (principal) | Esperado | Compra con MOS 35% | Precio 30-sep | Base/precio | Sin foso (retorno = costo) | Ponderado secundario 40/60 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PFDAVVNDA (Banco Davivienda) | 20.663 | 16.585 | 10.780 | 27.500 | −25% | ≈26.727 | 24.433 |
| PFDAVIGRP (Davivienda Group) | 23.160 | 20.728 | 13.473 | 39.600 | −42% | 27.892 | 22.899 |
| PFGRUPSURA (Grupo SURA PF) | 45.136 | 41.109 | 26.721 | 58.840 | −23% | 51.516 | 87.058 |
| GRUPOSURA (Grupo SURA ord.) | 45.136 | 41.109 | 26.721 | 69.000 | −35% | 51.516 | 87.058 |
| PFGRUPOARG (Grupo Argos PF) | 10.346 | 10.107 | 6.569 | 16.360 | −37% | 10.346 | 13.828 |

Antes (r2-r4, 9-11 oct): Banco 19.474 · Group 21.969 · SURA intrínseco 42.115 (publicado 60/40 91.033) · Argos 60/40 18.004 (DCF FCFF pegado 6.881).

## Qué cambió

1. **Corte común** (`respaldo_antes.json` guarda los valores anteriores):
   - ERP madura 4,20% (base jul-2026) → **3,70%** (implícita de Damodaran oct-2026, la de la cartera de EE.UU.) + prima país.
   - TES jul-2036 13,217% (25-sep) → **13,00%** (cierre de septiembre, fuente secundaria: Valora Analitik vía Yahoo Noticias, 6-oct-2026); Rf COP 11,25%.
   - Precios BVC del **30-sep-2026** (Yahoo Finance): PFDAVVNDA 27.500, PFDAVIGRP 39.600, PFGRUPSURA 58.840, GRUPOSURA 69.000, PFGRUPOARG 16.360, GRUPOARGOS 21.860, CEMARGOS 11.240, CELSIA 4.800, CIBEST 90.000.
2. **Valor principal = intrínseco Damodaran.** Bancos: RE/DDM o FCFE (ya lo eran). SURA: el intrínseco RE/DDM deja de ir aparte y pasa a principal; el 60/40 queda como referencia. Argos: nueva pestaña **«CO 15 DCF Damodaran»** con FCFF de Cementos Argos y Celsia (cuatro historias, WACC con beta del sector, inflación COP consistente con la Rf, ROIC terminal = WACC, minoritarios proporcionales al valor intrínseco, piso cero) + privadas a valores fechados − recompra y gastos de matriz (`argos_dcf_filiales.py`).
3. **Esperado, MOS 35% sobre el esperado y ponderado secundario 40% DCF + 60% múltiplos** en hojas, expedientes y app.
4. **Lectura de foso** (`lectura_foso_colombia.py`, `foso_colombia.json`): Banco, Group y Argos sin ventaja defendible; SURA mixta (Cibest con ventaja de escala). En el Banco, el Group y SURA AM/Suramericana el modelo deja el ROE terminal **por debajo** del Ke; con la regla de la cartera (ROE = Ke) valdrían más (columna «Sin foso»). No se cambió el Base.
5. **App** (Modelo-JMR `docs/colombia`): el visor y la biblioteca muestran el DCF Base intrínseco como principal, el esperado y el precio con MOS; el selector de métodos parte de 40% DCF + 60% múltiplos. **Prompts** `colombia-valuation-v1.md` y `colombia-research-v1.md`: regla r5 con precedencia.

## Controles

`python3 controles_r5.py` → 12/12 en los cinco expedientes (valor principal = hoja, esperado = suma, MOS, 40/60, corte, ERP, nota r5 en los informes, lectura Damodaran).

## Salvedades

- Argos: los insumos de Cementos y Celsia (ingresos y margen UDM, ventas/capital, spreads) son estimaciones del analista con fuentes de prensa y Yahoo Finance; Odinsa, Pactia y demás privadas siguen a valores fechados (sin flujos propios). El resultado es sensible al margen y al ventas/capital (ver ROIC del capital nuevo en la pestaña).
- El Banco «sin foso» es una aproximación fuera de la hoja (valor terminal residual = 0).
- Los informes de los expedientes llevan al inicio una nota r5 que manda sobre las cifras anteriores del cuerpo.
- Archivos de respaldo de escrituras: `respaldo_*.json`.

## r6 · 12-oct-2026 · ROE terminal = Ke y valoración de SURA con el prompt

- **ROE terminal = Ke** (sin foso, regla de la cartera) aplicado al Base en las hojas, con respaldo en `respaldo_roe_ke.json`: Banco (`Terminal regulatorio`!J6:K9: TV RE = 0, TV DDM = libro FY10), Group (`Entradas cierre`!E42:E45 = Ke terminal) y SURA (`Supuestos`!D15:D26 e I15:I26 = Ke estable; Cibest ya sin +1pp).

| Expediente | DCF Base r5 | DCF Base r6 | Esperado r6 | Compra MOS 35% | Precio 30-sep |
| --- | --- | --- | --- | --- | --- |
| PFDAVVNDA | 20.663 | **27.141** | 22.918 | 14.897 | 27.500 |
| PFDAVIGRP | 23.160 | **27.892** | 25.713 | 16.713 | 39.600 |
| PFGRUPSURA / GRUPOSURA | 45.136 | **51.511** | 49.519 | 32.187 | 58.840 / 69.000 |
| PFGRUPOARG | 10.346 | 10.346 | 10.107 | 6.569 | 16.360 |

- Con ROE = Ke el crecimiento terminal no crea valor (sensibilidad a g = 0 en SURA). Sensibilidades de SURA (`sura_sensibilidades_r6.json`): Rf ±1 pp −3.078/+3.253; ERP ±0,5 pp −1.114/+1.137.
- **SURA con el prompt**: informes v4 (14 secciones) y v5 (18) generados por `JMR-valuation/scripts/co_informes_sura.py` desde UNA lectura de la hoja (`co_lector.py`); reemplazan los de r3 en los dos expedientes. Combinado secundario 40/60 también en `CO · Ponderaciones`.
- **Ahorro de tokens**: núcleo `Modelo-JMR/docs/prompts/colombia-nucleo-v1.md` (2 KB frente a 55 KB por prompt) y habilidad `.claude/skills/valoracion-colombia`.
