from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from infrastructure.persistence.repository import PopulationRepository


FIXTURE = Path(__file__).resolve().parents[2] / "data" / "synthetic" / "catalog.json"


def test_repository_reads_entity_series_in_period_order() -> None:
    repository = PopulationRepository(FIXTURE)

    rows = repository.observations("P01-POP-TOTAL", "01")

    assert len(rows) == 5
    assert rows[0]["time_period"] == "2016"
    assert rows[-1]["value"] == 1100000
    repository.close()


def test_repository_ranks_entities_for_period() -> None:
    repository = PopulationRepository(FIXTURE)

    rows = repository.ranking("P01-POP-TOTAL", "2020")

    assert [row["geo_area"] for row in rows] == ["01", "02", "03"]
    repository.close()


def test_repository_reports_coverage() -> None:
    repository = PopulationRepository(FIXTURE)

    assert repository.coverage() == [
        {"indicator_id": "P01-POP-MEN", "geographies": 3, "observations": 15},
        {"indicator_id": "P01-POP-TOTAL", "geographies": 3, "observations": 15},
    ]
    repository.close()
