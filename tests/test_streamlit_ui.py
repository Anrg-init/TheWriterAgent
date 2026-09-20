from streamlit.testing.v1 import AppTest
from pathlib import Path


def test_frontend_renders_main_controls() -> None:
    app = AppTest.from_file(Path(__file__).parents[1] / "frontend.py").run(timeout=30)

    assert not app.exception
    assert [item.value for item in app.title] == ["Blog Writing Agent"]
    assert [item.label for item in app.sidebar.button] == ["🚀 Generate Blog"]
