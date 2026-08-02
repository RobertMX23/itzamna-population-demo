from __future__ import annotations

from dataclasses import dataclass

from .value_objects import GeographyCode, IndicatorId, Period


@dataclass(frozen=True)
class PopulationObservation:
    indicator_id: IndicatorId
    geo_area: GeographyCode
    time_period: Period
    value: float
    source_type: str = "synthetic"

    def __post_init__(self) -> None:
        if self.value < 0:
            raise ValueError("population value cannot be negative")
        if self.source_type not in {"official", "synthetic"}:
            raise ValueError("source_type must be official or synthetic")

    @property
    def key(self) -> tuple[str, str, str]:
        return (self.indicator_id.value, self.geo_area.value, self.time_period.value)
