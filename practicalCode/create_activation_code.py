#!/usr/bin/env python

import random, string

def rand_str(num, length = 8):
    # In python 2.x, using the follow:
    # chars = string.letters + string.digits
    chars = string.ascii_letters + string.digits
    f = open('activation_code.txt', 'wb')
    for i in range(num):
        s = [random.choice(chars) for j in range(length)]
        # str should call the encode function when write to file since using the python 3.x
        # ref: http://stackoverflow.com/questions/5471158/typeerror-str-does-not-support-the-buffer-interface
        f.write((''.join(s) + '\r\n').encode())
    f.close()
    print('Finished!')

if __name__ == '__main__':
    rand_str(200)
