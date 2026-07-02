"""
Template: Conditional Logic

Demonstrates conditional logic in templates:
- If/else blocks
- Comparison operators
- Nested conditions

Usage:
    python conditional_logic.py '{"score": 85}'
"""

import json
import sys


def render(template: str, context: dict) -> str:
    """Render template with conditionals and variables."""
    result = template
    for key, value in context.items():
        result = result.replace(f"{{{{{key}}}}}", str(value))

    # Process conditionals
    if "score" in context:
        score = int(context["score"])
        if score >= 80:
            result = result.replace("{{GRADE}}", "A")
        elif score >= 70:
            result = result.replace("{{GRADE}}", "B")
        else:
            result = result.replace("{{GRADE}}", "C")

    return result


def main():
    if len(sys.argv) < 2:
        print("Usage: python conditional_logic.py '{\"score\": 85}'")
        sys.exit(1)

    context = json.loads(sys.argv[1])
    template = """Score: {{score}}
Grade: {{GRADE}}
Status: {{STATUS}}
"""

    # Add status based on grade
    if "score" in context:
        score = int(context["score"])
        if score >= 60:
            status = "PASS"
        else:
            status = "FAIL"
        context["STATUS"] = status

    result = render(template, context)
    print(result)


if __name__ == "__main__":
    main()
