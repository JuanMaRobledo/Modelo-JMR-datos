"""controles_supuestos.revisar y probabilidades.calcular sobre los datos de R2 (no la ficha legada).
Construye en memoria la ficha con historias, margen LTM, industria e indicadores de VALORACION_A12_EN_REVISION.json."""
import json, sys, tempfile, shutil, os
from pathlib import Path
sys.path[:0]=['/home/user/JMR-valuation','/home/user/JMR-valuation/scripts']
import controles_supuestos as cs, probabilidades as pr
v=json.load(open('/home/user/Modelo-JMR-datos/candidatos/valoraciones/AMZN-20261102-A12-R2/VALORACION_A12_EN_REVISION.json'))
tmp=Path(tempfile.mkdtemp()); 
for x in cs.REF.iterdir():
    if x.name!='damodaran': os.symlink(x, tmp/x.name)
(tmp/'damodaran').mkdir()
ficha={'ticker':'AMZN','industria_damodaran':'Retail (General)','margen_ltm':v['margen_ltm'],
       'historias':[{'id':h['id'],'nombre':h['nombre'],'prob':h['prob'],'margen':h['margen'],'roic_terminal':h['roic_terminal'],'crec':h['crec']} for h in v['historias']],
       'indicadores':v['indicadores'],'ajustes_prob':v['ajustes_prob'], 'justificacion_supuestos': v.get('justificacion_supuestos') or {}}
(tmp/'damodaran'/'AMZN.json').write_text(json.dumps(ficha))
cs.REF=tmp
print('etapa:', pr.etapa('AMZN'))
print('probabilidades:', pr.calcular('AMZN', ficha))
al=cs.revisar('AMZN'); print('controles_supuestos R2:', al or 'sin hallazgos')
shutil.rmtree(tmp)
