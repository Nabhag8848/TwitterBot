from all_imports import *

hashtag = '#100daysofcode'
tweetnumber = 10

tweets = tweepy.Cursor(api.search, hashtag).items(tweetnumber)

def searchBot():
    for tweet in tweets:
        try:
            tweet.retweet()
            api.create_favorite(tweet.id)
            api.update_status('@' + tweet.entities['user_mentions'][0]['screen_name']+' Keep Going!!!  ' + tweet.entities['user_mentions'][0]['name'], tweet.id)
            time.sleep(2)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(2)

searchBot()
            