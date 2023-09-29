#!/usr/bin/python3

""" script that takes in arguments and
displays all values in the states
table of hbtn_0e_0_usa where name
matches the argument. But this time,
write one that is safe from MySQL
injections! """
import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(user=argv[1],
                           passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states")

    query_rows = cur.fetchall()
    [print(row) for row in query_rows if row == sys.argv[4]]
    cur.close()
    conn.close()
