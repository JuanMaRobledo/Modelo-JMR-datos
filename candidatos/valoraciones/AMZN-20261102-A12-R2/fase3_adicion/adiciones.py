"""Adiciones de fase 3 (AMZN R2): Anthropic y OpenAI en N1 (cap. 2, 8, 11, 12, 13, 14) y N2 (apartado 4).
Las cifras derivadas se formatean desde cifras.json (calculado desde el 10-Q y el JSON de la revisión); no se escriben a mano."""
import json, html
C = json.load(open('/tmp/claude-0/-home-user/2f2cd7ae-4d2d-5320-a1b0-17e0c985a12e/scratchpad/amzn/f3/cifras.json'))
n, d, base = C['n'], C['d'], C['base']

def m(x):  # millones con punto de miles
    return f"{x:,.0f}".replace(',', '.')
def u(x, k=2):  # decimales con coma
    return f"{x:,.{k}f}".replace(',', 'X').replace('.', ',').replace('X', '.')
def p(x, k=1):
    return u(100 * x, k) + ' %'

Q = 'https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm'
SRC = '[10-Q T3-26, nota 2]'

CAP2 = f"""### 2B. Anthropic y OpenAI: participadas, clientes y socios

Amazon mantiene con Anthropic y con OpenAI una relación doble que el lector debe separar: son clientes de AWS con compromisos plurianuales y, a la vez, empresas en las que Amazon invirtió capital propio. En Anthropic, Amazon compró entre el T3 de 2023 y el T4 de 2025 notas convertibles por 8.000 millones de dólares. Al 30 de septiembre de 2026, las notas que aún conserva figuraban a un valor razonable de {m(n['notas'])} millones, con una ganancia no realizada de {m(n['gan_notas'])} millones registrada en otro resultado integral. Parte de las notas se convirtió en acciones preferentes sin voto, y en el T2 de 2026 Amazon invirtió además 5.000 millones en la Serie G y 5.000 millones en la Serie H. Las preferentes figuraban por {m(n['pref'])} millones (164 millones de acciones, cada una convertible en diez acciones comunes sin voto). Las notas están sujetas a un tope de participación del 12 %, renunciable por Amazon, y sin ese tope se convertirían en unos 184 millones de preferentes. El acuerdo financiero del T2 de 2026 pone a disposición de Anthropic hasta 20.000 millones, que se habilitan a medida que AWS entrega capacidad de cómputo comprometida; tras la Serie H quedan 15.000 millones. {SRC}

En OpenAI la relación nació en el T1 de 2026. Ese trimestre se firmaron un acuerdo comercial de servicios de AWS, que incluye el uso y el desempeño de los chips propios de AWS, y un acuerdo de colaboración que pone modelos de OpenAI a disposición de Amazon y de los clientes de AWS. El compromiso comercial existente de 38.000 millones se amplió en 100.000 millones a ocho años. Amazon compró preferentes Serie C por 50.000 millones (15.000 en el T1, 13.700 en el T2 y 21.300 en el T3). En el T2, AWS y Anthropic ampliaron también su colaboración en más de 100.000 millones a diez años. {SRC}

La consecuencia económica es que una parte relevante de la demanda futura de AWS proviene de dos laboratorios de IA cuyo capital financia, en parte, el propio Amazon. Solo en 2026 Amazon desembolsó {m(n['inv26'])} millones en estas participaciones. Eso no vuelve ficticios los ingresos, porque los contratos son obligaciones exigibles, pero sí exige leer el backlog de AWS con cautela. Las obligaciones de desempeño no reconocidas suman 578.000 millones, {u(d['backlog_x'], 1)} veces los ingresos de AWS de los últimos doce meses, y el 10-Q no las desglosa por cliente: la concentración en Anthropic y OpenAI es **N/D** con la información pública. Amazon declara que ambas son entidades de interés variable que no consolida, y que su exposición máxima a pérdidas equivale al valor contable más los compromisos futuros de financiación. {SRC}

El resultado contable también depende de ellas. En los nueve meses de 2026, «otros ingresos» sumó {m(n['otros9m'])} millones, casi todo por revaluación de las preferentes de Anthropic ({m(n['ajuste_pref9m'])} millones), y la provisión fiscal incluyó {m(n['disc_tax'])} millones de impuesto discreto por esa causa. Esos otros ingresos representan {p(d['share_otros_pre'], 0)} de la utilidad antes de impuestos del periodo. Por eso este estudio mide la rentabilidad con el EBIT y trata las participaciones fuera del negocio operativo (capítulos 6, 9 y 11). [10-Q T3-26, notas 2 y 7; N2.4]
"""

CAP8 = f"""**Asignación de capital en participaciones de IA.** El capital destinado a Anthropic y OpenAI en 2026 ({m(n['inv26'])} millones) equivale a {p(n['inv26']/220000, 0)} de los cerca de 220.000 millones de capex en efectivo que Amazon prevé para 2026 (10-Q, guía), y se suma a compromisos de financiación todavía abiertos (15.000 millones disponibles para Anthropic). Las participaciones no dan control: son preferentes o comunes sin voto, con tope de 12 % en Anthropic, y no se consolidan. El juicio de gobierno depende de que esas inversiones se evalúen por su retorno propio y no solo como herramienta para asegurar demanda de AWS, y de que la empresa siga informando por separado su valor, sus derechos y sus restricciones de liquidez. {SRC}
"""

CAP11 = f"""**Peso de Anthropic y OpenAI en el valor.** La revisión suma al patrimonio {m(294595)} millones de activos no operativos, excluidos del capital operativo (`Input sheet!B83:B84`). De ese total, {m(d['anth'])} millones corresponden a Anthropic ({p(d['anth_share_nonop'], 0)}) y {m(n['openai'])} millones a OpenAI. En términos por acción, son {u(d['nonop_ps'])} USD del valor Base de {u(base)} USD, un {p(d['peso_base'])}: {u(d['anth_ps'])} USD por Anthropic y {u(d['oa_ps'])} USD por OpenAI. El importe es el valor contable reportado, de nivel 3, sin descuento adicional y **sin restar el impuesto diferido**. Solo por las notas de Anthropic, ese impuesto diferido es de {m(n['dtl'])} millones, {u(d['dtl_ps'])} USD por acción. Los diagnósticos de la revisión muestran que con las participaciones un 20 % más bajas la Base sería {u(d['m20'])} USD, y con un 50 % menos, {u(d['m50'])} USD. Ninguna de esas cifras sustituye el valor oficial; la reserva sigue abierta. [JSON R2: `ajustes_diagnosticos`; N2.4]
"""

CAP12 = f"""**Riesgo correlacionado de las participadas de IA.** La tesis bajista más seria sobre Anthropic y OpenAI es que su riesgo no es independiente del de AWS. Si la monetización de la IA decepciona, caerían a la vez el consumo comprometido de esos clientes, la utilización de la capacidad recién construida y el valor razonable de las participaciones. En la historia Disrupción de esta revisión, sin embargo, los no operativos se mantienen en {m(294595)} millones. Como ilustración aritmética, no como valor oficial: con un recorte de 50 % de esas participaciones, la Disrupción pasaría de {u(d['dis'])} a {u(d['dis50'])} USD por acción. Otros riesgos son las valoraciones de nivel 3, que se basan en rondas de financiación y descuentos por falta de liquidez; los periodos de bloqueo tras una eventual salida a bolsa; el tope de 12 % en Anthropic; y la posible concentración del backlog de AWS, que no se puede medir con datos públicos. {SRC}
"""

CAP13 = f"""**Seguimiento de Anthropic y OpenAI.** Señales verificables cada trimestre en el 10-Q (nota 2): (1) el valor razonable de las notas y las preferentes de Anthropic y de la Serie C de OpenAI, y los ajustes en «otros ingresos»; (2) el saldo dispuesto y disponible de la línea de 20.000 millones para Anthropic (hoy 15.000 disponibles); (3) nuevas rondas, salidas a bolsa o eventos de liquidez, que convertirían las preferentes y abrirían periodos de bloqueo; (4) la evolución del backlog de AWS (578.000 millones al 30-sep-2026) frente a sus ingresos. Un deterioro de las participaciones de 20 % o más, o una caída del backlog, es motivo para revisar el puente patrimonial y las historias, no para añadir una prima al WACC.
"""

CAP14 = """**Adición del 2-nov-2026 sobre Anthropic y OpenAI.** Los subapartados 2B, 8, 11, 12 y 13 sobre Anthropic y OpenAI, y la tabla N2.4, se añadieron después de la auditoría económica de fase 4 (hallazgo C-08), a pedido del usuario y **en la misma sesión que auditó la revisión**. Las cifras provienen del 10-Q del T3 de 2026 (nota 2, notas 4 y 7) y del JSON de la revisión. Las cifras por acción y los porcentajes se generaron por código (`fase3_adicion/adiciones.py`). No se modificó la valoración. Por independencia, **este contenido debe revisarlo una sesión o un LLM distinto** antes de considerarlo auditado. La concentración del backlog por cliente y la base fiscal de las preferentes no son públicas: N/D.
"""

N2 = f"""### Participaciones en Anthropic y OpenAI (desglose de los no operativos)

| Componente | Valor contable 30-sep-26 | Costo / aporte | Contabilización | Efecto en resultados 9M26 | Fuente |
|---|---|---|---|---|---|
| Anthropic: notas convertibles | {m(n['notas'])} | 8.000 (T3-23 a T4-25, parte ya convertida) | AFS, valor razonable, nivel 3; ganancia no realizada {m(n['gan_notas'])} en otro resultado integral | Reclasificación de {m(n['reclas9m'])} a otros ingresos | 10-Q nota 2 |
| Anthropic: preferentes sin voto (164 M acciones) | {m(n['pref'])} | Notas convertidas + Serie G 5.000 + Serie H 5.000 (T2-26) | Participación privada; ajustes por precios observables, nivel 3 | Ajustes al alza por {m(n['ajuste_pref9m'])} | 10-Q nota 2 |
| OpenAI: preferentes Serie C | {m(n['openai'])} | 15.000 (T1) + 13.700 (T2) + 21.300 (T3) | Participación privada; ajustes por precios observables, nivel 3 | — | 10-Q nota 2 |
| Otras participaciones privadas | {m(n['otras_priv'])} | N/D | Ídem | — | 10-Q nota 2 (143.700 − 92.500 − 50.000) |
| Warrants de capital | {m(n['warr'])} | N/D | Valor razonable, niveles 2 y 3 | En otros ingresos | 10-Q nota 2 |
| Método de participación | {m(n['eqm'])} | N/D | Método de participación / opción de valor razonable | — | 10-Q nota 2 |
| **Total no operativos (`Input sheet!B83:B84`)** | **{m(294595)}** | | Excluido del capital operativo; sumado una vez al patrimonio | | Captura R2 |

| Medida | Valor | Cálculo |
|---|---|---|
| No operativos por acción | {u(d['nonop_ps'])} USD | {m(294595)} / 10.811 |
| Peso en el valor Base | {p(d['peso_base'])} | {u(d['nonop_ps'])} / {u(base)} |
| Anthropic / OpenAI por acción | {u(d['anth_ps'])} / {u(d['oa_ps'])} USD | {m(d['anth'])} y {m(n['openai'])} / 10.811 |
| Impuesto diferido de las notas de Anthropic (no restado) | {m(n['dtl'])} M · {u(d['dtl_ps'])} USD por acción | AOCI, 10-Q |
| Otros ingresos 9M26 / utilidad antes de impuestos 9M26 | {p(d['share_otros_pre'], 1)} | {m(n['otros9m'])} / {m(n['pre9m'])} |
| Desembolso 2026 en Anthropic y OpenAI | {m(n['inv26'])} M | 5.000 + 5.000 + 15.000 + 13.700 + 21.300 |
| Línea de financiación a Anthropic | 20.000 M; 15.000 disponibles | 10-Q nota 2 |
| Backlog de AWS / ingresos de AWS LTM | {u(d['backlog_x'], 2)}× | 578.000 / {m(n['ltm_aws'])}; desglose por cliente N/D |
| Base con no operativos −20 % / −50 % (diagnóstico R2) | {u(d['m20'])} / {u(d['m50'])} USD | JSON `ajustes_diagnosticos` |
| Disrupción con participadas −50 % (ilustración aritmética) | {u(d['dis50'])} USD | {u(d['dis'])} − 0,5 × {u(d['nonop_ps'])}; no es valor oficial |
"""

def md_to_html(block):
    out = []; lines = block.strip('\n').split('\n'); i = 0
    def inline(t):
        t = html.escape(t, quote=False)
        import re
        t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
        t = re.sub(r'`([^`]+)`', r'<code>\1</code>', t)
        t = t.replace('[10-Q T3-26, nota 2]', f'[<a class="source" href="{Q}">10-Q T3-26, nota 2</a>]')
        t = t.replace('[10-Q T3-26, notas 2 y 7; N2.4]', f'[<a class="source" href="{Q}">10-Q T3-26, notas 2 y 7</a>; <a href="#n2-4">N2.4</a>]')
        t = t.replace('N2.4]', '<a href="#n2-4">N2.4</a>]')
        return t
    while i < len(lines):
        l = lines[i]
        if l.startswith('### '): out.append(f'<h3>{inline(l[4:])}</h3>'); i += 1
        elif l.startswith('|'):
            rows = []
            while i < len(lines) and lines[i].startswith('|'): rows.append(lines[i]); i += 1
            cells = lambda r: [c.strip() for c in r.strip('|').split('|')]
            h = ''.join(f'<th>{inline(c)}</th>' for c in cells(rows[0]))
            b = ''.join('<tr>' + ''.join(f'<td>{inline(c)}</td>' for c in cells(r)) + '</tr>' for r in rows[2:])
            out.append(f'<div class="table-scroll" tabindex="0"><table><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>')
        elif l.strip(): out.append(f'<p>{inline(l)}</p>'); i += 1
        else: i += 1
    return '\n'.join(out)

BLOQUES = {'n1-2': CAP2, 'n1-8': CAP8, 'n1-11': CAP11, 'n1-12': CAP12, 'n1-13': CAP13, 'n1-14': CAP14, 'n2-4': N2}


ANTES = {'n1-2': '## 3. Industria', 'n1-8': '## 9. Nuestro proceso', 'n1-11': '## 12. Riesgos', 'n1-12': '## 13. Catalizadores', 'n1-13': '## 14. Fuentes', 'n2-4': '## 5. Supuestos efectivos'}
HTML_ANTES = {'n1-2': '<h2 id="n1-3">', 'n1-8': '<h2 id="n1-9">', 'n1-11': '<h2 id="n1-12">', 'n1-12': '<h2 id="n1-13">', 'n1-13': '<h2 id="n1-14">', 'n1-14': '</section><details class="n2" id="nivel2">', 'n2-4': '<h2 id="n2-5">'}

if __name__ == '__main__':
    import sys
    D = sys.argv[1]
    n1 = open(f'{D}/AMZN_NIVEL_1.md').read(); n2 = open(f'{D}/AMZN_NIVEL_2.md').read(); h = open(f'{D}/AMZN_ANALISIS_A12_R2.html').read()
    assert 'Anthropic' not in n1 and 'Anthropic' not in n2, 'ya aplicado'
    for k, blk in BLOQUES.items():
        if k == 'n1-14':
            n1 = n1.rstrip('\n') + '\n\n' + blk.strip() + '\n'
        elif k.startswith('n1'):
            a = ANTES[k]; assert n1.count(a) == 1, a; n1 = n1.replace(a, blk.strip() + '\n\n' + a)
        else:
            a = ANTES[k]; assert n2.count(a) == 1, a; n2 = n2.replace(a, blk.strip() + '\n\n' + a)
        a = HTML_ANTES[k]; assert h.count(a) == 1, a
        sep = '' if k == 'n1-14' else '\n'
        h = h.replace(a, md_to_html(blk) + ('\n' if k != 'n1-14' else '') + a)
    open(f'{D}/AMZN_NIVEL_1.md', 'w').write(n1); open(f'{D}/AMZN_NIVEL_2.md', 'w').write(n2); open(f'{D}/AMZN_ANALISIS_A12_R2.html', 'w').write(h)
    print('aplicado')
