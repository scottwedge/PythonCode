#!/usr/bin/env python
# Filename: using_sys.py

import sys

print 'The command line arguments are:'
for i in sys.argv:
    print i
print 'Print command line arguments with while loop:'
j = 0
while j < len(sys.argv):
    print sys.argv[j]
    j = j + 1

print '\n\nThe PYTHONPATH is', sys.path, '\n'
