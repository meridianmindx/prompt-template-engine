#!/usr/bin/env python3
"""Push a new release to PyPI."""
import subprocess, os, sys

# Bump version
version = "2.0.0"

# Read current setup.py and update version
setup_path = "setup.py"
with open(setup_path) as f:
    content = f.read()

old_version = "1.0.0"
new_content = content.replace(f'version="{old_version}"', f'keywords="LLM, prompt templates, AI, LLM, templates"', )
new_content = new_content.replace(f'    version="{old_version}"', f'    version="{version}"')

# Actually let's just replace the version line
import re
new_content = re.sub(r'    version="[^"]*"', f'    version="{version}"', new_content)
with open(setup_path, "w") as f:
    f.write(new_content)

print(f"Updated setup.py to version {version}")
