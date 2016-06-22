#YelpPymongo.py 


from pymongo import MongoClient


#This lets pymongo about the connection we want to use, local host in our case
client = MongoClient()


#Setting context to new yelp database 
db = client.yelp

d = db.reviews.find({'business_id': 'LM71VvmoAWDD5z8h7XoVig'})
counter = 0
for n in d:
    print(n)
    counter += 1
    if counter == 100:
        break
    
