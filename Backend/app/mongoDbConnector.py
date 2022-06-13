from pymongo import MongoClient

def connect():
    # Connect with the portnumber and host
    myclient = MongoClient("mongodb://root:root@dbmongo:27017/?authMechanism=DEFAULT")
    # myclient = MongoClient("mongodb://root:root@localhost:8003/?authMechanism=DEFAULT")

    database = myclient["receipts_db"]
    receipts = database.receipts
    return receipts

if __name__ == '__main__':
    connect()
