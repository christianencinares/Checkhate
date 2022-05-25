from typing import ItemsView
import tweepy, csv, sys, re
import pandas as pd
import sched, time

import config
import preprocess

# Open/create a file to append data to
csvFile = open('tweets_dataset.csv', 'a', newline='', encoding='utf-8')

#Use csv writer
csvWriter = csv.writer(csvFile)
#csvWriter.writerow(["id", "created_at", "text - utf-8", "simplified"])

# Authentication
auth = tweepy.OAuth2AppHandler(
    config.api_key, config.api_key_secret
)

# Get place ID
api         = tweepy.API(auth)
#places      = api.search_geo(query="Manila", granularity="city"); place_id = places[1].id
places      = api.search_geo(query="Philippines", granularity="country"); place_id = places[0].id
query       = "place:%s -is:retweet -has:media" % place_id
n           = 10


#statuses = api.search_tweets(q=query, count=10000)
tweets = tweepy.Cursor(api.search_tweets,q=query,tweet_mode="extended").items(n)

for tweet in tweets:
    print(tweet.id)
    print(tweet.full_text)
    print(preprocess.re_punc(tweet.full_text))
    print(preprocess.re_emoji(tweet.full_text))
    print(preprocess.simplify_text(tweet.full_text))
    
    if preprocess.simplify_text(tweet.full_text):
        csvWriter.writerow([    tweet.id_str,
                                tweet.created_at,
                                tweet.full_text.encode('utf-8'),
                                preprocess.simplify_text(tweet.full_text),
                            ])