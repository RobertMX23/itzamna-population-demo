# Proyecto 01: tareas de Data Analyst Junior

## Secuencia

| ID | Tarea | Entregable | Estado |
|---|---|---|---|
| DA-01 | Definir y validar contrato del dataset | Validador Python y pruebas | En curso |
| DA-02 | Perfilar el dataset | Reporte de filas, tipos, nulos y rangos | Completada |
| DA-03 | Normalizar observaciones | Tabla analitica limpia | Completada |
| DA-04 | Cargar SQLite | Base reproducible y esquema SQL | En curso |
| DA-05 | Consultar con SQL | Consultas de resumen y ranking | Pendiente |
| DA-06 | Crear EDA | Notebook o reporte reproducible | Pendiente |
| DA-07 | Integrar filtros de periodo | Dashboard actualizado | Pendiente |
| DA-08 | Redactar insights | Hallazgos, limites y preguntas | Pendiente |
| DA-09 | Automatizar QA | CI con contrato, EDA y smoke tests | Pendiente |

## Regla de alcance

El proyecto demuestra analisis descriptivo junior. No incluye prediccion,
causalidad, scraping de HTML ni credenciales de produccion.

## Tarea actual: DA-04

La tabla plana se genera en `data/processed/population_observations.csv`. La
siguiente tarea es cargar esta tabla a SQLite y definir el esquema analitico.
