# Diccionario de datos

Define significado, tipo, unidad, origen y uso antes de construir el dataset.

## Indicador

| Campo | Tipo | Descripcion | Origen | Uso |
|---|---|---|---|---|
| `indicator_id` | texto | Clave unica del indicador | INEGI | Identidad y joins |
| `indicator_name` | texto | Nombre legible | INEGI | Titulo y busqueda |
| `FREQ` | texto | Frecuencia de observacion | INEGI | Contexto temporal |
| `TOPIC` | texto | Tema | INEGI | Filtro |
| `UNIT` | texto | Unidad de medida | INEGI | Etiqueta y filtro |
| `UNIT_MULT` | texto | Multiplicador | INEGI | Interpretacion numerica |
| `NOTE` | texto | Nota metodologica | INEGI | Limitaciones |
| `SOURCE` | texto | Fuente declarada | INEGI | Provenance |
| `LASTUPDATE` | fecha/texto | Ultima actualizacion | INEGI | Vigencia |
| `STATUS` | texto | Estado declarado | INEGI | Calidad descriptiva |

## Observacion

| Campo | Tipo | Descripcion | Origen | Uso |
|---|---|---|---|---|
| `TIME_PERIOD` | texto | Periodo de referencia | INEGI | Eje temporal |
| `OBS_VALUE` | numero/texto | Valor observado | INEGI | Visualizaciones |
| `OBS_STATUS` | texto | Estado de observacion | INEGI | Calidad |
| `OBS_SOURCE` | texto | Fuente de observacion | INEGI | Provenance |
| `OBS_NOTE` | texto | Nota de observacion | INEGI | Interpretacion |
| `COBER_GEO` | texto | Cobertura geografica | INEGI | Nivel territorial |

## Dimensiones y metricas derivadas

| Campo | Regla |
|---|---|
| `geo_area` | Codigo geografico como texto, conservando ceros iniciales |
| `geo_name` | Nombre geografico para presentacion |
| `fetched_at` | Momento de extraccion del sistema |
| `absolute_change` | `current - previous` |
| `percent_change` | `((current - previous) / previous) * 100` |
| `rank` | Orden por valor dentro de un periodo |

## Reglas de calidad

- `indicator_id`, `geo_area` y `TIME_PERIOD` son obligatorios.
- `OBS_VALUE` debe ser numerico para calcular variaciones.
- Los faltantes no se eliminan silenciosamente.
- El primer periodo no tiene variacion porcentual.
- Si el valor anterior es cero, la variacion es no disponible.
- Las metricas derivadas no son datos oficiales.
- El fixture publico usa `source_type=synthetic`.
