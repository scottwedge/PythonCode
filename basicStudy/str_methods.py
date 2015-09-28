#!/usr/bin/env python
# Filename: str_methods.py

name = 'Swaroop'    # This is a string object

if name.startswith('Swa'):
    print 'Yes, the string starts with "Swa"'

if 'a' in name:
    print 'Yes, it contains a string "a"'

if name.find('war') != -1:
    print 'Yes, it contains the string "war"'

name_replace = name.replace('a', 'aa')
print 'Replace "a" as "aa" in the string', name_replace

newline = 'zhuzhu\n'
del_newline = newline.rstrip()
print del_newline

delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print delimiter.join(mylist)

num = '123'
print num.isdigit()

string = 'absckk'
print string.isalpha()

alnum = '123sss'
print alnum.isalnum()
