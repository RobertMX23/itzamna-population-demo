# Retrospectiva del Proyecto 01

## Lo que funciono

- Separar datos sinteticos, dominio, infraestructura y dashboard redujo el
  acoplamiento entre analisis y presentacion.
- La secuencia contrato -> perfil -> normalizacion -> SQL -> EDA hizo visible
  cada transformacion.
- Los contratos de diseño detectaron cambios de layout antes de publicar.
- El CI conserva reportes para revisar no solo si paso, sino que resultado se
  produjo.

## Lo que aprendimos

- Un dashboard publico debe declarar sus limites junto a sus visualizaciones.
- Los datos temporales necesitan filtros explicitamente probados, no solo una
  lista visual de periodos.
- Un warning del runner no debe resolverse degradando la version de Node.js.
- En Windows, los permisos del directorio temporal pueden falsear una prueba;
  por eso el diagnostico debe separar fallo de codigo y fallo de entorno.

## Mejoras siguientes

- Sustituir el fixture sintetico por una ingesta controlada de INEGI en un
  proyecto privado separado.
- Añadir validacion estadistica contra fuentes oficiales y metadatos.
- Medir accesibilidad y rendimiento con un presupuesto explicito.
- Añadir versionado de contratos de datos antes de incorporar nuevos
  indicadores.
