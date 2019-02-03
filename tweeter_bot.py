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
    id_str= ""
    screen_name= ""
    for mention in mentions:
        temp_time = datetime.strptime(str(mention.created_at), "%Y-%m-%d %H:%M:%S")

        if ((temp_time > (datetime.now() - timedelta(hours = 10))) and mention.user.geo_enabled ):
            if '#sendpizza' in mention.text.lower():
                if (count <= mention.favorited):
                    print(mention.text)
                    count = mention.favorited
                    text = mention.text
                    cord = mention.coordinates["coordinates"]
                    id_str = mention.id_str
                    screen_name = mention.user.screen_name

    return text, cord, id_str, screen_name

def reply_to_tweets(id_str):
    print('retrieving and replying to tweets...', flush=True)
    
    # NOTE: We need to use tweet_mode='extended' below to show
    # all full tweets (with full_text). Without it, long tweets
    # would be cut off.
    mentions = api.mentions_timeline(
                        id_str,
                        tweet_mode='extended')
    for mention in mentions:
        print(str(mention.id) + ' - ' + mention.full_text, flush=True)     
        if '#sendpizza' in mention.full_text.lower():
            print('found #sendpizza!', flush=True)
            print('responding back...', flush=True)
           # print(mention.user.screen_name)
            api.update_status('@' + mention.user.screen_name +
                    ' Sending a Pizza Pie to you at this moment to support the movement and cause! I hope everyone has a safe protest and fills up their stomach with delicious Dominos Pizza! Thank you'
                        + ' so much for signing up with Share-Mates!', mention.id)
