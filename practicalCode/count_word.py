#!/usr/bin/env python

import re

def count_words(filename):
    f = open(filename, 'r')
    word_list = {}
    lines = f.readlines()
    for line in lines:
        line = re.sub('[^a-zA-Z]', ' ', line)
        words = line.split(' ')
        for word in words:
            if word == '':
                continue
            if word in word_list:
                word_list[word] += 1
            else:
                word_list[word] = 1

    return word_list

if __name__ == '__main__':
    filename = input('Input filename: ')
    word_list = count_words(filename)
    print(word_list)
