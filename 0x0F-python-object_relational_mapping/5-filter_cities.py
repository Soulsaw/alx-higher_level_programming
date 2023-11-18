#!/usr/bin/python3
"""This is the MySQLdb implementation
"""
if __name__ == '__main__':
    import sys
    import MySQLdb

    if (len(sys.argv) == 5):
        dhost = 'localhost'
        username = sys.argv[1]
        password = sys.argv[2]
        dbname = sys.argv[3]
        db = MySQLdb.connect(host=dhost, port=3306, user=username,
                             passwd=password, db=dbname)
        cur = db.cursor()
        param = sys.argv[4]
        query = "SELECT cities.name FROM cities, states WHERE \
                    cities.state_id = states.id AND states.name = %s"
        cur.execute(query, (param,))
        rows = cur.fetchall()
        size = len(rows)
        for row in range(size):
            print("{}{}".format(rows[row][0], ', '
                                if row < size - 1 else ''), end='')
        print()
        cur.close()
        db.close()
