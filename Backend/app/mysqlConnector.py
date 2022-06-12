import mysql.connector
from mysql.connector import Error


def connect():
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(host='localhost',port='8002', database='receipts', user='root', password='root')
        if conn.is_connected():
            print('Connected to MySQL database')
    except Error as e:
        print(e)
    finally:
        if conn is not None and conn.is_connected():
            return conn


if __name__ == '__main__':
    connect()