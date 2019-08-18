# 22

"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value
by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the
938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""
import time

from __GV__ import get_res


def import_files(param):
    with open(get_res(param)) as names:
        inputs = names.read()
        list_names = inputs.replace('"', "").split(',')
    return list_names


def get_alpha_value(name):
    total = 0
    for charv in name:
        total = total + ord(charv) - 64
    return total


def start():
    total = 0
    list_names = import_files('p022_names.txt')
    list_names.sort(key=str.lower)
    for (pos, name) in enumerate(list_names):
        alpha_sum = get_alpha_value(name)
        total = total + ((pos + 1) * alpha_sum)
        print(f"{name} = ({alpha_sum} @{pos+1}) = {(alpha_sum * pos + 1)}")
    print(total)
    pass


startTime = time.clock()
start()
print("--- %s seconds ---" % (time.clock() - startTime))
