# Actualización de análisis fundamentales — índice canónico de META (30-oct-2026)

## Alcance verificado

Catálogo activo al 29-oct-2026: **23** análisis. Se preserva su vínculo con la valoración
publicada y la revisión original. No hay recálculo financiero ni auditoría económica.

**Cinco documentos con los 18 títulos originales ya vigentes:** META, NVDA, XP, SHAK, UBER.
No se reescriben para evitar degradar su contenido.

**Catorce documentos reorganizados en este PR:** DUOL, MELI, CELH, ADBE, BSX, CMG,
NFLX, GOOGL, MSFT, NKE, PYPL, EPAM, NVO, INTU.
Cada uno ahora presenta en `articleHtml` los 18 capítulos canónicos, conservando
los apartados originales como subsecciones `h3`. Se dejaron explícitas como
pendientes las secciones sin material suficiente; no equivalen a artículos terminados.
`editorialMigration.missingCanonicalSections` registra esas carencias.

**Cuatro documentos sin sustitución del JSON:** ZTS, ONON, NU, AFYA.
No se consiguió actualizar esos archivos con las herramientas disponibles en esta
operación. Permanecen intactos. La aplicación, tras la fusión de
`Modelo-JMR` PR #140, ofrece una **reorganización solo de lectura** para artículos
legados que aún no cumplen el esquema. Esto no es migración ni certificación
editorial del archivo original.

## Validaciones ejecutadas

- De los 14 archivos sustituidos se compararon los párrafos HTML originales con
  la versión nueva: **0 párrafos perdidos** en cada uno.
- Ninguno de los campos ajenos a `html`, `articleHtml`,
  `calculationHtml` y `editorialMigration` fue alterado.
- Los cálculos preexistentes en `calculationHtml` permanecieron iguales en los
  14 archivos comprobados.
- Se verificaron los 18 títulos canónicos en los 14 documentos migrados.
- La adaptación de lectura en la app no reescribe las fichas de origen.
- Ni la presencia de los 18 títulos ni el control anterior de `research.js`
  acreditan calidad de fuentes, profundidad, noticias o análisis económico.

## Próxima fase editorial obligatoria

**No confundir reordenación con finalización del análisis.** Falta completar
con información específica del emisor los capítulos marcados como
`Pendiente de ampliación editorial`, al menos: discusión bull/bear,
filosofías de inversión, noticias fechadas, fuentes documentadas y señales
de vigilancia para numerosos emisores. Revisar coherencia económica,
correspondencia con su valoración oficial y exhaustividad de las 18 secciones
antes de cambiar el estado a análisis editorial completo.

La auditoría económica continúa separada y solo se inicia después de la
revisión visual y de que sea solicitada. La presente migración no cambia
el estado financiero `EN_REVISION` ni sustituye dictámenes previos.
