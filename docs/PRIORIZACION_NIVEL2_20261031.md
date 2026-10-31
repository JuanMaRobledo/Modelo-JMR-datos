# Modelo JMR — revisión de cobertura del Nivel 2 (31-oct-2026)

**Estado:** inventario técnico de lectura de los 20 expedientes Método A-1.2 en la rama del PR #211. No es auditoría económica, no valida cada fórmula ni autoriza fusión o publicación. El umbral de 7.500 palabras corresponde solo al **Nivel 1**, nunca al Nivel 2.

## Resultado de revisión documental

Todos los 20 JSON de análisis del catálogo se pudieron abrir, contienen `calculationHtml`, están vinculados a una valoración del mismo ticker y tienen `articleHtml` y `calculationHtml` incorporados al `html` completo. Esto comprueba presencia y enlace documental, **no** coherencia entre proyecciones y celdas.

| Expediente | Tamaño aproximado de Nivel 2 HTML | Tablas HTML | Prioridad |
| --- | ---: | ---: | --- |
| NU | 6,5 k caracteres | 5 | P1: contrato FCFE bancario, P/E, P/FCFE y P/BV |
| GOOGL | 8,1 k | 6 | P1: anclas y proyecciones P/E, P/FCFE, P/OCF |
| INTU | 9,5 k | 9 | P1: cuadros exploratorios no integrados, sin 5 matrices nativas oficiales |
| NVO | 13,5 k | 11 | P2: escenarios/ponderaciones nativos incompletos; P/BV N/D |
| MELI | 15,9 k | 13 | P1: FCFF/FCFE negativos y aplicabilidad por negocio mixto |
| ZTS / ONON / MSFT / PYPL / EPAM | 18–19 k | 13 cada uno | P2: escenarios, ponderaciones y conciliaciones relativas |
| UBER | 24,3 k | 12 | P1: cinco anclas relativas sin alimentar |
| SHAK | 28,0 k | 17 | P1: dos múltiplos N/D por flujos negativos; exportación oficial |
| CELH / BSX / CMG / NFLX / NKE | 23–25 k | 18 cada uno | P3: auditoría de anclas, fuentes y conciliaciones |
| ADBE | 62,6 k | 29 | P3: validar consistencia y fuentes, preservar análisis extenso |
| AFYA | 213,4 k | 50 | P2: ya ampliado en 12 apartados; cotejar impuestos, canje y fórmulas |
| DUOL | 222,4 k | 56 | P2: ya ampliado en 12 apartados; cotejar SBC, I+D y anclas |

**Nota metodológica:** los tamaños y tablas solo miden volumen documental, no calidad. Los 20 documentos mantienen salvedades de investigación y/o datos. Algunos encabezados de los N2 antiguos no usan IDs `jmr-calc-1..12` pese a contener secciones y tablas: no contar esta ausencia como un defecto financiero sin cotejar el HTML real y sus anclas.

## Orden de regularización

1. Resolver seis bloqueos financieros SHAK, MELI, GOOGL, UBER, INTU, NU desde hoja oficial y revisión exacta. Mantener `N/D` si falta el dato; no poner ceros. Para SHAK/MELI, `N/A` solo si el flujo negativo y la no aplicabilidad están fundamentados sin peso. Para NU aplicar FCFE bancario, no flujos industriales.
2. Completar descuentos Conservador/Optimista y pesos que faltan en EPAM, MSFT, NKE, NVO, ONON, PYPL y ZTS desde Sheets, sin recalcular precios artificialmente ni modificar supuestos durante depuración.
3. Revalidar Nivel 2 de los 20: fuente de estados y ajustes, fórmulas realmente utilizadas, cuatro escenarios, puente de empresa a equity, sensibilidad DCF y por método, pesos y diferencias FY+3 frente a valor presente. Cuando falten celdas o anclas, anotarlas por ticker y revisión.
4. Realizar QA visual de #151 con fuente de datos alineada a #211, acceso SSO válido y evidencia en móvil/escritorio. Solo tras gates y QA considerar fusión, con auditoría económica independiente posterior a la revisión visual del usuario.

## Precisión sobre INTU

El análisis heredado incluía el título «seis matrices Base validadas» para un contraste basado en una hoja alternativa, pese a que el JSON oficial de la revisión no incorpora las grillas 5×5 Base requeridas. Se cambió el rótulo por «seis matrices de contraste pendientes de integración oficial» y se añadió advertencia explícita. **No se alteraron sus cifras ni el DCF.**

## Nivel 1 editorial

En el último workflow de profundidad, los 20 expedientes cumplen el mínimo de extensión. Casos profundizados y verificados: SHAK 8.034, UBER 8.218, AFYA 8.146, DUOL 8.502 palabras. El Nivel 1 todavía necesita revisión semántica específica de cobertura de fuentes y capítulos; un conteo aprobado no certifica investigación suficiente.

Documentación de estado más reciente: [AVANCE_ESTANDARIZACION_20261031.md](AVANCE_ESTANDARIZACION_20261031.md). Mantener PR #211 en borrador mientras el gate financiero falle.
