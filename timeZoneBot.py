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
    lines = file.read().split('\n')
    for line in lines[:-1]:
        who, h, m, t = line.split("###")
        tArray[who] = (h, m)
    file.close()
    return tArray

def inputTime(who, time, filename):
    #Input
    file = loadFile(filename, "a")
    log("Input: {}".format(time))
    if not (validTime(time)):
        log("Invalid Input", "e")
        exit()
    if ":" not in time:
        time += ":00"
    h, m = time.split(":")
    h = int(h)
    m = int(m)

    h = lowerTime(h, 24)
    m = lowerTime(m, 60)

    log("hour  : {}".format(h))
    log("minute: {}".format(m))
    difH, difM = getTimeDifference(h, m)
    log("User: {} has a time difference of {}:{}".format(who, difH, difM))
    inputText = inputIntoFile(who, difH, difM)
    file.write(inputText)
    file.close()

def request(requester, time, tArray):
    requesterH = int(tArray[requester][0])
    requesterM = int(tArray[requester][1])
    reqH, reqM = time.split(":")
    reqH = int(reqH)
    reqM = int(reqM)

    zH = reqH+requesterH
    zM = reqM+requesterM

    rText = "=================================="
    for entry in tArray:
        log(entry)
        if not entry == requester:
            hDif = zH + int(tArray[entry][0])
            mDif = zM + int(tArray[entry][1])
            hDif = lowerTime(hDif, 24)
            mDif = lowerTime(mDif, 60)
            time = getTimeCorrectly(hDif, mDif)
            text = "\n{}, for you its {}".format(entry, time)
            log(text)
            rText += text
    print("")
    print(rText)



