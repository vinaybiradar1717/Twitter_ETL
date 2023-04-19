import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs


access_key = "HrVxrG1tVW0uoD8kbScMcJTuM"
access_secret = "sx83XZJjZdCqwZUBqygUdp21McmrX2f9VJ91FfZmson8Wb0g8Q"
consumer_key = "974327338442817536-giSTB9bwS887KB0A0yBZi5wfv6AJRo3"
consumer_secret = "0flKZhZHkAylYUf3KE7A1OQFt9wtfS5BBSGljqxFJxX0B"

# twitter authentication (read about this from twitter DOC)
auth = tweepy.OAuthHandler(access_key, access_secret)
auth.set_access_token(consumer_key, consumer_secret)

# create API object
api = tweepy.API(auth)

tweets = api.user_timeline(
    screen_name = '@elonmusk', #user name
    count = 200, #total tweets you want
    include_rts = False, #retweets
    tweet_mode = 'extended' #all detail
)

list = []
for tweet in tweets:
    text = tweet._json["full_text"]
    refined_tweet = {"user": tweet.user.screen_name,
                    'text' : text,
                    'favorite_count' : tweet.favorite_count,
                    'retweet_count' : tweet.retweet_count,
                    'created_at' : tweet.created_at}
    
    list.append(refined_tweet)
df = pd.DataFrame(list)
df.to_csv('refined_tweets.csv')