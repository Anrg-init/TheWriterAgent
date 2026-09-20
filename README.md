# The Writer Agent

The Writer Agent is a Streamlit application that uses LangGraph to research, plan, write, and package technical blog posts.

## Features

- Optional Tavily research with recency-aware evidence filtering
- Structured planning and parallel section generation
- Markdown preview and downloadable bundles
- Optional Gemini image generation
- Persistent generated output under `output/`

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Set these values in `.env`:

```env
GOOGLE_API_KEY=your_google_api_key
TAVILY_API_KEY=your_tavily_api_key
GOOGLE_MODEL=gemini-2.5-flash
GOOGLE_IMAGE_MODEL=gemini-3.1-flash-image
WRITER_OUTPUT_DIR=./output
```

`GOOGLE_API_KEY` is required to generate content. `TAVILY_API_KEY` is optional and enables web research. Never commit `.env` or real API keys.

## Run locally

```bash
streamlit run frontend.py
```

## Deploy on Streamlit Community Cloud

1. Push the repository to GitHub.
2. Create a new app at [share.streamlit.io](https://share.streamlit.io/).
3. Select the repository, branch, and `frontend.py` as the main file.
4. Add `GOOGLE_API_KEY` and, optionally, `TAVILY_API_KEY` under **Settings > Secrets** using TOML syntax:

```toml
GOOGLE_API_KEY = "your_google_api_key"
TAVILY_API_KEY = "your_tavily_api_key"
GOOGLE_MODEL = "gemini-2.5-flash"
GOOGLE_IMAGE_MODEL = "gemini-3.1-flash-image"
```

The app installs dependencies from `requirements.txt`. Generated markdown files and images are saved under `output/` during the current app session.

## Project layout

```text
.
├── writer_agent/
│   ├── config.py
│   ├── graph.py
│   ├── storage.py
│   └── ui.py
├── tests/
├── backend.py
├── frontend.py
├── .env.example
└── requirements.txt
```

## Test

```bash
pytest -q
```
