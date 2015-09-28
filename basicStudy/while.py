#!/usr/bin/env python
# Filename: while.py

number = 22
running = True
while running:
    guess = int(raw_input('Enter an integer: '))

    if guess == number:
        print 'Congratulation, you guessed it.'
        running = False
    elif guess < number:
        print 'No, it is a little higher than that'
    else:
        print 'No, it is a little lower than that'
else:
    print 'The while loop is over'

print 'Done'
