# 20
"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""


def fact(n, total=1):
    while True:
        if n == 1:
            return total
        n, total = n - 1, total * n


def f2s(factorial):
    total = 0
    for charv in str(factorial):
        total += int(charv)
    return total


def start():
    factorial = fact(100)
    factstring = f2s(factorial)
    print(factstring)
    pass


start()
