# test
from functions import *

def loadFile(filename):
    try:
        file = open(filename, "w")
    except Exception as e:
        log("Error while loading file: {}".format(e),"e")
    return file


def inputTime(who, time, file):
    #Input
    log("Input: {}".format(time))
    if not (validTime(time)):
        log("Invalid Input", "e")
        exit()
    h, m = time.split(":")
    h = int(h)
    m = int(m)

    while h > 24:
        h -= 24
    while m > 60:
        m -= 60
    log("hour  : {}".format(h))
    log("minute: {}".format(m))
    difH, difM = getTimeDifference(h, m)
    log("User: {} has a time difference of {}:{}".format(who, difH, difM))
    inputText = inputIntoFile(who, h, m)
    file.write(inputText)







