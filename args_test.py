"test argument pass"
import sys

print('Program arguments:', sys.argv)

VARIABLE = 'test global'

def func1():
    "test local variable"
    # global l1
    VARIABLE = 'test local'
    print('local VARIABLE', VARIABLE)

print('global VARIABLE', VARIABLE)

func1()

print('global VARIABLE', VARIABLE)

# check with 'pylint args_test.py'
