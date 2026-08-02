"""Validate the public population fixture before analysis."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any

REQUIRED_CATALOG_KEYS = {"dataset", "source_type", "metadata", "geographies", "indicators"}
REQUIRED_OBSERVATION_KEYS = {"geo_area", "time_period", "value"}


def validate_catalog(catalog: dict[str, Any]) -> list[str]:
    """Return actionable contract violations without mutating the input."""
    errors: list[str] = []
    errors.extend(_missing_keys(catalog, REQUIRED_CATALOG_KEYS, "catalog"))
    geographies = catalog.get("geographies", [])
    geography_codes = {item.get("geo_area") for item in geographies if isinstance(item, dict)}
    if len(geography_codes) != len(geographies):
        errors.append("geographies.geo_area must be unique")
    for indicator in catalog.get("indicators", []):
        if not isinstance(indicator, dict):
            errors.append("indicators must contain objects")
            continue
        indicator_id = indicator.get("indicator_id", "<missing>")
        seen: set[tuple[Any, Any]] = set()
        for index, observation in enumerate(indicator.get("observations", [])):
            location = f"{indicator_id}.observations[{index}]"
            if not isinstance(observation, dict):
                errors.append(f"{location} must be an object")
                continue
            errors.extend(_missing_keys(observation, REQUIRED_OBSERVATION_KEYS, location))
            key = (observation.get("geo_area"), observation.get("time_period"))
            if key in seen:
                errors.append(f"{location} duplicates geo_area and time_period")
            seen.add(key)
            if observation.get("geo_area") not in geography_codes:
                errors.append(f"{location}.geo_area references an unknown geography")
            value = observation.get("value")
            if not isinstance(value, (int, float)) or isinstance(value, bool) or not math.isfinite(value):
                errors.append(f"{location}.value must be a finite number")
    return errors


def _missing_keys(value: dict[str, Any], required: set[str], location: str) -> list[str]:
    """Build stable messages so CI output is easy to act on."""
    return [f"{location} is missing {key}" for key in sorted(required - value.keys())]


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the Project 01 population fixture")
    parser.add_argument("path", type=Path)
    args = parser.parse_args()
    catalog = json.loads(args.path.read_text(encoding="utf-8"))
    errors = validate_catalog(catalog)
    if errors:
        print("Dataset contract failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"Dataset contract passed: {args.path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
