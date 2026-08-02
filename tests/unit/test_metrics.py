from pathlib import Path
import sys

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from application.metrics import calculate_change, calculate_series


def test_first_period_is_not_comparable() -> None:
    metric = calculate_change(100.0, None)

    assert metric.comparable is False
    assert metric.percent_change is None
    assert metric.reason == "no_previous_period"


def test_change_has_absolute_and_percent_values() -> None:
    metric = calculate_change(110.0, 100.0)

    assert metric.absolute_change == 10.0
    assert metric.percent_change == 10.0
    assert metric.comparable is True


def test_zero_previous_value_is_not_divided() -> None:
    metric = calculate_change(10.0, 0.0)

    assert metric.absolute_change == 10.0
    assert metric.percent_change is None
    assert metric.reason == "zero_previous_value"


def test_series_uses_previous_period() -> None:
    metrics = calculate_series([100.0, 110.0, 99.0])

    assert [metric.percent_change for metric in metrics] == [None, 10.0, -10.0]


@pytest.mark.parametrize("values", [[-1.0], [float("nan")]])
def test_metrics_require_valid_population_values(values: list[float]) -> None:
    with pytest.raises(ValueError):
        calculate_series(values)
