"""
Template: Simple Greeting

A simple template that uses variable substitution to create a greeting.

Usage:
    python simple_greeting.py '{"name": "World"}'
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
        print("Usage: python simple_greeting.py '{\"name\": \"World\"}'")
        sys.exit(1)

    context = json.loads(sys.argv[1])
    template = "Hello, {{name}}!"
    result = render(template, context)
    print(result)


if __name__ == "__main__":
    main()
