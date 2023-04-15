# Flip a coin 100 times. Write "H" for heads and "T" for tails.
# Track how often a streak of six occurs.
import random

# Generate list of 100 coin flips
def flip100():
    flips = []

    for flip in range(100):
        r = random.randint(0, 1)
        
        if r == 0:
            flips.append('H')
        if r == 1:
            flips.append('T')
    # invoke function to check number of streaks        
    return checkStreak(flips)


# Check number of streaks
def checkStreak(flips):
    numOfStreaks = 0
    reached6 = False

    for i, flip in enumerate(flips):
        if numOfStreaks == 6:
            # print(f'{flip} has reached a streak of 6.')
            reached6 = True

        if i == 0:
            numOfStreaks += 1
        
        if i > 0:
            if flip == flips[i - 1]:
                numOfStreaks += 1
            else:
                numOfStreaks = 0
    return reached6


# Generate sample of 10000 tests
def sample10000():
    success = 0

    for sample in range(10000):
        flip = flip100()
        if flip == True:
            success += 1
    
    print(f'There were {success} flips that reached 6.')
    print('Chance of streak: %s%%' % (success / 100))

sample10000()