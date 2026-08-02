from pathlib import Path

from scripts.load_population_sqlite import load_csv_to_sqlite
from scripts.run_population_queries import run_queries


ROOT = Path(__file__).parents[2]


def test_sql_queries_return_latest_ranking_and_change(tmp_path: Path) -> None:
    database = tmp_path / "population.sqlite3"
    load_csv_to_sqlite(
        ROOT / "data" / "processed" / "population_observations.csv",
        database,
        ROOT / "queries" / "schema.sql",
    )
    report = run_queries(database, "P01-POP-TOTAL")
    assert len(report["summary_by_entity"]) == 3
    assert report["latest_values"][0]["geo_area"] == "01"
    assert report["latest_values"][0]["time_period"] == 2020
    assert len(report["year_over_year_change"]) == 12
    assert round(report["year_over_year_change"][0]["percent_change"], 2) == 2.0
