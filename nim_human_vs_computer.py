import random

def playgame():
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
    player1 = input("Player 1, what is your name? ")
    print("Computer is the second player. Are you ready?")
    computer = 'Computer'
    
    currentPlayer = player1
    print(f"Computer VS {player1}! \n LET'S BEGIN")

    while heapSize > 0:
        if currentPlayer == player1:
            while True:
                try:
                    move = int(input(f"{currentPlayer}, pick a number between 1 and 3: "))

                    if move < 1 or move > 3:
                        print("Players can only pick within 1-3 sticks")
                        move = int(input(f"{currentPlayer}, pick a number between 1 and 3"))
                    elif heapSize < move:
                        print("The number of sticks left in the heap is less than this")
                        move = int(input(f"{currentPlayer}, pick a number between 1 and 3"))
                    else:
                        break
                except ValueError:
                    print("Please enter a valid number!")
        else:
            move = random.randint(1, min(3, heapSize))
            print(f"{computer} picks {move} stick(s)")
        
        heapSize -= move
        print(f"{currentPlayer} removed {move} stick(s)")
        
        if heapSize == 0:
            print(f"{currentPlayer}, you just took the last stick and so you are the WINNER!")
            break

        currentPlayer = computer if currentPlayer == player1 else player1

playgame()




