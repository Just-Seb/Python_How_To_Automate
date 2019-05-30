#!python3

import random
import time
import threading
import string

def letter_picker(version):

    choice = None

    file = 'BufferTrillion' + version + '.txt'
    wordFile = open(file, 'w')

    characters = ['-','_','!','@','#','$','%','^','&','*','?','<','>',',',1,2,3,4,5,6,7,8,9,0,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for i in range(0,50):
        for i in range(0,200):
            if choice == None:
                choice = random.choice(str(characters))
            choice = choice + random.choice(str(characters))
        wordFile.write(choice + '\n')
        choice = None

    wordFile.close()


onefile = threading.Thread(target=letter_picker('1'), args=['1'])
onefile.start()

twofile = threading.Thread(target=letter_picker('2'), args=['2'])
twofile.start()

threefile = threading.Thread(target=letter_picker('3'), args=['3'])
threefile.start()

fourfile = threading.Thread(target=letter_picker('4'), args=['4'])
fourfile.start()
