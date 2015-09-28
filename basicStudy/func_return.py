#!/usr/bin/env python
# Filename: func_return.py

def maximum(x, y):
    if x >= y:
        return x
    else:
        return y

print maximum(2, 3)

x = int(raw_input('Enter an integer: '))
y = int(raw_input('Enter an integer: '))

z = maximum(x, y)
print z
