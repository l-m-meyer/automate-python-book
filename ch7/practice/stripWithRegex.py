#! python3
# stripWithRegex.py - Strip whitespace at the beginning and end of a string, or remove a specific character from the string.


import re


def stripR(str, char=' '):
    # remove matching character(s) found at beginning of string
    strip_left = re.sub(f"^{char}+", "", str)
    # remove matching charater(s) found at end of strip_left string
    result = re.sub(f"{char}+$", "", strip_left)
    
    print(f'BEFORE: "{str}", "{char}"')
    print(f'AFTER: "{result}"')
    print()


# TEST CASES
stripR(' string ')
stripR('    string    ')
stripR(' string string ')
stripR(' ring stringer ', 'r')
stripR('red rover', 'r')
stripR('red rover', 're')
stripR(' red rover', ' r')