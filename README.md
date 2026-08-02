# Itzamna Population Demo

Demo publico de un dashboard analitico para explorar poblacion por entidad y
periodo. Es una exportacion sanitizada del proyecto privado Itzamna y esta
enfocado en mostrar practicas de analisis de datos, arquitectura modular y
calidad de software.

## Ver demo

- [Abrir sitio publico](https://robertmx23.github.io/itzamna-population-demo/)
- [Abrir dashboard](https://robertmx23.github.io/itzamna-population-demo/dashboard/)

El sitio se publica con GitHub Pages mediante el workflow
[`deploy-pages`](.github/workflows/pages.yml). El workflow [`ci`](.github/workflows/ci.yml)
ejecuta las pruebas antes de integrar cambios.

## Lectura ejecutiva

Este demo muestra un flujo reproducible para:

- Catalogar indicadores por entidad, periodo y unidad.
- Explorar una serie historica de poblacion.
- Aplicar filtros y consultar un ranking comparativo.
- Validar el comportamiento con pruebas automatizadas.

El alcance es intencionalmente pequeno: sirve como evidencia tecnica y
visual, no como sustituto de una plataforma de produccion.

## Incluye

- Dataset sintetico.
- SQL y repositorio SQLite en memoria.
- Modelo de dominio sencillo.
- API FastAPI de lectura.
- Dashboard HTML/CSS/JavaScript.
- Pruebas unitarias, integracion y smoke.

## Ejecucion local

```powershell
python -m pip install -r requirements.txt
python -m pytest -q
python -m http.server 8080
```

Portada: `http://127.0.0.1:8080/`

Dashboard: `http://127.0.0.1:8080/dashboard/`

## Seguridad y alcance

La publicacion no contiene secretos, tokens, datos oficiales descargados ni
una API de produccion. El backend y la integracion privada permanecen fuera
de este demo. Consulta [SECURITY.md](SECURITY.md) para el limite de seguridad
y [LICENSE](LICENSE) para las condiciones de uso.

## Aviso de datos

Los datos son ficticios y no representan cifras oficiales de INEGI.
