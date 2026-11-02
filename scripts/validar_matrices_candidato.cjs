'use strict';
// Cierre de la fase 2 (2-nov-2026): aplica a un JSON CANDIDATO la misma regla de múltiplos que el CI aplica al catálogo
// (validar_catalogo.cjs → validateNativeMatrices). Un múltiplo prioritario en N/D se detecta aquí, no al publicar.
// Caso de origen: AMZN-20261102-A12-R2 cerró la fase 2 con EV/EBITDA, P/E y P/OCF en PENDIENTE_ANCLA y no pudo publicarse.
// Uso: node scripts/validar_matrices_candidato.cjs candidatos/valoraciones/<REV>/VALORACION_A12_EN_REVISION.json
const fs = require('node:fs');
const {validateNativeMatrices} = require('./validar_catalogo.cjs');
const file = process.argv[2];
if (!file) { console.error('Uso: node scripts/validar_matrices_candidato.cjs <VALORACION.json>'); process.exit(2); }
const v = JSON.parse(fs.readFileSync(file, 'utf8'));
try {
  validateNativeMatrices(v);
  console.log(`${v.revisionId || v.revision_id}: matrices de múltiplos aptas para publicar (misma regla que el CI)`);
} catch (e) {
  console.error(`${v.revisionId || v.revision_id}: NO APTA PARA PUBLICAR — ${e.message}`);
  process.exit(1);
}
