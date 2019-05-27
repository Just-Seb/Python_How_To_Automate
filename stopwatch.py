#!python3
# stopwatch.py - A simple stopwatch program

import time

print('Press ENTER to start. After that press ENTER to lap. You can also press Crtl-C to quit.')
input()
print('Started!')
start_time = time.time()
last_time  = start_time
lapNum = 1

try:
    while True:
        input()
        lapTime = round(time.time() - last_time, 2)
        totalTime = round(time.time() - start_time, 2)
        print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='' + '\n')
        lapNum += 1
        last_time = time.time()
except KeyboardInterrupt:
    print('\nDone!')