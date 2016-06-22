from textblob import TextBlob

text = "My family spent 2 nights here. From check in to check out the experience was excellent. Small hotel with great service. The front desk personnel were very friendly and helpful. While room was small (and what isn't in NYC) it was very functional, clean and neat. Had 2 double beds with 4 adults, so a little cramped but it worked just fine. Subway stop a half block away. Located in Chelsea neighborhood. Would recommend."
                                                                   
blob = TextBlob(text)
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
    
