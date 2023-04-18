#! python3
# multiplicationQuiz.py - A timed multiplication quiz program.


import pyinputplus as pyip
import random, time


def start_quiz():
    numberOfQuestions = 10
    correctAnswers = 0

    for questionNumber in range(1, numberOfQuestions + 1):
        prompt, num1, num2 = generate_question(questionNumber)
        
        correctAnswers = handle_question(prompt, num1, num2, correctAnswers)
        
        time.sleep(1)
    print(f'Score: {correctAnswers} / {numberOfQuestions}')


def generate_question(qnum):
    # pick two random numbers:
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)

    prompt = f'#{qnum}: {num1} x {num2} = '
   
    return prompt, num1, num2
    

def handle_question(prompt, n1, n2, correctAnswers):
    try:
        # right answers are handled by allowRegexes
        # wrong answers are handled by blockRegexes, with a custom message
        pyip.inputNum(prompt, 
                      allowRegexes=[f'^{n1 * n2}$'],
                      blockRegexes=[('.*', 'Incorrect!')],
                      timeout=20,
                      limit=10)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        # this block runs if no exceptions were raised in the try block
        print('Correct!')
        correctAnswers += 1
    return correctAnswers


if __name__ == '__main__':
    start_quiz()