"""Ejecuta scripts oficiales de JMR-valuation contra la hoja R2 de AMZN (override del resolvedor de hoja en memoria;
no modifica archivos del repositorio). Uso: python run_oficial.py <script> [args]"""
import sys, runpy, importlib
R2='1h6Xv5cNqwtKPpqI81KiZ_FNpTl4k_uQQS2QJEHphaBI'
sys.path[:0]=['/home/user/JMR-valuation','/home/user/JMR-valuation/scripts']
import hoja_vigente
_orig_hoja, _orig_reg = hoja_vigente.hoja_de, hoja_vigente.registro_activo
hoja_vigente.hoja_de=lambda tk,*a,**k: R2 if tk.upper()=='AMZN' else _orig_hoja(tk,*a,**k)
hoja_vigente.registro_activo=lambda tk,*a,**k: None if tk.upper()=='AMZN' else _orig_reg(tk,*a,**k)
import model_steps
model_steps.hoja_de=lambda tk: R2 if tk.upper()=='AMZN' else _orig_hoja(tk)
script=sys.argv[1]; sys.argv=[script]+sys.argv[2:]
runpy.run_path(f'/home/user/JMR-valuation/scripts/{script}', run_name='__main__')
