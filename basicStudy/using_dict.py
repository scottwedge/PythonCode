#!/usr/bin/env python
# Filename: using_dict.py

# 'ab' is short for 'a'ddress'b'ook
ab = {
    'Swaroop'   : 'Swaroopch@byteofpython.info',
    'Larry'     : 'larry@wall.org',
    'Matsumoto' : 'matz@ruby-lang.org',
    'Spammer'   : 'Spammer@hostmail.com'
}
print "Swaroop's address is", ab['Swaroop']

# adding a key/value pair
ab['Guido'] = 'guido@python.org'

# delete a key/value pair
del ab['Spammer']

print '\nThere are %d contacts on the address book\n' % len(ab)
for name, address in ab.items():
    print 'Contact %s at %s' % (name, address)

if 'Guido' in ab:
    print "\nGuido's address is %s" % ab['Guido']

if ab.has_key('Guido'):
    print "\nGuido's address is %s" % ab['Guido']
