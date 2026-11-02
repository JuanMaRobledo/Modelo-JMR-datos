
# TERPEL · TERPEL-20261102-A12-R1 · Fase 1 · CERRADA CON CONTROLES PENDIENTES

Fecha: 2026-11-02 · Herramienta: ChatGPT GPT-6 (esfuerzo no verificable como parámetro externo), GitHub, Google Drive/Sheets, consulta de documentos originales.
Estado financiero: CANDIDATO. NO EN_REVISION, NO PUBLICADO, NO AUDITADO.
Operación: desde cero con recuperación del expediente piloto original TERPEL (1-nov). Ninguna valoración anterior de TERPEL modificada.
Método: JMR A-1.2, operativa, FCFF/WACC, 4 escenarios posteriores; moneda nominal COP y NIIF consolidadas.
Identidad: Organización Terpel S.A., ordinaria BVC TERPEL, FY termina 31-dic.
Hoja oficial de esta revisión: https://docs.google.com/spreadsheets/d/1a2LkE76RH7Za-q0_fTp3FwSt4rieRf5C5wXfrOUhwkE/edit
Carpeta AAA Finanzas / Análisis / TERPEL: https://drive.google.com/drive/folders/1osSAnybYR42dewzs0C53G-HrZ9Xxffs-
Plantilla de origen: JMR-valuation/reference/plantillas.json vigente.ia (1e-lbQmCkObfq74YLpWnMmIidmcdsJQ-6uN4oiHnNTEQ); COPIA independiente con 46 pestañas nativas verificadas.
Inventario con períodos, fuentes, escalas, página y celdas: [INVENTARIO_INSUMOS_F1.md](INVENTARIO_INSUMOS_F1.md).

## Hecho y verificado

- AISLAMIENTO=OK: cambios solo de TERPEL en hoja nueva y esta rama; sin alterar plantilla, catálogo, otras empresas, corte global, Cartera ni web pública.
- Cotejados estados financieros CONSOLIDADOS: FY2022/FY2023 auditados, FY2024 comparativo re-presentado/FY2025 auditados, intermedios H1-2025/H1-2026 revisados por KPMG 13-ago-2026; fuentes individuales y notas en inventario y celdas.
- Fuente principal: estados reportados en M$ (miles COP), convertidos a millones COP dividiendo 1.000; acciones en millones. No usar estados separados como si fueran consolidados.
- Copia de 46 hojas en carpeta correcta; datos en Income Statement H:L FY2022-FY2025 + LTM; Balance Sheet H:L FY2022-FY2025 + junio 2026; Cash Flow Statement H:L FY2022-FY2025 + LTM; Input sheet A1,B4,B5,B8:B10.
- Ingresos LTM jun-2026: 39.259.184,905 MM COP, Income Statement!L3; EBIT LTM: 1.455.302,242 MM COP, L12; CFO 1.133.288,019 MM COP, Cash Flow Statement!L13; capex PPE+intangibles -332.622,922 MM COP, L15. Fórmulas FY2025 + H1-2026 - H1-2025 comprobadas en la hoja, con separador decimal local.
- Activos/Deuda/Equity al 30-jun-2026 tomados como BALANCE de esa fecha, no se sumaron como flujos. Acciones ordinarias 181.424.505 en circulación, 181,424505 millones en hoja.
- Nota 24 del intermedio 2026: préstamos/bonos corrientes y no corrientes separados de NIIF16 lease en Balance Sheet!K20:L21, K25:L26. Excluidos derivados financieros. Input sheet!B16 vía fórmula muestra deuda+leases al 30-jun-2026 de 3.702.161,425 MM COP sin duplicación.
- Pruebas independientes con efectivos de celdas: 5/5 balances de activo-pasivo-patrimonio (FY2022, FY2023, FY2024, FY2025, junio 2026) residual 0,0000 MM COP; 5/5 puentes ingresos-costo-SGA-otros gastos netos-EBIT (FY2022-2025, LTM) residual 0,0000 MM COP.
- Spot check de fórmulas Input/Income/Balance/CashFlow: Income Statement!L3/L12, Balance Sheet!J9:L9/J15:L15, Cash Flow Statement!L13/L15 sin errores de recálculo tras normalización decimal. Las hojas de DCF/proyecciones intactas; ninguna entrada de supuestos introducida.
- Categorías sectoriales Colombia y Oil/Gas Distribution elegidas de listas de validación nativas, industria provisional.

## Pasos oficiales Fase 1 — 10/10 tratados, reservas
0. Firewall: HECHO, aislamiento.
1. Identidad, método, revisión: HECHO TERPEL-20261102-A12-R1.
2. Fuentes: HECHO para tres expedientes primarios FY2022-25/H1-26, PARCIAL para revisión exhaustiva de la Información Relevante SFC; notas de noticias recientes 28-oct AutoGLP y 29-sep Jet A-1.
3. Corte de mercado: PARCIAL. Fecha 30-oct-2026 fijada, precio bursátil NO FIJADO. StockAnalysis cierre 18.220 COP; Bloomberg Línea/MarketScreener último 18.260 COP (diferencia 40 COP); precio 18.480 de La República se refiere al cierre previo. TES COP 10 años 30-oct no verificado. BanRep política monetaria 12,25% NO sustituye tasa TES para valorar. No se cambió corte global USD.
4. Hoja: HECHO; copia genuina y única en carpeta oficial, 46 pestañas.
5. Estados completos: PARCIAL. Estructura base y LTM utilizable con fórmulas, faltan D&A, desglose flujo directo y capital trabajo, series leasing 2022-24 y otros ajustes; no se rellenaron datos faltantes con ceros artificiales. CFO menos CapEx no es FCFF.
5b. Auditoría IFRS: PRUEBA EQUIVALENTE PARCIAL, únicamente 5/5 identidades de balance y 5/5 puentes EBIT. Script IFRS oficial NO EJECUTADO.
6. Calidad resultados: DETECTADO sin normalizar: activos para venta, FY2024 re-presentado, arrendamientos, exposición geográfica, fuel-price pass-through, impuestos y posibles eventos no recurrentes.
7. Sector: PARCIAL; clasificadora Damodaran Oil/Gas Distribution, sector/competidores por refinar, noticias fechas; no hay consenso cuantitativo robusto ni TES COP 30-oct documentado.
8. Inventario: HECHO en archivo separado, escala, fuente, período y celdas; notas por entrada.

## Controles de cierre reales
- estados_completos.py TERPEL: NO EJECUTADO — falta entorno/credenciales para importar y ejecutar scripts oficiales; datos específicos aún incompletos.
- diff_formulas_plantilla.py --sheet-id ID: NO EJECUTADO — falta entorno oficial; solo pruebas de fórmulas acotadas, NO equivalencia total 46 pestañas.
- auditar_estados_ifrs.py: NO EJECUTADO — prueba equivalente solo 5 balances y 5 EBIT, no un auditor integral NIIF.
- inputs_completos.py y candados.py TERPEL: NO EJECUTADOS — faltan insumos de fase 2; no publicar.
- Precio bursátil BVC, TES a 10 años COP y ERP del mismo corte: PENDIENTE, no mezclar USD y COP; Input sheet!D1 deliberadamente vacío.
- Cantidad de acciones, identidades y moneda: COMPROBADO según alcance descrito.
- Control de corte Cartera/corte_vigente.json: NO MODIFICADO.
- Valor intrínseco/MOS35%: NO CALCULADOS ni prometidos como oficiales.

## Bloqueos materiales y para Fase 2
1. Confirmar cierre BVC 30-oct-2026 (18.220 vs 18.260), TES cero-cupón nominal COP 10 años de fecha coherente y prima madura/país sin doble contar soberano.
2. Completar D&A, capital de trabajo (por flujo directo/no indirecto), resultados no recurrentes, reinversión, saldo inicial capital invertido, 2022-24 leasing separado y otros activos/inversiones no operativos; fiscalidad, país y exposición por segmentos; verificar cobertura Información Relevante SFC.
3. Ejecutar auditar_estados_ifrs, estados_completos, diff_formulas_plantilla, inputs_completos y candados en ambiente oficial; resolver faltantes materiales antes de DCF.
4. Continuar sobre la MISMA hoja y revisión, nunca otra hoja ni copiar fórmulas a números. Fase 2 trabajará supuestos y cuatro historias A-1.2 desde Cost of capital worksheet/DCF, con valor Base, MOS35%, múltiplos pertinentes y trazabilidad completa.
5. Dejar TERPEL CANDIDATO; Fase 3 y publicación EN_REVISION NO iniciadas; auditoría Fase 4 por sesión/modelo independiente.

PASOS F1: 10/10 abordados; parciales 2,3,5,5b,7 justificados; controles técnicos oficialmente pendientes. Cierre honesto: CERRADA CON CONTROLES PENDIENTES (NO CERRADA, NO BLOQUEADA total).
