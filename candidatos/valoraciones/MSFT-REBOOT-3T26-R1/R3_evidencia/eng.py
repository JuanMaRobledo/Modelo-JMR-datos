import sys,subprocess,os,openpyxl
SP='/tmp/claude-0/-home-user/b8c0d315-1e6b-524a-8878-fb2b853781cf/scratchpad'
ORIG=SP+'/orig/fcffsimpleginzu.xlsx'
COMMON={'B3':46332,'B4':'Microsoft Corporation','B7':'United States','B8':'Software (System & Application)','B9':'Software (System & Application)',
 'B11':346445,'B12':163191,'B13':3223,'B14':470509,'B15':106454,'B16':'Yes','B17':'No','B18':64509,'B19':37808,'B20':0,'B21':7504.195,'B22':530.61,'B23':0.1968,'B24':0.23,
 'B27':0.4824,'B30':5,'B34':0.0486,'B37':'No','B38':0,'B39':0,'B40':0,'B41':0,'B45':'No','B51':'No','B53':'V','B54':0.5,'B56':'No','B59':'No','B61':'No','B62':0,'B64':'No','B67':'Yes','B68':0.04,'B70':'No','B71':0,
 'C11':331839,'D11':1,'C12':155237,'C13':3051,'C14':442387,'C15':106888,'C18':76843,'C19':36348,'C20':0}
COC={'B11':'Detailed','B21':'Multibusiness(US)','B25':'Operating regions','B32':8,'B33':'Direct Input','B34':0.052,
 'G36':'Software (System & Application)','H36':76795,'G37':'Computers/Peripherals','H37':15484,'G38':None,'H38':None,'G39':None,'H39':None,
 'H21':None,'H22':None,'H23':None,'H24':None,'H25':None,'H26':None,'H27':None,'H28':170794,'H29':None,'H30':None,'H31':161045}
RD={'F6':3,'F7':36463,'B11':35562,'B12':32488,'B13':29510,'B14':None,'B15':None,'B16':None,'B17':None,'B18':None,'B19':None,'B20':None}
ERP={'B1':0.03387}
STORY={
 'base':{'B26':0.18,'B28':0.14,'B29':0.46,'B31':0.8,'B32':1.2,'B48':'Yes','B49':0.18},
 'cons':{'B26':0.13,'B28':0.07,'B29':0.40,'B31':0.55,'B32':0.9,'B48':'No','B49':0.18},
 'opt':{'B26':0.21,'B28':0.17,'B29':0.49,'B31':1.1,'B32':1.5,'B48':'Yes','B49':0.26}}
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
    d=f'{SP}/msft3/{tag}';os.makedirs(d,exist_ok=True);src=f'{d}/in.xlsx';wb.save(src)
    subprocess.run(['soffice','-env:UserInstallation=file://'+SP+'/msft3/prof_'+tag,'--headless','--calc','--convert-to','xlsx:Calc MS Excel 2007 XML','--outdir',d+'/out',src],capture_output=True,timeout=170)
    r=openpyxl.load_workbook(d+'/out/in.xlsx',data_only=True);vo=r['Valuation output'];ins=r['Input sheet'];cc=r['Cost of capital worksheet']
    return {'value':vo['B33'].value,'wacc0':ins['B35'].value,'wacc_t':vo['B17'].value,'beta':cc['C57'].value,'ubeta':cc['B23'].value,'erp':cc['B27'].value,'ke':cc['B13'].value,'opt':vo['B30'].value,'eq':vo['B31'].value,'op':vo['B24'].value,'m0':vo['B4'].value,'ebit0':vo['B5'].value,'roic0':vo['B40'].value,'rev5':vo['G3'].value,'kd':cc['B37'].value,'wd':None}
if __name__=='__main__':
    import json
    for s in ('base','cons','opt'): print(s,json.dumps(run(s,tag=s)))
    print('beta1.20',json.dumps(run('base',tag='alt',coc={'B21':'Direct Input','B22':1.2})))
