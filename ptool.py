"""Text processing CLI tool."""

def text_to_uppercase(text):
    """Convert text to uppercase."""
    return text.upper()

def word_count(text):
    """Count words in text."""
    return len(text.split())

def reverse_text(text):
    """Reverse the order of characters."""
    return text[::-1]

def remove_vowels(text):
    """Remove all vowels from text."""
    return ''.join([char for char in text if char.lower() not in 'aeiou'])

def main():
    """Main CLI entry point."""
    import sys
    
    if len(sys.argv) < 3:
        print("Usage: ptool <command> <text>")
        return
    
    command = sys.argv[1]
    text = sys.argv[2]
    
    if command == "uppercase":
        print(text_to_uppercase(text))
    elif command == "count":
        print(word_count(text))
    elif command == "reverse":
        print(reverse_text(text))
    elif command == "remove-vowels":
        print(remove_vowels(text))
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()