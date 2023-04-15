#! python3
# zombieDice.py - Players are zombies trying to eat as many human brains
# as possible without getting shot 3 times.


import zombiedice, random as r


class MyZombie:
    def __init__(self, name):
        # All zombies much have a name:
        self.name = name


    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.


        diceRollResults = zombiedice.roll()         # first roll
                
        """
        roll() returns a dictionary with keys 'brains', 'shotgun', and
        'footsteps' with how many rolls of each type there were.
        The 'rolls' key is a list of (color, icon) tuples with the
        exact roll result information.

        Example of a roll() return value:
        {'brains': 1,
         'footsteps': 1,
         'shotgun': 1,
         'rolls': [('yellow', 'brains'),
                    ('red', 'footsteps'),
                    ('green', 'shotgun')]}
        """

        # BOT0:
        BOT0_brains = 0
        while diceRollResults is not None:
            BOT0_brains += diceRollResults['brains']

            if BOT0_brains < 2:
                diceRollResults = zombiedice.roll()     # roll again
            else:
                break


        # BOT1: after first roll, randomly decides if it will continue or stop:
        BOT1_brains = 0
        while diceRollResults is not None:
            BOT1_brains += diceRollResults['brains']
            if r.randint(0, 1) == 1:
                diceRollResults = zombiedice.roll()     # roll again
            else:
                break


        # BOT2: stops rolling after it has rolled two brains
        BOT2_brains = 0
        while diceRollResults is not None:
            BOT2_brains += diceRollResults['brains']

            if BOT2_brains == 2:
                break
            else:
                diceRollResults = zombiedice.roll()     # roll again


        # BOT3: stops rolling after it has rolled two shotguns
        BOT3_shotguns = 0
        while diceRollResults is not None:
            BOT3_shotguns += diceRollResults['shotgun']

            if BOT3_shotguns == 2:
                break
            else:
                diceRollResults = zombiedice.roll()     # roll again


        # BOT4: initially decides it will roll the dice 1 to 4 times,
        # but will stop early if it rolls two shotguns.
        BOT4_shotguns = 0
        roll_max = r.randint(1, 4)
        roll_num = 0
        
        while diceRollResults is not None:
            BOT4_shotguns += diceRollResults['shotgun']
            if roll_num == roll_max or BOT4_shotguns == 2:
                break
            else:
                roll_num += 1
                diceRollResults = zombiedice.roll()     # roll again


        # BOT5: stops rolling after it has rolled more shotguns than brains.
        BOT5_brains = 0
        BOT5_shotguns = 0

        while diceRollResults is not None:
            BOT5_brains += diceRollResults['brains']
            BOT5_shotguns += diceRollResults['shotgun']

            if BOT5_shotguns > BOT5_brains:
                break
            else:
                diceRollResults = zombiedice.roll()     # roll again
    
zombies = (
    # zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    # zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    # zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2 Shotguns', minShotguns=2),
    # zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotgun', minShotguns=1),
    MyZombie(name='My Zombie Bot'),
    # Add any other zombie players here.
    MyZombie(name='Test1'),
    MyZombie(name='Test2'),
    MyZombie(name='Test3'),
    MyZombie(name='Test4'),
)

zombiedice.runTournament(zombies=zombies, numGames=100)
# zombiedice.runWebGui(zombies=zombies, numGames=1000)


















#######################################
# FIRST ATTEMPT BEFORE SCROLLING DOWN #
#######################################
'''
cup of 13 dice with the following icons:
   - brains
   - footsteps
   - shotgun

dice sides:
    - 2 sides with footsteps (all dies)
    - 2 or 3 brains (icon colour dependent)
    - 2 or 3 shotguns (icon colour dependent)

dice colours:
    - green-icon: more sides with brains
    - red-icon: more sides with shotguns
    - yellow-icon: even split of brains and shotguns
'''

# import random as r

# # Player randomly draws three dice from the cup and rolls them.
# # Players always roll exactly three dice.
# def drawDice():
#     dice = []

#     while len(dice) < 3:
#         dice.append(r.randint(1, 5))
#     print(dice)


# def rollDice():
#     # Dice sides
#     FOOTSTEP = 2
#     BRAIN = {'green': 3,
#              'red': 2,
#              'yellow': 2}
#     SHOTGUN = {'green': 2,
#                'red': 3,
#                'yellow': 2}
    
#     DICE_COLOURS = ('green', 'red', 'yellow')

# drawDice()