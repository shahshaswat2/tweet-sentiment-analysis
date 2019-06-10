# importing textblob for language processing
# importing sys module to manipulate different things
# importing tweepy library to use twitter's api

from textblob import TextBlob
import sys
import tweepy


def percentage(part, whole):
    return 100 * float(part)/float(whole)


# enter your api key for each semantics
consumerKey = "your api key"
consumerSecret = "your api key"
accessToken = "your api key"
accessTokenSecret = "your api key"

# we use OAuthHandler to call the API. Read the documentation here http://docs.tweepy.org/en/v3.5.0/auth_tutorial.html
auth = tweepy.OAuthHandler(consumer_key=consumerKey,
                           consumer_secret=consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

# we will take user input for particular keyword for sentiment analysis
searchKeyword = input("Enter your keyword or hastag to check polarity: ")
# user input to check total number of tweets
TotalSearchKeywords = int(input("Total numbers of tweet to check: "))

tweets = tweepy.Cursor(api.search, q=searchKeyword,
                       lang="English").items(TotalSearchKeywords)

# initializating
positive = 0
negative = 0
neutral = 0
polarity = 0

for tweet in tweets:
    # print(tweet.text)
    analysis = TextBlob(tweet.text)
    polarity += analysis.sentiment.polarity

    if (analysis.sentiment.polarity == 0):
        neutral += 1
    elif (analysis.sentiment.polarity < 0.00):
        negative += 1
    elif (analysis.sentiment.polarity > 0.00):
        positive += 1

positive = percentage(positive, TotalSearchKeywords)
negative = percentage(negative, TotalSearchKeywords)
neutral = percentage(neutral, TotalSearchKeywords)
polarity = percentage(polarity, TotalSearchKeywords)


positive = format(positive, '.2f')
neutral = format(neutral, '.2f')
negative = format(negative, '.2f')

print("This is how tweets for " + searchKeyword +
      " is, after going through " + str(TotalSearchKeywords) + " Tweets. ")

if (polarity == 0):
    print("Neutral")
elif (polarity < 0):
    print("Negative")
elif (polarity > 0):
    print("Positive")
