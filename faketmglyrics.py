#!/usr/bin/env python
import os
import time
import os, ssl
print os.environ['cons_key']
print os.environ['cons_secret']
print os.environ['access_token']
print os.environ['access_token_secret']

from markovbot import MarkovBot
#Initialize a MarkovBot instance
tweetbot = MarkovBot()
dirname = os.path.dirname(os.path.abspath("tmg copy.text"))
# Construct the path to the book
book = os.path.join(dirname, 'tmg copy.text')
# Make your bot read the book!
tweetbot.read(book)
my_first_text = tweetbot.generate_text(25, seedword=['you', 'I am', 'going to', 'my', 'love',])
print(my_first_text)
tweetbot.twitter_login(os.environ['cons_key'], os.environ['cons_secret'], os.environ['access_token'], os.environ['access_token_secret'])
# Start periodically tweeting
#tweetbot.twitter_tweeting_start(days=0, hours=0, minutes=5 keywords=None, prefix=None, suffix=None)
tweetbot._t.statuses.update(status=my_first_text)
