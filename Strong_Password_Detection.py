import re
import pyperclip

capital = re.compile(r'[A-Z]')
lower = re.compile(r'[a-z]')
number = re.compile(r'[0-9]')

def strong_Password_detection(inputString):
    if len(inputString) >= 8:
        if capital.search(inputString) and lower.search(inputString) and number.search(inputString):
            print('You have a strong password')
        else:
            print('please make a new password')

clipBoard = pyperclip.paste()
#clipBoard = ''

strong_Password_detection(clipBoard)
