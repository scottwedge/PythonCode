#!/usr/bin/env python

'''
Move .jpg file to JPG diretory on windows
'''

import os

cwd = os.listdir()
for item in os.listdir():
    if os.path.splitext(item)[1] == '.jpg':
        os.rename(cwd + '\\' + item, cwd + '\\JPG\\' + item)

