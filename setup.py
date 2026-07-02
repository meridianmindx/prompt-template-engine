from setuptools import setup, find_packages

setup(
    name="prompt-template-engine",
    version="0.2.0",
    description="Simple and safe templating engine for LLM prompts",
    author="Zach",
    author_email="zacharie@astera.org",
    packages=find_packages(),
    python_requires=">=3.10",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    entry_points={
        "console_scripts": [
            "ptemp=example:main",
        ],
    },
    test_suite="tests",
)
