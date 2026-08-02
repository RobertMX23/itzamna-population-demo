from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
HTML = (PROJECT_ROOT / "dashboard" / "index.html").read_text(encoding="utf-8")
CSS = (PROJECT_ROOT / "dashboard" / "styles.css").read_text(encoding="utf-8")
LANDING_HTML = (PROJECT_ROOT / "index.html").read_text(encoding="utf-8")
LANDING_CSS = (PROJECT_ROOT / "landing.css").read_text(encoding="utf-8")


def test_dashboard_has_required_semantic_regions() -> None:
    """Protect the default information hierarchy used by the dashboard."""
    for marker in [
        '<main class="shell">',
        "<header>",
        'class="toolbar"',
        'class="metrics"',
        'class="grid"',
        'class="panel"',
        "<footer>",
    ]:
        assert marker in HTML, f"Missing design region: {marker}"


def test_dashboard_design_contract_preserves_responsive_layout() -> None:
    required_css = [
        ".shell { width: min(100% - 48px, 1520px);",
        ".toolbar { grid-template-columns: repeat(2",
        ".metrics { grid-template-columns: repeat(3",
        ".grid { grid-template-columns: 1.4fr 1fr",
        "@media (max-width: 760px)",
        ".toolbar, .metrics, .grid { grid-template-columns: 1fr;",
    ]
    for rule in required_css:
        assert rule in CSS, f"Missing responsive design rule: {rule}"


def test_dashboard_design_contract_avoids_horizontal_overflow() -> None:
    assert "overflow-x: hidden" not in CSS, (
        "Do not hide horizontal overflow to conceal a broken layout; fix the component sizing."
    )


def test_landing_design_contract_preserves_executive_entrypoint() -> None:
    for marker in [
        '<main class="landing-shell">',
        'href="dashboard/"',
        'href="https://github.com/RobertMX23/itzamna-population-demo"',
        'class="evidence"',
    ]:
        assert marker in LANDING_HTML, f"Missing landing region: {marker}"

    for rule in [
        ".landing-shell { width: min(100% - 48px, 1520px);",
        ".hero { display: grid;",
        "@media (max-width: 760px)",
        "@media (prefers-reduced-motion: reduce)",
    ]:
        assert rule in LANDING_CSS, f"Missing landing design rule: {rule}"
