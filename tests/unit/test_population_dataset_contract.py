import json
from pathlib import Path

from scripts.validate_population_dataset import validate_catalog


CATALOG_PATH = Path(__file__).parents[2] / "data" / "synthetic" / "catalog.json"


def test_public_population_fixture_matches_data_contract() -> None:
    catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    assert validate_catalog(catalog) == []


def test_unknown_geography_is_reported() -> None:
    catalog = {
        "geographies": [],
        "indicators": [{"indicator_id": "x", "observations": [{"geo_area": "99", "time_period": "2020", "value": 1}]}],
    }
    errors = validate_catalog(catalog)
    assert "x.observations[0].geo_area references an unknown geography" in errors
