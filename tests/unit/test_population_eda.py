from pathlib import Path

from scripts.generate_population_eda import generate_report
from scripts.load_population_sqlite import load_csv_to_sqlite


ROOT = Path(__file__).parents[2]


def test_eda_report_contains_findings_and_limitations(tmp_path: Path) -> None:
    database = tmp_path / "population.sqlite3"
    load_csv_to_sqlite(
        ROOT / "data" / "processed" / "population_observations.csv",
        database,
        ROOT / "queries" / "schema.sql",
    )
    report = generate_report(
        database,
        ROOT / "docs" / "analysis" / "population_profile.json",
        "P01-POP-TOTAL",
    )
    assert "## Tendencia observada" in report
    assert "Entidad Norte" in report
    assert "## Limitaciones" in report
    assert "sinteticos" in report
