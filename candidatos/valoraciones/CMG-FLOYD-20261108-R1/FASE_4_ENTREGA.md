# F4 · CMG · Modelo JMR Floyd · CMG-FLOYD-20261108-R1 — entrega: CERRADA CON CONTROLES PENDIENTES (ver «Estado de CI y despliegue»)

**Fecha:** 2026-11-08 · **Estado propuesto:** EN_REVISION (solo si CI y revisión técnica pasan; auditoría económica F5 **NO REALIZADA**) · **Herramienta/modelo:** Claude Code, `claude-sonnet-5-5` (esfuerzo no reportado) · **AISLAMIENTO=OK**
**Valoración:** https://docs.google.com/spreadsheets/d/1f7BMt0ynbvjFUT84ftUmkPfxyJvmPvcqQ-7GW7EWtAY/edit · **Históricos:** https://docs.google.com/spreadsheets/d/14ONchw6fXR9tSQs_OlQ3_Nio6d1vobUcH9LLgyZ6REs/edit · **Análisis (Nivel 1 + Nivel 2):** https://docs.google.com/document/d/1pXWB3fkJpblgUpe6tljf2m6XXVYzCyFkGNJKUI-f-VA/edit
**Archivos:** `valoraciones/CMG-FLOYD-20261108-R1.json`, `analisis/CMG-research-CMG-FLOYD-20261108-R1.json` (copias idénticas en esta carpeta: `valoracion.json`, `analisis.json`), `NIVEL_1_14_CAPITULOS.md`, `NIVEL_2_12_APARTADOS.md`. Scripts reproducibles: `JMR-valuation/reference/modelo_floyd_2026-11-08/cmg/`. **PASOS: 8/8 ejecutados.**

## Controles ejecutados (APROBADO con evidencia)
1. **Integridad de fórmulas:** 0 diferencias en 26.346 fórmulas frente a la Maestra Floyd (valoración e históricos). `Huella motor` 0/0.
2. **Conciliaciones:** Históricos (balance, EBIT, Δ caja, LTM = FY + acumulado − comparable) y traspaso H2 (484 celdas; 14 diferencias = fórmulas dependientes de FY-3). ROE y ROIC reproducidos en dos períodos.
3. **M1, M2 y M3 (`JMR-valuation/scripts/consistencia_migracion.py`, perfil Floyd):** `{'M1': True, 'M2': True, 'M3': True}` sobre estos dos JSON. M1: tres centros DCF y cinco de múltiplos contra VP FY+3; M2: probabilidades 50/25/25, valor esperado, DCF Base = valor principal, MOS35 = Base × 0,65, sin Disrupción; M3: mismo `revisionId` y `sheet_id` en valoración y análisis, 14 capítulos, Nivel 2, sin la palabra «pendiente» como marcador.
4. **Probabilidades, DCF Base, MOS, DCF inverso y ocho matrices 5×5:** conciliados (ver F3). Réplica independiente del DCF: diferencia < 1e-5.
5. **Datos:** `node scripts/validar_catalogo.cjs`, `validar_no_regresion_20.cjs`, `auditar_integridad.cjs`, `auditar_profundidad.cjs` (CMG: 14 secciones), `auditar_ponderaciones.cjs`, `inventariar_cobertura_a.cjs`, `validar_profundidad_metodo_a.cjs`, `verificar_cierre_multiplos.py`, `registro_revisiones.py --check`, las 113 pruebas `node --test scripts/tests/*.test.cjs` y las pruebas Python del CI: todo en verde en local.
6. **App (Modelo-JMR):** sin cambios de código; 195/195 pruebas locales (`npm test`). Lógica JS de la ficha: `fromCatalog` marca CMG visible con método Floyd; `normalizeDcfMatrices` acepta las tres matrices con centro conciliado (`viewer_check.mjs`).
7. **Catálogo:** solo se sustituyó la referencia activa de CMG (valoración, análisis y `controlModeloA.empresas.CMG`). Los archivos A-1.2 (`valoraciones/CMG-20261028-A3.json`, `analisis/CMG-research-CMG-20261028-A3.json`, `auditorias/narrativas/CMG.md`) quedan intactos como histórico.
8. **Validadores generalizados sin relajar mínimos:** `validar_no_regresion_20.cjs`, `capturas_matrices_fuente.test.cjs` y `test_estandarizacion_20261031.py` aceptaban solo UBER como Floyd; ahora aceptan un conjunto cerrado {UBER, CMG} con las mismas aserciones por entrada, más protección de la huella A-1.2 sustituida (valor y `sheet_id` de CMG-A3).

## Estado de CI y despliegue
Se completa al final de la sesión (ver informe final): PR de las tres ramas, resultados de CI y diferencia entre PR fusionado y despliegue efectivo.

## Salvedades
Ver `valoracion.json` (7 salvedades) y el capítulo 14 del análisis: TAM N/D, beta y volatilidad de opciones como hipótesis, convención de arrendamientos (CMG-A3 restó el pasivo de arrendamientos con el EBIT neto de alquiler; Floyd no) y ROIC terminal sobre capital sin arrendamientos, CFO LTM con +222 M de impuestos diferidos, FY2016 parcial, scripts oficiales de auditoría de estados no ejecutados. QA visual en navegador: SIN REALIZAR en esta sesión salvo que el informe final indique lo contrario.

## F5
**NO REALIZADA.** Requiere sesión independiente: preguntas del usuario en `auditorias/solicitudes/CMG/CMG-FLOYD-20261108-R1.json` si existen y mínimos económicos (crecimiento, margen, ROIC, reinversión, WACC, terminal, arrendamientos, múltiplos).
