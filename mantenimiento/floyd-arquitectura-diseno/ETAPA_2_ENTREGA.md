# Etapa 2 · Decisión de arquitectura con pruebas — ENTREGA

> **REVISADA (2026‑11‑11, por instrucción del usuario):** el veredicto «B y C bloqueadas» se refinó: la fusión es viable cambiando solo el nombre de hoja referenciado en dos motores, con equivalencia verificada celda a celda. Ver `etapa2b/LIBRO_UNICO.md`. Lo que sigue es el análisis original.

**Estado: PARCIAL** (una prueba decisiva ejecutada; varios criterios son estimaciones declaradas) · 2026-11-11
Sin migración. Plantillas oficiales y libros de UBER **no modificados**. Pruebas solo en copias aisladas en `Drive/Modelo JMR/02 Pruebas y desarrollo` (`1OrleslgyCSLlQdzX0KshFnsiKC9kwC6x`).

## Prueba empírica: ¿pueden coexistir tres DCF en un libro?
**Procedimiento (ejecutado):** copia aislada del D‑B de UBER (`1dv4_HVnvhTigGcrDJWfxooOEzW-J0xcNz4z-OW-nGNc`); se duplicaron con `duplicateSheet` las hojas `Input sheet` → «Input sheet (C)» y `Valuation output` → «Valuation output (C)», que es el mecanismo que usaría una fusión de motores; se leyeron las fórmulas del duplicado.

**Resultado:**
- `Valuation output (C)!B5` = `=IF('Input sheet'!B17="Yes";…'Operating lease converter'!F32+'R& D converter'!D39…)` → **sigue apuntando a `'Input sheet'`, `'Operating lease converter'` y `'R& D converter'` originales**, no a «Input sheet (C)».
- `Valuation output (C)!B33` = `=B31/B32` → **98,74 (valor de la Base)**, aunque se hubiese llenado «Input sheet (C)» con la Conservadora.
- Conclusión: duplicar el motor dentro del mismo libro **liga silenciosamente la copia a la hoja de insumos de la Base**. Para que una 2.ª/3.ª historia calcule con sus propios insumos habría que reescribir las referencias (≈1 297 fórmulas × 2 y 76 comentarios, nombres de hojas, validaciones). Eso **cambia el motor Damodaran** → prohibido por contrato. Alternativa «un solo motor con selector de historia» no es 100 % viva (las tres historias dejarían de calcularse a la vez) y obligaría a congelar resultados.
- Intento complementario: `copy_sheet_to_another_spreadsheet` (D‑C → D‑B) falló dos veces con «Internal error»: **no concluyente**, no se usa como evidencia.

**Veredicto: B y C quedan BLOQUEADAS** por fusión de motores (ambas exigen tres DCF en un libro). No se cambia el contrato.

## Matriz (1 = peor, 5 = mejor). **Ev** = demostrado, **Est** = estimado/argumentado
| Criterio | A · 6 artefactos (vigente) | B · 3 artefactos | C · 2 artefactos |
|---|---|---|---|
| Preservación integral de Simple Ginzu | **5 Ev** (17 hojas intactas ×3) | 1 Ev (bloqueo) | 1 Ev (bloqueo) |
| Corrección / reproducibilidad | 4 Est (cifras conciliadas con JSON; ver defectos de sync) | 1 Ev (Conservadora/Optimista mal ligadas) | 1 Ev |
| Complejidad de vínculos | 2 Est (8 traspasos entre libros: H→D×3, H→M, D‑B→M, D‑C/D‑O/M→Resumen) | 4 Est (≈2) | 5 Est (0) |
| Recálculo | 3 Est (por libro; cadena de 3 niveles) | 3 | 4 |
| Detección de snapshots obsoletos | 2 Ev (SHA de valores, no del libro; hallazgo E1‑2) | 3 | 5 |
| Desempeño Google Sheets | 4 Est (≈190 KB por libro; no medido) | 3 Est | 2 Est (~51+ hojas de 26 000 celdas c/u; no medido) |
| Auditabilidad | 4 Est (un libro = una historia; huellas por libro) | 2 | 2 |
| Claridad UX | 3 Est (seis URL) | 3 | 4 |
| Mantenimiento | 3 Est | 2 | 2 |
| Operación ChatGPT/Claude | 3 Est (flujo R1–R6 existente) | 2 | 2 |
| Costo de migración / app | **5 Ev** (0: la app ya lee `jmr-reboot-3libros-v1`) | 1 | 1 |
| **Total (11 criterios, sin ponderar)** | **38** | 25 | 29 |
Los totales de B y C son **teóricos**: ambas están descalificadas por el criterio 1.

## Variante no bloqueada (candidata, NO probada)
**A2 = A con H + M en un solo libro** (3 DCF intactos separados + A): elimina el traspaso H→M (8 → 7 vínculos) sin tocar el motor Damodaran. Riesgos: nombres duplicados (`Income Statement`, `Balance Sheet`, `Cash Flow Statement`, `Trailing Valuation`, `Dividendos` existen en H y M con distinto diseño; M usa una fila «Other Operating Expenses» que solo existe en H), migración de la app (`historicos`/`multiplos` apuntarían al mismo libro) y 4 plantillas. Ganancia marginal frente al costo → **no recomendada ahora**.

## Recomendación
**Mantener la arquitectura A (seis artefactos).** Gana por ser la más simple de las técnicamente demostradas. La mejora real no está en reducir archivos sino en: (1) un componente de sincronización reproducible con huella del **contenido del libro** y estado fresco/obsoleto (Etapa 4); (2) `Presentación` completa y consistente (Etapa 3); (3) corregir los hallazgos E1‑3/4/5. Sin migración de plantilla oficial.

## Evidencia y limpieza
Copias de prueba en `02 Pruebas y desarrollo`: `PRUEBA E2 · …DCF BASE (copia aislada)` (con las 2 hojas duplicadas, que **no** deben usarse) y `PRUEBA E2 · …DCF CONSERVADORA (copia aislada)`. No se eliminan (regla «no borrar»); se archivan al cierre.

## Siguiente paso
Etapa 3: prototipo de `Presentación` (copia aislada de D‑B) con identidad JMR y revisión del código real de `expediente.html`/`visor.html`.
