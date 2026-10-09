# Revisión Damodaran PFDAVVNDA · 9-oct-2026

Perímetro reportado Banco Davivienda, no Davivienda Group ni cesión DAVIbank futura. El expediente publicado enlaza la hoja nativa con fórmulas. `python3 completar_modelo.py` reproduce cuatro historias y prepara solicitudes de hoja sin ejecutarlas; `python3 sensibilidades_finales.py` reproduce sensibilidades e inversa. Entradas numéricas proceden de los estados y supuestos declarados en los informes; no son datos de otra empresa.

`reverificacion_publicacion.json` recoge valores efectivos leídos nuevamente. P/E presente aplica semestre anualizado homogéneo; el motor de cuatro historias no usa el UDM mixto. Flujos negativos son financiación, no dividendos decretados; título con piso cero separado del VAN neto. Precio congelado 8-oct COP30.800, no precio vivo. Precio de cesión desconocido permanece null en el expediente.
