import time
import datetime


def time_stamp():
    t = time.time()
    return datetime.datetime.fromtimestamp(t).strftime('%Y%m%d_%H%M%S')
