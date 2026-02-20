import random
# I know that the optimal move here is whenever the computer picks a move that when divided by 4, equals to zero.

#n being the number of sticks in the heap. this is the legal move anyone can make.
def nim(n):
    return random.choice(range(1, min(n,3)+1))

def nim_minimal(n):
    return 1

#the optimal move, if the move is not optimal, that means you will juust pick a random number
def nim_best(n):
    move = n % 4
    if move != 0:
        return move
    else:
        return random.choice(range(1, min(n,3)+1))
    
def nim_human(n):
    while True:
        taken = int(input("There are %d sticks in the heap. How many do you take? " % n))
        if taken in range(1, min(3,n)+1):
            return taken
        print("Illegal Move")

player_pool= [nim_minimal, nim, nim_human, nim_best]
player_pool= {p.__name__:p for p in player_pool}
# dictionary: mapping the name of the function to the function in the list.


def pick_players():
    while True:
        player1 = input(f"Pick your players out of these: {player_pool.keys()} ")
        player2 = input(f"Pick your players out of these: {player_pool.keys()} ")

        if player1 in player_pool.keys() or player2 in player_pool.keys():
            players= [player1, player2]
            return players
        else:
            print("The player picked is not in the pool of players")

def game_controller():
    while True:
        n = int(input("What is your desired heap size? "))
        if n > 0:
            break
        else:
            print("Your heap size must be more than zero.")

    players = pick_players()
    
    print(f"Welcome to the game, {players[0]} vs {players[1]}")

    while True:
        ready = str(input("Are you Ready? Yes/No "))
        if ready == 'Yes':
            break
        else:
            print("Try again when you are ready.")
        
    current, other = players[0], players[1]

    while n > 0:
        print("Heap has %d sticks." %n)
        print(f"Current Player {current}")
        taken = player_pool[current](n)
        print("%s takes %d sticks. \n" %(current, taken))

        n-=taken
        current, other = other, current
    
    print("%s has lost." %current)

game_controller() 
        


