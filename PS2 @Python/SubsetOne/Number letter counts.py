# 17
"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out
in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of
"and" when writing out numbers is in compliance with British usage.
"""

numSizeDic = {
    0: 0,   #4,
    1: 3,
    2: 3,
    3: 5,
    4: 4,
    5: 4,
    6: 3,
    7: 5,
    8: 5,
    9: 4,
    10: 3,
    11: 6,
    12: 6,
    13: 8,
    14: 8,
    15: 7,
    16: 7,
    17: 9,
    18: 8,
    19: 8,
    20: 6,
    30: 6,
    40: 5,
    50: 5,
    60: 5,
    70: 7,
    80: 6,
    90: 6,
    100: 7,
    1000: 8
}


def count(num):
    total = 0
    if num < 20:
        total = numSizeDic[num]
    elif num < 100:
        total = numSizeDic[(num // 10) * 10]  # 53 => 50
        total += numSizeDic[num % 10]  # 53 => 3
    elif num < 1000:
        total = numSizeDic[num // 100]  # 536 => 500 = 5
        total += numSizeDic[100]
        if num % 100 != 0:
            total += 3
            total += count(num % 100)  # 536 => 36 --recursive call
    else:
        total = numSizeDic[num // 1000]
        total += numSizeDic[1000]
    return total


def start():
    total = 0
    for num in range(1, 1001):
        total += count(num)
    print(total)


start()
