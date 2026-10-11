"""r2 Davivienda: textos de las hojas alineados con los cálculos r2 (no cambia fórmulas).

Banco: 16smCZh7JIB3om_UabhiFymPElK6zyq_6Z8iY-P4Kgrs · Group: 1ogP8LfxEBxslOeC6Avgk2BAClJ_0cfzpgJ06icvVSys
Los cambios numéricos (precio 9-oct, opex Conservador 4%, puente de cesión, Ke del Group) se
hicieron antes en las celdas indicadas en README.md.
"""
from gs import S

BANK = "16smCZh7JIB3om_UabhiFymPElK6zyq_6Z8iY-P4Kgrs"
GROUP = "1ogP8LfxEBxslOeC6Avgk2BAClJ_0cfzpgJ06icvVSys"

bank = [
    ("Resumen!A1", "JMR · PFDAVVNDA · Valoración revisada Damodaran r2 · 11-oct-2026 (precio 9-oct)"),
    ("Resumen!A2", "Filas 6-20: perímetro consolidado reportado. La cesión DAVIbank (SFC Res. 1505, 2-oct-2026) se valora aparte en «Cesión Davibank»: intercambio a valor justo (VPN 0) + sinergias atribuibles con 50% de realización − costos de integración. Valor publicado = con cesión."),
    ("Supuestos!E7", "Conservadora: crecimiento 4%→3% (r2: antes 4,5%, ROE terminal 4,9% muy por debajo de la historia del Banco); riesgo 2,25%; CET1 meta 12,25%."),
    ("'Valoración JMR'!A32", "Valor intrínseco Base r2 **COP 19.474 por acción** con la cesión DAVIbank (perímetro reportado COP 17.387 + VPN de la cesión COP 2.087/acción). Esperado **COP 15.584** (50/25/15/10, piso cero en Disrupción). Precio 9-oct-2026: COP 31.460; Base/precio −38%. Ke 17,66%→18,92% (Rf COP 11,467%, ERP 4,20%, CRP por cartera). No es una certificación contable del emisor."),
    ("'Valoración JMR'!A37", "| Conservador | 3.923 | 3.923 | 25,00% | 6,2% terminal (r2) |"),
    ("'Valoración JMR'!A41", "Múltiplos solos Base COP 26.725; combinado secundario 80/20 con cesión COP 20.924 (perímetro reportado COP 19.255). El método principal sigue siendo FCFE/exceso de retornos. [Hoja revisada con fórmulas](https://docs.google.com/spreadsheets/d/16smCZh7JIB3om_UabhiFymPElK6zyq_6Z8iY-P4Kgrs/edit)."),
    ("'Valoración JMR'!A57", "Cesión DAVIbank (r2): la SFC la autorizó el 2-oct-2026 (Res. 1505); DAVIbank cede su operación bancaria colombiana al Banco a cambio de hasta 30% de las acciones de HDI, con términos fijados por un tercero independiente ([comunicado](https://cdn.aglty.io/scotiabank-colombia/davibank/Info_Relevante_0610_DAVIbank.pdf)). Con Damodaran, un intercambio a valor justo tiene VPN cero: solo cuentan sinergias y costos. Sinergias del Group 0,9–1,2 billones/año desde 2028 (guía 2T26); 70% atribuible al Banco, 50% de realización Base, 35% impuestos ⇒ VP COP 1,29 billones; costos de integración después de impuestos COP 0,27 billones; VPN Base COP 1,02 billones (+COP 2.087/acción)."),
    ("'Valoración JMR'!A59", "Riesgo de parte relacionada: comprador y vendedor tienen el mismo controlante. Un sobreprecio de 10% en la contraprestación resta COP 0,26 billones (≈COP 530/acción). Minoría controlada: Davivienda Group posee ≈98,9%; el CEO no ha decidido deslistar pero no lo descarta. El canje de 2025 se hizo a 1,39× libro (≈COP 48.100 con el libro actual) y PFDAVVNDA cotiza a 0,91× libro: el precio incorpora una opción de OPA/desliste que el modelo no pondera."),
]
group = [
    ("'Valoración actual'!A1", "PFDAVIGRP · Valoración estimada R4 (Ke armonizado) · 11/10/2026"),
    ("'Valoración actual'!A6", "Cierre PFDAVIGRP 09/10/2026: COP 40.620. R4: Ke con el mismo corte que Banco Davivienda, SURA y Argos (Rf COP 11,467%, ERP 4,20%): 17,62% inicial y 18,88% terminal (antes 17,68% y 14,36%). Base R3 COP 28.213 sustituido por COP 21.969."),
]
for sid, rows in ((BANK, bank), (GROUP, group)):
    S.spreadsheets().values().batchUpdate(spreadsheetId=sid, body={
        "valueInputOption": "RAW",
        "data": [{"range": r, "values": [[v]]} for r, v in rows]}).execute()
    print(sid, len(rows), "celdas")
