# encoding=utf-8
__author__ = 'bbogle'

def fib(x):
    """assumes x an int >= 0
       returns Fibonacci of x"""
    assert type(x) == int and x >= 0
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

print fib(0)
print fib(1)
print fib(2)
print fib(3)
print fib(13)
print fib(40)
