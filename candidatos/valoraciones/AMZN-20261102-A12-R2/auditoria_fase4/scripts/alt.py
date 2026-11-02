import copy, json
from blocks import block; from dcf import run
B=block(2); base=run(B)['ps']
E,D=10811*240.35,215026.2621; t=0.25; kd=0.0534
def wacc_path(rf, erp_init, mature, bu=0.8082016226002329):
    bl=bu*(1+(1-t)*D/E); ke=rf+bl*erp_init; w=E/(E+D)*ke+D/(E+D)*kd*(1-t)
    term=rf+mature
    path=[w]*5+[w-(w-term)*k/5 for k in range(1,6)]
    return path, term, ke, w
def alt(**kw):
    p=copy.deepcopy(B); p.update(kw); return p
res={}
def rec(name,p,mode='native'):
    v=run(p,mode)['ps']; res[name]=dict(ps=v, delta=v-base, pct=100*(v-base)/base); return v
# control: recomputar WACC del caso base con la función propia
pth,term,ke,w=wacc_path(0.0494,0.049057867221630184,0.0455)
rec('control_wacc_propio', alt(wacc=pth,wacc_t=term))
intl=0.049057867221630184-0.0455
for nm,rf,m in (('ERP_Nov26_T12m_3.79',0.0494,0.0379),('ERP_Nov26_payout_sost_4.41',0.0494,0.0441),('ERP_Oct26_corte_vigente_Rf5.29_3.70',0.0529,0.0370),('ERP_Nov26_ajustRf_4.01',0.0494,0.0401)):
    pth,term,ke,w=wacc_path(rf,m+intl,m); rec(nm,alt(wacc=pth,wacc_t=term)); res[nm].update(wacc1=w,term=term,ke=ke)
rec('arriendos_operativos_fuera_deuda', alt(debt=B['debt']-100288))
rec('DTL_ganancias_AFS_observado_34608', alt(nonop=B['nonop']-34608))
rec('DTL_total_estimado_57400', alt(nonop=B['nonop']-57400))
rec('no_operativos_menos_20pc', alt(nonop=B['nonop']*0.8))
rec('ROIC_terminal_16.5_ref_moat', alt(roic_t=0.165))
rec('ROIC_terminal_15.2_igual_ano10', alt(roic_t=0.15234960575696127))
rec('ROIC_terminal_11.0', alt(roic_t=0.11))
bu_sw=(970776.5573*0.7809280399984467+370837.8893*0.7809280399984467+161382*11.40876367309658*1.248199417466542)/(970776.5573+370837.8893+161382*11.40876367309658)
pth,term,ke,w=wacc_path(0.0494,0.049057867221630184,0.0455,bu_sw); rec('beta_AWS_Software',alt(wacc=pth,wacc_t=term)); res['beta_AWS_Software'].update(bu=bu_sw,wacc1=w)
rec('SC_0.65_anios1a5', alt(sc=[0.65]*5+B['sc'][5:]))
rec('SC_0.85_anios1a5', alt(sc=[0.85]*5+B['sc'][5:]))
rec('RSU_metodo_tesoro', B,'treasury'); rec('RSU_a_precio_mercado', B,'market')
rec('margen_obj_16', alt(mg=[B['mg'][0]+(0.16-B['mg'][0])*k/9 for k in range(10)], mg_t=0.16))
rec('margen_obj_18', alt(mg=[B['mg'][0]+(0.18-B['mg'][0])*k/9 for k in range(10)], mg_t=0.18))
rec('crec_mas_2pp_anios1a5', alt(gr=[x+0.02 for x in B['gr'][:5]]+B['gr'][5:]))
rec('crec_menos_2pp_anios1a5', alt(gr=[x-0.02 for x in B['gr'][:5]]+B['gr'][5:]))
rec('WACC_terminal_mas_50pb', alt(wacc_t=B['wacc_t']+0.005, wacc=B['wacc'][:5]+[B['wacc'][4]+(B['wacc_t']+0.005-B['wacc'][4])*k/5 for k in range(1,6)]))
rec('WACC_terminal_menos_50pb', alt(wacc_t=B['wacc_t']-0.005, wacc=B['wacc'][:5]+[B['wacc'][4]+(B['wacc_t']-0.005-B['wacc'][4])*k/5 for k in range(1,6)]))
print('base',base)
for k,v in res.items(): print(f"{k:40s} {v['ps']:9.2f} {v['delta']:+8.2f} {v['pct']:+7.2f}%", {a:round(b,5) for a,b in v.items() if a not in ('ps','delta','pct')})
json.dump(dict(base=base,alternativas=res),open('alternativas.json','w'),indent=1)
