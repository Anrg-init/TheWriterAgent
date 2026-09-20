"""Application configuration and filesystem locations."""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv
import streamlit as st

PACKAGE_DIR = Path(__file__).resolve().parent
PROJECT_DIR = PACKAGE_DIR.parent
load_dotenv(PROJECT_DIR / ".env")


def _load_cloud_secrets() -> None:
    """Expose Streamlit Cloud secrets to provider SDKs that read env vars."""
    try:
        for key in ("GOOGLE_API_KEY", "TAVILY_API_KEY", "GOOGLE_MODEL", "GOOGLE_IMAGE_MODEL"):
            if not os.getenv(key) and key in st.secrets:
                os.environ[key] = str(st.secrets[key])
    except Exception:
        # Local runs without a secrets file should continue using .env/defaults.
        pass


_load_cloud_secrets()

OUTPUT_DIR = Path(os.getenv("WRITER_OUTPUT_DIR", PROJECT_DIR / "output")).expanduser().resolve()
IMAGES_DIR = OUTPUT_DIR / "images"
GOOGLE_MODEL = os.getenv("GOOGLE_MODEL", "gemini-2.5-flash")
GOOGLE_IMAGE_MODEL = os.getenv("GOOGLE_IMAGE_MODEL", "gemini-3.1-flash-image")


def ensure_output_dirs() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)
