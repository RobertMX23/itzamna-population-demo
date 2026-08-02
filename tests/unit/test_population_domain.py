import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from domain.entities import PopulationObservation
from domain.value_objects import GeographyCode, IndicatorId, Period


def observation(value: float = 100.0) -> PopulationObservation:
    return PopulationObservation(IndicatorId("P01-POP-TOTAL"), GeographyCode("01"), Period("2020"), value)


def test_population_observation_has_stable_business_key() -> None:
    assert observation().key == ("P01-POP-TOTAL", "01", "2020")


def test_population_value_cannot_be_negative() -> None:
    with pytest.raises(ValueError, match="cannot be negative"):
        observation(-1)


@pytest.mark.parametrize("code", ["1", "001", "XX"])
def test_geography_code_requires_two_digits(code: str) -> None:
    with pytest.raises(ValueError, match="two-digit"):
        GeographyCode(code)


def test_period_exposes_year() -> None:
    assert Period("2020").year == 2020
