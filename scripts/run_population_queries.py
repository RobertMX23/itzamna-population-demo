"""Run the documented DA-05 SQL queries against the local SQLite database."""

from __future__ import annotations

import argparse
import json
import sqlite3
from pathlib import Path
from typing import Any


QUERIES = {
    "summary_by_entity": """SELECT geo_area, geo_name, COUNT(*) AS observation_count,
        MIN(value) AS minimum_value, MAX(value) AS maximum_value
        FROM population_observations WHERE indicator_id = :indicator_id
        GROUP BY geo_area, geo_name ORDER BY geo_area""",
    "latest_values": """WITH latest_period AS (
        SELECT MAX(time_period) AS time_period FROM population_observations
        WHERE indicator_id = :indicator_id)
        SELECT geo_area, geo_name, time_period, value
        FROM population_observations
        WHERE indicator_id = :indicator_id
        AND time_period = (SELECT time_period FROM latest_period)
        ORDER BY value DESC, geo_area""",
    "year_over_year_change": """WITH series AS (
        SELECT geo_area, geo_name, time_period, value,
        LAG(value) OVER (PARTITION BY indicator_id, geo_area ORDER BY time_period)
        AS previous_value FROM population_observations
        WHERE indicator_id = :indicator_id)
        SELECT geo_area, geo_name, time_period, value, previous_value,
        value - previous_value AS absolute_change,
        CASE WHEN previous_value IS NULL OR previous_value = 0 THEN NULL
        ELSE ((value - previous_value) / previous_value) * 100.0 END AS percent_change
        FROM series WHERE previous_value IS NOT NULL ORDER BY geo_area, time_period""",
}


def run_queries(database_path: Path, indicator_id: str) -> dict[str, list[dict[str, Any]]]:
    """Execute each named query with one explicit indicator parameter."""
    with sqlite3.connect(database_path) as connection:
        connection.row_factory = sqlite3.Row
        return {
            name: [dict(row) for row in connection.execute(query, {"indicator_id": indicator_id})]
            for name, query in QUERIES.items()
        }


def main() -> int:
    parser = argparse.ArgumentParser(description="Run Project 01 SQL analysis queries")
    parser.add_argument("database", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--indicator", default="P01-POP-TOTAL")
    args = parser.parse_args()
    report = run_queries(args.database, args.indicator)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"SQL analysis written: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
