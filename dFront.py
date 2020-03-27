from timeZoneBot import *

filename = "data.txt"

array = {}
#inputTime("KAWAII BAAAKA", "12:24", "data.txt")
#inputTime("Someone else", "20:52", "data.txt")
tArray = readFile(filename)

request("KAWAII BAAAKA", "20:58", tArray)
