import pymongo
client = pymongo.MongoClient("mongodb+srv://anildhiman31:Akd!23456@anil.27wwn.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {"name" : "Anil","mailid":"akd@gmail.com","surname":"Kumar"}

db1 = client['momgotest']
coll = db1['test']
coll.insert_one(d)
