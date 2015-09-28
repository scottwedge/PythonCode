#!/usr/bin/env python
# Filename: using_tuple.py

zoo = ('wolf', 'elephant', 'monkey', 'penguin')
print 'Number of animals in the zoo is', len(zoo)

new_zoo = ('dolphin', 'tiger', zoo)
print 'Number of animals in the new zoo is', len(new_zoo)
print 'All animals in the new zoo are', new_zoo
print 'Animals brought from old zoo are', new_zoo[2]
print 'Last animals brought from old zoo is', new_zoo[2][3]

# single element tuple
age = (12, )
# integer assignment
age_ = (12)
# see type
print type(age)
print type(age_)
