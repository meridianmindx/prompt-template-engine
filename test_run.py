import sys
sys.path.insert(0, '/root/prompt_templates')
from prompt_templates import get_templates, generate

# Count templates
templates = get_templates()
print(f"Total templates: {len(templates)}")

# Test generation
t = templates["cold_outreach"][0]
result = generate(t["template"], name="John", company="Acme", subject_line="Quick question")
print(f"\nSample output:\n{result}")
