# CELH Floyd R3 — historias, DCF y sensibilidad
Revisión `CELH-REBOOT-3T26-R1`; 10-nov-2026; ChatGPT GPT-6. **PARCIAL ECONÓMICA**, no dictamen de compra.

Tres DCF originales separados (motor de 17 hojas, sin editar fórmulas):
- Conservadora: https://docs.google.com/spreadsheets/d/1NpAfVDSyUCpnmNeiFaF9b-c2RxD-JbF3hPSH3Rup-tE/edit
- Base: https://docs.google.com/spreadsheets/d/1nZ0USHr2Wa_MX6ykOCsmJuLMFdDJrtBUFQFwOkFib40/edit
- Optimista: https://docs.google.com/spreadsheets/d/1SeAuYF8mS_ejX591XEa6Hc8_SypfbO_bNVw921sZ9JE/edit

**Historias y drivers** C/B/O: crecimiento FY+1 a 5 6%/11%/16%; EBIT normalizado US$412,375/505/565 millones, márgenes 13,01%/15,93%/17,83%; Sales-to-Capital 1,35/1,90/2,50; ROIC terminal 8%/11%/14%; WACC inicial común 7,398%, terminal 9,11%; g perpetuo 3%; probabilidad tentativa 25/50/25. Fuente Rf US Treasury 10Y 4,88% (9-nov-2026); ERP Damodaran 4,41% (1-nov-2026). El addback Base 92,625 M de los gastos por terminación LTM 169,522 M es **supuesto no auditado**.

**Salida automática Ginsu antes de preferentes:** valor operativo C/B/O US$4.416,993/7.969,516/12.559,006 M; equity antes preferentes US$4.442,907/7.995,430/12.584,920 M. Las salidas por acción sin claim Pepsi C/B/O = US$17,65/31,76/49,99, no son valor económico de la acción común.

**Puente simplificado A/B no certificado:** C US$13,14; B US$27,07; O US$43,84; esperado 27,78, MOS35% Base 17,60. Se usa reclamación/reparto estático de Series A (US$550 M o 22 M acciones a strike US$25) y Series B (US$585 M o 11,3 M acciones a US$51,75). **No usa calendarios 2031/2032/2035/2038 ni dividendos preferentes acumulativos 5% ni valor de opción**. No publicar como valor intrínseco final. SEC 10Q Nota de mezzanine: https://www.sec.gov/Archives/edgar/data/1341766/000134176626000062/celh-20260930.htm

**75 corridas del motor** en `SENSIBILIDADES_R3_CELH.json`: matrices 5×5 crecimiento/margen EBIT, WACC/g, ROIC terminal/g; centros 27,07253593 (sensible al puente provisional); DCF inverso a US$33,19 implica g FY1–5 ~15,386% o margen sostenible ~18,76%, manteniendo demás drivers Base. Las corridas restauraron los inputs Base.

**Puntos materialmente pendientes:** discontinuidad ROIC año10 (~17,40%) vs terminal (11%); Ginsu input B29, B32 heredadas dependen de B27/B31 e impiden trayectorias independientes margen/S/C en dos períodos sin cambiar fórmulas; valoración separada de preferentes con sus dividendos y opciones; RSU y tratamientos leases/caja restringida; auditoría diff motor 1.297 fórmulas/76 comentarios; sincronización oficial SHA-256. R6 independiente NO ejecutada.

**PASOS 4/6; AISLAMIENTO=PARCIAL.** No hay publicación.

## Actualización de cierre técnico (10-nov-2026)
Se documentó sensibilidad de valor temporal de preferentes Pepsi en `PEPSI_PREFERENTES_DIAGNOSTICO_R3.md`: Base estático US$27,07 frente a escenario diagnóstico Black–Scholes simplificado US$25,58, diferendo aproximado US$1,50/acción. Usa 60% volatilidad y 90% condicionante citados por SEC *para la modificación de 2025*, no recalibrados al corte 2026. No sustituye DCF, no constituye reclamo preferente contractual certificado; publicar sigue bloqueado. R6 reservado.
