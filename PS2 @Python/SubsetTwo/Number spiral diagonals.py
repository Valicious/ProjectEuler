# 28

"""
NOTE!
    Let M = 5x5 spiral
    let M have 4 diagonals:
        TL, TR, BL, BR
        where TL goes from Top Left to Mid ... respective for TR, BL, BR
    We get
        TL = 1,7,21
        TR = 1,9,25
        BL = 1,5,17
        BR = 1,3,13
    By inspection we see the the difference between each element is non constant but the second difference is:
        TL: 6,14 => 14 - 6 = 8
        TR: 8,16 => 16 - 8 = 8
        BL: 4,12 => 12 - 4 = 8
        BR: 2,10 => 10 - 2 = 8
    Thus we have a quadratic sequence:
         T(n) = a + (n - 1) * d + (1 / 2)(n - 1)(n - 2) * c
    Thus using an initial 3x3 spiral we have 6,8,4,2 as starting values and can
        then add multiples of 8 for each NxN matrix
            where N is uneven and >= 3
"""
from math import floor

import time


def start():
    spiralDim = 1001
    initValue = 1
    iterations = floor((spiralDim - 3) / 2) + 2 + 1
    TL = 0
    for n in range(2, iterations):
        TL += 1 + (n - 1) * 6 + (1 / 2) * (n - 1) * (n - 2) * 8
    TR = 0
    for n in range(2, iterations):
        TR += 1 + (n - 1) * 8 + (1 / 2) * (n - 1) * (n - 2) * 8
    BL = 0
    for n in range(2, iterations):
        BL += 1 + (n - 1) * 4 + (1 / 2) * (n - 1) * (n - 2) * 8
    BR = 0
    for n in range(2, iterations):
        BR += 1 + (n - 1) * 2 + (1 / 2) * (n - 1) * (n - 2) * 8
    print(f"The sum of the numbers on the diagonals is {initValue +TL +TR +BL +BR} :: {TL} ,{TR} ,{BL} ,{BR}")
    pass


startTime = time.clock()
start()
print("--- %s seconds ---" % (time.clock() - startTime))
