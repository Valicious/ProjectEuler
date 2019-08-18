# 24
"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits
1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
import math

import time


def find(listDigits, pos):
    def getMod(position, i, iteration):
        if i > 0:
            for num in range(i):
                if num >= iteration:
                    break
                fact = math.factorial(iteration - num - 1)
                position = position % fact
        return position

    digits = []
    ogSize = len(listDigits)
    for i in range(0, ogSize):
        curIteration = len(listDigits) - 1
        numerator = getMod(pos, i, ogSize)
        element = math.floor(numerator / math.factorial(curIteration))
        digits.append(listDigits[element])
        listDigits.remove(listDigits[element])
    return digits


def start():
    listDigits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    pos = 1000000-1
    # listDigits = [1, 2, 3, 4]
    # pos = 23
    element = find(listDigits, pos)
    print(element)
    pass


startTime = time.clock()
start()
print("--- %s seconds ---" % (time.clock() - startTime))

'''
digits = []
curIteration = len(listDigits) - 1
# first digit
iterations = math.factorial(curIteration)
temp = math.floor(pos / iterations)
digits.append(listDigits[temp])  # [0]

# second digit
listDigits.remove(listDigits[temp])
temp = pos % iterations
temp = math.floor(temp / math.factorial(len(listDigits) - 1))
digits.append(listDigits[temp])  # [1]

# third digit
listDigits.remove(listDigits[temp])
temp = round((pos % iterations) % (iterations / curIteration))
digits.append(listDigits[temp])  # [2]

# fourth digit
listDigits.remove(listDigits[temp])
digits.append(listDigits[0])  # [3]
'''
