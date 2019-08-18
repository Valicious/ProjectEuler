# 21

"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
import time


def d(n):
    ldivisors = []
    for num in range(1, n):
        if n % num == 0:
            ldivisors.append(num)
    # print(ldivisors)
    total = 0
    for num in ldivisors:
        total += num
    return total


def start():
    listamicable = []
    for n in range(1, 10001):  # d(n) = dn; d(dn) = val1;
        if n in listamicable:
            continue
        dn = d(n)
        val1 = d(dn)
        if n != dn and n == val1:
            listamicable.append(n)
            listamicable.append(dn)
            print(f"{n} , {dn}")
    total = 0
    for num in listamicable:
        total += num
    print(total)
    pass


startTime = time.clock()
start()
print("--- %s seconds ---" % (time.clock() - startTime))
