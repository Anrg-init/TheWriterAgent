def test_env_example_documents_all_provider_settings() -> None:
    from pathlib import Path

    env_example = Path(__file__).parents[1] / ".env.example"
    contents = env_example.read_text(encoding="utf-8")

    for key in (
        "TAVILY_API_KEY",
        "GOOGLE_API_KEY",
        "GOOGLE_MODEL",
        "GOOGLE_IMAGE_MODEL",
        "WRITER_OUTPUT_DIR",
    ):
        assert f"{key}=" in contents