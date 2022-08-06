#!/usr/bin/python3
'''This Script lists all states from the database
hbtn_0e_0_usa'''

import MySQLdb
from sys import argv
import re


def mysqlrun():
    """Function for connecting to MySQL database"""
    username, passwd, db_name = argv[1], argv[2], argv[3]
    try:
        db_connection = MySQLdb.connect(
                            host="localhost",
                            port=3306,
                            user=username,
                            passwd=passwd,
                            db=db_name
                            )
    except Exception:
        return (0)
    cur = db_connection.cursor()
    cur.execute("SELECT cities.name FROM cities "
                "LEFT JOIN states ON cities.state_id = states.id "
                "WHERE states.name = {}".format(argv[4])
                "ORDER BY cities.id")
    query = cur.fetchall()
    cities = ["".join(re.findall("[a-zA-Z]", str(row))) for row in query]
    print(", ".join(cities))
    cur.close()
    db_connection.close()


if __name__ == "__main__":
    mysqlrun()