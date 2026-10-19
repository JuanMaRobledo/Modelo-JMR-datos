'use strict';
// Mantener el comando histórico; el contrato vigente valida cifras y estados por bloque.
const {execFileSync}=require('node:child_process');
const path=require('node:path');
execFileSync(process.execPath,[path.join(__dirname,'auditar_integridad.cjs')],{stdio:'inherit'});
