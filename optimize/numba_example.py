import math
from timeit import timeit
from numba import jit

def hypot(a, b):
    return math.sqrt(a**2 + b**2)

print("Normal python function")
print(timeit('hypot(5, 6)', globals=globals()))
print(timeit('hypot(5, 6)', globals=globals()))

@jit
def hypot_jit(a, b):
    return math.sqrt(a**2 + b**2)

print("The @jit")
print(timeit('hypot_jit(5, 6)', globals=globals()))
print(timeit('hypot_jit(5, 6)', globals=globals()))

print("The @jit(nopython=True)")
@jit(nopython=True)
def hypot_jit_nopy(a, b):
    return math.sqrt(a**2 + b**2)

print(timeit('hypot_jit_nopy(5, 6)', globals=globals()))
print(timeit('hypot_jit_nopy(5, 6)', globals=globals()))