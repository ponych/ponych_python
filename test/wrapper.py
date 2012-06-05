#wrapper.py

from time import ctime, sleep

def tsfunc(func):
    def wrapperedFunc():
        print "[%s] %s() called" % (ctime(), func.__name__)
        return func()
    return wrapperedFunc


@tsfunc
def foo():
    pass


foo()

sleep(1)

foo()

for i in range(2):
    sleep(2)
    foo()