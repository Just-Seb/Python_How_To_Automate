#!python3

import random
import time
import threading


def letter_picker(version):

    file = 'BufferTrillion' + version + '.txt'
    wordFile = open(file, 'w')

    characters = [1,2,3,4,5,6,7,8,9,0,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for i in range(0,5000):
        for i in range(0,200):
            str(choice) = random.choice(str(characters))

    wordFile.close()

    print('File Closed')

    end_time = time.time()

    total_time = end_time - start_time

    print('It took ' + str(total_time) + ' seconds to run this program')


onefile = threading.Thread(target=letter_picker(), args='1')
onefile.start()

twofile = threading.Thread(target=letter_picker(), args='2')
twofile.start()

threefile = threading.Thread(target=letter_picker(), args='3')
threefile.start()

fourfile = threading.Thread(target=letter_picker(), args='4')
fourfile.start()