#! python3
# sandwichChef.py - A program that asks users for their sandwich preferences and ensures valid inputs.


import pyinputplus as pyip


def make_me_a_sandwich():
    bread, total = bread_choice()
    protein, total = protein_choice(total)
    print(bread, protein, total)


def bread_choice():
    choice = pyip.inputMenu(['wheat', 'white', 'sourdough'])
    
    if choice in ['wheat', 'white']:
        cost = 2.25
    else:
        cost = 3.00

    return choice, cost


def protein_choice(cost):
    choice = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'])

    if choice in ['chicken', 'turkey', 'ham']:
        cost += 4.50
    else:
        cost += 3.95

    return choice, cost


if __name__ == '__main__':
    make_me_a_sandwich()