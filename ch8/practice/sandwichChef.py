#! python3
# sandwichChef.py - A program that asks users for their sandwich preferences and ensures valid inputs.


import pyinputplus as pyip


def make_me_a_sandwich():
    bread, cost = bread_choice()
    
    print(bread, cost)


def bread_choice():
    prompt = pyip.inputMenu(['wheat', 'white', 'sourdough'])
    
    if prompt == 'wheat':
        cost = 2.25
    elif prompt == 'white':
        cost = 2.20
    else:
        cost = 3.00

    return prompt, cost


if __name__ == '__main__':
    make_me_a_sandwich()