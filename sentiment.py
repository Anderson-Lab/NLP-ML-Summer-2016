from textblob import TextBlob
##from nltk.classify import NaiveBayesClassifier
##from nltk.corpus import subjectivity
##from nltk.sentiment import SentimentAnalyzer
##from nltk.sentiment.util import *

text = "My family spent 2 nights here. From check in to check out the experience was excellent. Small hotel with great service. The front desk personnel were very friendly and helpful. While room was small (and what isn't in NYC) it was very functional, clean and neat. Had 2 double beds with 4 adults, so a little cramped but it worked just fine. Subway stop a half block away. Located in Chelsea neighborhood. Would recommend."

text1 = "What a wonderful hotel, an oasis amidst the bustle of New York. Nothing was too much trouble for the staff. The books are amazing, the room comfortable and the hotel is so well placed for all of the sights."                                                                

text2 = "The afternoon cheese/wine selection is great and was a great opportunity to gather the family after a days outing and plan the evening. Enjoyed the friendly staff and central location. The roof top bar is overpriced and could be so much better... otherwise great."

blob = TextBlob(text2)
blob.tags
blob.noun_phrases
total_score = 0
for sentence in blob.sentences:
    print(sentence.sentiment.polarity)
    total_score += sentence.sentiment.polarity
if total_score > 0:
	print ("Positive:", total_score)
elif total_score == 0:
	print ("The score is neutral")
else:
	print ("Negative:", total_score)
    

##n_instances = 100
##subj_docs = [(sent, 'subj') for sent in subjectivity.sents(categories='subj')[:n_instances]]
##obj_docs = [(sent, 'obj') for sent in subjectivity.sents(categories='obj')[:n_instances]]
##len(subj_docs), len(obj_docs)
##
##subj_docs[0]
