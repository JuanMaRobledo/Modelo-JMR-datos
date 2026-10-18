# Modelo JMR — Auditoría de ponderaciones (18-oct-2026)

**Alcance**: primera pasada estructural sobre los 38 JSON vigentes publicados en `valoraciones/`, y contraste económico selectivo con expedientes de `JMR-valuation/reference/multiplos_v3`. **No es certificación económica de los 38 expedientes**. El respaldo de anclas, comparables y estados requiere revisión individual antes de fijar pesos definitivos.

## Resultado de la primera pasada

- **38 valoraciones; 798 matrices esperadas**, con 723 centros conciliados y 75 N/D. N/D no es necesariamente un error: puede expresar denominador no interpretable.
- **11 brechas materiales** con diferencia absoluta de VP3 de múltiplos ponderados respecto a DCF Base superior al 30 %: AAPL, AFYA, AMZN, CELH, EPAM, MCD, NVDA, NVO, PFE, PLTR y SHAK.
- **7 expedientes especiales**: NFLX (ahora conciliado con Sheets, pares pendientes), GRUPOARGOS, PFGRUPOARG, MP, META, MU y P911.
- **20 restantes**: conservar sin republicar mientras se valida la calidad económica y editorial.
- Los métodos P/V y P/BV siguen calculados, con peso 0 salvo decisión individual sustentada. No sustituir P/BV por un número si el patrimonio común es negativo o no conciliado.
- El promedio contempla Conservador, Base y Optimista. Disrupción se muestra fuera del promedio; DCF Base conserva primacía en el MOS.

### Fórmula de diagnóstico

`Brecha % = 100 × [(Σ peso_método × VP3 Base_método / Σ pesos_métodos) / DCF Base vigente − 1]`

Se calcula solo si el expediente tiene DCF Base positivo, métodos coincidentes y centros VP3 numéricos en la valoración guardada. **Comparar valores hoy y FY+3 sin descuento induce una brecha falsa**. El umbral de ±30 % solamente prioriza auditoría: ni prueba que el DCF sea correcto ni obliga a modificar el múltiplo.

## Cambios propuestos en esta rama, con respaldo

**Netflix (NFLX).** Al auditar la hoja nativa Google vigente (18-oct-2026), se encontró que el JSON de publicación antiguo tenía **100 % DCF**, mientras que la hoja contiene **60 % DCF y 40 % múltiplos**. También comprobamos que los HTML de las hojas ya exportados en el JSON sí reflejaban 60/40, por lo que la primera corrección que consideraba 100 % como vigente era errónea. Se rectificó y concilió el registro estructurado y el análisis con la hoja: **DCF Base intrínseco US$71,68; múltiplos Base descontados US$87,60; mezcla secundaria Base US$78,05; objetivo FY+3 US$108,33; MOS 35 % sobre DCF Base → US$46,59**. Las 16 matrices conciliadas y cinco N/D permanecen. Se conservan sin cambio los supuestos del DCF, el MOS, el precio y las historias. Los comparables y el fundamento económico de los múltiplos siguen siendo provisionales.

Respaldos: `respaldos/ponderaciones-2026-10-18/NFLX-selector-previo.json` y `respaldos/ponderaciones-2026-10-18/NFLX-analisis-previo.json`. Además, el historial Git conserva versiones integrales.

## Hallazgos económicos con evidencia anterior

| Emisor | Decisión provisional | Justificación / condición |
|---|---|---|
| SHAK | Conservar DCF principal, EV/EBITDA, P/E y P/OCF como contraste | La historia relevante es corta y el ROIC de pares difiere materialmente; EV/FCFF y P/FCFE no son anclas sostenibles. No ajustar pesos para cerrar brecha de +310 %. |
| PLTR | No elevar peso relativo por la cotización histórica | El ancla de crecimiento de 82 % no equivale al múltiplo de FY+3 al crecer 40 %. Verificar conciliación de utilidades proyectadas y EBITDA; brecha +152 %. |
| CELH | Reducir confianza en historia y ajustar pares de forma fundamentada | Cargos extraordinarios por distribución y corto período comparable. Brecha +129 %. |
| DUOL | Mantener EV/FCFF y P/E como métodos relativos principales, a la espera de control de historias | Expediente identifica tratamiento de SBC e impuestos extraordinarios; discrepancia Base actual −18 % no amerita forzar una nueva ponderación. |
| GRUPOSURA / PFGRUPSURA | Priorizar SOTP como fundamento, P/E solo contraste | Escisión y cambio del perímetro contable, comparables heterogéneos y denominadores propios de holding financiera. |
| AFYA | Conservar mezcla provisional; revisar sensibilidad a pares brasileños | Múltiplos de educación superior deprimidos frente al crecimiento DCF; brecha −32 %. |
| EPAM | Conservar brecha explícita y revisar presión estructural de IA en márgenes | El mercado descuenta menor crecimiento que el DCF; brecha −41 %. |

## Matriz de estado de las 38 empresas

| Empresa | DCF reportado | Múltiplos sugeridos o registrados | Brecha relativa VP3–DCF | Centros N/D | Próxima decisión |
|---|---:|---:|---:|---:|---|
| AAPL | 40 % | 60 % | +49.2 % | 3 | Revisar anclas y pares |
| ADBE | 60 % | 40 % | +12.2 % | 0 | Mantener provisional |
| ADSK | 40 % | 60 % | -4.5 % | 0 | Mantener provisional |
| AFYA | 40 % | 60 % | -32.4 % | 0 | Revisar anclas y pares |
| AMZN | 40 % | 60 % | +34.2 % | 0 | Revisar anclas y pares |
| BSX | 40 % | 60 % | +4.8 % | 0 | Mantener provisional |
| CELH | 40 % | 60 % | +128.8 % | 0 | Revisar anclas y pares |
| CMG | 40 % | 60 % | +26.8 % | 0 | Mantener provisional |
| DPZ | 40 % | 60 % | +2.8 % | 3 | Mantener provisional |
| DUOL | 60 % | 40 % | -18.1 % | 0 | Mantener provisional |
| EPAM | 40 % | 60 % | -40.7 % | 0 | Revisar anclas y pares |
| GOOG | 40 % | 60 % | -9.5 % | 0 | Mantener provisional |
| GRUPOARGOS | N/D | 60 % | No calculable | 21 | Conciliar esquema |
| GRUPOSURA | 40 % | 60 % | -21.1 % | 8 | Mantener provisional |
| INTU | 40 % | 60 % | -29.8 % | 0 | Mantener provisional |
| LULU | 40 % | 60 % | -4.2 % | 0 | Mantener provisional |
| MCD | 40 % | 60 % | +57.3 % | 3 | Revisar anclas y pares |
| META | N/D | 60 % | No calculable | 0 | Conciliar esquema |
| MP | 80 % | 0 % | No calculable | 3 | Conciliar esquema |
| MSFT | 60 % | 40 % | -29.9 % | 0 | Mantener provisional |
| MU | N/D | 60 % | No calculable | 0 | Conciliar esquema |
| NFLX | 60 % | 40 % | No calculable | 5 | Conciliar esquema |
| NKE | 40 % | 60 % | -8.4 % | 0 | Mantener provisional |
| NU | 60 % | 40 % | +16.4 % | 0 | Mantener provisional |
| NVDA | 60 % | 40 % | +43.4 % | 0 | Revisar anclas y pares |
| NVO | 55 % | 45 % | +52.6 % | 0 | Revisar anclas y pares |
| ONON | 60 % | 40 % | +12.9 % | 0 | Mantener provisional |
| P911 | N/D | 60 % | No calculable | 0 | Conciliar esquema |
| PAGS | 40 % | 60 % | -1.2 % | 0 | Mantener provisional |
| PFDAVVNDA | 40 % | 60 % | -26.0 % | 0 | Mantener provisional |
| PFE | 55 % | 45 % | +87.1 % | 0 | Revisar anclas y pares |
| PFGRUPOARG | N/D | 60 % | No calculable | 21 | Conciliar esquema |
| PFGRUPSURA | 40 % | 60 % | -21.1 % | 8 | Mantener provisional |
| PLTR | 60 % | 40 % | +152.0 % | 0 | Revisar anclas y pares |
| PYPL | 40 % | 60 % | -29.2 % | 0 | Mantener provisional |
| SHAK | 60 % | 40 % | +310.0 % | 0 | Revisar anclas y pares |
| UBER | 60 % | 40 % | -2.9 % | 0 | Mantener provisional |
| ZTS | 40 % | 60 % | -10.5 % | 0 | Mantener provisional |

**Nota**: NFLX refleja ahora el 60/40 comprobado en la hoja nativa y conciliado en la rama; GRUPOARGOS y PFGRUPOARG conservan metadatos históricos no aplicables, a la espera de un SOTP terminado. En META, MU y P911 el peso DCF debe leerse del arreglo `metodos` antes de considerar una normalización; su ausencia en `descuentoMultiples.pesoDcf` no implica necesariamente un defecto económico.

## Puertas de publicación por emisor

1. Confirmar ticker, moneda, acciones diluidas, fecha de corte, niveles hoy / FY+3 / VP3 y el DCF Base vigente.
2. Conservar la versión anterior, comparar los cambios y garantizar que el MOS siga referenciado solo a DCF Base.
3. Revisar régimen histórico, exclusión de outliers justificada, mediana de pares fechada, ajustes por márgenes, reinversión, deuda, ROIC, riesgo, SBC y recompras; por método explicar el **porqué del múltiplo**.
4. Seleccionar la importancia de EV/EBITDA, EV/FCFF, P/E, P/FCFE, P/OCF, P/V y P/BV por emisor, sin dar peso positivo a N/D. Evitar doble conteo: los múltiplos comparten supuestos con el DCF y entre sí.
5. Conciliar las 21 matrices (siete métodos por tres historias) con VP3 Base, y dejar N/D explicados cuando corresponda. La disrupción se presenta en bloque independiente.
6. Ejecutar pruebas de paridad registro ⇔ hoja ⇔ artículo ⇔ visor y auditoría visual accesible. Republicar **solo** si hubo corrección económica o editorial verificada; registrar SHA y ruta del respaldo.
7. Dejar constancia de que una brecha grande **no** debe desaparecer por manipular el peso del método.

**Estado al 18-oct-2026:** los 38 expedientes han pasado una revisión **estructural**; solo NFLX tiene una sincronización estructural y editorial con la hoja vigente preparada en esta rama. Los restantes no se alteran; sus certificaciones económicas y posibles republicaciones continúan pendientes.
