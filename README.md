# Prompt Templates

A curated collection of high-quality LLM prompt templates for common use cases:

- Cold outreach emails
- Content generation
- Sales copywriting
- Technical documentation
- Social media posts

## Installation

```bash
pip install prompt_templates
```

Or from source:

```bash
git clone https://github.com/Leafon26/multi-agent-builder.git
cd multi-agent-builder/prompt_templates
pip install -e .
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

| Category | Templates | Description |
|---|---|---|
| `cold_outreach` | 5 | Cold email and LinkedIn outreach |
| `content_generation` | 5 | Blog and newsletter templates |
| `sales_copywriting` | 3 | Sales email and landing page copy |
| `technical_docs` | 3 | API docs and release notes |
| `social_media` | 5 | Twitter/LinkedIn/Reddit posts |

Each template supports Python `string.Template` formatting with `**kwargs`.

## Contributing

We welcome contributions! Just open a PR with your template.

## License

MIT License. See [LICENSE](LICENSE) file for details.