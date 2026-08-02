from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class QualityReport:
    checked_observations: int
    missing_required_fields: list[str]
    duplicate_keys: list[tuple[str, str, str]]
    non_numeric_values: list[tuple[str, str, str]]
    missing_periods: list[tuple[str, str, str]]
    inconsistent_units: list[str]

    @property
    def is_valid(self) -> bool:
        return not any(
            (
                self.missing_required_fields,
                self.duplicate_keys,
                self.non_numeric_values,
                self.missing_periods,
                self.inconsistent_units,
            )
        )


def validate_fixture(path: Path) -> QualityReport:
    payload: dict[str, Any] = json.loads(path.read_text(encoding="utf-8"))
    return validate_payload(payload)


def validate_payload(payload: dict[str, Any]) -> QualityReport:
    required = {"geo_area", "time_period", "value"}
    missing: list[str] = []
    duplicate_keys: list[tuple[str, str, str]] = []
    non_numeric: list[tuple[str, str, str]] = []
    seen: set[tuple[str, str, str]] = set()
    periods_by_group: dict[tuple[str, str], set[str]] = {}
    units_by_indicator: dict[str, set[str]] = {}
    checked = 0

    for indicator in payload.get("indicators", []):
        indicator_id = str(indicator.get("indicator_id", ""))
        units_by_indicator.setdefault(indicator_id, set()).add(str(indicator.get("unit", "")))
        for observation in indicator.get("observations", []):
            checked += 1
            missing.extend(sorted(required - observation.keys()))
            key = (indicator_id, str(observation.get("geo_area", "")), str(observation.get("time_period", "")))
            if key in seen:
                duplicate_keys.append(key)
            seen.add(key)
            if not isinstance(observation.get("value"), (int, float)):
                non_numeric.append(key)
            periods_by_group.setdefault((indicator_id, key[1]), set()).add(key[2])

    expected_periods = {str(period) for period in range(2016, 2021)}
    missing_periods = [
        (indicator_id, geo_area, period)
        for (indicator_id, geo_area), periods in periods_by_group.items()
        for period in sorted(expected_periods - periods)
    ]
    inconsistent_units = [indicator_id for indicator_id, units in units_by_indicator.items() if len(units) > 1]
    return QualityReport(checked, missing, duplicate_keys, non_numeric, missing_periods, inconsistent_units)
