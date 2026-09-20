"""Streamlit entry point for The Writer Agent."""

import runpy
from pathlib import Path


runpy.run_path(
    str(Path(__file__).resolve().parent / "writer_agent" / "ui.py"),
    init_globals={"__package__": "writer_agent"},
)
