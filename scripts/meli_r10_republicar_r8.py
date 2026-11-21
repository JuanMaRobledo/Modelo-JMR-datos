#!/usr/bin/env python3
"""Publicar la recuperación editorial R8 de MELI sobre los valores R10, sin tocar otras empresas."""
import gzip, hashlib, json, os, pathlib, re, sys, unicodedata
from bs4 import BeautifulSoup
import fitz
from weasyprint import HTML

ROOT = pathlib.Path(__file__).resolve().parents[1]
DIR = ROOT / "jmr-v2"
SOURCE = DIR / "fuentes-editoriales/MELI-R10-20261121.html"
PDF_REL = "jmr-v2/informes/MELI/MELI-V2-LTM20260930-R10_INFORME_FUNDAMENTAL.pdf"
PDF_PATH = ROOT / PDF_REL
REVISION = "MELI-V2-LTM20260930-R10"
VALUES = {"conservador": 1110.0353123134807, "base": 2367.5914843010655, "optimista": 3601.4948815116336}
KEYS = ["perfil","introduccion","negocio","calidad","direccion","competencia","ciclos","riesgos",
        "destruccion","tesis_contraria","supuestos","valoracion","conclusiones","fuentes"]
fmt = lambda x: f"{x:,.1f}".replace(",", "TEMP").replace(".", ",").replace("TEMP", ".")
manifest_path = DIR / "biblioteca.json"
manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
archive_path = DIR / manifest["archive"]
raw = gzip.decompress(archive_path.read_bytes())
assert hashlib.sha256(raw).hexdigest() == manifest["sha256"], "Biblioteca fuente corrupta"
lib = json.loads(raw)
files = lib["files"]
base_model = files["empresas/MELI.json"]
original_model = json.dumps(base_model, ensure_ascii=False, sort_keys=True)
old_catalog = json.dumps(files["catalogo.json"], ensure_ascii=False, sort_keys=True)
old_other = {key: json.dumps(val, ensure_ascii=False, sort_keys=True)
             for key,val in files.items() if key not in ("analisis/MELI.json","empresas/MELI.json","catalogo.json")}
doc = files["analisis/MELI.json"]
assert base_model["revision"]["id"] == REVISION
assert doc["revision"] == REVISION
assert all(abs(base_model["libro"]["valores"][k] - expected) < .02 for k,expected in VALUES.items())
assert abs(base_model["libro"]["valores"]["base"] * .65 - 1538.9344647956927) < .02
assert "INFORME" in PDF_REL
print("ESTADO_ORIGINAL",json.dumps({
    "revision": REVISION, "pdf":base_model.get("informe",{}).get("pdf"),
    "paginaOriginal":base_model.get("informe",{}).get("paginas"),
    "schemaAnalisis":doc.get("schemaVersion"),
    "bloquesLongitud":{k:len(str(v)) for k,v in doc.get("blocks",{}).items()},
    "periodos":len(base_model.get("financialPresentation",{}).get("periods",[])),
    "logo":bool(base_model.get("logoUrl")),"numeroEmpresas":len(files["catalogo.json"]["empresas"])
},ensure_ascii=False))

soup = BeautifulSoup(SOURCE.read_text(encoding="utf-8"), "html.parser")
sections = soup.select("section.chapter")
assert len(sections)==14, "Fuente editorial no contiene 14 capítulos"
assert [s.get("id") for s in sections] == [f"cap-{i}" for i in range(1,15)]
blocks={}
for key, section in zip(KEYS, sections):
    fragment=BeautifulSoup(str(section),"html.parser").select_one("section.chapter")
    heading=fragment.select_one(".chapter-head")
    assert heading and heading.h2 and heading.h2.get_text(strip=True)
    heading.decompose()
    for x in fragment.select("aside.reading"):
        x.name="blockquote"
        x.attrs={}
    for x in fragment.select(".key-label"):
        x.attrs={}
    for x in fragment.select(".table-scroll"):
        x.unwrap()
    for el in fragment.find_all(True):
        if el.has_attr("class"):el.attrs.pop("class")
        if el.has_attr("id"):el.attrs.pop("id")
        if el.has_attr("loading"):el.attrs.pop("loading")
    html="".join(str(x) for x in fragment.contents).strip()
    assert len(BeautifulSoup(html,"html.parser").get_text(" ",strip=True))>500,key
    blocks[key]=html

periods=base_model.get("financialPresentation",{}).get("periods",[])
assert len(periods)>=8, "No hay históricos suficientes para informe"
statements=[
  ("Estado de resultados — importes absolutos",
   [("Ingresos","revenue"),("Costo de ingresos","cogs"),("EBIT operativo","operatingProfit"),("Utilidad neta común","netIncomeCommon")]),
  ("Situación financiera — importes absolutos",
   [("Activos totales","assets"),("Pasivos totales","liabilities"),("Patrimonio","equity"),("Caja","cash"),("Deuda total reportada","totalDebt")]),
  ("Flujo de efectivo — importes absolutos",
   [("Flujo operativo","operatingCF"),("CAPEX","capex"),("Flujo de financiación","financingCF"),("Depreciación y amortización","da")])
]
def historic_tables(builder):
    h3=builder.new_tag("h3");h3.string="Anexo histórico R10 — los tres estados"
    desc=builder.new_tag("p");desc.string=("Importes absolutos en USD millones, años fiscales (FY) y LTM separados. "
                  "Fuente: cuadro A-1.2 del expediente vigente; N/D es dato no disponible, nunca cero.")
    tags=[h3,desc]
    for title, cols in statements:
        h4=builder.new_tag("h4");h4.string=title
        table=builder.new_tag("table")
        thead=builder.new_tag("thead");row=builder.new_tag("tr")
        for column in ["Período"]+[name for name,key in cols]:
            th=builder.new_tag("th");th.string=column;row.append(th)
        thead.append(row);table.append(thead)
        tbody=builder.new_tag("tbody")
        for item in periods:
            yr=item.get("year")
            period=item.get("periodo") or ("LTM sep-2026" if yr==2026 else f"FY{yr}")
            tr=builder.new_tag("tr")
            values=item.get("values") or {}
            colsout=[str(period)]
            for name,key in cols:
                v=values.get(key)
                if isinstance(v,(float,int)) and not isinstance(v,bool) and abs(v)<1e6:
                    colsout.append(fmt(v))
                else:
                    colsout.append("N/D")
            for val in colsout:
                td=builder.new_tag("td");td.string=val;tr.append(td)
            tbody.append(tr)
        table.append(tbody)
        wrapper=builder.new_tag("div");wrapper["class"]="table-scroll";wrapper.append(table)
        tags.extend([h4,wrapper])
    return tags
# Mantener íntegro el análisis R10 publicado: añadir la lectura R8, no reemplazar evidencia.
original_blocks=doc["blocks"].copy()
original_lengths={k:len(BeautifulSoup(str(v),"html.parser").get_text(" ",strip=True))
                  for k,v in original_blocks.items()}
for key in KEYS:
    old=BeautifulSoup(str(original_blocks.get(key,"")),"html.parser")
    current=BeautifulSoup(blocks[key],"html.parser")
    present={im.get("src") for im in current.find_all("img") if im.get("src")}
    for pic in old.find_all("img"):
        if pic.get("src") in present:
            ancestor=pic.find_parent("figure")
            if ancestor:ancestor.decompose()
            else:pic.decompose()
    evidence=old.get_text(" ",strip=True)
    if evidence and len(evidence)>150:
        addition='<h3>Detalle documental y evidencia de R10</h3>'+''.join(str(x) for x in old.contents)
        blocks[key]=blocks[key]+'\n'+addition
# Incorporar estados A-1.2 si el capítulo existente no muestra al menos tres tablas.
orig_quality=BeautifulSoup(str(original_blocks.get("calidad","")),"html.parser")
if len(orig_quality.find_all("table"))<3:
    q=BeautifulSoup(blocks["calidad"],"html.parser")
    for tag in historic_tables(q):q.append(tag)
    blocks["calidad"]="".join(str(x) for x in q.contents)
assert all(len(BeautifulSoup(blocks[k],"html.parser").get_text(" ",strip=True)) >= original_lengths.get(k,0)
           for k in KEYS), "Se perdió contenido narrativo original R10"
print("SIN_REGRESION_NARRATIVA",json.dumps({
 k:{"antes":original_lengths.get(k,0),"despues":len(BeautifulSoup(blocks[k],"html.parser").get_text(" ",strip=True))}
 for k in KEYS},ensure_ascii=False))

# El modelo económico, su revisión, el estado de auditoría y el resto del catálogo no cambian.
doc["schemaVersion"]="jmr-v2-analisis-3"
doc["blocks"]=blocks
doc["revision"]=REVISION
doc["editorialVersion"]="R10-ED2-20261121"
doc["editorialReference"]="MELI R8 (profundidad) y NVIDIA R6 (estilo), con cifras vigentes MELI R10"
doc["informePdf"]=PDF_REL
doc["pdf"]=PDF_REL
if isinstance(doc.get("source"),dict):
    doc["source"]["editorial"]="Restauración narrativa R8 y diseño editorial, 21-nov-2026; cifras y motor de R10 intactos"
doc["status"]=doc.get("status") if doc.get("status") not in (None,"") else "EN_REVISION"
assert set(blocks)==set(KEYS)
print("CAPITULOS",json.dumps({k:len(BeautifulSoup(v,"html.parser").get_text(" ",strip=True)) for k,v in blocks.items()},ensure_ascii=False))
print("TABLAS",sum(v.count("<table") for v in blocks.values()),"FIGURAS",sum(v.count("<figure") for v in blocks.values()))

# En el PDF se usan las mismas tablas que en la web. La composición conserva la portada
# y la presentación R8/R10, eliminando instrucciones internas de borrador.
pdfsoup=BeautifulSoup(str(soup),"html.parser")
pdfsoup.select_one("section.editor-note").decompose()
for index,key in enumerate(KEYS,1):
    target=pdfsoup.select_one(f"section#cap-{index}")
    header=target.select_one("header.chapter-head")
    assert header is not None
    header.extract()
    target.clear()
    target.append(header)
    target.append(BeautifulSoup(blocks[key],"html.parser"))
page=str(pdfsoup)
page=page.replace("Borrador editorial sobre R10 — no publicado ni auditado", "INFORME FUNDAMENTAL R10 · EN REVISIÓN ECONÓMICA")
page=page.replace("Borrador editorial / No publicado en aplicación","INFORME R10 · EN REVISIÓN ECONÓMICA")
page=page.replace("Este HTML es una vista previa editorial de la reconstrucción R8 + R10. No modifica ni reemplaza la publicación vigente de la app. Los valores proceden de la R10 y permanecen sujetos a auditoría económica.",
                  "Análisis fundamental MELI R10: narrativa recuperada de R8. Valoración económica pendiente de auditoría independiente.")
page=page.replace("https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&display=swap","")
for name in ["v-fcff.png","v-valor-precio.png","v-trayectorias.png","v-puente.png","v-sens-wacc-g.png","v-sens-m1-g1.png","v-sens-crec-margen.png","v-sens-roic-s2c.png"]:
    original="https://raw.githubusercontent.com/JuanMaRobledo/Modelo-JMR-datos/main/jmr-v2/imagenes/MELI-R10/"+name
    local=(DIR/"imagenes/MELI-R10"/name).resolve()
    assert local.is_file(), "Imagen ausente: "+name
    page=page.replace(original,local.as_uri())
PDF_PATH.parent.mkdir(parents=True,exist_ok=True)
HTML(string=page,base_url=ROOT.as_uri()).write_pdf(str(PDF_PATH))
assert PDF_PATH.stat().st_size>60000
pdf=fitz.open(PDF_PATH)
count=pdf.page_count
text_pdf="\n".join(p.get_text() for p in pdf)
lengths=[len(p.get_text().strip()) for p in pdf]
nonempty=sum(n>50 for n in lengths)
assert count>=23 and count<=85,(count,"Extensión visual inesperada")
empty=[i+1 for i,n in enumerate(lengths) if n<8]
print("CONTENIDO_POR_PAGINA",json.dumps(lengths))
if empty:
    for no in empty:
        before=pdf[no-2].get_text().strip()[-190:] if no>=2 else ""
        after=pdf[no].get_text().strip()[:190] if no<count else ""
        print("PAGINA_EN_BLANCO",no,"ANTERIOR",repr(before),"SIGUIENTE",repr(after),
              "IMAGENES",len(pdf[no-1].get_images(full=True)),flush=True)
assert not empty,("Páginas completamente vacías",empty)
for fragment in ["MercadoLibre","2.367","1.538","riesgos","Valora"]:
    assert fragment.lower() in text_pdf.lower(),fragment
for key,sec in zip(KEYS,sections):
    title=sec.select_one(".chapter-head h2").get_text(" ",strip=True)
    assert any(w.lower() in text_pdf.lower() for w in title.split() if len(w)>7),title
image_occurrences=sum(len(p.get_images(full=True)) for p in pdf)
assert image_occurrences>=8,("No se incorporaron figuras",image_occurrences)
print("PDF_OK",json.dumps({"paginas":count,"paginasTexto":nonempty,"imagenes":image_occurrences,
   "bytes":PDF_PATH.stat().st_size,"sha256":hashlib.sha256(PDF_PATH.read_bytes()).hexdigest()},ensure_ascii=False))
pdf.close()

base_model["informe"]["pdf"]["ruta"]=PDF_REL
base_model["informe"]["pdf"]["sha256"]=hashlib.sha256(PDF_PATH.read_bytes()).hexdigest()
base_model["informe"]["paginas"]=count
base_model["cierreEditorial"]={
    "completo":False, "revision":REVISION, "contratoVersion":"1.5.4",
    "pendientes":["La auditoría económica de Mercado Pago, arrendamientos y WACC sigue abierta; no existe aprobación personal"],
    "evidenciaEditorial":{"capitulos":14,"figuras":image_occurrences,"paginasPdf":count,
        "publicacionWebPdf":"Mismo texto de catorce capítulos, cuadros A-1.2 y ocho figuras",
        "visual":"Render PDF validado por PyMuPDF; revisión humana independiente no atribuida"}
}
assert json.dumps(files["catalogo.json"],ensure_ascii=False,sort_keys=True)==old_catalog,"Cambió catálogo"
assert all(json.dumps(files[k],ensure_ascii=False,sort_keys=True)==v for k,v in old_other.items()),"Cambió otra empresa"
for key,expected in VALUES.items():
    assert abs(base_model["libro"]["valores"][key]-expected)<.02
assert doc["revision"]==base_model["revision"]["id"]==REVISION
assert base_model["informe"]["pdf"]["sha256"]==hashlib.sha256(PDF_PATH.read_bytes()).hexdigest()
new_raw=(json.dumps(lib,ensure_ascii=False,separators=(",",":"))+"\n").encode()
sha=hashlib.sha256(new_raw).hexdigest()
new_name="biblioteca-"+sha+".json.gz"
(DIR/new_name).write_bytes(gzip.compress(new_raw,compresslevel=9,mtime=0))
manifest["archive"]=new_name
manifest["sha256"]=sha
manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=1)+"\n",encoding="utf-8")
assert hashlib.sha256(gzip.decompress((DIR/new_name).read_bytes())).hexdigest()==sha
assert set(lib["files"])==set(old_other)|{"analisis/MELI.json","empresas/MELI.json","catalogo.json"}
# Conservar las bibliotecas históricas y sus respaldos: solo la nueva será activa.
print("PUBLICACION_PREPARADA",json.dumps({
 "hash":sha,"archive":new_name,"pdf":PDF_REL,"paginas":count,
 "otrosArchivosIguales":len(old_other),"valorBase":base_model["libro"]["valores"]["base"],
 "mos":base_model["libro"]["valores"]["base"]*.65,
 "revision":REVISION,"cambioEconomico":False,"chapters":len(blocks)
},ensure_ascii=False))