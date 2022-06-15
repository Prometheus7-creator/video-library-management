from pymongo import MongoClient
import pymongo
import urllib

def get_database(dbname, collection_name):

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    from pymongo import MongoClient
    
    client = pymongo.MongoClient("mongodb+srv://ansh:"+urllib.parse.quote('Quit@777')+"@cluster0.klout.mongodb.net/?retryWrites=true&w=majority")
    

    return client[dbname][collection_name]