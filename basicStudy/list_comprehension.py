#!/usr/bin/env python
# Filename: list_comprehension.py

listone = [1, 2, 3, 4]
listtwo = [2*i for i in listone if i > 2]
print 'listone is', listone
print 'listtwo is', listtwo
