# 29
import time


def start():
    dim = 100 + 1
    count = 0
    matrix = {}
    for a in range(2, dim):
        removed = 0
        inserted = 0
        for b in range(2, dim):
            val = a ** b
            if val not in matrix:
                matrix[val] = val
                count += 1
                inserted += 1
            else:
                removed += 1
        print(f"{a}: rem({removed}), add({inserted})")
    print(count)


startTime = time.clock()
start()
print("--- %s ---" % (time.clock() - startTime))
