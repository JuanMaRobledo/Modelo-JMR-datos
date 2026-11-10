# Reconfiguración de UBER y CMG al perfil Reboot · estado al 2026-11-10

| Fase | UBER-REBOOT-3T26-R1 | CMG-REBOOT-3T26-R1 |
|---|---|---|
| R1 corte e identidad | HECHA (5 libros creados) | HECHA (5 libros creados) |
| R2 Históricos | HECHA (SEC XBRL; FY2017–FY2025 + LTM) | HECHA (FY2016–FY2025 + LTM) |
| R3 historias y DCF | PENDIENTE | HECHA (Cons 17,69 · Base 32,28 · Opt 40,47) |
| R4 múltiplos y resumen | PENDIENTE | HECHA (múltiplos 26,32 · 35,46 · 44,33; CONCILIADO) |
| R5 análisis y publicación | PENDIENTE | PENDIENTE |
| R6 auditoría independiente | PENDIENTE | PENDIENTE |

Las revisiones Floyd (UBER-FLOYD-3T26, CMG-FLOYD-20261108-R1) siguen activas en el catálogo hasta que cada versión Reboot pase sus puertas.

## Decisiones tomadas
- **Arrendamientos operativos (decisión del usuario, 2026-11-10):** no se restan como deuda en los libros DCF Reboot, porque el EBIT ya deduce el alquiler. Aplica a CMG y UBER. AAPL (R3) dejó 14.368 M de arrendamientos dentro de la deuda; se corrige en R6 (efecto estimado < 1 %).
- Historias de partida: las de la revisión Floyd vigente (probabilidades 50/25/25), revisadas contra los Históricos nuevos. Parámetros Floyd: CMG Base 8,9 % / 16 % / s2c 2,7–2,9 / ROIC 22 %; Conservadora 6,4 % / 13 % / 2,2–2,4 / 15 %; Optimista 10,9 % / 18 % / 2,9–3,2 / 28 %. UBER Base 13,4 % / 18 % / 2,8–2,5 / 14 %; Conservadora 9,2 % / 13 % / 2,0–1,8 / 9 %; Optimista 15,6 % / 22 % / 3,4–3,0 / 17 %.

## Datos que faltan para R3 de UBER (los de CMG ya se resolvieron)
- Opciones y RSU/PSU vigentes de ambas empresas: el XBRL de CMG solo trae opciones hasta FY2023; hay que leerlas del 10-K FY2025 y el 10-Q 3T-2026.
- UBER: clasificar inversiones LP (participaciones en otras empresas, valores disponibles para la venta, inversiones restringidas de seguros) para caja y activos no operativos; revisar el efecto de la liberación de valuation allowance en la tasa de impuestos.
- Costo de capital: Rf 4,86 %, ERP madura 3,387 %, beta por industria de Damodaran (Restaurant/Dining para CMG; mezcla Transportation/Software para UBER) y calificación de UBER.
- Motor local de réplica: `engine.py` de AAPL requiere parametrizarse por empresa.
