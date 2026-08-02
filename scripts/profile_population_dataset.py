"""Generate a deterministic profile for the Project 01 population fixture."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any


def profile_catalog(catalog: dict[str, Any]) -> dict[str, Any]:
    """Return descriptive quality and coverage statistics without changing data."""
    observations = [
        observation
        for indicator in catalog.get("indicators", [])
        for observation in indicator.get("observations", [])
    ]
    value_fields = sorted({key for row in observations for key in row})
    periods = sorted({row.get("time_period") for row in observations if row.get("time_period") is not None})
    values = [row["value"] for row in observations if isinstance(row.get("value"), (int, float))]
    keys = [
        (indicator.get("indicator_id"), row.get("geo_area"), row.get("time_period"))
        for indicator in catalog.get("indicators", [])
        for row in indicator.get("observations", [])
    ]
    duplicate_count = len(keys) - len(set(keys))

    return {
        "dataset": catalog.get("dataset"),
        "source_type": catalog.get("source_type"),
        "geography_count": len(catalog.get("geographies", [])),
        "indicator_count": len(catalog.get("indicators", [])),
        "observation_count": len(observations),
        "observation_fields": value_fields,
        "null_counts": {field: sum(row.get(field) is None for row in observations) for field in value_fields},
        "duplicate_geo_period_rows": duplicate_count,
        "periods": periods,
        "period_count": len(periods),
        "value_range": {"min": min(values) if values else None, "max": max(values) if values else None},
        "observations_by_geography": dict(sorted(Counter(row.get("geo_area") for row in observations).items())),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Profile the Project 01 population fixture")
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    catalog = json.loads(args.input.read_text(encoding="utf-8"))
    report = profile_catalog(catalog)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Profile written: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
