import json
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]


def test_population_fixture_is_readable() -> None:
    payload = json.loads((PROJECT_ROOT / "data" / "synthetic" / "catalog.json").read_text(encoding="utf-8"))
    assert payload["source_type"] == "synthetic"
    assert len(payload["indicators"]) == 2
    assert len(payload["geographies"]) == 3


def test_dashboard_contains_critical_user_controls() -> None:
    html = (PROJECT_ROOT / "dashboard" / "index.html").read_text(encoding="utf-8")
    for marker in ["id=\"indicator\"", "id=\"geography\"", "id=\"latest-value\"", "id=\"chart\"", "id=\"ranking\""]:
        assert marker in html


def test_dashboard_assets_exist() -> None:
    assert (PROJECT_ROOT / "dashboard" / "app.js").exists()
    assert (PROJECT_ROOT / "dashboard" / "styles.css").exists()
