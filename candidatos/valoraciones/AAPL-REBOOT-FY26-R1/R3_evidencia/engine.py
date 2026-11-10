import sys,subprocess,shutil,os,openpyxl,tempfile
SP='/tmp/claude-0/-home-user/b8c0d315-1e6b-524a-8878-fb2b853781cf/scratchpad'
ORIG=SP+'/orig/fcffsimpleginzu.xlsx'
COMMON_INPUT={  # Input sheet col B
 'B3':46332,'B4':'Apple Inc.','B7':'United States','B8':'Computers/Peripherals','B9':'Computers/Peripherals',
 'B11':478834,'B12':158063,'B13':3000,'B14':112093,'B15':94479,'B16':'Yes','B17':'No','B18':136935,'B19':0,'B20':0,'B21':14590.6,'B22':342.37,'B23':0.1699,'B24':0.25,
 'B34':0.0486,'B37':'No','B38':0,'B39':0,'B40':0,'B41':0,'B45':'No','B53':'V','B54':0.6,'B56':'No','B59':'No','B61':'No','B62':0,'B64':'No','B67':'Yes','B68':0.04,'B70':'No','B71':0,
 'C11':416161,'D11':1,'C12':133050,'C13':3500,'C14':73733,'C15':112377,'C18':132420,'C19':0,'C20':0}
COC={'B21':'Multibusiness(US)','B32':7,'B33':'Actual rating','B35':'Aa2/AA','G36':'Computers/Peripherals','H36':319956,'G37':'Electronics (General)','H37':35577,'G38':'Software (System & Application)','H38':123301,'G39':None,'H39':None,'G40':None,'H40':None,'G41':None,'H41':None,
 'H21':None,'H22':153147,'H23':None,'H24':None,'H25':None,'H26':None,'H27':None,'H28':198083,'H29':127604,'H30':None,'H31':None,'G5':None,'H5':None,'G6':None,'H6':None,'G16':None,'H16':None,'G52':None,'H52':None}
RD={'F6':5,'F7':45765,'B11':34550,'B12':31370,'B13':29915,'B14':26251,'B15':21914,'B16':None,'B17':None,'B18':None,'B19':None,'B20':None}
ERP={'B1':0.03387}
STORY={
 'base':{'B26':0.06,'B27':0.366,'B28':0.055,'B29':0.37,'B30':5,'B31':3.0,'B32':3.0,'B48':'Yes','B49':0.4476,'B51':'No','B52':0.05},
 'cons':{'B26':0.025,'B27':0.355,'B28':0.02,'B29':0.31,'B30':5,'B31':2.4,'B32':2.4,'B48':'No','B49':0.4476,'B51':'Yes','B52':0.05},
 'opt':{'B26':0.09,'B27':0.37,'B28':0.08,'B29':0.40,'B30':5,'B31':3.5,'B32':3.5,'B48':'Yes','B49':0.4476,'B51':'No','B52':0.05}}
def run(story,over=None,tag='x',coc=None):
    wb=openpyxl.load_workbook(ORIG)
    ws=wb['Input sheet']
    for k,v in {**COMMON_INPUT,**STORY[story],**(over or {})}.items(): ws[k]=v
    for k,v in {**COC,**(coc or {})}.items(): wb['Cost of capital worksheet'][k]=v
    for k,v in RD.items(): wb['R& D converter'][k]=v
    for k,v in ERP.items(): wb['Country equity risk premiums'][k]=v
    d=f'{SP}/lo/{tag}';os.makedirs(d,exist_ok=True)
    src=f'{d}/in.xlsx';wb.save(src)
    subprocess.run(['soffice','-env:UserInstallation=file://'+SP+'/lo/prof_'+tag,'--headless','--calc','--convert-to','xlsx:Calc MS Excel 2007 XML','--outdir',d+'/out',src],capture_output=True,timeout=170)
    r=openpyxl.load_workbook(d+'/out/in.xlsx',data_only=True)
    vo=r['Valuation output'];ins=r['Input sheet']
    return {'value':vo['B33'].value,'wacc0':ins['B35'].value,'wacc_term':vo['B17'].value,'ebit_adj':vo['B5'].value,'margin0':vo['B4'].value,'tv':vo['B19'].value,'sumpv':vo['B21'].value}
if __name__=='__main__':
    for s in ('base','cons','opt'):
        print(s,run(s,tag=s))
