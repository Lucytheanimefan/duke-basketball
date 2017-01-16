from pymongo import MongoClient

def get_db():
    client = MongoClient('TODO')
    db = client.heroku_#TODO
    return db