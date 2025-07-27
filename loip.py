#!/usr/bin/env python3
"""
Loip - Lorem Ipsum Generator
A minimal terminal-based Lorem Ipsum generator with clipboard support.
"""

import os
import sys
import argparse
import random
try:
    import pyperclip
    CLIPBOARD_AVAILABLE = True
except ImportError:
    CLIPBOARD_AVAILABLE = False
    print("Warning: pyperclip not installed. Clipboard functionality disabled.")
    print("Install with: pip install pyperclip")

# Lorem Ipsum word bank
LOREM_WORDS = [
    "lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit",
    "sed", "do", "eiusmod", "tempor", "incididunt", "ut", "labore", "et", "dolore",
    "magna", "aliqua", "enim", "ad", "minim", "veniam", "quis", "nostrud",
    "exercitation", "ullamco", "laboris", "nisi", "aliquip", "ex", "ea", "commodo",
    "consequat", "duis", "aute", "irure", "in", "reprehenderit", "voluptate",
    "velit", "esse", "cillum", "fugiat", "nulla", "pariatur", "excepteur", "sint",
    "occaecat", "cupidatat", "non", "proident", "sunt", "culpa", "qui", "officia",
    "deserunt", "mollit", "anim", "id", "est", "laborum", "at", "vero", "eos",
    "accusamus", "accusantium", "doloremque", "laudantium", "totam", "rem",
    "aperiam", "eaque", "ipsa", "quae", "ab", "illo", "inventore", "veritatis",
    "et", "quasi", "architecto", "beatae", "vitae", "dicta", "sunt", "explicabo",
    "nemo", "ipsam", "voluptatem", "quia", "voluptas", "aspernatur", "aut", "odit",
    "fugit", "sed", "quia", "consequuntur", "magni", "dolores", "ratione",
    "sequi", "nesciunt", "neque", "porro", "quisquam", "dolorem", "adipisci",
    "numquam", "eius", "modi", "tempora", "incidunt", "magnam", "quaerat"
]

def generate_words(count):
    """Generate a specified number of Lorem Ipsum words."""
    return [random.choice(LOREM_WORDS) for _ in range(count)]

def generate_sentence():
    """Generate a single sentence with 8-15 words."""
    word_count = random.randint(8, 15)
    words = generate_words(word_count)
    words[0] = words[0].capitalize()
    return ' '.join(words) + '.'

def generate_paragraph():
    """Generate a paragraph with 4-8 sentences."""
    sentence_count = random.randint(4, 8)
    sentences = [generate_sentence() for _ in range(sentence_count)]
    return ' '.join(sentences)

def generate_lorem(mode, count):
    """Generate Lorem Ipsum text based on mode and count."""
    if mode.lower() == "words":
        words = generate_words(count)
        words[0] = words[0].capitalize()
        return ' '.join(words) + '.'
    
    elif mode.lower() == "sentences":
        sentences = [generate_sentence() for _ in range(count)]
        return ' '.join(sentences)
    
    elif mode.lower() == "paragraphs":
        paragraphs = [generate_paragraph() for _ in range(count)]
        return '\n\n'.join(paragraphs)
    
    elif mode.lower() == "characters":
        # Generate text until we reach the character count
        text = ""
        while len(text) < count:
            text += generate_paragraph() + "\n\n"
        return text[:count].rstrip()
    
    return ""

def copy_to_clipboard(text):
    """Copy text to clipboard if available."""
    if CLIPBOARD_AVAILABLE:
        try:
            pyperclip.copy(text)
            return True
        except:
            return False
    return False

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_ui(mode="Paragraphs", count=3):
    """Display the simple TUI."""
    clear_screen()
    print("┌─ Loip Generator ─────────────────┐")
    print("│                                  │")
    print(f"│ Mode: {mode:<23} │")
    print("│                                  │")
    print(f"│ Count: {count:<22} │")
    print("│                                  │")
    print("│ Commands:                        │")
    print("│ [1] Paragraphs  [2] Words        │")
    print("│ [3] Sentences   [4] Characters   │")
    print("│ [g] Generate    [q] Quit         │")
    print("│ [n] New count                    │")
    print("│                                  │")
    print("└──────────────────────────────────┘")

def main_tui():
    """Run the interactive TUI mode."""
    modes = ["Paragraphs", "Words", "Sentences", "Characters"]
    current_mode = 0
    count = 3
    
    print("Starting Loip TUI mode...")
    print("Press Enter to continue...")
    input()
    
    while True:
        show_ui(modes[current_mode], count)
        
        cmd = input("\n> ").lower().strip()
        
        if cmd == 'q':
            print("Goodbye!")
            break
        elif cmd in ['1', '2', '3', '4']:
            current_mode = int(cmd) - 1
        elif cmd == 'n':
            try:
                new_count = int(input("Enter new count: "))
                if new_count > 0:
                    count = new_count
                else:
                    print("Count must be positive!")
                    input("Press Enter to continue...")
            except ValueError:
                print("Invalid number!")
                input("Press Enter to continue...")
        elif cmd == 'g':
            # Generate Lorem Ipsum
            text = generate_lorem(modes[current_mode], count)
            
            # Display the generated text
            clear_screen()
            print("┌─ Generated Text ─────────────────┐")
            print("│                                  │")
            
            # Split text into lines for display
            lines = text.split('\n')
            for line in lines[:10]:  # Show first 10 lines
                if len(line) > 32:
                    print(f"│ {line[:29]}... │")
                else:
                    print(f"│ {line:<32} │")
            
            if len(lines) > 10:
                print("│ ... (truncated for display)      │")
            
            print("│                                  │")
            print("└──────────────────────────────────┘")
            
            # Copy to clipboard
            if copy_to_clipboard(text):
                print("\n✓ Generated and copied to clipboard!")
            else:
                print("\n✓ Generated! (Clipboard not available)")
            
            print(f"\nFull text printed below:\n")
            print(text)
            
            input("\nPress Enter to continue...")
        elif cmd.isdigit():
            new_count = int(cmd)
            if new_count > 0:
                count = new_count
        else:
            print("Unknown command. Use 1-4, g, n, or q")
            input("Press Enter to continue...")

def main():
    """Main entry point with command line argument support."""
    parser = argparse.ArgumentParser(description='Loip - Lorem Ipsum Generator')
    parser.add_argument('count', nargs='?', type=int, default=1, 
                        help='Number of items to generate (default: 1)')
    parser.add_argument('-w', '--words', action='store_true', 
                        help='Generate words')
    parser.add_argument('-s', '--sentences', action='store_true', 
                        help='Generate sentences')
    parser.add_argument('-p', '--paragraphs', action='store_true', 
                        help='Generate paragraphs (default)')
    parser.add_argument('-c', '--characters', type=int, metavar='N',
                        help='Generate N characters')
    parser.add_argument('--tui', action='store_true', 
                        help='Start interactive TUI mode')
    parser.add_argument('-q', '--quiet', action='store_true',
                        help='Only copy to clipboard, no stdout')
    
    args = parser.parse_args()
    
    # TUI mode
    if args.tui:
        main_tui()
        return
    
    # Determine mode and count
    if args.characters:
        mode = "characters"
        count = args.characters
    elif args.words:
        mode = "words"
        count = args.count
    elif args.sentences:
        mode = "sentences"
        count = args.count
    else:  # default to paragraphs
        mode = "paragraphs"
        count = args.count
    
    # Generate text
    text = generate_lorem(mode, count)
    
    # Output
    if not args.quiet:
        print(text)
    
    # Copy to clipboard
    if copy_to_clipboard(text):
        if not args.quiet:
            print(f"\n✓ Copied to clipboard!", file=sys.stderr)
    else:
        if not args.quiet:
            print(f"\n⚠ Could not copy to clipboard", file=sys.stderr)

if __name__ == "__main__":
    main()