import multiprocessing
from random import randint
import time
import datetime

def random_process():
    seconds = randint(0, 5)
    time.sleep(seconds)
    print(datetime.datetime.now().time())


if __name__=="__main__":
    for n in range(3):
        p = multiprocessing.Process(target=random_process)
        p.start()