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
