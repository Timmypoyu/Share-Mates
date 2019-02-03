import tweepy
import time
import config
import requests
from datetime import datetime, timedelta, timezone


CONSUMER_KEY = config.consumer_key
CONSUMER_SECRET_KEY = config.consumer_secret_key
ACCESS_KEY = config.access_key
ACCESS_SECRET = config.access_secret

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
                    id_str = mention.id_str
                    screen_name = mention.user.screen_name

    return text, cord, id_str, screen_name
