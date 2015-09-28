#!/usr/bin/env python
# Filename: exec_eval_and_assert.py

exec('print "hello world!"')
print '2 * 3 + 4 is', eval('2*3+4')

mylist = ['item']
assert(len(mylist) >= 1)
mylist.pop()
try:
    assert(len(mylist) >= 1)
except AssertionError:
    print 'AssertionError was found'
