import csv
import sqlite3
from pathlib import Path

from scripts.load_population_sqlite import load_csv_to_sqlite


ROOT = Path(__file__).parents[2]


def test_sqlite_loader_creates_analytical_table(tmp_path: Path) -> None:
    csv_path = ROOT / "data" / "processed" / "population_observations.csv"
    database_path = tmp_path / "population.sqlite3"
    schema_path = ROOT / "queries" / "schema.sql"

    assert load_csv_to_sqlite(csv_path, database_path, schema_path) == 30
    with sqlite3.connect(database_path) as connection:
        assert connection.execute("SELECT COUNT(*) FROM population_observations").fetchone()[0] == 30
        assert connection.execute(
            "SELECT COUNT(*) FROM population_observations WHERE geo_area = '01'"
        ).fetchone()[0] == 10
