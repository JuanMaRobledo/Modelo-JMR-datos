# Propuesta técnica — Floyd híbrido Commerce + Fintech + SOTP (NO INTEGRADA)
**Corte de diseño:** 2026-11-09. **Caso de validación:** MELI-FLOYD-3T26-R1. **Fuente de autoridad:** `Modelo-JMR/modelo/REGLAS_VIGENTES.md` v34, `docs/CONTRATO_EJECUCION_FLOYD.md`, `docs/prompts/ordenes-floyd.md`. El documento es propuesta y NO modifica ni invalida esos contratos; exige implementación y PR de aplicación/validadores.

## Problema encontrado verificablemente
El contrato de publicación en app para Floyd lleva `contratoLibros=floyd-h1-h2-separados-v1`, un H1 y un H2. Para una empresa con negocio operativo + plataforma de pagos asset-light + créditos con capital, hay **un H1 consolidado, dos H2 de valoración por economía separada (Commerce y Fintech) y un libro de síntesis patrimonial SOTP**. La ficha estándar no sabe resolver tres H2, y su validador espera un único Simple Ginzu. El motor original preserva 1.883 fórmulas pero no valora credit-only sin FCFE. NO se debe publicar un JSON que apunte solo al H2 SOTP y oculte de dónde vienen los historiales/DCF, o que trate crédito como deuda industrial.

## Arquitectura de cuatro libros y un documento
1. `historicos`: H1 único con series hasta 10 FY+LTM, estado y relaciones legales de segmentos, SEC/NIIF y referencias con fuente; conservar notas de transferencias de caja y fondeo.
2. `commerce`: H2A con Simple Ginzu FCFF ORIGINALES, 3 historias + I+D, leases, option value, 5 múltiplos operativos aplicables, WACC por moneda y distribución geográfica; traspaso H1→H2A unidireccional y rastreado.
3. `fintech`: H2B con FCFF pagos/adquirencia *operativa*, separando intereses financieros y fees que ya se incluyen en Commerce, y FCFE para créditos con NI neta de pérdidas y fondeo y capital incremental regulatorio/económico; distinguir activos/pasivos de clientes y intercompany; tres historias y múltiplos de equity P/E/P/FCFE, P/BV cuando aplicable. El uso de `fcfebankvaluation.xlsx` NO es precondición: el tratamiento financiero viene de flujos y capital, no de una etiqueta de banco.
4. `sotp`: H2C modelo JMR de integración que **lee resultados por fórmula** directamente de H2A y H2B, a igual corte, no snapshots. Suma EV operativos y equity de créditos; resta deuda holding y obligaciones UNA sola vez; añade solo caja transferible y ajusta RSUs, opciones y no operativos con evidencias; 3 historias y MOS35% del Base. Sensibilidades independientes 5×5 centrales = DCF Base, múltiplos en la unidad correcta.
5. `analisis`: documento N1 (14 capítulos) y N2 (12 apartados), con cifras, links de celda y fuentes de ambos H2 y SOTP; F5 por sesión distinta.

## Fases obligatorias
F1: ID/ticker/corte, detectar unidad mixta y registrar excepción `FLOYD_HIBRIDO_SOTP` sin transformar crédito en negocio operativo. Definir mapa de ingresos atribuibles a Commerce, fee processing, crédito y otrosFin; gobierno de cash/float.
F2: H1 → H2A/H2B. Las cargas de historia han de ser **traspasos unidireccionales materializados** que conservan fórmulas del motor, sin usar `IMPORTRANGE` para sustituir series históricas. Validar estados y perimetraje (gastos corporativos, financiera, eliminaciones), EBIT grupo, liquidez legal por entidad, provisiones y RWA real; no llenar ausencias con 0. Reportar por libro `Huella motor`, flags y fechas.
F3: historias con diferentes g, margen, ROIC, capital y WACC/Ke por actividad; mantener g∞≤Rf y WACC/Ke>g∞. Calcular cada H2 en su motor y evaluar valores; reportar porcentaje terminal EV, ROE frente a Ke y score provisión/capital. Calcular SOTP con ajustes una vez; controles fórmulas motor, perimetraje ingreso/EBIT y matriz de múltiplos en cada bloque.
F4: serialización única del SOTP con fuentes completas y componentes por negocio, con vínculos back to H2A/H2B y H1. Ejecutar validación `hojas→JSON→visor`, 7 pestañas, lectura H1 por estados y los H2 por valoraciones; publicar `EN_REVISION` solo si compuertas económicas y técnicas APROBADAS y hay rollback.
F5: revisor independiente comprueba por libro y SOTP estados, caja, capital, NI, microeconomía y true peers, terminal y matemáticas; no autocertificar desde F3/F4.

## Propuesta de contrato JSON, NO VIGENTE
```json
{
  "ticker": "MELI",
  "revisionId": "MELI-FLOYD-3T26-R1",
  "perfil_valoracion": "Floyd",
  "contratoLibros": "floyd-h1-multi-h2-sotp-v1",
  "libros": {
    "historicos": "ID H1 real",
    "valoracion": "ID H2C SOTP real, compatibilidad visual",
    "commerce": "ID H2A real",
    "fintech": "ID H2B real",
    "sotp": "ID H2C real",
    "analisis": "ID Doc real"
  },
  "resultadoPrincipal": "sotp.valor_base",
  "estado": "CANDIDATO"
}
```
Solo promover este esquema cuando extractores, validadores y app implementen lectura, muestra, conciliación y casos legado SIN regresiones. **Nunca dejar que la publicación tome el EV Commerce y lo llame valor patrimonial de MELI, ni sumar EBITDA crédito como industrial**.

## Controles de aceptación a implementar
- H1 un único FY/LTM y fecha de precio, correctos 2016–2025; H2A/H2B/H2C distintos, H2C Presentación única para ficha MELI; historial fuentes en ambos H2 materializado.
- `revenue_consolidado - SUM(revenue_actividades)=0` con intercompany asignado; EBIT/NI por negocio + corporate conciliados contra grupo, sin parear NI aftertax con EBIT no ajustado.
- Terminal FCFF con g/ROIC; FCFE crédito reinversión MAX(ΔNI/ROE, Δcartera×capital), antes de fondos cliente; ROE terminal versus Ke.
- Deducción deuda holding vs financiación cartera sin doble conteo y cash legal transferible; LTRP cash-settled versus RSU opciones por no duplicar gastos y dilución.
- 3 escenarios y probabilidad total1, fracaso solo Conservadora; MOS35% del Base; matrices5×5 centros exactamente Base, sin errores Sheets.
- Múltiplos aplicables (5 prioridades por unidad, N/A o N/D escrito); pares fechados, P/BV crediticio solo con book equity legal conciliado; precio normalizado y split.
- `ESTADOS`: CANDIDATO hasta pasar gates; EN_REVISION solo si CI/visores y fuentes económicas pasan; F5 después por auditor separado. Tests automáticos nuevos para modelos mixtos, verificación regresión UBER/CMG Floyd legados.

## Situación MELI
Hay una valoración condicional de 4 motores en H2C Base US$1.115,04/acc, MOS35 US$724,78, con resultados de hoja que recalculan, pero **Ginzu original sigue 0/3 LISTO**, fuente de NI/fees/RWA/cash grupo no auditada, precios pares no homogéneos y JSON/app no adaptados. El estado `CANDIDATO` es correcto; este documento no certifica una ejecución o publicación futuras.
