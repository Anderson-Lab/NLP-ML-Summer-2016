from pymongo import MongoClient
import json
from textblob import TextBlob
from nltk import *
from collections import Counter
from math import *


''' Connect to the database'''
client = MongoClient()
db = client.yelp

'''Get the number of reviews per Business ID'''
def count_reviews():
    d = db.reviews.find({})
    ids = []
    count = 1
    for n in d:
        item = n['business_id']
        ids.append(item)
        print (Counter(ids))

'''Retrieve data based on the business_id'''
def search_by_business(id):
    return db.reviews.find({'business_id': id})

'''Perform sentiment analysis based on number of stars'''
def sentiment_analysis(stars):
    review = db.reviews.find({'stars': stars})
    scores = []
    counter = 0
    for item in review:
        counter +=1
        blob = TextBlob(item['text'])
        blob.tags
        blob.noun_phrases
        total_score = 0
        for sentence in blob.sentences:
            total_score += sentence.sentiment.polarity
            scores.append(total_score)
        if counter == 10:
            break
    return scores

''' Open file and write the sentiment scores of reviews line by line'''
def collect_data (file, scores):
    file = open(file, 'a')
    file.write(str(scores) + '\n')
    file.close()

''' Open file and write the sentiment scores of reviews line by line'''
def write_scores (score, stars):
    result = db.sentiments.insert_one(
        {
            "Sentimets": {
                "stars": stars,
                "score": score
            }
        }
        )

''' Calculate the mean score from data base'''
def mean_score (scores):
    counter = 0
    score = 0
    for item in scores:
        score += item
        counter += 1
    collect_data('5star.txt', score/counter)
    return score/counter

'''Calculate mean score from file reading line by line'''
def mean_score_file (file):
    counter = 0
    score = 0
    file = open (file, 'r')
    for line in file:
        score += float(line)
        counter += 1
    file.close()
    return score/counter

'''Calculate Standard Deviation'''
def standard_deviation (file, mean):
    file = open(file, 'r')
    difference = 0
    counter = 0
    for line in file:
        difference += (float(line) - mean)**2
        counter +=1
    return sqrt(abs(difference/counter))
    

''' Returns reviews containing the given word '''
def find_reviews (word):
    reviews = db.reviews.find({})
    for item in reviews:
        if word in item['text']:
            print (item['text'])


''' Construct 99% Confidence Interval'''
def ninety_nine_confidence (mean, standard_deviation, sample, value):
    standard_error = standard_deviation/sqrt(sample)
    critical_value = 2.575
    margin_of_error = critical_value * standard_error
    if value <= mean + margin_of_error and value >= margin_of_error:
        print ("With 99% Confidence, it is a 5 star review")
    else:
        print ("With 99% Confidence, it is not a 5 star review")

''' Construct 98% Confidence Interval'''
def ninety_nine_confidence (mean, standard_deviation, sample, value):
    standard_error = standard_deviation/sqrt(sample)
    critical_value = 2.575
    margin_of_error = critical_value * standard_error
    if value <= mean + margin_of_error and value >= margin_of_error:
        print ("With 99% Confidence, it is a 5 star review")
    else:
        print ("With 99% Confidence, it is not a 5 star review")


''' Construct 95% Confidence Interval'''
def ninety_five_confidence (mean, standard_deviation, sample, value):
    standard_error = standard_deviation/sqrt(sample)
    critical_value = 1.96
    margin_of_error = critical_value * standard_error
    if value <= mean + margin_of_error and value >= margin_of_error:
        print ("With 95% Confidence, it is a 5 star review")
    else:
        print ("With 95% Confidence, it is not a 5 star review")


    

def create_training (file):
    file = open(file, 'r')
    counter = 0
    for line in file:
        counter +=1
    train_number = counter * 0.9




scores = sentiment_analysis(5)
for score in scores:
    write_scores(score, '5')
cursor = db.sentiments.find()
for line in cursor:
    print(line)




##def main():
##    print(sentiment_analysis(5))

    
    

#find_reviews('shrimp and grits')
 
#print(standard_deviation(('5star.txt'), mean_score_file('5star.txt')))



    
        
        

##print(mean_score(sentiment_analysis(1)))




##d = search_by_business('2SwC8wqpZC4B9iFVTgYT9A')
##
##counter = 0
##for n in d:
##    print(n)
##    counter += 1
##    if counter == 100:
##        break
##print (counter)

