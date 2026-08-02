# Insights del Proyecto 01

## Contexto

Este análisis usa el fixture publico sintetico de poblacion total. Su objetivo
es demostrar el flujo de un Data Analyst junior: preparar datos, consultar,
comparar, visualizar y comunicar limites.

## Hechos observados

1. Entidad Norte tiene el valor mas alto en 2020: `1,100,000`.
2. Entidad Centro tiene `910,000` en 2020.
3. Entidad Sur tiene `715,000` en 2020.
4. Las tres entidades tienen cinco observaciones, de 2016 a 2020.
5. Las tres entidades terminan el periodo por encima de su valor inicial.

## Metricas derivadas

| Entidad | Cambio 2016-2020 | Lectura descriptiva |
|---|---:|---|
| Entidad Norte | `+10.00%` | Mayor crecimiento acumulado del fixture |
| Entidad Centro | `+1.11%` | Crecimiento acumulado moderado |
| Entidad Sur | `+2.14%` | Crecimiento acumulado positivo |

La formula utilizada es:

```text
((valor_final - valor_inicial) / valor_inicial) * 100
```

## Interpretacion responsable

El fixture muestra niveles y ritmos distintos entre entidades. La diferencia
entre valores puede orientar una pregunta de negocio o una siguiente consulta,
pero no explica por que cambia la poblacion. Para explicar causas se
necesitarian datos oficiales adicionales sobre nacimientos, defunciones,
migracion, estructura por edad y metodologia de medicion.

## Preguntas de seguimiento

- La tendencia se mantiene cuando se incorporan todos los estados reales?
- El crecimiento observado se relaciona con natalidad, migracion o cambios de
  cobertura?
- Como cambia la lectura al bajar de entidad a municipio?
- Los indicadores de hombres y poblacion total son coherentes entre si?

## Limitaciones

- Los valores son sinteticos y no representan cifras oficiales de INEGI.
- Cinco periodos no bastan para establecer una tendencia demografica de largo
  plazo.
- No se mide causalidad ni se hace pronostico.
- Los porcentajes son calculados por el proyecto y no sustituyen metadatos
  metodologicos oficiales.
