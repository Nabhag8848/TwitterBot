import tweepy
import os
from dotenv import load_dotenv
import time

load_dotenv()

consumer_key = os.getenv('TWITTER_API_KEY')
consumer_secret = os.getenv('TWITTER_API_KEY_SECRET')
access_token = os.getenv('TWITTER_ACCESS_TOKEN')
access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweets = api.mentions_timeline()
print(tweets[0].entities['user_mentions'][0]['screen_name'])