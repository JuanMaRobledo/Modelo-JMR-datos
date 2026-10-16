# CMG, DUOL, NKE y NFLX · auditoría16-oct-2026

Se ejecutaron los auditores oficiales de estructura y fórmulas y una conciliación numérica independiente de los cuatro DCF, FCFF después de impuestos/NOL, valor presente, puente a patrimonio, opciones y WACC. Pasaron598 controles numéricos. Los cuatro valores Base publicados coinciden con las hojas y no se modifican.

|Activo|DCF Base USD|MOS nativo|Umbral USD|
|---|---:|---:|---:|
|CMG|23,99143407|35%|15,59443214|
|DUOL|108,27931647|35%|70,38155570|
|NKE|33,59021463|35%|21,83363951|
|NFLX|71,68383444|35%|46,59449239|

Correcciones: MOS exclusivamente sobre el DCF Base en resumen y descuento de múltiplos; sincronización del35% de la hoja NFLX frente al25% antiguo del artículo; precio congelado NFLX70,57 frente a fórmulas GOOGLEFINANCE en el resumen; NKE sincroniza campos del DCF inverso con CAGR implícito1,9425% y Base1,0086%; el visor conserva los cuatro escenarios NFLX sin probabilidades ni promedio inventado. Se archiva el JSON DUOL antiguo y se conserva el vigente enlazado al artículo.

Verificación visual: cuatro importaciones XLSX en el visor del código propuesto, sin errores JavaScript. Pasan tablero, etiqueta, resumen y MOS; se revisaron capturas y PDF. La sesión privada de producción no está disponible para revisión visual autenticada.

Evidencia: https://github.com/JuanMaRobledo/JMR-valuation/actions/runs/38921709636

## Resultado de controles oficiales

No se declara certificación completa. CMG, DUOL y NKE tienen28 discrepancias de fórmulas canónicas cada una, principalmente guardas introducidas después de construir las hojas. NFLX tiene24 discrepancias y carece de la pestaña industrial Escenarios e historias: usa Escenarios JMR NFLX sin probabilidades justificadas. Estos hallazgos no equivalen por sí solos a un error de suma del DCF, pero impiden pasar el gate vigente.

Las probabilidades de CMG, DUOL y NKE sí suman100% en la conciliación independiente. El preflight antiguo informa probabilidades incompletas en CMG/NKE porque exige una columna de estado que todavía no existe en ellas. No se rellenan estados falsos para hacerlo pasar.

Pendientes concretos:

- **CMG:** migrar guardas WACC, fiscales, activos no operativos y casos especiales; completar manifiesto de fuentes; mantener explícita la estimación del ajuste EBIT de leases frente al pasivo conciliado.
- **DUOL:** migrar guardas sin sobrescribir B111:B112, que contienen CAGR conservador8% y optimista17%; completar conciliación de leases y activos no operativos, controles fiscales y evidencia de proxies WACC.
- **NKE:** migrar guardas y evidencia de fuentes; conciliar PV del calendario de leases frente al pasivo reconocido. Mantener expuestos proxies regionales y cargos Pace.
- **NFLX:** validador compatible con sus cuatro escenarios sin probabilidades; migrar controles sin pisar la trayectoria en B120:B153; sustentar volatilidad45% y vida4,79 usadas en opciones, además de conciliar leases/claims. No cambiar a VALIDADO sin esas pruebas.
- **Los cuatro:** revisión visual con sesión autenticada en producción.

Las hojas vigentes se editaron en su misma identidad; no se borraron hojas. Celdas y JSON anteriores se conservan bajo `respaldos/2026-10-16/cuatro-activos/`. Los informes oficiales y numéricos detallados se guardan junto a este documento.
