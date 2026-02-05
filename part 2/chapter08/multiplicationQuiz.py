import pyinputplus as pyip
import random
import time

number_of_questions = 10
correct_answer = 0
for question_number in range(number_of_questions):
    #pick two random numbers:
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)

    prompt = f'# {question_number + 1}) {num1} x {num2}\n'

    try:
        pyip.inputStr(prompt, allowRegexes=[f'^{num1 * num2}$'],
                       blockRegexes=[('.*', 'Incorrect')],
                       timeout=8, limit=3)
    except pyip.TimeoutException:
        print("out of time")
    except pyip.RetryLimitException:
        print("out of tries")
    
    else:
        print('Correct!')
        correct_answer += 1
    
    time.sleep(1) #brief pause to let user see the result.

print(f'score: {correct_answer} of {number_of_questions} questions!')