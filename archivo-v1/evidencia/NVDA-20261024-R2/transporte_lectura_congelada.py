"""Test transport: actual connector capture, no new network query or authentication.
Only active inside this isolated checkout. Financial control code is unchanged.
"""
import json,pathlib,re,sys,types
ROOT=pathlib.Path(__file__).parent;capture=json.loads((ROOT.parent.parent/'R2/reference/central_snapshot.json').read_text());data=capture['data'];sid=data['spreadsheetId'];grids={}
for s in data['sheets']:
 d={};grids[s['properties']['title']]=d
 for block in s.get('data',[]):
  for r,row in enumerate(block.get('rowData',[]),block.get('startRow',0)):
   for c,cell in enumerate(row.get('values',[]),block.get('startColumn',0)):d[(r,c)]=cell
def xy(a):
 m=re.fullmatch(r'([A-Z]+)(\d+)',a);c=0
 for x in m[1]:c=c*26+ord(x)-64
 return int(m[2])-1,c-1
class Sheet:
 def worksheets(self):return [types.SimpleNamespace(title=t)for t in grids]
 def values_get(self,address,params=None):
  tab,span=address.split('!');tab=tab.strip("'");ends=span.split(':');r0,c0=xy(ends[0]);r1,c1=xy(ends[-1]);covered=False
  for q in capture['ranges']:
   t,a=q.split('!');ends=a.split(':');y0,x0=xy(ends[0]);y1,x1=xy(ends[-1])
   if t.strip("'")==tab and y0<=r0<=r1<=y1 and x0<=c0<=c1<=x1:covered=True
  if not covered:raise ValueError('Rango no capturado: '+address)
  form=(params or {}).get('valueRenderOption')=='FORMULA';rows=[]
  for r in range(r0,r1+1):
   row=[]
   for c in range(c0,c1+1):
    cell=grids[tab].get((r,c),{});v=cell.get('userEnteredValue',{})if form else cell.get('effectiveValue',{});value=next(iter(v.values()),None)
    if isinstance(value,dict):raise ValueError('Error de fórmula capturado: '+address+' '+str(value))
    row.append('' if value is None else value)
   rows.append(row)
  return {'range':address,'values':rows}
 def values_batch_get(self,ranges,params=None):return {'valueRanges':[self.values_get(x,params)for x in ranges]}
class Client:
 capture=capture
 http_client=types.SimpleNamespace(request=lambda *a,**k:types.SimpleNamespace(json=lambda:{'revisions':[]}))
 def open_by_key(self,key):
  if key!=sid:raise FileNotFoundError('NOT_FOUND: hoja no capturada para este control acotado')
  return Sheet()
client=Client()
ms=types.ModuleType('model_steps')
def hoja_de(ticker):
 sys.path.insert(0,str(ROOT/'scripts'));from hoja_vigente import hoja_de as real
 return real(ticker,ROOT)
ms.hoja_de=hoja_de;ms.open_sheet=client.open_by_key;sys.modules['model_steps']=ms
pkg=types.ModuleType('jmr_valuation');pkg.__path__=[];io=types.ModuleType('jmr_valuation.io');io.__path__=[];auth=types.ModuleType('jmr_valuation.io.sheets_auth');auth.get_gspread_client=lambda:client;auth.open_target_sheet=lambda gc,key:gc.open_by_key(key)
sys.modules.update({'jmr_valuation':pkg,'jmr_valuation.io':io,'jmr_valuation.io.sheets_auth':auth})
print('CAPTURA CONECTOR R2: '+capture['capturedAt']+'; controles sobre lectura congelada, no consulta nueva; historial de revisiones no capturado.',file=sys.stderr)
