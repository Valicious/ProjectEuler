# 33
import time


class Container(object):
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d


def concat(a, b):
    return int(f"{a}{b}")


def semiBruteForce():
    arr = []
    for a in range(1, 10):
        for c in range(1, 10):
            if a == c:
                continue
            for b in range(1, 10):
                if concat(a, b) / concat(c, b) == a / c and a / c < 1:
                    arr.append(Container(a, b, c, b))
                elif concat(a, b) / concat(b, c) == a / c and a / c < 1:
                    arr.append(Container(a, b, b, c))
                elif concat(b, a) / concat(c, b) == a / c and a / c < 1:
                    arr.append(Container(b, a, c, b))
                elif concat(b, a) / concat(b, c) == a / c and a / c < 1:
                    arr.append(Container(b, a, b, c))
    prod = 1
    for elm in arr:
        val = concat(elm.a, elm.b) / concat(elm.c, elm.d)
        prod *= val

        print(f"a={elm.a} b={elm.b} c={elm.c} d={elm.d}")
        print(f"{elm.a}{elm.b}/{elm.c}{elm.d}")
        print("\n")

    print(prod)
    pass


def start():
    semiBruteForce()
    pass


startTime = time.time()
start()
print("--- %s seconds ---" % (time.time() - startTime))
