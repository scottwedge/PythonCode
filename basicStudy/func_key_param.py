#!/usr/bin/env python
# Filename: func_key_param.py

def func(a, b = 5, c = 10):
    print 'a is', a, 'and b is', b, 'and c is', c

func(3, 7)
func(25, c = 24)
func(b = 50, a = 100)
func(c = 50, a = 100)   # func(c = 50, 100) is error
