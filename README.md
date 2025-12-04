# BlackJack

A Python implementation of the classic BlackJack card game with both CLI and graphical (Pygame) interfaces.

## Features

- **CLI Mode**: Play BlackJack in your terminal with colored output
- **GUI Mode**: Play with a graphical interface using Pygame
- **Strategic AI**: The bettor (player) follows basic BlackJack strategy
- **Standard Rules**: Dealer hits on 16 and below, stands on 17+
- **Type-Safe**: Full type hints and strict type checking with mypy
- **Code Quality**: Follows PEP 8 standards, formatted with Black, linted with flake8

## Installation

### Prerequisites

- Python 3.12 or higher
- pip (Python package manager)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/Nowarr/BlackJack.git
cd BlackJack
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### CLI Version

Run the command-line version:
```bash
python main.py
```

The CLI version will run 3 rounds of BlackJack automatically, then ask if you want to play again.

### Pygame Version

Run the graphical version:
```bash
python main_pygame.py
```

In the GUI version:
- Click "Start Game" to begin a new round
- Click "Hit" to draw another card
- Click "Stand" to end your turn and let the dealer play
- Click "Play Again" after a round ends to start a new game
- Click "Quit" to exit

## Game Rules

### Basic Rules
- The goal is to get a hand value as close to 21 as possible without going over
- Face cards (Jack, Queen, King) are worth 10 points
- Aces are worth 11 points (simplified rules)
- Number cards are worth their face value

### Bettor Strategy
The bettor follows these strategic rules:
1. Always stand on 21
2. Always hit on 11 or lower
3. Between 12-16: Hit if dealer shows 7+, otherwise stand
4. Stand on hard 17+
5. Hit on soft 17 if dealer shows 7+

### Dealer Rules
- Dealer hits on 16 or below
- Dealer stands on 17 or above

## Development

### Code Quality Tools

This project uses several tools to maintain code quality:

- **Black**: Code formatter
- **flake8**: Style guide enforcement
- **mypy**: Static type checker

### Running Quality Checks

Format code with Black:
```bash
black .
```

Check code style with flake8:
```bash
flake8 . --max-line-length=88 --extend-ignore=E203,W503
```

Run type checking with mypy:
```bash
mypy src/ main.py main_pygame.py --ignore-missing-imports
```

### Project Structure

```
BlackJack/
├── main.py                 # CLI version entry point
├── main_pygame.py          # Pygame version entry point
├── requirements.txt        # Project dependencies
├── pyproject.toml         # Tool configurations
├── resources/             # Game assets (fonts)
│   ├── EBG-Reg.ttf
│   └── EBG-Italic.ttf
└── src/                   # Source code
    ├── __init__.py
    ├── bettor.py          # Player logic
    ├── card_dealer.py     # Card dealing logic
    ├── colors.py          # ANSI color codes
    ├── dummy.py           # Dealer logic
    ├── manager.py         # Game state management
    └── game_visual/       # Pygame UI components
        ├── __init__.py
        ├── button.py      # Button widget
        └── game_window.py # Main game window
```

## Contributing

Contributions are welcome! Please ensure:
1. Code follows PEP 8 standards
2. All type hints are properly added
3. Code is formatted with Black
4. No flake8 warnings
5. mypy passes with no errors

## License

This project is open source and available for educational purposes.
