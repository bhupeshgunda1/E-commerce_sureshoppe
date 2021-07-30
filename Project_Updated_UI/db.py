import pymongo
from pymongo import MongoClient


class db:
        def db_connection(self):
            connection_string = "mongodb+srv://Bhupesh:1234@cluster0.7at15.mongodb.net/eCommerce_Project?retryWrites=true&w" \
                            "=majority"
            my_client = pymongo.MongoClient(connection_string)
            db = my_client["eCommerce_Project"]
            return db


