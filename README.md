# Yahtzee in Python

<p align="center">
  <strong>A complete terminal implementation of the classic dice game.</strong><br>
  Built with the Python standard library, modular game logic, and automated scoring tests.
</p>

<p align="center">
  <a href="https://www.python.org/"><img alt="Python" src="https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white"></a>
  <a href="https://github.com/tiagoslantunes/Yahtzee/actions/workflows/quality.yml"><img alt="Quality checks" src="https://github.com/tiagoslantunes/Yahtzee/actions/workflows/quality.yml/badge.svg"></a>
  <img alt="Dependencies" src="https://img.shields.io/badge/dependencies-standard%20library-4C1">
</p>

Developed for the Programming for Data Science course, this project separates the reusable scoring engine from the terminal interface. It demonstrates input validation, state management, deterministic scoring rules, and testable functional design.

## Highlights

- Complete 13-round Yahtzee game with up to three rolls per round.
- All upper and lower scoring categories, including straights and Yahtzee.
- Upper-section bonus and live scorecard totals.
- Defensive validation for dice selection and category choice.
- No third-party runtime dependencies.

## Project structure

| Path | Purpose |
|---|---|
| [`main.py`](main.py) | Terminal interface and 13-round game loop |
| [`yahtzee.py`](yahtzee.py) | Dice, scoring, scorecard, and round logic |
| [`tests/`](tests) | Automated tests for the core scoring rules |

## Quick start

```bash
git clone https://github.com/tiagoslantunes/Yahtzee.git
cd Yahtzee
python main.py
```

Enter the dice you want to keep as digits. For example, `336` keeps two threes and one six. Press Enter to keep none.

## Scoring model

| Category | Rule |
|---|---|
| Ones to sixes | Sum of matching dice |
| Three/four of a kind | Sum of all dice when the count threshold is met |
| Full house | 25 points for a 3+2 split |
| Four/five straight | 30/40 points |
| Yahtzee | 50 points for five equal dice |
| Chance | Sum of all dice |

The upper section receives a 35-point bonus when its subtotal reaches 63.

## Tests

```bash
python -m unittest discover -s tests -v
```

The test suite covers scorecard initialization, dice bounds, straight detection, category scoring, the upper bonus, and reroll invariants.

## Design notes

- A `Counter` represents dice multiplicities and makes combination checks explicit.
- Game logic lives outside the UI loop, so the scoring engine can be tested independently.
- Hands are sorted after rolls for predictable display and simpler debugging.
- `None` marks unused scorecard categories without conflating them with a score of zero.

## Author

Tiago Antunes

## License

The original code and documentation are shared for portfolio viewing under an all-rights-reserved notice. See [LICENSE](LICENSE).
