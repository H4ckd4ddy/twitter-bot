#!/usr/bin/env python3

import os
import random
import json
import tweepy

TRIGGERS = os.environ['TRIGGERS'].split(';')
BLACKLIST = os.environ['BLACKLIST'].split(';')
RESPONSES = os.environ['RESPONSES'].split(';')

class stream_listener(tweepy.StreamListener):

    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):

        if any(trigger in tweet.user.screen_name.lower() for trigger in TRIGGERS) or any(word in tweet.user.screen_name.lower() for word in BLACKLIST):
            return

        if not any(trigger in tweet.text.lower() for trigger in TRIGGERS):
            return

        if any(word in tweet.text.lower() for word in BLACKLIST):
            return

        if tweet.retweeted or 'RT @' in tweet.text:
            return
        
        print(f"{tweet.user.screen_name}:{tweet.text}")

        response = RESPONSES[random.randrange(0, len(RESPONSES))]
        self.api.update_status(f"@{tweet.user.screen_name} {response}", tweet.id)

    def on_error(self, status):
        print("Error detected")


# Authenticate to Twitter
auth = tweepy.OAuthHandler(os.environ['CONSUMER_API'], os.environ['CONSUMER_API_SECRET'])
auth.set_access_token(os.environ['ACCES_TOKEN'], os.environ['ACCES_TOKEN_SECRET'])

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


tweets_listener = stream_listener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
stream.filter(track=TRIGGERS, languages=["fr"])

