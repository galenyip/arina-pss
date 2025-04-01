def paper_function(opponent_choice):
    """Handle paper choice logic.
    
    Args:
        opponent_choice: The choice made by the opponent (1=paper, 2=scissors, 3=stone)
    
    Returns:
        str: Result of the match
    """
    if opponent_choice == 1:  # Paper vs Paper
        return "It is a tie!"
    elif opponent_choice == 2:  # Paper vs Scissors
        return "Player 2 wins!"
    elif opponent_choice == 3:  # Paper vs Stone
        return "Player 1 wins!"
    else:
        return "Invalid opponent choice"


def scissors_function(opponent_choice):
    """Handle scissors choice logic.
    
    Args:
        opponent_choice: The choice made by the opponent (1=paper, 2=scissors, 3=stone)
    
    Returns:
        str: Result of the match
    """
    if opponent_choice == 1:  # Scissors vs Paper
        return "Player 1 wins!"
    elif opponent_choice == 2:  # Scissors vs Scissors
        return "It is a tie!"
    elif opponent_choice == 3:  # Scissors vs Stone
        return "Player 2 wins!"
    else:
        return "Invalid opponent choice"


def stone_function(opponent_choice):
    """Handle stone choice logic.
    
    Args:
        opponent_choice: The choice made by the opponent (1=paper, 2=scissors, 3=stone)
    
    Returns:
        str: Result of the match
    """
    if opponent_choice == 1:  # Stone vs Paper
        return "Player 2 wins!"
    elif opponent_choice == 2:  # Stone vs Scissors
        return "Player 1 wins!"
    elif opponent_choice == 3:  # Stone vs Stone
        return "It is a tie!"
    else:
        return "Invalid opponent choice"


def check_winner(player_1, player_2):
    """Check who wins based on the choices."""
    # Use the appropriate function based on player 1's choice
    if player_1 == 1:  # Paper
        return paper_function(player_2)
    elif player_1 == 2:  # Scissors
        return scissors_function(player_2)
    elif player_1 == 3:  # Stone
        return stone_function(player_2)
    else:
        return "Invalid player 1 choice"


def main():
    """Main function to run the rock-paper-scissors game."""
    print("Make a choice below:")
    print("1 represent paper.")
    print("2 represent scissor")
    print("3 represent stone")
    print("0 to end game")
    
    while True:
        try:
            # Player 1's turn
            player_1 = int(input("Player 1, Enter your choice: "))
            if player_1 == 0:
                print("End")
                break
            
            if player_1 not in [1, 2, 3]:
                print("Invalid input! Please enter 1, 2, 3, or 0 to end.")
                continue
                
            # Player 2's turn
            player_2 = int(input("Player 2, Enter your choice: "))
            if player_2 == 0:
                print("End")
                break
                
            if player_2 not in [1, 2, 3]:
                print("Invalid input! Please enter 1, 2, 3, or 0 to end.")
                continue
            
            # Display result
            result = check_winner(player_1, player_2)
            print(result)
            
        except ValueError:
            print("Invalid input! Please enter a number.")


# Call main function directly
main() 