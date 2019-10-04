import pymongo

new_client = pymongo.MongoClient('mongodb://localhost:27017')
mydb = new_client['mydatabase']
my_new_collection = mydb['costumers']  # init collection
print(new_client.list_database_names())  # is exist database
print(mydb.list_collection_names())  # is exist collection

# my_new_dict = {'name': 'Mike', 'last_name': 'Stel'}
# x = my_new_collection.insert_one(my_new_dict)  # add 1 record
# print(x.inserted_id)  # return id

my_new_list = [
    {'name': 'Mike', 'last_name': 'Stels'},
    {'name': 'Oleg', 'last_name': 'Steller'},
    {'name': 'Dima', 'last_name': 'Stelin'},
    {'name': 'Alex', 'last_name': 'Stely'},
    {'name': 'Roma', 'last_name': 'Stelpher'},
    {'name': 'Kola', 'last_name': 'Stelaf'},
    {"_id": 777, 'name': 'Kolla', 'last_name': 'Stelaffan'}  # - with given ID
]

# x = my_new_collection.insert_many(my_new_list)  # add many records
# print(x.inserted_ids)  # return ids


# find
x = my_new_collection.find_one()  # first
print(x)

for i in my_new_collection.find().limit(5):  # all , limit - show 5 records
    print(i)

for i in my_new_collection.find({}, {'name': 1}):  # only id and name
    print(i)
new_query = {'name': 'Mike'}
for i in my_new_collection.find(new_query):
    print(i)
new_query = {'Name': {'$gt': 'M'}}  # Find documents where name starts with the letter "M" or higher
new_query2 = {'name': {'$regex': '^A'}}  # Find documents where the name starts with the letter "A":
mydoc = my_new_collection.find().sort('name')  # sort by name; ('name',-1) - decrease

# delete
# my_new_collection.delete_one({'name': 'Oleg'}) - delete 1
# my_new_collection.delete_many({'name', {'$regex': '^A'}}) - delete all names begins 'A'
# my_new_collection.delete_many({}) - delete all
# my_new_collection.drop() - delete collection

# update
myquery = {"name": "alex"}
newvalues = {"$set": {"name": "Alexx"}}
my_new_collection.update_one(myquery, newvalues)  # update one

myquery = {"name": {"$regex": "^M"}}
newvalues = {"$set": {"name": "Mikee"}}
x = my_new_collection.update_many(myquery, newvalues) # update many
print(x.modified_count, "documents updated.")

