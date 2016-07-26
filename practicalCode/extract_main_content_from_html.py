#!/usr/bin/env python

import re
import sys

html_tag_start = r'<html>'
html_tag_end   = r'</html>'


def extract(html):
    pass

if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as f:
            html = f.readlines()
            main_content = extract(html)
            print main_content
    else:
        print 'Usage: python ', sys.argv[0], ' <filename>'
