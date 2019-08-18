# 34

import time


def fact(n, total=1):
    while True:
        if n == 1:
            return total
        n, total = n - 1, total * n


def start():
    print(fact(100))
    pass


startTime = time.time()
start()
print("--- %s seconds ---" % (time.time() - startTime))
