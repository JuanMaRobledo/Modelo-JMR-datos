> **ESTADO VIGENTE 03-nov-2026 · R1 tras Work**: el cálculo nativo actualizado y listo para integrar es **DCF Base US$141,0085164686**, MOS35% **US$91,6555357046**, Conservador102,820990, Optimista172,892801, Disrupción71,268253. Precio de referencia **US$331,90 cierre 3-nov-2026** posterior a presentación SEC. WACC Detailed inicial**12,86221066%**, terminal**9,70%**, Ke12,994506%, ROICterminal15%. Múltiplos secundarios Base hoy**US$183,946667**, combinado secundario hoy**US$166,771407**. **Fuente única de estos números:** [hoja JMR](https://docs.google.com/spreadsheets/d/1dEycisHE5Ai34Z50ELOByAiZxub87dPG2TwOmYjS2tA/edit) y `SNAPSHOT_FINANCIERO_NATIVO.json` / `valoraciones/AAPL-20261103-A12-R1.json` en el PR. El texto posterior registra estado de fases ANTERIOR y sus cifras Base 150,04 / WACC12,48 / precio338,32 están **SUPERSEDIDAS**; no usar como valores activos de AAPL. El artículo completo actualizado consta de **14 capítulos y 9.668 palabras**, 12 apartados Nivel2, en `ANALISIS_N1_N2_CANDIDATO.json` / `analisis/AAPL-research-AAPL-20261103-A12-R1.json`. El catálogo está preparado en rama; sólo se publica tras CI aprobado y fusión del PR. Auditoría F5 independiente pendiente.

> **RESOLUCIÓN PARCIAL 03-nov-2026:** El bloqueo específico de deuda=0 y `Cost of capital worksheet!B84=PENDIENTE` documentado más abajo **ya se corrigió en la hoja AAPL**: WACC Detailed12,483033%, deuda mercado78658M, Ke12,615632%, Kd5,31%, control B84=VALIDADO. Se usó PROXY de intereses brutos2937M porque Apple no informa bruto separado. Esto no equivale a validación económica ni ejecución de 18 candados. DCF nativo Base150,042339, MOS97,527521, cuatro historias LISTO. Consultar `FASE_3_ENTREGA.md` y `FASE_4_ENTREGA.md` actuales. El texto inferior se conserva como evidencia histórica de la incidencia, no como estado actual.

# AAPL R1 — control de continuación · 3-nov-2026

## Hallazgo crítico: WACC y comparabilidad

Relectura **directa de fórmulas y resultados** en hoja https://docs.google.com/spreadsheets/d/1dEycisHE5Ai34Z50ELOByAiZxub87dPG2TwOmYjS2tA/edit :

- `Cost of capital worksheet!B12=Detailed`.
- `B22=Multibusiness(Global)` con ingresos **Productos 355.533 / Servicios 123.301** en H53:H54, y beta sin apalancar combinada `B24=1,3992145139`.
- `B25=4,91%` Treasury; `B26=Operating regions`, `B28=5,4383773437%` ERP global ponderada.
- `B61=4.916.553,86488` USD M de equity market cap (precio 338,32 × acciones14.532,259); `C61=0` deuda **NO VALORADA**, porque `B34` (método costo deuda), `B33` (vencimiento) y `B38` (costo deuda) permanecen vacíos.
- `E63=12,5194565111%` **NO es un WACC válido**: se calculó 100% equity por ausencia de deuda, aunque deuda libros y leases FY2026 = **94.479** USD M. La cifra es un valor de hoja provisional/degenerado, NO el WACC certificado.
- DCF externo en `DCF_CONTRASTE_INDEPENDIENTE.md` usó **9,45%** inicial y **9,32%** terminal como supuestos, sin enlace al `Cost of capital worksheet`. La diferencia 3,07 puntos porcentuales frente al 12,52% es **material**. No utilizar el precio Base externo 174,52 ni MOS113,44 como valoración oficial, ni compararlo directamente con precio de mercado para decisión de inversión.
- `Escenarios e historias!K5:K8` todos `PENDIENTE`, los cuatro escenarios **no se calcularon**. `Resumen de Valoración` carece de cinco múltiplos y valor objetivo.
- `Input sheet!B85=VALIDADO` para investments 80.213M no corrientes, B83=80.213 B84=80.213 y B86=Sin solapamiento, pero la documentación misma admite auditoría pendiente sobre rendimientos, impuestos y restricciones. **Control formal de hoja ≠ auditoría económica**.
- `Input sheet!B92=PENDIENTE` porque falta nota fiscal B91 (no rellenar con certeza no demostrada).
- La hoja conserva **46 pestañas** y no se ha tocado `catalogo.json` ni `valoraciones/`.

## Secuencia obligatoria siguiente

1. Obtener **desde SEC y notas de deuda** interés de deuda y vencimiento medio ponderado, rating real o synthetic, valor mercado deuda y bridge ASC842, y escoger `B34` en Cost of capital con evidencia. El resultado debe tener deuda positiva y Ke/Kd calculados; recalcular beta apalancada y WACC nativo.
2. Auditar mezcla beta sectorial (computers/peripherals y software), ERP por regiones y Treasury con corte común, comprobar que 12,52% no se confunda con WACC correcto.
3. Fiscalidad: anotar `Input!B91` con fuente SEC y puente tasa efectiva 16,995% → marginal estadounidense21% o marginal mundial defendible. No introducir nota vaga.
4. Completar stock options vs RSU y NOL con SEC; dilución de capital y valores no operativos, clasificación de caja.
5. Recalibrar escenarios en `Escenarios e historias` y `Input` **con WACC real**, comprobar 3 matrices 5×5 y valores nativos, cinco múltiplos FY+1/2/3.
6. F2 diez años y tests de estados; F3 juicios económicos y 18 candados; F4 publicación EN_REVISION solo con controles aprobados, prueba de ficha Vercel. F5 auditoría posterior.

## Estado de salida

**CANDIDATO**. El PR #241 debe permanecer DRAFT; la ficha NO se publicó. Hallazgo económico relevante identificado, no corregido sin datos fuente suficientes. No afirmar CI verde ni validación de producción.
