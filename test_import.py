#!/usr/bin/env python3
from prompt_templates import TEMPLATES
print(f"Categories: {len(TEMPLATES)}")
for cat in TEMPLATES:
    print(f"  {cat}: {len(TEMPLATES[cat])} templates")
