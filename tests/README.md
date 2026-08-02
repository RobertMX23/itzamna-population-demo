# QA del proyecto

## Capas

- `unit/`: reglas del dominio, metricas y calidad.
- `integration/`: repositorio y contrato API.
- `smoke/`: fixture, assets y controles criticos del dashboard.

La prueba E2E completa se agregara cuando el dashboard se sirva mediante su
runtime final. No se simula una prueba de navegador con una comprobacion de
texto; cada capa conserva su responsabilidad.
