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

## Aviso de datos

Los datos son ficticios y no representan cifras oficiales de INEGI.
