# multi_threaded.py
import time
from threading import Thread

COUNT = 50000000

def countdown(n):
    while n > 0:
        n -= 1

# single thread
start = time.time()
countdown(COUNT)
end = time.time()

print('Затраченное время в секундах -', end - start)
# Затраченное время в секундах - 3.9776179790496826

# multithreading

COUNT = 50000000

t1 = Thread(target=countdown, args=(COUNT//2,))
t2 = Thread(target=countdown, args=(COUNT//2,))

start = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()

print('Затраченное время в секундах -', end - start)
# Затраченное время в секундах - 4.190810203552246

# use multiprocessing -> GIL_example_multithreading.py
