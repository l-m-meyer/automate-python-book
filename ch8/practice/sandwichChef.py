#! python3
# sandwichChef.py - A program that asks users for their sandwich preferences and ensures valid inputs.


import pyinputplus as pyip


def make_me_a_sandwich():
    bread, total = bread_choice()
    protein, total = protein_choice(total)
    cheese, total = cheese_choice(total)
    condiments, total = condiment_choice(total)
    sandwiches, total = num_of_sandwiches(total)
    
    print(f'''Your order is for {sandwiches} sandwiches each with the following:
        bread: {bread},
        protein: {protein},
        cheese: {cheese},
        condiments: {*condiments,}
    For a total of ${total}''')


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


def cheese_choice(cost):
    choice = pyip.inputYesNo('Would you like some cheese?\n')

    if choice == 'yes':
        choice = pyip.inputMenu(['cheddar', 'swiss', 'mozzarella'])
        cost += 1.50
    
    return choice, cost


def condiment_choice(cost, toppings=[]):
    choice = pyip.inputYesNo('Would you like any more toppings?\n')

    if choice == 'yes':
        choice = pyip.inputMenu(['mayo', 'mustard', 'lettuce', 'tomato'])
        toppings.append(choice)
        cost += 0.5
        return condiment_choice(cost, toppings)
    
    return toppings, cost


def num_of_sandwiches(cost):
    choice = pyip.inputInt('How many sandwiches do you want?\n', min=1)
    total = choice * cost
    
    return choice, round(total, 2)


if __name__ == '__main__':
    make_me_a_sandwich()