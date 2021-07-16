import pymongo
from pymongo import MongoClient


class db:
    def __init__(self, query, coll_name):
        self.query = query
        self.coll_name = coll_name

    def db_connection(self):
        connection_string = "mongodb+srv://Bhupesh:1234@cluster0.7at15.mongodb.net/eCommerce_Project?retryWrites=true&w" \
                            "=majority"
        my_client = pymongo.MongoClient(connection_string)
        dblist = my_client.list_database_names()
        db = my_client["eCommerce_Project"]  # database
        coll = db["users"]  # collection

    def insertData(query, collection):
        c_db = db(query, collection)
        coll = c_db.constructDb()
        c_db.insertsToDb(db, coll, query)

    def fetchData(collection, query):
        c_db = db(query, collection)
        coll = c_db.constructDb()
        res = c_db.fetchInfo(db, coll, query)
        return res
