import tweepy
import time
#import config
import requests
from datetime import datetime, timedelta, timezone


CONSUMER_KEY = "nFpgZnq2KPNNA4wb6JwqpT6tm"
CONSUMER_SECRET_KEY = "3ZolVazwhTdW6xRSlfl2Zsnt5VjCRgdGi6xlFTCCOMgSnjrCfW"
ACCESS_KEY = "946302291300290560-KksVRF89EN6RsO0LYqKHzYZnrBAgnbO"
ACCESS_SECRET = "EFz3IE3PA8dI5W3kkzJQOV7HZ4krHm0hllSPaalorPThO"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def champion_tweets():
    print('finding best tweets...', flush=True)
    mentions = api.mentions_timeline()

    count = 0
    text= ""
    cord= []
    for mention in mentions:
        temp_time = datetime.strptime(str(mention.created_at), "%Y-%m-%d %H:%M:%S") 
        
        if ((temp_time > (datetime.now() - timedelta(hours = 2))) and mention.user.geo_enabled ):  
            if '#sendpizza' in mention.text.lower():
               
                if (count <= mention.favorited):
                   
                    count = mention.favorited
                    text = mention.text
                    cord = mention.coordinates["coordinates"]
               
                                
    return text, cord