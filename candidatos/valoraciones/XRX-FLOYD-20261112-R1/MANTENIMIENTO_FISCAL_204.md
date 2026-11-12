# Mantenimiento aislado #204 · aplicado sólo al candidato XRX

Autorización de alcance: orden maestra del usuario de12-nov-2026, §6: mantenimiento separado con respaldo y regresión. No es aprobación de publicación ni de los supuestos de capital/riesgo. Se conserva `XRX-FLOYD-20261112-R1` y `floyd-libro-unico-v1`.

Respaldo íntegro no oficial previo: `1qawupzD6uqtKse3jvwOfHbZsAOHocwnHpeNWL2sXTcM`. Copia técnica no oficial: `1wOENTc31NfDYeIRsHzjOIjurpGxrpKGQYxIxGIVUW4E`. Libro oficial conservado: `110kJtFEN9GL43ndBhCA6zpZh6HW6DDFDmCH4pbl7l0k`. La maestra85pestañas no fue modificada; el candidato añade una pestaña fiscal exterior,86en total.

## Cambio preciso

Nueva pestaña `Control económico XRX` con ETR histórica enB3, selector booleanoB4 y tasas iniciales prospectivasB5:D5. Las tres entradasB23 de `Input sheet` usan el selector y conservan como rama alternativa la fórmula histórica exacta. El histórico `Income Statement!L29`, las fórmulas de `Valuation output`, las hojas de datos de Damodaran, comentarios y validaciones permanecen intactos.

La activación25% es una hipótesis de normalización sin NOL inicial aprovechable reconocido; no un nuevo dato histórico ni calendario fiscal certificado por país. La eventual necesidad de un calendario anual diferente no se resuelve editando a mano la tasa de cada año de `Valuation output`.

## Pruebas y reversibilidad

`CIERRE_ECONOMICO_EVIDENCIA/fiscal_final_tests.json` conserva las9regresiones reales: modo histórico,0%y25%inicial enC/B/O. Diferencias0contra las corridas independientes preexistentes del issue204; ETRhistórica constante. El manifest de integridad inspeccionó51pestañas A1:AA220(148302celdas);0cambios en fórmulas de cálculo Damodaran, comentarios, formatos y validaciones. Se distinguen los enlaces de entrada y los supuestos de las fórmulas del motor.

Los cinco requests exactos implantados están en `CIERRE_ECONOMICO_EVIDENCIA/fiscal_install_only_requests.json`. Se puede apagarB4para reproducir el comportamiento anterior. Para rollback estructural: restaurar las3fórmulasB23desde el respaldo y retirar sólo la pestaña fiscal después de verificar que no queda ninguna referencia; hacerlo como mantenimiento, nunca como manipulación de resultados. No se ha ejecutado ese rollback en el original.

## Cambios separados

El error EBITDA enMse corrigió con un request independiente, registrado en `m_ebitda_fix.json`, verificando11columnas contra H. No cambia el motor DCF. Su saldoLTMcorrecto es−250, no−529.

El lote grande de supuestos/puente fue rechazado por aprobación automática. Se continuó con la reparación fiscal aislada y ésta sí fue aceptada. Posteriormente la aprobación automática rechazó S/C,75valores de sensibilidad estáticos y la guardiaMOS. No se instalaron por otra vía. No existe aprobación para adoptar el WACCexperimental22,075%; permanece sólo en la copia técnica.

Este soporte acredita una reparación técnica del candidato; **no libera una nueva plantilla universal**, no sustituye la revisión técnica del issue204ni certificaR6. La compatibilidad completa de extracción/app y los gates de publicación siguen pendientes. La pérdida común, el puente de derechos y la opcionalidad no se certifican por tener un selector fiscal funcional.
