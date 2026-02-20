# Nim Game 🎮

A command-line implementation of the classic **Nim** stick game in Python, featuring multiple player types including human input, random, minimal, and optimal AI strategies.

## How the Game Works

Players take turns removing **1 to 3 sticks** from a shared heap. The player who takes the **last stick loses**. The game supports two players chosen from a pool of available strategies.

## Player Types

| Player | Description |
|--------|-------------|
| `nim_human` | A human player — prompted to enter their move via the terminal |
| `nim` | Picks a random legal move (1–3 sticks) |
| `nim_minimal` | Always takes exactly 1 stick |
| `nim_best` | Plays optimally using the modulo-4 strategy |

## Optimal Strategy

`nim_best` uses the following logic: if the current heap size `n % 4 != 0`, take `n % 4` sticks to leave your opponent in a losing position. If `n % 4 == 0`, you are already in a losing position, so a random legal move is made.

## How to Run

Make sure you have Python 3 installed, then run:

```bash
python nim.py
```

You will be prompted to:
1. Enter a heap size (must be greater than 0)
2. Choose two **different** players from the available pool
3. Confirm you are ready to start

## Example Session

```
What is your desired heap size? 12
Pick your players out of these: ['nim_minimal', 'nim', 'nim_human', 'nim_best']
nim_human
Pick your players out of these: ['nim_minimal', 'nim', 'nim_human', 'nim_best']
nim_best
Welcome to the game, nim_human vs nim_best
Are you Ready? Yes/No Yes
Heap has 12 sticks.
There are 12 sticks in the heap. How many do you take? 2
nim_human takes 2 sticks.
Heap has 10 sticks.
nim_best takes 2 sticks.
...
```

## Requirements

- Python 3.x
- No external libraries required (only the built-in `random` module)
