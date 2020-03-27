# test
from functions import *

def loadFile(filename, type):
    try:
        file = open(filename, type)
    except Exception as e:
        log("Error while loading file: {}".format(e),"e")
    return file

def readFile(filename):
    tArray = {}
    file = loadFile(filename, "r")
    print(file.readlines())

    for entry in file.readlines():
        who, h, m, t = entry.split("###")

    file.close()
    return tArray

def inputTime(who, time, filename):
    #Input
    file = loadFile("data.txt", "a")
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
    file.close()







