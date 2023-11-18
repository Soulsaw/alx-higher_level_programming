#!/usr/bin/python3
"""This is the MySQLdb implementation
"""
if __name__ == '__main__':
    import sys
    import MySQLdb

    dhost = 'localhost'
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    db = MySQLdb.connect(host=dhost, port=3306, user=username, passwd=password, db=dbname)
    cur = db.cursor()
    param = sys.argv[4]
    cur.execute("SELECT * FROM states WHERE name = %s", (param,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
