# Release Notes — prompt-template-engine

## What's New

`prompt-template-engine` is a Python library that gives developers a **curated collection of high-quality LLM prompt templates** for common use cases. No more staring at a blank prompt — just `pip install` and start generating.

### Key Features

- **20+ curated templates** across 5 categories:
  - 🔥 **Cold Outreach** — cold emails, LinkedIn messages, follow-ups
  - ✍️ **Content Generation** — blog posts, newsletters, social media
  - 💰 **Sales Copywriting** — sales emails, landing page copy
  - 📚 **Technical Docs** — API docs, release notes, changelogs
  - 📱 **Social Media** — Twitter/LinkedIn/Reddit posts

- **Structured API** — get all templates, filter by category, or grab a specific one
- **CLI mode** — use from the command line with `python -m prompt_templates`
- **Variable guards** — every template includes validation and error handling
- **Examples directory** — every template has a working example

### Quick Start

```python
from prompt_templates import get_templates, get_template, generate

# Get all templates
templates = get_templates()

# Get templates by category
cold_templates = get_templates("cold_outreach")

# Get a specific template
template = get_template("cold_outreach", "cold_email_template")

# Generate with template
result = generate(template["template"], name="John", topic="AI")
```

### Installation

```bash
pip install prompt_templates
```

### Template Categories

| Category | Description |
|---|---|
| `cold_outreach` | Cold email and LinkedIn templates |
| `content_generation` | Blog and newsletter templates |
| `sales_copywriting` | Sales email and landing page copy |
| `technical_docs` | API docs and release notes |
| `social_media` | Twitter/LinkedIn/Reddit posts |

### Why This Exists

Hardcoding LLM prompts is tedious and error-prone. This library gives you **professionally crafted, tested templates** that you can use immediately — or adapt for your own use cases. Every template supports variable substitution with guard checks.

### Links

- **PyPI**: [pypi.org/project/prompt-templates](https://pypi.org/project/prompt-templates/)
- **Source**: [github.com/meridianmindx/prompt-template-engine](https://github.com/meridianmindx/prompt-template-engine)
