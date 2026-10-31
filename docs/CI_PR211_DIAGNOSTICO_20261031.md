# PR #211 — diagnóstico de cierre técnico, 31-oct-2026

**Estado:** BLOQUEADO, mantener PR en borrador. Esta nota no constituye aprobación financiera ni de publicación. La app PR #151 ya fue fusionada y el usuario aprobó el diseño; el registro de datos sigue separado.

## Evidencia reproducible

- Última ejecución de datos: [Control JMR de ponderaciones #41221087332](https://github.com/JuanMaRobledo/Modelo-JMR-datos/actions/runs/41221087332): **failure**. Las otras dos verificaciones de profundidad editorial del SHA `1fccf9cedfedf9aab06c5b15b0360fd1016aaa9c` están **success**.
- En el mismo workflow, 57 de 63 pruebas Node generales pasaron, seis fallaron. La corrida informa por separado errores de auditoría de integridad, cierre histórico y catálogo. Esto es diagnóstico adicional, **no un gate relajado**.
- `scripts/validar_catalogo.cjs` y `scripts/auditar_integridad.cjs` rechazan UBER porque aún no hay matrices Base exportadas al JSON. No se deben suplantar con N/D=0 ni bajar controles. Las matrices Base 5×5 están integradas en **16/20** revisiones A del PR; UBER, GOOGL, INTU y NU siguen pendientes.
- Se reorganizó `.github/workflows/auditar-ponderaciones.yml` para ejecutar diagnósticos posteriores incluso con fallo previo (`if: !cancelled()`); el gate financiero sigue obligatorio y la conclusión global permanece **failure**.
- Se modernizaron cuatro pruebas negativas de `scripts/tests/auditar_ponderaciones.test.cjs`: usan la matriz Base de A-1.2 y el caso SOTP sintético basado en XP histórico, en lugar de contadores y pesos propios del modelo antiguo. Ninguna revisión de empresa se cambió en ese commit.

## Bloqueos detallados

1. **UBER:** el registro PR mantiene DCF 100% / múltiplos 0%; Google Sheets original presenta 60% / 40%, cinco múltiplos con override manual marcado **«Sí — revisar»**, y las estadísticas de `Múltiplos históricos` consultadas carecen de series útiles. DCF Base coincide, pero no hay anclas independientes certificadas. Guardar captura contemporánea, justificar por método y reconciliar ponderaciones antes de integrar.
2. **GOOGL:** nueva captura nativa completa y anclas no dependientes de precio; el resumen histórico de tres métodos no corresponde a la hoja observada con seis métodos calculados. No reutilizar centros de otra fecha.
3. **INTU:** siete múltiplos nativos N/D; matrices exploratorias no sustituyen fuentes. **NU:** contrato FCFE bancario Ke / P/E, P/FCFE y P/BV, independiente del DCF industrial.
4. **EPAM, NKE, NVO, ONON, PYPL, ZTS:** ponderaciones y descuentos divergentes frente a hoja, sin transferencia aprobada. MSFT ya está reconciliada. No copiar pesos automáticamente.
5. **Hashes de recaptura META y NVDA:** `scripts/tests/publicacion_recaptura.test.cjs` informa hash de los análisis vigentes distinto del manifiesto: META esperado `b9adc086...`, observado `2300d050...`; NVDA esperado `842b7b42...`, observado `9559a225...`. No concluir manipulación o regresión económica sin cotejar diff y versión del manifiesto. Prohibido reescribir hashes para aparentar validación.
6. **Pruebas históricas:** dos casos que esperan `validate()` global verde fallan por UBER; una prueba de ruta enlazada espera un texto de error previo (el rechazo sigue ocurriendo); una prueba de MOS espera otro texto. `scripts/verificar_cierre_multiplos.py` busca `cierreMultiplos` en una revisión A activa que no usa ese contrato. Debe apuntar expresamente a snapshots históricos apropiados o usar un verificador específico para A; no confundir expedientes archivados y actuales.

## Secuencia para cierre

1. Cotejar y clasificar diferencias hash META/NVDA contra manifiestos originales y cambios editoriales. Mantener rechazo si hay diferencias no reconciliadas.
2. Corregir **tests históricos y sus selecciones de revisión** sin eliminar casos negativos ni debilitar assert de integridad.
3. Reconciliar UBER con fotografía de la misma revisión y anclas independientes antes de ajustar sus matrices y pesos; repetir para GOOGL.
4. Completar contratos nativos INTU y NU, y luego las seis discrepancias de descuentos. Mantener DCF/ROIC/MOS y estados de revisión hasta nueva decisión documentada.
5. Ejecutar CI completo con sus tres workflows **success** en un mismo SHA, más cotejo cruzado de los 20 expedientes, revisión de cambios y permisos. Solo entonces evaluar fusión de #211.
6. QA funcional real en producción para los siete paneles de la app, especialmente sensibilidades, y revisión visual del usuario; auditoría económica independiente **después** de la revisión visual.

**No realizado:** cambios en Google Sheets, publicación de valores, fusión de #211, aprobación económica o cierre ficticio del gate.
