from copy import deepcopy
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from application.quality import validate_fixture, validate_payload


FIXTURE = Path(__file__).resolve().parents[2] / "data" / "synthetic" / "catalog.json"


def test_synthetic_fixture_passes_quality_rules() -> None:
    report = validate_fixture(FIXTURE)

    assert report.is_valid
    assert report.checked_observations == 30
    assert report.missing_periods == []


def test_quality_report_exposes_duplicate_keys() -> None:
    payload = __import__("json").loads(FIXTURE.read_text(encoding="utf-8"))
    duplicate = deepcopy(payload["indicators"][0]["observations"][0])
    payload["indicators"][0]["observations"].append(duplicate)

    report = validate_payload(payload)

    assert not report.is_valid
    assert report.duplicate_keys == [("P01-POP-TOTAL", "01", "2016")]
