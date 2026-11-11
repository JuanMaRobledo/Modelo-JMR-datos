# Libro único: H + tres motores + M + Presentación en UN libro, con fórmulas entre hojas

**Estado: PROTOTIPO VERIFICADO en copias aisladas de UBER y CMG. No adoptado; producción sin tocar.** 2026‑11‑11. Reemplaza, para las revisiones nuevas, el esquema de varios libros con sincronización por scripts (`floyd_sync`), a petición del usuario («innecesariamente complicado»).

## Qué cambia respecto del veredicto de la Etapa 2
La Etapa 2 declaró bloqueadas las opciones B y C porque, al duplicar el motor dentro de un libro, la copia sigue apuntando a las hojas del original. Se midió ahora qué hace falta para evitarlo y resulta **un cambio de nombre de hoja, no de lógica**: el motor tiene 1 225 fórmulas con referencias a 13 hojas por nombre, **0 rangos con nombre, 0 `INDIRECT`, 0 referencias externas, 0 gráficos** y 1 formato condicional.
Para la arquitectura nueva se asume ese cambio de nombre en dos de los tres motores. **Es un cambio de contrato** («no cambiar nombres de pestañas»): el usuario lo pidió expresamente; se mantiene la prueba de equivalencia y el motor Base conserva sus nombres originales.

## Diseño (83 pestañas, ≈ 1,9 M celdas de cuadrícula = 19 % del límite de Google Sheets)
| Grupo | Pestañas | Color | Nombres |
|---|---|---|---|
| Cabecera | Presentación · Guía del libro · Resumen de valoraciones · Sensibilidades DCF | tinta | — |
| Históricos (H) | 12 | azul | originales |
| Motor Base | 17 (fcffsimpleginzu) | verde | **originales, sin cambios** |
| Motor Conservadora | 17 | naranja | `… · C` |
| Motor Optimista | 17 | morado | `… · O` |
| Múltiplos (M) | 16 | dorado | originales; `M · Income Statement/Balance Sheet/Cash Flow Statement/Trailing Valuation/Dividendos` (chocan con H) |
**Datos entre hojas por fórmula, sin scripts ni IMPORTRANGE:** H→3 motores (11 celdas c/u), H→estados de M (reglas por etiqueta: 73 filas en UBER; preservan blancos), motores→`Entradas desde DCF` de M (8×3), motores y M→`Resumen`. La IA solo escribe entradas: estados y auxiliares de H, supuestos en el `Input sheet` de cada motor (en UBER 6 celdas por historia difieren de la Base), multiplicadores/pesos de M y probabilidades.

## Cómo se construye (reproducible, idempotente)
`python3 -m scripts.floyd_libro_unico.construir CONFIG.json` sobre un libro que ya tiene el motor Base + Presentación + Resumen (copia de la plantilla 02b): copia las hojas de M y de H, **duplica el motor Base como C y O**, reapunta las referencias (`'Input sheet'!` → `'Input sheet · C'!`), aplica las celdas propias de cada historia (diferencias con su libro original) y cablea con fórmulas. `verificar.py` compara celda a celda con los libros originales. (Las hojas `Input sheet` y `Valuation output` no se pueden copiar entre libros con la API —error 500—: por eso los motores C/O se obtienen duplicando dentro del libro.)

## Evidencia
| Comprobación | UBER | CMG |
|---|---|---|
| Motor Base / Conservadora / Optimista vs libro original (17 hojas c/u) | 11 936 / 11 936 / 11 936 celdas, **0 diferencias** | 11 936 ×3, **0 diferencias** |
| M (16 hojas) vs original | 8 020 celdas, **0** | 7 995, **0** |
| H (12 hojas) vs original | 2 483, **0** | 2 425, **0** |
| `Resumen`/`Presentación`/`Sensibilidades` vs esquema multilibro | 3 diferencias: etiquetas de control `PENDIENTE`/`DIFERENCIA` en la copia sincronizada y `CONCILIADO`/`OK` en el libro único | igual (3) |
| Cifras | DCF 98,7383 / 45,2912 / 149,6689; múltiplos Base 70,3069; esperado 98,1091 | DCF 32,2837 / 17,6858 / 40,4675; múltiplos 35,4600 |
| **Prueba de mutación** (editar `H!Income Statement!L3` y mirar, sin ejecutar nada) | +1000 → **100,4482 / 46,0556 / 152,2798; múltiplos 71,1742** (idéntico al sincronizador); matriz pasa sola a `REVISAR`; restaurado idéntico | +500 → 33,5262 / 18,3542 / 42,0319 / 36,7748; restaurado idéntico |
La propagación es inmediata (lectura a los ~3 s, sin sincronización) y **ya no existe obsolescencia entre libros**: un cambio en H llega a motores, M, Resumen y Presentación por el propio recálculo de Sheets.

## Defectos encontrados y corregidos durante la construcción
1. Hojas copiadas conservan el texto de la fórmula pero evalúan `#REF!` hasta reescribirlas → utilidad de reenlazado (relee y reescribe cada fórmula).
2. La suma de dos celdas en blanco daba 0 → ahora queda en blanco (regla `suma`).
3. El cableado no era idempotente (trataba como fórmula una fila ya cableada) → las filas cuyas fórmulas apuntan a H cuentan como entradas.
4. **`R& D converter` se cableaba siempre**: en CMG (sin capitalización de I+D) sobrescribía los datos de ejemplo de Damodaran → ahora solo si `Input sheet!B16 = Yes`; celdas restauradas desde los originales y re‑verificado.
5. Cuota de la API (60 lecturas/min): llamadas con reintento y construcción reanudable.

## Límites, riesgos y decisiones que necesito
- **Contrato y app:** el contrato describe seis artefactos y la app lee seis URL por revisión (`libros.historicos`, `libros.dcf.{base,conservadora,optimista}`, `libros.multiplos`, `libros.analisis`). Con un libro único serían **dos artefactos** (libro + documento A) y la app tendría que leer pestañas por nombre de un solo libro: requiere un nuevo valor de `contratoLibros` (p. ej. `floyd-libro-unico-v1`) y cambios en `docs/expediente.js`/`visor.html`. No se ha hecho (Etapa 7).
- **Plantilla:** falta construir la plantilla oficial «libro único» (a partir de 01, 02b y 03) y archivar las tres separadas. El constructor lo permite; no se ha ejecutado sobre las plantillas.
- **Sensibilidades 5×5** siguen siendo valores de corridas del motor (estáticos); el libro muestra `OBSOLETA` si cambia cualquier supuesto, pero rehacerlas sigue siendo manual (cada corrida modifica entradas).
- **Tamaño:** 83 pestañas; la exportación a PDF del libro completo tiene 184 páginas (la Presentación es una). El recálculo se percibe inmediato en las pruebas; no se midió con carga real de varios usuarios.
- **Mantenimiento:** las hojas « · C» y « · O» son duplicados; si Damodaran publica una versión nueva del motor, hay que regenerarlas con el constructor (no editar a mano).
- **Sincronizador (`floyd_sync`)**: ya no es necesario en la arquitectura nueva; se conserva para revisiones heredadas de seis libros (UBER, CMG, MELI, MSFT, AAPL) hasta migrarlas.
- **Libros de producción:** no se tocaron. Prototipos: UBER `1a4GO-PubO5SXOFNOeSDfGwzzo49IVHORFW-42LGb3GE`, CMG `16nvnhl-WCimwKs0xpQ_5sOV6jBK1hdXO1d8uaT33Pr0` (carpeta `02 Pruebas y desarrollo`).
