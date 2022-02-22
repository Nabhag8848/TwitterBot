import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

consumer_key = os.getenv('TWITTER_API_KEY')
consumer_secret = os.getenv('TWITTER_API_KEY_SECRET')
access_token = os.getenv('TWITTER_ACCESS_TOKEN')
access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

try:
   #  print(api.verify_credentials())
    print("Successfully logged in")
except tweepy.TweepError as e:
    print(e) 
except Exception as e:
    print(e)


def get_user_timeline():
   userTimeline = api.user_timeline()
   for tweet in userTimeline:
      print(str(tweet.id) + ' -> ' + tweet.text)


# print(tweets)
# print(tweets[0].id)
# print(tweets[0].text)
# print(tweets[0].entities)

def get_mention_timeline():
   
   tweets = api.mentions_timeline()
   for tweet in tweets:
      if '#Nabhag' in tweet.text:
         print(str(tweet.id) + ' -> ' + tweet.text)
         api.destroy_favorite(tweet.id)
         api.unretweet(tweet.id)
   



