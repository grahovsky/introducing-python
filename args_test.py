import sys

print('Program arguments:', sys.argv)

l1 = 'test global'

def func1():
    # global l1
    l1 = 'test local'
    print('local l1', l1)

print('global l1', l1)

func1()

print('global l1', l1)
