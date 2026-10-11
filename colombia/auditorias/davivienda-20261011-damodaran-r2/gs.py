import os,json,sys
from google.oauth2 import service_account
from googleapiclient.discovery import build
info=json.loads(os.environ['GOOGLE_SERVICE_ACCOUNT_JSON_CONTENT'])
cr=service_account.Credentials.from_service_account_info(info,scopes=['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive'])
S=build('sheets','v4',credentials=cr,cache_discovery=False)
def titles(sid):
    m=S.spreadsheets().get(spreadsheetId=sid,fields='properties.title,sheets.properties(title,sheetId)').execute()
    return m
def vals(sid,rng):
    return S.spreadsheets().values().get(spreadsheetId=sid,range=rng).execute().get('values',[])
if __name__=='__main__':
    m=titles(sys.argv[1]); print(m['properties']['title']); print([s['properties']['title'] for s in m['sheets']])
