# Prompt Template Engine

> **Production-ready LLM prompt templates** — copy, customize, and ship in seconds.

A curated collection of high-quality LLM prompt templates for common use cases, packaged for immediate use.

| Feature | Detail |
|---|---|
| **What** | 20+ curated templates across 5 categories |
| **Use cases** | Cold outreach, content, sales copy, docs, social media |
| **API** | `get_templates()`, `get_template()`, `generate()` |
| **Install** | `pip install prompt_templates` |
| **License** | MIT — free for commercial use |

## Quick Start

```python
from prompt_templates import get_templates, get_template, generate

# All templates
templates = get_templates()

# By category
cold = get_templates("cold_outreach")

# Generate output
result = generate(template["template"], name="John", topic="AI")
```

## Template Categories

| Category | Templates |
|---|---|
| Cold Outreach | Cold email, LinkedIn, follow-up |
| Content Generation | Blog posts, newsletters, social media |
| Sales Copywriting | Sales emails, landing page copy |
| Technical Docs | API docs, release notes, changelogs |
| Social Media | Twitter/X, LinkedIn, Reddit posts |

## License

MIT — use freely for personal or commercial projects.

## Links

- [PyPI](https://pypi.org/project/prompt-templates/)
- [Source Code](https://github.com/meridianmindx/prompt-template-engine)
- [Template Library](https://meridianmindx.github.io/prompt-template-engine/)
- [Hugging Face](https://huggingface.co/MeridianMindX)
- [Medium Blog](https://medium.com/@meridianmindx)

---

*Built with ❤️ by [Meridian Mind](https://meridianmindx.github.io/)*
