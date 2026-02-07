import random

def get_toss():
    if random.randint(0, 1) == 0:
        return 'tails'
    else:
        return 'heads'
    
def get_guess():
    guess = ''
    while guess not in ('heads', 'tails'):
        print('Guess the coin toss! Enter heads or tails:')
        guess = input()
    return guess

guess = get_guess()
toss = get_toss()

if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = get_guess()
    toss = get_toss()

    if toss == guess:
        print('You got it!')
    else:
        print('Nope. you are really bad at this game.')