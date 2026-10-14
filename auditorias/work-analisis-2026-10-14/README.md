# Actualización de análisis JMR · 14 de octubre de 2026

Se actualizaron las vistas Nivel 1 y Nivel 2 de los 39 análisis vigentes. Se conserva íntegro el HTML fuente anterior y su historial Git. No se cambiaron estados financieros, hipótesis ni registros de valoración.

## Comprobaciones

- 39 artículos con las 18 secciones acordadas y referencias internas comprobadas.
- 35 modelos reproducidos contra las hojas con tolerancia máxima de 0,001 por acción; 105 matrices de sensibilidad, con centro idéntico al Base de la hoja.
- 32 inversos con precio fijo reconstruido y error menor a 0,001. PAGS, GRUPOSURA y PFGRUPSURA no encontraron raíz modificando solo crecimiento; se explica la limitación y no se fuerza una respuesta.
- Se preservaron trayectorias propias y la reinversión explícita de MU; las financieras usan FCFE/Ke.
- La prueba existente de carga de informes de la aplicación pasa; seis pruebas de navegación a cálculos y desplegables también pasan. No se certifica apariencia ni exportación PDF de producción.

## Diferencias entre la hoja y el registro publicado

| Empresa | DCF Base guardado | DCF Base de hoja leída |
|---|---:|---:|
| AAPL | USD 147,748684 | USD 150,131950 |
| DUOL | USD 107,462981 | USD 103,538395 |
| MP | USD 0,284820 | USD 0,260424 |
| PYPL | USD 119,698374 | USD 100,098304 |

Estas revisiones se identifican como pendientes en los artículos. Las nuevas matrices describen el modelo de la hoja, no la tarjeta anterior. No se publicó una valoración nueva ni se certificaron sus fuentes por este cambio editorial.

## Casos con pendientes específicos

- Grupo Argos ordinaria/preferencial: SOTP preliminar, pendientes previos conservados; DCF consolidado retirado no restaurado.
- Grupo SURA ordinaria/preferencial: FCFE vigente reproducido, sin declararlo equivalente a SOTP; necesita contraste por participaciones.
- NU: comprobar método FCFE y capital regulatorio; no certificar sensibilidad industrial para un banco.
- PFDAVIGRP.CL: falta una hoja y registro enlazado verificable en el análisis. No se combina con PFDAVVNDA.
- MP: preferente convertible y elección económica por historia necesitan certificación independiente.

## Reproducibilidad

Ejecutar `node reproduce.cjs` desde esta carpeta. `snapshot-inputs.json` registra las lecturas acotadas de Sheets del 14-oct-2026; `numerical.json` contiene entradas, resultados, matrices y controles. `jmr_engine.cjs` reproduce el motor de Modelo-JMR en el commit ec9d3d2ea5396e209aac81ee1a503ad745bacdf5, con las transformaciones de sensibilidad descritas en reproduce.cjs y los anexos.

Los cálculos son condicionales al contenido y fórmulas de las hojas. Reproducirlos no constituye auditoría contable ni verificación de cada fuente externa. No se revisaron noticias posteriores al corte de cada expediente. Las nuevas matrices de esta edición están en los anexos de la aplicación; su escritura a pestañas de Sheets y la sincronización de todos los Google Docs siguen pendientes.

## Publicación

La aplicación consume `analisis/*.json` de Modelo-JMR-datos en tiempo de ejecución; guardar esos archivos no requiere desplegar nuevo código del visor. El commit de código vigente tiene estado Vercel success, pero el acceso directo a producción devuelve 401 y el conector Vercel devolvió 403. La verificación visual en producción y el PDF quedan pendientes. No se modificaron controles de acceso.
