# DUOL · JMR Atlas R1 — publicación solicitada, bloqueada por puertas materiales

**Fecha de revisión:** 2026-11-05 (Colombia) · **Corte financiero:** 2026-09-30 · **Corte de mercado:** 2026-11-05
**Estado:** CANDIDATO / NO PUBLICAR. **No modificar** `catalogo.json`, `valoraciones/`, `analisis/` ni la ficha activa DUOL R2 mientras las puertas siguientes no estén superadas.

## 1. Entregables revisados
- Datos Atlas: https://docs.google.com/spreadsheets/d/1f3lPGhv8Lx0DzrA-vwXbLlD5JxzTcjPtj_Nn026mZJA/edit
- DCF Atlas: https://docs.google.com/spreadsheets/d/1YPtE7UWhIPCMhiENnRNCe-jX8mzoGEnjpv78P6TdNt4/edit
- Múltiplos y ponderación: https://docs.google.com/spreadsheets/d/1K0yBSETJQkWjdAHRy6Os-3iQ5dmHW_bc88LTMXhUxYU/edit
- Nivel 1: https://docs.google.com/document/d/1vJtGag0P7q8QRmHpz4WyNxfQDihK5KlEm9jtjIUAvZI/edit

## 2. Valoración actual de Atlas (NO CERTIFICADA)
DCF Base **US$108,7473**; MOS 35% **US$70,6857**. Conservador US$69,0562; Optimista US$168,3179; esperanza condicional 25/50/25 US$113,7172. Stress IA no ponderado US$58,3131. Contraste con DUOL R4 Base US$111,4427: no se calibró al precio. La app vigente mantiene DUOL R2, Base US$139,1087 y MOS US$90,4206 hasta una promoción válida.

La ponderación **específica de DUOL** que se ha cableado en la hoja Atlas es 60% DCF y 40% múltiplos. Dentro del bloque: EV/FCFF 37,5%, EV/EBITDA 25%, P/E 12,5%, P/FCFE 12,5%, P/OCF 12,5%. En términos globales: 60%, 15%, 10%, 5%, 5%, 5%; P/S y P/BV con 0%. Son pesos de trabajo basados en DUOL R2 y deben ser ratificados por razones económicas para Atlas; NO se han copiado los valores relativos de R2.

**Punto crítico:** los 5 valores presentes por múltiplos de Atlas son N/D. No existe aún mediana de pares certificada ni combinación DCF + múltiplos válida. El libro 03 ya contiene las fórmulas y las casillas de fuente/validación, el P/OCF y la ponderación global, pero *no* tiene derecho a producir un valor relativo numérico.

## 3. Puertas por cerrar (orden)
1. **Marco de descuento y etapas:** El DCF Atlas usa g terminal 3% y diferentes WACC iniciales por escenario, mientras `modelo/REGLAS_VIGENTES.md` §2/§4 exige costo de capital común entre historias y g nominal USD 4% (si no hay excepción aprobada). El Rf 4,84% de 2026-11-05 y ERP 3,70% de 2026-10-01 no comparten corte; rehacer la reconciliación con `Cost of capital worksheet`, beta/ERP y estructura de capital. Revisar el peso terminal.
2. **I+D rolling:** Tres cohortes LTM (293,16; 219,16; 188,57 USD M) heredadas de revisión DUOL R4, sin recertificación SEC periodo por periodo. La capitalización/EBIT económico es reproducible pero la autoridad de cada cohorte aún requiere contraste.
3. **Arrendamientos ASC 842:** SEC muestra pasivo operating lease USD 84,216M y ROU asset USD 73,359M al 2026-09-30. Atlas añade leasing una sola vez al debt bridge, pero la amortización usada de 7,279M es una **estimación**, no un desglose confirmado. Medir sensibilidad conservando el modo GAAP apropiado.
4. **SBC, NOL, activos fiscales y acciones:** SBC LTM USD 156,596M; la empresa estima 50,8M acciones plenamente diluidas y recompra títulos. Quedan por conciliar flujo de recompra, dilución futura, NOL y cash taxes sin confundir con el ingreso fiscal extraordinario FY2025.
5. **Valoración relativa conforme §5/§5A:** Generar desde la misma revisión Atlas las anclas históricas fechadas, el múltiplo justificado por fundamentales y el contraste de emisores realmente comparables, normalizando IFRS/GAAP, SBC e I+D. Cada uno de EV/EBITDA, EV/FCFF, P/E, P/FCFE y P/OCF debe tener FY+1/2/3 y valor presente, control y matriz Base 5×5 (solo si válido). Mantener N/D en caso contrario; nunca copiar precios R2/R4 en Atlas. P/S/P/BV son opcionales.
6. **Sensibilidades DCF:** Se verificaron centros WACC×g y ROIC×g; falta matriz 5×5 crecimiento explícito×margen EBIT y otras pertinentes; centros deben coincidir con nuevo DCF definitivo.
7. **Dos niveles JMR:** Nivel 1 de Atlas existe en Google Doc (18 capítulos exploratorios); debe adecuarse al contrato editorial vigente de 14 capítulos y producir un Nivel 2 reproducible con mismas cifras, formulas y matrices de la revisión promovida.
8. **Validaciones oficiales:** ejecutar `bash scripts/controles_todas.sh`, `diff_formulas_plantilla.py`, cobertura SEC, candados, QA JSON→Sheets→app y QA Vercel móvil/escritorio con siete pestañas, sin desactivar protección. Probar DUOL y regresión de otras fichas.

## 4. Decisión
No fusionar ni modificar el catálogo oficial mientras los cinco métodos y las entradas materiales permanezcan sin certificar o acotar. La autorización del usuario para publicar DUOL Atlas está registrada; **no exime** las puertas de publicación descritas en REGLAS_VIGENTES §§0A, 0B, 4A, 4B, 5A, 6 y 8A.

## 5. Evidencia SEC y financiera
- SEC carta Q3 2026, publicado 2026-11-03: https://www.sec.gov/Archives/edgar/data/1562088/000162828026069474/q3fy26duolingo9-30x26share.htm
- Normativa: https://github.com/JuanMaRobledo/Modelo-JMR/blob/main/modelo/REGLAS_VIGENTES.md
- Contrato de visualización de múltiples: https://github.com/JuanMaRobledo/Modelo-JMR/blob/main/docs/ESTRUCTURA_APP.md
- Revisión oficial previa: https://github.com/JuanMaRobledo/Modelo-JMR-datos/blob/main/valoraciones/DUOL-20261103-A12-R2.json

**Alcance de este PR:** solo archivos candidatos; NO publica la ficha y NO afirma QA oficial ejecutada.
