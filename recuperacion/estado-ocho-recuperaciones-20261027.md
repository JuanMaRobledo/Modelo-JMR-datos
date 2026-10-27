# Recuperación de ocho estudios (ADBE, BSX, CELH, DUOL, MSFT, NVO, ONON, PYPL) · estado al 27-oct-2026

Alcance: controles de **solo lectura** sobre las hojas Google de cada registro y sobre los JSON de `valoraciones/`, `analisis/` y `auditorias/narrativas/`. No se modificó ninguna hoja, supuesto, registro ni `catalogo.json`. **Ningún estudio se publica en esta etapa.**

## 1. Siete múltiplos (`verificar_multiplos_hoja.py`, 27-oct)
Las ocho: 7/7 con fórmula y resultado numérico (`Descuento de múltiplos!J20:J24`, `PV!E42`, `PBV!E42`). Estructural; no certifica supuestos.

## 2. Fórmulas frente a la maestra vigente (`audit_master_formulas.py`, maestra 22-oct-2026, sin `--gates`)
Pestañas de cálculo y de los siete múltiplos: **0 desviaciones** en las ocho. Solo difieren celdas de entrada del analista en `Input sheet` (B27:B33: crecimiento, margen, ventas/capital con valor fijo; ADBE y MSFT además B30 con paréntesis adicional). PYPL: 0. Son entradas autorizadas, no fórmulas dañadas; no se tocaron.

## 3. Consistencia hoja = registro = análisis (`consistencia_migracion.py --hoja`)
| Ticker | M1 | M2 | M3 | H1 | H2 | H3 |
|---|---|---|---|---|---|---|
| ADBE, BSX, CELH, NVO, PYPL | OK | OK | OK | OK | OK | OK |
| DUOL | OK | OK | OK | OK | OK | **NO** (EV/FCFF Cons 16,6x > actual 14,1x) |
| MSFT | OK | OK | OK | OK | OK | **NO** (EV/FCFF Base 30,0x > 0,78·prom 26,3x) |
| ONON | **NO** | **NO** | OK | **NO** | OK | OK |

- ONON: el registro está en esquema anterior (sin `multiplesAdicionales`/contrato ni `valorEsperado.dcfBase`). La hoja da DCF Base 34,1756 y promedio 34,4049, iguales a `valorCentral`/`valor` del registro. Requiere regenerar el registro desde la hoja, no recalcular.
- DUOL/MSFT H3: es un asunto de supuestos (múltiplo de salida). No se modifica por defecto.

## 4. Controles de publicación (`controles_todas.sh`, 27-oct): fallan las ocho
- **Candados 15/18** en las ocho: faltan `Financials Multiples!M34:M36`. `reference/candados_plantilla.json` es de la plantilla del 21-oct y condiciona fórmulas a `M34="LISTO"`; la maestra vigente del 22-oct no tiene esas celdas (L34:M36 vacías) ni esa condición en `EVFCFF!F8`. NKE pasa 18/18 porque su hoja trae el bloque «Control 7 métodos». Es una discrepancia entre control y maestra: debe resolverse por mantenimiento autorizado del control o migrando las hojas; no se rellenan celdas para aprobarlo.
- **Integridad**: hallazgos de comparación contra el «motor legado» en ADBE (4), BSX (1), DUOL (1), ONON (12) y diferencias de la pestaña H5:H8 en las ocho; sin diagnóstico concluyente todavía.
- **Supuestos**: DUOL (margen 23/28/32 % > 2,5× sector sin ventaja durable, S1) y PYPL (cinco múltiplos Optimista sin `justificacion_salto`, S4).

## 5. Otros bloqueos
- `fecha` de las valoraciones no es ISO («Análisis del 30 de sept de 2026»); `validar_catalogo.cjs` exige ISO y `a.date >= v.fecha`.
- DUOL y CELH: P/S y P/BV de la hoja son −1,2109 y −0,1777 por acción frente al registro, de forma uniforme en escenarios (ambos métodos con peso 0). Hay que recapturar esos valores con el flujo oficial y actualizar las referencias de análisis/auditoría si cambian.
- Las tres piezas de cada empresa enlazan la misma hoja y `sourcePath`, y el análisis cita el DCF Base del registro. Esto no sustituye los controles anteriores.

## Estado por empresa
| Ticker | Siete múltiplos | Estado |
|---|---|---|
| ADBE, BSX, NVO | conforme (fórmula y resultado) | No publicable aún: candados/integridad |
| CELH | conforme, con desajuste P/S-P/BV | No publicable: candados, integridad, recaptura de 2 salidas |
| DUOL | conforme, con desajuste P/S-P/BV | No publicable: además H3 y S1 |
| MSFT | conforme | No publicable: candados, integridad, H3 |
| ONON | conforme | No publicable: registro en esquema anterior |
| PYPL | conforme | No publicable: candados, integridad, S4 |

Se conservan las versiones; no se archivó ni se borró nada.
