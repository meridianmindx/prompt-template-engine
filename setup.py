from setuptools import setup, find_packages

setup(
    name="prompt_templates",
    version="0.3.0",
    packages=find_packages(),
    description="A curated collection of high-quality LLM prompt templates",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.7",
    author="Meridian Mind",
    install_requires=[
        "jinja2>=3.0.0",
        "click>=8.0.0",
    ],
    entry_points={
        "console_scripts": [
            "ptem=ptem_cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)