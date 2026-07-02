"""Example usage of prompt_templates."""

from prompt_templates import get_template, generate

# Get a specific template
template = get_template("cold_outreach", "cold_email_template")

# Generate with template
result = generate(template["template"], name="John", topic="AI")
print(result)
