# Prompt para ChatGPT/Work · Corrección de MELI-FLOYD-3T26-R1 (F3 y F4)

Copia y pega todo lo que sigue.

---

Ejecuta la corrección de la valoración y el análisis Floyd de **MELI** con el contrato de `Modelo-JMR/docs/CONTRATO_EJECUCION_FLOYD.md`. Retoma la revisión **MELI-FLOYD-3T26-R1** (PR #260 de `Modelo-JMR-datos`, rama `meli-floyd-3t26-r1`). No crees libros ni revisiones nuevas. Antes de editar, lee en este orden:

1. `modelo/REGLAS_VIGENTES.md` (§0, §1, §4, §4A, §4B, §4C, §11).
2. `docs/CONTRATO_EJECUCION_FLOYD.md` y `docs/prompts/ordenes-floyd.md` (F3 y F4).
3. `docs/HISTORIAS_A_NUMEROS.md`.
4. Las entregas F1–F4 de `candidatos/valoraciones/MELI-FLOYD-3T26-R1/` y la revisión crítica `REVISION_CLAUDE_20261108.md`, que está en la rama `ccr-d8664753-j2j79d` de `Modelo-JMR-datos`.

Libros: H1 `1TF8KaMkn-Wc3csoCK1z9-IierhPhOBZwwdX7fiBYN6Q`, H2 `1wkFwjzufTR8KqrLSc7gxmxuB_qepFjEDc-LMuFi5oR0`, documento de análisis `1bv2hPD1XvgVM2Vz3WjQdX8Sh1bLo0FXEhqPc3GZCxVk`. Corte contable 30-sep-2026, precio US$1.510 al 6-nov-2026.

## Regla central
Los valores salen de las fórmulas de H2. Los scripts de Python `diagnostico_flujo_accionista.py` y `revision_supuestos.py` quedan solo como réplica de control y no como fuente de ninguna cifra publicada. No sustituyas fórmulas ni selectores por números.

## Correcciones, en este orden

**1. Método (cierra primero).**
- Decide y documenta el método según §4C: SOTP con Commerce y corporativo en el motor FCFF Floyd, y el crédito/Fintech en FCFE/ROE.
- Resuelve el puente de fondeo, caja restringida, fondos de clientes y capital distribuible de Mercado Pago, con la tabla de saldos iniciales que pedía tu propia F3.
- No sumes dos veces deuda colateralizada ni arrendamientos ASC842.
- Si el perímetro sigue sin poder acotarse, deja el resultado como N/D en lugar de un valor central.

**2. Costo de capital.**
- Calcula Ke y WACC en `Cost of capital worksheet` (modo Detailed) con tasa libre y prima madura de la misma fecha.
- Registra fuente, fecha y beta de cada componente. La Ke de 12,5 % actual no tiene respaldo documentado.
- Aplica §4: g terminal de 4,0 % (con techo en la tasa libre) y costo de capital terminal con beta 1. Si te apartas, documenta por qué (las financieras FCFE pueden tener un g propio justificado) y cuantifica el impacto frente a §4B.
- Mi sensibilidad, que debes reconciliar y no copiar: con Ke terminal de 9,7 % el central de tu modelo pasa de US$1.022 a unos US$1.280–1.320.

**3. Retención e inversión.**
- Sustituye la retención interpolada por una evolución explícita de cartera, fondeo y patrimonio (o por Sales-to-Capital y ROIC en la parte FCFF).
- Reconcilia el ROE implícito con el ROE actual de unos 24 %. La retención actual de 45 % en el año 1 implica un ROE incremental de unos 60 %.

**4. Tres historias (`Escenarios e historias`).**
- Escribe Conservadora, Base y Optimista con mecanismo, evidencia, contraevidencia, rango y celda por palanca (`HISTORIAS_A_NUMEROS`).
- Asigna probabilidades que sumen 100 %. El fracaso va solo en la Conservadora.
- Verifica que Conservadora ≤ Base ≤ Optimista.
- Calcula el valor esperado. El MOS del 35 % va solo sobre el DCF Base.

**5. Cierre del cálculo.**
- Ejecuta el DCF, el DCF inverso, los cinco múltiplos aplicables y las matrices 5×5.
- Concilia cada centro con su referencia.
- Reporta la huella de fórmulas observada.
- Concilia el resultado con la revisión A-1.2 `MELI-20261028-A3` (Base US$2.030, margen objetivo 15 %, g 4 %, WACC 10,8→10,2 %), con un cuadro antes → después de las palancas que explican la diferencia.

**6. Análisis (F4).** Rehaz Nivel 1 (14 capítulos) y Nivel 2 (12 apartados) con **una sola cifra central**. Elimina la corrida anterior de US$1.310,55, el «umbral del 65 %» (US$851,86) y el inverso con otra definición, salvo en una sección de conciliación. Usa una única definición de inverso.

## Reglas de ejecución
- Declara modelo, herramienta y esfuerzo reales.
- Marca cada control como `APROBADO`, `PARCIAL` o `NO_EJECUTADO`, con evidencia (celda, fuente, comando).
- No declares aislamiento, huella ni gates que no hayas ejecutado.
- Actualiza `FASE_3_ENTREGA.md` y `FASE_4_ENTREGA.md`.
- La revisión permanece como CANDIDATO. Solo se publica como `EN_REVISION` si pasan los controles técnicos de F4 y `validar_catalogo.cjs`.
- F5 queda para una sesión independiente. No te autocertifiques.
- Trabaja en una rama y un PR, sin sobrescribir el trabajo del PR #260 sin actualizarte primero.
- Al final entrega el primer siguiente paso exacto.
