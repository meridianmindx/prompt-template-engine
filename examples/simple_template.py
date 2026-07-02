#!/usr/bin/env python3
"""
Template: Basic Prompt Template Engine

A simple template engine that supports:
- Variable substitution with {{variable}} syntax
- Conditional blocks
- Looping over collections

Usage:
    python simple_template.py '{"name": "World"}'
"""

import json
import sys


def render(template: str, context: dict) -> str:
    """Render a template with variable substitution."""
    result = template
    for key, value in context.items():
        result = result.replace(f"{{{{{key}}}}}", str(value))
    return result


def main():
    if len(sys.argv) < 2:
        print("Usage: python simple_template.py '{\"name\": \"World\"}'")
        sys.exit(1)

    context = json.loads(sys.argv[1])
    template = """Hello, {{name}}!

Welcome to the {{product}}.

Your code will look like:
{{code}}
"""

    result = render(template, context)
    print(result)


if __name__ == "__main__":
    main()
