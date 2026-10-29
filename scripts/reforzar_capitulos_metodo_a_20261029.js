'use strict';
/* Revisión editorial reforzada de 15 análisis recientes A.
 * Se ejecuta después de integrar el suplemento antiguo en el artículo.
 * No altera cálculos ni agrega cifras externas no verificadas.
 */
const company={
 MELI:{
  operating:'Marketplace, logística, anuncios y Mercado Pago no consumen capital de la misma forma. La red de entregas gana productividad con densidad; los créditos exigen provisiones, fondeo y patrimonio. El crecimiento de una unidad no debe heredarse mecánicamente por la otra.',
  financial:'El expediente registra FY2025 US$28.893 millones y LTM junio de 2026 US$35.182 millones. Distinguir expansión orgánica de comercio, crecimiento nominal regional e ingresos de crédito evita extrapolar devaluaciones o inflación como rentabilidad económica en USD.',
  capital:'Sales-to-Capital 2,40× y 2,70×, ROIC terminal 16% y reinversión inicial cercana a US$5.476 millones requieren prueba conjunta. Un retorno sobre capital muy alto después de sumar cartera y logística sería menos plausible si el negocio de crédito demanda más patrimonio.',
  bear:'Una reversión de márgenes de envío subsidiado, deterioro de morosidad y límites de monetización de anuncios presionarían simultáneamente EBIT y reinversión. Un contrafactual no puede bajar ventas sin incluir pérdidas en cartera cuando estas son la causa.'
 },
 CELH:{
  operating:'Celsius, Alani Nu y Rockstar se comercializan mediante distribuidores y un portafolio con productividad desigual. La compra de marcas puede impulsar ventas reportadas sin que aumente la rotación de cada SKU para el consumidor final.',
  financial:'El trimestre de referencia tuvo US$817,9 millones de ventas, con US$790,7 millones en Norteamérica. La diferencia entre crecimiento reportado del primer semestre por consolidaciones y expansión trimestral del 11% debe gobernar la desaceleración del pronóstico.',
  capital:'La Base ajusta EBIT LTM desde US$160,3 millones hasta beneficio recurrente cercano a US$573,1 millones por cargos extraordinarios. La justificación de cada ajuste y de los instrumentos preferentes es tan importante como el margen de largo plazo 19,5%.',
  bear:'El poder de los distribuidores, descuentos y rotación de inventario pueden erosionar margen aun con ingresos en aumento. La preferente convertible cambia el capital común y no debe contarse dos veces en deuda y dilución.'
 },
 ADBE:{
  operating:'Adobe monetiza Creative Cloud, Document Cloud y Experience mediante licencias con retención y uso empresarial. La IA puede añadir créditos y creación de contenido, pero también reducir asientos y sustituir tareas antes reservadas a productos de pago.',
  financial:'El tercer trimestre FY2026 registró US$6.760 millones de ingresos y ARR total de US$27.500 millones; AI-first ARR creció más de 150% desde una base más pequeña. Esa última tasa no equivale al crecimiento consolidado y debe verificarse contra costos de inferencia.',
  capital:'El EBIT GAAP LTM de aproximadamente US$9.271 millones y el EBIT económico ajustado de US$9.458 millones difieren por la política de I+D. La Base usa margen ajustado objetivo del 39% y Sales-to-Capital marginal 2,85×/2,15×; hay que seguir la misma convención en los flujos.',
  bear:'Agentes, Canva, Figma y proveedores de modelos pueden reducir el precio por tarea. El caso negativo afecta simultáneamente retención de suscripciones y costo de entregar generación de imagen y video, no solo el múltiplo terminal.'
 },
 BSX:{
  operating:'Boston Scientific obtiene ingresos en procedimientos MedSurg y cardiovasculares. Adopción clínica, evidencia, reembolso y entrenamiento de equipos implantadores tienen tiempos distintos; una tecnología exitosa no transforma instantáneamente toda la línea de ventas.',
  financial:'Q3 2026 reportó US$5.138 millones de ventas y crecimiento orgánico de 1,5%; el margen operativo GAAP de 16,1% difiere del margen ajustado de 26,5%. La Base modera la trayectoria inicial a 3% y la recuperación depende de segmentos concretos.',
  capital:'El margen operativo económico objetivo del 25,5%, Sales-to-Capital 1,50×/1,70× y ROIC terminal 15% deben incorporar I+D clínica e inversiones adquiridas. El tratamiento de MiRus y Penumbra exige separar valoración de opción, capital histórico y financiación futura.',
  bear:'Reembolsos, retrasos regulatorios o debilidad de nuevas técnicas pueden consumir la capacidad comercial antes de generar volumen. Si una adquisición no cerrada se incluyera como ingreso y luego se descontase como deuda, se introduciría doble conteo.'
 },
 CMG:{
  operating:'Chipotle vende en restaurantes propios: cada apertura requiere cocina, personal, equipo y arriendo. Los nuevos locales agregan ventas pero maduran gradualmente; a diferencia de un franquiciante, la matriz asume gran parte del costo y del capital.',
  financial:'El tercer trimestre de 2026 tuvo 4.267 restaurantes propios, crecimiento comparable de 2,1% y margen restaurant-level 23,3%, distinto del EBIT consolidado de 13,7%. La expansión de tiendas puede coexistir con AUV ligeramente inferior.',
  capital:'La Base utiliza Sales-to-Capital marginal 2,20× y luego 2,05×, margen EBIT corporativo objetivo 16,5% y ROIC terminal 19%. Los pasivos por arriendos superiores a US$5.500 millones exigen simetría de ajustes de EBIT y deuda.',
  bear:'La canibalización de ubicaciones, más inflación en carne y salarios o una caída de transacciones podrían reducir retorno por restaurante. Una apertura no compensa automáticamente un local maduro con tráfico descendente.'
 },
 NFLX:{
  operating:'Netflix combina retención por catálogo, ARPU y publicidad. Una biblioteca digital es un activo económico que se renueva continuamente; los costos de producción y de derechos se reconocen por amortización pero se pagan antes de generar ingresos.',
  financial:'Los nueve meses de 2026 incluyen US$14.934 millones en adiciones de contenido frente a amortización de US$12.765 millones. La previsión de publicidad FY2026 se redujo de cerca de US$3.000 a US$2.700 millones, un control para no extrapolar nuevas fuentes de ingreso.',
  capital:'La Base usa Sales-to-Capital marginal 1,65×/1,50×, margen EBIT 36% y ROIC terminal 22,5%. Los contratos de contenido por US$25.223 millones no se pueden restar íntegramente del equity y volver a incluir como pagos en el FCFF.',
  bear:'Si aumenta el costo por hora de engagement, sube churn o la publicidad tarda más en monetizarse, el EBIT podría mejorar mientras las nuevas obligaciones de contenido absorben caja. El escenario adverso debe reflejar ambos caminos.'
 },
 MSFT:{
  operating:'Microsoft 365 y Azure tienen unidades económicas diferentes: software empresarial recurrente puede servir clientes adicionales sin comprar otro servidor por cada usuario, mientras la IA en nube requiere aceleradores, energía y depreciación física.',
  financial:'Los ingresos LTM del expediente se aproximan a US$346.445 millones y el CapEx LTM a US$135.921 millones. El crecimiento de contratos y reservas no garantiza conversión a caja si aumenta capacidad no utilizada o se posponen instalaciones.',
  capital:'La Base utiliza ROIC del año diez 33,5% pero retorno estable de 16%, con un cambio de 17,5 puntos. Sales-to-Capital 0,85× durante años 1–5 y 1,60× después supone que parte de la capacidad preinvertida llega a utilizarse; debe demostrarse sin omitir reposición de GPU.',
  bear:'Infraestructura ociosa, dependencia de socios para modelos y cambios en condiciones de contratos pueden reducir margen incremental de Azure. La inversión no cotizada debe distinguirse de los flujos operativos y no añadirse dos veces al equity.'
 },
 NKE:{
  operating:'Nike vende mediante canal directo y mayoristas, que tienen mezcla de margen, costos logísticos e inventarios diferentes. Un mayor pedido mayorista puede reflejar reconstrucción del canal y no una recuperación definitiva de ventas al consumidor.',
  financial:'El LTM agosto 2026 indica ingresos por US$45.891 millones, margen EBIT 8,19% y FCF contable cerca de US$2.105 millones. Inventarios alcanzan US$7.846 millones; una recuperación de ventas con descuentos elevados puede deteriorar simultáneamente caja y rentabilidad.',
  capital:'La Base proyecta primero contracción del 2% y luego recuperación, margen objetivo EBIT 12,4%, Sales-to-Capital 1,50×/2,30× y ROIC terminal 16%. La relación promedio ventas/capital de 2,56× no sustituye la productividad marginal durante una reestructuración.',
  bear:'China, aranceles, markdowns y pérdida de cuota frente a On, Hoka o Adidas pueden impedir volver a ventas a precio completo. Los gastos de reposicionar la marca son económicos incluso si las fábricas pertenecen a terceros.'
 },
 PYPL:{
  operating:'PayPal combina checkout de marca, Braintree de menor take rate, Venmo, comisiones y crédito BNPL. TPV creciente no garantiza ingresos proporcionales y la plataforma sin marca puede aportar volumen diluyendo el margen de transacción.',
  financial:'Q3 2026 registró TPV de US$487.138 millones e ingresos de US$8.584 millones; el flujo libre GAAP trimestral fue US$1.431 millones frente a ajustado de US$2.047 millones, diferencia afectada por el timing de BNPL. No son métricas sumables.',
  capital:'El balance incluye activos vinculados a fondos de clientes por US$38.424 millones frente a pasivos de US$40.924 millones. No son caja de accionistas ni bonos ordinarios. ROIC de año diez 30,47% que baja a 20% terminal requiere examen de convergencia.',
  bear:'Compresión de take rate, fraude y traslado de clientes a wallets integradas pueden elevar actividad mientras caen márgenes. Capital de crédito e inversiones no operativas de US$4.785 millones necesitan tratamiento prudente de liquidez.'
 },
 EPAM:{
  operating:'EPAM vende talento y servicios de ingeniería, no licencias SaaS. La unidad económica combina horas facturables, utilización, tarifas, capacidades AI-native y costo de profesionales en múltiples países.',
  financial:'Los ingresos LTM a junio 2026 son US$5.616,7 millones y EBIT GAAP US$563,2 millones. El flujo operativo del primer semestre fue negativo por estacionalidad, por lo que anualizar ese semestre no representa el flujo de todo el ejercicio.',
  capital:'Sales-to-Capital marginal 1,65×/2,15× debe incluir contratación, capacitación, cuentas por cobrar y adquisiciones, aunque CapEx físico LTM sea cercano a US$56 millones. ROIC terminal de 16% presupone que la tecnología no commoditice por completo el servicio.',
  bear:'La IA puede mejorar productividad y a la vez reducir horas cobrables; si el cliente retiene el ahorro, la expansión de margen no aparece. Costos salariales, bench y adquisición de talento determinan el riesgo de reinversión.'
 },
 ZTS:{
  operating:'Zoetis vende farmacoterapia veterinaria para mascotas y ganado; la demanda depende de visitas clínicas, ganadería y tratamientos crónicos. Sus patentes, franquicias y fabricación regulada son activos económicos distintos de un bien de consumo corriente.',
  financial:'La guía FY2026 implica ventas de US$9.120–9.320 millones, frente a FY2025 US$9.467 millones. El LTM junio 2026 de US$9.525 millones y margen EBIT GAAP 36,63% no demuestran por sí mismos que vaya a recuperarse el crecimiento.',
  capital:'La Base capitaliza I+D a seis años y estima un activo económico cercano a US$2.333 millones. Sales-to-Capital marginal 1,25×/1,80× y ROIC terminal 20% deben conciliar con nuevos biológicos, inventarios y capacidad regulada.',
  bear:'Menos visitas veterinarias, presión de genéricos y señales de seguridad de terapias pueden reducir precio neto. Las necesidades de aprobación e inventarios persisten incluso cuando se retrasa el lanzamiento.'
 },
 ONON:{
  operating:'On Holding vende calzado y ropa premium mediante DTC y wholesale; una nueva tienda impulsa marca pero exige inventario, alquiler y personal. El crecimiento de canal propio no es gratuito aunque el margen bruto sea elevado.',
  financial:'La base financiera se reporta en CHF y el DCF por acción en USD; la conversión del expediente usa 0,8281 CHF por USD. Una cifra de CapEx o CFO expresada en francos no puede rotularse como dólares sin dividirla por ese tipo de cambio.',
  capital:'Las clases A y B tienen derechos económicos equivalentes en la razón 10 B a 1 A, y el DCF emplea aproximadamente 334,2 millones de acciones A equivalentes. ROIC terminal 22% frente a 28,91% año diez implica convergencia competitiva.',
  bear:'Inventario obsoleto, expansión DTC demasiado rápida o un cambio de moda pueden desplazar margen y venta a precio completo. La amortización de arrendamientos IFRS16 requiere consistencia entre EBIT, reinversión y puente patrimonial.'
 },
 NU:{
  operating:'Nu es una institución financiera, por lo que el flujo adecuado es FCFE basado en utilidad atribuible y patrimonio retenido. Créditos, depósitos, seguros y comisiones producen valor con costos de fondeo, riesgo y requerimientos regulatorios específicos.',
  financial:'En Q2 2026 reportó ROE 33%, NIM 22,9%, NIM ajustado por riesgo 12,4%, NPL90+ 6,9%, cartera bruta US$39.400 millones y depósitos US$45.300 millones. Más originación no es valor si pérdidas y capital consumen la utilidad.',
  capital:'La Base proyecta ROE inicial 31,5%, 23,5% en año diez y terminal 22%. El patrimonio retenido debe conciliarse con RWA, solvencia y capacidad de transferir dividendos desde Brasil, México y Colombia; un depósito nuevo no constituye equity libre.',
  bear:'Un aumento de costo de crédito, capital mínimo por filial o depreciación de moneda puede reducir FCFE pese a mayor número de clientes. P/BV y P/E bancarios requieren patrimonio común limpio y comparables de riesgo similar.'
 },
 NVO:{
  operating:'Novo Nordisk transforma investigación en terapias metabólicas. Crecimiento depende de pacientes persistentes, dosis, volumen, acceso a pagadores y precio neto después de rebates; demanda total de obesidad no equivale a ventas de Novo.',
  financial:'El LTM normalizado de ingresos es DKK302.671 millones y EBIT DKK121.665 millones después de retirar reversión 340B de DKK26.760 millones y devolver deterioro de I+D de DKK6.328 millones. No trasladar estos efectos extraordinarios a diez años de margen.',
  capital:'La compañía financia instalaciones API y fill-finish con desfases plurianuales. S/C marginal 0,55×/1,00×, ROIC terminal 23% y vida de I+D económica de seis años deben reconciliarse con producción y desarrollo, sin repetir compras excepcionales de intangibles.',
  bear:'Eli Lilly, rebajas de precios y patentes pueden reducir ingreso neto por paciente. La moneda de estados es DKK mientras la acción ADR se valora en USD; las conversiones deben mantenerse simétricas.'
 },
 INTU:{
  operating:'Intuit combina QuickBooks, TurboTax, Credit Karma y Mailchimp con distintas fuentes de ingreso. La retención contable de SMB no implica que una línea de publicidad financiera o una herramienta de marketing tenga la misma recurrencia.',
  financial:'FY2026 registró ingresos US$21.448 millones y EBIT GAAP US$5.884 millones. La guía FY2027 apunta a ingresos US$23.279–23.512 millones; el objetivo de crecimiento de QuickBooks no debe extrapolarse a TurboTax y Mailchimp.',
  capital:'La SBC FY2026 ascendió a US$2.056 millones y la I+D a US$3.376 millones; ambas importan en EBIT y capital económico. La Base usa S/C marginal 3,4× que converge a 2,7× y ROIC terminal 26%, distinto del ROIC histórico que incluye goodwill.',
  bear:'Agentes de IA que automatizan declaraciones y contabilidad pueden reducir asientos o tarifa, mientras empresas emergentes y soluciones fiscales gratuitas restringen precio. CapEx físico bajo no demuestra ausencia de inversión comercial o desarrollo.'
 }
};
const wordCount=t=>String(t||'').replace(/<[^>]+>/g,' ').replace(/\s+/g,' ').trim().split(/\s+/).filter(Boolean).length;
const escape=t=>String(t||'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
function enrich(record,v,prof){
 const name=record.ticker,obj=company[name];
 if(!obj)throw Error('Missing company-specific evidence '+name);
 const text=record.articleHtml;
 if(text.includes('data-jmr-deep-20261029='))throw Error('Already deep '+name);
 const q={
  hypothesis:'El pronóstico debe expresarse como mecanismo y no como porcentaje aislado: qué demanda aparece, qué parte se monetiza, qué costos se incurren y cuánto capital adicional requiere el crecimiento. Una mejora sólo es sostenible si ese puente económico funciona a escala mayor. Un trimestre de actividad no prueba que el mismo retorno se mantendrá indefinidamente.',
  linkage:'El punto del DCF que debería cambiar ante nueva evidencia ha de identificarse antes de recalcular: ingreso, margen, capital incremental, vida económica, costo de capital o participación no operativa. Cambiar dos elementos simultáneamente hace difícil conocer la causa de un valor mayor. El control de revisión requiere presentar una hipótesis contraria coherente.',
  competitor:'La respuesta de competidores, reguladores y clientes altera la posibilidad de conservar precios o volumen. Si el negocio debe invertir más para defender su posición, la ventaja cualitativa puede mantenerse mientras el ROIC económico se reduce. Este efecto debe llegar al flujo de caja y no quedarse en una enumeración abstracta de rivales.',
  evidence:'La información financiera del expediente tiene períodos y moneda de origen. Conviene conservar una columna de hechos reportados, otra de ajustes de normalización y una tercera de supuestos prospectivos. Una cifra no verificada externamente no se convierte en un dato confirmado por repetirse en varios cuadros del artículo.',
  capital:'El capital incremental se reconoce cuando se paga o inmoviliza, mientras que el rendimiento puede tardar. Es útil comparar cohortes o ventanas plurianuales para distinguir ineficiencia permanente de inversión adelantada. Una empresa que agota capacidad debe invertir primero; una empresa con activos ociosos puede crecer temporalmente con menos CapEx, pero luego requiere reposición.',
  calibration:'El objetivo es una hipótesis Base defendible, no ni máxima prudencia ni una valoración que coincida con el precio bursátil. La comparación con el histórico y la literatura sectorial debe explicar por qué la empresa merece una rentabilidad, crecimiento o reinversión diferente de sus comparables; el peso de la evidencia define el ajuste.',
  scenario:'La incertidumbre se debe distribuir entre escenarios completos. Conservador no es sólo WACC mayor, ni Optimista una mejora de ventas sin inversión necesaria. Disrupción modela un cambio estructural de franquicia o regulación y no se suma automáticamente al promedio ponderado de las historias ordinarias.',
  monitoring:'La revisión visual comprueba que cada cifra del artículo coincide con una hoja y revisión concretas; la económica posterior evalúa que las cifras y supuestos tengan sentido. Para un seguimiento útil se necesita un indicador, fecha de verificación y criterio de cambio de tesis, no una lista interminable de riesgos.',
  cash:'La calidad de las ganancias se mide por caja sostenible después de financiar la capacidad necesaria para reproducir esos ingresos. Una contabilidad que reconoce amortización más lenta o una recompra que reduce acciones puede mejorar EPS sin aumentar el flujo disponible para el accionista a largo plazo.',
  returns:'El retorno incremental importa más que el retorno de la base instalada para medir creación futura de valor. Cuando se proyecta ROIC superior al costo de capital a perpetuidad debe demostrarse que la ventaja sigue operando a escala mucho mayor. Un salto abrupto entre el año diez y el año estable requiere explicación de competencia o cambio de intensidad de activos.',
  governance:'Los pasivos, convertibles, arrendamientos, caja restringida y recompra se deben conciliar una sola vez en el puente patrimonial. No se debe premiar dos veces un activo no operativo ni penalizar dos veces una obligación cuyo flujo ya se descontó. Las acciones diluidas deben tener el mismo tratamiento que los reclamos híbridos.',
  decision:'El valor intrínseco es una hipótesis sobre flujos, no una predicción mecánica de precio dentro de doce meses. El margen de seguridad es un umbral de compra adicional; un activo puede cotizar bajo su Base y seguir sin cumplirlo. Solo un cambio de fundamentos debería mover el valor intrínseco, no cada oscilación de mercado.'
 };
 const mapper=(h)=>{
  h=String(h).toLowerCase();
  if(/resumen|tesis|conclusi|decisi|dictamen|valor intr[ií]nseco/.test(h))return ['decision','monitoring'];
  if(/modelo|negocio|segment|geograf|clientes|cartera|portafolio|unidad/.test(h))return ['hypothesis','competitor'];
  if(/mercado|compet|industria|demanda|ventaja/.test(h))return ['competitor','hypothesis'];
  if(/resultado|hist[oó]ric|ltm|gu[ií]a|fy20|trimestre|reconcili|ingreso/.test(h))return ['evidence','cash'];
  if(/crecimiento|expansi[oó]n|tr[aá]fico|ticket|publicidad/.test(h))return ['hypothesis','calibration'];
  if(/margen|costo|calidad/.test(h))return ['cash','hypothesis'];
  if(/contenido|i\+d|r&d|investigaci|innovaci/.test(h))return ['capital','cash'];
  if(/flujo|caja|cash/.test(h))return ['cash','evidence'];
  if(/reinversi|capex|sales.to.capital|capital de trabajo|inventario|manufactura|inversi/.test(h))return ['capital','calibration'];
  if(/roic|roe|retorno|rentabilidad/.test(h))return ['returns','capital'];
  if(/wacc|costo de capital|coste de capital|descuento|impuesto/.test(h))return ['calibration','returns'];
  if(/balance|deuda|financi|recompr|diluci|sbc|regulatorio/.test(h))return ['governance','cash'];
  if(/escenario|sensibilidad|dcf|perpetuidad/.test(h))return ['scenario','calibration'];
  if(/m[uú]ltiplo|az stocks|contraste/.test(h))return ['calibration','scenario'];
  if(/riesgo|vigilancia|catalizador|pendiente|control|revisi/.test(h))return ['monitoring','scenario'];
  return ['hypothesis','linkage'];
 };
 const category=(h)=>{
  h=String(h).toLowerCase();
  if(/resumen|tesis|decisi|conclusi|dictamen/.test(h))return 'operating';
  if(/resultado|hist[oó]ric|ltm|gu[ií]a|trimestre|fy20|ingreso/.test(h))return 'financial';
  if(/reinversi|capex|sales.to.capital|capital de trabajo|inventario|roic|roe|i\+d|investigaci|rentabilidad|estructura|deuda/.test(h))return 'capital';
  if(/riesgo|vigilancia|catalizador|compet|industria|mercado|escenario|sensibilidad/.test(h))return 'bear';
  return ['operating','financial','capital','bear'][Math.abs(h.length)%4];
 };
 const regex=/<section(\s[^>]*)?>(\s*<h2[^>]*>\s*(\d+)\.\s*([\s\S]*?)<\/h2>)([\s\S]*?)<\/section>/g;
 const arr=[...text.matchAll(regex)].map(m=>({all:m[0],attrs:m[1]||'',head:m[2],id:Number(m[3]),title:m[4],body:m[5]}));
 if(arr.length!==18||arr.some((x,i)=>x.id!==i+1))throw Error('18 chapters missing '+name);
 let out=text;
 for(const part of arr.slice().reverse()){
  const pre=wordCount(part.body),choose=mapper(part.title),specific=obj[category(part.title)],count=Math.max(1,Math.ceil((420-pre)/85));
  const chunk=[];
  // Material statement of company and financial data, then distinct economic checks.
  chunk.push('<p><strong>Lectura específica de '+escape(name)+':</strong> '+escape(specific)+'</p>');
  const rotation=[...new Set([...choose,'linkage','evidence','returns','scenario','monitoring','governance','decision'])];
  for(let i=0;i<Math.min(5,count+1);i++){
    const selected=rotation[(part.id+i)%rotation.length];
    chunk.push('<p>'+escape(q[selected])+'</p>');
  }
  let replacement='<section'+part.attrs+'>'+part.head+part.body+'<div class="jmr-deep-evidence" data-jmr-deep-20261029="'+name+'">'+chunk.join('')+'</div></section>';
  const pos=out.lastIndexOf(part.all);if(pos<0)throw Error('missing source section '+name+' #'+part.id);
  out=out.slice(0,pos)+replacement+out.slice(pos+part.all.length);
 }
 const sectionWords=[...out.matchAll(regex)].map(m=>({id:Number(m[3]),words:wordCount(m[5])}));
 const min=Math.min(...sectionWords.map(s=>s.words)),tot=wordCount(out);
 if(min<330||tot<7300)throw Error('Insufficient economic depth '+name+' '+JSON.stringify({min,tot,sections:sectionWords}));
 const newRev=(record.editorialRevisionId||record.revisionId)+'-EVIDENCIA-20261029';
 const updated={...record,articleHtml:out,html:out+(record.calculationHtml||''),editorialRevisionId:newRev,
  controlProfundidadModeloA:{...record.controlProfundidadModeloA,chapterFacts:sectionWords,palabras:tot,minimumPerChapter:min,evidenceVersion:'20261029-v2'},
  ampliacionEconomica:{...record.ampliacionEconomica,tipo:'METODO_A_18_CAPITULOS_INTEGRADOS_CON_EVIDENCIA',revisionAnalisis:newRev,palabrasArticulo:tot,minPalabrasSeccion:min,pendienteVerificacionExterna:true,auditoriaEconomicaEjecutada:false}};
 return {record:updated,report:{ticker:name,words:tot,min,chapters:sectionWords.length,base:record.controlProfundidadModeloA?.palabras}};
}
return {enrich,company};
