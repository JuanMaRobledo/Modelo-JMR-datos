#!/usr/bin/env python3
"""Actualización controlada y reversible de MELI en la biblioteca V2. No publica por sí sola."""
import argparse, copy, gzip, hashlib, json, pathlib, re, sys

OLD="MELI-V2-LTM20260930-R9"
NEW="MELI-V2-LTM20260930-R10"
PDF=f"jmr-v2/informes/MELI/{NEW}_INFORME_FUNDAMENTAL.pdf"
URL="https://docs.google.com/spreadsheets/d/1rlA1zK3hTDCYlUC7n90lMuO9wTTebMeICPbv4bs8mag/edit"
XLSX="https://drive.google.com/file/d/1TRB3o3cF_S9SulFErw3xYLC1GHuZ55ZM/view"
PRICES={"conservador":1110.0353123134807,"base":2367.5914843010655,"optimista":3601.4948815116336}
GROWTH={"conservador":(.22,.12,.11,.12),"base":(.30,.20,.12,.15),"optimista":(.34,.24,.13,.175)}
RESEARCH={"expenseLTM":2757,"fy2025":2269,"fy2024":1934,"fy2023":1831,"years":3,"asset":4914.333333333333,"amortization":2011.3333333333335,"ebitAdjustment":745.6666666666665,"adjustedEbit":3604.6666666666665}
PVD={"operations":114272.31669649723,"presentForecast":39336.420096060254,"presentTerminal":74935.89660043699,"equity":120029.31669649723,"shares":50.696802,"mos":1538.9344647956927}
FORMATS={
"2.059,46":"2.367,59","2059.46":"2367.59","2,059.46":"2,367.59",
"1.338,65":"1.538,93","1338.65":"1538.93",
"778,05":"1.110,04","778.05":"1,110.04",
"3.381,00":"3.601,49","3381.00":"3601.49",
"2.059,5":"2.367,6","1.338,7":"1.538,9",
"98.651,19":"114.272,32","98.651":"114.272",
"104.408,19":"120.029,32","104.408":"120.029",
"74.416,32":"74.935,90","74.416":"74.936",
"24.234,86":"39.336,42","24.235":"39.336",
"75,43 %":"65,58 %","75,4 %":"65,58 %"
}
def dump(path,x):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(x,ensure_ascii=False,indent=1)+"\n",encoding="utf-8")
def patch_text(s):
    for old,new in FORMATS.items(): s=s.replace(old,new)
    return s
def update_in_place(obj):
    if isinstance(obj,dict): return {k:update_in_place(v) for k,v in obj.items()}
    if isinstance(obj,list): return [update_in_place(x) for x in obj]
    if isinstance(obj,str): return patch_text(obj)
    return obj

def prepare(repo,staging):
    manifest=json.loads((repo/"jmr-v2/biblioteca.json").read_text())
    raw=gzip.decompress((repo/"jmr-v2"/manifest["archive"]).read_bytes())
    assert hashlib.sha256(raw).hexdigest()==manifest["sha256"],"Hash biblioteca origen inválido"
    lib=json.loads(raw);f=lib["files"];m=f["empresas/MELI.json"];d=f["analisis/MELI.json"]
    assert m["revision"]["id"]==OLD,(m["revision"]["id"],OLD)
    assert d["revision"]==OLD
    assert abs(m["libro"]["valores"]["base"]-2059.462973969111)<.01
    original=copy.deepcopy(m)
    m["revision"]["historial"][OLD]=copy.deepcopy(original["libro"]["valores"])
    m["revision"]["id"]=NEW;m["revision"]["anterior"]=OLD
    m["revision"]["nota"]="Revisión material: márgenes de Damodaran e I+D a tres años, crecimiento de año 1 reducido y crecimiento anual estabilizado años 2–5; valor 20-nov-2026. R9 preservada en historial y libro Drive."
    for sc,(g1,g25,mar1,target) in GROWTH.items():
        a=m["assumptions"][sc]
        a.update(growth1=g1,growth2to5=g25,margin1=mar1,marginTarget=target)
    m["libro"].update(id=f"{NEW}_VALORACION.xlsx",sha256="b798cd448f34d773a7dd781461e886c12d85976b16863dabaec98c9bd4cb1aa1",url=XLSX,editableUrl=URL,valores=copy.deepcopy(PRICES),capitalizacionID=copy.deepcopy(RESEARCH))
    m["informe"]["pdf"]={"ruta":PDF,"sha256":None}
    m["informe"]["html"]=f"{NEW}_INFORME_FUNDAMENTAL.html"
    m["cierreEditorial"]={"completo":False,"pendientes":["Informe R10 debe regenerarse y revisarse visualmente; auditoría económica del fondeo Mercado Pago, arrendamientos y WACC pendiente"],"revision":NEW,"contratoVersion":"1.5.4","limite":"El editor y los controles no certifican auditoría económica ni aprobación personal."}
    m["warnings"]=[x for x in m.get("warnings",[]) if not ("Supuestos del Base definidos" in x or "Análisis inverso al precio" in x or "valor terminal pesa 75" in x.lower())]
    m["warnings"]+= [
      "R10: crecimiento Base año 1 30 %, años 2–5 20 % anual constante; márgenes operativos 12 % año 1 y 15 % objetivo (fuente: ejemplo Damodaran MercadoLibre26.xlsx), capitalización de I+D a 3 años con cifras propias LTM.",
      "R10: impacto aislado de la capitalización I+D sobre valor por acción en el motor de esta revisión = 0; efecto sobre EBIT histórico +USD 745,67 M y activo de investigación +USD 4.914,33 M. El cambio de valoración respecto de R9 proviene de crecimiento y márgenes prospectivos.",
      "R10: valor terminal representa 65,58 % del valor operativo. Puente EV–patrimonio sujeto a revisión independiente del fondeo de Mercado Pago y de obligaciones de arrendamientos; WACC sectorial 10,6795 % vs cálculo alternativo 11,81 %.",
      "R10: revisión de libro y app actualizada, pendiente auditoría económica independiente y aprobación del propietario. Los archivos históricos R9 y sus informes no son valores vigentes."
    ]
    m["justificaciones"]=update_in_place(m.get("justificaciones",{}))
    for k in list(m["justificaciones"]):
        kl=k.lower()
        if "crec" in kl or "growth" in kl:
            m["justificaciones"][k]="Base R10: 30 % año 1; 20 % anual constante años 2–5 (Conservador 22 %/12 %, Optimista 34 %/24 %). Se desacelera desde el crecimiento reportado del 3T26 de 45 % nominal y 41 % neutral a divisas, por maduración de comercio/crédito, competencia y volatilidad cambiaria. SEC 10-Q 3T26 y resultados publicados el 4-nov-2026. No copiar este supuesto a otras empresas."
        if "margin" in kl or "margen" in kl:
            m["justificaciones"][k]="Márgenes operativos futuros R10: Base 12 % año 1 y 15 % año 5 (como ejemplo MELI de Damodaran); Conservador 11 %→12 %, Optimista 13 %→17,5 %. EBIT LTM reportado 2.859 M (7,42 %), EBIT ajustado por capitalización de I+D de 3 años 3.604,67 M (9,36 %). La recuperación proyectada exige mejora de rentabilidad de crédito/logística y sigue sujeta a auditoría."
    m["justificaciones"]["capitalizacionID"]="Método Damodaran de capitalización de I+D (vida 3 años). Datos enlazados en el libro vigente: FY2023 1.831 M, FY2024 1.934 M, FY2025 2.269 M, LTM sep-2026 2.757 M; activo I+D 4.914,33 M, amortización 2.011,33 M y ajuste EBIT +745,67 M. La activación del convertidor no cambió por sí sola el valor DCF porque el motor usa márgenes proyectados y ventas/capital explícitos."
    m["justificaciones"]["actualizacionR10"]="Fuente directa: libro Google Sheet "+URL+" y copia XLSX con sha256 "+m["libro"]["sha256"]+". Revisión V2 v1.5.4. No altera motor ni otras empresas."
    if isinstance(m.get("analysis"),dict):
        m["analysis"]=update_in_place(m["analysis"])
        m["analysis"]["story"]="R10: crecimiento Base de ingresos de 30 % en año 1 y 20 % anual en años 2 a 5 (desaceleración desde +45 % reportado 3T26); márgenes 12 % año 1 y 15 % año 5 (criterio del ejemplo de Damodaran); amortización económica de I+D a tres años usando gastos propios, con ajustes de EBIT/ROIC sin doble contabilización."
        m["analysis"]["conclusion"]="Valor intrínseco Base R10 US$2.367,59, Conservador US$1.110,04 y Optimista US$3.601,49; umbral de compra Base MOS 35 % US$1.538,93 vs cotización fechada 19-nov-2026 US$1.355,49. Valoración EN_REVISION: la selección de financiación del negocio fintech, la capitalización de arrendamientos y el WACC siguen pendientes de auditoría económica. No es aprobación personal ni recomendación individualizada."
    d["revision"]=NEW;d["informePdf"]=PDF;d["pdf"]=PDF
    d["source"]["type"]="Revisión MELI R10, libro Google Sheets de 20-nov-2026 con metodologías de márgenes e I+D de Damodaran y crecimientos propios; informe completo de 14 capítulos adaptado desde R9. Pendiente de auditoría personal y económica."
    d["source"]["url"]=URL
    d["blocks"]=update_in_place(d["blocks"])
    # Una revisión material necesita nuevas secciones de valoración y supuestos para que no queden cifras R9 implícitas.
    d["blocks"]["supuestos"]='''<p><strong>Actualización R10 (20-nov-2026), prevalece sobre las estimaciones anteriores.</strong> Corte financiero LTM sep-2026 y precio de referencia 19-nov-2026. Fuente principal: informes oficiales 10-K FY2025 y 10-Q 3T26, libro R10 y ejemplo de Aswath Damodaran de agosto 2026. Estos supuestos son proyecciones propias, no guidance del emisor.</p>
<h3>Historias, números y contraevidencia</h3>
<table><thead><tr><th>Variable</th><th>Conservador</th><th>Base</th><th>Optimista</th></tr></thead><tbody>
<tr><td>Crecimiento ingresos año 1</td><td>22 %</td><td>30 %</td><td>34 %</td></tr>
<tr><td>Crecimiento anual constante años 2–5</td><td>12 %</td><td>20 %</td><td>24 %</td></tr>
<tr><td>Margen EBIT año 1</td><td>11 %</td><td>12 %</td><td>13 %</td></tr>
<tr><td>Margen EBIT objetivo año 5</td><td>12 %</td><td>15 %</td><td>17,5 %</td></tr>
<tr><td>Ventas/capital años 1–10</td><td>2,5×</td><td>3,5×</td><td>4,5×</td></tr>
<tr><td>ROIC terminal</td><td>10,68 %</td><td>18 %</td><td>22 %</td></tr>
<tr><td>WACC</td><td>10,6795 %</td><td>10,6795 %</td><td>10,6795 %</td></tr>
<tr><td>g terminal</td><td>4,0 %</td><td>4,0 %</td><td>4,0 %</td></tr>
</tbody></table>
<p><strong>Historia Base:</strong> los ingresos de MELI crecieron 45 % interanual en 3T26 (41 % a tipo de cambio neutral). El 30 % de año 1 anticipa desaceleración a medida que crece la escala; el 20 % anual estable en años 2–5 refleja adopción de comercio electrónico, publicidad y pagos, con maduración gradual del negocio de crédito. Los ingresos proyectados de año 5 son USD 103.845,68 millones, desde USD 38.523 millones LTM; no es una tasa implícita perpetua.</p>
<p><strong>Contraevidencia:</strong> la expansión del crédito puede elevar las provisiones, la logística y promociones pueden erosionar margen, las tasas y divisas pueden afectar el crecimiento nominal y el mercado latinoamericano es heterogéneo. El margen EBIT reportado LTM es 7,42 %. Pasar a 12 % en el año 1 exige una recuperación exigente; el 15 % de año 5 se adopta por instrucción del propietario del modelo MELI de Damodaran, no por dato observado.</p>
<h3>Capitalización de I+D de Damodaran</h3>
<p>Se capitaliza I+D y tecnología elegible con vida económica de 3 años. Las cohortes propias LTM/FY son USD 2.757 M, USD 2.269 M, USD 1.934 M y USD 1.831 M. El activo I+D estimado es USD 4.914,33 M y su amortización anual USD 2.011,33 M: aumento de EBIT histórico USD 745,67 M hasta USD 3.604,67 M (margen ajustado 9,36 %). El resultado económico no debe sumar este activo por segunda vez al puente patrimonial ni fingir que por sí solo elevó el DCF.</p>
<p><strong>Reinversión, descuento y terminal:</strong> ventas/capital marginal Base 3,5×; WACC por mezcla sectorial 10,6795 %, diferente de una alternativa bottom-up de aproximadamente 11,81 %. ROIC terminal 18 % y crecimiento perpetuo 4 %. La conciliación del fondeo fintech con EBIT, deuda y provisiones, así como arrendamientos, sigue sin auditoría económica. Una valoración optimista requiere evidencia futura de rentabilidad del crédito, monetización publicitaria y estabilidad del costo de capital.</p>
<p>Libro con celdas enlazadas y escenarios: <a href="'''+URL+'''">MELI R10 oficial, Google Sheets</a>.</p>
'''
    d["blocks"]["valoracion"]='''<p><strong>DCF FCFF Simple Ginsu · actualización R10 calculada en el libro oficial.</strong> No es valoración auditada ni recomendación de inversión.</p>
<h3>Resultado de los tres escenarios</h3>
<table><thead><tr><th>Escenario</th><th>Valor intrínseco por acción</th><th>Lectura</th></tr></thead><tbody>
<tr><td>Conservador</td><td>US$1.110,04</td><td>Menor crecimiento, margen y reinversión más exigente</td></tr>
<tr><td>Base</td><td><strong>US$2.367,59</strong></td><td>Crecimiento 30 %/20 % y margen 12 %→15 %</td></tr>
<tr><td>Optimista</td><td>US$3.601,49</td><td>Mayor escala y margen operativo objetivo 17,5 %</td></tr>
<tr><td>Precio con MOS del 35 % sobre Base</td><td><strong>US$1.538,93</strong></td><td>Regla del modelo, no pronóstico de cotización</td></tr>
<tr><td>Precio de referencia 19-nov-2026</td><td>US$1.355,49</td><td>Fecha distinta de los insumos históricos de Damodaran</td></tr>
</tbody></table>
<h3>De valor de operaciones a patrimonio</h3>
<table><thead><tr><th>Componente</th><th>USD millones</th></tr></thead><tbody>
<tr><td>PV flujos FCFF años 1–10</td><td>39.336,42</td></tr>
<tr><td>PV valor terminal</td><td>74.935,90</td></tr>
<tr><td>Valor de operaciones</td><td>114.272,32</td></tr>
<tr><td>Deuda corporativa restada</td><td>(2.369,00)</td></tr>
<tr><td>Caja disponible sumada</td><td>4.010,00</td></tr>
<tr><td>Otros activos no operativos sumados</td><td>4.116,00</td></tr>
<tr><td>Valor patrimonial</td><td>120.029,32</td></tr>
<tr><td>Acciones diluidas (millones)</td><td>50,696802</td></tr>
<tr><td>Valor intrínseco Base por acción</td><td>2.367,59</td></tr>
</tbody></table>
<p>El valor terminal equivale a 65,58 % del valor operativo. Esta elevada dependencia exige sensibilidad del WACC y g terminal y contraste con una estimación de WACC bottom-up. El diferencial de precio al Base no demuestra margen de seguridad económico hasta auditar el tratamiento integral del fondeo de Mercado Pago, cartera, deterioros, arrendamientos y riesgo por país. El WACC utilizado es 10,6795 % y el crecimiento terminal 4,0 %.</p>
<p>La capitalización de I+D modifica EBIT ajustado y capital invertido, pero la prueba aislada no cambió el valor por acción en el DCF con márgenes exógenos. El aumento frente al R9 de origen obedece a márgenes futuros más elevados y el posterior descenso a una proyección de crecimiento menor. Ver la <a href="'''+URL+'''">hoja R10</a> para supuestos, flujos, sensibilidad y controles.</p>
'''
    d["blocks"]["supuestos"] += '<figure><img src="https://raw.githubusercontent.com/JuanMaRobledo/Modelo-JMR-datos/main/jmr-v2/imagenes/MELI-R10/v-trayectorias.png" alt="MELI R10: trayectoria de ingresos y margen operativo Base"/><figcaption>Proyección R10 Base calculada a partir del libro oficial; cifras USD millones y porcentajes.</figcaption></figure>'
    d["blocks"]["valoracion"] += '<figure><img src="https://raw.githubusercontent.com/JuanMaRobledo/Modelo-JMR-datos/main/jmr-v2/imagenes/MELI-R10/v-valor-precio.png" alt="MELI R10: valor por escenario, MOS y precio de referencia"/><figcaption>Valores recalculados por el mismo motor, sin auditoría independiente.</figcaption></figure><figure><img src="https://raw.githubusercontent.com/JuanMaRobledo/Modelo-JMR-datos/main/jmr-v2/imagenes/MELI-R10/v-puente.png" alt="Puente de valor operativo a patrimonio, MELI R10"/><figcaption>USD millones; el fondeo Mercado Pago requiere auditoría.</figcaption></figure><figure><img src="https://raw.githubusercontent.com/JuanMaRobledo/Modelo-JMR-datos/main/jmr-v2/imagenes/MELI-R10/v-sens-wacc-g.png" alt="Sensibilidad R10 WACC y g terminal"/><figcaption>Sensibilidad 5×5 calculada por el motor V2; valor por acción USD.</figcaption></figure>'
    # Cuadros históricos auténticos del A-1.2/financialPresentation:
    # evita un PDF que se limita a describir los estados sin presentarlos.
    import html as html_escape
    periods=m.get("financialPresentation",{}).get("periods",[])
    if len(periods)<3:raise ValueError("No hay períodos suficientes para presentar los tres cuadros")
    specs=[
      ("Estado de resultados",[
        ("Ingresos", "revenue"),("Costo de ingresos", "cogs"),
        ("EBIT operativo", "operatingProfit"),("Utilidad neta", "netIncomeCommon")]),
      ("Balance general",[
        ("Activos", "assets"),("Pasivos", "liabilities"),
        ("Patrimonio", "equity"),("Caja", "cash"),("Deuda total reportada", "totalDebt")]),
      ("Estado de flujos de efectivo",[
        ("Flujo operativo", "operatingCF"),("Capex", "capex"),
        ("Flujo de financiación", "financingCF"),("Depreciación y amortización", "da")])
    ]
    tables=['<h3>Cuadros históricos oficiales · FY y LTM separados</h3><p>Importes absolutos, USD millones. Fuente: estados A-1.2 del expediente y 10-K/10-Q de MercadoLibre. N/D significa no disponible, no cero.</p>']
    for title,cols in specs:
        tables.append('<h4>'+html_escape.escape(title)+'</h4><table><thead><tr><th>Período</th>'+''.join('<th>'+html_escape.escape(label)+'</th>' for label,_ in cols)+'</tr></thead><tbody>')
        for item in periods:
            year=item.get("year"); period=item.get("periodo") or (("LTM 30-sep-2026" if year==2026 else "FY"+str(year)))
            values=item.get("values") or {}
            row=['<tr><td>'+html_escape.escape(str(period))+'</td>']
            for label,key in cols:
                value=values.get(key)
                cell=("N/D" if value is None or not isinstance(value,(int,float)) else f"{value:,.1f}")
                row.append('<td>'+cell+'</td>')
            row.append('</tr>');tables.append(''.join(row))
        tables.append('</tbody></table>')
    chapter="calidad" if "calidad" in d["blocks"] else ("finanzas" if "finanzas" in d["blocks"] else None)
    if not chapter:raise ValueError("No hay capítulo de calidad/finanzas para incluir los tres estados históricos")
    d["blocks"][chapter]+='\n'+''.join(tables)
    # Sincronizar cabeceras de los capítulos y las referencias a imágenes de valoración.
    for key,html in d["blocks"].items():
        if key in ("supuestos","valoracion"): continue
        html=re.sub(r"(?i)34(?:,2)?\s*%\s*por debajo del valor", "42,75 % por debajo del valor",html)
        html=re.sub(r"(?i)1,3\s*%\s*por encima del precio con margen de seguridad", "11,92 % por debajo del precio con margen de seguridad",html)
        for name in ("v-valor-precio.png","v-trayectorias.png","v-fcff.png","v-puente.png","v-sens-wacc-g.png","v-sens-m1-g1.png","v-sens-crec-margen.png","v-sens-roic-s2c.png"):
            html=html.replace("/jmr-v2/imagenes/MELI/"+name,"/jmr-v2/imagenes/MELI-R10/"+name)
        d["blocks"][key]=html
    d["blocks"]["perfil"]='<p><strong>Ficha vigente R10 · Base US$2.367,59 · MOS 35 % US$1.538,93 · precio 19-nov-2026 US$1.355,49 · no auditada.</strong></p>'+d["blocks"]["perfil"]
    d["blocks"]["conclusiones"]='<p><strong>Conclusión económica actualizada, R10:</strong> el escenario Base da US$2.367,59 por acción con crecimiento de 30 % el primer año, 20 % estable del año 2 al 5, margen operativo 12 %→15 % y I+D capitalizada en tres años. MOS 35 %: US$1.538,93. Comparar con precio de referencia US$1.355,49 (19-nov-2026); la valoración permanece EN_REVISION hasta conciliar fondeo de Mercado Pago, arrendamientos y WACC.</p>'+d["blocks"]["conclusiones"]
    for key,val in d["blocks"].items():
        if not isinstance(val,str) or not val.strip(): raise ValueError("Capítulo vacío "+key)
        if any(x in val for x in ["2.059,46","1.338,65","US$778,05","3.381,00"]):raise ValueError("Cifra obsoleta en capítulo "+key)
    for key,val in f.items():
        dest=staging/"origen"/key
        dump(dest,val)
    dump(staging/"render"/"inventario.json",{"sourceLibrarySha":manifest["sha256"],"empresas":[{"ticker":"MELI","revision":NEW,"estado":"CANDIDATO_JSON","pdf":PDF}]})
    dump(staging/"render"/"MELI"/"meta.json",{"ticker":"MELI","company":"MercadoLibre, Inc.","revision":NEW,"estado":"EN_REVISION","asOf":"2026-09-30","pdf":PDF,"sourceLibrarySha":manifest["sha256"]})
    dump(staging/"render"/"MELI"/"analisis.json",d)
    dump(staging/"expected.json",{"oldSha":manifest["sha256"],"revision":NEW,"prices":PRICES,"pdf":PDF,"research":RESEARCH,"metrics":PVD})
    print("STAGING_OK",NEW,len(f),"archived source",manifest["sha256"])

def finish(repo,staging):
    expected=json.loads((staging/"expected.json").read_text())
    pdf=staging/"render/MELI"/pathlib.Path(PDF).name
    if not pdf.exists() or pdf.stat().st_size<50000:raise RuntimeError("No hay PDF regenerado válido")
    inventory=json.loads((staging/"render/inventario.json").read_text())
    rec=next(x for x in inventory["empresas"] if x["ticker"]=="MELI")
    if rec["estado"]!="CANDIDATO_PDF" or rec["paginasVacias"] or rec["textoFueraDePagina"]:
        raise RuntimeError("PDF no pasó verificación: "+str(rec))
    model_path=staging/"origen/empresas/MELI.json";m=json.loads(model_path.read_text())
    m["informe"]["pdf"]["sha256"]=hashlib.sha256(pdf.read_bytes()).hexdigest()
    m["informe"]["paginas"]=rec["paginas"]
    m["cierreEditorial"]={"completo":False,"pendientes":["Inspección visual humana de todas las páginas y auditoría económica independiente aún pendientes"],"revision":NEW,"contratoVersion":"1.5.4","limite":"Render y controles técnicos no son auditoría económica ni aprobación personal."}
    dump(model_path,m)
    dest=repo/PDF;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(pdf.read_bytes())
    # Materializa solo los 8 gráficos económicos recalculados; no sobrescribe imágenes originales R9.
    source=staging/"imagenes"
    target=repo/"jmr-v2/imagenes/MELI-R10"
    target.mkdir(parents=True,exist_ok=True)
    names=["v-valor-precio.png","v-trayectorias.png","v-fcff.png","v-puente.png","v-sens-wacc-g.png","v-sens-m1-g1.png","v-sens-crec-margen.png","v-sens-roic-s2c.png"]
    for name in names:
        file=source/name
        if not file.exists() or file.stat().st_size<2000:raise RuntimeError("Falta gráfico vigente: "+name)
        (target/name).write_bytes(file.read_bytes())
    print("RENDER_OK",rec["paginas"],"pages","PDF sha",m["informe"]["pdf"]["sha256"])
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("mode",choices=["prepare","finish"]);p.add_argument("--repo",default=".");p.add_argument("--stage",default="/tmp/meli-r10")
    a=p.parse_args()
    if a.mode=="prepare":prepare(pathlib.Path(a.repo).resolve(),pathlib.Path(a.stage))
    else:finish(pathlib.Path(a.repo).resolve(),pathlib.Path(a.stage))
