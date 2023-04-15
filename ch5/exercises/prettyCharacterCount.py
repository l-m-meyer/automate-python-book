from pprint import pprint as pp
# import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] += 1

pp(count)
# pprint.pprint(count)