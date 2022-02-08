import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('TWITTER_API_KEY')
API_SECRET = os.getenv('TWITTER_API_KEY_SECRET')
ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

twitter_oauth = tweepy.OAuthHandler(API_KEY, API_SECRET)
twitter_oauth.set_access_token(ACCESS_TOKEN, TOKEN_SECRET)

api = tweepy.API(twitter_oauth)

try:
    print(api.verify_credentials())
    print("Successfully logged in")
except tweepy.TweepError as e:
    print(e)
except Exception as e:
    print(e)

api.update_status("I can Do it!!")
