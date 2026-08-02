from __future__ import annotations

import json
import sqlite3
from pathlib import Path
from typing import Any


SCHEMA = """
CREATE TABLE population_observation (
    indicator_id TEXT NOT NULL,
    indicator_name TEXT NOT NULL,
    geo_area TEXT NOT NULL,
    time_period TEXT NOT NULL,
    value REAL NOT NULL,
    unit TEXT NOT NULL,
    topic TEXT NOT NULL,
    source_type TEXT NOT NULL,
    PRIMARY KEY (indicator_id, geo_area, time_period)
)
"""


class PopulationRepository:
    """Read-only SQLite adapter for the project fixture."""

    def __init__(self, fixture_path: Path) -> None:
        self.connection = sqlite3.connect(":memory:", check_same_thread=False)
        self.connection.row_factory = sqlite3.Row
        self.connection.execute(SCHEMA)
        self._load_fixture(fixture_path)

    def _load_fixture(self, fixture_path: Path) -> None:
        payload: dict[str, Any] = json.loads(fixture_path.read_text(encoding="utf-8"))
        rows = []
        for indicator in payload["indicators"]:
            for observation in indicator["observations"]:
                rows.append(
                    (
                        indicator["indicator_id"],
                        indicator["indicator_name"],
                        observation["geo_area"],
                        observation["time_period"],
                        observation["value"],
                        indicator["unit"],
                        indicator["topic"],
                        payload["source_type"],
                    )
                )
        self.connection.executemany(
            "INSERT INTO population_observation VALUES (?, ?, ?, ?, ?, ?, ?, ?)", rows
        )
        self.connection.commit()

    def observations(self, indicator_id: str, geo_area: str) -> list[dict[str, Any]]:
        rows = self.connection.execute(
            """
            SELECT indicator_id, geo_area, time_period, value
            FROM population_observation
            WHERE indicator_id = ? AND geo_area = ?
            ORDER BY time_period
            """,
            (indicator_id, geo_area),
        ).fetchall()
        return [dict(row) for row in rows]

    def ranking(self, indicator_id: str, time_period: str) -> list[dict[str, Any]]:
        rows = self.connection.execute(
            """
            SELECT geo_area, SUM(value) AS value
            FROM population_observation
            WHERE indicator_id = ? AND time_period = ?
            GROUP BY geo_area
            ORDER BY value DESC
            """,
            (indicator_id, time_period),
        ).fetchall()
        return [dict(row) for row in rows]

    def coverage(self) -> list[dict[str, Any]]:
        rows = self.connection.execute(
            """
            SELECT indicator_id, COUNT(DISTINCT geo_area) AS geographies,
                   COUNT(*) AS observations
            FROM population_observation
            GROUP BY indicator_id
            ORDER BY indicator_id
            """
        ).fetchall()
        return [dict(row) for row in rows]

    def close(self) -> None:
        self.connection.close()
