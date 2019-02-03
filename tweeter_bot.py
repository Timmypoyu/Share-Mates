import tweepy
import time
import config
import requests
from datatime import datetime, timedelta, timezone


CONSUMER_KEY = config.consumer_key
CONSUMER_SECRET_KEY = config.consumer_secret_key
ACCESS_KEY = config.access_key
ACCESS_SECRET = config.access_secret

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def champion_tweets():
    print('finding best tweets...'. flush=True)
    mentions = api.mentions_timeline()

    count = 0
    for mention in mentions:
        temp_time = datetime.strptime(mention.created_at, "%a %b %d %H:%M:%S %z %Y") 
        
        if ((temp_time > datetime.now(timezone.utc) - timedelta(hours = 2)) and mention.user.geo_enabled ):
            if '#sendpizza' in mention.text.lower():
                if (count < mention.favorited):
                    count = mention.favorited
                    text = mention.text
                    cord = mention.coordinates.coordinates
                                
    return text, cord


text, cord = champion_tweets()
r = requests.post("http://localhost:5000/pizza", json={"text": text, "cord": cord})

if (r.status_code == 200):
    print("YEAH!")
else:
    print("OH NO!")


