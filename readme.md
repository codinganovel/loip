# loip
**loip** is a minimal Lorem Ipsum generator for your terminal. It's a tool designed to quickly generate placeholder text with randomized word combinations, sentence lengths, and paragraph structures — with automatic clipboard support and an optional interactive TUI mode.
> No bloat. No network calls. Just generate and go.
---
## ✨ Features
- Randomized Lorem Ipsum generation (not static blocks)
- Multiple output modes: paragraphs, words, sentences, characters
- Automatic clipboard copying with `pyperclip`
- Simple interactive TUI mode with box-drawing interface
- Command-line interface for scripting and quick generation
- Offline operation — no API calls required
---
## 📦 Installation

[get yanked](https://github.com/codinganovel/yanked)

---
## 🚀 Usage
### Command Line Mode
```bash
# Basic usage
python loip.py                 # 1 paragraph (default)
python loip.py 3               # 3 paragraphs
python loip.py -w 100          # 100 words
python loip.py -s 5            # 5 sentences
python loip.py -c 500          # 500 characters

# Quiet mode (clipboard only, no stdout)
python loip.py -q 2            # 2 paragraphs to clipboard only
```

### Interactive TUI Mode
```bash
python loip.py --tui
```
Navigate with simple commands:
- `1-4`: Switch between modes (Paragraphs/Words/Sentences/Characters)
- `n`: Set new count
- `g`: Generate text
- `q`: Quit

---
### Available Commands
| Command         | Description                          |
|----------------|--------------------------------------|
| `loip`          | Generate 1 paragraph (default)       |
| `loip N`        | Generate N paragraphs                |
| `loip -w N`     | Generate N words                     |
| `loip -s N`     | Generate N sentences                 |
| `loip -c N`     | Generate N characters                |
| `loip --tui`    | Start interactive TUI mode           |
| `loip -q`       | Quiet mode (clipboard only)         |

Text is automatically copied to your clipboard and printed to stdout (unless using `-q` flag).
---
## 📋 Clipboard Support & Dependencies
`loip` uses [pyperclip](https://pypi.org/project/pyperclip/) to interact with the system clipboard.
### macOS  
✅ Works out of the box using built-in `pbcopy`
### Windows  
✅ Works out of the box using Windows clipboard API
### Linux  
⚠️ You need to install a clipboard utility:
```bash
sudo apt install xclip   # or
sudo apt install xsel
```
### Installation
```bash
pip install pyperclip
```
---
## 📄 License

under ☕️, check out [the-coffee-license](https://github.com/codinganovel/The-Coffee-License)

I've included both licenses with the repo, do what you know is right. The licensing works by assuming you're operating under good faith.
---
## ✍️ Created by Sam  
Because placeholder text shouldn't be the same every time.
