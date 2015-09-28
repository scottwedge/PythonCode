#!/usr/bin/env python
# Filename: break.py

while True:
    s = raw_input('Enter something: ')

    if s == 'quit':
        break
    print 'Length of', s, 'is', len(s)
print 'Done'
