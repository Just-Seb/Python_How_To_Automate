#!python3

import random
import time
import string

def letter_picker():

    characters = [1,2,3,4,5,6,7,8,9,0,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    return random.choice(str(characters))

start_time = time.time()
buffer = 'a'
str(buffer)

print('Started')

wordFile = open('BufferTrillion.txt', 'w')

for i in range(0,2000000000):
    for i in range(0,200):
        buffer = buffer + letter_picker()

    wordFile.write(buffer + '\n')
    buffer = 'a'

wordFile.close()

print('File Closed')

end_time = time.time()

total_time = end_time - start_time

print('It took ' + str(total_time) + ' seconds to run this program')
