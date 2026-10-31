#!/usr/bin/env python3
"""Separate existing cycle discussion and build a linked N1 index. No financial edits."""
import copy
import json
import re
from html import escape
from html.parser import HTMLParser
from pathlib import Path


class Element:
    def __init__(self, tag, attrs, start, parent):
        self.tag, self.attrs, self.start, self.parent = tag, dict(attrs), start, parent
        self.open_end = self.end = None


class Document(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=False)
        self.text, self.nodes, self.stack = text, [], []
        self.lines = [0]
        self.lines.extend(m.end() for m in re.finditer('\n', text))
        self.feed(text)

    def position_offset(self):
        line, col = self.getpos()
        return self.lines[line - 1] + col

    def handle_starttag(self, tag, attrs):
        node = Element(tag, attrs, self.position_offset(), self.stack[-1] if self.stack else None)
        node.open_end = node.start + len(self.get_starttag_text())
        self.nodes.append(node)
        if tag not in {'br', 'hr', 'img', 'input', 'meta', 'link', 'wbr', 'source', 'area', 'base', 'col', 'embed', 'param', 'track'}:
            self.stack.append(node)
        else:
            node.end = node.open_end

    def handle_endtag(self, tag):
        for i in range(len(self.stack)-1, -1, -1):
            if self.stack[i].tag == tag:
                node = self.stack[i]
                node.end = self.text.find('>', self.position_offset()) + 1
                del self.stack[i:]
                break


ENGINES = {
 'MELI': 'El comercio electrónico crece con compradores, frecuencia, vendedores, logística y publicidad; los servicios financieros, con pagos, saldos y crédito. Los dos negocios consumen capital y asumen riesgos diferentes. El volumen comercial no debe confundirse con ingresos ni la expansión de cartera con caja libre. La contribución de crédito exige separar pérdidas, fondeo y capital retenido del flujo del comercio, manteniendo trazabilidad del perímetro que valora esta revisión.',
 'SHAK': 'La expansión de Shacks propios, las licencias y las ventas comparables son motores distintos. Las aperturas corporativas exigen inversión y gastos de arranque; las licencias generan regalías con otra intensidad de capital. La frecuencia y el ticket deben analizarse por separado para distinguir demanda de aumentos de precio. El volumen incremental solo crea valor si compensa alquileres, trabajo, alimentos y capital comprometido durante la maduración de cada cohorte.',
 'UBER': 'La frecuencia de los usuarios, la disponibilidad de conductores y comercios, y la conversión entre movilidad y reparto determinan la expansión de la plataforma. Reservas brutas, viajes e ingreso contable no son equivalentes: cambian con precios, mezcla geográfica y forma de reconocer ingresos. La expansión de publicidad y servicios complementarios debe evaluarse por contribución operativa y costo de adquisición, sin atribuir a toda la facturación la rentabilidad de un servicio de software.',
 'AFYA': 'El crecimiento depende de cupos médicos autorizados, ocupación, matrícula y avance de las cohortes. Ampliar capacidad consume docentes, instalaciones y convenios antes de completar ingresos de todos los cursos. La formación continua y las soluciones para médicos tienen economías diferentes del pregrado. La proyección standalone conserva ese perímetro; no incorpora ingresos ni sinergias de YDUQS por la sola existencia de un acuerdo de fusión.',
 'DUOL': 'La expansión combina usuarios activos, retención, conversión a suscripción y mezcla de planes. Un mayor número de usuarios gratuitos puede ampliar el embudo, pero también el costo de atender sesiones. Las reservas de suscripción y el ingreso reconocido tienen calendarios diferentes. Matemáticas, música y nuevas herramientas amplían el uso potencial; la valoración exige monetización y permanencia, sin contar cada lanzamiento como una nueva fuente de ingresos ya demostrada.',
 'ADBE': 'La renovación de suscripciones, la expansión de cuentas y la monetización de herramientas creativas y documentales sostienen la proyección. La inteligencia artificial puede aumentar utilidad y consumo, pero también costo por generación y competencia. Deben distinguirse crecimiento de asientos, precio y consumo adicional. Convertir uso en ingresos exige comprobar retención y margen después del costo de inferencia, sin capitalizar dos veces el mismo beneficio en ventas y rentabilidad.',
 'BSX': 'El crecimiento debe explicarse por procedimientos, penetración de dispositivos, mezcla de productos y adquisiciones. La innovación médica requiere evidencia clínica, aprobación regulatoria y capacidad de distribución. Una compra aumenta el perímetro y el capital comprometido; sus ventas no equivalen a crecimiento orgánico. La proyección existente se conserva y debe contrastarse con adopción, márgenes y conversión a caja del portafolio que efectivamente pertenece a esta revisión.',
 'CELH': 'La demanda del consumidor, la distribución, la disponibilidad en puntos de venta y la mezcla de marcas impulsan las ventas. Los despachos a distribuidores pueden adelantarse al consumo final. La expansión geográfica y del portafolio debe traducirse en reposición y margen después de promociones, logística y acuerdos comerciales. La capacidad de vender más con el mismo capital no debe confundirse con financiación gratuita permanente de inventarios y cuentas por cobrar.',
 'CMG': 'Las aperturas, las ventas comparables y el formato de cada restaurante explican la expansión. El tráfico aporta una señal distinta al ticket y a los aumentos de precio. Una nueva unidad consume construcción, equipamiento y gastos preoperativos antes de alcanzar una productividad madura. La mejora de margen depende de ejecución, volumen y costos; no debe extrapolarse automáticamente del restaurante al EBIT consolidado después de gastos centrales.',
 'NFLX': 'Las membresías, la mezcla de planes, los precios y la monetización publicitaria determinan el avance del ingreso. El consumo de contenido no equivale por sí solo a facturación adicional. La inversión en programación y el calendario de amortización deben acompañar la expansión sin duplicar el costo de contenido. Las nuevas ofertas solo añaden valor si mejoran retención, adquisición o ingreso por cliente después de sus costos incrementales.',
 'GOOGL': 'La publicidad en búsqueda y video, la nube y las suscripciones tienen motores y necesidades de capital diferentes. El uso de inteligencia artificial puede cambiar la forma de consultar, los costos de respuesta y la monetización. La infraestructura necesaria se evalúa como inversión que debe producir flujo futuro; no se presume que todo gasto de IA sea investigación ni que cada dólar de capacidad produzca ingresos inmediatos.',
 'MSFT': 'Las suscripciones empresariales, la nube y las nuevas herramientas de productividad combinan crecimiento de usuarios, consumo y precio. La capacidad de centros de datos debe financiarse antes de monetizarse plenamente. La adopción de asistentes no equivale automáticamente a margen incremental: importa el costo de inferencia, la utilización y la retención de contratos. La valoración conserva los supuestos registrados, sin añadir ingresos hipotéticos por cada anuncio de producto.',
 'NKE': 'El volumen, el precio, la mezcla de canales y la recuperación de demanda de producto explican el ingreso. Vender directamente cambia margen bruto y gastos de distribución; no garantiza un mayor margen operativo. Inventarios, descuentos y relaciones con distribuidores condicionan la conversión a caja. La recuperación requiere que innovación y demanda reduzcan promociones sin elevar de forma permanente el capital inmovilizado en existencias.',
 'PYPL': 'El volumen procesado, la frecuencia, la mezcla entre servicios y el rendimiento neto por transacción explican los ingresos. Un volumen mayor puede acompañarse de menor monetización o mayores costos. La aceptación del comercio y el uso recurrente deben traducirse en contribución después de pérdidas, procesamiento e incentivos. La expansión no se valora solo por cuentas registradas: importan actividad, retención y productividad del gasto comercial.',
 'EPAM': 'El gasto tecnológico de los clientes, las horas facturables, la utilización de profesionales y las tarifas explican el crecimiento. Una contratación adelantada a la demanda presiona margen; una utilización muy alta puede limitar entregas y calidad. La inteligencia artificial puede cambiar productividad y forma de cobrar. Debe distinguirse recuperación del presupuesto de clientes de una mejora estructural del valor económico capturado por empleado.',
 'ZTS': 'El número de animales atendidos, el gasto por tratamiento, el precio y la mezcla de productos determinan las ventas. Los tratamientos recurrentes y los lanzamientos tienen perfiles distintos de adopción y riesgo. La innovación necesita evidencia y acceso a canales veterinarios. El crecimiento debe convertirse en margen y flujo después de fabricación, comercialización e investigación, sin asignar a productos todavía inciertos la economía de una cartera consolidada.',
 'ONON': 'La ampliación de distribución, la venta directa, las categorías y la repetición de compra sostienen el crecimiento. El atractivo de marca debe contrastarse con volumen a precio completo y rotación, no solo con presencia geográfica. El canal directo consume logística y capital comercial. La expansión de inventario puede adelantarse a la demanda; la productividad del capital y el margen deben evaluarse conjuntamente al aumentar escala.',
 'NU': 'La ampliación de clientes activos, el uso de productos y el ingreso por cliente determinan la expansión bancaria. El crédito necesita capital regulatorio, fondeo y absorción de pérdidas. Crecer cartera no equivale a crecer flujo disponible para accionistas. La monetización debe evaluarse después del costo de depósitos, provisiones y capital retenido, usando ROE y FCFE bancario, sin trasladar mecánicamente Sales-to-Capital industrial a intermediación financiera.',
 'NVO': 'El volumen tratado, el acceso, la capacidad productiva y los precios netos determinan el crecimiento. La demanda clínica no equivale a ventas realizables si faltan capacidad o cobertura. Las inversiones industriales preceden a la monetización y compiten con cambios de precio y nuevos tratamientos. La valoración debe distinguir expansión de pacientes, mezcla y precio, manteniendo el costo de fabricar y distribuir la capacidad adicional.',
 'INTU': 'La retención, la incorporación de clientes, la mezcla de soluciones y la monetización de servicios asociados explican el ingreso. Las líneas de impuestos, contabilidad y finanzas tienen calendarios y factores competitivos diferentes. Las herramientas automatizadas pueden mejorar utilidad y productividad, pero requieren gasto de producto y adquisición. La expansión debe convertirse en flujo después de desarrollo y remuneración en acciones; no basta con crecimiento de ingresos recurrentes.',
}


def standardize(a):
    before = copy.deepcopy(a)
    h = a['articleHtml']
    if 'data-jmr-n1-standard="14-20261031"' in h:
        return a
    h = re.sub(r'<h3>Índice</h3>\s*<p>1\. Tesis de inversión y conclusión;[\s\S]*?</p>', '', h)
    doc = Document(h)
    headings = [n for n in doc.nodes if n.tag == 'h2' and re.match(r'\s*\d+\.', h[n.open_end:n.end])]
    assert len(headings) == 13, a['ticker']
    h4, h5 = headings[3:5]
    cycle_heads = [n for n in doc.nodes if n.attrs.get('id') == 'jmr-ciclo-empresa']
    edits = []
    if a['ticker'] == 'UBER':
        start, end = h4.end, h5.start
    elif a['ticker'] == 'SHAK':
        start = cycle_heads[0].start
        end = h.rfind('</section>', start, h5.start)
        assert end > start
    else:
        node = cycle_heads[0].parent
        assert node.tag == 'section' and node.end is not None
        start, end = node.start, node.end
    cycle = h[start:end]
    # Remove only the cycle span; keep all other narrative and original anchors.
    edits.append((start, end, ''))
    for nav in [n for n in doc.nodes if n.tag == 'nav']:
        assert nav.end is not None
        edits.append((nav.start, nav.end, ''))
    labels = []
    for i, node in enumerate(headings, 1):
        old = re.sub('<[^>]+>', '', h[node.open_end:node.end].rsplit('</h2>', 1)[0]).strip()
        title = re.sub(r'^\d+\.\s*', '', old)
        number = i if i < 5 else i + 1
        if i == 4:
            title = 'Motores del crecimiento futuro'
        labels.append((number, title))
        opening = h[node.start:node.open_end]
        assert ' id=' not in opening, (a['ticker'], opening)
        opening = opening[:-1] + f' id="jmr-n1-chapter-{number}">'
        edits.append((node.start, node.end, opening + f'{number}. {title}</h2>'))
    # Insert chapter five immediately before the old chapter five's wrapper.
    insertion = h5.parent.start if h5.parent.tag == 'section' and h5.parent.attrs.get('class') == 'jmr-v19-chapter' else h5.start
    chapter = '<section class="jmr-v19-chapter" id="jmr-n1-cycles"><h2 id="jmr-n1-chapter-5">5. Ciclos empresariales, macroeconómicos y de mercado</h2>' + cycle + '</section>\n'
    edits.append((insertion, insertion, chapter))
    edits.append((h4.end, h4.end, '<p data-jmr-growth-20261031="'+a['ticker']+'">'+ENGINES[a['ticker']]+'</p>'))
    for start, end, replacement in sorted(edits, key=lambda e:(e[0], e[1]), reverse=True):
        h = h[:start] + replacement + h[end:]
    labels.append((5, 'Ciclos empresariales, macroeconómicos y de mercado'))
    index = '<nav aria-label="Índice del análisis fundamental" data-jmr-n1-standard="14-20261031"><ol>' + ''.join(f'<li><a href="#jmr-n1-chapter-{i}">{i}. {escape(title)}</a></li>' for i,title in sorted(labels)) + '</ol></nav>'
    first = h.index('<h2')
    # Keep the index outside the first chapter wrapper.
    fresh = Document(h)
    firstnode = next(n for n in fresh.nodes if n.tag == 'h2' and n.attrs.get('id') == 'jmr-n1-chapter-1')
    first = firstnode.start
    if firstnode.parent.tag == 'section' and firstnode.parent.attrs.get('class') == 'jmr-v19-chapter':
        first = firstnode.parent.start
    h = h[:first] + index + h[first:]
    a['articleHtml'] = h
    a['html'] = h + a.get('calculationHtml', '')
    a['estandarizacionEditorial20261031'] = {'nivel1Capitulos':14,'indiceInteractivo':True,'ciclosSeparados':True,'calculosModificados':False,'auditoriaEconomicaEjecutada':False,'completitudInvestigacion':'PENDIENTE'}
    if 'editorialN21' in a:
        a['editorialN21']['chapters'] = 14
    c = a.get('controlCobertura', {})
    if 'articleChapters' in c:
        c['articleChapters'] = 14
    if c.get('niveles') == 'N1_13_N2_12':
        c['niveles'] = 'N1_14_N2_12_PENDIENTE_VALIDACION_CONTENIDO'
    assert a['calculationHtml'] == before['calculationHtml']
    for k in before.keys() - {'articleHtml','html','editorialN21','controlCobertura'}:
        assert a[k] == before[k], k
    nums = re.findall(r'<h2[^>]*>\s*(\d+)\.', h)
    assert nums == list(map(str, range(1,15))), (a['ticker'], nums)
    assert h.count(cycle) == 1
    assert all(h.count(f'id="jmr-n1-chapter-{i}"') == 1 for i in range(1,15))
    return a


if __name__ == '__main__':
    root = Path(__file__).resolve().parent.parent
    catalog=json.loads((root/'catalogo.json').read_text())
    for p in sorted(root/path for path in catalog['analisis']):
        a = json.loads(p.read_text())
        if a.get('version_metodo') != 'A-1.2':
            continue
        result = standardize(a)
        p.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
        print(a['ticker'], '14 capítulos, índice y ciclos separados')
