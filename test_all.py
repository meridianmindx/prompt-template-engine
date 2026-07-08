import sys
sys.path.insert(0, '.')
from prompt_templates import get_templates, generate, TEMPLATES

# Test: count all templates
all_templates = get_templates()
print(f"Total categories: {len(TEMPLATES)}")
print(f"All template names: {list(all_templates)}")

# Test generate
template = get_templates("cold_outreach")[0]["template"]
result = generate(template, name="John", company="Acme", subject_line="Quick question")
print("\nGenerated output:")
print(result)
