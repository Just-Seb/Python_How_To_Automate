import logging
logging.basicConfig(filename='myProgramlog.txt', level=logging.disable(), format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

def factorial(n):
    logging.critical('Start of factorial(%s%%)' % (n))
    total = 1
    for i in range(1,n + 1):
        total *= i
        logging.info('i is ' + str(i) + ', total is ' + str(total))
    logging.warning('End of factorial(%s%%)' % (n))
    return total

print(factorial(5))
logging.debug('End of program')