from pathlib import Path


INSIGHTS = Path(__file__).parents[2] / "docs" / "analysis" / "population_insights.md"


def test_insights_document_separates_evidence_from_limitations() -> None:
    content = INSIGHTS.read_text(encoding="utf-8")
    assert "## Hechos observados" in content
    assert "## Interpretacion responsable" in content
    assert "## Limitaciones" in content
    assert "sinteticos" in content
    assert "natalidad" in content
