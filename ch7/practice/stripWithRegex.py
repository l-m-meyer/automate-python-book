#! python3
# stripWithRegex.py - Strip whitespace at the beginning and end of a string, or remove a specific character from the string.


import re


def stripR(str, char=' '):
    print(f'BEFORE: "{str}", "{char}"')
    print(f'AFTER: "{re.sub(char, "", str)}"')


stripR(' string ')
stripR(' string ', 'r')