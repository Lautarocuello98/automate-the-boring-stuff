import random
import time

print("Welcome to the Multiplication Quiz!")

number_of_questions = 10
correct_answers = 0

for question_number in range(number_of_questions):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    correct = num1 * num2

    start_time = time.time()
    intentos = 0

    while intentos < 3:
        elapsed_time = time.time() - start_time
        if elapsed_time > 8:
            print("out of time")
            break
        user_input = input(f'# {question_number + 1}) {num1} x {num2}\n')

        try:
            user = int(user_input)
            
        except ValueError:
            print("Please enter a valid number.")
            intentos += 1
            continue

        if user == correct:
            print("Correct!")
            correct_answers += 1
            break

        else:
            print("Incorrect")
            intentos += 1
            if intentos == 3:
                print("out of tries")   
            continue

print(f'score: {correct_answers} of {number_of_questions} questions!')