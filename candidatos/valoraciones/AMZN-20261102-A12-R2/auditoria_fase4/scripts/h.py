import json,re,sys
C=json.load(open('/tmp/claude-0/-home-user/2f2cd7ae-4d2d-5320-a1b0-17e0c985a12e/scratchpad/amzn/captura_auditor.json'))
def ci(c):
    n=0
    for ch in c: n=n*26+ord(ch)-64
    return n-1
def addr(a):
    m=re.match(r'([A-Z]+)(\d+)',a); return int(m.group(2))-1, ci(m.group(1))
def g(tab,a,key='values'):
    r,c=addr(a); rows=C[key][tab]
    try: return rows[r][c]
    except IndexError: return None
def f(tab,a): return g(tab,a,'formulas')
def dump(tab,r0,r1,cols='ABCDEFGHIJKLMN',key='values',w=14):
    for r in range(r0,r1+1):
        row=[]
        for c in cols:
            v=g(tab,f'{c}{r}',key)
            if v in (None,''): v=''
            s=str(round(v,4) if isinstance(v,float) else v)
            row.append(s[:w])
        if any(row): print(r,' | '.join(row))
