# Rock Paper Scissors in Python: A Beginner's Guide

---

## What is Rock Paper Scissors?

* A classic hand game for two players.
* Each player chooses one of three shapes: Rock, Paper, or Scissors.
* The winner is decided based on these rules:
    * Rock crushes Scissors
    * Scissors cuts Paper
    * Paper covers Rock

---

## Our Goal

To create a simple, text-based version of the Rock Paper Scissors game using Python that two players can play together.

---

## How to Play Our Game

1.  **Open your terminal or command prompt.**
2.  **Navigate to the project folder.**
3.  **Run the program:**
    ```bash
    python rock_paper_scissors.py
    ```
4.  **Follow the on-screen instructions!**
    *   Player 1 enters their choice (1 for Paper, 2 for Scissors, 3 for Stone).
    *   Player 2 enters their choice.
    *   The program declares the winner or a tie.
    *   Enter 0 to quit.

---

## How the Code is Structured

We use **functions** to organize the code into logical blocks.

*   `paper_function()`: Decides the outcome if Player 1 chose Paper.
*   `scissors_function()`: Decides the outcome if Player 1 chose Scissors.
*   `stone_function()`: Decides the outcome if Player 1 chose Stone.
*   `main()`: Runs the main game loop, gets input, calls the other functions, and prints results.

```python
# Example: paper_function
def paper_function(opponent_choice):
    """Determine the result when Player 1 chooses Paper"""
    if opponent_choice == 1:  # Paper vs Paper
        return "It is a tie!"
    # ... other rules ...

# Example: main function structure
def main():
    # Print instructions
    while True:
        # Get Player 1 input
        # Get Player 2 input
        # Determine winner based on choices
        if player_1 == 1:
            result = paper_function(player_2)
        # ... other choices ...
        # Print result
```

---

## Key Python Concepts Used

*   **Functions (`def`)**: Reusable blocks of code.
*   **Input (`input()`)**: Gets input from the user.
*   **Type Conversion (`int()`)**: Converts text input to numbers.
*   **Loops (`while True`)**: Repeats the game turns.
*   **Conditionals (`if`/`elif`/`else`)**: Makes decisions (who wins?).
*   **Loop Control (`break`, `continue`)**: Ends the game (`break`) or skips invalid input (`continue`).
*   **Error Handling (`try`/`except`)**: Catches errors if input isn't a number.
*   **Printing (`print()`)**: Shows messages and results to the players.

---

## Game Logic Example

Inside the `main()` function, after getting choices from both players:

```python
# Determine winner directly in main function
result = None
if player_1 == 1:  # Player 1 chose Paper
    result = paper_function(player_2) # Call the paper function
elif player_1 == 2: # Player 1 chose Scissors
    result = scissors_function(player_2)
elif player_1 == 3: # Player 1 chose Stone
    result = stone_function(player_2)

# Display result
print(result)
```

---

## Visualizing the Flow

For a visual overview of how the program runs, check out the flowchart:

[`mermaid_flowchart.md`](./mermaid_flowchart.md)

(You can view this on GitHub or using a Markdown tool that supports Mermaid.)

---

## Want to Try Modifying It?

*   Add a score counter.
*   Make Player 2 a computer opponent (using Python's `random` module).
*   Add more choices (Lizard, Spock?).

---

# The End

Thanks for exploring the Rock Paper Scissors game! 