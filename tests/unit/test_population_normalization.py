import json
from pathlib import Path

from scripts.normalize_population_dataset import OUTPUT_FIELDS, normalize_catalog


CATALOG_PATH = Path(__file__).parents[2] / "data" / "synthetic" / "catalog.json"


def test_normalization_creates_analysis_ready_rows() -> None:
    catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    rows = normalize_catalog(catalog)
    assert len(rows) == 30
    assert list(rows[0]) == OUTPUT_FIELDS
    assert rows[0]["geo_name"] in {"Entidad Norte", "Entidad Centro", "Entidad Sur"}
    assert rows[0]["source_type"] == "synthetic"


def test_normalization_preserves_geography_codes_as_text() -> None:
    catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    rows = normalize_catalog(catalog)
    assert {row["geo_area"] for row in rows} == {"01", "02", "03"}
