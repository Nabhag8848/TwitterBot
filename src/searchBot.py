from all_imports import *

hashtag = '#100daysofcodechallenge'
tweetnumber = 10

tweets = tweepy.Cursor(api.search, hashtag).items(tweetnumber)

def searchBot():
    for tweet in tweets:
        try:
            tweet.retweet()
            api.create_favorite(tweet.id)
            api.update_status('@' + tweet.entities['user_mentions'][0]['screen_name']+' ☑️Keep Going!!! ' + tweet.entities['user_mentions'][0]['name'], tweet.id)
            if 'day' in tweet.text.lower():
                api.create_friendship(tweet.entities['user_mentions'][0]['id'])
            time.sleep(15)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(15)
while True:
    searchBot()
    time.sleep(500)
            