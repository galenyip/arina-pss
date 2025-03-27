def check_winner(player_1, player_2):
    """Check who wins based on the choices."""
    if player_1 == player_2:
        return "It is a tie!"
    elif (player_1 == 1 and player_2 == 3) or \
         (player_1 == 2 and player_2 == 1) or \
         (player_1 == 3 and player_2 == 2):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

def main_game():
    """Main function to run the game."""
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

if __name__ == "__main__":
    main_game() 