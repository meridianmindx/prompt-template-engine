"""prompt_template_engine - Simple and safe templating engine for LLM prompts."""

__version__ = "0.2.0"


class Engine:
    """Minimal template engine for LLM prompts."""

    def render(self, template, **kwargs):
        """Render a template string with variable substitution."""
        result = template
        for key, value in kwargs.items():
            result = result.replace("{{" + key + "}}", str(value))
        return result

    def render_guarded(self, template, **kwargs):
        """Render with validation - rejects if any variable is missing."""
        for key in kwargs:
            if "{{" + key + "}}" not in template:
                raise ValueError(f"Variable '{{'{key}'}}' not found in template")
        return self.render(template, **kwargs)

    def render_batch(self, templates, **kwargs):
        """Render a list of templates."""
        return [self.render(t, **kwargs) for t in templates]
