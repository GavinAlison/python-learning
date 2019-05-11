import pymongo

'''
pymongo的crud
'''

client = pymongo.MongoClient('localhost', 27017)
db = client.infos
doc = db.student.find_one()
for item in db.student.find():
    print(item)
db.student.find().count()
db.student.find().sort("name")  #默认为升序
db.student.find().sort("name",pymongo.ASCENDING)   #升序
db.student.find().sort("name",pymongo.DESCENDING)  #降序
db.student.insert({"accout":21,"user_name":"xiao"})
db.student.update({"user_name":"xiao"},{"$set":{"email":"jeiker@126.com","password":"123456"}})

#db.student.remove()
db.student.remove({"user_name":"xiao"})

# db = client.infos
client.infos.student.insert(
    {"item": "canvas",
     "qty": 100,
     "tags": ["cotton"],
     "size": {"h": 28, "w": 35.5, "uom": "cm"}})


client.infos.student.insert_many([
    {"item": "journal",
     "qty": 25,
     "tags": ["blank", "red"],
     "size": {"h": 14, "w": 21, "uom": "cm"}},
    {"item": "mat",
     "qty": 85,
     "tags": ["gray"],
     "size": {"h": 27.9, "w": 35.5, "uom": "cm"}},
    {"item": "mousepad",
     "qty": 25,
     "tags": ["gel", "blue"],
     "size": {"h": 19, "w": 22.85, "uom": "cm"}}])



