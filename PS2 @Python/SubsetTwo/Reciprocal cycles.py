# 26
import time


def checkCycle(loopList, checkVal, num, bTC):
    if checkVal == loopList[bTC]:
        bTC += 1
        return bTC
    return 0


def getMax(param):
    bTC = 0
    loopList = []
    if param < 10:
        checkMod = 10
    elif param < 100:
        checkMod = 100
    else:
        checkMod = 1000
    checkVal = checkMod % param
    curVal = checkVal * 10
    loopList.append(checkVal)
    for num in range(1, 2000):
        curVal = curVal % param
        if curVal == 0:
            return 0
        bTC = checkCycle(loopList, curVal, num, bTC)
        if bTC * 2 == num:
            return bTC + 1
        loopList.append(curVal)
        curVal = curVal * 10
    return 0


def start():
    maxlen = 0
    for num in range(1, 1000):
        maxlen = max(maxlen, getMax(num))
        print(f"{num}:{maxlen}  {1/num}")
    pass


startTime = time.clock()
start()
print("--- %s seconds ---" % (time.clock() - startTime))
