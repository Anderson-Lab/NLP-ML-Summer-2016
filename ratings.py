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


'''Perform sentiment analysis based on number of stars. Returns mean score per review'''
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
        scores.append(total_score/counter)
        if counter == 10:
            break
    return scores

''' Open file and write the sentiment scores of reviews line by line'''
def collect_data (file, scores):
    file = open(file, 'a')
    file.write(str(scores) + '\n')
    file.close()

''' Create a 'sentiments' collection and write mean score per review based on number of stars'''
def write_scores (score, stars):
    result = db.sentiments.insert_one(
        {
            "sentiments": {
                "stars": stars,
                "score": score
            }
        }
        )


''' Calculate the mean score from array passed as a parameter'''
def mean_score (scores):
    counter = 0
    score = 0
    for item in scores:
        score += float(item)
        counter += 1
    return score/counter


''' Calculate the mean score from data base'''
def mean_score (stars):
    scores = db.sentiments.find({})
    counter = 0
    total = 0
    for item in scores:
        total += float(item['sentiments']['score'])
        counter += 1
    return total/counter


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

'''Calculate Standard Deviation from DataBase'''
def standard_deviation (mean):
    difference = 0
    counter = 0
    for line in mean:
        difference += (float(line) - mean)**2
        counter +=1
    return sqrt(abs(difference/counter))

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
def ninety_eight_confidence (mean, standard_deviation, sample, value):
    standard_error = standard_deviation/sqrt(sample)
    critical_value = 2.33
    margin_of_error = critical_value * standard_error
    if value <= mean + margin_of_error and value >= margin_of_error:
        print ("With 98% Confidence, it is a 5 star review")
    else:
        print ("With 98% Confidence, it is not a 5 star review")

''' Construct 97% Confidence Interval'''
def ninety_five_confidence (mean, standard_deviation, sample, value):
    standard_error = standard_deviation/sqrt(sample)
    critical_value = 2.17
    margin_of_error = critical_value * standard_error
    if value <= mean + margin_of_error and value >= margin_of_error:
        print ("With 97% Confidence, it is a 5 star review")
    else:
        print ("With 97% Confidence, it is not a 5 star review")


''' Construct 96% Confidence Interval'''
def ninety_five_confidence (mean, standard_deviation, sample, value):
    standard_error = standard_deviation/sqrt(sample)
    critical_value = 2.05
    margin_of_error = critical_value * standard_error
    if value <= mean + margin_of_error and value >= margin_of_error:
        print ("With 96% Confidence, it is a 5 star review")
    else:
        print ("With 96% Confidence, it is not a 5 star review")
        

''' Construct 95% Confidence Interval'''
def ninety_five_confidence (mean, standard_deviation, sample, value):
    standard_error = standard_deviation/sqrt(sample)
    critical_value = 1.96
    margin_of_error = critical_value * standard_error
    if value <= mean + margin_of_error and value >= margin_of_error:
        print ("With 95% Confidence, it is a 5 star review")
    else:
        print ("With 95% Confidence, it is not a 5 star review")


''' Construct 94% Confidence Interval'''
def ninety_five_confidence (mean, standard_deviation, sample, value):
    standard_error = standard_deviation/sqrt(sample)
    critical_value = 1.88
    margin_of_error = critical_value * standard_error
    if value <= mean + margin_of_error and value >= margin_of_error:
        print ("With 94% Confidence, it is a 5 star review")
    else:
        print ("With 94% Confidence, it is not a 5 star review")


''' Construct 93% Confidence Interval'''
def ninety_five_confidence (mean, standard_deviation, sample, value):
    standard_error = standard_deviation/sqrt(sample)
    critical_value = 1.81
    margin_of_error = critical_value * standard_error
    if value <= mean + margin_of_error and value >= margin_of_error:
        print ("With 93% Confidence, it is a 5 star review")
    else:
        print ("With 93% Confidence, it is not a 5 star review")


''' Construct 92% Confidence Interval'''
def ninety_five_confidence (mean, standard_deviation, sample, value):
    standard_error = standard_deviation/sqrt(sample)
    critical_value = 1.75
    margin_of_error = critical_value * standard_error
    if value <= mean + margin_of_error and value >= margin_of_error:
        print ("With 92% Confidence, it is a 5 star review")
    else:
        print ("With 92% Confidence, it is not a 5 star review")


''' Construct 91% Confidence Interval'''
def ninety_five_confidence (mean, standard_deviation, sample, value):
    standard_error = standard_deviation/sqrt(sample)
    critical_value = 1.70
    margin_of_error = critical_value * standard_error
    if value <= mean + margin_of_error and value >= margin_of_error:
        print ("With 91% Confidence, it is a 5 star review")
    else:
        print ("With 91% Confidence, it is not a 5 star review")


''' Construct 90% Confidence Interval'''
def ninety_five_confidence (mean, standard_deviation, sample, value):
    standard_error = standard_deviation/sqrt(sample)
    critical_value = 1.645
    margin_of_error = critical_value * standard_error
    if value <= mean + margin_of_error and value >= margin_of_error:
        print ("With 90% Confidence, it is a 5 star review")
    else:
        print ("With 90% Confidence, it is not a 5 star review")


    

def create_training (file):
    file = open(file, 'r')
    counter = 0
    for line in file:
        counter +=1
    train_number = counter * 0.9



db.sentiments.delete_many({})
scores = sentiment_analysis(5)
for item in scores:
    write_scores(item,'5')

scores = sentiment_analysis(4)
for item in scores:
    write_scores(item,'4')

scores = sentiment_analysis(4)
for item in scores:
    write_scores(item,'4')

scores = sentiment_analysis(3)
for item in scores:
    write_scores(item,'3')

scores = sentiment_analysis(2)
for item in scores:
    write_scores(item,'2')

scores = sentiment_analysis(1)
for item in scores:
    write_scores(item,'1')

cursor = db.sentiments.find({'sentiments':{'stars':stars}})
for line in cursor:
    print(line['sentiments'])

##print(db.collections.find({'stars': '5'}))

print(mean_score('5'))
##print(standard_deviation(mean_values))


    

##standard_deviation_db(
##
##
##
##
##





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

