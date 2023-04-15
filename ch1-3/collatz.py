def collatz(number):
    # If number is even:
    if not number % 2:
        print(f'{number} // 2 = {number // 2}')
        return number // 2
    # If number is odd:
    else:
        print(f'3 * {number} + 1 = { 3 * number + 1}')
        return 3 * number + 1

try:
    print('Enter a number:')
    number = None
    while number != 1:
        number = int(input())
        collatz(number)

except ValueError:
    print('You must enter an integer')