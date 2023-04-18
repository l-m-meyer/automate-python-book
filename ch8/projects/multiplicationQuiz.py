#! python3
# multiplicationQuiz.py - A timed multiplication quiz program.


import pyinputplus as pyip
import random, time


def start_quiz():
    numberOfQuestions = 10
    correctAnswers = 0

    for questionNumber in range(numberOfQuestions):
        prompt, answer = generate_question(questionNumber)
        
        correctAnswers = handle_question(prompt, answer, correctAnswers)
        
        time.sleep(1)
    print(f'Score: {correctAnswers} / {numberOfQuestions}')


def generate_question(qnum):
    # pick two random numbers:
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    op = generate_op()
    answer = get_answer(num1, num2, op)
   
    prompt = f'#{qnum}: {num1} {op} {num2} = '
    
    return prompt, answer


def generate_op():
    ops = ['x', '/', '+', '-']
    op = random.randint(0,3)

    return ops[op]
    
    
def get_answer(n1, n2, op):
    if op == 'x':
        return n1 * n2
    if op == '/':
        return n1 / n2
    if op == '+':
        return n1 + n2
    if op == '-':
        return n1 - n2
    

def handle_question(prompt, answer, correctAnswers):
    try:
        # right answers are handled by allowRegexes
        # wrong answers are handled by blockRegexes, with a custom message
        pyip.inputStr(prompt, 
                      allowRegexes=[f'^{answer}$'],
                      blockRegexes=[('.*', 'Incorrect!')],
                      timeout=8,
                      limit=3)
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