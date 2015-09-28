#!/usr/bin/env python
# Filename: pattern_print.py

import sys

if len(sys.argv) < 3:
    print 'No file chosen.'
    exit()

prog = sys.argv[0]
pattern = sys.argv[1]
for filename in sys.argv[2:]:
    found = [lines for lines in open(filename) if lines.find(pattern) != -1]
    for line in found:
        print line,
