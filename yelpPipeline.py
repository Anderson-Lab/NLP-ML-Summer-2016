#yelpPipeline.py
#Charles Powell 
#Earl of Sandwich businesssId: 2e2e7WgqU1BnpxmQL5jbfw
from pymongo import MongoClient
from pprint import pprint
import nltk
import numpy as np
import matplotlib.pyplot as plt
from datetime import *
from matplotlib.dates import DateFormatter

#Limited to this business
businessId = "2e2e7WgqU1BnpxmQL5jbfw"
howManyReviews = 1000

#Variables for data gathered 
reviewCount = 0
starsCount = {"1" : 0, "2": 0, "3": 0, "4": 0, "5": 0}
votes = {'cool' : 0, 'funny': 0, 'useful': 0}
coolestReviewId = ""
funniestReviewId = ""
mostUsefulReviewId = ""
longestReviewTextId = ""
starsByDate = {}
reviewsPerDay = {}
averageReviewPerDay = {}
popularDays = {"0" : 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0 ,"6": 0}

#This lets pymongo about the connection we want to use, local host in our case
client = MongoClient()

#Setting context to new yelp database 
db = client.yelp

#d = db.reviews.find({text: {"$regex" : ".*earl of sandwich.*"}})
allReviews = db.reviews.find({'business_id': businessId}) 

coolestTemp = 0
funniestTemp = 0
mostUsefulTemp = 0
longestReviewTemp = 0


for oneReview in allReviews:

#how many reviews 
    reviewCount += 1

#Incrementing how many ratings have x amount of stars 
    starsCount[str(oneReview["stars"])] += 1

#Formatting for datetime object    
    tempStrip = oneReview["date"].replace("-", " ")
#If the datetime key does not already exist a key, add it with review stars( these are in a list, so len() will give
#numner of reviews for a given day.
    if datetime.strptime(tempStrip, "%Y %m %d") in starsByDate:
        starsByDate[datetime.strptime(tempStrip, "%Y %m %d")].append(oneReview["stars"])
        reviewsPerDay[datetime.strptime(tempStrip, "%Y %m %d")] += 1
    else:
        reviewsPerDay[datetime.strptime(tempStrip, "%Y %m %d")] = 1
        starsByDate.update({datetime.strptime(tempStrip, "%Y %m %d"): [oneReview["stars"]]})    

#Find longest review etc. 
    if longestReviewTemp < len(oneReview["text"]):
        longestReviewTemp = len(oneReview["text"])
        longestReviewTextId = str(oneReview['review_id'])
        longestReviewText = oneReview

    votes["cool"] += oneReview["votes"]["cool"]
    if coolestTemp < oneReview["votes"]["cool"]:
        coolestTemp = oneReview["votes"]["cool"]
        coolestReviewId = str(oneReview['review_id'])
        coolestReview = oneReview
       
    votes["funny"] += oneReview["votes"]["funny"]
    if funniestTemp < oneReview["votes"]["funny"]:
        funniestTemp = oneReview["votes"]["funny"]
        funniestReviewId = str(oneReview['review_id'])
        funniestReview = oneReview

    votes["useful"] += oneReview["votes"]["useful"]
    if mostUsefulTemp < oneReview["votes"]["useful"]:
        mostUsefulTemp = oneReview["votes"]["useful"]
        mostUsefulReviewId = str(oneReview['review_id'])
        mostUsefulReview = oneReview

    if reviewCount == howManyReviews:
        break

#popularDays, increment by day of the week review was posted. 
for k in starsByDate:
 popularDays[str(k.weekday())] += len(starsByDate[k])

#Text output

print("++++++++++++++++++++++Most Useful review++++++++++++++++++++++")
pprint(mostUsefulReview)

if mostUsefulReview != coolestReview:
    print("++++++++++++++++++++++Coolest review++++++++++++++++++++++")
    pprint(coolestReview)
else:
    print("++++++++++++++++++++++Is also coolest review++++++++++++++++++++++")

if funniestReview != coolestReview:
    print("++++++++++++++++++++++Funniest review++++++++++++++++++++++")
    pprint(funniestReview)
else:
    print("++++++++++++++++++++++Is also funniest review++++++++++++++++++++++")

print("++++++++++++++++++++++longest Review++++++++++++++++++++++")
pprint(longestReviewText)

#Taking the existing dic list data and creating stars average by day dic named starsByDateHis
totalTemp = 0
starsByDateHis = starsByDate.copy()
for dates in starsByDateHis:
    totalTemp = len(starsByDateHis[dates])
    starsByDateHis[dates] = sum(starsByDateHis[dates])/totalTemp

#Setting up x and y for matplotlib plots
lists = sorted(starsByDateHis.items())
x, y = zip(*lists)
datesHisX = np.array(x)
avgStarsHisY = np.array(y)

#Stars average over time, LINE 
plt.figure(figsize=(30, 10))
plt.title('Average Rating by Date')
x = np.array(datesHisX)
y = np.array(avgStarsHisY)
ax = plt.gca()
ax.grid(True)
line = ax.plot(datesHisX, avgStarsHisY)
plt.setp(line, linewidth=3, color='r')
ax.set_ylim(0, 5)
ax.set_xlabel('Dates')
ax.set_ylabel('Average Rating')
plt.show()

###Average Rating by Date, BAR
##plt.figure(figsize=(20, 10))
##plt.title('Average Rating by Date')
##ax = plt.gca()
##ax.grid(True)
##plt.bar(range(len(datesHisX)), avgStarsHisY, align='center')
##plt.xticks(range(howManyReviews), datesHisX, rotation=30, ha="right", fontsize=8)
##ax.set_xlabel('Dates')
##ax.set_ylabel('Average Rating')
##plt.show()

#Number of reviews with x amount of stars, BAR
plt.figure(figsize=(20, 9))
plt.title("Number of reviews with x amount of stars. (%s reviews total)" % howManyReviews )
ax = plt.gca()
ax.grid(True)
plt.bar(range(len(starsCount)), sorted(starsCount.values()), align='center')
plt.xticks(range(len(starsCount)), [1,2,3,4,5])
ax.set_xlabel('Star Rating')
ax.set_ylabel('Reviews')
plt.show()


#Number of reviews per day of the week, BAR
#this loop makes a list containing the correctly ordererd reviews per day, the dic didnt work the way I wanted. 
L = []
i = 0
for i in range(len(popularDays)):
    L.append(popularDays[str(i)])
    i += 1
    
plt.figure(figsize=(20, 9))
plt.title("Number of reviews per day of the week. (%s reviews total)" % howManyReviews )
ax = plt.gca()
ax.grid(True)
plt.bar(range(len(popularDays)), L, align='center')
plt.xticks(range(len(popularDays)), ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"], rotation=30)
ax.set_xlabel('Day of the week')
ax.set_ylabel('Reviews')
plt.show()




