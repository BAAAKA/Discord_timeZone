#test
from functions import *


time = input("Your time? (xx:xx format): ")
log("Input: {}".format(time))
if not(validTime(time)):
    log("Invalid Input", "e")
    exit()
h, m = time.split(":")
h=int(h)
m=int(m)

while h>24:
    h-=24
while m>60:
    m-=60
log("hour  : {}".format(h))
log("minute: {}".format(m))

