import re
from time import gmtime, strftime


def validTime(time):
    if (re.findall(r'^\d{1,2}:\d{1,2}$', time)):
        return True
    else:
        return False


def log(t, type="i"):
    if (type == "i"):
        typeT = "[INFO] "
    elif (type == "e"):
        typeT = "[ERROR]"
    print("{} {}".format(typeT, t))


def getTimeDifference(inputH, inputM):
    h = int(strftime("%H", gmtime()))
    m = int(strftime("%M", gmtime()))
    finalH = inputH - h
    finalM = inputM - m
    log("dif hour  : {}".format(finalH))
    log("dif minute: {}".format(finalM))
    return finalH, finalM

def inputIntoFile(who, h, m):
    return "{}###{}###{}".format(who, h, m)