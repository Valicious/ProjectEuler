# General Usage

import os


def get_res(filename):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dir_path = dir_path + "\\res\\" + filename
    return dir_path


def get_primes(maxvalue):
    print(f"LOG:Loading primes from 1 < p < {maxvalue}")
    prime = [2]
    i = 3
    while i <= maxvalue:
        testlist = []
        for number in prime:
            testlist.append(i % number)
        if 0 not in testlist:
            prime.append(i)
        i = i + 1
    print(f"LOG:Primes loaded successful!")
    return prime
