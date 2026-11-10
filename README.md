# Modelo JMR datos

Repositorio público de datos utilizado por el [Visor Modelo JMR](https://juanmarobledo.github.io/Modelo-JMR/visor.html) para guardar y consultar valoraciones empresariales en formato JSON.

## Contenido

- Registros de valoración en `valoraciones/`.
- Datos derivados de fuentes públicas y del modelo de valoración.
- No contiene el código de la aplicación.

## Seguridad

Los tokens de acceso no se almacenan en este repositorio. Las escrituras se realizan mediante la API de contenidos de GitHub con un token guardado únicamente en el navegador del usuario.

Este repositorio no debe utilizarse para datos personales, posiciones de cartera, credenciales ni información confidencial.

## Floyd R1–R6 oficial · 10-nov-2026
El modelo desarrollado como Reboot pasa a llamarse **Floyd R1–R6**: seis archivos (H, tres DCF, M, análisis). Las revisiones previas preservan su `revisionId` REBOOT como identificador inmutable y el contrato `jmr-reboot-3libros-v1` como ID técnico. El antiguo Floyd F1–F5 y A-1.2 se archivan en `archivo-v1/` sin alterar sus datos. En la rama candidata UBER conserva temporalmente la publicación anterior hasta superar R5 y las pruebas de integración. No confundir una rama PR con el catálogo de producción.. Las nuevas valoraciones siguen el esquema de tres libros del plan de reboot (Históricos · DCF · Múltiplos) más el documento de análisis.
