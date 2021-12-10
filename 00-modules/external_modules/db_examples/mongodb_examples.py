from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client.test_database
# db = client['test-database']
collection = db.test_collection


# insert
import datetime
post = {
        "author": "Can",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()
        }

post_id = db.posts.insert_one(post).inserted_id

# bulk insert
new_posts = [
    {
        "author": "Can2",
        "text": "Another post!",
        "tags": ["bulk", "insert"],
        "date": datetime.datetime(2009, 11, 12, 11, 14)},
    {
        "author": "Can3",
        "title": "MongoDB is fun",
        "text": "and pretty easy too!",
        "date": datetime.datetime(2009, 11, 10, 10, 45)
    }
        ]
result = db.posts.insert_many(new_posts)



print(db.list_collection_names())

# get
import pprint
pprint.pprint(db.posts.find_one({"author": "Can"}))

# get by objectid, does not works with only string id
from bson.objectid import ObjectId
pprint.pprint(db.posts.find_one({"_id": ObjectId('61b3910923a389666e51ba16')}))
def get(post_id):
    # Convert from string to ObjectId:
    return client.db.collection.find_one({'_id': ObjectId(post_id)})

# get all
for post in db.posts.find():
    pprint.pprint(post)

# get all with query
for post in db.posts.find({"author": "Can"}):
  pprint.pprint(post)


# counting
print(db.posts.count_documents({}))
print(db.posts.count_documents({"author": "Can"}))


# range
d = datetime.datetime(2009, 11, 12, 12)
for post in db.posts.find({"date": {"$lt": d}}).sort("author"):
    pprint.pprint(post)


# indexing and duplicate prevention
import pymongo
result = db.profiles.create_index([('user_id', pymongo.ASCENDING)], unique=True)
sorted(list(db.profiles.index_information()))

user_profiles = [
    {'user_id': 211, 'name': 'Can'},
    {'user_id': 212, 'name': 'Test'}]
result = db.profiles.insert_many(user_profiles)

duplicate_profile = {'user_id': 212, 'name': 'Tommy'}
result = db.profiles.insert_one(duplicate_profile)


