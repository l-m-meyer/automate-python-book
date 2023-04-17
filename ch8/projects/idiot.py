#! python3
# idiot.py - How to keep an idito busy for hours.


import pyinputplus as pyip


def en_idiot():
    prompt = 'Want to know how to keep an idiot busy for hours?\n'
    response = pyip.inputYesNo(prompt)
    return response


def sp_idiot():
    prompt = '¿Quieres saber cómo mantener ocupado a un idiota durante horas?\n'
    response = pyip.inputYesNo(prompt, yesVal='sí', noVal='no')
    return response


if __name__ == '__main__':
    language_preference = pyip.inputChoice(['English', 'Spanish'])

    while True:
        if language_preference == 'English':
            response = en_idiot()
        else:
            response = sp_idiot()
        
        if response == 'no':
            break

    print('Thank you. Have a nice day.')