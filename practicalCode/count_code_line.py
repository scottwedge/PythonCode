#!/usr/bin/env python

import os
import sys
from collections import Counter

def lineType(line):
    line = line.strip()
    if len(line) == 0:
        return 0
    elif line[0] == '#':
        return 1
    else:
        return 2

def count_code_line(directory):
    statics = {
        'code'      : 0,
        'empty'     : 0,
        'comment'   : 0
    }

    if os.path.exists(directory):
        os.chdir(directory)
        all_files = os.listdir(os.getcwd())

        for i in all_files:
            if os.path.splitext(i)[1] == '.py':
                with open(i, 'r') as f:
                    for line in f.readlines():
                        if lineType(line) == 0:
                            statics['empty'] += 1
                        elif lineType(line) == 1:
                            statics['comment'] += 1
                        else:
                            statics['code'] += 1
    else:
        print directory, ' is not exist.'

    return statics

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage: '
        print '\tpython ', sys.argv[0], ' directory'
    else:
        statics = count_code_line(sys.argv[1])
        for key in statics:
            print key, ' => ', statics[key]
