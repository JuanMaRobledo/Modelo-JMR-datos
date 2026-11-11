# Plantilla «libro único» (candidata) · Input sheet alimentado 100 % desde H

**Estado: PLANTILLA CANDIDATA VALIDADA en copia aislada. No publicada en la carpeta oficial; plantillas 01, 02b y 03 sin archivar.** 2026‑11‑11.
Archivo: `PLANTILLA CANDIDATA · JMR Floyd · LIBRO ÚNICO (H + 3 motores + M + Presentación)` — `1T1Cs2HGlVSe5_5OwqGGQvsN1k1KJaweXZEUM3HGttKk` (Drive `02 Pruebas y desarrollo`). Se construye con `python3 -m scripts.floyd_libro_unico.construir_plantilla DESTINO PROTOTIPO` (partiendo de una copia de 02b; usa 01, 02 y 03).

## Pedido: «los datos del Input sheet deben tomarse de las hojas de históricos»
Ahora **todas las cifras de la empresa** del `Input sheet` de los tres motores son fórmulas hacia H:
| Celda | Fuente en H | Nota |
|---|---|---|
| B3 fecha · B4 nombre · **columna C (periodo anterior) · D11** | `Guía y empresa`, estados y auxiliares | lógica propia de la plantilla 02b; **IMPORTRANGE → INDIRECT** (misma fórmula, `P3` = «libro único») |
| B11 ingresos · B12 EBIT · B13 intereses | `Income Statement` L3 · L12 · L15 | |
| B14 patrimonio | `Balance Sheet` L35 | incluye minoritarios |
| B15 deuda | `Balance Sheet` L20 + L25 | arrendamientos fuera (política «otros pasivos») |
| B16 ¿I+D a capitalizar? | `Income Statement` L10 > 0 → Yes/No | **por fórmula** |
| B18 caja | `Balance Sheet` L3 + L4 | |
| B19 activos no operativos | `Entradas históricas auxiliares` **L36** (nueva) | también alimenta M (`Supuestos y control!B61`) |
| B20 minoritarios | aux L4 + **L34** (redimibles, nueva) | también alimenta M (`M · Balance Sheet!L63`); desaparece el override manual `Puente EEFF!D21` |
| B21 acciones | `Income Statement` L27 (portada) + aux **L35** (RSU/PSU esperadas, nueva) | |
| B22 precio | `Trailing Valuation` L3 | |
| B23 tasa efectiva | `ROUND(Income Statement!L29; 4)` | |
| B37 ¿opciones? · B38 número · B39 ejercicio · B40 vencimiento | aux **L37–L39** (nuevas) | |
| `R& D converter` F7, B11:B13 | `Income Statement` L10, K10, J10, I10 | **condicional viva**: `=IF(Input sheet!B16="Yes"; H; dato de ejemplo original)` |
**Sigue siendo entrada de la IA (no es dato de H):** B17 (política de arrendamientos), B24 tasa marginal, B26–B32 (drivers de cada historia), B34 tasa libre, B41 volatilidad, selectores de overrides, hoja `Cost of capital worksheet`.
**Bloque nuevo en H** (`Entradas históricas auxiliares` filas 33–40, columna L): minoritarios redimibles, acciones por RSU/PSU, activos no operativos, opciones (número, ejercicio, vencimiento). Cada cifra requiere fuente en `Fuentes y clasificación`. Se migraron sin cambiar valores: UBER 388 / 65,539 / 11 473 / 5,549 a 52,23 (4,27 años); CMG 0 / 5,174 / 100,365 / 12,268 a 39,51 (4,2 años). *Pendiente: registrar la fuente primaria de cada una (hoy provienen de la carga previa de D).*

## Defectos de las plantillas oficiales descubiertos al construir y validar
1. **Cálculo iterativo desactivado en 02/02b** (todos los libros de valoración reales lo tienen activado a mano: 100 iteraciones, 1e‑6). Sin él el motor da «Circular dependency». Corregido en la plantilla única.
2. **Plantilla M 03: la compuerta `Supuestos y control!B60` nunca se abre.** `B18` devuelve «LISTO · CONECTADO» y `B60` exige «MODELADO · SIN CERTIFICAR» (texto de una versión anterior). En UBER la IA había restaurado a mano la fórmula vieja de `B18`. Corregida `B60` en la plantilla única.
3. **02b usa IMPORTRANGE** en el `Input sheet` (13 fórmulas × motor, URL en `P3`), contra el contrato («sin IMPORTRANGE»). Sustituido por INDIRECT.
4. **Deriva de versión:** los libros de UBER/CMG se construyeron con versiones anteriores de 01/02b/03 (p. ej. la hoja auxiliar de H pasó de «saldos iniciales» a «control de conciliación R2 y puente EV»; `Resumen` cambió la fórmula del combinado). Las plantillas actuales son coherentes entre sí; las revisiones publicadas no. Cualquier migración debe tratarlo como cambio de versión de plantilla.
5. El motor tiene **bucles circulares propios** (incl. `Option value`): con el cálculo iterativo, un `#DIV/0!` transitorio durante un llenado por partes queda «pegado». Se resuelve moviendo y restaurando una entrada del bucle (p. ej. el número de opciones); `plantilla.reiniciar_bucles` lo automatiza para `B28`.

## Validación (copia E8 llenada solo con las entradas de UBER; 83 hojas, 47 156 celdas)
| Resultado | Plantilla + entradas de UBER | Prototipo de UBER |
|---|---|---|
| DCF Base / Conservadora / Optimista | **98,7383 / 45,2912 / 149,6689** | idéntico |
| 5 múltiplos × 3 escenarios y combinado (40,2426 / 70,3069 / 104,8971) | idénticos | idénticos |
| Celdas distintas | **223 de 47 156 (0,5 %)** | |
Clasificación de las 223: (a) diseño esperado (marcador de enlace `P3:P5`, etiquetas nuevas «LISTO · CONECTADO», «CONECTADO · 24/24», bloque de conciliación del `Resumen`, textos de cabecera); (b) celdas auxiliares sin efecto en la valoración (`Trailing 12 month` del motor, `Input sheet!B46` bajo selector «No»); (c) **`Entradas históricas auxiliares` (172) y ratios de `Eficiencia de capital`/`Trailing Valuation`:** la plantilla actual rediseñó esa hoja y mi script de llenado copió los rótulos antiguos de UBER sobre ella; no es un defecto del libro único.
Plantilla en blanco: 0 fórmulas con IMPORTRANGE, `Presentación` sin errores («N/D»), motores con `#DIV/0!` hasta cargar H (normal).

## Límites
- La IA debe **sobrescribir** las fórmulas por defecto del `Input sheet` (p. ej. `B27 =I26`, `B29 =B27`) con sus supuestos; el llenado de prueba lo hace así.
- `INDIRECT` (columna C, B3/B4) es volátil; efecto de rendimiento no medido con carga real.
- La construcción completa tarda ~15 min por la cuota de la API (60 lecturas/min).
- Las sensibilidades 5×5 y el DCF inverso siguen siendo corridas manuales del motor (la hoja marca «OBSOLETA» si algo cambia).
- Sin QA visual de la app ni migración de revisiones.
