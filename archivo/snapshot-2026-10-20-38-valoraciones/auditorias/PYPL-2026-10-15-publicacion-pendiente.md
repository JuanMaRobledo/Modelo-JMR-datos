# PYPL · Prepublicación JMR · 15-oct-2026

**Estado: BLOQUEADA POR PREFLIGHT (no publicar ni hacer merge hasta cerrar controles).**
**Autorización de publicación recibida del usuario:** sí, 15-oct-2026.
**Alcance:** actualización PYPL exclusivamente, sin alterar otros tickers ni la plantilla maestra.

## Fuentes de la versión propuesta
- Hoja de trabajo independiente: https://docs.google.com/spreadsheets/d/1LI1LHXYFiCqg5i1_DDzs53Rd4eKv4zhDex2pxSvKuCs/edit
- Artículo íntegro nivel 1 + cálculos nivel 2: https://docs.google.com/document/d/1sJZi5I3dI1Lv02nr5mrkT4bOVrXY91fPaXqxAaINqTc/edit
- Fuente financiera: 10-Q al 30-jun-2026, https://www.sec.gov/Archives/edgar/data/1633917/000163391726000082/pypl-20260630.htm
- Precio de cierre, 15-oct-2026, US$57,16: https://stockanalysis.com/stocks/pypl/history/
- Treasury a 10 años, 15-oct-2026, ~5,086%: https://www.wsj.com/livecoverage/stock-market-today-dow-sp-500-nasdaq-10-15-2026

## Resultados derivados (preliminares)
| Concepto | Valor |
|---|---:|
| DCF Base US$/acción | 100,8559361529 |
| Conservador US$/acción | 68,91 |
| Optimista US$/acción | 136,03 |
| Disrupción US$/acción | 39,29 |
| Promedio de historias (solo informativo) | 88,91 |
| Precio de cierre 15-oct-2026 | 57,16 |
| MOS | 35% |
| Precio con MOS referido al DCF Base | 65,5563584994 |
| WACC inicial | 8,204991704968359% |
| WACC terminal | 8,99% |
| g terminal | 3% |
| ROIC marginal terminal | 15,582150210969634% |
| DCF inverso, delta común tasas años 1–5 | −12,4021325236 pp |
| CAGR 5 años Base / inverso | 4,9005139195% / −7,5016186051% |
| Reproducción DCF | error < 0,001 USD/acción |
| Sensibilidades | tres matrices centradas y consistentes |

### Discrepancia actual que la republicación deberá corregir
- Registro producción: `valoraciones/PYPL-1790205796042.json` (blob inicial `545944b72cf900031a9bd78330435ba3dae551ba`) incluye Base histórico US$119,698374, `baseMOS=valorEsperado`, `precioMOS=66,4294`, y datos desactualizados; **no modificar parcialmente**.
- Research producción: `analisis/PYPL-research-1790205847031-vcqtg.json` (blob inicial `9009522847b574e636147db097e6326277d7f3ce`) sigue referenciando el Base histórico y el snapshot anterior.
- El DCF Base actual de la hoja de trabajo es **100,855936**, sin utilizar el promedio para MOS.
- Se requieren los valores recalculados en TODO el paquete (escenarios, matrices, crecimiento implícito, comparables, zonas, tarjeta PDF, artículo y cálculo) y no una sustitución aislada de los números en JSON.

## Controles obligatorios NO APROBADOS en la copia de PYPL
- [ ] `Input sheet!B81`: arrendamientos reconocidos vs conversor, pasivo incremental y EBIT incremental, no doble conteo.
- [ ] `Input sheet!B85`: activos no operativos US$1.735 M, valor económico vs importe contable y exclusión del capital invertido.
- [ ] `Input sheet!B92`: impuestos efectivos/marginales, tasa de arranque y convergencia con fuente.
- [ ] `Input sheet!B108`: NOL, fracaso, I+D, acciones/opciones/RSU y preferentes/convertibles; fuente 10-Q y efecto de dilución, sin doble restar SBC.
- [ ] `Cost of capital worksheet!B84`: estado VALIDADO, con Rf/ERP beta por negocio, Kd preimpuesto de fecha comparable y E/D/P.
- [ ] `Escenarios e historias!K5:K8`: controles LISTO individuales de cuatro historias; comprobar liberación de capital en la disrupción.
- [ ] Manifiesto de fuentes PYPL y preflight `scripts/audit_dcf_certificado.py` completado contra la hoja candidata.
- [ ] Multiplicadores históricos/pares homogéneos auditados: el anexo FY+3 actual contiene proxies, no múltiplos LTM de mercado verificados.
- [ ] Verificar actualizaciones del documento vs 10-Q: claims de caja libre, SBC, recompras y deuda.
- [ ] Ejecutar `implied_growth.py` contra hoja guardada y comparar con el inverso independiente (−12,4021 pp), y reproducir precio dentro de US$0,001.
- [ ] Volver a generar el JSON completo del visor desde la hoja, sincronizar research, bitácora y tarjeta PDF, en vez de editar cifras sueltas.
- [ ] Validación estática y visual de la app (incluye enlaces «Ver cálculo» y PDF con tarjeta).
- [ ] Confirmar estado integrado/desplegado/visible y snapshot de versión SHA.

## Regla de despliegue
No hacer merge ni publicar este PR como sustituto del control. Usar `JMR-valuation/scripts/desde_cero.sh validar` con manifiesto PYPL y los controles del archivo `reference/protocolos/JMR_DAMODARAN_CONTROL_CERTIFICADO_2026-10-12.md`. Ejecutar `app --autorizar-publicacion` solo cuando los gates estén aprobados. Este manifiesto es una preparación trazable, NO un registro publicado, NO un análisis certificado.
