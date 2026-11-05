# CMG-20261105-A12-R4 — CANDIDATO, NO PUBLICAR

Método A-1.2; corte financiero30-sep-2026; mercado04-nov-2026. AISLAMIENTO=OK.

Base del auxiliar económico24,310268 USD; MOS35%15,801674 USD. Cuatro historias calculadas. La copia oficial NO concilia por referencias previas rotas y adaptación de leases: no se puede promover.

Hoja candidata: https://docs.google.com/spreadsheets/d/1yKVuNYzxq-89qwyh0DvPbN64qrA1BdnJ_YZc29LlID8/edit

Auxiliar económico: https://docs.google.com/spreadsheets/d/1tC2y4OwTBkmQq8xD_TGOOgbOuYmW1SWSFnY0GNzJCPI/edit

Informe completo: CMG_R4_ANALISIS_NIVEL_1_2.md. Cálculos y fuentes: results.json y scripts auxiliares. verification.json documenta comprobaciones equivalentes y límites; official_attempts.json contiene los errores reales de lanzamiento de scripts oficiales. No es una auditoría F5 independiente.

No cambia catálogo, valoración publicada ni aplicación. No hay PR de publicación porque no se superaron los controles.

## Cierre adicional ejecutado

- Transición marginal 19,425% → 14% en cinco/diez años: US$24,572300 / US$24,800383.
- Erosión completa del exceso de ROIC hasta WACC: US$20,693394 / US$21,139241.
- Residuales LTM expuestos, sin clasificación inventada: pasivo lease +US$30,952345M; ROU −US$5,672233M.
- OCF normalizado corregido por ΔNWC; SBC permanece como costo.
- 18/18 comprobaciones del cierre pasan; varias repiten controles previos y no deben sumarse como 47 pruebas independientes. No certifican la suite oficial.

Reproducción local del cálculo: ejecutar model.py, build_spec.py, add_audit.py, close_review.py y build_workbook.mjs en ese orden. Python requiere openpyxl para el informe/verificación; Node usa @oai/artifact-tool. Los scripts resuelven datos relativos a su propia carpeta salvo build_workbook.mjs, cuyo directorio de trabajo debe adaptarse al checkout. Para verificar Google Sheets, exportar el auxiliar a aux_native_final.xlsx y ejecutar verify_close.py; después write_report.py. La exportación nativa es evidencia fechada, no se regenera mediante la copia local del motor. El verificador usa tolerancia relativa 1e-9 por precisión del caché XLSX.

closure_results.json: cálculo independiente. closure_native.json: fórmulas y valores nativos leídos. closure_verification.json: controles y hash del export. El auxiliar contiene11 pestañas JMR; la copia oficial conserva51.

## Promoción bloqueada

La referencia Valuation output!M14 suma Country equity risk premiums!B1, que devuelve texto CMG; la referencia de prima numérica está desplazada. Además, activar el conversor puede sumar otra vez deuda lease ya reconocida. No se modifican fórmulas originales para ocultar ninguno de los problemas.

Pendientes materiales: integración IA y conciliación de su salida; cierre del recast estimado y renovaciones/altas; anclas económicas de múltiplos; historia financiera y controles oficiales. La transición terminal queda cuantificada como sensibilidad, sin atribuir certeza a la persistencia del ROIC14%.

Estado final: ENTREGADO COMO CANDIDATO CON RESERVAS. Sin PR de publicación, fusión ni despliegue.
