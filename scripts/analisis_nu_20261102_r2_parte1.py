#!/usr/bin/env python3
"""NU-20261102-A12-R2 · Nivel 1 (14 capítulos).
Reutiliza los capítulos 2, 3, 4, 5, 6 y 9 de la R1 (hechos del negocio, sin cifras de valoración) y reescribe 1, 7, 8, 10, 11, 12, 13 y 14,
que dependen del Ke, del capital y del valor. Todas las cifras de valoración salen del JSON de la R2 (construido desde la captura de su hoja)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REV = 'NU-20261102-A12-R2'
_src = (Path(__file__).resolve().parent / 'analisis_nu_20261102_parte1.py').read_text()
_src = (_src.replace("REV = 'NU-20261102-A12-R1'", "REV = 'NU-20261102-A12-R2'")
        .replace("ALT = SD['alternativaCapital']", "ALT = SD.get('alternativaCapital', {'valor': [0, 0, 0, 0]})")
        .replace('patrimonioROE', 'patrimonioRequerido')
        .replace("if __name__ == '__main__':", "if False:"))
_ns = {'__file__': __file__}
exec(compile(_src, 'analisis_nu_20261102_parte1.py', 'exec'), _ns)
CAPS = _ns['CAPS']; P = _ns['P']; n = _ns['n']; usd = _ns['usd']; pc = _ns['pc']
V = _ns['V']; SD = V['sensibilidadDCF']; SUP = V['supuestosModeloA']; ESC = V['escenarios']
H = {h['nombre']: h for h in V['valorEsperado']['historias']}; MET = {m['nombre']: m for m in V['metodos']}
PROY = V['nivel2ProyeccionBase']; CAPR = SUP['controlCapitalRegulatorio']; INV = SD['dcfInverso']; RET = SD['retencionDividendos']
base, cons, opt, disr = ESC['base'], ESC['conservador'], ESC['optimista'], ESC['disrupcion']
precio = V['precio']; mos = V['precioMOS']; prom = V['valorEsperado']['valor']
ke = SUP['ke']; crp = SUP['crpPonderada']; erp = SUP['erpMadura']
pe, pbv, pfcfe = MET['P/E']['valorHoy'], MET['P/BV']['valorHoy'], MET['P/FCFE']['valorHoy']
CAPT = json.loads((ROOT / f'evidencia/captura-hoja-20261102/{REV}_resultados_hoja.json').read_text())['data']['fcfe']
c_ = lambda r, k: (CAPT[r - 1][k] if r - 1 < len(CAPT) and k < len(CAPT[r - 1]) else None)
vp_fcfe, vp_tv, patr, vt, ni10 = c_(45, 1), c_(48, 1), c_(49, 1), c_(47, 1), c_(44, 4)
kecol = [SD['matrices'][0]['values'][i][2] for i in range(5)]
roecol = [SD['matrices'][1]['values'][i][2] for i in range(5)]
ut = [SD['matrices'][2]['values'][i][2] for i in range(5)]
R1_BASE = 15.139922964354914  # NU-20261102-A12-R1 (valoraciones/NU-20261102-A12-R1.json)
roe1, roe5, roe10 = PROY[0]['ROE'], PROY[4]['ROE'], PROY[-1]['ROE']


def put(i, titulo, *partes):
    CAPS[i - 1] = (titulo, ''.join(partes))


put(1, '1. Tesis y resumen ejecutivo',
    P('Nu Holdings (Nubank) es el banco digital más grande de América Latina por clientes: 139 millones a junio de 2026, con casi 118 millones en Brasil, 15,8 millones en México y más de 5 millones en Colombia. '
      'Su economía por cliente (un costo de servir y de gastos generales por cliente activo que la compañía estima cerca de 85 % inferior al de los bancos tradicionales en Brasil, una actividad mensual de 83,5 % y un ingreso medio por cliente activo de unos US$17 al mes) '
      f'financia un crecimiento de utilidades que, descontado al costo del patrimonio, vale <strong>{usd(base)} por acción</strong> en la historia Base de esta revisión, frente a un cierre de {usd(precio)} el 30 de octubre de 2026. '
      f'El precio máximo de compra con margen de seguridad del 35 % es {usd(mos)}: el mercado cotiza por debajo del valor intrínseco, pero no ofrece el margen de seguridad que exige el Método.'),
    P(f'Las cuatro historias valen {usd(cons)} (Conservadora), {usd(base)} (Base), {usd(opt)} (Optimista) y {usd(disr)} (Disrupción, aparte). El promedio ponderado ordinario de las tres primeras es {usd(prom)}. '
      'Como institución financiera, el método principal es un FCFE a diez años descontado al costo del patrimonio (Ke); los depósitos, el fondeo y las pérdidas de crédito son la materia prima del negocio, no deuda ni gasto financiero ajeno.'),
    P(f'<strong>Qué cambia frente a la R1 y por qué.</strong> La auditoría de la R1 (A1/A1.1, 2-nov-2026) encontró dos problemas de calibración en direcciones opuestas. '
      f'(i) El Ke era bajo: usaba una beta sectorial de 0,76 y la prima país de enero; la R2 usa beta 1,00, prima país estimada al 30-oct y prima madura ajustada a la misma fecha, y el Ke Base sube de 10,93 % a {pc(ke["Base"], 2)}. '
      f'(ii) El capital era demasiado conservador: la R1 imponía un ROE que caía de 28 % a 17 %, lo que equivalía a retener patrimonio muy por encima de lo que muestran los datos de capital regulatorio; la R2 liga el patrimonio a los activos ponderados por riesgo observados (APR) y el ROE resulta de {pc(roe1)} a {pc(roe10)}. '
      f'El efecto neto es {usd(base)} frente a {usd(R1_BASE)} de la R1. Crecimiento y márgenes se revisaron y no se cambiaron: no eran conservadores frente a la evidencia.'),
    P(f'Lo que descuenta el precio: con los flujos Base, el precio equivale a un Ke de {pc(INV["keImplicito"])}, {n((INV["keImplicito"] - ke["Base"]) * 100, 1)} puntos por encima del Ke de la casa; con el Ke de la casa, el mercado descuenta el {pc(INV["utilidadRelativaImplicita"], 0)} de la utilidad Base. '
      f'Tres reservas siguen abiertas: la retención de 10 % que Brasil aplica desde 2026 a los dividendos enviados al exterior (no incluida; con ella el valor sería {usd(RET["valor"][2])}), la estimación de la prima país con datos de prensa y la deriva futura de la densidad del APR. '
      'Este expediente está en revisión y no ha sido auditado económicamente.'))

put(7, '7. Drivers de crecimiento, márgenes e hipótesis A-1.2',
    P('El modelo proyecta por año e historia el crecimiento de ingresos y el margen neto (que dan la utilidad), la deriva de densidad del APR y la relación patrimonio/APR τ (que dan el capital), y el Ke. '
      f'En la Base los ingresos crecen 30 %, 24 %, 20 %, 17 % y 15 % los primeros cinco años y 13 %, 11 %, 9 %, 7,5 % y 6 % después; el margen neto sube de 17,5 % a 19,5 % en el quinto año y baja a 18,5 % por competencia y normalización del costo de crédito. La utilidad pasa de US${n(PROY[0]["utilidad"])} millones en el año 1 a US${n(PROY[-1]["utilidad"])} millones en el año 10.'),
    P('<strong>Revisión pedida por el usuario: ¿eran demasiado conservadores?</strong> Se contrastaron los cuatro motores con la evidencia. '
      'El margen neto normalizado a una tasa efectiva de 26 % fue 18,1 % en 2025, 16,8 % en los doce meses a junio de 2026, 15,5 % en el primer semestre de 2026 y 16,6 % en el 2T26. La Base arranca en 17,5 % y llega a 19,5 %, por encima de cualquier año histórico: no es conservadora y no se sube. '
      'El crecimiento del año 1 (30 % sobre el UDM, US$25.141 millones) ya supera el consenso de ingresos de 2027 (+24 %, S&P vía stockanalysis.com, 27-oct-2026) y equivale a 14 % por encima del ritmo anualizado del 2T26: tampoco es conservador. '
      'Donde la R1 sí era conservadora era en la reinversión: suponía que la rentabilidad sobre el capital caería mucho más de lo que muestran los datos (capítulo 8).'),
    P('Justificación del año 1: el ingreso NIIF del 2T26 fue US$5.513 millones; anualizado (US$22.053 millones) ya supera en 14 % el UDM de US$19.340 millones. La Conservadora crece 20 % el primer año por una desaceleración de la cartera; la Optimista 36 %, apoyada en México y en la monetización de segmentos de ingresos altos. '
      'Cada riesgo va en un solo lugar: el riesgo de crédito está en el margen, el riesgo país y de mercado en el Ke, el riesgo regulatorio de capital en la densidad del APR y en τ, y el riesgo de ventaja competitiva en las probabilidades y en la Disrupción.'),
    P(f'<strong>Coherencia crecimiento–reinversión–rentabilidad.</strong> En la regla de Damodaran, crecimiento = retención × rentabilidad sobre el capital. En el año 10 de la Base los ingresos crecen 6 %, el ROE es {pc(roe10)} y el patrimonio crece al ritmo del APR (6 % con τ bajando a 30 %), lo que implica retener alrededor de un sexto de la utilidad: la proyección es coherente. '
      'El terminal usa crecimiento de 4 % (con techo en la tasa libre de 4,94 %) y ROE terminal de 16 %: retener 25 % de la utilidad para crecer 4 % es la convergencia prudente que exige la regla de moat, no un recorte adicional.'))

put(8, '8. Reinversión, capital regulatorio y retorno sobre el patrimonio',
    P('En un banco, la reinversión es el patrimonio que debe retenerse para sostener los activos ponderados por riesgo (APR). La R2 lo modela de forma explícita: APR del año = APR anterior × (1 + crecimiento de ingresos) × (1 + deriva de densidad); patrimonio requerido = τ × APR; FCFE = utilidad − aumento del patrimonio requerido. '
      'El ROE deja de ser un supuesto y pasa a ser un resultado que se puede contrastar con la historia.'),
    P('<strong>Evidencia de capital (20-F 2025 y 6-K 2T26).</strong> El APR del conglomerado prudencial de Brasil pasó de US$20.072 millones (dic-24) a US$31.142 millones (dic-25, +55 %, con ingresos +37 %) y a US$35.710 millones (jun-26). '
      'El índice CET1 bajó de 14,7 % a 13,0 % y a 11,9 %; el capital total de 18,1 % a 16,6 % y a 15,7 %, con un margen sobre el mínimo de US$1.848 millones. México reporta capital de US$427,6 millones (índice 14,9 %) y Colombia US$179,7 millones (15,3 %), ambos con mínimo de 10,5 %. '
      'Con México y Colombia derivados de sus índices, el APR total aproximado era US$39.755 millones a junio de 2026, y el patrimonio de la controladora (US$13.250 millones) equivalía al 33,3 % de ese APR: 15,7 % de capital regulatorio, ~12 % de deducciones no distribuibles (impuesto diferido US$3.649 millones, plusvalía US$409 millones, intangibles US$747 millones) y un colchón de la matriz.'),
    P('<strong>Calibración.</strong> La densidad (APR / ingresos UDM) fue 1,94 (dic-24), 2,19 (dic-25) y 2,06 (jun-26): subió 3,8 % anual en dieciocho meses, con un año de alza y un semestre de baja. La utilidad normalizada sobre APR fue 9,2 %, 8,3 % y 8,2 %. '
      f'La Base supone una deriva de densidad de 3,8 % anual durante tres años y de 1,9 % en los años 4 y 5, que se desvanece después, y una τ que baja de 33,3 % a 30 % a medida que el crecimiento se modera y el colchón se usa. El resultado es un ROE de {pc(roe1)} en el año 1, {pc(roe5)} en el año 5 y {pc(roe10)} en el año 10, y una utilidad sobre APR que baja de 8,2 % a {pc(PROY[-1]["utilidad"] / PROY[-1]["APR"])}.'),
    P(f'<strong>Por qué la R1 era demasiado conservadora y la R2 no sobrecorrige.</strong> La R1 imponía un ROE de 28 % a 17 %. Con la misma utilidad, eso exigía un patrimonio de US$87.600 millones en el año 10, equivalente a suponer que la densidad del APR crece ~6 % al año durante diez años, más de una vez y media la deriva observada (3,8 %). '
      f'La R2 no libera todo el «exceso» que mostraba el control de la R1: mantiene τ en 30 % o más (el doble del capital regulatorio) y conserva una deriva de densidad. Las historias cubren el rango: la Conservadora mantiene la deriva de 3,8 % los diez años y τ en 33,3 %; la Disrupción, una deriva de 6 %; la Optimista, sin deriva y τ que baja a 28 %.'),
    P(f'<strong>Repatriación.</strong> Desde 2026 Brasil retiene 10 % de los dividendos enviados al exterior (Ley 15.270/2025) y la retención sobre intereses sobre el capital subió de 15 % a 17,5 % (Ley Complementaria 224, citada en el 20-F). Para Nu Holdings (Islas Caimán) esto puede reducir el flujo que llega al accionista. '
      f'Con 10 % sobre el 90,9 % del FCFE que proviene de Brasil, el valor Base bajaría a {usd(RET["valor"][2])} ({pc(RET["variacion"][2], 0)}). No se incorpora a la Base porque existen transición para dividendos aprobados hasta 2025, un mecanismo de crédito y la alternativa de recomprar acciones con caja fuera de Brasil; su tratamiento debe confirmarlo un asesor tributario.'))

put(10, '10. Coste del patrimonio, tasas y fechas',
    P(f'Ke = tasa libre + beta × prima madura + prima país ponderada. Tasa libre: Treasury a 10 años del 30-oct-2026, 4,94 %. Prima madura: {pc(erp, 2)}, la implícita de Damodaran de octubre (3,70 %, calculada con el S&P 500 y el Treasury del 30-sep) ajustada al 30-oct replicando su método con el S&P 500 en 7.580 y el Treasury en 4,94 % (+0,08 puntos). '
      f'Prima país ponderada por los ingresos del 1S26 (Brasil 90,9 %, México 7,2 %, otros 1,8 %): {pc(crp, 2)}. Ke Base y Optimista: {pc(ke["Base"], 2)}; Conservadora (beta 1,30): {pc(ke["Conservador"], 2)}; Disrupción (beta 1,50 y 1,5× prima país): {pc(ke["Disrupcion"], 2)}.'),
    P('<strong>Prima país «a hoy».</strong> La tabla oficial de Damodaran sigue siendo la de enero de 2026 (su página indica «Last updated: January 5, 2026»; no publicó actualización de mitad de año): Brasil 3,24 % por calificación (Ba1) y 3,37 % por CDS. '
      'Después de las elecciones del 25-oct, el CDS a 5 años de Brasil subió de 120 a 152 puntos básicos (S&P Global Market Intelligence, vía Rio Times, 26-oct-2026). Con el CDS a 10 años de 196,8 pb del 22-oct (Investing.com) escalado por ese salto (≈ 248 pb), restando el CDS de Suiza (0,14 %) y multiplicando por la volatilidad relativa de Brasil de Damodaran (1,523), la prima país de Brasil al 30-oct es ≈ 3,57 %. '
      'Es una estimación con fuentes secundarias (margen ± 0,25 puntos); México y Colombia conservan la tabla de enero.'),
    P('<strong>Beta.</strong> Las betas sectoriales de Damodaran (enero de 2026) son bajas para un banco digital con crédito sin garantía: bancos globales 0,70, servicios financieros no bancarios globales 0,82, bancos de mercados emergentes 0,59–0,60. '
      'La beta de abajo hacia arriba ponderada por la mezcla de utilidad bruta de Nu (crédito y comisiones 66 %, float 34 %) es 0,78. La regresión de NU contra el S&P 500 da 0,86 ± 0,39 (5 años mensual), 1,31 ± 0,11 (2 años diario) y 1,40 ± 0,22 (3 años semanal); ajustada hacia 1 (Blume), 1,21. '
      'La R2 usa 1,00, el punto medio de ambas aproximaciones, que además coincide con la beta de 0,98 que usa la valoración de XP en esta misma cartera. La Conservadora usa 1,30 (la regresión sin ajuste) como estrés.'),
    P(f'Contraste: el DCF inverso encuentra un Ke de {pc(INV["keImplicito"])} que iguala el valor Base al precio. Con Ke de {pc(ke["Base"] - 0.01, 1)}, {pc(ke["Base"], 1)} y {pc(ke["Base"] + 0.01, 1)} la Base vale {usd(kecol[1])}, {usd(kecol[2])} y {usd(kecol[3])}. '
      'Fechas: estados al 30-jun-2026 (6-K del 13-ago-2026, revisados y no auditados por KPMG); precio y tasas al 30-oct-2026; el valor se calcula al 30-jun y se capitaliza 122 días al Ke.'))

put(11, '11. Historias, probabilidades y señales de refutación',
    P(f'<strong>Base ({pc(H["Base"]["probabilidad"])}; {usd(base)}).</strong> Ingresos +30 % que decaen a +6 %; margen neto 17,5 %–19,5 %; APR con deriva de densidad que se desvanece en cinco años; τ de 33,3 % a 30 %; ROE de {pc(roe1)} a {pc(roe10)} y terminal 16 %; Ke {pc(ke["Base"], 2)}. '
      f'Utilidad con CAGR de {pc(H["Base"]["crecimientoNIprimeros5"])} en cinco años. Refutación: ROE trimestral por debajo de 22 % con tasa efectiva normalizada, o densidad del APR creciendo más de 5 % anual dos años seguidos.'),
    P(f'<strong>Conservadora ({pc(H["Conservadora"]["probabilidad"])}; {usd(cons)}).</strong> Ingresos +20 % que decaen a +4,5 %, margen neto 15,5 % → 14 %, densidad del APR creciendo 3,8 % los diez años con τ en 33,3 %, beta 1,30 (Ke {pc(ke["Conservador"], 2)}) y ROE terminal igual al Ke (sin ventaja residual). '
      'Es una Nu que se parece a un banco brasileño grande: buena, pero sin rentabilidad excedente a largo plazo. Refutación: crecimiento de ingresos por encima de 25 % con costo de crédito estable.'),
    P(f'<strong>Optimista ({pc(H["Optimista"]["probabilidad"])}; {usd(opt)}).</strong> Ingresos +36 % que decaen a +8 %, margen neto hasta 21,5 %, sin deriva de densidad y τ que baja a 28 %, ROE terminal 20 %. México y los segmentos de ingresos altos aportan escala. Refutación: ARPAC de México por debajo de US$10 a dos años del lanzamiento del banco o eficiencia por encima de 22 %.'),
    P(f'<strong>Disrupción, aparte ({pc(H["Disrupción"]["probabilidad"])}; {usd(disr)}).</strong> El crédito sin garantía se deteriora, la densidad del APR sube 6 % anual, el margen neto cae a 9 %, la beta sube a 1,50 con 1,5× la prima país (Ke {pc(ke["Disrupcion"], 2)}) y el ROE termina por debajo del Ke. No entra en el promedio ordinario. '
      f'Probabilidades: previa de la etapa de crecimiento alto (40 / 22,5 / 22,5 / 15), sin ajustes porque ningún indicador con umbral escrito lo cruzó. Pesos renormalizados de las tres historias: 47,1 % / 26,5 % / 26,5 %; promedio ordinario {usd(prom)}; valor esperado de las cuatro (etiquetado) {usd(base * 0.40 + cons * 0.225 + opt * 0.225 + disr * 0.15)}.'),
    P('Umbrales de seguimiento propuestos (aún no escritos en la ficha de indicadores del Método, por lo que no mueven probabilidades): morosidad de 90 días 8 %, ROE trimestral normalizado 22 %, densidad del APR, CET1 de Brasil 11 %, costo de depósitos 95 % del interbancario, ARPAC de México US$10.'))

put(12, '12. Valor intrínseco, MOS, precio y puente a equity',
    P(f'Valor Base: <strong>{usd(base)}</strong>. Valor presente de los diez FCFE: US${n(vp_fcfe)} millones; valor presente del valor terminal: US${n(vp_tv)} millones ({pc(vp_tv / patr, 0)} del total); patrimonio al 30-jun-2026: US${n(patr)} millones, capitalizado 122 días al Ke y dividido por 4.908,8 millones de acciones. '
      f'El primer año tiene FCFE negativo (US${n(PROY[0]["FCFE"])} millones) porque el APR crece más que la utilidad; el flujo se vuelve positivo desde el año 2 y llega a US${n(PROY[-1]["FCFE"])} millones en el año 10.'),
    P(f'MOS 35 %: {usd(base)} × 0,65 = <strong>{usd(mos)}</strong>. Precio: {usd(precio)} (30-oct-2026). El precio está {pc(precio / mos - 1)} por encima del precio con margen de seguridad y {pc(1 - precio / base)} por debajo del valor Base. Promedio ordinario: {usd(prom)}. Disrupción: {usd(disr)}. '
      f'El valor del patrimonio equivale a {n(patr / 13249.67, 1)} veces el patrimonio contable, frente a {n(precio * 4908.841 / 13249.67, 1)} veces que implica el precio. No hay puente de deuda: en un FCFE el valor ya es del accionista; depósitos, fondeo y arrendamientos son operación.'),
    P(f'<strong>Puente con la R1.</strong> R1: {usd(R1_BASE)} (Ke 10,93 %, ROE impuesto de 28 % a 17 %). Solo con el Ke de la R2 y el capital de la R1, el valor sería ≈ US$12,0; solo con el capital de la R2 y el Ke de la R1, ≈ US$17,8. '
      f'Ambas correcciones van en direcciones opuestas y la R2 queda en {usd(base)}. Ninguna cifra se ajustó para acercarse a la cotización; el DCF inverso sigue mostrando que el mercado exige un Ke mayor ({pc(INV["keImplicito"])}) que el de la casa.'))

put(13, '13. Múltiplos y sensibilidades',
    P(f'Métodos pertinentes para un banco: P/E, P/FCFE y P/BV; EV/EBITDA, EV/FCFF y P/OCF son N/A. Peso 0 en todos. Valores presentes de la Base (FY+3 descontado al Ke): P/E {usd(pe["base"])} (13×), P/BV {usd(pbv["base"])} (3,8× sobre el patrimonio del modelo), P/FCFE {usd(pfcfe["base"])} (PENDIENTE_ANCLA: el FCFE del año 3 es residual tras la retención de capital). '
      'Anclas: serie propia de NU (P/E 39,3×, 26,4× y 28,9× en diciembre de 2023–2025; P/BV 6,3×–7,3×) y pares brasileños (P/E mediano 5,7×; P/BV 0,85×). Los múltiplos de salida son juicios entre ambos extremos; el Conservador no supera el múltiplo actual y el Optimista no pasa +25 % sobre él. '
      'El denominador de P/BV es el patrimonio del propio modelo y P/E usa su utilidad: son chequeos de coherencia, no confirmaciones independientes.'),
    P(f'Sensibilidades de la Base (centro = valor Base, control 0). Ke × g: de {usd(SD["matrices"][0]["values"][4][0])} (Ke +2 puntos, g 3 %) a {usd(SD["matrices"][0]["values"][0][4])} (Ke −2, g 4,9 %). '
      f'ROE terminal × g (con g 4 %): {usd(roecol[0])} con 11,5 %, {usd(roecol[2])} con 16 % y {usd(roecol[4])} con 20 %. Utilidad relativa × Ke: con 15 % menos de utilidad en toda la trayectoria, {usd(ut[1])}; con 15 % más, {usd(ut[3])}. '
      f'Retención sobre dividendos: 5 % efectivo, {usd(RET["valor"][1])}; 9,09 %, {usd(RET["valor"][2])}; 10 %, {usd(RET["valor"][3])}.'),
    P(f'DCF inverso: el precio de {usd(precio)} equivale al {pc(INV["utilidadRelativaImplicita"], 0)} de la utilidad Base con el Ke de la casa, o a un Ke de {pc(INV["keImplicito"])} con la utilidad Base. Es decir, el mercado acepta la historia operativa casi completa, pero exige una prima de riesgo mayor tras las elecciones.'))

put(14, '14. Catalizadores, riesgos, fuentes y decisiones pendientes',
    P('<strong>Catalizadores.</strong> (1) Resultados del 3T26 (el año anterior se publicaron el 13 de noviembre): ROE, tasa efectiva, costo de crédito, morosidad, ARPAC y APR/CET1. (2) Banco en México (lanzado en agosto de 2026) y licencia bancaria plena en Brasil. (3) Copom del 4-nov-2026. (4) Recompras (US$500 millones ejecutados al 30-jun). (5) Nombramiento del director de tecnología.'),
    P('<strong>Riesgos.</strong> Costo de crédito de la cartera sin garantía; regulación de Brasil (CSLL más alta desde 2028, retención sobre dividendos al exterior desde 2026, Pix y Open Finance); concentración en Brasil (90,9 % de los ingresos del 1S26); real frente al dólar; liquidez (92,5 % de los depósitos a la vista); calidad de la utilidad por el impuesto diferido; densidad creciente del APR; ejecución internacional; gobierno concentrado en el fundador (74,3 % del voto).'),
    P('<strong>Fuentes.</strong> 20-F 2025 (8-abr-2026); 6-K de estados del 2T26 (13-ago-2026) y comunicado; 6-K del 23-oct-2026; Treasury a 10 años (Departamento del Tesoro, 30-oct-2026); Damodaran: primas por país (enero de 2026), betas por industria (enero de 2026) y ERP implícita (octubre de 2026); Yahoo Finance (precios, betas de regresión y múltiplos de pares); Rio Times / S&P Global Market Intelligence e Investing.com (CDS de Brasil); EY, Mayer Brown y Baker McKenzie (Ley 15.270/2025); prensa brasileña (contexto electoral y Selic).'),
    P('<strong>Decisiones pendientes para el usuario y la auditoría.</strong> (a) Incorporar o no la retención sobre dividendos a la Base; (b) confirmar la prima país con un dato de CDS de cierre del 30-oct; (c) seguimiento trimestral de la densidad del APR, que es la variable que más distingue las historias; (d) ROE terminal de 16 %; (e) anclas independientes para P/E y P/BV. '
      'La R1 (NU-20261102-A12-R1) y su auditoría se conservan sin cambios. Este expediente no ha sido auditado económicamente.'))


def extra(i, *partes):
    t, b = CAPS[i - 1]
    CAPS[i - 1] = (t, b + ''.join(partes))


pb_just = (0.16 - 0.04) / (ke['Base'] - 0.04)
extra(12, P(f'<strong>Qué implica el valor terminal.</strong> El valor terminal de la Base es US${n(vt)} millones en el año 10, {n(vt / ni10, 1)} veces la utilidad de ese año y {n(vt / PROY[-1]["patrimonioRequerido"], 2)} veces el patrimonio requerido. '
            f'Con ROE terminal de 16 %, g de 4 % y Ke de {pc(ke["Base"], 2)}, el múltiplo justificado del patrimonio es (ROE − g) ÷ (Ke − g) = {n(pb_just, 2)} veces: la Base supone que en diez años Nu cotizaría a menos de la mitad del múltiplo de libro actual (4,3 veces), '
            'un supuesto de convergencia exigente con la ventaja competitiva de hoy y que por eso no puede calificarse de optimista.'),
          P(f'<strong>Dinámica del flujo.</strong> El FCFE de la Base es negativo en el año 1 (el APR crece 35 % entre crecimiento y densidad), modesto en los años 2 y 3 (US${n(PROY[1]["FCFE"])} y US${n(PROY[2]["FCFE"])} millones) y se acelera desde el año 4, cuando la deriva de densidad se reduce y el crecimiento de ingresos baja de 20 %. '
            f'El valor presente de los diez años de flujos es US${n(vp_fcfe)} millones, {pc(vp_fcfe / patr, 0)} del total: frente a la R1 (19 %), una parte mayor del valor depende de flujos explícitos y no del terminal, lo que lo hace más verificable con los resultados trimestrales.'))
extra(13, P('<strong>Cómo leer las sensibilidades.</strong> La matriz Ke × g muestra que un punto de Ke mueve el valor más que medio punto de g: el riesgo de tasa domina. La matriz de ROE terminal muestra el costo de la regla de moat: con ROE terminal igual al de la Optimista (20 %) la Base subiría a '
            f'{usd(roecol[4])}, y con el de los pares grandes (11,5 %) bajaría a {usd(roecol[0])}. La matriz de utilidad × Ke permite combinar escenarios: una utilidad 15 % menor con un punto más de Ke da {usd(SD["matrices"][2]["values"][1][3])}, y una utilidad 15 % mayor con un punto menos de Ke da {usd(SD["matrices"][2]["values"][3][1])}.'),
          P('<strong>Contraste de los múltiplos con el DCF.</strong> El P/E de salida de 13× en el año 3 es menor que el múltiplo actual (15,8× UDM) y muy superior a la mediana de los pares (5,7×); el P/BV de 3,8× es menor que el actual (4,3×). '
            f'Que los valores presentes de P/E ({usd(pe["base"])}) y P/BV ({usd(pbv["base"])}) queden a {pc(abs(pe["base"] / base - 1), 0)} y {pc(abs(pbv["base"] / base - 1), 0)} del DCF indica que los supuestos de utilidad y capital son coherentes con múltiplos de salida plausibles, no que el DCF esté confirmado.'))
extra(14, P('<strong>Plan de seguimiento trimestral.</strong> Para cada informe se actualizan, en este orden, los indicadores que distinguen las historias: (1) APR de Brasil, México y Colombia y su relación con los ingresos (la deriva de densidad separa la Base de la Conservadora); '
            '(2) ROE con la tasa efectiva normalizada; (3) costo de crédito y morosidad temprana y tardía; (4) margen antes de impuestos; (5) CET1 y capital total de Brasil y uso de la recompra; (6) ARPAC y clientes activos por país; (7) CDS de Brasil y Selic para la prima país.'),
          P('<strong>Vigencia.</strong> Estados al 30-jun-2026; precio, Treasury, prima madura ajustada y prima país estimada al 30-oct-2026; hechos posteriores leídos hasta el 6-K del 23-oct-2026. '
            'Si el 3T26 muestra una densidad de APR creciendo más de 5 % anual o un ROE normalizado por debajo de 22 %, la siguiente revisión debe mover probabilidades hacia la Conservadora, conforme a los umbrales que se incorporen a la ficha de indicadores.'))

extra(11, P('<strong>Por qué las historias son simétricas en evidencia.</strong> La Conservadora y la Optimista se construyen con la misma exigencia: cada una mueve crecimiento, margen, densidad del APR y ROE terminal en la dirección de su relato, '
            'y ninguna se apoya en un dato que la otra ignore. La Conservadora toma la deriva de densidad observada (3,8 %) como permanente y la beta de regresión sin ajustar; la Optimista toma la ausencia de deriva del primer semestre de 2026 y el ROE terminal que justificaría una ventaja duradera. '
            'La Base queda entre ambas en cada palanca, que es lo que el Método exige de una mediana, y la prudencia vive en el margen de seguridad, no en la Base.'))
extra(7, P('<strong>Resumen de la revisión de motores.</strong> Crecimiento: sin cambio (supera consenso). Márgenes: sin cambio (superan el histórico normalizado). Reinversión y ROE: corregidos (la R1 suponía una caída de rentabilidad sobre el capital no observada). '
           'Costo del patrimonio: corregido al alza (beta y prima país). Las dos correcciones se compensan parcialmente y ninguna se calibró contra el precio.'))

extra(10, P('<strong>Coherencia de moneda y riesgo.</strong> El modelo descuenta flujos en dólares con una tasa libre en dólares, una prima madura de mercado y una prima país por exposición de ingresos; el crecimiento terminal de 4 % también está en dólares. '
            'No se suma un recargo discrecional por las elecciones: el movimiento posterior al 25-oct ya entra a través del CDS en la prima país. El riesgo de crédito no se cuenta en el Ke, porque ya está en el margen neto y en la densidad del APR.'))


def nivel1_html():
    nav = ''.join(f'<li><a href="#jmr-n1-chapter-{i+1}">{t}</a></li>' for i, (t, _) in enumerate(CAPS))
    sec = ''.join(f'<section id="jmr-n1-chapter-{i+1}"><h2>{t}</h2>{b}</section>' for i, (t, b) in enumerate(CAPS))
    cab = (f'<header><h1>Nu Holdings — análisis fundamental Método JMR A-1.2</h1><p>EN_REVISION. Revisión {REV} (sustituye a NU-20261102-A12-R1 tras su auditoría). Estados al 30-jun-2026 (6-K 2T26); precio de referencia {usd(precio)} al 30-oct-2026. '
           f'Valor Base {usd(base)}; MOS35 {usd(mos)}. Auditoría económica de esta revisión no realizada; sin QA visual autenticado.</p></header>')
    return f'<article data-jmr-revision="{REV}" data-metodo="A-1.2">{cab}<nav aria-label="Índice del análisis fundamental" data-jmr-n1-standard="14-20261031"><ol>{nav}</ol></nav>{sec}</article>'


if __name__ == '__main__':
    import re
    h = nivel1_html()
    w = lambda x: len(re.sub(r'<[^>]+>', ' ', x).split())
    print(len(CAPS), 'capítulos', w(h), 'palabras', [w(b) for _, b in CAPS])
