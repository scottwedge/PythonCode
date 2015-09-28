#!/usr/bin/env python
# Filename: touch.py

filename = raw_input('Enter the name of the file:')
try:
    fp = open(filename, 'w')
except:
    print 'Create File Fail!'
    exit(1)
else:
    print 'Create File Successfully!'

fp.write('Hello file World!\n')
fp.close()
