#!/usr/bin/env python
# Filename: objvar.py

class Person:
    """Represents a person"""
    population = 0

    def __init__(self, name):
        """Initializes the person's data"""
        self.name = name

        # when the person is created, she/he
        # adds to population
        Person.population += 1

    def __del__(self):
        """I am dying."""
        print '%s says bye.' % self.name

        Person.population -= 1
        if Person.population == 0:
            print 'I am the last one.'
        else:
            print 'There are still %d people left.' % Person.population

    def sayHi(self):
        """Greeting by the person.

        Really, that is all it does."""
        print 'Hello, my name is %s' % self.name

    def howMany(self):
        """Print the current population."""
        if Person.population == 1:
            print 'I am the only person.'
        else:
            print 'We have %d persons here.' % Person.population

swaroop = Person('Swaroop')
swaroop.sayHi()
swaroop.howMany()

kalam = Person('Abdul kalam')
kalam.sayHi()
kalam.howMany()

swaroop.sayHi()
swaroop.howMany()
