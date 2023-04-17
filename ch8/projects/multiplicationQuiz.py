#! python3
# multiplicationQuiz.py - A timed multiplication quiz program.


import pyinputplus as pyip
import random, time


def generate_question(qnum):
    # pick two random numbers:
        num1 = random.randint(0,9)
        num2 = random.randint(0,9)

        return f'#{qnum}: {num1} x {num2} = '


if __name__ == '__main__':
    numberOfQuestions = 10
    correctAnswers = 0

    for questionNumber in range(numberOfQuestions):
        prompt = generate_question(questionNumber)

        try:
            # right answers are handled by allowRegexes
            # wrong answers are handled by blockRegexes, with a custom message
            pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)],
                                blockRegexes=[('.*', 'Incorrect!')],
                                timeout=8, limit=3)
        except pyip.TimeoutException:
            print('Out of time!')
        except pyip.RetryLimitException:
            print('Out of tries!')
        else:
            # this block runs if no exceptions were raised in the try block.
            print('Correct!')
            correctAnswers += 1

        time.sleep(1)
    print('Score: %s / %s' % (correctAnswers, numberOfQuestions))