# CELH Floyd R1–R6 · R1 identidad y corte

- Agente real: ChatGPT GPT-6; ejecución conversacional con GitHub/Google Drive y web. Esfuerzo: razonamiento técnico; motor ejecutable no utilizado.
- Revisión: `CELH-REBOOT-3T26-R1`. Fecha preparación: 2026-11-10. Estado: **CANDIDATO**.
- Corte contable: 2026-09-30 (10-Q); FY 2025 (10-K); precio **USD 33,19**, cierre 2026-11-09. Escala USD millones.
- Fuente original 10-K FY2025: https://www.sec.gov/Archives/edgar/data/1341766/000134176626000024/celh-20251231.htm
- Fuente original 10-Q 3T2026: https://www.sec.gov/Archives/edgar/data/1341766/000134176626000062/celh-20260930.htm
- Cotización: https://chartexchange.com/symbol/nasdaq-celh/historical
- Rf USD Treasury 10Y 2026-11-09 **4,88%**: https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value_month=202611&type=daily_treasury_yield_curve
- ERP Damodaran a 2026-11-01 **4,41%**, modified payout: https://pages.stern.nyu.edu/~adamodar/New_Home_Page/home.htm
- **Seis IDs distintos:** H https://docs.google.com/spreadsheets/d/1EUBryCf1jKcrQHNywOcUM4H9COQnNkDPw_CSXlxm9WU/edit; D-B https://docs.google.com/spreadsheets/d/1nZ0USHr2Wa_MX6ykOCsmJuLMFdDJrtBUFQFwOkFib40/edit; D-C https://docs.google.com/spreadsheets/d/1NpAfVDSyUCpnmNeiFaF9b-c2RxD-JbF3hPSH3Rup-tE/edit; D-O https://docs.google.com/spreadsheets/d/1SeAuYF8mS_ejX591XEa6Hc8_SypfbO_bNVw921sZ9JE/edit; M https://docs.google.com/spreadsheets/d/1ytZ7woFOuq-mhgkA1jaREuGmdQR6jF0LHKv-4oOQSe4/edit; A https://docs.google.com/document/d/1KguK_xZWgWr7a5j92O-Ye7_mmN7up5kWN8QlxBeb8c0/edit.
- Plantillas copiadas, no editadas, de carpeta oficial https://drive.google.com/drive/folders/1fFlAbKsdMKfjPB_nPcc6Y-9hQ7tQj14t . D-C/D-O tienen 17 hojas; D-B tiene 17 hojas de motor + Presentación y Resumen (19); M 16 hojas; H 12.
- Contrato main `docs/CONTRATO_REBOOT_JMR.md` blob SHA `2ab811f220602915e68ff477bbe0783ee10da682`, perfil Floyd, contrato `jmr-reboot-3libros-v1`.
- Revisión anterior `CELH-20261028-A1` preservada e identificada por `catalogo.json/reconfiguracion/CELH`; no está activa bajo nuevo contrato. Floyd F1–F5 de 2026-11-08 también legado, no es R1–R6.
- PASOS **5/7**: ticker/fecha/fuentes, plantillas/copias, precios, Rf/ERP y arquitectura comprobados. Pendientes: inventario de todas las fuentes auxiliares y comparación automatizada fórmulas/comentarios post-copia.
- Controles: **APROBADO** seis documentos reales con 17 hojas Ginsu visibles y corte, cotización, Rf y ERP; **PARCIAL** integridad del motor (sin diff automatizado ni comentario por comentario); **NO_EJECUTADO** auditoría de conexión hoja/JSON/app.
- AISLAMIENTO de fuente/plantilla: copias nuevas verificadas; **AISLAMIENTO=PARCIAL** hasta diff integral.
- Siguiente: R2 completar 10 FY, clasificación de preferentes/DSD, reconciliación SEC y fórmulas.
