#!/usr/bin/env python
# Filename: lambda.py

def make_repeater(n):
    return lambda s: s*n

twice = make_repeater(2)
print twice('world')
print twice(5)

# lambda expression calculation
def func(x, y, z):
    return x + y + z

f = lambda x, y, z: x + y + z

a = func(2, 3, 4)
b = f(2, 3, 4)
print 'a is', a
print 'b is', b

# lambda logical test
lower = (lambda x, y: x if x < y else y)
print lower('bb', 'aa')
print lower(12, 33)
