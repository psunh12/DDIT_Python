from random import random
def getHJ():
    ret = ""
    rnd = random()
    if rnd >0.5 :
        ret = "홀"
    else:
        ret = "짝"
    return ret


com = getHJ()
print("com",com)