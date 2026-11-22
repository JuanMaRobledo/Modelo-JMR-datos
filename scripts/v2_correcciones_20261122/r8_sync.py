import json,sys,pathlib
from bs4 import BeautifulSoup
O=pathlib.Path(sys.argv[1]); INF=pathlib.Path('/home/user/Modelo-JMR-datos/jmr-v2/informes')
for t,rev in [('XRX','XRX-V2-LTM20260930-R2'),('NU','NU-V2-LTM20260930-R3')]:
    a=json.load(open(O/'analisis'/f'{t}.json')); hp=INF/t/f'{rev}_INFORME_FUNDAMENTAL.html'; s=BeautifulSoup(hp.read_text(),'html.parser')
    IMG=f'https://raw.githubusercontent.com/JuanMaRobledo/Modelo-JMR-datos/main/jmr-v2/imagenes/{t}/'
    for k,v in a['blocks'].items():
        if k=='perfil': continue
        sec=s.find('section',id=k); kick=sec.find('div',class_='kicker'); h1=sec.find('h1')
        for ch in list(sec.children):
            if ch not in (kick,h1): ch.extract()
        fr=BeautifulSoup(v.replace(IMG,f'../../imagenes/{t}/'),'html.parser')
        for q in fr.find_all('blockquote'): q.name='div'; q['class']='reading'
        sec.append(fr)
    hp.write_text(str(s),encoding='utf-8'); print(t,'ok')
