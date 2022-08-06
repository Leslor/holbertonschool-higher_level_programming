#!/usr/bin/python3
'''This Script lists all states from the database
hbtn_0e_0_usa'''


if __name__ == "__main__":
   """ Connect to the DB and execute a query"""
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

        cur = db_connection.cursor()
        cur.execute("SELECT * FROM states ORDER BY id")
        query = cur.fetchall()
        for row in query:
            print(row)
        cur.close()
        db_connection.close()
    mysqlrun()
