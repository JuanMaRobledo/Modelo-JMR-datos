# Revisión de que no fallen las valoraciones · 1-nov-2026 (tras fusionar #221, #154, #182 y #183)

Solo lectura. 21 valoraciones activas del catálogo (`main` = `feaeb27`).

| Control | Resultado |
|---|---|
| DCF Base de la hoja = JSON publicado | 21/21 (XP en `XP FCFE!B64`, motor FCFE) |
| Escenarios de `Escenarios e historias!H5:H8` = historias del JSON | 20/20 FCFF sin diferencias (DUOL con `escenariosDCF`, coincide al centavo) |
| MOS = Base × 0,65 | 21/21 |
| Compuertas `K5:K8` LISTO, `B85`, `B108`, `B84` VALIDADO | 20/20 FCFF (XP: excepción FCFE documentada) |
| Celdas con error en pestañas clave | 0, salvo `Input sheet!N26:N28,N32` = `#N/A` en MELI y XP (referencia sectorial; industria `B9:B10` vacía; ninguna fórmula las usa) |
| App local (código `main` `c0504c8`, datos de `main`) | Portada con 21 empresas; INTU fuera; Base y MOS visibles = JSON en las 21 fichas; sin errores JS |
| CI de `main` en los tres repositorios | En verde tras las fusiones |

Pendientes no bloqueantes: industria vacía en MELI y XP; puerta técnica de META/NVDA
(`docs/PUERTA_TECNICA_META_NVDA_20261101.md`); prueba visual en producción (Vercel exige sesión).
Corrección: la nota de conciliación de XP citaba `B65`; el valor FCFE está en `B64` (`B65` es el precio con MOS).
