#! python3
# stripWithRegex.py - Strip whitespace at the beginning and end of a string, or remove a specific character from the string.


import re


def stripR(str, char=' '):
    strip_left = re.sub(f"^{char}+", "", str)
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