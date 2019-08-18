# 19

import datetime


def start():
    count = 0
    for year in range(1901, 2001):
        for month in range(1, 13):
            uhm = datetime.datetime(year, month, 1)
            if uhm.strftime('%a') == "Sun":
                count += 1
    print(count)
    pass


start()
