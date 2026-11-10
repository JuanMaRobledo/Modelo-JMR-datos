import sys,subprocess,os,openpyxl
SP='/tmp/claude-0/-home-user/b8c0d315-1e6b-524a-8878-fb2b853781cf/scratchpad'
ORIG=SP+'/orig/fcffsimpleginzu.xlsx'
COMMON={'B3':46332,'B4':'MercadoLibre, Inc.','B7':'United States','B8':'Retail (General)','B9':'Retail (General)',
 'B11':38523,'B12':2859,'B13':150,'B14':8200,'B15':2369,'B16':'Yes','B17':'No','B18':8126,'B19':0,'B20':0,'B21':50.696802,'B22':1510,'B23':0.2646,'B24':0.32,
 'B27':0.0936,'B30':5,'B34':0.0486,'B37':'No','B38':0,'B39':0,'B40':0,'B41':0,'B45':'No','B51':'No','B53':'V','B54':0.5,'B56':'No','B59':'No','B61':'No','B62':0,'B64':'No','B67':'Yes','B68':0.04,'B70':'No','B71':0,
 'C11':28893,'D11':1,'C12':3201,'C13':125,'C14':6748,'C15':1773,'C18':6710,'C19':0,'C20':0}
COC={'B11':'Detailed','B21':'Multibusiness (Global)','B25':'Operating countries','B32':6,'B33':'Direct Input','B34':0.069,
 'G5':'Brazil','H5':16305,'G6':'Mexico','H6':6742,'G7':'Argentina','H7':5355,'G8':'Chile','H8':500,'G9':'Colombia','H9':450,'G10':'Uruguay','H10':250,'G11':'Peru','H11':162,
 'G12':None,'H12':None,'G13':None,'H13':None,'G14':None,'H14':None,'G15':None,'H15':None,'G16':None,'H16':None,'G17':None,'H17':None,
 'G52':'Retail (General)','H52':16771,'G53':'Information Services','H53':12993}
RD={'F6':3,'F7':2757,'B11':2269,'B12':1934,'B13':1831,'B14':None,'B15':None,'B16':None,'B17':None,'B18':None,'B19':None,'B20':None}
ERP={'B1':0.03387}
STORY={
 'base':{'B26':0.30,'B28':0.19,'B29':0.135,'B31':3.2,'B32':3.0,'B48':'Yes','B49':0.14},
 'cons':{'B26':0.22,'B28':0.11,'B29':0.09,'B31':2.5,'B32':2.3,'B48':'No','B49':0.14},
 'opt':{'B26':0.36,'B28':0.23,'B29':0.165,'B31':3.8,'B32':3.4,'B48':'Yes','B49':0.164}}
from math import log,exp,sqrt,erf
def Nn(x): return 0.5*(1+erf(x/sqrt(2)))
def adjS(S,K,T,sig,r,n,N):
    s_=S
    for _ in range(200):
        d1=(log(s_/K)+(r+sig*sig/2)*T)/(sig*sqrt(T));d2=d1-sig*sqrt(T)
        V=s_*Nn(d1)-K*exp(-r*T)*Nn(d2)
        s_new=(S*N+V*n)/(N+n)
        if abs(s_new-s_)<1e-12: break
        s_=s_new
    return s_
def run(story,over=None,tag='x',coc=None):
    wb=openpyxl.load_workbook(ORIG);ws=wb['Input sheet']
    for k,v in {**COMMON,**STORY[story],**(over or {})}.items(): ws[k]=v
    for k,v in {**COC,**(coc or {})}.items(): wb['Cost of capital worksheet'][k]=v
    for k,v in ERP.items(): wb['Country equity risk premiums'][k]=v
    for k,v in RD.items(): wb['R& D converter'][k]=v
    I={**COMMON,**STORY[story],**(over or {})}
    d=f'{SP}/meli3/{tag}';os.makedirs(d,exist_ok=True);src=f'{d}/in.xlsx';wb.save(src)
    subprocess.run(['soffice','-env:UserInstallation=file://'+SP+'/meli3/prof_'+tag,'--headless','--calc','--convert-to','xlsx:Calc MS Excel 2007 XML','--outdir',d+'/out',src],capture_output=True,timeout=170)
    r=openpyxl.load_workbook(d+'/out/in.xlsx',data_only=True);vo=r['Valuation output'];ins=r['Input sheet'];cc=r['Cost of capital worksheet']
    return {'value':vo['B33'].value,'wacc0':ins['B35'].value,'wacc_t':vo['B17'].value,'beta':cc['C57'].value,'ubeta':cc['B23'].value,'erp':cc['B27'].value,'ke':cc['B13'].value,'opt':vo['B30'].value,'eq':vo['B31'].value,'op':vo['B24'].value,'m0':vo['B4'].value,'ebit0':vo['B5'].value,'roic0':vo['B40'].value,'rev5':vo['G3'].value,'kd':cc['B37'].value,'wd':None}
if __name__=='__main__':
    import json
    for s in ('base','cons','opt'): print(s,json.dumps(run(s,tag=s)))
    print('beta1.20',json.dumps(run('base',tag='alt',coc={'B21':'Direct Input','B22':1.2})))
