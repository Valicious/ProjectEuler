# 30
import time


def splitt(num):
    newVal = [int(i) ** 5 for i in str(num)]
    total = sum(newVal)
    if total == num:
        return total
    return 0


def start():
    total = 0
    for num in range(2, 1000000):
        newVal = splitt(num)
        if newVal != 0:
            total += splitt(num)
            print(f"{num} @ {newVal}. sum({total})")
    print(total)
    pass


startTime = time.time()
start()
print("--- %s seconds ---" % (time.time() - startTime))
