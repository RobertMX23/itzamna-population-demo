from pathlib import Path
import sys

from fastapi.testclient import TestClient

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from interfaces.api.app import app


client = TestClient(app)


def test_health_contract() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["source_type"] == "synthetic"


def test_catalog_contract() -> None:
    response = client.get("/api/indicators")

    assert response.status_code == 200
    assert response.json()["total"] == 2


def test_observations_contract() -> None:
    response = client.get("/api/indicators/P01-POP-TOTAL/observations?geo_area=01")

    assert response.status_code == 200
    assert response.json()["total"] == 5


def test_trend_contract_has_derived_metrics() -> None:
    response = client.get("/api/indicators/P01-POP-TOTAL/trend?geo_area=01&window=5")

    assert response.status_code == 200
    assert response.json()["items"][0]["comparable"] is False
    assert response.json()["items"][-1]["percent_change"] == 2.8


def test_unknown_indicator_returns_explicit_not_found() -> None:
    response = client.get("/api/indicators/UNKNOWN/observations?geo_area=01")

    assert response.status_code == 404
