def playGame():

    print("Welcome to NIM Game. \n Rules: Each player can only pick 1-3 sticks. The player with the last stick WINS!")
    while True:
        try:
            heapSize = int(input("Pick a number for the heap size for this round: "))
            if heapSize > 0:
                break
            else:
                print(" Please enter a positive number!")
        except ValueError:
            print("Only integers allowed! \n")
    


    player1 = input("Player 1, What is your name: ")
    player2 = input("Player 2, What is your name: ")

    currentPlayer = player1

    while heapSize > 0:

        move = int(input(f"{currentPlayer}, Pick a number between 1-3: "))

        if move < 1 or move > 3:
            print("Player can only pick numbers between 1 and 3")
            move = int(input("Pick your number between 1-3: "))
        elif heapSize < move:
            print("The heap size is less than this move. Pick another number")
            move = int(input("Pick your number between 1-3: "))
        else:
            heapSize -= move

        if heapSize == 0:
            print(f"Player {currentPlayer} took the last stick and WINS!")
            break

        
        currentPlayer = player2 if currentPlayer == player1 else player1


playGame()
    
    