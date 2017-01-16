from pymongo import MongoClient

def get_db():
    client = MongoClient('mongodb://heroku_cst6h6w4:60vdukdm4lt2k26gtb2ssf28ib@ds133358.mlab.com:33358/heroku_cst6h6w4')
    db = client.heroku_cst6h6w4
    return db