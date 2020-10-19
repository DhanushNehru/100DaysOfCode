import tweepy
import time

#Authenticate to Twitter
CONSUMER_KEY = '< your consumer key >'
CONSUMER_SECRET = '< your consumer secret key >'
ACCESS_KEY = '< your consumer access key >'
ACCESS_SECRET = '< your consumer access secret key >'

#Setting up connection
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

#Setting number of tweets & search text
user= api.me()
num_tweet = 300
search = '#100DaysOfCode'

#Searching for the tweets to like & retweet them
for tweet in tweepy.Cursor(api.search, search).items(num_tweet):
	try:
		print('Tweet Liked')
		tweet.favorite()
		
		print('Retweet done')
		tweet.retweet()
		time.sleep(15)
		
	except tweepy.TweepError as e:
		print(e.reason)
	except StopIteration:
		break