#!/usr/bin/env python
# Filename: seq.py

shoplist = ['apple', 'mango', 'carrot', 'banana']

print 'shoplist contains', shoplist
# Indexing of 'Subscription' operator
print 'Item 0 is', shoplist[0]
print 'Item 1 is', shoplist[1]
print 'Item 2 is', shoplist[2]
print 'Item 3 is', shoplist[3]
print 'Item -1 is', shoplist[-1]
print 'Item -2 is', shoplist[-2]

# Slicing on a list
print 'Item 1 to 3 is', shoplist[1:3]
print 'Item 2 to end is', shoplist[2:]
print 'Item 1 to -1 is', shoplist[1:-1]
print 'Item start to end is', shoplist[:]

# Slicing on a string
name = 'Swaroop'
print 'name contains', name
print 'Character 1 to 3 is', name[1:3]
print 'Character 2 to end is', name[2:]
print 'Character 1 to -1 is', name[1:-1]
print 'Character start to end is', name[:]
