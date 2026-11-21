#!/usr/bin/env python3
"""Gráficos MELI R10: datos de la hoja vigente y sensibilidades calculadas por el motor V2."""
import json,pathlib,sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
stage=pathlib.Path(sys.argv[1] if len(sys.argv)>1 else '/tmp/meli-r10')
data=json.loads((stage/'engine-results.json').read_text())
expected=json.loads((stage/'expected.json').read_text())
out=stage/'imagenes';out.mkdir(exist_ok=True)
PRICE=1355.49;MOS=expected['metrics']['mos'];PRICES=data['scenarios']
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,'axes.spines.right':False,'figure.facecolor':'white','savefig.facecolor':'white'})
NAVY='#234c63';TURQ='#1b958e';GOLD='#c4a167';GREY='#667687'
def save(name):
 plt.tight_layout(pad=2);plt.savefig(out/name,dpi=165,bbox_inches='tight');plt.close()
fig,ax=plt.subplots(figsize=(10,5))
labels=['Conservador','Base','Optimista']
vals=[PRICES[x] for x in ['conservador','base','optimista']]
bars=ax.barh(labels,vals,color=[GREY,TURQ,NAVY],height=.55)
for b,v in zip(bars,vals):ax.text(v+45,b.get_y()+b.get_height()/2,'US$ '+f'{v:,.0f}',va='center',fontsize=11,weight='bold')
ax.axvline(PRICE,linestyle='--',color='#9d6e59',linewidth=2,label='Precio 19-nov-2026 · US$ 1.355,49')
ax.axvline(MOS,linestyle=':',color=GOLD,linewidth=2.2,label='MOS Base 35 % · US$ 1.538,93')
ax.set_xlim(0,max(vals)*1.27);ax.set_xlabel('Valor por acción · USD');ax.set_title('MELI · valoración por escenarios · R10',loc='left',weight='bold')
ax.legend(loc='lower right',frameon=False,fontsize=8)
save('v-valor-precio.png')
years=list(range(0,11))
revenue=[38523,50079.9,60095.88,72115.056,86538.0672,103845.68064,121291.75498752,137787.4336658227,152117.32676706827,163069.77429429718,169592.56526606908]
margin=[.0935718055880037,.12,.132,.138,.144,.15,.15,.15,.15,.15,.15]
fig,ax=plt.subplots(figsize=(10,5))
ax.plot(years,[x/1000 for x in revenue],marker='o',color=NAVY,linewidth=2.5,label='Ingresos USD mil millones')
ax.set_xlabel('Año proyectado (0=LTM sep-2026)');ax.set_ylabel('Ingresos (USD mil millones)',color=NAVY)
ax2=ax.twinx();ax2.plot(years,[x*100 for x in margin],marker='D',linestyle='--',color=TURQ,linewidth=2,label='Margen EBIT %')
ax2.set_ylabel('Margen operativo (%)',color=TURQ);ax2.set_ylim(0,20)
ax.set_title('MELI R10 · ingresos y margen EBIT del escenario Base',loc='left',weight='bold');ax.grid(alpha=.15)
l1,h1=ax.get_legend_handles_labels();l2,h2=ax2.get_legend_handles_labels();ax.legend(l1+l2,h1+h2,loc='upper left',frameon=False,fontsize=9)
save('v-trayectorias.png')
fcff=[1557.7938877153983,2399.6929603557537,3197.8357294852694,4219.247887852361,6470.75770338117,8432.43136651527,10572.7721475068,12769.197697968099,14864.410901135061,15131.29094813192]
fig,ax=plt.subplots(figsize=(10,4.7))
ax.bar(range(1,11),[n/1000 for n in fcff],color=TURQ,width=.68)
ax.set_title('MELI R10 · FCFF proyectado (Base)',loc='left',weight='bold');ax.set_xlabel('Año');ax.set_ylabel('FCFF USD mil millones');ax.set_xticks(range(1,11));ax.grid(axis='y',alpha=.15)
save('v-fcff.png')
fig,ax=plt.subplots(figsize=(10,5))
bridge=[114272.31669649723,-2369,4010,4116,120029.31669649723]
names=['Valor operativo','Deuda','Caja','Otros activos','Patrimonio']
ax.bar(names,[x/1000 for x in bridge],color=[NAVY,'#ae7777',TURQ,GOLD,NAVY],width=.6)
for i,v in enumerate(bridge):ax.text(i,v/1000+(2 if v>=0 else -4),f'{v/1000:,.1f}',ha='center',fontsize=9)
ax.set_ylim(-12,135);ax.tick_params(axis='x',rotation=15);ax.set_ylabel('USD mil millones')
ax.set_title('MELI R10 · conciliación EV–patrimonio',loc='left',weight='bold');ax.grid(axis='y',alpha=.15)
save('v-puente.png')
matrix=[
 ('wacc_g','v-sens-wacc-g.png','WACC inicial/terminal × crecimiento perpetuo',True,True),
 ('margen1_crecimiento1','v-sens-m1-g1.png','Margen EBIT año 1 × crecimiento año 1',True,True),
 ('crecimientoto5_margenobjetivo','v-sens-crec-margen.png','Crecimiento años 2–5 × margen objetivo',True,True),
 ('roicterminal_ventascapital','v-sens-roic-s2c.png','ROIC terminal × ventas/capital marginal',True,False)
]
for key,name,title,rowPercent,colPercent in matrix:
 grid=data['grids'][key]
 values=np.asarray(grid['values'],dtype=float)
 fig,ax=plt.subplots(figsize=(9.4,5.7))
 im=ax.imshow(values,cmap='YlGnBu',aspect='auto',interpolation='nearest')
 fmt=lambda x,p: f'{x*100:.1f} %' if p else f'{x:.1f}×'
 ax.set_xticks(range(5),[fmt(x,colPercent) for x in grid['columnAxis']])
 ax.set_yticks(range(5),[fmt(x,rowPercent) for x in grid['rowAxis']])
 for i in range(5):
  for j in range(5):ax.text(j,i,'$'+f'{values[i,j]:,.0f}',ha='center',va='center',fontsize=9,color='white' if values[i,j]>values.min()+(values.max()-values.min())*.54 else NAVY,weight='bold' if (i,j)==(2,2) else 'normal')
 ax.set_title('MELI R10 · sensibilidad: '+title,loc='left',fontsize=12,weight='bold')
 ax.set_ylabel(title.split(' × ')[0]);ax.set_xlabel(title.split(' × ')[-1])
 fig.colorbar(im,ax=ax,label='Valor intrínseco por acción (USD)',shrink=.85)
 save(name)
print('GRAFICOS_OK',len(list(out.glob('*.png'))),[x.name for x in out.glob('*.png')])
