import time, random

reaction_time = 0

def timer():
    print('Get Ready!')
    delay = random.randint(1, 8)
    time.sleep(delay)
    start_time = time.time()
    print('Go!!!!!!')
    stop = input()
    end_time = time.time()
    result = end_time - start_time
    print('Your reaction time was: ' + str(result))


print('Are you ready? y/N')
answer = input()

if answer == 'Y' or 'y':
    timer()
else:
    print('Have a good day!')