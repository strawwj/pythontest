import pymongo
conn = pymongo.MongoClient('localhost',27017)
db = conn.hero
collection = db['movice']
collection.find()
db.movice.insert({'title':'asi'})


