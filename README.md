# Rock Paper Scissors Game

A simple Python implementation of the Rock Paper Scissors game with a flowchart.

## Requirements

No external dependencies are required to run the game.

## Running the Game

To play the rock-paper-scissors game:

```
python rock_paper_scissors.py
```

## Flowchart

A Mermaid-based flowchart visualizes the game logic in the file `mermaid_flowchart.md`.

You can view this flowchart:
- On GitHub (it renders automatically)
- Using any Markdown viewer that supports Mermaid diagrams
- Using the Mermaid Live Editor: https://mermaid.live (paste the content between the mermaid tags)

You can also generate the flowchart using:

```
python create_mermaid_flowchart.py
```

## Game Rules

1. Paper (1) wins against Stone (3)
2. Scissors (2) win against Paper (1)
3. Stone (3) wins against Scissors (2)

Enter 0 at any point to end the game.

## Python Beginner's Guide to the Code

If you're new to Python, here's a breakdown of how this program works:

### Program Structure

The program is organized into functions - reusable blocks of code that perform specific tasks:

1. `paper_function()` - Handles logic when Player 1 chooses paper
2. `scissors_function()` - Handles logic when Player 1 chooses scissors 
3. `stone_function()` - Handles logic when Player 1 chooses stone
4. `check_winner()` - Determines who wins by calling the appropriate function based on Player 1's choice
5. `main()` - Handles the game flow, user input, and output; serves as the entry point of the program

### Key Python Concepts Used

#### 1. Functions
Functions are defined using the `def` keyword followed by the function name and parameters:
```python
def paper_function(opponent_choice):
    # Function code here
```

#### 2. Conditional Statements
The program uses `if`, `elif` (else if), and `else` to make decisions:
```python
if opponent_choice == 1:  # Paper vs Paper
    return "It is a tie!"
elif opponent_choice == 2:  # Paper vs Scissors
    return "Player 2 wins!"
elif opponent_choice == 3:  # Paper vs Stone
    return "Player 1 wins!"
```

#### 3. Loops
A `while True` loop keeps the game running until the user enters 0:
```python
while True:
    # Game code here
    if player_1 == 0:
        break  # Exits the loop
```

#### 4. Loop Control Statements
The program uses two important loop control statements:

##### break
The `break` statement immediately terminates the loop and moves to the code after the loop:
```python
if player_1 == 0:
    print("End")
    break  # Exits the loop completely
```
In our game, `break` is used to end the game when a player enters 0.

##### continue
The `continue` statement skips the rest of the current iteration and jumps to the next iteration of the loop:
```python
if player_1 not in [1, 2, 3]:
    print("Invalid input! Please enter 1, 2, 3, or 0 to end.")
    continue  # Skips the rest of the loop and starts again from the top
```
In our game, `continue` is used when a player enters an invalid choice, allowing them to try again without proceeding to the next player's turn.

#### 5. Input and Type Conversion
The `input()` function gets text from the user, and `int()` converts it to a number:
```python
player_1 = int(input("Player 1, Enter your choice: "))
```

#### 6. Error Handling
`try`/`except` blocks catch errors if the user enters something that's not a number:
```python
try:
    # Code that might cause an error
except ValueError:
    print("Invalid input! Please enter a number.")
```

#### 7. Lists and Membership Testing
The code checks if a value is in a list using the `in` operator:
```python
if player_1 not in [1, 2, 3]:
    # Handle invalid input
```

### How to Modify the Game

To modify the game, you could:
- Add a score counter to track wins
- Implement a computer opponent with random choices
- Add more options (like "Rock, Paper, Scissors, Lizard, Spock")
- Create a graphical interface instead of text-based 