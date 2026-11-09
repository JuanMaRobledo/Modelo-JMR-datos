# F4 · Análisis fundamental y publicación · AAPL-FLOYD-FY26-R1
Estado: **EN_REVISION preliminar (registrado en catálogo, 9-nov-2026). F5 independiente PENDIENTE; QA visual en la app NO realizado.**
Agente: Claude (Claude Code; modelo configurado claude-sonnet-5-5; esfuerzo no identificable). Acceso real: Sheets, Docs y Drive (lectura/escritura), SEC (data.sec.gov), FMP (precios), Alpha Vantage (cotejo secundario); sin Vercel/app.

## Entregables
- H1 Históricos: https://docs.google.com/spreadsheets/d/1MHlhgbWgRGysN11_LnyBS94aueV4KijXnqKvLhN5U98/edit
- H2 Valoración/Presentación: https://docs.google.com/spreadsheets/d/1gtAc2TclEjszznAC8tfDGiOviq3bagTA7AzOh2r1h0c/edit
- H3 N1 (14 capítulos) + N2 (12 apartados): https://docs.google.com/document/d/1SfPYnHbSKUh7_0ziFsPTYOI5gIg-pRJDLIb8P2gU-xs/edit
- Registro: `valoraciones/AAPL-FLOYD-FY26-R1.json` + `analisis/AAPL-research-AAPL-FLOYD-FY26-R1.json`; `catalogo.json` v. FLOYD-UBER-CMG-AAPL-20261109-R4.
- La ficha A-1.2 anterior (AAPL-20261103-A12-R1) permanece en `archivoFloyd`; no se borró.

## Controles (APROBADO / PARCIAL / NO_EJECUTADO)
- Cotejo H1 FY2017-FY2026 vs XBRL de los 10-K (SEC): **APROBADO** 168/170; 2 reexpresiones de FY2017 (CFO 63.598 vs 64.225; cuentas por pagar 49.049 vs 44.242), H1 usa el 10-K original.
- Huella motor H2 (0 dif./1.883 fórmulas), 3/3 historias LISTO: **APROBADO**. Comparación celda a celda contra la Maestra: **NO_EJECUTADO**.
- Tres matrices DCF y cinco de múltiplos con centro conciliado: **APROBADO**.
- `node scripts/validar_catalogo.cjs`: **APROBADO**. `node scripts/validar_profundidad_floyd.cjs`: **APROBADO** con PENDIENTE_EDITORIAL (Nivel 1 = 2.246 palabras < 7.500).
- `scripts/tests/validar_catalogo.test.cjs` 6/6 (se actualizó la lista fija de empresas Floyd activas a UBER, CMG, AAPL); `dcf_fcfe_informativo`, `validar_matrices_nativas`, `contrato_nativo_a12`, `cmg_dcf_export` en verde. Fallos preexistentes en `main` sin relación (amzn_r5, auditar_ponderaciones, capturas_matrices_fuente, meta/nvda/xp/pags, relativos_revision): idénticos antes y después.
- Pruebas de la app (Modelo-JMR, `npm test`): **203/203** (instalando linkedom sin guardar en package.json).
- CI en PR, despliegue y comprobación de la ficha en la app/Vercel: **NO_EJECUTADO**. QA visual autenticado: **NO_EJECUTADO**.

## Reservas (también en `salvedades` del JSON)
Limitación I+D año −1 (+0,7 % Base); AVISO ROIC año 10→terminal; TAM N/D; Nivel 1 corto (2.246 palabras); EV FY2017-20 N/D; NCI/preferentes = 0 sin cotejo por año; F5 pendiente.

## Primer siguiente paso
Abrir PR de la rama `ccr-fe43c63f-s172pu` (Modelo-JMR-datos), esperar CI, desplegar y confirmar la ficha AAPL en la app; luego F5 en sesión independiente. Ampliar el Nivel 1 hasta ≥ 7.500 palabras si se quiere cerrar PENDIENTE_EDITORIAL.
