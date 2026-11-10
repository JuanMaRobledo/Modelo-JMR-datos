# MELI · Continuación de reinicio · MELI-20261028-R1

**Corte financiero:** 30-06-2026. **Estado:** EN_PREPARACION. **App:** NO PUBLICADO. **Auditoría económica:** diferida, a petición del usuario.

## Qué está realmente hecho

1. Localizada la hoja nueva, aislada, con fórmulas originales y ahora evidencia contable: https://docs.google.com/spreadsheets/d/1Td7E4awGlz-glT-n6KEG9lwKRvA9g5RY_uKf7cEEN30/edit.
2. Incorporados estados consolidados SEC FY2022–FY2025, más los balances a junio 2026 y la síntesis LTM. El 10-K FY2024 reexpresa cuentas de 2022-23; FY2022 balance procede de 10-K FY2023 y tiene comparabilidad señalada.
3. Nueva pestaña `MELI · SEC 2026-06`: cálculos LTM, información operacional, segregación preliminar del financiamiento, notas de origen y puentes por resolver.
4. Confirmada conciliación de activos=pasivos+patrimonio para 2022 (13.736 = 11.909+1.827), 2023 (17.612 = 14.541+3.071), 2024 (25.196=20.845+4.351), 2025 (42.667=35.919+6.748) y jun 2026 (51.356=43.522+7.834). Unidades US$ millones.

## Diagnóstico fundamentado (NO equivale a resultado de DCF)

- Ingresos LTM USD 35.182 M, EBIT 2.907 M (8,26 %), utilidad neta 1.863 M. FY2025 margen EBIT 11,08 %. El efecto de crecimiento de ingresos convive con compresión de margen por envío gratuito en Brasil, logística, financiación y mayores provisiones.
- Ingresos H1'26 19.014 M frente a H1'25 12.725 M; en Q2'26 GMV 21.926 M, TPV 100.952 M, EBIT 683 M (margen 6,7 %). Commerce crece 48,8 % e ingresos Fintech aproximadamente 50 % interanual en H1.
- **Bandera roja del DCF:** CFO LTM 13.905 M − capex 1.496 M = 12.409 M, pero el flujo está afectado por saldos de clientes, proveedores de pagos, cartera y fondeo Fintech. El flujo ajustado definido por el emisor es 1.127 M LTM, también distinto de FCFF de Damodaran. Ni uno ni otro se debe transcribir sin reconciliación.
- A junio 2026: fondos de clientes 16.035 M, caja restringida 13.114 M, deuda contable mixta 10.626 M, y leases 2.550 M. Separar flujos y deuda de comercio/corporativo frente a financiación Fintech; fuente 10-Q 2026, notas 10-11 y conciliación ajustada de liquidez.
- Producto y Tecnología FY2025 2.269 M y H1'26 1.428 M frente a H1'25 1.118 M. No es gasto homogéneo de I+D capitalizable: incluye sueldos, depreciación, mantenimiento y uso de IA. La prueba `R& D converter` debe identificar componente plurianual y reconciliar EBIT, activo intangible y reinversión.
- Arrendamientos ya reconocidos ASC842: no volver a convertir/reducir deuda dos veces.
- Las cuentas de resultados son geográficamente reportadas en Brasil, México, Argentina y otros; Commerce y Fintech son cortes económicos del negocio y requieren conciliación de costes internos antes de un DCF sum-of-parts.
- El 01-01-2026 Ariel Szarfsztejn asumió la dirección ejecutiva y el fundador Marcos Galperin pasó a presidente ejecutivo del consejo.

## Hipótesis de trabajo (juicio, no estimaciones finales)

**Base:** red Commerce, logística y pagos mantienen crecimiento superior al mercado; la cartera de crédito aporta penetración pero requiere capital y provisiones; la presión por envíos se modera gradualmente, sin suponer que retorne automáticamente el margen FY2023.

**Conservadora:** mayores gastos logísticos y de distribución, presión de precios y mayores pérdidas crediticias reducen la conversión del crecimiento en FCFF, con costo de capital congruente y sin doble aplicar riesgos.

**Optimista:** volumen y fidelización sostenibles con apalancamiento operativo de logística, publicidad y eficiencia de distribución financiera, siempre con evidencia explícita de margen/ROIC/capital.

**Disrupción:** deterioro duradero de crédito/financiación o competitividad, tensión de capital y pérdida de eficiencia del ecosistema. Se muestra aparte y no entra en promedio ordinario.

Estas historias son cualitativas y **todavía no tienen inputs numéricos validados, probabilidades ajustadas ni precio por acción**.

## Candados y próximos pasos técnicos en orden

1. Completar FY2016–2021 y conciliación de reclasificaciones de presentación FY2022–2023; cotejar activos/fondos vinculados a clientes por año.
2. Construir puente Fintech vs Commerce/Corporate con notas 10, 11 y Adjusted FCF; distinguir lending como capital operativo financiero y dejar transparencia en rentabilidad y deuda por componente.
3. Determinar alternativa de valoración consistente con §1 y §4A de REGLAS_VIGENTES v14: DCF principal con FCFF operativo y tratamiento separado no duplicado de riesgo financiero, con referencia sectorial y país.
4. WACC exclusivamente `Cost of capital worksheet` en modo Detailed y multibusiness solo con ventas/betas trazables; costo marginal de deuda, pesos de mercado y ERP/Rf misma fecha.
5. Capitalizar I+D elegible, conciliar leases ASC842, derechos SBC/options, reinversión, ROIC y sales-to-capital sin doble conteo.
6. Rellenar cuatro DCF, los siete múltiplos de las hojas de la plantilla con fórmulas, DCF inverso y sensibilidades 5×5 solo Base. Completar el artículo en 18 secciones y 2 niveles, con ambas versiones de múltiplos del Base.
7. Ejecutar integridad, 18 candados, origen de fuentes, controles de supuestos, coincidencia hoja↔JSON↔app y `bash scripts/controles_todas.sh`. **Solo si todos pasan, publicar juntos como EN_REVISION.** El dictamen económico permanece sin realizar hasta auditoría visual.

## Referencias primarias

- sec_2025_10k: https://www.sec.gov/Archives/edgar/data/1099590/000109959026000006/meli-20251231.htm
- sec_2026_10q: https://www.sec.gov/Archives/edgar/data/1099590/000109959026000023/meli-20260630.htm
- sec_2024_10k: https://www.sec.gov/Archives/edgar/data/1099590/000109959025000007/meli-20241231.htm
- sec_2023_10k: https://www.sec.gov/Archives/edgar/data/1099590/000109959024000008/meli-20231231.htm
- sec_q2_2026_letter: https://www.sec.gov/Archives/edgar/data/1099590/000109959026000021/meli-20260805xex991.htm
- sec_proxy_2026: https://www.sec.gov/Archives/edgar/data/1099590/000109959026000010/meli-20260423.htm
