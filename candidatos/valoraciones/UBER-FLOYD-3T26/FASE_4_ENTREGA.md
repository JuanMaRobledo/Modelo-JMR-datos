# F4 · UBER-FLOYD-3T26 · CANDIDATO

- Corte contable 30-sep-2026. Cierre de mercado US$68,59, 6-nov-2026.
- Valoración: https://docs.google.com/spreadsheets/d/1jMzDqRnTiBdbeFJmB0UH4aLdthBtC1JtiRhl8PEQBcg/edit
- Análisis: https://docs.google.com/document/d/1KGzxUKOCrpyqG0cgo84eTC9lFMPN_D_1VZS87QMK2mE/edit
- Históricos: https://docs.google.com/spreadsheets/d/1m19UGgqKLS5dhkBjABTxh8fyzD3vrxXAqsefq9OXn24/edit
- AISLAMIENTO=OK para esta exportación: mismo ticker, revisión y sheet_id en los dos JSON. El catálogo principal conserva la revisión activa anterior.

## Controles comprobados

1. Paridad DCF inverso con B35: 100,19381867706664 USD/acción. Las tres soluciones reproducen 68,59 a precisión numérica.
2. Escenarios: Conservadora 48,64133539, Base 100,19381868, Optimista 145,0858766. Probabilidades 25 %, 50 %, 25 %. Promedio 98,52871233. MOS 35 %: 65,12598214.
3. Tres matrices DCF de 5 × 5 con centro igual al Base. Cinco matrices de múltiplos de 5 × 5 con centro igual al VP3 de cada método. Normalización DCF probada usando la función vigente de `docs/expediente.js` en Node. Esta prueba no sustituye la ficha completa en el visor.
4. Huella nativa reportada: 0 diferencias de 1.883 fórmulas. El JSON y el análisis coinciden en revisión, hoja, Base y MOS.
5. SHA-256 de las exportaciones:
- `162e5c9fcdd0843dc790e03528e27b37fd3b33609a393dfe2f8706f58a5ff1c2  valoracion.json`
- `7fc2d5c871daa53992205bdb3cab940c2108172c8799e6fa3e79d581475f2514  analisis.json`

## Puertas pendientes o fallidas

- FALLA reproducida al ejecutar `offline` de `JMR-valuation/scripts/consistencia_migracion.py` sobre los dos JSON: `{'M1': False, 'M2': False, 'M3': False}`. M1 y M3 aún exigen Disrupción separada y métodos opcionales P/V y P/BV. M2 usa identificadores A/B/D para el promedio y no reconoce el tercer escenario Floyd (C). El promedio y el MOS sí pasan la comprobación numérica independiente.
- NO EJECUTADO como gate aprobatorio: batería completa con ruta Floyd para probabilidades, historia a números e integridad, conciliación completa en visor/preview y CI de promoción. El módulo de múltiplos del visor oculta candidatos sin validación de publicación. No habilitarlo con indicadores ficticios.
- PARCIAL: actualización del artículo y anexo. El análisis conserva apartados pendientes en industria/TAM, macro/mercado y gobierno. Revisión económica independiente F5 pendiente.
- Conclusión: CANDIDATO. Adaptar y probar el contrato de publicación Floyd, completar el cierre editorial y verificar la ficha en preview antes de reemplazar el catálogo.

PASOS F4: 3/5 de esta entrega ejecutados (reconciliación de valores, actualización parcial del análisis, exportación y prueba local). Integración de producción y publicación pendientes. Herramientas: conector Sheets/Docs, Node 24 y Python 3.12, ChatGPT Work.
