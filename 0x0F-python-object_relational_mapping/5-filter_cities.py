#!/usr/bin/python3
""" script that takes in the name of a
state as an argument and lists all cities
of that state, using the database
hbtn_0e_4_usa """

import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3])

    cur = conn.cursor()

    cur.execute("""SELECT * FROM cities as c
                INNER JOIN states as s ON c.state_id = s.id
                ORDER BY c.id""")

    query_row = cur.fetchall()
    print(", ".join([row[2] for row in query_row if row[4] == sys.argv[4]]))

    cur.close()
    conn.close()
