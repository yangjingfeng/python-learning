import pymongo
client = pymongo.MongoClient(host='192.168.1.232', port=27017)
post = {
    'auther' : 'Mike',
}
db = client.testdb
collection = db.testcoll
posts = db.posts
posts_id = posts.insert_one(post)

print(db.list_collection_names())
