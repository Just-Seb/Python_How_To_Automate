#! python3
# countDown.py - A simple countdown script.

import time, subprocess

endFile = open('endFile.txt', 'w')
endFile.write('It\'s over!!! It\'s over!!! It\'s over!!! \n It\'s over!!! It\'s over!!! It\'s over!!! \n It\'s '
              'over!!! It\'s over!!! It\'s over!!!')
endFile.close()

try:
    print('How long do you want the countdown to be?')
    requesed_time = int(input())

    timeLeft = requesed_time
    while timeLeft > 0:
        print(timeLeft, end='   ')
        time.sleep(1)
        timeLeft = timeLeft - 1

    # at the end of the countdown play the sound file and open a text file

    subprocess.Popen(['start', 'BOMB_SIREN-BOMB_SIREN-247265934.mp3'], shell=True)
    subprocess.Popen(['start', 'endFile.txt'], shell=True)

except KeyboardInterrupt:
    print('Countdown aborted')

