#!/usr/bin/env python
# Filename: func_local_var.py

def func(x):
    print 'x is', x
    x = x + 1
    print 'change local x to', x

x = 32
func(x)
print 'x is still', x
