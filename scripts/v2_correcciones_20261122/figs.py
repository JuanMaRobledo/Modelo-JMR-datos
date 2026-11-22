import json,matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt, numpy as np, sys
W=sys.argv[1]; O=sys.argv[2]; c=json.load(open(W+'/calc.json')); P=11.27
NAVY,BLUE,LIGHT,TAN,RED,GRID,TXT='#1d3449','#5b8baa','#a8c3d3','#c4a282','#c0394b','#e3e8ec','#1d3449'
plt.rcParams.update({'font.family':'Liberation Sans','font.size':11,'axes.edgecolor':'#b9c6cf','axes.titleweight':'bold','axes.titlecolor':TXT,'axes.titlesize':13})
fmt=lambda x,d=2:f'{x:,.{d}f}'.replace(',','@').replace('.',',').replace('@','.')
def fuente(fig,t): fig.text(0.5,0.01,t,ha='center',color='#7d8b96',fontsize=8.5)
def lim(ax): ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False); ax.grid(color=GRID,lw=.8); ax.set_axisbelow(True)
E=c['esc']
# 1 valor vs precio + descomposición
fig,(a1,a2)=plt.subplots(1,2,figsize=(11.5,4.6),gridspec_kw={'width_ratios':[1.35,1]})
lab=['Conservador','MOS 35 % (Base)','Base','Optimista']; val=[E['conservador']['v'],E['base']['v']*.65,E['base']['v'],E['optimista']['v']]
a1.barh(lab,val,color=[LIGHT,TAN,NAVY,BLUE],height=.55); a1.axvline(P,color=RED,ls='--',lw=2,label=f'Cierre 20-nov-2026: USD {fmt(P)}')
for i,v in enumerate(val): a1.text(v+.3,i,f'USD {fmt(v)}',va='center',fontweight='bold',color=TXT)
a1.set_title('Valor intrínseco por escenario vs. precio'); a1.set_xlabel('USD por acción'); a1.set_xlim(0,max(val)*1.3); a1.legend(loc='lower right',frameon=False,fontsize=9); lim(a1); a1.grid(axis='y',visible=False)
b=E['base']; parts=[b['bv0'],b['pvExc'],b['pvTV']]; names=['Patrimonio\ncontable inicial','VP exceso de\nretorno años 1–10','VP exceso de\nretorno terminal']
a2.bar(names,parts,color=[NAVY,BLUE,TAN],width=.55)
for i,v in enumerate(parts): a2.text(i,v+.15,f'USD {fmt(v)}\n({fmt(100*v/b["v"],1)} %)',ha='center',fontweight='bold',fontsize=9.5,color=TXT)
a2.set_title(f'Descomposición del Base (USD {fmt(b["v"])})'); a2.set_ylabel('USD por acción'); a2.set_ylim(0,max(parts)*1.35); lim(a2); a2.grid(axis='x',visible=False)
fuente(fig,'Fuente: libro oficial NU-V2-LTM20260930-R3_VALORACION.xlsx (Equity Excess Return, Damodaran) y cierre 20-nov-2026. MOS 35 % solo Base. Elaboración JMR.')
fig.tight_layout(rect=(0,.05,1,1)); fig.savefig(O+'/valor_vs_precio_r3.png',dpi=150); plt.close(fig)
# 2 trayectorias
fig,(a1,a2)=plt.subplots(1,2,figsize=(11.5,4.4))
for n,col in [('conservador',LIGHT),('base',NAVY),('optimista',BLUE)]:
  y=E[n]['years']; t=[r['t'] for r in y]
  a1.plot(t,[r['bv']/1000 for r in y],marker='o',color=col,lw=2,label=n.capitalize())
  a2.plot(t,[100*r['roe'] for r in y],marker='o',color=col,lw=2,label=n.capitalize())
a2.axhline(100*E['base']['ke'],color=RED,ls='--',lw=1.6,label=f'Ke {fmt(100*E["base"]["ke"])} %')
a1.set_title('Patrimonio común al inicio de cada año'); a1.set_ylabel('USD miles de millones'); a1.set_xlabel('Año de proyección')
a2.set_title('ROE proyectado frente al costo del patrimonio'); a2.set_ylabel('%'); a2.set_xlabel('Año de proyección')
for a in (a1,a2): lim(a); a.legend(frameon=False,fontsize=9); a.set_xticks(range(1,11))
fuente(fig,'Fuente: libro oficial R3 (Equity Excess Return). El patrimonio crece con ROE × retención; desde el año 6 el ROE converge al estable. Elaboración JMR.')
fig.tight_layout(rect=(0,.05,1,1)); fig.savefig(O+'/trayectorias_r3.png',dpi=150); plt.close(fig)
# 3 sensibilidades
fig,(a1,a2)=plt.subplots(1,2,figsize=(11.5,4.4))
def heat(ax,M,rl,cl,tit,xl,yl,ci,cj):
  M=np.array(M); ax.imshow(M>=P,cmap=matplotlib.colors.ListedColormap(['#f4e3e3','#e3efe6']),aspect='auto')
  for i in range(M.shape[0]):
    for j in range(M.shape[1]): ax.text(j,i,fmt(M[i,j]),ha='center',va='center',fontweight='bold' if (i,j)==(ci,cj) else 'normal',color=TXT,fontsize=9.5)
  ax.add_patch(plt.Rectangle((cj-.5,ci-.5),1,1,fill=False,ec=NAVY,lw=2)); ax.set_xticks(range(len(cl))); ax.set_xticklabels(cl); ax.set_yticks(range(len(rl))); ax.set_yticklabels(rl)
  ax.set_title(tit,fontsize=11.5); ax.set_xlabel(xl); ax.set_ylabel(yl)
s=c['sensKeG']; heat(a1,[r['cells'] for r in s['rows']],[fmt(100*r['ke'])+' %' for r in s['rows']],[fmt(100*g,1)+' %' for g in s['gs']],'Costo del patrimonio × crecimiento estable','Crecimiento estable (g)','Ke',2,2)
s=c['sensRoe']; heat(a2,s['rows'],[fmt(100*x,0)+' %' for x in s['hg']],[fmt(100*x,1)+' %' for x in s['st']],'ROE alto crecimiento × ROE estable','ROE estable (año 10 en adelante)','ROE años 1–5',2,2)
fuente(fig,'Fuente: motor V2 «exceso» (réplica verificada de eqexret). Verde: valor ≥ precio USD 11,27; rosado: inferior. Recuadro = Base. Elaboración JMR.')
fig.tight_layout(rect=(0,.05,1,1)); fig.savefig(O+'/sensibilidades_r3.png',dpi=150); plt.close(fig)
# 4 estres
fig,ax=plt.subplots(figsize=(11.5,4.2)); L=['Base R3']+[x[0].split(' (')[0] for x in c['estres']]; V=[E['base']['v']]+[x[1] for x in c['estres']]
ax.barh(L[::-1],V[::-1],color=[RED if v<P else BLUE for v in V[::-1][:-1]]+[NAVY],height=.55); ax.axvline(P,color=RED,ls='--',lw=2,label=f'Cierre USD {fmt(P)}'); ax.axvline(E['base']['v']*.65,color=TAN,ls=':',lw=2,label=f'Precio MOS USD {fmt(E["base"]["v"]*.65)}')
for i,v in enumerate(V[::-1]): ax.text(v+.15,i,f'USD {fmt(v)}',va='center',fontweight='bold',color=TXT)
ax.set_xlim(0,max(V)*1.25); ax.set_xlabel('USD por acción'); ax.set_title('Pruebas de estrés sobre el escenario Base (motor de exceso de retorno)'); ax.legend(frameon=False,loc='lower right',fontsize=9); lim(ax); ax.grid(axis='y',visible=False)
fuente(fig,'Fuente: simulaciones ilustrativas no oficiales con el motor V2 «exceso» sobre la base R3 (4.881,1 M acciones diluidas). Elaboración JMR.')
fig.tight_layout(rect=(0,.05,1,1)); fig.savefig(O+'/estres_r3.png',dpi=150); plt.close(fig)
print('ok')
