import re

def validTime(time):
    if(re.findall(r'^\d{1,2}:\d{1,2}$', time)):
        return True
    else:
        return False

def log(t, type = "i"):
    if(type == "i"):
        typeT = "[INFO] "
    elif(type == "e"):
        typeT = "[ERROR]"


    print("{} {}".format(typeT, t))
