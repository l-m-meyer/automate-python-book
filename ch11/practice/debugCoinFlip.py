#! python3
# debugCoinFlip.py - Debug to find the errors!


import random


guess = ''

while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

# BUG: never sets toss value to heads or tails
toss = random.randint(0, 1)     # 0 is tails, 1 is heads

# to resolve bug, assign toss value to heads or tails
if toss:
    toss = 'heads'
else:
    toss = 'tails'


if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')