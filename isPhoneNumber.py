def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-' and ',':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-' and ',':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True

import pyperclip

"""
answer = isPhoneNumber()
if answer == True:
    print('It is a phone number!')
else:
    print('Sorry it is not a phone number')


print(isPhoneNumber(pyperclip.paste()))
"""

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'

for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
    else:
        print('Failed')