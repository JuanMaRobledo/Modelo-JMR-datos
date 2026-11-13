# CELH · Control contractual de instrumentos preferentes y sincronización

**Revisión:** `CELH-REBOOT-3T26-R1` · **Fecha:** 10 de noviembre de 2026 · **Estado:** CANDIDATO — BLOQUEO MATERIAL. R6 reservada.

## Fuente primaria: SEC 10-Q a 30/09/2026
https://www.sec.gov/Archives/edgar/data/1341766/000134176626000062/celh-20260930.htm (Nota 12 «Mezzanine equity», pp. 29–33; balance p.5).

### Derechos Pepsi
- Serie A 1.466.666 preferentes, valor nominal de emisión US$550 millones, preferencia de liquidación **US$550 M**; precio de conversión US$25/acción ordinaria; aproximadamente **22,0 M** acciones en conversión.
- Serie B 390.000 preferentes, valor nominal de emisión US$585 millones, preferencia de liquidación **US$585 M**; precio conversión US$51,75; aproximadamente **11,3 M** acciones ordinarias.
- Equity mezzanine en balance US$852,355 M (A) y US$907,620 M (B), **US$1.759,975 M contables**, no equivalente a valor justo actual ni a deuda bancaria.
- Dividendos acumulativos **5% anual**, pagaderos en efectivo, especie o combinación; participaciones en dividendos ordinarios as-converted. 9M2026 dividendos pagados A US$20,6 M y B US$21,9 M.
- La conversión automática queda supeditada a condiciones, incluyendo desde **28/08/2031** una prueba de cuota de mercado y VWAP superior al precio de conversión; desde **28/08/2032** hay opción de conversión para la sociedad si el VWAP supera el precio. También pueden producirse eventos al terminar distribución. La opción de rescate de la sociedad comienza desde 2032 o terminación de acuerdos, bajo condiciones; Pepsi puede pedir rescate en **2032, 2035 y 2038**, con liquidación proporcional y penalizaciones por demora.
- En 2025 la compañía utilizó modelo **Monte Carlo** con volatilidad **60%** y probabilidad de condiciones de mercado **90%** al estimar la modificación de la Serie A; esa probabilidad fechada no se puede trasladar sin revisión al corte 2026.

### Por qué el valor actual es provisional
Las 3 copias del Ginsu calculan **valor total del equity antes de descontar los derechos preferentes**: C US$4.442,907 M; B US$7.995,430 M; O US$12.584,920 M (cálculos de copia Ginsu, USD millones). Un puente simplificado puramente estático resta la preferencia de liquidación o diluye por acciones si supera strike. Produce por ordinaria C US$13,14; B US$27,07; O US$43,84, pero **NO es valor justo contractual**. Ignora el valor temporal de la convertibilidad, eventos contingentes y el PV de dividendos futuros. Tampoco se deben descontar a la vez 1.760 M de carrying y diluir 33,3 M comunes. **No publicar valores per-share como definitivos.**

### Solución económica exigida para R3
Implementar como **cálculo externo independiente del motor de 17 hojas**, previa aprobación de infraestructura, una valoración de derechos preferentes A/B que respete: plazo hasta eventos 2031/2032/2035/2038, 5% dividendos, opción de rescate, escenarios de VWAP y cuota de mercado, volatilidad justificada al corte, posible dilución y capital preferente como componente del capital. Registrar sensibilidad, conciliar puente EV→deuda→preferred→common y comprobar que los dividendos no se descuentan dos veces. El ajuste se documenta en A, no se modifica el motor Ginsu.

## Sincronización H→D / H→M / D→M
Contrato normativo `Modelo-JMR/docs/CONTRATO_REBOOT_JMR.md` (v1.0) y `modelo/REGLAS_VIGENTES.md` v38: solo **scripts predefinidos con SHA-256**, **no IMPORTRANGE**, no pegar cálculos.

En esta sesión se probaron enlaces IMPORTRANGE en **574 entradas M**, **39 entradas D**, y 22 celdas adicionales para totales de M. El acceso entre libros funcionó, pero la inspección normativa mostró que **no está permitido**. Se revirtió la prueba, restaurando **603 celdas de M** (incluidas seis entradas '0' no sustentadas, y 22 totales vacíos) y **39 entradas D** al valor snapshot correspondiente. Relectura limitada: **0 fórmulas IMPORTRANGE** en estados M (A1:L40) y D Input Sheet (A1:C72), sin errores de cálculo en esas zonas. Las fórmulas de las 17 hojas del Ginsu no se tocaron. El ensayo no prueba integridad completa de las 1.297 fórmulas ni de los 76 comentarios.

Los archivos permanecen con datos SEC como **fotografía de revisión**, pero **NO existe evidencia de ejecución del sincronizador oficial con SHA-256** en esta revisión. Los nombres de scripts identificados en `JMR-valuation/scripts/` no ofrecen una orden canónica inequívoca específica `H→D→M` del nuevo contrato. Debe identificarse el script canónico, ejecutarse en un entorno con acceso autenticado a las seis hojas y registrarse huella, inputs, outputs y conciliación. **Bloqueo de R4 y publicación**, no autoriza cambiar la arquitectura ni scripts durante valoración.

## Otros bloqueos
- Libro M `Supuestos y control!B60`: **FALTAN DATOS Y SUPUESTOS**, B63 **PENDIENTE**, B64 **NO PUBLICAR**.
- M `Balance Sheet!K51:L51` exige mezzanine redimible; la celda clasificatoria es «intereses no controlantes redimibles» y **no debe utilizarse para disfrazar acciones preferentes Pepsi como NCI**. Se requiere un traspaso aprobado que reconozca mezzanine distinta del capital ordinario y del NCI sin editar plantilla desde valoración.
- En 2025 hay efectivo restringido (US$141,121 M) y compensaciones diferidas de acuerdos de distribución: no sumar caja restringida a caja disponible.
- No se completó el diff motor copiado vs plantilla ni análisis robusto de opciones laborales/PSU/RSU, leases y normalización de márgenes/ROIC.
- La ficha antigua y el catálogo de `main` siguen intactos, el PR está en borrador y **R6 no se ejecuta**.

**Dictamen técnico:** cuantificación DCF provisional reproducible; R1–R3 parcialmente completados; R4 sin compuerta; R5 no publicable.
