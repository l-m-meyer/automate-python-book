#! python3
# factorialLog.py


import logging
# logging.disable()

# Log to console
# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

# Log to a file 
logging.basicConfig(filename='myProgramLog.txt',
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')


def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug(f'i is {str(i)}, total is {str(total)}')
    logging.debug('End of factorial (%s)' % (n))
    return total


print(factorial(5))
logging.debug('End of program')