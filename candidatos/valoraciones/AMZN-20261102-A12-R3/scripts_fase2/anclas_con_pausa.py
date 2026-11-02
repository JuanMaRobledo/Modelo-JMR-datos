"""Ejecuta scripts/multiples_anchors.py sin modificarlo, envolviendo peer_multiples con pausas y reintentos por el límite de Yahoo."""
import sys, time, runpy
sys.path[:0]=['/home/user/JMR-valuation','/home/user/JMR-valuation/scripts']
import multiples_anchors as ma
_orig=ma.peer_multiples
def lento(ticker, *a, **k):
    for intento in range(5):
        time.sleep(15)
        try:
            return _orig(ticker,*a,**k)
        except Exception as e:
            if 'Too Many Requests' not in str(e) and 'Rate' not in str(e): raise
            print(f'  {ticker}: límite de Yahoo, reintento {intento+1}', flush=True); time.sleep(45)
    return _orig(ticker,*a,**k)
ma.peer_multiples=lento
sys.argv=['multiples_anchors.py']+sys.argv[1:]
ma.main() if hasattr(ma,'main') else runpy.run_path('/home/user/JMR-valuation/scripts/multiples_anchors.py',run_name='__main__')
