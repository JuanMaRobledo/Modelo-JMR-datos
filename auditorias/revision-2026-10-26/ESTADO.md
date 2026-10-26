# Estado del trabajo y cómo retomarlo (26-oct-2026)

Rama de trabajo en los tres repositorios: `ccr-68242d45-bfmwvh` (nada se ha fusionado a `main`).

## Hecho
- 33 valoraciones y análisis del 20-oct restaurados (`LEEME.md` en `archivo/snapshot-2026-10-20-38-valoraciones/`), sin el bloque `posicion`.
- Prompts: 30-sep recuperados con adenda de sensibilidades solo en la Base; contrato de múltiplos, MOS y prompt de investigación alineados;
  `REGLAS_VIGENTES` **v11** (§11 hojas unificadas) y auditoría **v1.3** (porqué de cada supuesto y fuente de todos los datos).
- Auditoría de registro de las 33 (`RESUMEN.md`), contraste con la SEC (`SEC.md`), profundidad del análisis (`PROFUNDIDAD.md`).
- Scripts: `auditar_registro.py`, `contrastar_sec.py`, `auditar_profundidad.py` (este repo) y `unificacion_hojas.py` (JMR-valuation).

## Bloqueos conocidos
- La credencial de Google de este entorno **no puede leer las hojas de las 29 empresas antiguas** (archivadas el 24-oct); solo lee las
  plantillas y las hojas vigentes de NFLX, NKE, NVDA y META. Para unificarlas hay que crear una copia nueva de la maestra por empresa
  (`scripts/reset_from_master.py --new "Modelo JMR - <T>"`), llenar datos crudos (`refresh_native_model.py`, SEC) y fichas de supuestos
  (`reference/damodaran/<T>.json`), y regenerar (`bash scripts/valorar.sh <T> <ID_COPIA>`).
- Cuota de Sheets (60 lecturas por minuto): `unificacion_hojas.py` tarda unos 20 minutos por hoja la primera vez.
- Financial Datasets sin créditos; la SEC sí responde.

## Cola, en este orden
1. Terminar `unificacion_hojas.py` sobre NFLX, NVDA, NKE y META (informes en `/tmp` del entorno; repetir si se perdieron):
   `cd JMR-valuation && PYTHONPATH=.:scripts python3 scripts/unificacion_hojas.py --copy-id <ID> --salida auditorias/.../unificacion/<T>.json`.
   Hojas: NFLX `1ZPNMHxc7m3Iv60mdGspgi6-cc2zwf5kZ4ocsuANQUNM`; los otros IDs están en `hojaGoogle` de cada registro vigente.
   Hallazgo previo: NKE y META tienen 7 pestañas añadidas y NVDA 2 (formato no unificado).
2. PYPL: fijar la base de ingresos en LTM a 2T26 (hoy usa FY2025) y revisar los 8-K/6-K posteriores (`SEC.md`).
3. Corregir hallazgos de regla por empresa (`RESUMEN.md`): pesos de múltiplos con razón económica por método, probabilidades simétricas,
   g terminal 4 %, MOS 35 % (AAPL y otra con 25 %), enlace análisis→valoración.
4. Análisis incompletos (`PROFUNDIDAD.md`): CMG (faltan secciones), PYPL, ADBE, GRUPOARGOS y PFGRUPOARG son los más cortos.
5. Hoja nueva unificada por empresa, de la que más pesa en la cartera a la que menos; en cada una: datos crudos con fuente → supuestos con
   su porqué → `controles_todas.sh` (con `UNIFICACION=1`) → auditoría v1.3.
6. Contrastar a mano las que la SEC no cubre: P911, ONON, NU, PAGS, y los trimestres de AFYA y NVO.

## Resultado parcial · unificación de hojas (NFLX, 26-oct)
`unificacion/NFLX.json`: 61 de 61 pestañas, mismo orden; **122 de 122 selectores conservados**; de 21.265 fórmulas de la maestra, 336 perdidas y 233 editadas.
Todas las perdidas y 175 de las editadas están en «Sensibilidad por múltiplo» (la hoja tiene 9 columnas frente a 17: es el cambio deliberado a matrices solo
Base). Las otras 58 ediciones están en `Financials Multiples` (12) y en las pestañas de método `POCF`, `PE`, `PFCFE`, `PV`, `PBV` (9 cada una) y
`Resumen de Valoración` (1): las copias referencian celdas propias donde la maestra referencia otras. Decidir si la maestra adopta esos cambios (entonces se
actualiza la plantilla) o si la hoja de NFLX vuelve a la fórmula de la maestra (REGLAS §5A: no reconstruir fórmulas por empresa).
NKE, NVDA y META siguen en la cola de `unificacion_hojas.py` (tarda ~20 min por hoja); NKE y META tienen 7 pestañas añadidas y NVDA 2.

## Resultado completo · unificación de las 4 hojas accesibles (26-oct)
Informes en `unificacion/<T>.json`. **Selectores: 122 de 122 conservados en las cuatro** (NFLX, NVDA, NKE, META). Ninguna hoja está unificada:

| Hoja | Pestañas añadidas | Fórmulas de la maestra perdidas (de 21.265) | Editadas | Dónde |
|---|---:|---:|---:|---|
| NFLX | 0 | 336 | 233 | Sensibilidad por múltiplo (Base 9 columnas), métodos y Financials Multiples |
| NVDA | 2 | 6.436 | 8.594 | Motor sensibilidad DCF; Trailing Valuation; Income Statement |
| NKE | 7 | 4.069 | 11.227 | Motor sensibilidad DCF; Income Statement; Financials Multiples |
| META | 7 | 110 | 2.499 | Motor sensibilidad DCF; Financials Multiples; Income Statement |

Las pestañas añadidas **no se pueden borrar**: 13 (NVDA), 24 (NKE) y 170 (META) fórmulas editadas las citan. Unificar estas hojas exige rehacerlas desde la maestra.

## Bloqueo decisivo: Drive
La cuenta de servicio `jmr-valuation-bot@jmr-valuation-508617.iam.gserviceaccount.com` **no puede crear archivos** (Drive responde `storageQuotaExceeded`) y **no tiene permiso sobre las hojas de las otras 29 empresas** (archivadas el 24-oct). Con autorización completa no se puede saltar eso; hace falta una de estas acciones de una persona con acceso a Drive:
- **A (recomendada):** para cada empresa, abrir la maestra (`1OYhz6ulMNNUAs-aW8q9FatOJgmfKAVTBAOmRMhqZzaY`) → Archivo → Hacer una copia, llamarla «Modelo JMR - <TICKER> - <fecha>», compartirla con el correo de la cuenta de servicio como Editor y pasar el ID. Con el ID se ejecuta `bash scripts/valorar.sh <T> <ID> "<pares>" "<industria>"`.
- **B:** compartir con la cuenta de servicio (Editor) las hojas antiguas de la carpeta «Valoraciones antiguas»; luego se reinician en el sitio con `reset_from_master.py --sheet-id ... --allow-destructive-reset` tras respaldar sus fórmulas en JSON.

## Actualización · carpeta compartida (26-oct, tarde)
Se compartió con la cuenta de servicio la carpeta **AAA Finanzas** (`1IS-H1WlSq71AWZXAE6r3LOhJXegSwLkz`). Ahora se ven sus 263 elementos
(documentos fuente, `.md` de valoraciones antiguas, plantillas y respaldos), pero **ninguna de las hojas de las 29 empresas antiguas**: los IDs
de `reference/multiplos_v3/*_anclas.json` y de `hojaGoogle` siguen dando `PermissionError` (existen, pero no están compartidas con la cuenta).
Las dos carpetas donde `REGLAS` §10 dice que están archivadas dan 404 para la cuenta:
- Valoraciones antiguas: `https://drive.google.com/drive/folders/10HZCGoZ4hKVqtg6ekcyYHsm8IHPZOBVLq`
- Revisiones sustituidas: `https://drive.google.com/drive/folders/1M2sWqAR60HBIBx0JbRn057kawpD9ZsZG`
Falta compartir esas dos carpetas (Editor) con `jmr-valuation-bot@jmr-valuation-508617.iam.gserviceaccount.com`. La cuenta sigue sin poder crear archivos
nuevos (cuota de Drive 0), así que la vía es reiniciar las hojas antiguas en el sitio (Opción B).
Nota de seguridad: dentro de AAA Finanzas hay un archivo `jmr-valuation-508617-64baa7fd0964.json` (parece la clave de la cuenta de servicio) y una carpeta `credentials`.
