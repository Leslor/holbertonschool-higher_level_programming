#!/usr/bin/python3
'''This Script lists all states from the database
hbtn_0e_0_usa'''

import MySQLdb
from sys import argv


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
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities "
                "LEFT JOIN states ON cities.state_id = states.id "
                "ORDER BY id")
    query = cur.fetchall()
    for row in query:
        print(row)
    cur.close()
    db_connection.close()


if __name__ == "__main__":
    mysqlrun()
