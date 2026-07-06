"""
Template: Loop Template

Demonstrates looping over collections:
- Iterating over arrays
- Accessing object properties
- Building lists from templates

Usage:
    python loop_template.py '[{"name": "Alice"}, {"name": "Bob"}]'
"""

import json
import sys


def render(template: str, context: dict) -> str:
    """Render template with loops."""
    result = template
    for key, value in context.items():
        result = result.replace(f"{{{{{key}}}}}", str(value))

    # Process loops
    if "items" in context:
        items = context["items"]
        loop_template = "{{#items}}\n- {{name}}: {{role}}\n{{/items}}"
        rendered_loop = ""
        for item in items:
            rendered_loop += f"\n- {item['name']}: {item.get('role', 'N/A')}"
        result = result.replace("{{#items}}\n- {{name}}: {{role}}\n{{/items}}", rendered_loop)

    return result


def main():
    if len(sys.argv) < 2:
        print("Usage: python loop_template.py '[{\"name\": \"Alice\", \"role\": \"Dev\"}]'")
        sys.exit(1)

    context = json.loads(sys.argv[1])
    template = """Team Members:
{{#items}}
- {{name}}: {{role}}
{{/items}}
"""

    result = render(template, context)
    print(result)


if __name__ == "__main__":
    main()
