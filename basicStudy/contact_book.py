#!/usr/bin/env python
# Filename: contact_book.py

import sys

class Person:
    def __init__(self, name, types, phone, mailAddr):
        self.name = name
        self.types = types
        self.phone = phone
        self.mailAddr = mailAddr

my_contact_book = {}

def quit():
    sys.exit()

def add():
    global my_contact_book
    print 'Input new contact info'
    name = raw_input('Name: ')
    types = raw_input('Types: ')
    phone = raw_input('Phone: ')
    mailAddr = raw_input('E-mail address: ')
    new_contact = Person(name, types, phone, mailAddr)
    my_contact_book[new_contact.name] = new_contact

def change():
    global my_contact_book
    print '1 for types, 2 for phone, 3 for e-mail address'
    op = raw_input('Select what to change: ')
    name = raw_input('Input name: ')
    new_info = raw_input('Input new info: ')
    if op == '1':
        my_contact_book[name].types = new_info
    elif op == '2':
        my_contact_book[name].phone = new_info
    elif op == '3':
        my_contact_book[name].mailAddr = new_info
    else:
        print 'Unkown action.'

def delete():
    global my_contact_book
    name = raw_input('Input name that you want to delete: ')
    try:
        del my_contact_book[name]
    except:
        print 'Delete Error.'
    else:
        print 'Delete successfully.'

def search():
    global my_contact_book
    name = raw_input('Input searching name: ')
    if name in my_contact_book:
        print 'Name: "%s", Types: "%s", Phone: "%s"' % \
        (name, my_contact_book[name].types, my_contact_book[name].phone)
        print 'E-mail address: "%s"' % my_contact_book[name].mailAddr

def print_contact():
    global my_contact_book
    print 'contact Book\n'
    for name in my_contact_book:
        print 'Name: "%s", Types: "%s", Phone: "%s"' % \
        (name, my_contact_book[name].types, my_contact_book[name].phone)
        print 'E-mail address: "%s"' % my_contact_book[name].mailAddr
        print   # print an empty line
    

def select_operator():
    op = raw_input('Select an operator: ')
    if op == '0':
        quit()
    elif op == '1':
        add();
    elif op == '2':
        change();
    elif op == '3':
        delete()
    elif op == '4':
        search()
    elif op == '5':
        print_contact()
    else:
        print 'Unkown operator.'

# script starts here
print '0 for quit, 1 for add contact, 2 for change info,'
print '3 for delete contact, 4 for search contact, 5 for print.'
while True:
    select_operator()
