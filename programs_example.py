import os

print(os.getpid())
print(os.getcwd())

# print(os.getuid())
# print(os.getgid())

# create a process with subpocess
import subprocess

ret = subprocess.getoutput('dir')
print(ret)

# in linux

# ret = subprocess.getoutput('date -u')
# variant method called check_output() takes a list of the command and arguments
# ret = subprocess.check_output(['date', '-u'])


# If you don’t want to capture the output but might want to know its exit status, use call():
# ret = subprocess.call('date')