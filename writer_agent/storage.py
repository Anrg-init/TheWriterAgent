"""Persistence helpers for generated markdown and image bundles."""

from __future__ import annotations

import re
import zipfile
from io import BytesIO
from pathlib import Path
from typing import Optional

from .config import IMAGES_DIR, OUTPUT_DIR, ensure_output_dirs


def safe_slug(title: str) -> str:
    slug = re.sub(r"[^a-z0-9 _-]+", "", title.strip().lower())
    slug = re.sub(r"\s+", "_", slug).strip("_")
    return slug or "blog"


def list_past_blogs() -> list[Path]:
    ensure_output_dirs()
    return sorted(OUTPUT_DIR.glob("*.md"), key=lambda path: path.stat().st_mtime, reverse=True)


def read_markdown(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def extract_title(markdown: str, fallback: str = "blog") -> str:
    for line in markdown.splitlines():
        if line.startswith("# "):
            return line[2:].strip() or fallback
    return fallback


def bundle_zip(markdown: str, markdown_filename: str) -> bytes:
    ensure_output_dirs()
    buffer = BytesIO()
    with zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr(markdown_filename, markdown.encode("utf-8"))
        for path in IMAGES_DIR.rglob("*"):
            if path.is_file():
                archive.write(path, arcname=path.relative_to(OUTPUT_DIR))
    return buffer.getvalue()


def images_zip() -> Optional[bytes]:
    ensure_output_dirs()
    files = [path for path in IMAGES_DIR.rglob("*") if path.is_file()]
    if not files:
        return None
    buffer = BytesIO()
    with zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in files:
            archive.write(path, arcname=path.relative_to(OUTPUT_DIR))
    return buffer.getvalue()
