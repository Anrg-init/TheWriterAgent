<<<<<<< HEAD
#  TheWriterAgent

> Multi-Agent AI Blog Writer built with LangGraph that researches, plans, writes, reviews, and generates images for technical blogs.

---

##  Demo

> ![alt text](image.png)


##  Features

-  Multi-Agent workflow using LangGraph
-  Optional web research with Tavily
-  Intelligent blog planning & outlining
-  Section-by-section content generation
-  AI image generation
-  Markdown export
-  Streamlit UI

---

##  Architecture

```text
                                         ┌──────────────┐
                         │    User      │
                         └──────┬───────┘
                                │
                                ▼
                     ┌────────────────────┐
                     │    Streamlit UI    │
                     └─────────┬──────────┘
                               │
                               ▼
                   ┌────────────────────────┐
                   │ LangGraph Orchestrator │
                   └─────────┬──────────────┘
                             │
      ┌──────────────┬───────────────┬───────────────┐
      ▼              ▼               ▼               ▼
   Router        Research        Planner         Image Planner
      │              │               │
      │           Tavily API         │
      │              │               │
      └──────────────┴───────┬───────┘
                             ▼
                   Parallel Writer Agents
                             │
                             ▼
                       Merge Sections
                             │
                             ▼
                    Gemini Image Generator
                             │
                             ▼
                Markdown + Images + Download
```

---

##  Tech Stack

- Python
- LangGraph
- LangChain
- Streamlit
- Groq
- Tavily
- Gemini Image API

---

##  Project Structure

```text
.
├── backend.py
├── frontend.py
├── requirements.txt
├── images/
└── README.md
```

---

## ▶ Run

```bash
pip install -r requirements.txt
streamlit run frontend.py
```

Create `.env`

```env
GROQ_API_KEY=
TAVILY_API_KEY=
GOOGLE_API_KEY=
```

---

## ⭐ If you like this project, consider giving it a star!
=======
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

Edit `.env` and add your keys:

```env
TAVILY_API_KEY=your_tavily_api_key
GOOGLE_API_KEY=your_google_api_key
GOOGLE_MODEL=gemini-2.5-flash
GOOGLE_IMAGE_MODEL=gemini-3.1-flash-image
WRITER_OUTPUT_DIR=./output
```

`GOOGLE_API_KEY` is required to generate content. Tavily is optional for web research. Never commit `.env` or real API keys.

## Run

```bash
streamlit run frontend.py
```

Generated markdown files and images are saved in `output/`. Existing markdown files can be loaded from the Past blogs panel.

## Project Layout

```text
.
├── writer_agent/
│   ├── config.py       # Environment and output locations
│   ├── graph.py        # LangGraph workflow and providers
│   ├── storage.py      # Saved blogs and ZIP bundles
│   └── ui.py           # Streamlit interface
├── tests/              # Regression tests
├── backend.py          # Compatibility graph import
├── frontend.py         # Compatibility Streamlit entry point
├── .env.example        # Safe configuration template
└── requirements.txt
```

## Test

```bash
pytest -q
```
>>>>>>> 2147a22 (fix/prod_issue)
