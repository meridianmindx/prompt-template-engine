# Prompt Templates

A curated collection of high-quality LLM prompt templates for common use cases:

- Cold outreach emails
- Content generation
- Sales copywriting
- Technical documentation
- Social media posts

[Visit the website](https://meridianmindx.github.io/prompt-template-engine/)

<!-- Live demo and project overview: https://meridianmindx.github.io/prompt-template-engine/ -->

## Installation

```bash
pip install prompt_templates
```

## Usage

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

## Template Categories

- `cold_outreach` - Cold email and LinkedIn templates
- `content_generation` - Blog and newsletter templates
- `sales_copywriting` - Sales email and landing page copy
- `technical_docs` - API docs and release notes
- `social_media` - Twitter/LinkedIn/Reddit posts
