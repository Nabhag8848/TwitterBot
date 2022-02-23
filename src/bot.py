from all_imports import *

def get_user_timeline():
   userTimeline = api.user_timeline()
   for tweet in userTimeline:
      print(str(tweet.id) + ' -> ' + tweet.text)

FILE_NAME = 'last_seen.txt'

def read_last_id(FILE_NAME):
   file_read = open(FILE_NAME,'r')
   last_id = int(file_read.read().strip())
   file_read.close()
   return last_id

def write_last_id(FILE_NAME, last_id):
   file_write = open(FILE_NAME, 'w')
   file_write.write(str(last_id))
   file_write.close()
   return 

def reply(): 
   tweets = api.mentions_timeline(read_last_id(FILE_NAME), tweet_mode = 'extended')
   for tweet in reversed(tweets):
      if '#nabhag' in tweet.full_text.lower():
         print(str(tweet.id) + ' -> ' + tweet.full_text)
      api.update_status('You did it!!', tweet.id)
      api.create_favorite(tweet.id)
      api.retweet(tweet.id)
      write_last_id(FILE_NAME, tweet.id)
         
while(True):
   reply()
   time.sleep(2)


