
# coding: utf-8

# In[1]:

import requests
from pymongo import MongoClient
import json


# In[18]:

#YelpPymongo.py 
from pymongo import MongoClient

#This lets pymongo about the connection we want to use, local host in our case
client = MongoClient()

#Setting context to new yelp database 
db = client.yelp

d = db.reviews.find({'business_id': 'LM71VvmoAWDD5z8h7XoVig'})
counter = 0
for n in d:
    #print(n)
    counter += 1
    #if counter == 100:
        #break
    


# In[8]:

#YelpPymongo.py 
from pymongo import MongoClient

#This lets pymongo about the connection we want to use, local host in our case
client = MongoClient()

#Setting context to new yelp database 
db = client.yelp

d = db.reviews.find({'business_id': 'LM71VvmoAWDD5z8h7XoVig'})


# In[19]:

counter


# In[20]:

#Setting context to new yelp database 
db = client.yelp
d = db.reviews.find({'business_id': 'LM71VvmoAWDD5z8h7XoVig'})


# In[26]:

import nltk
from nltk.corpus import stopwords
for i in range(counter):
    text = d[i]['text']
    allWords = nltk.tokenize.word_tokenize(text)
    stopwords = nltk.corpus.stopwords.words('english')
    allWordExceptPunc = [w for w in allWords if w.isalpha()]
    allWordExceptPuncStop = [w for w in allWordExceptPunc if w not in stopwords]
    tempAllWordExceptPuncStopDist = nltk.FreqDist(w.lower() for w in allWordExceptPuncStop)
    if i != 0: 
        allWordExceptPuncStopDist = allWordExceptPuncStopDist + tempAllWordExceptPuncStopDist
    else:
        allWordExceptPuncStopDist = tempAllWordExceptPuncStopDist


# In[27]:

allWordExceptPuncStopDist


# In[28]:
#most common words
most_common = allWordExceptPuncStopDist.most_common(10)
print(most_common)


