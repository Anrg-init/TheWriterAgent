from zipfile import ZipFile
from io import BytesIO

from writer_agent.storage import extract_title, safe_slug
from writer_agent.graph import _message_content_to_text, _safe_image_filename
from writer_agent.graph import decide_images


def test_safe_slug_is_stable_and_usable() -> None:
    assert safe_slug("  Python: Fast APIs! ") == "python_fast_apis"
    assert safe_slug("***") == "blog"


def test_extract_title_uses_first_h1() -> None:
    assert extract_title("intro\n# A useful title\n", "fallback") == "A useful title"
    assert extract_title("no heading", "fallback") == "fallback"


def test_generated_image_filename_cannot_escape_image_directory() -> None:
    assert _safe_image_filename("../../secret.png", 1) == "secret.png"
    assert _safe_image_filename("", 2) == "image_2.png"


def test_safe_slug_accepts_list_shaped_model_title() -> None:
    from writer_agent.graph import _safe_slug

    assert _safe_slug(["A useful", "title"]) == "a_useful_title"


def test_orchestrator_accepts_dict_evidence(monkeypatch) -> None:
    from writer_agent.graph import orchestrator_node

    class Planner:
        def invoke(self, messages):
            return type(
                "PlanStub",
                (),
                {"blog_kind": "explainer", "model_dump": lambda self: {}},
            )()

    class FakeLLM:
        def with_structured_output(self, schema):
            return Planner()

    monkeypatch.setattr("writer_agent.graph.get_llm", lambda: FakeLLM())
    result = orchestrator_node(
        {
            "topic": "testing",
            "mode": "hybrid",
            "as_of": "2026-09-21",
            "recency_days": 45,
            "evidence": [{"title": "Source", "url": "https://example.com"}],
        }
    )

    assert result["plan"].blog_kind == "explainer"


def test_gemini_list_content_is_normalized_to_markdown() -> None:
    assert _message_content_to_text(
        {"content": [{"type": "text", "text": "## First"}, {"text": "\nBody"}]}
    ) == "## First\n\nBody"


def test_image_planning_failure_preserves_article(monkeypatch) -> None:
    class BrokenPlanner:
        def with_structured_output(self, schema):
            return self

        def invoke(self, messages):
            raise RuntimeError("malformed tool arguments")

    monkeypatch.setattr("writer_agent.graph.get_llm", lambda: BrokenPlanner())
    result = decide_images(
        {
            "topic": "testing",
            "merged_md": "# Article\n\nContent",
            "plan": type("PlanStub", (), {"blog_kind": "explainer"})(),
        }
    )

    assert result == {"md_with_placeholders": "# Article\n\nContent", "image_specs": []}


def test_bundle_contains_markdown_and_relative_images(tmp_path, monkeypatch) -> None:
    import writer_agent.storage as storage

    output_dir = tmp_path / "output"
    images_dir = output_dir / "images"
    images_dir.mkdir(parents=True)
    (images_dir / "diagram.png").write_bytes(b"image")
    monkeypatch.setattr(storage, "OUTPUT_DIR", output_dir)
    monkeypatch.setattr(storage, "IMAGES_DIR", images_dir)

    archive = storage.bundle_zip("# Title\n", "title.md")
    with ZipFile(BytesIO(archive)) as bundle:
        assert set(bundle.namelist()) == {"title.md", "images/diagram.png"}