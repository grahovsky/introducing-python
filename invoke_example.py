# pip install invoke
# One use of invoke is to make functions available as command-line arguments

from invoke import task

@task
def mytime(ctx):
    import time
    now = time.time()
    time_str = time.asctime(time.localtime(now))
    print("Local time is", time_str)


# $ invoke mytime
# Use the argument -l or --list to see what tasks are available:
# $ invoke -l