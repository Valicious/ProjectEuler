# 25
import time

fib = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]


def start():
    thousandDigits = "1"
    for num in range(1000-1):
        thousandDigits += "0"
    print(len(thousandDigits))
    while True:
        last = len(fib)-1
        fn = fib[last] + fib[last-1]
        fib.append(fn)

        if fn > int(thousandDigits):
            print(f"done. {fn}")
            print(len(fib))
            break
        else:
            print(f"at {fn}")

    pass


startTime = time.clock()
start()
print("--- %s seconds ---" % (time.clock() - startTime))
