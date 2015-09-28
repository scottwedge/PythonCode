#!/usr/bin/env python
# Filename: ls.py
def ls():
    """This function used to list the file name"""
    import os
    import sys
    # path = os.getcwd()
    path = sys.argv[1]
    filelist = os.listdir(path)
    filelist.sort()

    col = 5
    raw = len(filelist) / col
    length = len(filelist)

    for i in range(raw):
        j = i
        while (j < length):
            print '%-23s' % filelist[j],
            j = j + raw
        print

ls()
