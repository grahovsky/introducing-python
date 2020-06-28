import pickle
import datetime

now1 = datetime.datetime.utcnow()
print(now1)
pickled = pickle.dumps(now1)

print(pickled)

now2 = pickle.loads(pickled)
print(now2)
