from gs import S
import json
SID='1Nb9_T6n8xbJikr68TN5MA5bIIiwm0aKrsF7m4MmOHyM'; q="'CO · Ke y SOTP 60-40'"
data=[]
def put(r,v): data.append({'range':r,'values':v})
put(f"{q}!A3",[["Mismo Ke en las cuatro historias. Pesos por país VERIFICADOS 2T26: Cibest por cartera (6-K 2T26; Banistmo vendido el 30-jun-2026), SURA AM por AUM y Suramericana por primas LTM (presentación corporativa Grupo SURA 2T26)."]])
put(f"{q}!A13:E23",[["País","CRP Damodaran jul-2026","Cibest · cartera 2T26 COPm","SURA AM · AUM 2T26 COP bn","Suramericana · % primas LTM 2T26"],
 ["Colombia",0.0272018253,229573,267,0.65],["Panamá",0.0272018253,0,0,0.03],["El Salvador",0.0804417616,16959,0,0],["Guatemala",0.0309777,16736,0,0],
 ["Chile",0.0104734301,0,202,0.15],["México",0.0272018253,0,321,0.07],["Perú",0.0197831457,0,52,0],["Uruguay",0.0197831457,0,18,0.03],["Brasil",0.0309777,0,0,0.05],["Rep. Dominicana",0.0372356,0,0,0.02]])
put(f"{q}!A32:E32",[["ROE de la INVERSIÓN NUEVA en crecimiento estable = Ke estable + spread","","Cibest","SURA AM","Suramericana"]])
put(f"{q}!A37:B37",[["Criterio","Damodaran: en crecimiento estable la inversión nueva rinde el Ke (sin ventaja) o algo más con ventaja durable; el libro existente conserva su ROE contable (Supuestos!D). Valor año 10 = NI11 × (1 − g/ROE nuevo)/(Ke estable − g). La r2 aplicaba ROE = Ke a todo el libro, lo que obligaba a SURA AM (5,9 billones de plusvalía) a subir su ROE contable de 12% a 17,6%."]])
put("Supuestos!D15:D26",[[.17],[.14],[.135],[.14],[.10],[.10],[.19],[.16],[.15],[.08],[.07],[.06]])
put("Supuestos!D14:I14",[["ROE contable terminal","g libro años 1–5","g libro terminal","Ke inicial","Ke estable (β=1)","ROE inversión nueva (estable)"]])
gcol={1:'C',2:'D',3:'E'}; I=[]
for i in range(12):
    p=i%3+1; c=gcol[p]; sp=[33,34,35][i//3] if i<9 else None
    I.append([f"={q}!${c}$28+{q}!{c}{sp}"] if sp else [f"=D{15+i}"])
put("Supuestos!I15:I26",I)
put("Supuestos!A29",[["ROE contable terminal (D) = analista sobre el libro existente; ROE de la inversión nueva (I) = Ke estable + spread (Disrupción: igual a D). El valor terminal usa NI11 × (1 − g/ROE nuevo)/(Ke estable − g)."]])
for si,n in enumerate(['Base','Conservador','Optimista','Disrupcion']):
    for p in (1,2,3):
        sh=f"{n}_{p}"; r=15+si*3+(p-1)
        put(f"{sh}!A23:B24",[["TV rentas excedentes (= TV DDM − libro año 10)","=B24-K17"],["TV dividendos: NI11 × (1 − g/ROE nuevo)/(Ke estable − g)",f"=K17*Supuestos!D{r}*(1-Supuestos!F{r}/Supuestos!I{r})/($B$32-Supuestos!F{r})"]])
put("Sensibilidad!A6:B6",[["ROE contable terminal +1pp (tres participadas)","=IF(Datos!B30=0;0;((Base_1!K17*Datos!D6*(1-Supuestos!F15/Supuestos!I15)/(Base_1!B32-Supuestos!F15)/Base_1!K19)+(Base_2!K17*Datos!D7*(1-Supuestos!F16/Supuestos!I16)/(Base_2!B32-Supuestos!F16)/Base_2!K19)+(Base_3!K17*Datos!D8*(1-Supuestos!F17/Supuestos!I17)/(Base_3!B32-Supuestos!F17)/Base_3!K19))*1/100*1000000/Datos!B30)"]])
d=json.load(open('/home/user/Modelo-JMR-datos/colombia/auditorias/holdings-20261010-damodaran-r2/sura_sensibilidades.json'))
rows=[["Choque económico univariante (no sumar)","Intrínseco RE COP/acción","Δ RE","Base 60/40 COP/acción","Δ 60/40"],["Base copia actual","=Resumen!B14",0,"='CO · Ke y SOTP 60-40'!B73",0]]
rows+=[[c['driver'],round(c['intrinsicRE'],2),round(c['deltaRE'],2),round(c['blend6040'],2),round(c['deltaBlend'],2)] for c in d['cases']]
rows+=[["","","","",""]]*(15-len(rows))
put("Sensibilidad!A10:E24",rows)
put("Sensibilidad!A25:B25",[["ADVERTENCIA","Filas 12-23: recálculo completo (10 años + terminal, Ke variable) con la réplica independiente auditorias/holdings-20261010-damodaran-r2/sura_sensibilidades.py (r3). Son valores; la Base coincide con la hoja al peso."]])
print(S.spreadsheets().values().batchUpdate(spreadsheetId=SID,body={'valueInputOption':'USER_ENTERED','data':data}).execute()['totalUpdatedCells'])
