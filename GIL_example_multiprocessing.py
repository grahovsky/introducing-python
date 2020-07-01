# multiprocessing
import time
from multiprocessing import Pool

COUNT = 50000000

def countdown(n):
    while n > 0:
        n -= 1

if __name__ == '__main__':
    pool = Pool(processes=2)
    start = time.time()
    r1 = pool.apply_async(countdown, [COUNT // 2])
    r2 = pool.apply_async(countdown, [COUNT // 2])
    pool.close()
    pool.join()
    end = time.time()
    print('Затраченное время в секундах -', end - start)

# Затраченное время в секундах - 2.0909018516540527