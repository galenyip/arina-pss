# Rock Paper Scissors Game

A simple Python implementation of the Rock Paper Scissors game with flowchart generators.

## Requirements

Before running the program, make sure you have the required dependencies:

```
pip install -r requirements.txt
```

Note: You also need to have Graphviz installed on your system for the graphviz flowchart generation. 
You can download it from: https://graphviz.org/download/

## Running the Game

To play the rock-paper-scissors game:

```
python rock_paper_scissors.py
```

## Generating the Flowchart

### Using Graphviz

To generate the flowchart of the program using Graphviz:

```
python create_flowchart.py
```

This will create a PNG file named `rock_paper_scissors_flowchart.png` in the current directory.

### Using Mermaid

A Mermaid-based flowchart is available in the file `rock_paper_scissors_flowchart.md`.

You can view this flowchart:
- On GitHub (if you push your code to GitHub, it will render automatically)
- Using any Markdown viewer that supports Mermaid diagrams
- Using the Mermaid Live Editor: https://mermaid.live (paste the content between the mermaid tags)

## Game Rules

1. Paper (1) wins against Stone (3)
2. Scissors (2) win against Paper (1)
3. Stone (3) wins against Scissors (2)

Enter 0 at any point to end the game.

## Python Beginner's Guide to the Code

If you're new to Python, here's a breakdown of how this program works:

### Program Structure

The program is organized into functions - reusable blocks of code that perform specific tasks:

1. `check_winner()` - Determines who wins based on player choices
2. `main_game()` - Handles the game flow, user input, and output

### Key Python Concepts Used

#### 1. Functions
Functions are defined using the `def` keyword followed by the function name and parameters:
```python
def check_winner(player_1, player_2):
    # Function code here
```

#### 2. Conditional Statements
The program uses `if`, `elif` (else if), and `else` to make decisions:
```python
if player_1 == player_2:
    return "It is a tie!"
elif (conditions):
    return "Player 1 wins!"
else:
    return "Player 2 wins!"
```

#### 3. Loops
A `while True` loop keeps the game running until the user enters 0:
```python
while True:
    # Game code here
    if player_1 == 0:
        break  # Exits the loop
```

#### 4. Input and Type Conversion
The `input()` function gets text from the user, and `int()` converts it to a number:
```python
player_1 = int(input("Player 1, Enter your choice: "))
```

#### 5. Error Handling
`try`/`except` blocks catch errors if the user enters something that's not a number:
```python
try:
    # Code that might cause an error
except ValueError:
    print("Invalid input! Please enter a number.")
```

#### 6. Lists and Membership Testing
The code checks if a value is in a list using the `in` operator:
```python
if player_1 not in [1, 2, 3]:
    # Handle invalid input
```

#### 7. Main Function Check
The `if __name__ == "__main__":` line ensures the game only runs when the script is executed directly:
```python
if __name__ == "__main__":
    main_game()
```

### How to Modify the Game

To modify the game, you could:
- Add a score counter to track wins
- Implement a computer opponent with random choices
- Add more options (like "Rock, Paper, Scissors, Lizard, Spock")
- Create a graphical interface instead of text-based 