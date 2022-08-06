#!/usr/bin/python3
'''This Script lists all states from the database
hbtn_0e_0_usa'''

import MySQLdb
from sys import argv


if __name__ == "__main__":
    """Connect to DB and execute query """

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
        cur.execute("SELECT * FROM states WHERE name LIKE %s", [state])
        query = cur.fetchall()
        for row in query:
            print(row)
        cur.close()
        db_connection.close()
