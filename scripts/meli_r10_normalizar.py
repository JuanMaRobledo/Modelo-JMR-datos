#!/usr/bin/env python3
"""Restaurar exactamente todas las empresas no-MELI tras exportar JMR V2 y sellar biblioteca final."""
import gzip,hashlib,json,pathlib,sys
root=pathlib.Path(sys.argv[1] if len(sys.argv)>1 else "jmr-v2")
oldName="biblioteca-a588c49d3294c15af27cd854ff178d54fe15d59134db5fdbfc022cf7d79c32b0.json.gz"
base=json.loads(gzip.decompress((root/oldName).read_bytes()))
manifestPath=root/"biblioteca.json"
manifest=json.loads(manifestPath.read_text())
archive=root/manifest["archive"]
current=json.loads(gzip.decompress(archive.read_bytes()))
originalFiles=base["files"]; now=current["files"]
assert set(now)==set(originalFiles),f"Las claves de biblioteca cambiaron: {set(now)^set(originalFiles)}"
assert now["empresas/MELI.json"]["revision"]["id"]=="MELI-V2-LTM20260930-R10"
assert now["analisis/MELI.json"]["revision"]=="MELI-V2-LTM20260930-R10"
# Preservar literalmente todos los demás expedientes, informes y JSON de la instantánea original.
for key in originalFiles:
    if key not in ("empresas/MELI.json","analisis/MELI.json","catalogo.json"):
        now[key]=originalFiles[key]
oldCatalog=originalFiles["catalogo.json"]
newCatalog=now["catalogo.json"]
assert len(oldCatalog["empresas"])==len(newCatalog["empresas"])
newMeli=[x for x in newCatalog["empresas"] if x["ticker"]=="MELI"]
assert len(newMeli)==1
oldTickers=[x["ticker"] for x in oldCatalog["empresas"]]
assert set(oldTickers)=={x["ticker"] for x in newCatalog["empresas"]}
newCatalog["empresas"]=[newMeli[0] if x["ticker"]=="MELI" else x for x in oldCatalog["empresas"]]
now["catalogo.json"]=newCatalog
assert all(now[k]==v for k,v in originalFiles.items() if k not in ("empresas/MELI.json","analisis/MELI.json","catalogo.json"))
assert all(x==y for x,y in zip(now["catalogo.json"]["empresas"],oldCatalog["empresas"]) if x["ticker"]!="MELI")
raw=(json.dumps(current,ensure_ascii=False,separators=(',',':'))+"\n").encode()
digest=hashlib.sha256(raw).hexdigest()
newArchiveName="biblioteca-"+digest+".json.gz"
(root/newArchiveName).write_bytes(gzip.compress(raw,compresslevel=9,mtime=0))
manifest["archive"]=newArchiveName
manifest["sha256"]=digest
manifestPath.write_text(json.dumps(manifest,ensure_ascii=False,indent=1)+"\n")
if archive.name!=newArchiveName and archive.name!=oldName:archive.unlink(missing_ok=True)
print("NORMALIZACION_OK",json.dumps({"sha":digest,"catalogoMELI":newMeli[0]["valorBase"],"otrosExpedientesPreservados":len(now)-3,"manifest":newArchiveName}))
