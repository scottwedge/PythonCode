#!/usr/bin/env python
# Filename: read_file.py

import sys

if len(sys.argv) < 2:
    print 'Error: required filename as arguments'
    exit(1)
i = 1
while i < len(sys.argv):
    for line in open(sys.argv[i]):
        print line,
    i += 1
