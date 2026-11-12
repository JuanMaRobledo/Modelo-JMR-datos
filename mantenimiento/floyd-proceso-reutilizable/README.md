# Mantenimiento del proceso Floyd (12-nov-2026)

Los validadores ahora interpretan `floyd-libro-unico-v1` directamente, sin simular
libros separados. Conservan probabilidades, MOS, hashes, centros y comprobaciones
financieras; el nuevo preflight verifica también la clasificación que usa la app.

## Procedencia de las cinco fichas migradas

Se leyeron en Drive los bloques A46:F51 de EVEBITDA, EVFCFF, PE, PFCFE y POCF,
en cada libro M anterior y su libro único actual. Los diez JSON de esta carpeta
son respuestas de lectura de valores efectivos. Resultado: 25/25 bloques idénticos.
Se conserva sourceSheetIdAnterior, se vincula sourceSheetId al libro único actual
y se enlaza la evidencia de destino. No se cambia ningún valor, matriz ni supuesto.
La igualdad del resto de cada JSON frente a origin/main se comprobó por comparación
estructural excluyendo solo esos tres campos de procedencia.

## Pruebas

- validar_reboot: 6 pares valoración/análisis; PASS.
- auditar_integridad: 6 empresas, 29 matrices OK, 1 N/A; PASS.
- validar_catalogo: 6 valoraciones, 6 análisis; PASS con avisos editoriales preexistentes.
- Pruebas de catálogo, proceso y UBER: 15 PASS.
- En Modelo-JMR: 13 pruebas de contratos y selección de libros; PASS.
- En JMR-valuation: 3 pruebas del instalador; PASS.

## Plantilla

Copia probada, restaurada y sin sellos:
https://docs.google.com/spreadsheets/d/1GtMcMapinEe4-0n0aFCDngiUNlnZtZGAUvwj3o9-Hzc/edit

Respaldo de la maestra:
https://docs.google.com/spreadsheets/d/18NXunNWhaZcCP-yIMbsgMUEGW7w6bB92jr5v9RiAnrY/edit

Pruebas vivas en copia: vacía => NO PUBLICAR; excepción exacta => 1; dato resuelto
=> 0; cambio de input después de sellar firmas de prueba => matrices e inverso
OBSOLETOS. Input/fórmula restaurados; sellos, excepción y ticker de prueba borrados.
No se ejecutó una valoración económica nueva ni se certificó R6. El formato se
revisó por API; no se realizó revisión visual de Google Sheets en navegador.

La instalación en la maestra fue bloqueada por revisión automática de permisos
(por interpretar autorización limitada a la copia). La maestra permanece intacta.
La adopción en producción y los merges de los PR quedan pendientes de aprobación.
