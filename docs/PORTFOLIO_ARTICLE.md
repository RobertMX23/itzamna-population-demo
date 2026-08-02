# Bienvenido al Proyecto 01: Population Dashboard

## Que vas a encontrar

Bienvenido a este primer proyecto de portafolio. Aquí vas a encontrar una
demostración pequeña, reproducible y deliberadamente acotada de cómo convierto
datos en una lectura útil para tomar decisiones.

El proyecto utiliza un dataset sintético inspirado en indicadores de población.
No vas a encontrar secretos, credenciales ni una conexión productiva. Vas a
encontrar el proceso técnico y analítico que permite construir una solución de
forma ordenada, verificable y fácil de explicar.

## El problema que resolví

Cuando tienes indicadores separados por entidad y periodo, encontrar una
respuesta sencilla puede requerir revisar varias tablas, limpiar nombres,
comparar fechas y construir cálculos manualmente.

En este proyecto construí una vista que te permite seleccionar un indicador,
una entidad y un periodo. A partir de esa selección puedes revisar el último
valor disponible, el cambio porcentual, la serie temporal y un ranking
comparativo.

## El recorrido de los datos

El proyecto sigue una secuencia reproducible:

1. Definí un contrato para conocer la estructura esperada del dataset.
2. Validé identificadores, geografías, periodos y observaciones.
3. Perfileré filas, tipos, valores nulos y rangos.
4. Normalicé los registros en una tabla analítica.
5. Cargué la información en SQLite.
6. Escribí consultas SQL para obtener resúmenes, cambios y rankings.
7. Generé un reporte de EDA con hallazgos y limitaciones.
8. Construí el dashboard para explorar los resultados.
9. Añadí pruebas automatizadas y un quality gate en CI.

## Qué habilidades demuestra

Este proyecto demuestra principalmente un nivel de Data Analyst junior sólido.
También incorpora prácticas de nivel intermedio en varias áreas:

- Python para validación, transformación y automatización.
- SQL para consultas analíticas y ranking.
- SQLite como almacenamiento reproducible.
- HTML, CSS y JavaScript para visualización interactiva.
- Pruebas unitarias, de integración, smoke y E2E.
- GitHub Actions para integración continua.
- Contratos de diseño responsive y control de overflow.
- Documentación de insights, decisiones y límites.
- Separación modular entre datos, dominio, infraestructura y presentación.

## Cómo leer el resultado

El dashboard no intenta sustituir un sistema estadístico oficial. Su objetivo
es ayudarte a explorar una selección de datos y reconocer patrones
descriptivos.

Por ejemplo, puedes observar qué entidad tiene el mayor valor en el último
periodo, cómo cambia una serie temporal o qué diferencia existe entre entidades.
Estas lecturas sirven para formular preguntas; no prueban causalidad ni
explican por sí mismas los motivos demográficos detrás de un cambio.

## Qué nivel profesional representa

La fortaleza del proyecto no está únicamente en mostrar una gráfica. Está en
mostrar el recorrido completo: contrato, calidad, transformación, consulta,
visualización, pruebas y documentación.

Por eso lo presento como un proyecto de **Data Analysis reproducible con
fundamentos de data engineering, frontend, QA automatizado y CI/CD**.

Todavía no lo presento como una plataforma senior de producción. Para llegar a
ese nivel tendría que incorporar datos oficiales a escala, observabilidad,
seguridad operativa, rendimiento, despliegue cloud, modelos estadísticos y
operación continua.

## Qué puedes revisar después

- La [ficha de entrega](DELIVERY.md) resume la evidencia técnica.
- La [retrospectiva](RETROSPECTIVE.md) explica aprendizajes y siguientes mejoras.
- El [reporte EDA](analysis/population_eda.md) muestra la lectura descriptiva.
- El [dashboard público](https://robertmx23.github.io/itzamna-population-demo/dashboard/)
  permite explorar la interfaz.

Este primer proyecto es el punto de partida. La intención es que cada proyecto
siguiente aumente la profundidad analítica sin perder reproducibilidad,
claridad ni control sobre la calidad.
