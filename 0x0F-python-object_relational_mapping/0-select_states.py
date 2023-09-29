#!/usr/bin/python3
"""  a python script that connects to an sql server
importing MySQLdb and sys module """

import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM `states`")
    [print(state) for state in cur.fetchall()]
    cur.close()
    db.close()
