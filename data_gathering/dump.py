"""
# Client
client  = tweepy.Client(bearer_token=config.bearer_token)

# Query
"hindi sabihin nalang totoo anong"
query   = "anong -is:retweet -has:media"
tweets  = client.search_recent_tweets(query=query, tweet_fields=[context_annotations created_at geo],
                                  place_fields=[place_type geo], expansions=geo.place_id max_results=10)

for tweet in tweets.data:
    print(tweet.data)
    csvWriter.writerow([tweet.id, tweet.created_at, tweet.text.encode('utf-8')])
"""

"""
        if preprocess.simplify_text(status.text):
            print(preprocess.translate(preprocess.simplify_text(status.text),target_lang='en'))
            csvWriter.writerow([    status.id,
                                    status.created_at,
                                    status.text.encode('utf-8'),
                                    preprocess.simplify_text(status.text),
                                    preprocess.translate(preprocess.simplify_text(status.text),target_lang='en')
                                ])
        else:
            csvWriter.writerow([    status.id,
                                    status.created_at,
                                    status.text.encode('utf-8'),
                                    preprocess.simplify_text(status.text),
                                    ""
                                ])
"""

"""
__abstractmethods__
__class__
__class_getitem__
__contains__
__delattr__
__dir__
__doc__
__eq__
__format__
__ge__
__getattr__
__getattribute__
__getitem__
__gt__
__hash__
__init__
__init_subclass__
__iter__
__le__
__len__
__lt__
__module__
__ne__
__new__
__reduce__
__reduce_ex__
__repr__
__reversed__
__setattr__
__sizeof__
__slots__
__str__
__subclasshook__
_abc_impl
attachments
author_id
context_annotations
conversation_id
created_at
data
entities
geo
get
id
in_reply_to_user_id
items
keys
lang
non_public_metrics
organic_metrics
possibly_sensitive
promoted_metrics
public_metrics
referenced_tweets
reply_settings
source
text
values
withheld
"""