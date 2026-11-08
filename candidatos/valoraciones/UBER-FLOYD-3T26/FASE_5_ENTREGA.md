# F5 · UBER · Modelo JMR Floyd · 3T-2026 — entrega

**Fecha:** 2026-11-08 · **Estado:** auditoría NO INDEPENDIENTE · **Dictamen: PENDIENTE**
**Libro auditado:** `1jMzDqRnTiBdbeFJmB0UH4aLdthBtC1JtiRhl8PEQBcg` (candidato; no publicado)
**Auditoría (Google Sheets independiente):** `1mKz3qxQViXjst_j4cdhNDZhDVF4IOPNcWc4MVqtBFZ0`, en AAA Finanzas/Análisis/UBER.

## Independencia
La misma conversación construyó el libro y lo auditó; solo cambió el modelo (Sonnet 5.5 frente a Opus 5.5). La regla F5 pide otro modelo o sesión nueva, así que no se emite dictamen independiente.

## Por qué PENDIENTE
1. Sin revisor independiente.
2. No existen F2, F3 ni F4: el libro es CANDIDATO, sin artículo, JSON ni app.
3. «Historias → números» marca «PENDIENTE: 13 faltantes» en las tres historias.
4. Múltiplos sin cargar (pesos 0 %).

## Pruebas aprobadas
- Recálculo independiente de los tres bloques: Base 101,1423, Conservadora 49,5876, Optimista 146,0359 (diferencia 0,0).
- LTM al 3T-2026 conciliado con el 10-Q y XBRL; balance, resultados y flujo de caja cuadran.
- Rf 4,94 % y prima madura 3,387 % coinciden con ERPNov26. Huella de fórmulas 0/1.883.

## Hallazgos (detalle en el Sheets de auditoría)
Bloqueantes: F5-01 (historias → números), F5-02 (independencia).
Altas: F5-03 (la justificación del margen Base dice que el gasto corporativo baja a ~5 %, pero el 10-Q lo muestra subiendo de 7,4 % a 7,7 % de los ingresos), F5-04 (valor terminal y ROIC terminal).
Medias: F5-05 (múltiplos), F5-06 (NOL no actualizado), F5-12 (Delivery Hero).
Bajas: F5-07 a F5-11, F5-13 y F5-14.

Lectura económica: el precio de 68,59 equivale a margen 14 % con crecimiento ≈ 9-10 % anual, o a margen 18 % con crecimiento ≈ 3 %. La palanca decisiva es el margen (±2 pp = ±11,8 por acción).

## Cambios
Ninguno en el libro auditado. Las sensibilidades se corrieron en una réplica (`JMR-valuation/reference/modelo_floyd_2026-11-08/uber_3t26/f5_audit/`).

## Pendientes
Corregir F5-01, F5-03, F5-05 y F5-12; ejecutar F2-F4; repetir F5 con revisor independiente. Al promover Floyd, mover la A-1.2 a «Revisiones sustituidas» (REGLAS §10).
