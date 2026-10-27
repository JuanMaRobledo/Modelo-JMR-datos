# Conciliación de salidas por múltiplos — 27 de octubre de 2026

**Alcance:** inspección de SOLO LECTURA de los valores/fórmulas nativos en Google Sheets frente a `valoraciones/*.json`, usando los archivos existentes y la hoja `hojaGoogle` de cada registro. Sin revaloración, sin modificar entradas, fórmulas, valores, catálogo ni auditorías. Tolerancia operativa ±US$0,01/acción (para las empresas internacionales examinadas). Esta comprobación **NO sustituye** el control de identidad/equivalencia contra la plantilla maestra ni valida supuestos, WACC, métodos adicionales o dictamen completo.

## Resultados (16 archivos; una hoja por archivo)

| Empresa | Fórmulas / salidas numéricas | Conciliación JSON ↔ Sheets | Decisión |
|---|---|---|---|
| NFLX | 7/7 | Coinciden, tolerancia 0,01 | Salidas conciliadas |
| NKE | 7/7 | Coinciden, tolerancia 0,01 | Salidas conciliadas |
| META | 7/7 | Coinciden, tolerancia 0,01 | Salidas conciliadas |
| NVDA | 7/7 | Coinciden, tolerancia 0,01 | Salidas conciliadas |
| ADBE | 7/7 | Coinciden, tolerancia 0,01 | Salidas conciliadas, no publicada en catálogo |
| BSX | 7/7 | Coinciden, tolerancia 0,01 | Salidas conciliadas, no publicada en catálogo |
| EPAM | 7/7 | Coinciden, tolerancia 0,01 | Salidas conciliadas, no publicada en catálogo |
| MSFT | 7/7 | Coinciden, tolerancia 0,01 | Salidas conciliadas, no publicada en catálogo |
| NVO | 7/7 | Coinciden, tolerancia 0,01 | Salidas conciliadas, no publicada en catálogo |
| ONON | 7/7 | Coinciden, tolerancia 0,01 | Salidas conciliadas, no publicada en catálogo |
| UBER | 7/7 | Coinciden, tolerancia 0,01 | Salidas conciliadas, no publicada en catálogo |
| PYPL | 7/7 | P/S y P/BV difieren ≈−0,00059; bajo tolerancia | Salidas conciliadas, no publicada en catálogo |
| DUOL | 7/7 | P/S y P/BV del libro son **1,21091 USD** menores que el registro | Recapturar SOLO esas dos salidas y documentos afectados, tras investigar la causa |
| CELH | 7/7 | P/S y P/BV del libro son **0,17770 USD** menores que el registro | Recapturar SOLO esas dos salidas y documentos afectados, tras investigar la causa |
| SHAK | 7 fórmulas presentes / 5 salidas numéricas | EV/FCFF y P/FCFE devuelven vacío; ambos tienen peso cero. El registro también guarda vacío | Justificar explícitamente N/A por no aplicabilidad económica o corregir entradas necesarias; NO inventar precios |
| XP | **4/4 calculadas en el adaptador financiero**; 3 N/A documentadas | Coinciden P/E, P/FCFE, P/S, P/BV con `XP Múltiplos` | Fuente financiera conciliada; conserva auditoría condicionada |

**Total:** doce de dieciséis con 7/7 salidas numéricas conciliadas; DUOL/CELH con dos desajustes cada una; SHAK con dos salidas vacías; XP con cuatro fórmulas financieras + tres N/A. La etiqueta «conciliada» aquí significa **solo conciliación de las salidas por múltiplos**, NO que la valoración esté auditada ni publicada.

## Celdas fuente del método estándar
- `Descuento de múltiplos!J20:J24`: EV/EBITDA, EV/FCFF, P/E, P/FCFE, P/OCF.
- `PV!E42`: P/S (P/V).
- `PBV!E42`: P/BV.
- Antes de publicar, verificar existencia de las pestañas nativas `Financials Multiples`, `EVEBITDA`, `EVFCFF`, `PE`, `PFCFE`, `POCF`, `PV`, `PBV`, `Descuento de múltiplos`; la existencia de fórmula no prueba equivalencia con la maestra.

## XP: excepción financiera documentada
- P/E `XP Múltiplos!I6` = **13,73966**.
- P/FCFE `XP Múltiplos!I15` = **13,10947**.
- P/S `XP Múltiplos!I9` = **12,15685**.
- P/BV `XP Múltiplos!I12` = **12,32823**.
- `XP Control!B16`: «4 calculados; 3 N/A financieros»; EV/EBITDA, EV/FCFF y P/OCF no se calculan como múltiplos industriales en XP.
- Las hojas industriales comunes permanecen en blanco en esta empresa **intencionalmente**; no rellenarlas ni declarar 0/7 sin revisar el adaptador. El método principal es FCFE. PR financiero #166 y PR interfaz #106 distinguen este contrato.

## Próximas acciones, sin repetir trabajo
1. **DUOL, CELH:** verificar por qué el libro actual difiere de la foto del JSON en P/S/PBV; recapturar exclusivamente los valores de las fórmulas vigentes y actualizar sus referencias en análisis/auditoría si efectivamente cambian. No sobrescribir las fórmulas.
2. **SHAK:** documentar criterio N/A o recuperar los supuestos requeridos para que calculen EV/FCFF y P/FCFE, aun con peso cero; conservar evidencia económica.
3. **XP:** conservar como expediente financiero condicionado, comprobando fórmulas del adaptador; no forzar el esquema industrial.
4. **Resto:** mantener resultados existentes; completar conciliación de las tres piezas, validación de fórmulas contra la maestra y publicación del catálogo solo cuando corresponda. No rehacer ni revalorar automáticamente.

**Archivos de origen:** `valoraciones/<T>*.json` en este repositorio, asociados al `hojaGoogle` de cada registro. El catálogo oficial aún contiene NFLX, NKE, META, NVDA y XP. Los once restantes están en inventario, pero no se deben declarar publicados por este documento.

**Automatización existente:** `JuanMaRobledo/JMR-valuation/scripts/verificar_multiplos_hoja.py`, que coteja los precios presentes (no FY+3) con las salidas originales, y tiene adaptador financiero específico para XP. Debe ejecutarse sobre las hojas reales cuando se vaya a publicar o recapturar.
