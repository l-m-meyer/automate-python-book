#! python3
# idiot.py - How to keep an idito busy for hours.


import pyinputplus as pyip


# Does the following:
# - Ask the user if they'd like to know how to keep an idiot busy for hours
# - If the user answers no, quit
# - If the user answers yes, go to Step 1


while True:
    prompt = 'Want to know how to keep an idiot busy for hours?\n'
    response = pyip.inputYesNo(prompt)
    
    if response == 'no':
        break

print('Thank you. Have a nice day.')