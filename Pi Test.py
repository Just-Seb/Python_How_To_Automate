import math
def calcSide(a):
     side = math.sqrt(2)
     H = math.sqrt(1/2)
     for x in range(1,a):
             b = side/2
             x = 1 - H
             side = math.sqrt(b**2+x**2)
             H = math.sqrt(1-(side/2)**2)
     r = {"side":side,"H":H}
     return r

def calcPi(a):
     r = calcSide(a)
     side = r["side"]
     H = r["H"]
     pi = (side*H*(2**(a+1)))/2
     return pi

calcPi(5000)
