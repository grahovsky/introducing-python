import time

def snooze():
    time.sleep(1)

def time_decorator(func):
    def inner(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print(f"{(t2-t1):.4f}")
        return result
    return inner

@time_decorator
def naptime():
    snooze()

naptime()