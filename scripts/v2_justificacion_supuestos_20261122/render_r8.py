import sys,pathlib,fitz
from weasyprint import HTML, default_url_fetcher
ROOT=pathlib.Path('/home/user/Modelo-JMR-datos')
def fetch(url):
    url=url.replace('file:///home/runner/work/Modelo-JMR-datos/Modelo-JMR-datos/','file://'+str(ROOT)+'/')
    return default_url_fetcher(url)
def render(html_path,pdf_path):
    html_path=pathlib.Path(html_path)
    HTML(string=html_path.read_text(encoding='utf-8'),base_url=html_path.resolve().as_uri(),url_fetcher=fetch).write_pdf(pdf_path)
    with fitz.open(pdf_path) as d: return len(d)
if __name__=='__main__':
    print(render(sys.argv[1],sys.argv[2]))
