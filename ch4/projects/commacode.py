# Write a function that takes a list value as an argument
# returns a string with all the items separated by a comma and a space
# with `and` inserted before the last item

spam = ['apples', 'bananas', 'tofu', 'cats']

def listValues(arg):
    str = ''
    for i in arg:
        if i != arg[-1]:
            str += f'{i}, '
        else:
            str += f'and {i}'
    print(str)

listValues(spam)