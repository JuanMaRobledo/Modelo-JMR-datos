# CMG · continuación del reinicio
Revisión: CMG-2026-10-28-R1-REINICIO. Rama exclusiva: ccr-e19723cb-q1m72p.

**PREPARACION. No publicado. Auditoría económica PENDIENTE; no es dictamen ni manifiesto certificado.**

Hoja: https://docs.google.com/spreadsheets/d/1SF3cYhIe01LazAiW4klGgYd6QrYG_uC-X-A8N5yYETc/edit

## Resultado actual
DCF Base24,9369270995; Conservadora11,0615407413; Optimista32,2273851892; Disrupción3,7174385572 US$/acción. Esperado ordinario23,2906950324; MOS35%soloBase16,2090026147. Precio31,95 cierre30-sep-2026. Inverso14,3573%uniforme1–5 con margen17%.

## Trabajo guardado
- Correcciones split/accionesLTM, impuestos exactos, fórmulas originales, entradas y cuatro historias; cero datos de valoraciones antiguas CMG reutilizados.
- scripts/cmg_entradas.py reproduce210entradas con preflight de fórmulas; scripts/cmg_contenido.py reproduce172textos/estadísticas.
- Narrativa/fuentes propias y decisiones de moat, ciclo y siete múltiplos en reference.
- Artículo BORRADOR de18secciones y Nivel2con estados completos, ratios, insumos, cuatroDCF, siete métodos y matrices: JMR-valuation/data/CMG_Research_Fundamental_Modelo_JMR_2026-10-28.md y CMG_Nivel2_Calculos_2026-10-28.md.
- analisis-borrador.json contiene articleHtml y calculationHtml del borrador, analysisSchema requerido y publicación PREPARACION. **No está activo en analisis/ ni en catálogo; linkedValuation pendiente.**
- Modelo-JMR/tests/cmg_reinicio_smoke.py preparado: falla antes de abrir navegador si no hay registro/catálogo CMGúnico. Intercepta GitHub a datos locales, bloquea escrituras, prueba ficha/lector/visor. NO EJECUTADO.

## Controles que sí ocurrieron
Comparación61pestañas:21.265fórmulas originales,0diferencias (excepto precioC25 solicitado),122validaciones preservadas. 66identidades contables,0fallos a0,005US$M. Cuatrohistorias idénticas al motor nativo JS a precisión numérica. TrescentrosDCF y siete centros relativosBase concilian. Las172escrituras posteriores preflight0conflictos con fórmulas.36fórmulas temporales para promedios se leyeron y se retiraron.

MatrizDCFde tasa: desplaza inicial yterminal juntos. No afirmar que varía exclusivamente el terminal. Se probó motor con −1pp:32,8254358735, igual a hoja. Tasasbase delrepo: IPC2015/ago2026 contrastados con BLS; media/mediana yfracciones son referencias multisectoriales con interpolación, no probabilidades CMG.

## Bloqueo demostrado
exec_command("pwd") devolvió: "No usable execution environment is available. Wait for an environment to become available before using this tool."
No hay Python/Chromium/Playwright utilizables; conectores de Sheets/GitHub y V8 sí funcionaron. No simular exportación ni pruebas.

## Orden de continuación
1. Clonar/actualizar tresrepos a ccr-e19723cb-q1m72p; leer reglas/prompts vigentes. No PR, no main.
2. Ejecutar controles oficiales y verificación editorial. No se localizó unificacion_hojas.py en fuente ni auditar_profundidad.py en Modelo-JMR-datos/scripts; localizar antes de afirmar corrida.
3. Completar inventario agregado8-Kal corte (fuentes individuales julio/agosto/septiembre ya consultadas). Revisar borrador18secciones ylímites reales; no entregar como artículo final hasta pasar mínimos oficiales.
4. Conciliar requisito sensibilidad exclusivamente terminal con conservación de plantilla; no sobrescribir fórmulas originales. Siete matrices relativasBase ya concilian.
5. Exportar usando sistema existente, registrar CMG, implied_growth/sync/normalización/migración/contrato; preparar JSONde valoración yvincular analisis-borrador al resultado exportado.
6. Publicar EN_REVISION en rama autorizada, validationStatus PENDIENTE_AUDITORIA_ECONOMICA, authorization citando petición. Catalogar solo registro coherente. Gate exige certificado: no fabricarlo; documentar salvedad si se omite con alcance explícito.
7. Ejecutar prueba local preparada yguardar capturas/resultados. Appreal lee main: no decir publicación comprobada en producción.
8. Mantener auditoría económica diferida hasta revisión visual. No audit_report.py. Solo al estar listo solicitar autorización para fusionar a main.

## Salvedades económicas pendientes de revisión
Kd5,48% yvolatilidad35,2%son proxies reportadas; RSU/PSUreclamo separado enB21, accionescomunesdenominador; privadas a valor libro; contratosleases sin iniciar ycalendarioFY25vsjunio26; fórmulas mecánicas originales deFinancialsMultiples preservadas. No son dictamen de materialidad.

8-K5-ago: guía29-jul **no incluía** posible impacto financiero de investigación sanitaria. No afirmar "impacto cero". La Base asume ausencia de daño duradero como juicio sujeto a contraste.

## Eliminación y preservación
No se eliminaron archivos adicionales en esta continuación. El contexto del usuario informa purga previa de ramas actuales y51elementosDrive a papelera; no se revalidó ni se declara definitiva. HistorialGit/papeleraDrive pueden conservar copias; casos de estudio, bitácora, screener, compras ydatos de mercado/pares legítimos se preservan. Carpeta personalDrive14qnWfkDeJezc_-RdaE3n7ADdhMlosYQQintacta; requiere autorización específica para borrarla.

## Commits
Fuente final: 0d1c658f00cd5117c0680ac70bce14c749bafcf9
App (prueba preparada): 50374bfc99c3f49d45fab33f07ed7d92867a97f3
Los commits llevan Co-Authored-By: OpenAI Codex <noreply@openai.com>.
