"""Load normalized population observations into a reproducible SQLite database."""

from __future__ import annotations

import argparse
import csv
import sqlite3
from pathlib import Path


def load_csv_to_sqlite(csv_path: Path, database_path: Path, schema_path: Path) -> int:
    """Replace the analytical table and return the number of loaded rows."""
    database_path.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(database_path) as connection:
        connection.executescript(schema_path.read_text(encoding="utf-8"))
        connection.execute("DELETE FROM population_observations")
        with csv_path.open(encoding="utf-8", newline="") as source:
            rows = list(csv.DictReader(source))
        connection.executemany(
            """INSERT INTO population_observations
            (indicator_id, indicator_name, topic, topic_label, unit, unit_label,
             geo_area, geo_name, time_period, value, source_type)
            VALUES (:indicator_id, :indicator_name, :topic, :topic_label, :unit,
                    :unit_label, :geo_area, :geo_name, :time_period, :value,
                    :source_type)""",
            rows,
        )
        connection.commit()
    return len(rows)


def main() -> int:
    parser = argparse.ArgumentParser(description="Load normalized population data into SQLite")
    parser.add_argument("csv_path", type=Path)
    parser.add_argument("database_path", type=Path)
    parser.add_argument("schema_path", type=Path)
    args = parser.parse_args()
    count = load_csv_to_sqlite(args.csv_path, args.database_path, args.schema_path)
    print(f"SQLite load passed: {count} rows -> {args.database_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
