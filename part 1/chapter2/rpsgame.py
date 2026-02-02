import random, sys

print("ROCK, PAPER, SCISSORS")

wins = 0
losses = 0
ties = 0

while True:
    print(f"{wins} wins, {losses} losses, {ties} ties")
    while True:
        print("enter your move: (r) rock, (p) paper, (s) scissors or (q) quit")
        playerMove = input()
        if playerMove == 'q':
            print("Thanks for playing!")
            sys.exit()
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break
        print("Type one of r, p, s, or q")

    if playerMove == 'r':
        print("ROCK versus...")
    elif playerMove == 'p':
        print("PAPER versus...")
    elif playerMove == 's':
        print("SCISSORS versus...")
    
    randomNum = random.randint(1, 3)
    if randomNum == 1:
        computerMove = 'r'
        print("ROCK")
    elif randomNum == 2:
        computerMove = 'p'
        print("PAPER")
    elif randomNum == 3:
        computerMove = 's'
        print("SCISSORS")


    if playerMove == computerMove:
        print("It's a tie!")
        ties += 1
    elif (playerMove == 'r' and computerMove == 's'):
        print("You win!")
        wins += 1
    elif (playerMove == 'p' and computerMove == 'r'):
        print("You win!")
        wins += 1 
    elif (playerMove == 's' and computerMove == 'p'):
        print("You win!")
        wins += 1
    elif (playerMove == 'r' and computerMove == 'p'):
        print("You lose!")
        losses += 1
    elif (playerMove == 'p' and computerMove == 's'):
        print("You lose!")
        losses += 1
    elif (playerMove == 's' and computerMove == 'r'):
        print("You lose!")
        losses += 1