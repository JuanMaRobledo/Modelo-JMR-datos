# KO · KO-20261103-A12-R1 · F4 · VALIDACIÓN PARCIAL
Fecha: 04-nov-2026. Método A-1.2. AISLAMIENTO=OK.
Hoja: https://docs.google.com/spreadsheets/d/17bX2bK0z1LSxO02GGv7HDFpAU6f8hkxIH4rUMdfnyEE/edit
PR #244. Constructor ChatGPT Work; esfuerzo interno no expuesto.

## Resultado vigente
DCF Base US$59,49298288; MOS35% US$38,67043887.
Conservador40,20535617; optimista71,71935197; disrupción30,86592400.
Rf5,29% y ERP4,41%, par mensual Damodaran 01-nov. WACC inicial7,740507351%, terminal8,99%. Crecimiento -3% año1 y5% años2–5; margen terminal33,5%; S/C1,7/1,6; ROIC marginal18%; g4%.
Los valores anteriores64,026942/41,617513 son históricos sustituidos.

## Comprobaciones ejecutadas
- Hoja/JSON: PV explícito91669,354811 + PV terminal146783,514899 = EV238452,869710 millones. Puente patrimonial y acciones concilian dentro de1e-8 USD/acción.
- Tres centros DCF y cinco centros relativos conciliados. Matrices recapturadas tras corregir tasas.
- Comparación 7882 fórmulas,46 pestañas, primeras400 filas según alcance del script oficial: cero fórmulas reemplazadas por números/borradas;16 reescrituras de históricos y11 encabezados documentados.
- Nivel1:14 capítulos; Nivel2 ampliado con cuatro DCF completos, tres estados históricos y matrices.
- Cotejo SEC nuevo:297 comprobaciones de27 métricas principales FY2016–2025 yLTM.290 coinciden con último dato seleccionado;7 coinciden con informes originales y difieren de presentaciones posteriores. Se conserva la base originalmente publicada. Evidencia COTEJO_SEC_297_20261104.json incluye etiquetas, celdas y accession. Este alcance no es un cotejo de cada nota/subpartida.
- Integridad catálogo y no-regresión aprobadas; registro regenerado con script oficial.
- Fuentes Damodaran aplicadas en APLICACION_DAMODARAN_20261104.md. Las aproximaciones y el estrés fiscal condicional no son probabilidades externas ni nuevas cifras certificadas.

## Verificación app: BLOQUEADA POR AUTENTICACIÓN
Producción Vercel observada READY, dpl_2pyi9qL6ksjnY2kfxygNfPFFrpry, commit app588ee9bd2a460eb20007fcf543d46513ffbed594.
Se intentó acceso mediante conector Vercel, que creó enlace temporal; falló tras redirección con401 deployment_authentication_required. Fallback CLI instalado y ejecutado: vercel whoami informa Logged out. No se desactivó protección ni se declaró QA aprobada.
KO sigue en rama candidata: no hay publicación efectiva ni evidencia visual de la ficha KO en producción.

## Límites de la entrega
No equivale a cierre integral de publicación: el cotejo SEC cubre métricas principales, y el tratamiento de perímetro CCBA/Asia, participaciones y contingencia fiscal conserva aproximaciones explícitas de valoración. No se emite dictamen independienteF5. Los controles no ejecutados no quedan aprobados por CI.
