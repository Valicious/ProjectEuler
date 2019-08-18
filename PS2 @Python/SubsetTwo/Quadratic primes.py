# 27
import time

from __GV__ import get_primes


def start():
    max_ab = [0, 0, 0]
    primesPos = get_primes(1000)
    primesNeg = []
    for item in primesPos:
        primesNeg.append(item * -1)
    primes = primesPos + primesNeg + [1, -1]
    primesPos = get_primes(10000)

    for a in primes:
        for b in primes:
            for num in range(500):
                value = num ** 2 + a * num + b
                if value not in primesPos:
                    if value > primesPos[-1]:
                        print(f"{value} too big (>primesPos[-1]) current value at {num}")
                    if num > 10:
                        print(f"{a},{b} @ 0 < n < {num}")
                    if num - 1 > max_ab[2]:
                        max_ab = [a, b, num - 1]
                    break

    print(f"{max_ab[0]}*{max_ab[1]} = {max_ab[0]*max_ab[1]} @ {max_ab[2]}")
    pass


startTime = time.clock()
start()
print("--- %s seconds ---" % (time.clock() - startTime))
