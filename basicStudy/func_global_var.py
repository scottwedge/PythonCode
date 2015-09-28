#!/usr/bin/env python
# Filename: func_local_var.py

def func():
    global x
    print 'x is', x
    x = x + 1
    print 'change local x to', x

x = 32
func()
print 'Value of x is', x
