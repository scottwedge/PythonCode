#!/usr/bin/env python
# Filename: func_doc.py

def printMax(x, y):
    '''Prints the maximum of two numbers.

    The two values must be integers.'''
    x = int(x)  # converts to integer, if posiible
    y = int(y)

    if x >= y:
        print x, 'is maximum'
    else:
        print y, 'is maximum'

printMax(3, 6)
print printMax.__doc__

# help(printMax)