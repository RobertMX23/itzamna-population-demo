"""Flatten the population catalog into an analysis-ready table."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any, Iterable


OUTPUT_FIELDS = [
    "indicator_id",
    "indicator_name",
    "topic",
    "topic_label",
    "unit",
    "unit_label",
    "geo_area",
    "geo_name",
    "time_period",
    "value",
    "source_type",
]


def normalize_catalog(catalog: dict[str, Any]) -> list[dict[str, Any]]:
    """Return one flat row per indicator, geography and observation period."""
    geography_names = {
        geography["geo_area"]: geography["geo_name"]
        for geography in catalog.get("geographies", [])
    }
    rows: list[dict[str, Any]] = []
    for indicator in catalog.get("indicators", []):
        for observation in indicator.get("observations", []):
            rows.append(
                {
                    "indicator_id": indicator["indicator_id"],
                    "indicator_name": indicator["indicator_name"],
                    "topic": indicator.get("topic"),
                    "topic_label": indicator.get("topic_label"),
                    "unit": indicator.get("unit"),
                    "unit_label": indicator.get("unit_label"),
                    "geo_area": observation["geo_area"],
                    "geo_name": geography_names[observation["geo_area"]],
                    "time_period": observation["time_period"],
                    "value": observation["value"],
                    "source_type": catalog.get("source_type"),
                }
            )
    return sorted(rows, key=lambda row: (row["indicator_id"], row["geo_area"], row["time_period"]))


def write_csv(rows: Iterable[dict[str, Any]], output: Path) -> None:
    """Write a stable UTF-8 CSV that can be loaded by SQLite or a spreadsheet."""
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=OUTPUT_FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser(description="Normalize the Project 01 population fixture")
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    catalog = json.loads(args.input.read_text(encoding="utf-8"))
    rows = normalize_catalog(catalog)
    write_csv(rows, args.output)
    print(f"Normalized rows written: {len(rows)} -> {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
