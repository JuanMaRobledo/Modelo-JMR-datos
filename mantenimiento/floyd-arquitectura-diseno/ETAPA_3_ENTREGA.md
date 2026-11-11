# Etapa 3 · Prototipo y diseño visual JMR — ENTREGA

**Estado: PARCIAL.** Hoja `Presentación`: prototipo construido y verificado visualmente (PDF → imagen) en copia aislada. App/expediente: **NO_EJECUTADO** (acceso con usuario/contraseña; no se evita la autenticación). 2026‑11‑11.

## Qué se hizo
| Elemento | Tipo | Evidencia |
|---|---|---|
| Prototipo `Presentación` en copia aislada de D‑B de UBER | **cambio efectuado + verificado** | `PROTOTIPO E3 · UBER-REBOOT-3T26-R1 · DCF BASE · Presentación JMR` — `15P2WOocyh5d12s1dQz4-zO1Rxl80a327Ib4drkkT480` (carpeta `02 Pruebas y desarrollo`) |
| Antes / después | efectuado | `etapa3/presentacion_ANTES.png`, `etapa3/presentacion_DESPUES.png` |
| Contraste de la paleta (WCAG) | medido | tabla abajo |
| Revisión del código de `expediente.html`, `visor.html`, temas CSS | leído | hallazgos abajo |
| Capturas de la ficha en escritorio y móvil | **NO_EJECUTADO** | `expediente.html` muestra «Acceso» (usuario/contraseña); captura solo de esa pantalla (`app_acceso_desktop.png`) |
| Referencia visual `JMR / FLOYD — Presentación` y AZ Stocks | **no accedida** | la imagen adjunta no está disponible en esta sesión (solo llegó el `.md`) y AZ Stocks no se consultó; el diseño sigue §6.1 del prompt. No se trasladó ninguna cifra ilustrativa. |

## Diseño de `Presentación` (siete bloques, una página)
Cabecera `JMR / FLOYD` (empresa, ticker, fecha de mercado, moneda, revisión, estado) → 1 valor principal (DCF Base, precio, precio con MOS 35 %, upside +44,0 % con ubicación del precio) → 2 tres escenarios (valor, upside, probabilidad, aportación, WACC; Base resaltada como ancla; esperado ponderado aparte; N/D si las probabilidades no suman 100 %) → 3 matriz 5×5 WACC × g con celda Base resaltada y control de centro → 4 drivers (WACC inicial/terminal, g, ROIC terminal, VP VT / VP total, crecimiento, CAGR, margen objetivo, ventas/capital) → 5 cinco múltiplos (peso, tres escenarios, base vs. precio, combinado) → 6 integridad (revisión, estado, sincronización, conciliación, SHA‑256, control de sensibilidades, enlaces a H, D‑C, D‑O, M, A).
- **Solo fórmulas** (ningún número escrito en la hoja). Verificado contra D‑B original: 98,74 / 68,59 / 64,18 / 98,11 / 70,31 / 71,44 / matriz B (centro 98,74) idénticos; el motor sigue calculando 98,74 en la copia.
- Para no introducir entradas en `Presentación`, los metadatos (ticker, revisión, estado, fecha del precio, última sincronización, 5 URL) van como **entradas amarillas en `Resumen de valoraciones!A52:B63`** (cargadas por script con huella). **Implicación:** la plantilla 02b necesitará esas filas (Etapa 7).
- Corregidos en el prototipo los hallazgos E1‑4 y parte de E1‑7: ya no existe texto estático contradictorio (el pie se deriva de `Estado`); aparecen drivers, matriz, procedencia y fecha de mercado.
- Sin imágenes ni logotipos incrustados; gridlines ocultas; formatos numéricos con alineación a la derecha, negativos en rojo y positivos en verde (reglas condicionales).

## Contraste (WCAG 2.x)
| Par | Ratio | AA texto normal (4,5) |
|---|---|---|
| Tinta `#16231F` / blanco | 16,2 | sí |
| Texto suave `#51615A` / blanco · / `#F5F6F2` | 6,6 · 6,0 | sí |
| Positivo `#1E7F52` / blanco | 5,0 | sí |
| Negativo `#B0452F` / blanco | 5,6 | sí |
| Dorado cabecera `#D6AB4B` / tinta | 7,6 | sí |
| Dorado del prompt `#A6791F` / `#F5F6F2` · / blanco | 3,6 · 3,9 | **no** (solo texto grande) → sustituido |
| **Dorado de texto adoptado `#8A6414`** / `#F5F6F2` · blanco | 4,9 · 5,4 | sí |
| Blanco / celda Base `#8A6414` | 5,4 | sí |
| **App · botón «Entrar» `#3730A3` sobre `#4F46E5`** | **1,58** | **no (defecto de la app)** |

## Hallazgos de la app (código real, no supuestos)
1. **Dos identidades visuales:** `visor.html` define inline los tokens JMR (`--bg:#F5F6F2; --ink:#16231F; --ink-soft:#51615A…`), pero `expediente.html` carga `jmr-theme.css` con otra paleta (`--bg:#f8fafc; --accent:#4f46e5` índigo/pizarra). El prompt supone tokens JMR en la app: solo se cumple en el visor. Unificar es una decisión de diseño que **no se ha ejecutado** (no se reescribe el tema sin verificación visual).
2. **Ya existe** un componente compartido de cabecera de valor (`jmr-mos-summary.css`: tres precios, comparaciones, `.jmr-mos-scenarios`) y siete pestañas en el expediente (`analisis, valoracion, financieros, indicadores, modelo, sensibilidades, revision`). Los objetivos «precio, DCF Base, MOS, upside, escenarios visibles» no requieren un componente nuevo; hay que **verificar** su estado con sesión.
3. Contraste insuficiente del botón de acceso (1,58:1).
4. `expediente.js` lee `raw.githubusercontent.com/…/main/catalogo.json`; fuera de línea o sin permisos la ficha no abre (comportamiento esperado, declarado en su mensaje de estado).

## No realizado (y por qué)
- Capturas desktop/móvil de la ficha, comprobación de desbordes y alineación en móvil, y la matriz 5×5 compacta móvil en la app: requieren sesión autenticada. **Se necesita que el usuario proporcione una sesión de solo lectura o capturas.**
- Cambios en `docs/*.html|css|js`: ninguno (no hay forma de verificarlos visualmente aquí).
- «Descuento de múltiplos»/formatos de H, M y de las 17 hojas del motor: sin cambios.
- La hoja se muestra en una sola densidad; impresión a una página comprobada en PDF; no se probó en móvil de Google Sheets.

## Siguiente paso
Etapa 4: sincronización y recálculo con prueba obligatoria (modificar una entrada, sincronizar, comprobar dependientes y no dependientes, restaurar) en copias de UBER.
