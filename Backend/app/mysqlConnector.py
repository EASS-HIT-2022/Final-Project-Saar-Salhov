import mysql.connector
from mysql.connector import Error


def GetConnection():
    try:
        connection = mysql.connector.connect(host='localhost', port='8002',database='receipts',user='root',password='root')
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        return connection