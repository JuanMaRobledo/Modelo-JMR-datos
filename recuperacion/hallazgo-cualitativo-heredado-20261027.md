# Depuración editorial de Cualitativo · 27-oct-2026

**Ámbito:** 16 valoraciones activas del `catalogo.json`; análisis mediante lectura de la propiedad `hojas.analisis.Cualitativo` de cada JSON de valoración. Resultado: **12 de 16** conservan rótulos específicos de un caso externo heredado de la plantilla (Topaz Labs, acuerdo Disney, Digital Experience, segmentos Digital Media/Publishing y otra fecha Morningstar).

**Afectadas:** NFLX, ADBE, BSX, DUOL, MSFT, NVO, ONON, PYPL, EPAM, SHAK y UBER. **Sin esos rótulos en el campo consultado:** NKE, META, NVDA y XP (en NKE/META/NVDA la pestaña no está publicada en ese campo; por tanto no se afirma que haya sido auditada fuera de él).

**Causa comprobada:** las tres plantillas oficiales Maestra, IA y Manual del 22-oct contienen idénticos rótulos en la pestaña `Cualitativo` (p. ej. A13:A15, A24, A29:A30, A32, A35, A42:A43, A47:A50). El problema estaba en el origen editorial, no en DCF, proyecciones, Financials Multiples o ajustes del capital.

**Contención aplicada en la app:** [Modelo-JMR PR #116](https://github.com/JuanMaRobledo/Modelo-JMR/pull/116) fusionado, tras tres comprobaciones CI verdes. El anexo `Cualitativo` importado con Topaz/Disney no se muestra como investigación del emisor; aparece una advertencia que remite al análisis fundamental auténtico y a la hoja original. También se corrigió la apertura de tablas del visor de anexos. **Esto no edita los JSON originales ni las Google Sheets**.

**Remediación estructural de plantillas:** copias de seguridad realizadas en carpeta de plantillas no vigentes:
- Maestra: `11zFwKSamBLxOzSe2l3M6i72RQLDapbhcqWsBGcqvSQo`
- IA: `13SSnPVG6ULtHsxgsgNfC_4-dg30GjiAxH9_JrdkresU`
- Manual: `1VJDzv26ccK1x_yPNSSfZBCOVk5kceK92ux98Gdy6C7g`

El script de corrección propuesto (solo 14 etiquetas editoriales) está en `JMR-valuation/scripts/limpiar_cualitativo_plantillas.py` (rama audit/certificacion-tres-plantillas-20261027). Exige doble guarda: coincidencia exacta de los textos originales y variable `JMR_EDITAR_MAESTRA=1` al aplicar. No puede alterar fórmulas ni validaciones. **No declarar aplicada la limpieza hasta ejecutar su escritura y verificarla.**

**Regla de calidad futura:** ninguna etiqueta fija, texto de fuente, ejemplo de noticias ni dato de otra compañía debe aparecer en una plantilla reutilizable. Las futuras copias deben salir de plantillas limpias, sin borrar ni sobreescribir expedientes históricos; la hoja cualitativa debe poblarse con hechos específicos, referencias, fecha de consulta, ventajas competitivas, bull/bear y gobierno corporativo del emisor.

**Estado financiero:** los 16 registros publicados y sus DCF no cambian. Este hallazgo afecta fidelidad editorial en anexos, no demuestra un error numérico en las valoraciones. Continúan las salvedades económicas documentadas por ticker.
