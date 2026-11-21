# Corte de trabajo — Modelo JMR, 30-oct-2026

**Propósito:** identificar brechas comprobables antes de sustituir los expedientes activos. Este es un registro de trabajo, no una valoración ni una auditoría económica. **No cambia catálogo, valoraciones, artículos, hojas ni producción.**

## A. Cuatro valoraciones pendientes de recalibrar con Método A-1.2

| Orden | Ticker | Revisión activa | DCF principal guardado (USD/acción) | Hoja verificada | Resolución técnica que falta |
|---|---|---|---:|---|---|
| 1 | UBER | UBER-REC-20261027-R1 | 73,27 | [Hoja UBER](https://docs.google.com/spreadsheets/d/1R3V8gISxXCYIujVFSITu0svVBC3AsN4GF_pQHHLs5dw/edit) | Contraste previo ya modelado: [DCF proxy y sensibilidades](../documentos/UBER-20261030-A12-candidato-DCF-independiente.md). Rehacer en hoja/motor oficial, fuentes y capitalización de I+D |
| 2 | META | META-20261025-R5 | 726,65 | [Hoja META](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit) | Conciliar inversiones IA/CapEx, gasto legal registrado vs provisión, clase de acciones y dilución; recalibrar ROIC/reinversión y escenarios |
| 3 | NVDA | NVDA-20261025-R4 | 381,79 | [Hoja NVDA](https://docs.google.com/spreadsheets/d/1gbtwORZsvjhZNCV8xlNDloHYEeE09cEbXmPZOoLJ8gY/edit) | Validar crecimiento/terminal, duración de ventaja competitiva, ROIC, ventas/capital, I+D, demanda IA y sensibilidad a normalización |
| 4 | XP | XP-JMR-20261026-R2 | 13,53 | [Hoja XP](https://docs.google.com/spreadsheets/d/18DYy3HRcy8SCBue16aBoba3ELBZ0pyjoFO472dic0-I/edit) | **La pestaña `Input sheet` y el resumen estándar están vacíos** en la lectura del 30-oct. El expediente FCFE del JSON contiene valoración propia, pero NO debe modelarse XP como empresa industrial usando esas celdas. Reconstruir FCFE/Ke desde datos bancarios, capital regulatorio y capacidad distribuible |

Todos los valores de esta tabla son **históricos, NO actualizados**. En particular, los precios de comparación congelados de UBER US$68,51 (30-sep), META US$648,85 (22-oct), NVDA US$210,96 (23-oct), XP US$15,37 (26-oct) **no son cotizaciones actuales**.

### Hallazgos económicos por emisor (fuentes primarias)

**UBER.** El 2T26 arroja ingresos US$14.191 M (+12%), gross bookings US$58.022 M (+24%), ingreso operativo GAAP US$1.890 M, y efecto positivo no operativo aproximado US$1.600 M por revaluación de inversiones dentro del beneficio neto. Fuente: [Uber 2T26](https://investor.uber.com/news-events/news/press-release-details/2026/Uber-Announces-Results-for-Second-Quarter-2026/default.aspx) y [SEC](https://www.sec.gov/Archives/edgar/data/1543151/000154315126000032/uber-20260630.htm). Implicación: crecimiento reservas ≠ crecimiento ingresos, utilidad no operativa no capitalizable como EBIT recurrente. La consolidación de márgenes exige evidencia de mix, tarifas y capacidad de monetización en movilidad/entregas. Sensibilizar competencia, automatización, regulación y S/C.

**META.** El 3T26 arroja ingresos US$64.601 M (+26%), margen operativo contable 20% afectado por US$9.890 M de cargos legales, CAPEX incluyendo principal de leases US$34.910 M en trimestre. Guía de CAPEX FY26 US$135.000–145.000 M. Fuentes: [SEC 10-Q](https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm) y [comunicado SEC](https://www.sec.gov/Archives/edgar/data/1326801/000162828026066700/meta-09302026xexhibit991.htm). Implicación: partir de EBIT normalizado, cuantificar cuánto de costos legales está ya dentro del balance y evitar descontar una segunda vez la obligación. I+D y CAPEX tecnológico no son sinónimos; las fábricas de cómputo se amortizan, la investigación sigue norma propia de capitalización económica. **No duplicar reinversión por S/C y CAPEX**. La financiación y clases de acciones requieren vigilancia al recalcular dilución.

**NVDA.** El 2T FY2027 (finalizado 26-jul-2026) presentó ingresos US$96.221 M (+106% a/a), segmento Data Center US$89.000 M (+117%) y guía de ingresos 3T FY2027 US$108.000 M ±2%. Fuentes: [resultados del emisor](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-Second-Quarter-Fiscal-2027/) y [SEC 10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm). Implicación: el crecimiento de infraestructura IA es real, pero el precio depende de permanencia de márgenes y ROIC; la sensibilidad debe incluir compresión de margen y cambios de volumen tras el ciclo de CapEx de clientes, competidores y restricciones de exportación.

**XP.** IR informa para 2T26 activos de clientes de **R$1.534 miles de millones**, revenue bruto LTM **R$20.200 M** y EBT LTM **R$6.000 M**; no confundir volumen de activos de clientes con activos propios. Fuente: [XP IR](https://investors.xpinc.com/en/). El FCFE debe partir de beneficios atribuibles, patrimonio regulatorio, consumo de capital por crecimiento y transferibilidad de dividendos. La revisión anterior deja explícita incertidumbre en puente CET1/Tier1 y distribución; por tanto, el método A financiero no se obtiene completando filas vacías de FCFF.

### Reglas económicas antes de elegir valor final

1. Para negocios industriales: DCF FCFF Base como valor principal; flujos año 1–10 e hipótesis de ROIC y reinversión terminal `g/ROIC`. Reconciliar `ΔIngresos / Sales-to-Capital` contra CAPEX neto + cambio capital de trabajo + intangibles, **no sumarlos**.
2. Para intermediación financiera XP: FCFE/Ke principal, patrimonio regulatorio y distribución sostenible; EV/EBITDA/EV/FCFF industriales no aplican.
3. Cuatro historias (Base/Conservador/Optimista/Disrupción), la última separada del promedio principal. Valor MOS35% calculado sobre **DCF Base de hoy**. Mostrar precio actual fechado, no usar el precio guardado como si fuera intradía.
4. Sensibilidades 5×5 de DCF: WACC terminal × g; ROIC terminal × g; ROIC terminal × WACC terminal; margen EBIT × crecimiento; margen EBIT × S/C; WACC inicial × crecimiento; impuestos × reinversión; peso terminal.
5. Múltiplos prioritarios: EV/EBITDA, EV/FCFF, P/E, P/FCFE y P/OCF donde sean económicamente aplicables. Sensibilidades de múltiplos del escenario Base, anclas de mercado y proyección de cada denominador. P/BV y P/S son complementarios, no condición de cierre.

## B. Estado editorial de los 23 análisis

**El objetivo no es insertar títulos vacíos.** El Nivel 1 debe explicar industria, negocio, ciclo de vida, macro/monetario/crédito, asignación de capital, ventaja/erosión competitiva, hipótesis cualitativas, tesis contraria, catalizadores y riesgos con fuentes verificadas; el Nivel 2 debe permitir reconstruir el precio por acción **desde las entradas efectivas**, fórmulas reales, proyecciones de flujos, puentes EV–equity, cuatro historias, sensibilidad DCF y múltiplos.

- Primer lote de profundización técnica: `MELI, CELH, ADBE, BSX, CMG, NFLX, GOOGL, MSFT, NKE, PYPL, EPAM, ZTS, ONON, NU, NVO, INTU` (16). Después `AFYA, DUOL, SHAK`. Hay que revisar también los cuatro estudios actualizados `UBER, META, NVDA, XP` para cerrar sus Niveles 1 y 2.
- La migración del índice de 18 a 13 capítulos **no constituye nueva investigación**. `docs/ESTILO_JMR_V19_MIGRACION_20261030.md` declara `structuralOnly=true` en expedientes reordenados y, en algunos, capítulos que necesitan investigación. `docs/ESTADO_MIGRACION_EDITORIAL_20261030.md` documenta migración alternativa a 18 títulos. Resolver el contrato editorial único en reglas, análisis y validador **sin perder el estilo de 18 capítulos solicitado** cuando corresponda.
- `DUOL` y `SHAK` ya tienen una revisión A-1.2 activa y **no deben reiniciarse sin causa**. Requieren control de fuentes, completar proyecciones y ajustar narrativa, sin hacer auditoría económica antes de la revisión visual.

## C. Gate de publicación y bloqueos

La revisión documentada en [PR #202](https://github.com/JuanMaRobledo/Modelo-JMR-datos/pull/202) identificó fallos de `validar_catalogo`, vínculos análisis–valoración, contrato de sensibilidad/múltiplos y discrepancias 13/18 capítulos. Su propia evidencia afirma: **6/23 pasan integridad individual y 17/23 bloqueados**, con gate global aún rojo. Esto impide presentar la mera existencia del JSON como publicación íntegra aprobada.

**Estado del presente cambio**: solo documentos de investigación en rama independiente. No modifica ningún registro activo ni merge, no declara verificación por CI, no sustituye auditoría económica. Siguiente paso operativo seguro: construir cada valoración en copia de la plantilla oficial, verificar datos/cálculos/contratos, unir con artículo completo y luego publicar `EN_REVISION` únicamente si supera los controles; auditoría económica posterior a la revisión visual del usuario.
