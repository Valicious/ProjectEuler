# 31
import time


def start():
    value = 200
    count = 0
    for h in range(2):
        for g in range(3):
            for f in range(5):
                for e in range(11):
                    print(f"({h},{g},{f},{e}) @ {count}   (1,2,4,10) ")
                    for d in range(21):
                        for c in range(41):
                            for b in range(101):
                                for a in range(201):
                                    newVal = 1 * a + 2 * b + 5 * c + 10 * d + 20 * e + 50 * f + 100 * g + 200 * h
                                    if newVal == value:
                                        # print(f"{a} {b} {c} {d} {e} {f} {g} {h}")
                                        count += 1
                                    if newVal > value:
                                        break
    print(count)


startTime = time.clock()
start()
print("--- %s seconds ---" % (time.clock() - startTime))
