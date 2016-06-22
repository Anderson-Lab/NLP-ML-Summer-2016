#YelpPymongo.py pymongo


import requests
from pymongo import MongoClient
import json


#This lets pymongo about the connection we want to use, local host in our case
client = MongoClient()


#Setting context to new yelp database 
db = client.yelp

d = db.reviews.find({'business_id': 'ADD HERE'})
counter = 0
for n in d:
    print(n)
    counter += 1
    if counter == 100:
        break
    
