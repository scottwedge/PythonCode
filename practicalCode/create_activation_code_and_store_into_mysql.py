#!/usr/bin/env python

import string, random
import MySQLdb as mysql 

def create_activaton_code(num, length=8):
    codes = []
    chars = string.letters + string.digits
    for i in range(num):
        s = [random.choice(chars) for j in range(length)]
        codes.append(''.join(s))
    return codes

if __name__ == '__main__':
    db = mysql.connect('localhost', 'zhushh', 'zhushuhuang', 'test')
    cursor = db.cursor()

    query = "INSERT INTO activation_code VALUES (%s)"
    codes = create_activaton_code(200)

    try:
        cursor.executemany(query, [(code,) for code in codes])
        db.commit()
    except:
        print 'Error!'
        db.rollback()
    finally:
        db.close()
