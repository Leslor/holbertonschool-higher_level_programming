#!/usr/bin/python3
'''This Script lists all states from the database
hbtn_0e_0_usa'''

import MySQLdb
from sys import argv


def mysqlrun():
    """Function for connecting to MySQL database"""
    username, passwd, db_name = argv[1], argv[2], argv[3]
    db_connection = MySQLdb.connect(
                        host="localhost",
                        port=3306,
                        user=username,
                        passwd=passwd,
                        db=db_name
                        )
    state = argv[4]
    cur = db_connection.cursor()
    query_1 = """SELECT * FROM states
                WHERE name=%s
                ORDER BY id"""
    cur.execute(query_1, (state,))
    query = cur.fetchall()
    for row in query:
        print(row)
    cur.close()
    db_connection.close()


if __name__ == "__main__":
    mysqlrun()
