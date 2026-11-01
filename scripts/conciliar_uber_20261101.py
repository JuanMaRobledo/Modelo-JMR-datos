"""Conciliar etiquetas y evidencia UBER sin cambiar los flujos ni sus supuestos."""
import json, hashlib, re
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
VP=ROOT/'valoraciones/UBER-20261030-A1.json'
AP=ROOT/'analisis/UBER-research-UBER-20261030-A1.json'
EP=ROOT/'evidencia/uber-conciliacion-20261101/lectura-final.json'
v=json.loads(VP.read_text()); a=json.loads(AP.read_text())
replacements={
 'Cinco múltiplos aún N/D':'Cinco contrastes relativos provisionales con peso cero',
 'La ficha debe mostrar la ausencia de datos relativos como N/D con motivo':'La ficha debe distinguir matrices calculadas de anclas pendientes, con peso cero y motivo',
 'Definiciones y matrices pendientes':'Definiciones de matrices calculadas; anclas y normalización pendientes',
 'Cinco múltiplos y matrices Base N/D: Financials Multiples extrapola ingresos no operativos no recurrentes. Bloqueo de contrato de publicación.':'Cinco matrices Base calculadas como contrastes provisionales, peso cero; anclas sin certificar y normalización de ingresos no operativos pendiente.',
 'Gate de repositorio global en rojo; sin auditoría económica independiente.':'Gate global: último control confirmado aprobado en run 41354221137; comprobar el SHA de cada nueva integración. Auditoría económica pendiente.',
 'Gate global en repo datos continúa bloqueado por PR #202. Esta revisión permanece borrador hasta controles superados.':'UBER-20261030-A1 está integrado EN_REVISION. El PR #209 conserva su borrador histórico; el gate global tuvo ejecución posterior aprobada (41354221137). Verificar el SHA de esta conciliación por separado.',
 'las celdas objetivo de `EVEBITDA`, `EVFCFF`, `PE`, `PFCFE`, `POCF` devuelven N/D y `Sensibilidad por múltiplo` devuelve N/D':'las cinco matrices de `Sensibilidad por múltiplo` están calculadas y conciliadas al VP3, pero sus anclas son provisionales y su peso es cero',
 'las celdas objetivo de <code>EVEBITDA</code>, <code>EVFCFF</code>, <code>PE</code>, <code>PFCFE</code>, <code>POCF</code> devuelven N/D y <code>Sensibilidad por múltiplo</code> devuelve N/D':'las cinco matrices de <code>Sensibilidad por múltiplo</code> están calculadas y conciliadas al VP3, con anclas provisionales y peso cero',
 'por ello no existen matrices relativas oficiales 5×5 que permitan certificar una valoración secundaria':'existen cinco matrices relativas 5×5 provisionales, sin anclas independientes certificadas ni peso en el DCF',
 'hasta resolver dichas reservas y el gate del repositorio':'con dichas reservas expresas y controles técnicos de cada SHA',
 'la ponderación 60/40 de la fuente no se adopta en el objetivo principal':'la hoja se concilió a DCF 100% y múltiplos 0% el 1-nov-2026',
 '5 matrices Base; por eso no establecer promedio alternativo':'5 anclas Base sin certificar; por eso no establecer promedio alternativo',
}
def walk(x):
 if isinstance(x,str):
  for p,q in replacements.items(): x=x.replace(p,q)
  return x
 if isinstance(x,dict): return {k:walk(z) for k,z in x.items()}
 if isinstance(x,list): return [walk(z) for z in x]
 return x
v=walk(v);a=walk(a)
v['validationStatus']='DCF_4_LISTO_DCF_3_CENTROS_OK;_MULTIPLOS_5_PROVISIONALES_PESO_0;_RESERVAS_MATERIALES'
v['controlPublicacion'].update(multiplesCentros5OK=True,multiplesAnclasCertificadas=False,analisisPublicacion='N1_14_N2_EN_REVISION',gateCI='CONSULTAR_SHA_ACTUAL;_ULTIMO_CONFIRMADO_41354221137_SUCCESS')
v['sensibilidadMultiples']['advertencia']='Cinco contrastes provisionales EN_REVISION, sin certificación económica. Hoja y JSON: DCF 100%, múltiplos 0%; criterio Solo 3 años. Anclas e ingresos no recurrentes pendientes de normalización.'
e={'revisionId':v['revisionId'],'sourceSheetId':v['sheet_id'],'sourcePath':str(EP.relative_to(ROOT)),'sha256':hashlib.sha256(EP.read_bytes()).hexdigest(),'fecha':'2026-11-01','estado':'CONCILIADO_CON_RESERVAS_MATERIALES','pesoDcf':1,'pesoMultiplos':0,'dcfBase':v['valorPrincipal'],'mos35':v['precioMOS'],'gateGlobalReferencia':{'run':41354221137,'commit':'35c005df6987926e9f5f70d96c357f44202a80d4','conclusion':'success'},'auditoriaEconomica':'PENDIENTE','verificacionVisualNativa':'PENDIENTE','verificacionDespliegueApp':'PENDIENTE'}
v['conciliacionHoja']=e
v['descuentoMultiples']['criterio']='Solo 3 años; contraste provisional a VP3, peso cero en DCF'
v['descuentoMultiples']['chequeo']['multiples']='CENTROS_5_OK;_ANCLAS_NO_CERTIFICADAS'
for key in ['validationStatus','controlPublicacion','salvedades','sensibilidadMultiples','descuentoMultiples','conciliacionHoja']:
 a[key]=v[key]
a['linkedValuation']['descuentoMultiples']=v['descuentoMultiples']
note='<p data-conciliacion-uber="20261101"><strong>Conciliación 1-nov-2026.</strong> DCF Base presente US$91,14; MOS35% US$59,24. Hoja y JSON usan DCF 100% y múltiplos 0%. El DCF capitalizado FY+3 es US$123,22 y no es el valor presente ni el MOS. Las cinco matrices relativas existen como contrastes provisionales con centros VP3 conciliados: EV/EBITDA y EV/FCFF US$95,39; P/E, P/FCFE y P/OCF US$78,76. Sus anclas no están certificadas y los ingresos no recurrentes pendientes no permiten usarlas como confirmación independiente. El gate global tuvo ejecución posterior aprobada (41354221137); cada cambio requiere control sobre su SHA. Persisten reservas materiales sobre inversiones, dilución y transición ROIC; NOL y tasas requieren soporte. Auditoría económica pendiente.</p>'
for k in ['articleHtml','calculationHtml']:
 if 'data-conciliacion-uber=' not in a[k]: a[k]=a[k].replace('</article>',note+'</article>') if '</article>' in a[k] else a[k]+note
a['html']=a['articleHtml']+a['calculationHtml']
for p,x in [(VP,v),(AP,a)]: p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
for p in ROOT.glob('documentos/UBER-20261030-A1-NIVEL*.md'):
 t=walk(p.read_text());p.write_text(t+'\n\n## Conciliación documental · 1-nov-2026\n\nDCF presente US$91,14 y MOS35% US$59,24. Cinco matrices relativas calculadas, con peso cero y anclas sin certificar; criterio Solo 3 años. El DCF capitalizado FY+3 US$123,22 se identifica por separado. Gate global posterior aprobado: run 41354221137; los controles de esta revisión se registran por SHA. Persisten reservas materiales; auditoría económica pendiente.\n' if '## Conciliación documental' not in t else t)
print('UBER: DCF, escenarios, supuestos y matrices preservados; etiquetas conciliadas')
