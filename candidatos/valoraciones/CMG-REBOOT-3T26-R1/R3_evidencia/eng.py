import sys,subprocess,os,openpyxl
SP='/tmp/claude-0/-home-user/b8c0d315-1e6b-524a-8878-fb2b853781cf/scratchpad'
ORIG=SP+'/orig/fcffsimpleginzu.xlsx'
COMMON={'B3':46332,'B4':'Chipotle Mexican Grill, Inc.','B7':'United States','B8':'Restaurant/Dining','B9':'Restaurant/Dining',
 'B11':12713.477,'B12':1794.941,'B13':0,'B14':2455.144,'B15':0,'B16':'No','B17':'No','B18':902.564,'B19':100.365,'B20':0,'B21':1270.149,'B22':34.43,'B23':0.2474,'B24':0.25,
 'B30':5,'B34':0.0486,'B37':'Yes','B38':12.268,'B39':39.51,'B40':4.2,'B41':0.35,'B45':'No','B53':'V','B54':0.5,'B56':'No','B59':'No','B61':'No','B62':0,'B64':'No','B67':'Yes','B68':0.04,'B70':'No','B71':0,
 'C11':11925.601,'D11':1,'C12':1935.798,'C13':0,'C14':2830.607,'C15':0,'C18':1049.136,'C19':197.123,'C20':0,'B51':'No'}
COC={'B21':'Single Business(US)','B32':7,'B33':'Direct input','B34':0.0586,'B25':'Operating regions','H28':12713.477,
 'H21':None,'H22':None,'H23':None,'H24':None,'H25':None,'H26':None,'H27':None,'H29':None,'H30':None,'H31':None,'H36':None,'H37':None,'H38':None,'G36':None,'G37':None,'G38':None}
ERP={'B1':0.03387}
STORY={
 'base':{'B26':0.095,'B27':0.1412,'B28':0.088,'B29':0.16,'B31':2.7,'B32':2.9,'B48':'Yes','B49':0.1836},
 'cons':{'B26':0.064,'B27':0.1412,'B28':0.064,'B29':0.13,'B31':2.2,'B32':2.4,'B48':'No','B49':0.1836},
 'opt':{'B26':0.11,'B27':0.1412,'B28':0.109,'B29':0.18,'B31':2.9,'B32':3.2,'B48':'Yes','B49':0.1836}}
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
    I={**COMMON,**STORY[story],**(over or {})}
    wb['Option value']['B17']=adjS(I['B22'],I['B39'],I['B40'],I['B41'],I['B34'],I['B38'],I['B21'])
    d=f'{SP}/cmg3/{tag}';os.makedirs(d,exist_ok=True);src=f'{d}/in.xlsx';wb.save(src)
    subprocess.run(['soffice','-env:UserInstallation=file://'+SP+'/cmg3/prof_'+tag,'--headless','--calc','--convert-to','xlsx:Calc MS Excel 2007 XML','--outdir',d+'/out',src],capture_output=True,timeout=170)
    r=openpyxl.load_workbook(d+'/out/in.xlsx',data_only=True);vo=r['Valuation output'];ins=r['Input sheet'];cc=r['Cost of capital worksheet']
    return {'value':vo['B33'].value,'wacc0':ins['B35'].value,'wacc_t':vo['B17'].value,'beta':cc['C57'].value,'ubeta':cc['B23'].value,'erp':cc['B27'].value,'ke':cc['B13'].value,'opt':vo['B30'].value,'eq':vo['B31'].value,'op':vo['B24'].value}
if __name__=='__main__':
    for s in ('base','cons','opt'): print(s,run(s,tag=s))
