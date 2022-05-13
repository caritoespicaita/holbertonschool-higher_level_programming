#!/usr/bin/python3
"""takes in the name of a state as an argument and lists all cities"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute('SELECT c.name FROM states AS s INNER JOIN cities AS c ON\
    c.state_id = s.id WHERE s.name = %(fil)s\
    ORDER BY c.id', {'fil': sys.argv[4]})
    rows = cur.fetchall()
    print(', '.join([fila[0] for fila in rows]))
    