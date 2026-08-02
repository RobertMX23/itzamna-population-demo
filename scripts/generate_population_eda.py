"""Generate a concise exploratory data analysis report for Project 01."""

from __future__ import annotations

import argparse
import json
import sqlite3
from pathlib import Path


def generate_report(database_path: Path, profile_path: Path, indicator_id: str) -> str:
    """Build a deterministic EDA narrative from stored profile and SQL data."""
    profile = json.loads(profile_path.read_text(encoding="utf-8"))
    with sqlite3.connect(database_path) as connection:
        connection.row_factory = sqlite3.Row
        rows = connection.execute(
            """SELECT geo_area, geo_name, time_period, value
            FROM population_observations
            WHERE indicator_id = ? ORDER BY geo_area, time_period""",
            (indicator_id,),
        ).fetchall()
    by_geo: dict[str, list[sqlite3.Row]] = {}
    for row in rows:
        by_geo.setdefault(row["geo_area"], []).append(row)
    trend_lines = []
    for geo_rows in by_geo.values():
        first, last = geo_rows[0], geo_rows[-1]
        change = ((last["value"] - first["value"]) / first["value"]) * 100
        direction = "crecio" if change > 0 else "disminuyo" if change < 0 else "se mantuvo"
        trend_lines.append(
            f"- **{last['geo_name']}**: {direction} {abs(change):.2f}% "
            f"entre {first['time_period']} y {last['time_period']}."
        )
    latest = max(rows, key=lambda row: row["time_period"])
    latest_rows = [row for row in rows if row["time_period"] == latest["time_period"]]
    ranking = sorted(latest_rows, key=lambda row: row["value"], reverse=True)
    ranking_lines = [f"{index}. {row['geo_name']}: {row['value']:,}" for index, row in enumerate(ranking, 1)]
    return f"""# EDA: poblacion total

## Pregunta analitica

Como cambia la poblacion entre entidades y periodos dentro del fixture del Proyecto 01?

## Perfil del dataset

| Metrica | Resultado |
|---|---:|
| Fuente | `{profile['source_type']}` |
| Geografias | {profile['geography_count']} |
| Indicadores | {profile['indicator_count']} |
| Observaciones | {profile['observation_count']} |
| Periodos | {profile['period_count']} ({profile['periods'][0]}-{profile['periods'][-1]}) |
| Nulos | {sum(profile['null_counts'].values())} |
| Duplicados geo-periodo | {profile['duplicate_geo_period_rows']} |

## Tendencia observada

{chr(10).join(trend_lines)}

## Ranking del ultimo periodo ({latest['time_period']})

{chr(10).join(ranking_lines)}

## Interpretacion junior

El fixture muestra diferencias descriptivas entre entidades y una tendencia
temporal no uniforme. Estos resultados sirven para practicar limpieza,
agregacion, comparacion y comunicacion; no representan cifras oficiales de
INEGI ni permiten inferir causas demograficas.

## Limitaciones

- Los datos son sinteticos y no deben usarse para decisiones reales.
- El periodo cubre solo cinco observaciones por entidad.
- No se incluyen nacimientos, defunciones, migracion ni municipios.
- El porcentaje es una metrica derivada, no un valor oficial.
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate Project 01 EDA report")
    parser.add_argument("database", type=Path)
    parser.add_argument("profile", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--indicator", default="P01-POP-TOTAL")
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(generate_report(args.database, args.profile, args.indicator), encoding="utf-8")
    print(f"EDA report written: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
