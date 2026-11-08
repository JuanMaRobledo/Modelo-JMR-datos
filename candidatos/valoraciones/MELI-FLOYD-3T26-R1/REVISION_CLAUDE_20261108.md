# Revisión crítica de MELI-FLOYD-3T26-R1 (PR #260) · 8-nov-2026

**Revisor:** Claude (Claude Code, sesión cloud; esfuerzo no expuesto). **Alcance:** F1–F4 de ChatGPT (PR #260, rama `meli-floyd-3t26-r1`, commit `451d84b`), `ANALISIS_N1_N2.md` y los scripts `diagnostico_flujo_accionista.py` y `revision_supuestos.py`, reproducidos.
**No es F5.** Es una revisión solicitada por el usuario, no un dictamen independiente. **NO EJECUTADO:** apertura de H1/H2 en Google Sheets, cotejo de cifras con la SEC, cotización. No se modificó ningún valor ni archivo del PR #260.

## Resultado reproducido
Central US$1.021,81 · Conservador 495,03 · Optimista 1.811,69 · terminal 56 % del valor. Coincide con lo declarado.

## Hallazgos
| # | Hallazgo | Severidad | Evidencia |
|---|---|---|---|
| 1 | Los valores (US$1.310,55 y US$1.021,81) salen de scripts de Python, no del motor de la hoja. | Estructural | F2: «No se activó el motor»; REGLAS §11 |
| 2 | Método sin cerrar: F1 pidió evaluar SOTP (FCFF Commerce + FCFE crédito, §4C) y no se hizo; hay un modelo consolidado utilidad × (1 − retención) a una sola Ke. Puente de fondeo/caja restringida/capital sin resolver. | Estructural | F1, F3 |
| 3 | Terminal fuera de §4 sin justificar: Ke 12,5 % perpetua y g 3,5 % (§4: g 4,0 %, terminal con beta 1). Ke no sale de `Cost of capital worksheet`; sin Rf/ERP/beta/fecha. | Material (+25 a +29 % con Ke terminal 9,7 %) | script `sensibilidades_revision_claude.py` |
| 4 | Retención interpolada por crecimiento, sin evolución de patrimonio: ROE incremental implícito 60 % → 15 % frente a ROE actual ≈ 24 %. | Supuesto sin sustento; sensibilidad ±2 % (35–55 %) | mismo script |
| 5 | Tres historias sin mecanismo/evidencia/contraevidencia, sin probabilidades ni valor esperado, sin fracaso modelado; faltan matrices y anclas de múltiplos. | Incumple F3 | `HISTORIAS_A_NUMEROS`, órdenes F3 |
| 6 | Expediente incoherente: dos centrales (1.310,55 y 1.021,81), inverso con definiciones distintas (neto 10,48 % / EBIT 17,15 %), capítulos con la corrida anterior, «umbral 65 %» sin respaldo en reglas. | Incumple F4 | `ANALISIS_N1_N2.md` |
| 7 | Descuento de fin de año sin ajuste por fecha de valoración (con medio año ≈ US$1.084). | Menor/convención | script |

Contexto: la revisión A-1.2 `MELI-20261028-A3` (`INCOMPLETA_EN_REVISION`) da Base US$2.030 con margen objetivo 15 %, g 4 %, WACC 10,8→10,2 %. La diferencia con US$1.022 no está conciliada y se explica sobre todo por tasa y margen terminal.
Las Rf 5,29 % y ERP 4,41 % (Damodaran 1-nov-2026) provienen de otras revisiones del repo (DUOL) y no se verificaron para este corte.

## Qué hacer (primer paso exacto)
1. Decidir el método: SOTP con Commerce en el motor Floyd (FCFF) y crédito en FCFE con evolución explícita de cartera, fondeo y patrimonio.
2. Calcular Ke/WACC en `Cost of capital worksheet` (Detailed), con Rf y ERP de una misma fecha; terminal según §4 o con justificación documentada.
3. Cargar H2, escribir las tres historias con probabilidades y calcular en la hoja; el Python queda solo como réplica.
4. Reescribir Nivel 1 y 2 con una única cifra central; después ejecutar los gates y dejar F5 a otra sesión.
