# Simple Python CLI Tool

A lightweight command-line interface for basic text processing tasks.

## Features

- **text-to-uppercase**: Convert text to uppercase
- **word-count**: Count words in a string
- **reverse-text**: Reverse the order of characters
- **remove-vowels**: Remove all vowels from text

## Installation

```bash
pip install .
```

## Usage

```bash
# Convert text to uppercase
ptool uppercase "hello world"

# Count words
ptool count "this is a test"

# Reverse text
ptool reverse "abcdef"

# Remove vowels
ptool remove-vowels "hello world"
```

## Development

```bash
pip install -e .
```

## Testing

```bash
python -m unittest tests/
```
