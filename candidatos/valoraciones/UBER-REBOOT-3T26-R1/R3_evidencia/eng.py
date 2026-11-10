import sys,subprocess,os,openpyxl
SP='/tmp/claude-0/-home-user/b8c0d315-1e6b-524a-8878-fb2b853781cf/scratchpad'
ORIG=SP+'/orig/fcffsimpleginzu.xlsx'
COMMON={'B3':46332,'B4':'Uber Technologies, Inc.','B7':'United States','B8':'Transportation','B9':'Transportation',
 'B11':56526,'B12':7034,'B13':502,'B14':28575,'B15':15664,'B16':'Yes','B17':'No','B18':10068,'B19':11473,'B20':1304,'B21':2107.437,'B22':68.59,'B23':0.2517,'B24':0.25,
 'B27':0.1408,'B30':5,'B34':0.0486,'B37':'Yes','B38':5.549,'B39':52.23,'B40':4.27,'B41':0.40,'B45':'No','B51':'No','B53':'V','B54':0.5,'B56':'No','B59':'No','B61':'No','B62':0,'B64':'No','B67':'Yes','B68':0.04,'B70':'No','B71':0,
 'C11':52017,'D11':1,'C12':5565,'C13':440,'C14':27918,'C15':10521,'C18':7633,'C19':9465,'C20':1042}
COC={'B21':'Direct Input','B22':1.2,'B25':'Operating regions','B32':7.5,'B33':'Direct input','B34':0.061,
 'G36':'Transportation','H36':29885,'G37':'Business & Consumer Services','H37':20693,'G38':'Trucking','H38':5948,
 'H21':None,'H22':6987,'H23':None,'H24':None,'H25':4091,'H26':None,'H27':None,'H28':29543,'H29':None,'H30':15905,'H31':None}
RD={'F6':3,'F7':4152,'B11':3402,'B12':3109,'B13':3164,'B14':None,'B15':None,'B16':None,'B17':None,'B18':None,'B19':None,'B20':None}
ERP={'B1':0.03387}
STORY={
 'base':{'B26':0.11,'B28':0.14,'B29':0.18,'B31':2.8,'B32':2.5,'B48':'Yes','B49':0.1323},
 'cons':{'B26':0.07,'B28':0.0975,'B29':0.13,'B31':2.0,'B32':1.8,'B48':'No','B49':0.1323},
 'opt':{'B26':0.13,'B28':0.1625,'B29':0.22,'B31':3.4,'B32':3.0,'B48':'Yes','B49':0.1821}}
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
    wb['Option value']['B17']=adjS(I['B22'],I['B39'],I['B40'],I['B41'],I['B34'],I['B38'],I['B21'])
    d=f'{SP}/uber3/{tag}';os.makedirs(d,exist_ok=True);src=f'{d}/in.xlsx';wb.save(src)
    subprocess.run(['soffice','-env:UserInstallation=file://'+SP+'/uber3/prof_'+tag,'--headless','--calc','--convert-to','xlsx:Calc MS Excel 2007 XML','--outdir',d+'/out',src],capture_output=True,timeout=170)
    r=openpyxl.load_workbook(d+'/out/in.xlsx',data_only=True);vo=r['Valuation output'];ins=r['Input sheet'];cc=r['Cost of capital worksheet']
    return {'value':vo['B33'].value,'wacc0':ins['B35'].value,'wacc_t':vo['B17'].value,'beta':cc['C57'].value,'ubeta':cc['B23'].value,'erp':cc['B27'].value,'ke':cc['B13'].value,'opt':vo['B30'].value,'eq':vo['B31'].value,'op':vo['B24'].value,'m0':vo['B4'].value,'ebit0':vo['B5'].value,'roic0':vo['B40'].value,'rev5':vo['G3'].value,'kd':cc['B37'].value,'wd':None}
if __name__=='__main__':
    import json
    for s in ('base','cons','opt'): print(s,json.dumps(run(s,tag=s)))
    print('beta1.20',json.dumps(run('base',tag='alt',coc={'B21':'Direct Input','B22':1.2})))
