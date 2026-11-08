# F4 · UBER · Modelo JMR Floyd · 3T-2026 — entrega: BLOQUEADA (sin publicar)

**Fecha:** 2026-11-08 · **Estado:** CANDIDATO con artículo; no se publicó en la app ni se sincronizó hoja → JSON → app.
**Libro:** `1jMzDqRnTiBdbeFJmB0UH4aLdthBtC1JtiRhl8PEQBcg` · **Análisis:** `ANALISIS_CANDIDATO.md` (esta carpeta).
**Herramienta/modelo:** Claude Code, Sonnet 5.5 (construcción previa con Opus 5.5 en la misma sesión).

## Verificado (APROBADO)
- Recálculo independiente de los tres bloques: Base 101,1514, Conservadora 49,5967, Optimista 146,0449 (diferencia 0,0).
- Huella de fórmulas de Damodaran: 0 diferencias sobre 1.883. El libro difiere de la plantilla Floyd solo en `Input sheet!D12`; notas y selectores idénticos.
- Historias → números: COMPLETA en las tres (TAM N/D con motivo). Marco de tres escenarios y compuertas: APTO CON AVISOS JUSTIFICADOS.
- LTM del 3T-2026 conciliado con 10-Q y XBRL.

## Por qué no se publicó (gates NO EJECUTADOS o no aplicables)
1. **Los controles de publicación asumen cuatro historias.** `probabilidades.py` (prior B/C/O/D), `consistencia_migracion.py` (hoja = app = motor), `integridad_hojas.py`, `historias_control.py` y las pruebas de la app (`tests/*.test.*`, fixtures) leen el bloque de Disrupción. Floyd tiene tres: ejecutarlos daría falsos fallos o falsos aprobados. `scripts/controles_todas.sh`: NO EJECUTADO.
2. **El registro y la app no conocen Floyd.** `catalogo.json` no tiene entrada de UBER-Floyd; `reference/plantillas.json` mantiene la A-1.2 como vigente; REGLAS_VIGENTES v34 y los prompts F1-F5 describen cuatro historias.
3. **F2 y F3 no se ejecutaron** (diez años de historia; revisión de supuestos). Los capítulos 3, 5 (b y c), 6 y 8 del artículo están PENDIENTES.
4. **Múltiplos sin cargar** (peso 0 %) y DCF por FCFE sin revisar.
5. **Auditoría F5 no independiente.**
6. Publicar exigiría fusionar a main; la restricción «no fusionar PR» sigue vigente sin autorización expresa.

## Qué desbloquea la publicación
Adaptar a tres historias `probabilidades.py`, `consistencia_migracion.py`, `integridad_hojas.py`, `historias_control.py`, el esquema JSON y la app, actualizar REGLAS y los prompts, registrar Floyd como vigente y ejecutar F2-F3; después `controles_todas.sh` y CI sin fallas.

## Drivers Base (anterior → nuevo)
A-1.2 vigente (Base 91,14): crecimiento 1-5, margen y S/C de la hoja `1i0B9cPX…` → Floyd: CAGR 1-5 13,4 %, margen 18 %, S/C 2,8/2,5, ROIC terminal 14 %, g 4 %, WACC 9,37 % → 8,33 %.
