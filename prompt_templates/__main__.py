"""
Usage: python3 -m prompt_templates [category]
"""
import sys
from prompt_templates.templates import get_templates, TEMPLATES

if __name__ == "__main__":
    if len(sys.argv) > 1:
        category = sys.argv[1]
        templates = get_templates(category)
        print(f"Templates in '{category}':")
        for t in templates:
            print(f"  - {t['name']}: {t['description']}")
    else:
        print("Available categories:")
        for category in TEMPLATES:
            templates = TEMPLATES[category]
            print(f"  {category}: {len(templates)} templates")
