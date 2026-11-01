# Estado de la organización del Modelo JMR · 1-nov-2026 (verificado en esta sesión)

Verificado hoy contra GitHub, Drive (cuenta de servicio y conector) y `catalogo.json`. «Verificado» = leído de la fuente en esta sesión.

| Bloque | Estado | Evidencia | Pendiente |
|---|---|---|---|
| GitHub y PR | confirmado | Modelo-JMR-datos #211, #215–#220 cerrados con fecha de fusión; `main`=`6b9252b`, 3 workflows en success (runs 41297451000/…009/…052). Modelo-JMR #151–#153 fusionados; `main`=`c1b4e6d`, CI en success. JMR-valuation #181 fusionado | JMR-valuation: #179 y #180 (SHAK, borrador) siguen abiertos |
| Catálogo (23) | confirmado | 23 valoraciones, 23 análisis, 23 tickers únicos, todos A-1.2 / EN_REVISION | `controlModeloA.estado` = INCOMPLETA_EN_REVISION en los 23 (auditoría económica pendiente) |
| Drive: hojas vigentes | confirmado | Las 23 hojas del catálogo están en `Análisis/<TICKER>/` (padre verificado por ID) | Subcarpetas ajenas en Análisis: `BVC`, `Nueva carpeta (2)` (vacía), no tocadas |
| Drive: Archivo | parcial | `Archivo/` tiene ADBE(8), CMG(28 archivos de datos), META(1), NFLX(4), NKE(1), NVDA(1), UBER(1) | No hay carpeta de archivo para los otros 16 tickers: no se ha movido ni creado nada sin evidencia de versiones anteriores |
| Hojas: pestañas | confirmado | 12 hojas con 46; 11 con otro número (manifiesto en `evidencia/manifiesto-pestanas-20261101/`). Ninguna carece de pestañas de la plantilla; los extras solo se añaden | No se eliminó ni ocultó nada; falta mapear dependencias por fórmula |
| App / Vercel | bloqueado | `modelo-jmr.vercel.app` responde 401 sin sesión en `/`, `expediente.html`, `visor.html` | Prueba visual y commit desplegado: necesita sesión del propietario |
| Calidad económica | parcial | ver `docs/RECONCILIACION_HOJA_JSON_23_20261101.md` | INTU y NU sin DCF nativo; UBER/GOOGL con anclas ligadas al precio; XP con motor FCFE (compuertas estándar PENDIENTE) |

## Nota sobre UBER
El documento de relevo cita como hoja oficial `1T2GB36H…` (61 pestañas, B35 = 73,27, precio 68,51, «EN PREPARACION»). El catálogo apunta a `1i0B9cPX…` (46 pestañas, B35 = 91,14 = JSON, precio 65,74). La primera está en `Archivo/UBER`; la segunda en `Análisis/UBER`. Prevalece el catálogo.

## Bloqueo de permisos
La carpeta `Análisis` tiene «cualquier persona con el enlace: editor»; las 23 hojas lo heredan, incluidas XP y CELH, que antes eran solo del propietario. Quitarlo no se puede hacer con las herramientas de esta sesión; hay que hacerlo en Drive (Compartir → Acceso general → Restringido). La cuenta de servicio `jmr-valuation-bot` ya tiene permiso de editor directo sobre la carpeta.
