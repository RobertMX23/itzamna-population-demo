from __future__ import annotations

from dataclasses import dataclass
from math import isfinite


@dataclass(frozen=True)
class ChangeMetric:
    current: float
    previous: float | None
    absolute_change: float | None
    percent_change: float | None
    comparable: bool
    reason: str | None = None


def calculate_change(current: float, previous: float | None) -> ChangeMetric:
    """Calculate descriptive change without presenting causality."""
    if not isfinite(current) or current < 0:
        raise ValueError("population values must be finite and non-negative")
    if previous is not None and (not isfinite(previous) or previous < 0):
        raise ValueError("population values must be finite and non-negative")
    if previous is None:
        return ChangeMetric(current, None, None, None, False, "no_previous_period")
    absolute_change = current - previous
    if previous == 0:
        return ChangeMetric(current, previous, absolute_change, None, False, "zero_previous_value")
    percent_change = round((absolute_change / previous) * 100, 2)
    return ChangeMetric(current, previous, absolute_change, percent_change, True)


def calculate_series(values: list[float]) -> list[ChangeMetric]:
    """Calculate each value against the immediately previous value."""
    metrics: list[ChangeMetric] = []
    previous: float | None = None
    for value in values:
        metric = calculate_change(value, previous)
        metrics.append(metric)
        previous = value
    return metrics
