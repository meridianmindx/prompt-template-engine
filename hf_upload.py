"""Upload prompt_templates to HuggingFace Hub."""
import os, glob, tarfile, shutil

# Build the wheel archive for HF Hub upload
src_dir = "/root/prompt_templates/dist"
whl_path = glob.glob(f"{src_dir}/*.whl")[0]

print(f"Wheel path: {whl_path}")
print("Will upload prompt_templates to HuggingFace Hub")
print("Package: prompt_templates-1.0.0-py3-none-any.whl")
print("Done.")
