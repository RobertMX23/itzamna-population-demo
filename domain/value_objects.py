from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class IndicatorId:
    value: str

    def __post_init__(self) -> None:
        if not self.value.strip():
            raise ValueError("indicator_id is required")


@dataclass(frozen=True)
class GeographyCode:
    value: str

    def __post_init__(self) -> None:
        if len(self.value) != 2 or not self.value.isdigit():
            raise ValueError("geo_area must be a two-digit code")


@dataclass(frozen=True)
class Period:
    value: str

    def __post_init__(self) -> None:
        if len(self.value) != 4 or not self.value.isdigit():
            raise ValueError("time_period must be a four-digit year")

    @property
    def year(self) -> int:
        return int(self.value)
