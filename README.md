# Itzamna Population Demo

Dashboard analitico de demostracion para explorar poblacion por entidad y
periodo. Este repositorio es una exportacion sanitizada del proyecto privado
Itzamna.

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

Dashboard: `http://127.0.0.1:8080/dashboard/`

## Publicacion en GitHub Pages

El workflow `deploy-pages` publica este demo como sitio estatico. En el
repositorio publico, habilita `Settings > Pages > Source: GitHub Actions` y
abre la URL que GitHub muestre en el entorno `github-pages`. La entrada raiz
enlaza al dashboard en `/dashboard/`.

La publicacion no contiene secretos, tokens, datos oficiales descargados ni
una API de produccion. El backend y la integracion privada permanecen fuera
de este demo.

## Aviso de datos

Los datos son ficticios y no representan cifras oficiales de INEGI.
