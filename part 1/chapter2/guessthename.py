import random

secret_number = random.randint(1, 20)
print("I'm thinking of a number between 1 and 20. Can you guess it?")

for guesstaken in range(1, 5):
    print("Take a guess.")
    guess = int(input())

    if guess < secret_number:
        print("Your guess is too low.")
    elif guess > secret_number:
        print("Your guess is too high.")
    else:
        break
if guess == secret_number:
    print(f"good job! You guessed my number in {guesstaken} guesses!")
else:
    print(f"Sorry, you've run out of guesses. The number I was thinking of was {secret_number}.")