import pymongo

client = pymongo.MongoClient("mongodb+srv://NIKHIL:chnr1997@nikhil.qbvhu.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
d = {
    "name" : "Nikhil",
    "surname" : "chalamalla"
}
db1 = client['mongotest']
c = db1['test']
c.insert_one(d)