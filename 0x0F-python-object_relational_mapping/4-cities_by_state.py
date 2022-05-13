#!/usr/bin/python3
""" lists all cities"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute('SELECT c.id, c.name, s.name FROM states AS s INNER JOIN\
    cities AS c ON c.state_id = s.id ORDER BY id'
                )
    rows = cur.fetchall()
    for fila in rows:
        print(fila)
