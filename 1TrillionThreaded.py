#!python3

import random
import time
import threading

all_start_time = time.time()

print('Started')


def letter_picker_1(version):

    start_time = time.time()

    choice = None

    file = 'BufferTrillion' + version + '.txt'
    wordFile = open(file, 'w')

    characters = ['-','_','!','@','#','$','%','^','&','*','?','<','>',',',1,2,3,4,5,6,7,8,9,0,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for i in range(0,6250000):
        for i in range(0,400):
            if choice == None:
                choice = random.choice(str(characters))
            choice = choice + random.choice(str(characters))
        wordFile.write(choice + '\n')
        choice = None

    wordFile.close()
    
    end_time = time.time()
    total_time = end_time - start_time
    total_time = str(total_time)
    
    print('It took ' + total_time + ' for thread ' + version)


def letter_picker_2(version):
    start_time = time.time()

    choice = None

    file = 'BufferTrillion' + version + '.txt'
    wordFile = open(file, 'w')

    characters = ['-', '_', '!', '@', '#', '$', '%', '^', '&', '*', '?', '<', '>', ',', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0,
                  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                  'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for i in range(0, 6250000):
        for i in range(0, 400):
            if choice == None:
                choice = random.choice(str(characters))
            choice = choice + random.choice(str(characters))
        wordFile.write(choice + '\n')
        choice = None

    wordFile.close()

    end_time = time.time()
    total_time = end_time - start_time
    total_time = str(total_time)

    print('It took ' + total_time + ' for thread ' + version)


def letter_picker_3(version):
    start_time = time.time()

    choice = None

    file = 'BufferTrillion' + version + '.txt'
    wordFile = open(file, 'w')

    characters = ['-', '_', '!', '@', '#', '$', '%', '^', '&', '*', '?', '<', '>', ',', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0,
                  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                  'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for i in range(0, 6250000):
        for i in range(0, 400):
            if choice == None:
                choice = random.choice(str(characters))
            choice = choice + random.choice(str(characters))
        wordFile.write(choice + '\n')
        choice = None

    wordFile.close()

    end_time = time.time()
    total_time = end_time - start_time
    total_time = str(total_time)

    print('It took ' + total_time + ' for thread ' + version)


def letter_picker_4(version):
    start_time = time.time()

    choice = None

    file = 'BufferTrillion' + version + '.txt'
    wordFile = open(file, 'w')

    characters = ['-', '_', '!', '@', '#', '$', '%', '^', '&', '*', '?', '<', '>', ',', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0,
                  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                  'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for i in range(0, 6250000):
        for i in range(0, 400):
            if choice == None:
                choice = random.choice(str(characters))
            choice = choice + random.choice(str(characters))
        wordFile.write(choice + '\n')
        choice = None

    wordFile.close()

    end_time = time.time()
    total_time = end_time - start_time
    total_time = str(total_time)

    print('It took ' + total_time + ' for thread ' + version)


onefile = threading.Thread(target=letter_picker_1('1'), args=['1'])

twofile = threading.Thread(target=letter_picker_2('2'), args=['2'])

threefile = threading.Thread(target=letter_picker_3('3'), args=['3'])

fourfile = threading.Thread(target=letter_picker_4('4'), args=['4'])


onefile.start()
twofile.start()
threefile.start()
fourfile.start()

total_end_time = time.time()

time_taken = total_end_time - all_start_time
time_taken = str(time_taken)

print('It took for the whole program ' + time_taken)
