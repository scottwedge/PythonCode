#!/usr/bin/env python
# Filename: continue.py

while True:
    s = input('Enter something: ')
    s = str(s)
    if s == 'quit':
        break
    if len(s) < 5:
        continue
    print('Length of suficient string')
