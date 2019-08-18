# 32
import time


def concat(a, b):
    return int(f"{a}{b}")


def isPandigital(n, val):
    return n % val == 0 and ''.join(sorted(f"{n}{val}{int(n/val)}")) == '123456789'


def checkNumner(n):
    arrTemp = ([1, 2, 3, 4, 5, 6, 7, 8, 9])
    arr = ([1, 2, 3, 4, 5, 6, 7, 8, 9])
    for elm in map(int, str(n)):  # O(arr.length)
        try:
            arr.remove(elm)
        except:
            return False
    arrMultipels = ([])
    for elmFirst in arr:  # O(arr.length^2)
        for elmSecond in arr:
            if elmFirst != elmSecond:
                arrMultipels.append(concat(elmFirst, elmSecond))
    arrMultipels.extend(arrTemp)
    for c in arrMultipels:
        if isPandigital(n, c):
            print(f"\n{c} * {int(n/c)} = {n}")
            return True
    return False
    pass


def start():
    sum = 0
    maxValue = 9876
    minValue = 1234
    for i in range(minValue, maxValue):
        if checkNumner(i):
            sum += i
            print(f"{sum}: {i}")
    print(sum)
    pass


startTime = time.time()
start()
print("--- %s seconds ---" % (time.time() - startTime))
