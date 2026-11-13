# Biblioteca de JMR V2

`biblioteca.json` es una instantánea completa del catálogo, expedientes y análisis de **Modelo JMR V2**, independiente de Floyd y JMR múltiplos. La genera `scripts/exportar-biblioteca.mjs` de `JuanMaRobledo/Modelo-JMR-V2`, con el mismo motor y controles del catálogo. No editar valores derivados a mano.

Publicar cambios de este archivo en `main` actualiza la biblioteca que lee la nueva aplicación sin desplegar código. No conectar este repositorio a Vercel. Conservar el historial Git para poder revertir.

Los borradores editoriales e imágenes se guardan en `borradores/` e `imagenes/`. Un borrador no modifica la valoración ni entra automáticamente en la biblioteca. Para publicarlo, incorporarlo a `analisis/TICKER.json` de la carpeta de trabajo y volver a exportar. La visibilidad nunca equivale a auditoría ni aprobación personal.

La biblioteca inicial conserva EPAM y ORCL. No se eliminan los archivos antiguos hasta comprobar la nueva app en producción. El repositorio es público: no incluir documentos privados ni credenciales.
