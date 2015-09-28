#!/usr/bin/env python
# Filename: classMathod.py

class Person:
    def sayHi(self):
        print 'Hi, how are you?'

p = Person()
p.sayHi()   # also can't be written as Person().sayHi()
