import time

def snooze():
    time.sleep(1)

class TimeContextManager:
    def __enter__(self):
        self.t1 = time.time()
        return self
    def __exit__(self, type, value, traceback):
        t2 = time.time()
        print(f"{(t2-self.t1):.4f}")


with TimeContextManager():
    snooze()