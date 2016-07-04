#yelpPipelineClustering.py
#Charles Powell 
#Earl of Sandwich businesssId: 2e2e7WgqU1BnpxmQL5jbfw
from pymongo import MongoClient
from pprint import pprint
import nltk
import numpy as np
import matplotlib.pyplot as plt
from datetime import *
from matplotlib.dates import DateFormatter
import sklearn 
from numpy import array
from sklearn.cluster import KMeans
from matplotlib import style
import math

#Limited to this business
businessId = "2e2e7WgqU1BnpxmQL5jbfw"
howManyReviews = 3000

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
reviewsForMatrix = []

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

#Create array of list that have features of each review, [votes for cool, votes for funny, votes for useful, day of the week, stars]. For example: [3,5,1,0,5], 0 = monday 
    reviewsForMatrix.append([oneReview["votes"]["cool"], oneReview["votes"]["funny"], oneReview["votes"]["useful"],
                             datetime.strptime(tempStrip, "%Y %m %d").weekday(), oneReview["stars"]])

    
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

#Clustering
#The rule of thumb is to determine number of clusters with forumal: clusters = int(math.sqrt(howManyReviews/2)). Not used do to large data set. 
style.use("ggplot")
X = np.array(reviewsForMatrix)

#The rule of thumb is to determine number of clusters with forumal: clusters = int(math.sqrt(howManyReviews/2)). Not used due to large data set. 
kmeans = KMeans(n_clusters=4)
kmeans.fit(X)
centroids = kmeans.cluster_centers_
labels = kmeans.labels_
colors = ["g.","r.","c.","y."]

#cool/funny clustering 
for i in range(len(X)):
    plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize = 10)

plt.scatter(centroids[:, 0],centroids[:, 1], marker = "x", s=150, linewidths = 5, zorder = 10)
ax = plt.gca()
ax.set_xlabel('Cool Votes')
ax.set_ylabel('Funny Votes')
plt.show()

#Useful/Funny clustering
for i in range(len(X)):
    plt.plot(X[i][2], X[i][1], colors[labels[i]], markersize = 10)

plt.scatter(centroids[:, 2],centroids[:, 1], marker = "x", s=150, linewidths = 5, zorder = 10)
ax = plt.gca()
ax.set_xlabel('Useful Votes')
ax.set_ylabel('Funny Votes')
plt.show()

#Day of the week/stars clustering (this is ulgy) 
for i in range(len(X)):
    plt.plot(X[i][3], X[i][4], colors[labels[i]], markersize = 10)

plt.scatter(centroids[:, 3],centroids[:, 4], marker = "x", s=150, linewidths = 5, zorder = 10)
ax = plt.gca()
ax.set_xlabel('Day of the weeek (0 = Monday)')
ax.set_ylabel('Stars')
plt.show()


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
#this loop makes a list containing the correctly ordered reviews per day, the dic didnt work the way I wanted. 
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




