
def playgame():
    print("Welcome to the NIM Game. \n Rules: Players take turns removing 1-3 sticks from the heap. \n The player who takes the LAST stick WINS! \n Good luck!")

    heapSize = int(input("How many sticks in the heap for this game? "))
    print(f"Starting this game with {heapSize} sticks.")

    player1 = input("Player 1, What is your name? ")
    player2 = input("Player 2, What is your name? ")

    print(f"\n {player1} vs {player2} - Let the game begin!\n")
    
    currentPlayer = player1
    
    while heapSize > 0:
        print(f"\nSticks remaining: {heapSize}")
        move = int(input(f"Player {currentPlayer}, pick a number (1-3): "))
        
        # Validate move
        while move < 1 or move > 3 or move > heapSize:
            if move > 3:
                print("Players can only pick 1-3 sticks at most.")
            elif move > heapSize:
                print(f"You can't pick more sticks than available ({heapSize}).")
            else:
                print("You must pick at least 1 stick.")
            move = int(input(f"Player {currentPlayer}, pick a number (1-3): "))
        
        # Update heap
        heapSize -= move
        
        # Check for winner
        if heapSize == 0:
            print(f"\nPlayer {currentPlayer} took the last stick and WINS!")
            break
        
        # Switch players
        currentPlayer = player2 if currentPlayer == player1 else player1

playgame()