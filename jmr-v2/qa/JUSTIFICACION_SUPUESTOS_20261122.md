# Justificación de supuestos JMR V2 · 22-nov-2026

Ampliación editorial de las 22 valoraciones de la biblioteca V2. **No cambia supuestos, valores, motor, revisiones ni estados.** Paridad motor–libro 0,000 % comprobada antes y después; controles del expediente sin cambios (P02 auditoría independiente sigue pendiente en todas).

## Qué cambió
- Expediente (`justificaciones`): escenarios Conservador/Base/Optimista reescritos con tesis, crecimiento, márgenes, reinversión, ROIC, descuento, terminal, evidencia y contraevidencia; campos por supuesto. Se eliminaron los textos «Supuestos heredados del libro Floyd» (AAPL, CMG, MSFT, UBER) y los campos mal asignados de NVDA.
- Análisis (`blocks.supuestos`): sección «Justificación de cada supuesto» con tabla de contraste histórico, razón de cada supuesto, contraevidencia, pruebas de coherencia del motor (peso terminal, DCF inverso, sensibilidades) y correcciones pendientes.
- MELI R10: supuestos verificados contra «Input sheet» del libro R10 (30 %/20 %, margen 12 %→15 %, ventas/capital 3,5×, WACC 10,68 %, ROIC 18 %, g 4 %); se sustituyó el texto antiguo (32 %/24 %, 5 %→12 %).
- PDF regenerados con su generador original: 18 con `v2-render-homologados.py` (fidelidad previa ≥ 99,7 % de texto) y MELI/BSX/NU desde su HTML R8. XRX (sin HTML fuente): capítulo 10 recompuesto con el CSS R8 de BSX y empalmado; pies posteriores renumerados.
- Cierre editorial: AMZN, BSX, GOOGL, INTU, NU y XRX pasan a pendiente hasta actualizar las huellas de su manifiesto de cierre.

## Correcciones que requieren recalcular el libro (nueva revisión)

- **AAPL**: La beta apalancada 1,30 es entrada directa: sustituirla por beta bottom-up de la industria con fórmula, como en las revisiones más recientes.
- **AAPL**: La hoja registra calificación A1/A+; las agencias califican a Apple en el nivel máximo. Con un peso de deuda de ~1,7 % el efecto en el WACC es inmaterial, pero debe corregirse.
- **ADBE**: Homologar la tasa libre (5,12 % → 5,15 %) y la prima madura (4,41 % → 3,387 %, convención Damodaran nov-2026 del resto de la biblioteca); hoy el WACC terminal es 9,53 % frente a 8,54 % en las demás empresas. Requiere recalcular el libro y abrir R2.
- **AMZN**: El ventas/capital de los años 1–5 (1,0×) es más favorable que el observado: documentar la trayectoria de capex de 2027–2028 o ajustar el supuesto en una nueva revisión.
- **BSX**: Incorporar Penumbra en una nueva revisión cuando cierre la operación.
- **CMG**: El WACC inicial (7,97 %) es inferior al de una empresa madura (8,54 %) porque excluye los pasivos por arrendamiento de la deuda y usa beta directa 0,78. Recalcular con beta bottom-up de restaurantes y arrendamientos como deuda (método Damodaran) en una nueva revisión.
- **DPZ**: El WACC inicial (7,74 %) es inferior al terminal por el alto apalancamiento y la exclusión de arrendamientos; documentar por qué un emisor con deuda titulizada tiene menor riesgo que una empresa madura media o recalcular.
- **EPAM**: Contrastar el ventas/capital de 2,2× con el ratio incremental observado (~0,8×, afectado por adquisiciones) y documentar la política de adquisiciones futura.
- **GOOGL**: El ventas/capital de los años 1–5 (1,0×) es más del doble del observado (0,43×): documentar la normalización del capex o ajustarlo en una nueva revisión.
- **LULU**: El WACC inicial (8,22 %) es inferior al terminal (8,54 %); documentar la beta y la ERP usadas o igualarlo al terminal.
- **MELI**: Conciliar el fondeo de Mercado Pago y los arrendamientos en el puente de valor (salvedad de auditoría R9 vigente).
- **MSFT**: La beta 1,28 es entrada directa: sustituirla por beta bottom-up con fórmula.
- **MSFT**: La hoja registra calificación A1/A+; Microsoft tiene la máxima calificación (efecto inmaterial con un peso de deuda pequeño).
- **MSFT**: El ventas/capital de los años 1–5 (0,8×) duplica el observado: documentar la normalización del capex o ajustarlo en una nueva revisión.
- **NKE**: Completar opciones/RSU y la ERP primaria, identificadas como pendientes en el libro.
- **NU**: MÉTODO: Nu es un banco (capta depósitos y presta). El contrato exige valorar bancos con flujo al accionista (FCFE) o patrimonio descontado al costo del capital (Ke) con el motor «financieras», no con FCFF/WACC operativo: en un banco la deuda es materia prima y el margen EBIT y el ventas/capital no están bien definidos. Rehacer el libro con perfil «banco» y abrir R3.
- **NVDA**: Actualizar el corte (26-jul-2026) con el trimestre a oct-2026 cuando se incorpore al libro.
- **NVDA**: Contrastar el ventas/capital de 2,7× con el ratio incremental observado (~1,6×).
- **ONON**: Contrastar el ventas/capital de 3,0× con el observado (~2,1×) y documentar la reinversión en tiendas propias e inventario.
- **ONON**: Reflejar la recompra de hasta US$1.000 M autorizada en sep-2026 cuando se ejecute.
- **ORCL**: Actualizar beta y pesos de deuda/capital (datos de R3) cuando esté disponible la deuda de mercado.
- **PYPL**: El WACC inicial (8,18 %) es inferior al terminal porque la beta del sector (0,806) es baja; confirmar que «Business & Consumer Services» es la industria adecuada para un procesador de pagos.
- **UBER**: La beta 1,20 es entrada directa: sustituirla por beta bottom-up con fórmula.
- **XRX**: PUENTE DE VALOR: el déficit neto de pensiones (−US$498 M después de impuestos) no se resta. Según el método de Damodaran es una obligación asimilable a deuda; restarlo deja el patrimonio en aproximadamente −US$59 M (valor por acción cercano a cero).
- **XRX**: PROBABILIDAD DE FRACASO: un emisor CCC con muro de vencimientos 2028–2029 no debería tener 0 % en el Base; la tasa de impago histórica de emisores CCC supera ampliamente el 12 % usado solo en el Conservador.
- **XRX**: Ambas correcciones requieren recalcular el libro y abrir R2.
- **ZTS**: Documentar la evidencia de la reaceleración a 4 % o usar g igual al crecimiento de los años 2–5 en el Conservador.

## PDF

| Empresa | PDF | Páginas | SHA-256 |
|---|---|---|---|
| AAPL | jmr-v2/informes/AAPL/AAPL-V2-FY2026-R6_INFORME_FUNDAMENTAL.pdf | 27 | bf76edadd074e8d2… |
| ADBE | jmr-v2/informes/ADBE/ADBE_JMR_V2_20261116_R1_INFORME_FUNDAMENTAL.pdf | 24 | 117484f886411870… |
| AMZN | jmr-v2/informes/AMZN/AMZN-V2-LTM20260930-R1_INFORME_FUNDAMENTAL.pdf | 28 | c388ebd6f8170c1d… |
| BSX | jmr-v2/informes/BSX/BSX-V2-LTM20260930-R2_INFORME_FUNDAMENTAL.pdf | 36 | 9b379c8d4295aa61… |
| CMG | jmr-v2/informes/CMG/CMG-V2-LTM20260930-R5_INFORME_FUNDAMENTAL.pdf | 24 | 48387cb2db1d5ac9… |
| DPZ | jmr-v2/informes/DPZ/DPZ-V2-LTM20260906-R2_INFORME_FUNDAMENTAL.pdf | 25 | 303c7cd45b2f66fe… |
| DUOL | jmr-v2/informes/DUOL/DUOL-V2-LTM20260930-R6_INFORME_FUNDAMENTAL.pdf | 23 | fa3df2b240305165… |
| EPAM | jmr-v2/informes/EPAM/EPAM-V2-LTM20260930-R6_INFORME_FUNDAMENTAL.pdf | 24 | c42119df6abef4ce… |
| GOOGL | jmr-v2/informes/GOOGL/GOOGL-V2-LTM20260930-R1_INFORME_FUNDAMENTAL.pdf | 26 | b21652f30d78cf22… |
| INTU | jmr-v2/informes/INTU/INTU-V2-LTM20261031-R1_INFORME_FUNDAMENTAL.pdf | 33 | f9d75e9ecc392351… |
| LULU | jmr-v2/informes/LULU/LULU-V2-LTM20260802-R4_INFORME_FUNDAMENTAL.pdf | 24 | 45fe8f0717fef28f… |
| MELI | jmr-v2/informes/MELI/MELI-V2-LTM20260930-R10_INFORME_FUNDAMENTAL.pdf | 41 | 5d871750a3d6fa6e… |
| MSFT | jmr-v2/informes/MSFT/MSFT-V2-LTM20260930-R5_INFORME_FUNDAMENTAL.pdf | 25 | 396917fc9df959ce… |
| NKE | jmr-v2/informes/NKE/NKE-V2-LTM20260831-R5_INFORME_FUNDAMENTAL.pdf | 24 | 68e0e4a64e3ce930… |
| NU | jmr-v2/informes/NU/NU-V2-LTM20260930-R2_INFORME_FUNDAMENTAL.pdf | 30 | 26cefc72622a0e57… |
| NVDA | jmr-v2/informes/NVDA/NVDA-V2-FY26Q2FY27-R6_INFORME_FUNDAMENTAL.pdf | 28 | cabcd814f16e85d1… |
| ONON | jmr-v2/informes/ONON/ONON-V2-LTM20260930-R1_INFORME_FUNDAMENTAL.pdf | 27 | 979e6f9f6b822b66… |
| ORCL | jmr-v2/informes/ORCL/ORCL-V2-LTM20260831-R8_INFORME_FUNDAMENTAL.pdf | 26 | a211cdfc71987b8d… |
| PYPL | jmr-v2/informes/PYPL/PYPL-V2-LTM20260930-R2_INFORME_FUNDAMENTAL.pdf | 23 | 5173fcf7e003f54b… |
| UBER | jmr-v2/informes/UBER/UBER-V2-LTM20260930-R5_INFORME_FUNDAMENTAL.pdf | 24 | c23056f04f3898f4… |
| XRX | jmr-v2/informes/XRX/XRX-V2-LTM20260930-R1_INFORME_FUNDAMENTAL.pdf | 37 | bcc13279531cc3b9… |
| ZTS | jmr-v2/informes/ZTS/ZTS-V2-LTM20260930-R2_INFORME_FUNDAMENTAL.pdf | 27 | c5431e0c20b6d167… |
