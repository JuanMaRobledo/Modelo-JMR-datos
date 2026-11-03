# AAPL-20261103-A12-R1 · FASE 4 · CERRADA CON PUBLICACIÓN BLOQUEADA

- **Fecha**: 2026-11-03 · **Método** JMR A-1.2 FCFF · **Estado** `CANDIDATO_REVISADO`, **NO FUSIONADO**, **NO PUBLICADO**.
- **AISLAMIENTO=OK**: hoja https://docs.google.com/spreadsheets/d/1dEycisHE5Ai34Z50ELOByAiZxub87dPG2TwOmYjS2tA/edit en `AAA Finanzas/Análisis/AAPL`, mismo `revision_id=AAPL-20261103-A12-R1`.
- ChatGPT GPT-6, conectores Google Sheets/GitHub, SEC; esfuerzo no disponible. **PASOS 6/6 examinados: 3 parciales, 3 no cerrados**; la entrega no equivale a F5 ni dictamen independiente.

## Expediente editorial
`ANALISIS_BORRADOR_NIVEL_1_Y_2.md` contiene Nivel 1 en 14 capítulos y Nivel 2 en 12 secciones cuantitativas, aquí actualizado con los resultados nativos. Resultado principal DCF Base US$150,042339 por acción; MOS35% US$97,527521; Conservador108,788831, Optimista184,757116, Disrupción73,755343; media tres historias148,589288. Múltiplos secundarios promedio185,161646, ponderado hoy171,113923, precio objetivo FY+3 236,905390 (NO valor hoy). Precio Nov2 338,32 anterior al informe SEC Nov3; corte contable FY2026 terminado 26-sep. Ver fuentes en F2/F3.

## Evidencia realmente comprobada
1. `Escenarios e historias`: 4/4 `LISTO`, probabilidad total1 y disrupción separada.
2. `Sensibilidad DCF`: 3 matrices5×5, centros `OK` vs US$150,042339.
3. `Sensibilidad por múltiplo`: cinco matrices5×5, centros `OK` vs salida FY+3 de cada método.
4. WACC Detailed calculado E63=12,483033%, `Cost of capital worksheet!B84=VALIDADO`, deuda mercado positiva, DCF suma PV explícito+terminal, puente equity; balance FY2026 activo=pasivo+patrimonio.
5. Precios bursátiles por fecha fiscal FY2017–26, splits, balances y leasing histórico FY2021–24 reclasificados sin doble recuento. No se alteró plantilla maestra.
6. GitHub check `verificar` inicialmente éxito en PR #241 **solo de documentación candidata**, NO prueba técnica de valoración/18 candados/app.

## Gate de publicación que impide EN_REVISION
- No ejecución del gate oficial `scripts/controles_todas.sh`, 18 candados ni tests de integridad SEC/cero/plantilla y regresión de 138 referencias reancladas FY2026.
- No cierre de dilución RSU142,405M, coste SBC futuro, evidencia de gasto interés bruto FY26 (proxy2937M), concentración terminal54,89%, normalización de OCF prospectivo ≠ SEC CFO, supuestos múltiples EV/FCFF y P/FCFE sin serie histórica económica.
- No generación ni prueba del JSON nativo de valoraciones/análisis contra mismo `sheet_id` + `revision_id`; no CI de contrato de datos ni prueba de app/Vercel autenticada. La app no se ha cambiado.
- La auditoría económica independiente F5 exige sesión/agente distinto y posterior revisión visual del usuario.

**DECISIÓN F4**: NO fusionar PR #241 ni editar `catalogo.json`/rutas activas `valoraciones` y `analisis`, ni desplegar producción mientras falten gates. La autorización del usuario para publicar no autoriza falsear controles. Mantener el expediente candidato preparado y sus números coherentes para cierre técnico ulterior.
