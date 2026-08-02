# Ficha de entrega: Proyecto 01

## Objetivo

Demostrar un flujo reproducible de Data Analyst junior usando un dataset
sintetico de poblacion: contrato, perfilado, limpieza, SQL, EDA, visualizacion
y QA automatizado.

## Evidencia tecnica

| Capacidad | Evidencia |
|---|---|
| Python | `scripts/` y pruebas unitarias |
| Calidad de datos | contrato, perfil y normalizacion |
| SQL | `queries/schema.sql` y reporte de analisis |
| Visualizacion | `dashboard/` con filtros, serie y ranking |
| QA | `tests/unit`, `tests/integration`, `tests/smoke` y `tests/e2e` |
| CI/CD | `.github/workflows/ci.yml` y `pages.yml` |
| Gobernanza | `governance/` y `SECURITY.md` |

## Resultado verificable

- `39` pruebas Python pasan localmente.
- La sintaxis de `dashboard/app.js` se valida con Node.js 24.
- CI genera evidencia analitica como artefacto.
- La demo publica esta disponible en [GitHub Pages](https://robertmx23.github.io/itzamna-population-demo/).

## Limites declarados

Este repositorio es una demostracion publica sanitizada. Usa datos
sinteticos, no contiene tokens ni conexion productiva, y no pretende resolver
prediccion, causalidad o analisis demografico oficial.

## Reproduccion minima

```powershell
python -m pip install -r requirements.txt
python -m pytest -q
python -m http.server 8080
```

Abrir `http://127.0.0.1:8080/dashboard/` para revisar el dashboard.
