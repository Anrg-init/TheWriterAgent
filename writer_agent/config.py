"""Application configuration and filesystem locations."""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

PACKAGE_DIR = Path(__file__).resolve().parent
PROJECT_DIR = PACKAGE_DIR.parent
load_dotenv(PROJECT_DIR / ".env")

OUTPUT_DIR = Path(os.getenv("WRITER_OUTPUT_DIR", PROJECT_DIR / "output")).expanduser().resolve()
IMAGES_DIR = OUTPUT_DIR / "images"
GOOGLE_MODEL = os.getenv("GOOGLE_MODEL", "gemini-2.5-flash")
GOOGLE_IMAGE_MODEL = os.getenv("GOOGLE_IMAGE_MODEL", "gemini-3.1-flash-image")


def ensure_output_dirs() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)
