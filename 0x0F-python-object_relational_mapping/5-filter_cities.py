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
    state = argv[4]
    cur = db_connection.cursor()
    query_1 = """SELECT cities.name FROM cities
                INNER JOIN states ON cities.state_id = states.id
                WHERE states.name=%s
                ORDER BY cities.id"""
    cur.execute(query_1, (state,))
    query = cur.fetchall()
    cities = ["".join(re.findall("[a-zA-Z0-9]", str(row))) for row in query]
    print(", ".join(cities))
    cur.close()
    db_connection.close()


if __name__ == "__main__":
    mysqlrun()
