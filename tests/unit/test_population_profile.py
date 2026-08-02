import json
from pathlib import Path

from scripts.profile_population_dataset import profile_catalog


CATALOG_PATH = Path(__file__).parents[2] / "data" / "synthetic" / "catalog.json"


def test_population_profile_reports_expected_coverage() -> None:
    catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    report = profile_catalog(catalog)
    assert report["geography_count"] == 3
    assert report["indicator_count"] == 2
    assert report["observation_count"] == 30
    assert report["periods"] == ["2016", "2017", "2018", "2019", "2020"]
    assert report["duplicate_geo_period_rows"] == 0
    assert report["null_counts"] == {"geo_area": 0, "time_period": 0, "value": 0}
