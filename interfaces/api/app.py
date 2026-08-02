from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

from fastapi import FastAPI, HTTPException, Query

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from application.metrics import calculate_series
from infrastructure.persistence.repository import PopulationRepository

FIXTURE = PROJECT_ROOT / "data" / "synthetic" / "catalog.json"
repository = PopulationRepository(FIXTURE)
app = FastAPI(title="Project 01 Population API", version="0.1.0")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "source_type": "synthetic"}


@app.get("/api/indicators")
def indicators() -> dict[str, Any]:
    rows = repository.connection.execute(
        "SELECT DISTINCT indicator_id, indicator_name, unit, topic, source_type FROM population_observation ORDER BY indicator_id"
    ).fetchall()
    return {"items": [dict(row) for row in rows], "total": len(rows)}


@app.get("/api/indicators/{indicator_id}/observations")
def observations(indicator_id: str, geo_area: str = Query(min_length=2, max_length=2)) -> dict[str, Any]:
    rows = repository.observations(indicator_id, geo_area)
    if not rows:
        raise HTTPException(status_code=404, detail="No observations found for indicator and geography")
    return {"indicator_id": indicator_id, "geo_area": geo_area, "items": rows, "total": len(rows)}


@app.get("/api/indicators/{indicator_id}/trend")
def trend(indicator_id: str, geo_area: str = Query(min_length=2, max_length=2), window: int = Query(default=5, ge=2, le=20)) -> dict[str, Any]:
    rows = repository.observations(indicator_id, geo_area)
    if not rows:
        raise HTTPException(status_code=404, detail="No observations found for indicator and geography")
    selected = rows[-window:]
    metrics = calculate_series([float(row["value"]) for row in selected])
    items = [
        {**row, "absolute_change": metric.absolute_change, "percent_change": metric.percent_change, "comparable": metric.comparable, "reason": metric.reason}
        for row, metric in zip(selected, metrics)
    ]
    return {"indicator_id": indicator_id, "geo_area": geo_area, "window": window, "items": items, "total": len(items)}
