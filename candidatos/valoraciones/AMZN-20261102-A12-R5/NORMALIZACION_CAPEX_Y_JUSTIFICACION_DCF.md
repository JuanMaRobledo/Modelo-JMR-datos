# AMZN R5 · Normalización económica de CAPEX y justificación del FCFF negativo

**Fecha:** 2026-11-03. **Revisión:** AMZN-20261102-A12-R5. **Estado:** expediente de conciliación CAPEX completo, hipótesis F3 **NO APROBADA**. **No alterar GAAP ni forzar FCFF positivo.** Hoja: https://docs.google.com/spreadsheets/d/199x_GNl2608SFjj58hCtTjWpxleL2rqtRPJl4lZdW5I/edit

## 1. Fuente SEC (USD millones)
| Concepto y corte | Dato | Celda fuente |
|---|---:|---|
| CFO doce meses a 30-sep-2026 | +168.300 | Cash Flow Statement!L13 |
| CAPEX bruto en efectivo (PPE) doce meses | −215.192 | Cash Flow Statement!L15 |
| Ventas de activos e incentivos reconocidos | +4.535 | Cash Flow Statement!L16 |
| CAPEX neto de incentivos | **210.657** | Input sheet!B163 fórmula |
| FCF reportado por Amazon | **−42.357** | Input sheet!B164 fórmula |
| Flujo excluyendo incentivos | **−46.892** | 168300 − 215192, distinto de FCF reportado |
| Otras inversiones/adquisiciones en CFI (agregado) | −65.156 | Cash Flow Statement!L21, **FUERA de CAPEX** |
| D&A total cash-flow LTM | 79.353 | Cash Flow Statement!L4, **no equivale a mantenimiento** |

**Fuentes:** 2026 10-Q https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm ; resultados Q3 2026 https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Third-Quarter-Results/default.aspx .

Amazon espera ~US$220.000M de CAPEX en efectivo en FY2026 y **mayor** volumen en FY2027 (sin guía numérica exacta para 2027). **No** imponer vuelta inmediata a CAPEX histórico o margen de caja positivo en 2027.

## 2. Evidencia de inversión en crecimiento ≠ contabilización de mantenimiento

SEC 10-Q segmentos nueve meses a septiembre2026:
- Adiciones netas a PPE de todo el grupo, **US$196.910M**, de AWS **US$147.236M** (**74,77%**) y otros negocios US$49.674M.
- Depreciación/amortización de PPE de grupo **US$41.845M** (AWS US$24.583M). La diferencia adiciones-PPE DA grupo **US$155.065M** es indicador de expansión sustancial; AWS **US$122.653M**.
- **Las adiciones netas PPE por segmentos no son pagos de CAPEX en efectivo**, incorporan elementos de arrendamientos y activos adquiridos con financiación; no sumarlas a capex cash LTM. La depreciación de PPE es **costo de activos pasados**, no una cuenta directa de reemplazo de activos. Mantener legibilidad de períodos 9M y LTM.
- D&A PPE anualizada 9M × 12/9 = **US$55.793M** como **PROXY de sensibilidad** de mantenimiento, nunca dato revelado de CAPEX de mantenimiento.
- FCF antes del exceso de CAPEX neto sobre D&A total: +US$88.947M; si se usa DA PPE anualizada: +US$112.507M. **NINGUNO ES FCF DISPONIBLE, FCFF NORMALIZADO OFICIAL NI PRECIO INTRÍNSECO**: son ilustraciones de autofinanciación previa a CAPEX adicional. Seguir exigiendo reinversión económica para obtener crecimiento.

Fuentes: SEC nota PPE por segmento y cash flows https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm ; Damodaran, FCFF/valores y reinversión https://people.stern.nyu.edu/adamodar/pdfiles/papers/valcre.pdf .

## 3. Qué está calculando el DCF JMR (no usa CAPEX histórico como input proyectado)

En `Valuation output!C10` la inversión marginal no se toma del CAPEX GAAP registrado; es **inversión por incremento de ventas / Sales-to-Capital**, con `Input sheet!B58=2` años de desfase, control de reinversión en escenarios E5:F8. Para Base:
- `Escenarios e historias!E5=0,72` S/C incrementales años1–5 y F5=1,65 en años6–10, **juicios no publicados**;
- `Valuation output!C9=US$96.156M` NOPAT FY+1; `C10=US$121.712M` reinversión FY+1; `C11=−US$25.555M` **FCFF FY+1** por diferencia.
- FY+2 **−US$15.679M**, FY+3 **−US$6.372M**, FY+4 **+US$4.636M**; FCFF mejora cuando NOPAT sube y reinversión relativa desacelera. Un FCFF negativo de primeros años no exige que EV/DCF sea negativo; valor intrínseco Base calculado **US$149,1915/acción**.
- En puente **no directamente comparable** a CAPEX histórico, si se le suma a reinversión FY+1 la DA PPE anualizada proxy 55.793M, el supuesto "capex equivalente" es ~US$177.505M vs CAPEX neto LTM210.657M, brecha ~US$33.152M. Riesgo: en 2027 CAPEX aumenta, y el S/C0,72 podría SUBESTIMAR inversión verdadera. Requiere fase 3 con forecast de D&A, ΔNWC, nuevos arrendamientos e I+D capitalizada para conciliar cash capex vs reinversión económica; de lo contrario este puente es **indicativo**.
- **CAPEX inorgánico / aportes financieros no es lo mismo que CAPEX operativo**: separar adquisiciones/inversiones y contabilización de valor Anthropic/OpenAI en bridge patrimonial; no cargarlo en FCFF y a la vez añadir participaciones de nuevo.

## 4. Pruebas reales de sensibilidad (restauradas en la hoja)
Se modificó temporalmente SOLO `Escenarios e historias!E5` para probar S/C y se restauró `0,72`. Datos leídos directamente de la hoja:

| S/C 1–5 | DCF Base US$/acción | Reinversión FY+1 US$M | FCFF FY+1 US$M | FCFF FY+3 US$M |
|---:|---:|---:|---:|---:|
| 0,50 | 128,7214 | 175.265 | −79.108 | −62.669 |
| 0,55 | 134,8117 | 159.332 | −63.175 | −45.920 |
| **0,72** | **149,1915** | **121.712** | **−25.555** | **−6.372** |
| 0,90 | 158,4961 | 97.369 | −1.213 | +19.218 |

Las tres matrices DCF `Sensibilidad DCF!B12/B23/B34` retornaron **OK** tras cada cálculo y tras restaurar Base. **La prueba no demuestra que 0,72 sea el supuesto económicamente más razonable.** Si se usa 0,50–0,55 para stress de mayor capital requerido, Base baja a USD128,72–134,81/acción. No escribir estos valores como DCF oficial ni reemplazar los cuatro escenarios sin F3.

## 5. Contrato de normalización correcto para todas las empresas
- Mantener CAPEX GAAP bruto y flujos reportados inmutables. Ajustar incentivos/venta de activos solo con clasificación SEC trazada y sin restar activos vendidos dos veces.
- Separar como **hipótesis y sensibilidad**, no como cifras reportadas, CAPEX de mantenimiento, expansión, inversión no cash, leasing, capitalización I+D, SBC, adquisiciones e inversiones patrimoniales.
- FCFF = EBIT normalizado(1−t) − [(CAPEX económico−D&A) + ΔNWC + adquisiciones operativas cuando aporten crecimiento y no se valoren aparte]; si se usa Sales-to-Capital, **NO volver a sumar capex bruto encima del resultado**, pues sería doble conteo.
- Exigir explicación por AWS/IA, lead time, ROIC marginal y convergencia de S/C. Si el CAPEX esperado 2027 supera guidance previa, la historia Base debe incorporar inversión mayor o justificar ganancia de productividad futura, no suprimir su costo.
- Evitar dos errores simétricos: (a) usar el CAPEX extraordinario LTM para siempre en perpetuidad; (b) reemplazarlo por DA para todo el horizonte mientras se conserva crecimiento de dos dígitos.

## 6. Estado
**Completado:** captura SEC, puente histórico y segmentado, identificación mantenimiento/crecimiento como proxies, reconciliación, escenarios de stress y restitución 0,72. **PENDIENTE ECONÓMICO MATERIAL de F3:** previsión CAPEX FY2027 por inversión comprometida, conciliación cash capex y reinversión DCF, separación de leases, productividad de activos y ROIC incremental. **F1/F2 no se certifican por este puente**; consulte [CIERRE_OPERATIVO_F1_F2.md](CIERRE_OPERATIVO_F1_F2.md). No se fusiona ni publica PR #234.

## 7. Validación adicional del CAPEX de 2026 y conciliación ilustrativa con 2027 (3-nov-2026)

La fuente primaria SEC confirma **cash CAPEX FY2026 nueve meses 175.670 M** (estado cash flows), frente a **guía FY2026 de ~220.000 M** de efectivo. La parte implícita de cuarto trimestre para llegar a ese importe sería **44.330 M**; **cálculo**, no previsión comunicada para Q4. Fuente: [10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm), [resultado 29-oct-2026](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000038/amzn-20260930xex991.htm).

La guía cualitativa indica que el CAPEX cash FY2027 será mayor que FY2026, pero **NO aporta cuantía FY2027**. Para hacer explícita la condición económica y evitar extrapolar ganancias sin inversión, se añadió `Input sheet!A210:B226`:

| Concepto ilustrativo, US$ M | Importe |
|---|---:|
| Guía cash CAPEX FY2026, referencia (NO guía FY2027) | 220.000 |
| Menos incentivos y ventas PPE observados LTM (NO proyección) | 4.535 |
| Cash CAPEX neto ilustrativo | **215.465** |
| Reinversión FY+1 ya contenida en DCF Base | **121.711,57** |
| **D&A menos ΔNWC requerido para conciliar ambas series (bajo supuestos simplificadores)** | **93.753,43** |
| D&A cash flow reportada LTM (incluye contenido y lease) | 79.353 |
| Brecha sin justificar si D&A igual LTM y ΔNWC=0 | **14.400,43** |
| Aumento de D&A para conciliar con ΔNWC=0 | **18,15%** |

**No hay equivalencia contable automática**: CAPEX FY2026 vs reinversión FY2027, provisiones e incentivos, timing, importes no pagados, compras vía arrendamientos, depreciación de contenido/ROU y capital de trabajo difieren. Los resultados son un **test condicional**, no CAPEX sostenible calculado ni instrucción para subir o bajar DCF. Con inversión efectiva FY2027 mayor, el test exigiría más D&A y/o ΔNWC negativo, mayor reinversión o eficiencia demostrable.

SEC divulga además aumentos netos LTM de PPE adquirido y no pagado por **26.779 M** y PPE financiado con leases por **4.543 M**: `Input B223:B224`. Son componentes de actividad no cash, **no sumarlos encima del CAPEX cash reportado** ni tratar todo como flujo incremental para el DCF. Esto explica por qué la comparación de adiciones a activos (196.910M en 9M) no debe reemplazar los desembolsos de efectivo (175.670M en 9M).

**F1/F2:** datos históricos, clasificación, puente y test condicional documentados; **F3 deberá decidir si el S/C 0,72 y el desfase 2 años subestiman la reinversión 2027**, con productividad AWS, ROIC marginal y renovación de activos. Hasta entonces DCF Base US$149,19 **candidato**, no normalizado al alza para eliminar FCFF negativos. Los cuatro escenarios originales y tres sensibilidades centrales continúan LISTO/OK tras escritura y lectura.

